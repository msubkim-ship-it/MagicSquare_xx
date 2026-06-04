"""Logic Track · control · D-06, D-06b."""

from entity.constants import MAGIC_CONSTANT

from control.line_sums import sum_lines


def test_d_06_g0_line_sums_equal_magic_constant(grid_g0):
    """TestID: D-06 | Rule: R-05 | Invariant: INV-05."""
    assert all(s == MAGIC_CONSTANT for s in sum_lines(grid_g0))


def test_d_06b_tl04_diagonal_fails(grid_tl04):
    """TestID: D-06b | Rule: R-05 | TL-04."""
    sums = sum_lines(grid_tl04)
    assert all(s == MAGIC_CONSTANT for s in sums[:4])
    assert sums[8] != MAGIC_CONSTANT or sums[9] != MAGIC_CONSTANT
