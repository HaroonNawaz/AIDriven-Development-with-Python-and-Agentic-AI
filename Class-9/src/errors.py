"""Exception classes for calculator operations."""


class CalculatorError(Exception):
    """Base exception for calculator errors."""


class ArithmeticError(CalculatorError):  # pylint: disable=redefined-builtin
    """Exception raised for arithmetic operation errors."""


class ValidationError(CalculatorError):
    """Exception raised for input validation errors."""
