"""Input validation — E001~E005 at boundary (R-06 order)."""

from boundary.constants import (
    BLANK_CELL,
    BLANK_COUNT,
    CELL_MAX,
    CELL_MIN,
    GRID_SIZE,
)
from boundary.errors import BoundaryValidationError


def _blank_count(grid: list[list[int]]) -> int:
    return sum(1 for row in grid for cell in row if cell == BLANK_CELL)


def _has_duplicate_nonzero(grid: list[list[int]]) -> bool:
    seen: set[int] = set()
    for row in grid:
        for value in row:
            if value == BLANK_CELL:
                continue
            if value in seen:
                return True
            seen.add(value)
    return False


def validate_grid(grid: list[list[int]] | None) -> list[list[int]]:
    """Validate grid; raise BoundaryValidationError on contract violation."""
    if grid is None:
        raise BoundaryValidationError("E003", "INVALID_NULL")

    if isinstance(grid, str):
        raise BoundaryValidationError("E005", "INVALID_TYPE")

    if not isinstance(grid, list) or len(grid) != GRID_SIZE:
        raise BoundaryValidationError("E001", "INVALID_SIZE")

    for row in grid:
        if not isinstance(row, list) or len(row) != GRID_SIZE:
            raise BoundaryValidationError("E001", "INVALID_SIZE")

    if _blank_count(grid) != BLANK_COUNT:
        raise BoundaryValidationError("E002", "INVALID_BLANKS")

    for row in grid:
        for value in row:
            if value != BLANK_CELL and not (CELL_MIN <= value <= CELL_MAX):
                raise BoundaryValidationError("E003", "INVALID_RANGE")

    if _has_duplicate_nonzero(grid):
        raise BoundaryValidationError("E004", "INVALID_DUPLICATE")

    return grid
