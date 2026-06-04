"""Boundary layer — E001~E007, I/O (no entity direct import)."""

from boundary.errors import BoundaryValidationError
from boundary.input_handler import validate_grid
from boundary.solve_gateway import solve_partial

__all__ = ["BoundaryValidationError", "solve_partial", "validate_grid"]
