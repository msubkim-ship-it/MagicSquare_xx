"""Logic Track · entity · D-04."""

from entity.duplicates import has_duplicate_nonzero


def test_d_04_duplicate_nonzero_detected():
    """TestID: D-04 | Rule: R-03 | Invariant: INV-03."""
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 15],
    ]
    assert has_duplicate_nonzero(grid) is True
