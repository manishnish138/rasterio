"""rasterio.vrt: a module concerned with GDAL VRTs"""

from rasterio._warp import WarpedVRTReaderBase
from rasterio.enums import Resampling
from rasterio.env import ensure_env
from rasterio.io import WindowMethodsMixin, TransformMethodsMixin


class WarpedVRT(WarpedVRTReaderBase, WindowMethodsMixin,
                TransformMethodsMixin):
    """Creates a virtual warped dataset.

    Abstracts the details of raster warping and allows access to data
    that is reprojected when read.

    This class is backed by an in-memory GDAL VRTWarpedDataset VRT file.

    Attributes
    ----------

    src_dataset : dataset
        The dataset object that is virtually warped.
    dst_crs : CRS or str
        The warp operation's destination coordinate reference system.
    resampling : int
        One of the values from rasterio.enums.Resampling. The default is
        `Resampling.nearest`.
    tolerance : float
        The maximum error tolerance in input pixels when approximating
        the warp transformation. The default is 0.125.
    src_nodata : float, int, or None
        The nodata value for the source dataset.
    dst_nodata : float, int, or None
        The nodata value for the virtually warped dataset.
    warp_extras : dict
        GDAL extra warp options.

    Example
    -------

    >>> with rasterio.open('tests/data/RGB.byte.tif') as src:
    ...     with WarpedVRT(src, dst_crs='EPSG:3857') as vrt:
    ...         data = vrt.read()

    """

    def __repr__(self):
        return "<{} WarpedVRTReader name='{}' mode='{}'>".format(
            self.closed and 'closed' or 'open', self.name, self.mode)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args, **kwargs):
        self.stop()
