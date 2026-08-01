from __future__ import annotations

from importlib.metadata import version

from packaging.version import Version

_scanpy_mpl_settings = None
_scanpy_settings = None

try:
    from scanpy.plotting.legacy import _utils as _scanpy_plotting_utils
    from scanpy.plotting.legacy import mpl_settings as _scanpy_mpl_settings
    from scanpy.plotting.legacy._tools.scatterplots import _add_categorical_legend as add_categorical_legend
    from scanpy.plotting.legacy._tools.scatterplots import _panel_grid as panel_grid
    from scanpy.plotting.legacy.palettes import default_102 as default_palette
except ModuleNotFoundError as error:
    if error.name != "scanpy.plotting.legacy":
        raise
    from scanpy import settings as _scanpy_settings
    from scanpy.plotting import _utils as _scanpy_plotting_utils
    from scanpy.plotting._tools.scatterplots import _add_categorical_legend as add_categorical_legend
    from scanpy.plotting._tools.scatterplots import _panel_grid as panel_grid
    from scanpy.plotting.palettes import default_102 as default_palette

__all__ = [
    # scanpy
    "set_default_colors_for_categorical_obs",
    "add_categorical_legend",
    "panel_grid",
    "add_colors_for_categorical_sample_annotation",
    "default_palette",
    "scanpy_frameon",
    "scanpy_vector_friendly",
    # anndata
    "ArrayView",
    "SparseCSCView",
    "SparseCSRView",
]

add_colors_for_categorical_sample_annotation = _scanpy_plotting_utils.add_colors_for_categorical_sample_annotation
set_default_colors_for_categorical_obs = getattr(
    _scanpy_plotting_utils,
    "_set_default_colors_for_categorical_obs",
    None,
)
if set_default_colors_for_categorical_obs is None:
    set_default_colors_for_categorical_obs = _scanpy_plotting_utils.set_default_colors_for_categorical_obs


def scanpy_frameon() -> bool:
    if _scanpy_mpl_settings is not None:
        return _scanpy_mpl_settings.FRAMEON
    assert _scanpy_settings is not None
    return _scanpy_settings._frameon


def scanpy_vector_friendly() -> bool:
    if _scanpy_mpl_settings is not None:
        return _scanpy_mpl_settings.VECTOR_FRIENDLY
    assert _scanpy_settings is not None
    return _scanpy_settings._vector_friendly


CAN_USE_SPARSE_ARRAY = Version(version("anndata")) >= Version("0.11.0rc1")
if CAN_USE_SPARSE_ARRAY:
    from anndata._core.views import ArrayView
    from anndata._core.views import SparseCSCMatrixView as SparseCSCView
    from anndata._core.views import SparseCSRMatrixView as SparseCSRView
else:
    from anndata._core.views import ArrayView, SparseCSCView, SparseCSRView
