"""UI Track · boundary · U-IN-01~02 (입력 검증)."""

import pytest

from boundary.errors import BoundaryValidationError
from boundary.input_handler import validate_grid


def test_u_in_01_none_grid_raises_e003(grid_none):
    """TestID: U-IN-01 | Rule: R-06 | E003 / INVALID_NULL."""
    # Given: grid is None
    # When: validate_grid(None)
    # Then: E003 INVALID_NULL
    with pytest.raises(BoundaryValidationError) as exc_info:
        validate_grid(grid_none)

    err = exc_info.value
    assert err.code == "E003"
    assert err.label == "INVALID_NULL"


def test_u_in_02_grid_3x4_raises_e001(grid_3x4):
    """TestID: U-IN-02 | Rule: R-01 / TL-01 | E001 / INVALID_SIZE."""
    # Given: 3×4 격자 (TL-01)
    # When: validate_grid(3×4)
    # Then: E001 INVALID_SIZE
    with pytest.raises(BoundaryValidationError) as exc_info:
        validate_grid(grid_3x4)

    err = exc_info.value
    assert err.code == "E001"
    assert err.label == "INVALID_SIZE"


def test_u_in_03_zero_blanks_raises_e002(grid_zero_blanks):
    """TestID: U-IN-03 | Rule: R-02 | E002 / INVALID_BLANKS."""
    with pytest.raises(BoundaryValidationError) as exc_info:
        validate_grid(grid_zero_blanks)
    assert exc_info.value.code == "E002"
    assert exc_info.value.label == "INVALID_BLANKS"


def test_u_in_04_one_blank_raises_e002(grid_one_blank):
    """TestID: U-IN-04 | Rule: R-02 | TL-02 | E002."""
    with pytest.raises(BoundaryValidationError) as exc_info:
        validate_grid(grid_one_blank)
    assert exc_info.value.code == "E002"


def test_u_in_05_value_17_raises_e003(grid_with_17):
    """TestID: U-IN-05 | Rule: R-03 | E003 / INVALID_RANGE."""
    with pytest.raises(BoundaryValidationError) as exc_info:
        validate_grid(grid_with_17)
    assert exc_info.value.code == "E003"
    assert exc_info.value.label == "INVALID_RANGE"


def test_u_in_06_duplicate_raises_e004(grid_duplicate):
    """TestID: U-IN-06 | Rule: R-03 | TL-03 | E004."""
    with pytest.raises(BoundaryValidationError) as exc_info:
        validate_grid(grid_duplicate)
    assert exc_info.value.code == "E004"
    assert exc_info.value.label == "INVALID_DUPLICATE"


def test_u_in_07_invalid_type_raises_e005(grid_invalid_type):
    """TestID: U-IN-07 | E005 / INVALID_TYPE."""
    with pytest.raises(BoundaryValidationError) as exc_info:
        validate_grid(grid_invalid_type)
    assert exc_info.value.code == "E005"
    assert exc_info.value.label == "INVALID_TYPE"
