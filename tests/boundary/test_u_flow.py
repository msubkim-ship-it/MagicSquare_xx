"""UI Track · boundary · U-FLOW-01~03."""

import pytest

from boundary.errors import BoundaryValidationError
from boundary.solve_gateway import solve_partial
from control.solver import get_solution_call_count, reset_solution_call_count


def test_u_flow_01_g1_calls_control_once(grid_g1):
    """TestID: U-FLOW-01 | G1 · control solution 1회."""
    reset_solution_call_count()
    solve_partial(grid_g1)
    assert get_solution_call_count() == 1


def test_u_flow_02_none_grid_no_control_call(grid_none):
    """TestID: U-FLOW-02 | grid=None · solution 0회."""
    reset_solution_call_count()
    with pytest.raises(BoundaryValidationError):
        solve_partial(grid_none)
    assert get_solution_call_count() == 0


def test_u_flow_03_invalid_size_no_control_call(grid_3x4):
    """TestID: U-FLOW-03 | E001 · solver 미호출."""
    reset_solution_call_count()
    with pytest.raises(BoundaryValidationError):
        solve_partial(grid_3x4)
    assert get_solution_call_count() == 0
