"""Magic square validation (R-05)."""

from entity.constants import MAGIC_CONSTANT

from control.line_sums import sum_lines


def is_magic_square(grid: list[list[int]]) -> bool:
    """True iff all 10 line sums equal MAGIC_CONSTANT."""
    return all(total == MAGIC_CONSTANT for total in sum_lines(grid))


def is_valid_magic_square(grid: list[list[int]]) -> bool:
    """Filled grid passes 10-line check (D-10)."""
    return is_magic_square(grid)
