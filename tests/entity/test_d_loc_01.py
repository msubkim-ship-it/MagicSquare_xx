"""Logic Track · entity · D-LOC-01 (FR-LOC-01)."""

from entity.locator import find_blank_coords


def test_d_loc_01_blank_coords_row_major(grid_g1):
    """TestID: D-LOC-01 | Rule: R-02 | Invariant: I6 row-major | FR: FR-LOC-01."""
    # Given: G1 격자 (0이 2개)
    # When: find_blank_coords(grid_g1) 호출
    # Then: [(2,2),(3,3)] 반환 (1-index, row-major)
    assert find_blank_coords(grid_g1) == [(2, 2), (3, 3)]
