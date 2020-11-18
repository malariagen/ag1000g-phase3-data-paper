from pathlib import Path
import allel
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import dask.array as da
import zarr
import gcsfs
import yaml
from warnings import warn
import intake

__version__ = '0.1.1'


# helper class to load phase 3 data
# doesn't get involved with storing data
# just exists to know where files are in relation to one another.
class release_data:
    
    release_dir = None
    gcs = None
    _data_catalog = intake.open_catalog("https://malariagen.github.io/intake/gcs.yml")
    _all_sample_sets = _data_catalog.ag3.sample_sets.read()['sample_set'].tolist()
    _location_colours = None
    try:
        with open('location_colours.yaml') as file:
            _location_colours = yaml.load(file, Loader=yaml.Loader)
    except FileNotFoundError as e:
        warn(e)
    
    
    def __init__(self, release_path=Path("vo_agam_release/v3"), gcs_filesystem=gcsfs.GCSFileSystem()):
        
        # input checking
        if isinstance(release_path, str):
            release_path = Path(release_path)
        elif isinstance(release_path, Path):
            pass
        else:
            raise ValueError("`release_path` expects a string or pathlib.Path object")
        
        assert isinstance(gcs_filesystem, gcsfs.GCSFileSystem), "`gcs_filesystem` must be a gcsfs.GCSFileSystem object"
        
        self.release_dir = release_path
        self.gcs = gcs_filesystem
    
    @property
    def all_sample_sets(self):
        return self.__class__._all_sample_sets
    
    @property
    def all_wild_sample_sets(self):
        return [x for x in self.all_sample_sets if x != "AG1000G-X"]
    
    @property
    def location_colours(self):
        return self.__class__._location_colours
    
    
    def load_mask(self, seq_id, mask_id, filters_model="dt_20200416", field="filter_pass"):
        
        mask_group = self.__class__._data_catalog.ag3[f'site_filters_{filters_model}_{mask_id}'].to_zarr()
        return da.from_zarr(mask_group[seq_id]["variants"][field])
    
    
    def load_crosses(self, seq_id, cross_id, field):
        
        # Not available via intake 22 Oct 2020
        
        crosses_path = self.release_dir / "site_filters" / "crosses_stats"
        crosses_store = self.gcs.get_mapper(crosses_path.as_posix())
        crosses_group = zarr.Group(crosses_store)
        return da.from_zarr(crosses_group[seq_id][field][cross_id])
    
    
    def load_variants(self, seq_id, field="POS", mask=None):

        calldata = self.__class__._data_catalog.ag3.snp_sites.to_zarr()
        arr = da.from_zarr(calldata[f"{seq_id}/variants/{field}"])

        if mask is not None:
            
            assert isinstance(mask, da.core.Array), "mask must be a dask_array"
            arr = da.compress(mask, arr, axis=0).compute_chunk_sizes()

        return arr
    
    
    def load_sample_set_calldata(self, seq_id, sample_set, field="GT", mask=None):

        if isinstance(sample_set, str):

            calldata = self.__class__._data_catalog.ag3.snp_genotypes(sample_set=sample_set).to_zarr()
            arr = da.from_zarr(calldata[f"{seq_id}/calldata/{field}"])
            
        elif isinstance(sample_set, list):
            arr = da.concatenate(
                [self.load_sample_set_calldata(seq_id, s, field=field, mask=None) for s in sample_set], axis=1)
        else:
            raise ValueError("sample_set must be a string, or a list of strings")

        if mask is not None:

            assert isinstance(mask, da.core.Array), "mask must be a dask_array"

            arr = da.compress(mask, arr, axis=0).compute_chunk_sizes()

        return arr
    
    
    def load_sample_set_metadata(
        self, sample_set, include_aim_species_calls=True, include_pca_species_calls=False, species_analysis="species_calls_20200422",
        convenience_species_assignment=True):

        if isinstance(sample_set, str):

            df = self.__class__._data_catalog.ag3.samples(sample_set=sample_set).read().set_index('sample_id')
            df["sample_set"] = sample_set
            
            if include_aim_species_calls:
                df_aim = self.__class__._data_catalog.ag3[f'{species_analysis}_aim'](sample_set=sample_set).read().set_index('sample_id')

            if include_pca_species_calls:
                df_pca = self.__class__._data_catalog.ag3[f'{species_analysis}_pca'](sample_set=sample_set).read().set_index('sample_id')

            if include_aim_species_calls and include_pca_species_calls:
                df_species = df_aim.join(df_pca, lsuffix='_aim', rsuffix='_pca')
                df = pd.concat([df, df_species], axis=1, sort=False)
                convenience_species_assignment = False
                warn("Setting `convenience_species_assignment` to False. Using both PCA/AIM creates ambiguity.")
            elif include_aim_species_calls:
                df = pd.concat([df, df_aim], axis=1, sort=False)
            elif include_pca_species_calls:
                df = pd.concat([df, df_pca], axis=1, sort=False)
            else:
                convenience_species_assignment = False
                
            # only makes sense if exactly one of the include_species_call_x variables is true.
            if convenience_species_assignment:
                df["is_arabiensis"] = df.species_gambcolu_arabiensis == "arabiensis"
                df["is_gamb_colu"] = df.species_gambcolu_arabiensis == "gamb_colu"
                df["is_gambiae"] = df.species_gambiae_coluzzii == "gambiae"
                df["is_coluzzii"] = df.species_gambiae_coluzzii == "coluzzii"

            return df
        
        elif isinstance(sample_set, list):
            
            return pd.concat(
                [self.load_sample_set_metadata(s, include_aim_species_calls, include_pca_species_calls) for s in sample_set],
                axis=0, sort=False)


