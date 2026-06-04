import pytest

_GRID_3X4 = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
)

_GRID_ONE_BLANK = (
    (16, 3, 2, 13),
    (5, 10, 11, 8),
    (9, 6, 7, 12),
    (4, 15, 14, 0),
)


@pytest.fixture
def grid_3x4():
    return [list(row) for row in _GRID_3X4]


@pytest.fixture
def grid_one_blank():
    return [list(row) for row in _GRID_ONE_BLANK]
