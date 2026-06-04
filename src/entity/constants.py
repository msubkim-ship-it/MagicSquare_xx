"""Domain constants (SSOT). R-04: no literal 34/16/4 in tests beyond this module."""

GRID_SIZE = 4
BLANK_COUNT = 2
BLANK_CELL = 0
COORD_ONE_BASE = 1
CELL_MAX = GRID_SIZE * GRID_SIZE
_MAGIC_SUM = sum(range(1, CELL_MAX + 1))
MAGIC_CONSTANT = _MAGIC_SUM // GRID_SIZE
