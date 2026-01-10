"""Tests for error handling."""

import pytest

from src.errors import ArithmeticError, CalculatorError, ValidationError


class TestExceptions:
    """Tests for exception classes."""

    def test_arithmetic_error_is_calculator_error(self) -> None:
        """Test that ArithmeticError inherits from CalculatorError."""
        error = ArithmeticError("Test")
        assert isinstance(error, CalculatorError)

    def test_validation_error_is_calculator_error(self) -> None:
        """Test that ValidationError inherits from CalculatorError."""
        error = ValidationError("Test")
        assert isinstance(error, CalculatorError)

    def test_arithmetic_error_message(self) -> None:
        """Test ArithmeticError message."""
        error = ArithmeticError("Cannot divide by zero")
        assert str(error) == "Cannot divide by zero"

    def test_validation_error_message(self) -> None:
        """Test ValidationError message."""
        error = ValidationError("Invalid input")
        assert str(error) == "Invalid input"
