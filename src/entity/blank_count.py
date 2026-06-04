"""Blank cell count (R-02 / INV-02)."""

from entity.constants import BLANK_CELL


def count_blanks(grid: list[list[int]]) -> int:
    """Count cells equal to BLANK_CELL."""
    return sum(1 for row in grid for cell in row if cell == BLANK_CELL)
