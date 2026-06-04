"""Boundary entry to control solver (no entity direct import)."""

from boundary.input_handler import validate_grid
from control.solver import reset_solution_call_count, solution


def solve_partial(grid: list[list[int]] | None) -> list[int]:
    """Validate input then delegate to control.solution."""
    validated = validate_grid(grid)
    return solution(validated)
