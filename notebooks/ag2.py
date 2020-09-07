from pathlib import Path
import dask.array as da
import zarr
import gcsfs

__version__ = '0.1.0'

# helper class to load phase 2 data
class release_data:
    
    release_dir = None
    gcs = None

    def __init__(self, release_path=Path("ag1000g-release/phase2.AR1"), gcs_filesystem=gcsfs.GCSFileSystem()):
        
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

    def load_is_accessible(self, seq_id):

        path = self.release_dir / "accessibility" / "accessibility.zarr"
        storez = self.gcs.get_mapper(path.as_posix())
        zarrdata = zarr.Group(storez)
        return da.from_zarr(zarrdata[f"{seq_id}/is_accessible"])


    def load_filter_n(self, seq_id):

        path = self.release_dir / "accessibility" / "accessibility.zarr"
        storez = self.gcs.get_mapper(path.as_posix())
        zarrdata = zarr.Group(storez)
        return da.from_zarr(zarrdata[f"{seq_id}/filter_n"])