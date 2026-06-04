"""Boundary E001~E007 error types."""


class BoundaryValidationError(Exception):
    """Raised when input fails boundary validation (E001~E007)."""

    def __init__(self, code: str, label: str, message: str = "") -> None:
        self.code = code
        self.label = label
        super().__init__(message or f"{code}:{label}")
