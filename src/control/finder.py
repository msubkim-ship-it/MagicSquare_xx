"""Blank coords and missing numbers (S-02, I7)."""

from entity.constants import BLANK_CELL, CELL_MAX, CELL_MIN
from entity.locator import find_blank_coords


def find_blanks(grid: list[list[int]]) -> list[tuple[int, int]]:
    """1-index blank coordinates, row-major (D-07)."""
    return find_blank_coords(grid)


def find_not_exist_nums(grid: list[list[int]]) -> list[int]:
    """Missing values from 1..16 not present as non-blank, ascending."""
    present = {value for row in grid for value in row if value != BLANK_CELL}
    return [n for n in range(CELL_MIN, CELL_MAX + 1) if n not in present]
