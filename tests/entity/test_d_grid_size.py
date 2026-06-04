"""Logic Track · entity · D-01."""

from entity.grid_size import is_valid_grid_size


def test_d_01_grid_3x4_invalid_size(grid_3x4):
    """TestID: D-01 | Rule: R-01 | Invariant: INV-01."""
    assert is_valid_grid_size(grid_3x4) is False
