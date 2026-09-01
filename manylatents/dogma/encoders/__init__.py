"""Central dogma foundation model encoders.

Provides encoders for the three levels of the central dogma:
    - Evo2Encoder: DNA sequences (nucleotides)
    - OrthrusEncoder: RNA sequences (uses mamba-ssm 2.x)
    - ESM3Encoder: Protein sequences (amino acids)
    - AlphaGenomeEncoder: DNA sequences with regulatory predictions (JAX-based)

Note: These are direct imports. The encoders themselves do lazy model loading
in their _load_model() methods, so importing the class is lightweight - only
the actual model weights are loaded when encode() is first called.
"""

from manylatents.algorithms.latent.foundation_encoder import FoundationEncoder

from .alphagenome import AlphaGenomeEncoder
from .esm import ESMEncoder
from .esm3 import ESM3Encoder
from .evo2 import Evo2Encoder
from .orthrus_native import OrthrusNativeEncoder as OrthrusEncoder

__all__ = ["FoundationEncoder", "Evo2Encoder", "OrthrusEncoder", "ESM3Encoder", "ESMEncoder", "AlphaGenomeEncoder"]
