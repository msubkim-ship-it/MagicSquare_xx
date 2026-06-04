"""Control layer — orchestrates entity domain (no boundary import)."""

from control.finder import find_blanks, find_not_exist_nums
from control.line_sums import sum_lines
from control.solver import solution
from control.validator import is_magic_square, is_valid_magic_square

__all__ = [
    "find_blanks",
    "find_not_exist_nums",
    "is_magic_square",
    "is_valid_magic_square",
    "solution",
    "sum_lines",
]
