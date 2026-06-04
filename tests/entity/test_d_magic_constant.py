"""Logic Track · entity · D-05."""

from entity.constants import CELL_MAX, GRID_SIZE
from entity.magic_constant import MagicConstant


def test_d_05_magic_constant_derived():
    """TestID: D-05 | Rule: R-04 | Invariant: INV-04."""
    expected = sum(range(1, CELL_MAX + 1)) // GRID_SIZE
    assert MagicConstant().value == expected
