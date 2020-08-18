from pathlib import Path
import allel
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import dask.array as da
import zarr
import gcsfs

__version__ = '0.1.0'

# helper class to load phase 3 data
# doesn't get involved with storing data
# just exists to know where files are in relation to one another.
class release_data:
    
    release_dir = None
    gcs = None
    _all_sample_sets = ["AG1000G-AO", "AG1000G-BF-A", "AG1000G-BF-B", "AG1000G-BF-C", "AG1000G-CD",
                       "AG1000G-CF", "AG1000G-CI", "AG1000G-CM-A", "AG1000G-CM-B", "AG1000G-CM-C",
                       "AG1000G-FR", "AG1000G-GA-A", "AG1000G-GH", "AG1000G-GM-A", "AG1000G-GM-B",
                       "AG1000G-GM-C", "AG1000G-GN-A", "AG1000G-GN-B", "AG1000G-GQ", "AG1000G-GW",
                       "AG1000G-KE", "AG1000G-ML-A", "AG1000G-ML-B", "AG1000G-MW", "AG1000G-MZ",
                       "AG1000G-TZ", "AG1000G-UG", "AG1000G-X"]
    
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
        return self._all_sample_sets
    
    @property
    def all_wild_sample_sets(self):
        return [x for x in self._all_sample_sets if x != "AG1000G-X"]


    def load_mask(self, seq_id, mask_id, filters_model="dt_20200416", field="filter_pass"):
    
        mask_path = self.release_dir / "site_filters" / filters_model / mask_id
        mask_store = self.gcs.get_mapper(mask_path.as_posix())
        mask_group = zarr.Group(mask_store)
        return da.from_zarr(mask_group[seq_id]["variants"][field])


    def load_crosses(self, seq_id, cross_id, field):
    
        crosses_path = self.release_dir / "site_filters" / "crosses_stats"
        crosses_store = self.gcs.get_mapper(crosses_path.as_posix())
        crosses_group = zarr.Group(crosses_store)
        return da.from_zarr(crosses_group[seq_id][field][cross_id])


    def load_variants(self, seq_id, field="POS", mask=None):
    
        """
        release_pa

        """

        path = self.release_dir / "snp_genotypes" / "all" / "sites"

        # need to open as mapping if this on cloud
        storez = self.gcs.get_mapper(path.as_posix())
        calldata = zarr.Group(storez)

        arr = da.from_zarr(calldata[f"{seq_id}/variants/{field}"])

        if mask is not None:
            
            assert isinstance(mask, da.core.Array), "mask must be a dask_array"
            arr = da.compress(mask, arr, axis=0).compute_chunk_sizes()

        return arr


    def load_sample_set_calldata(self, seq_id, sample_set, field="GT", mask=None):
    
        if isinstance(sample_set, str):

            path = self.release_dir / "snp_genotypes" / "all" / sample_set

            # need to open as mapping if this on cloud
            storez = self.gcs.get_mapper(path.as_posix())
            calldata = zarr.Group(storez)

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

            metadata_path = self.release_dir / "metadata" / "general" / sample_set / "samples.meta.csv"
            with self.gcs.open(metadata_path) as gcs_fh:
                df = pd.read_csv(gcs_fh, index_col=0)
                df["sample_set"] = sample_set

            if include_aim_species_calls:
                species_path_aim = self.release_dir / "metadata" / species_analysis / sample_set / "samples.species_aim.csv"
                with self.gcs.open(species_path_aim) as gcs_fh:
                    df_aim = pd.read_csv(gcs_fh, index_col=0)

            if include_pca_species_calls:
                species_path_pca = self.release_dir / "metadata" / species_analysis / sample_set / "samples.species_pca.csv"
                with self.gcs.open(species_path_pca) as gcs_fh:
                    df_pca = pd.read_csv(gcs_fh, index_col=0)

            if include_aim_species_calls and include_pca_species_calls:
                df_species = df_aim.join(df_pca, lsuffix='_aim', rsuffix='_pca')
                df = pd.concat([df, df_species], axis=1, sort=False)
                convenience_species_assignment = False
                print("Setting `convenience_species_assignment` to False. Using both PCA/AIM creates ambiguity.")
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
    
    def __init__(self, genome, *args, **kwargs):
        self.chromosomes = kwargs.pop('chromosomes', ['2R', '2L', '3R', '3L', 'X', 'UNKN'])
        maxchrsize = max(genome[chrom] for chrom in self.chromosomes)
        fig = plt.figure(*args, **kwargs)
        self.fig = fig
        self.ax = dict()
        for i, chrom in enumerate(self.chromosomes):
            ax = fig.add_subplot(3, 2, i+1)
            self.ax[chrom] = ax
            S = np.arange(1, genome[chrom], 1, dtype=np.int64)
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
