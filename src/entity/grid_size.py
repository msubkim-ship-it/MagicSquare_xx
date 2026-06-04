"""Grid dimensions (R-01 / INV-01)."""

from entity.constants import GRID_SIZE


def is_valid_grid_size(grid: list[list[int]]) -> bool:
    """Return True iff grid is 4×4."""
    if not isinstance(grid, list) or len(grid) != GRID_SIZE:
        return False
    return all(isinstance(row, list) and len(row) == GRID_SIZE for row in grid)
