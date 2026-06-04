"""Logic Track · entity · D-03."""

from entity.cell_range import is_in_range


def test_d_03_value_17_out_of_range():
    """TestID: D-03 | Rule: R-03 | Invariant: INV-03."""
    assert is_in_range(17) is False
