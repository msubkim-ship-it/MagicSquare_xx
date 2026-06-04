"""Logic Track · control · D-SOL-01, D-SOL-02."""

from control.solver import solution


def test_d_sol_01_step_a_success(grid_g1):
    """TestID: D-SOL-01 | Invariant: I8."""
    result = solution(grid_g1)
    assert len(result) == 6


def test_d_sol_02_g1_solution_int6(grid_g1):
    """TestID: D-SOL-02 | Invariant: I6, I8."""
    assert solution(grid_g1) == [2, 2, 10, 3, 3, 7]
