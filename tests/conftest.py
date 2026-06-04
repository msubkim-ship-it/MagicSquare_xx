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
GRID_SIZE = _constants.GRID_SIZE

# G1 — partial grid, blanks @ 1-index (2,2) and (3,3); missing 7, 10
_G1_ROWS = (
    (16, 3, 2, 13),
    (5, 0, 11, 8),
    (9, 6, 0, 12),
    (4, 15, 14, 1),
)


@pytest.fixture
def grid_g1():
    grid = [list(row) for row in _G1_ROWS]
    assert len(grid) == GRID_SIZE
    assert all(len(row) == GRID_SIZE for row in grid)
    assert sum(cell == 0 for row in grid for cell in row) == BLANK_COUNT
    return grid