class GenomeFigure(object):
    
    """
    NB: the genome object contains set of keys where the len() function must work on each 
    for a zarr version that works on cloud, see: https://nbviewer.jupyter.org/gist/alimanfoo/5b3e86966ac02787723df28c53c19334
    else a pyfaidx object works on local.
    """
    
    
    
    def __init__(self, genome, *args, **kwargs):
        self.chromosomes = kwargs.pop('chromosomes', ['2R', '2L', '3R', '3L', 'X', 'UNKN'])
        maxchrsize = max(len(genome[chrom]) for chrom in self.chromosomes)
        fig = plt.figure(*args, **kwargs)
        self.fig = fig
        self.ax = dict()
        for i, chrom in enumerate(self.chromosomes):
            ax = fig.add_subplot(3, 2, i+1)
            self.ax[chrom] = ax
            S = np.arange(1, len(genome[chrom]), 1, dtype=np.int64)
            if i % 2 == 1:
                sns.despine(ax=ax, offset=10, top=True, left=True, right=False)
                ax.set_xlim(0, maxchrsize)
                ax.yaxis.tick_right()
                ax.yaxis.set_label_position('right')
            else:
                ax.set_xlim((S.size)-(maxchrsize), S.size)
                ax.yaxis.tick_left()
                sns.despine(ax=ax, offset=10, top=True, left=False, right=True)
            ax.set_xticks(range(0, S.size, int(5e6)))
            ax.set_xticklabels(range(0, int(S.size/1e6), 5))
            ax.set_title(chrom, fontweight='bold')
            ax.xaxis.tick_bottom()
        fig.tight_layout()
        
    def apply(self, f, **kwargs):
        chromosomes = kwargs.pop('chromosomes', self.chromosomes)
        for chrom in chromosomes:
            ax = self.ax[chrom]
            f(chrom, ax, **kwargs)
        
        
def subplots(*args, **kwargs):
    fig, ax = plt.subplots(*args, **kwargs)
    sns.despine(ax=ax, offset=10)
    return fig, ax
