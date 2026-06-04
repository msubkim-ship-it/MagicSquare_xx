import importlib.util
from pathlib import Path

import pytest

_SRC = Path(__file__).resolve().parent.parent / "src"
_constants_path = _SRC / "entity" / "constants.py"
_spec = importlib.util.spec_from_file_location("entity_constants", _constants_path)
_constants = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_constants)
BLANK_COUNT = _constants.BLANK_COUNT
BLANK_CELL = _constants.BLANK_CELL
GRID_SIZE = _constants.GRID_SIZE
MAGIC_CONSTANT = _constants.MAGIC_CONSTANT

# G1 — partial grid, blanks @ 1-index (2,2) and (3,3); missing 7, 10
_G1_ROWS = (
    (16, 3, 2, 13),
    (5, 0, 11, 8),
    (9, 6, 0, 12),
    (4, 15, 14, 1),
)

# G0 — filled 4×4 magic square (G1 + 10 @ (2,2), 7 @ (3,3))
_G0_ROWS = (
    (16, 3, 2, 13),
    (5, 10, 11, 8),
    (9, 6, 7, 12),
    (4, 15, 14, 1),
)

# TL-04 — all rows sum to MAGIC_CONSTANT; diagonals do not
_TL04_ROWS = (
    (8, 9, 10, 7),
    (7, 8, 9, 10),
    (10, 7, 8, 9),
    (9, 10, 7, 8),
)


@pytest.fixture
def grid_g1():
    grid = [list(row) for row in _G1_ROWS]
    assert len(grid) == GRID_SIZE
    assert all(len(row) == GRID_SIZE for row in grid)
    assert sum(cell == BLANK_CELL for row in grid for cell in row) == BLANK_COUNT
    return grid


@pytest.fixture
def grid_g0():
    return [list(row) for row in _G0_ROWS]


@pytest.fixture
def grid_tl04():
    return [list(row) for row in _TL04_ROWS]
