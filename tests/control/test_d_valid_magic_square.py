"""Logic Track · control · D-VAL-01, D-VAL-02, D-10."""

from control.solver import solution
from control.validator import is_magic_square, is_valid_magic_square


def test_d_val_01_g0_is_magic_square(grid_g0):
    """TestID: D-VAL-01 | Rule: R-01~05."""
    assert is_magic_square(grid_g0) is True


def test_d_val_02_tl04_not_magic_square(grid_tl04):
    """TestID: D-VAL-02 | Invariant: INV-05 | TL-04."""
    assert is_magic_square(grid_tl04) is False


def test_d_10_filled_g1_valid_magic_square(grid_g1):
    """TestID: D-10 | Rule: R-05 | Invariant: INV-05."""
    result = solution(grid_g1)
    filled = [list(row) for row in grid_g1]
    filled[result[0] - 1][result[1] - 1] = result[2]
    filled[result[3] - 1][result[4] - 1] = result[5]
    assert is_valid_magic_square(filled) is True
