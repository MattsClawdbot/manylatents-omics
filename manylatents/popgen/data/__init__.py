"""Population genetics datasets."""

from .manifold_genetics import ManifoldGeneticsDataModule
from .manifold_genetics_dataset import ManifoldGeneticsDataset

__all__ = [
    "ManifoldGeneticsDataset",
    "ManifoldGeneticsDataModule",
]
