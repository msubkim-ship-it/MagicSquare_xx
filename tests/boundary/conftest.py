"""Boundary Track fixtures — U-IN-* (no entity import)."""

import pytest

# TL-01 — 3×4 격자 (R-01 FAIL → E001)
_GRID_3X4_ROWS = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
)


@pytest.fixture
def grid_none():
    """U-IN-01 — null grid."""
    return None


@pytest.fixture
def grid_3x4():
    """U-IN-02 / TL-01 — 3 rows × 4 cols (invalid size)."""
    return [list(row) for row in _GRID_3X4_ROWS]


_GRID_ZERO_BLANKS = (
    (16, 3, 2, 13),
    (5, 10, 11, 8),
    (9, 6, 7, 12),
    (4, 15, 14, 1),
)

_GRID_ONE_BLANK = (
    (16, 3, 2, 13),
    (5, 10, 11, 8),
    (9, 6, 7, 12),
    (4, 15, 14, 0),
)

_GRID_DUPLICATE = (
    (16, 3, 2, 13),
    (5, 0, 11, 8),
    (9, 6, 0, 12),
    (4, 15, 14, 14),
)


@pytest.fixture
def grid_zero_blanks():
    """U-IN-03 — no blank cells."""
    return [list(row) for row in _GRID_ZERO_BLANKS]


@pytest.fixture
def grid_one_blank():
    """U-IN-04 / TL-02 — one blank."""
    return [list(row) for row in _GRID_ONE_BLANK]


@pytest.fixture
def grid_with_17():
    """U-IN-05 — value 17 out of range."""
    return [
        [16, 3, 2, 13],
        [5, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 15, 14, 17],
    ]


@pytest.fixture
def grid_duplicate():
    """U-IN-06 / TL-03 — duplicate non-zero."""
    return [list(row) for row in _GRID_DUPLICATE]


@pytest.fixture
def grid_invalid_type():
    """U-IN-07 — wrong type."""
    return "not-a-grid"
