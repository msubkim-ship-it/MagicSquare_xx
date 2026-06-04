"""Logic Track · control · D-MIS-01."""

from control.finder import find_not_exist_nums


def test_d_mis_01_g1_missing_sorted(grid_g1):
    """TestID: D-MIS-01 | Invariant: I7, I11."""
    assert find_not_exist_nums(grid_g1) == [7, 10]
