"""Logic Track · entity · D-02."""

from entity.blank_count import count_blanks


def test_d_02_one_blank_count(grid_one_blank):
    """TestID: D-02 | Rule: R-02 | Invariant: INV-02."""
    assert count_blanks(grid_one_blank) == 1
