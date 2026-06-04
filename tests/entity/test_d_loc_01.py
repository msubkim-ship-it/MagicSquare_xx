"""Logic Track · entity · D-LOC-01~03 (FR-LOC-01) · G1 Golden."""

from entity.constants import BLANK_COUNT, COORD_ONE_BASE, GRID_SIZE
from entity.locator import find_blank_coords


def _row_major_index(row: int, col: int) -> int:
    return (row - COORD_ONE_BASE) * GRID_SIZE + (col - COORD_ONE_BASE)


def test_d_loc_01_blank_coords_row_major(grid_g1):
    """TestID: D-LOC-01 | Rule: R-02 | Invariant: I6 row-major | FR: FR-LOC-01."""
    # Given: G1 격자 (0이 2개)
    # When: find_blank_coords(grid_g1) 호출
    # Then: [(2,2),(3,3)] 반환 (1-index, row-major)
    assert find_blank_coords(grid_g1) == [(2, 2), (3, 3)]


def test_d_loc_02_blank_coords_count(grid_g1):
    """TestID: D-LOC-02 | Rule: R-02 | Invariant: INV-02 | G1 Golden."""
    # Given: G1 격자
    # When: find_blank_coords(grid_g1) 호출
    # Then: 빈칸 좌표 개수 == BLANK_COUNT (2)
    assert len(find_blank_coords(grid_g1)) == BLANK_COUNT


def test_d_loc_03_blank_coords_row_major_order(grid_g1):
    """TestID: D-LOC-03 | Rule: R-02 | Invariant: I6 row-major | G1 Golden."""
    # Given: G1 격자
    # When: find_blank_coords(grid_g1) 호출
    # Then: row-major 스캔 순서 (인덱스 단조 증가)
    coords = find_blank_coords(grid_g1)
    indices = [_row_major_index(r, c) for r, c in coords]
    assert indices == sorted(indices)
    assert len(indices) == BLANK_COUNT
