"""Partial grid solver — Step A combination try (I8)."""

import copy

from entity.constants import COORD_ONE_BASE

from control.finder import find_blanks, find_not_exist_nums
from control.validator import is_magic_square

_solution_call_count = 0


def get_solution_call_count() -> int:
    return _solution_call_count


def reset_solution_call_count() -> None:
    global _solution_call_count
    _solution_call_count = 0


def _fill_grid(grid: list[list[int]], blanks: list[tuple[int, int]], n1: int, n2: int) -> list[list[int]]:
    filled = copy.deepcopy(grid)
    (r1, c1), (r2, c2) = blanks
    filled[r1 - COORD_ONE_BASE][c1 - COORD_ONE_BASE] = n1
    filled[r2 - COORD_ONE_BASE][c2 - COORD_ONE_BASE] = n2
    return filled


def solution(grid: list[list[int]]) -> list[int]:
    """Return [r1, c1, n1, r2, c2, n2] 1-index (D-SOL-01/02). Step A: forward then reverse."""
    global _solution_call_count
    _solution_call_count += 1

    blanks = find_blanks(grid)
    missing = find_not_exist_nums(grid)
    if len(blanks) != 2 or len(missing) != 2:
        raise ValueError("G1 Golden expects 2 blanks and 2 missing numbers")

    orders = (missing, [missing[1], missing[0]])
    for n1, n2 in orders:
        filled = _fill_grid(grid, blanks, n1, n2)
        if is_magic_square(filled):
            r1, c1 = blanks[0]
            r2, c2 = blanks[1]
            return [r1, c1, n1, r2, c2, n2]

    raise ValueError("No valid Step A combination")
