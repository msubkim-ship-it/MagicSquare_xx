"""Cell value range (R-03 / INV-03)."""

from entity.constants import BLANK_CELL, CELL_MAX, CELL_MIN


def is_in_range(value: int) -> bool:
    """Return True iff value is BLANK_CELL or in 1..CELL_MAX."""
    if value == BLANK_CELL:
        return True
    return CELL_MIN <= value <= CELL_MAX
