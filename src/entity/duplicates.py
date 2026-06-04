"""Non-zero duplicate detection (R-03 / INV-03)."""

from entity.constants import BLANK_CELL


def has_duplicate_nonzero(grid: list[list[int]]) -> bool:
    """Return True if any non-blank value appears more than once."""
    seen: set[int] = set()
    for row in grid:
        for value in row:
            if value == BLANK_CELL:
                continue
            if value in seen:
                return True
            seen.add(value)
    return False
