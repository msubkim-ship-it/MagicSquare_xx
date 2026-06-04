"""Logic Track · control · D-07."""

from control.finder import find_blanks


def test_d_07_g1_blank_coords_row_major(grid_g1):
    """TestID: D-07 | Rule: R-02 | Invariant: I6."""
    assert find_blanks(grid_g1) == [(2, 2), (3, 3)]
