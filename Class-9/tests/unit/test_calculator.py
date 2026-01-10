"""Unit tests for calculator operations."""

from decimal import Decimal

import pytest

from src.calculator import add, divide, get_operation, multiply, subtract
from src.errors import ArithmeticError


class TestAddition:
    """Tests for addition operation."""

    def test_add_positive_integers(self) -> None:
        """Test addition of two positive integers."""
        assert add(Decimal(5), Decimal(3)) == Decimal(8)

    def test_add_decimals(self) -> None:
        """Test addition of decimal numbers."""
        assert add(Decimal("2.5"), Decimal("3.7")) == Decimal("6.2")

    def test_add_negative_numbers(self) -> None:
        """Test addition with negative numbers."""
        assert add(Decimal(-5), Decimal(3)) == Decimal(-2)

    def test_add_zero(self) -> None:
        """Test addition with zero."""
        assert add(Decimal(5), Decimal(0)) == Decimal(5)


class TestSubtraction:
    """Tests for subtraction operation."""

    def test_subtract_positive_integers(self) -> None:
        """Test subtraction of two positive integers."""
        assert subtract(Decimal(10), Decimal(4)) == Decimal(6)

    def test_subtract_with_negative(self) -> None:
        """Test subtraction with negative numbers."""
        assert subtract(Decimal(5), Decimal(-3)) == Decimal(8)

    def test_subtract_result_negative(self) -> None:
        """Test subtraction resulting in negative number."""
        assert subtract(Decimal(3), Decimal(5)) == Decimal(-2)


class TestMultiplication:
    """Tests for multiplication operation."""

    def test_multiply_positive_integers(self) -> None:
        """Test multiplication of two positive integers."""
        assert multiply(Decimal(7), Decimal(6)) == Decimal(42)

    def test_multiply_with_decimal(self) -> None:
        """Test multiplication with decimal numbers."""
        assert multiply(Decimal("0.5"), Decimal(4)) == Decimal(2)

    def test_multiply_negative_numbers(self) -> None:
        """Test multiplication of two negative numbers."""
        assert multiply(Decimal(-4), Decimal(-5)) == Decimal(20)

    def test_multiply_by_zero(self) -> None:
        """Test multiplication by zero."""
        assert multiply(Decimal(5), Decimal(0)) == Decimal(0)


class TestDivision:
    """Tests for division operation."""

    def test_divide_positive_integers(self) -> None:
        """Test division of two positive integers."""
        assert divide(Decimal(20), Decimal(4)) == Decimal(5)

    def test_divide_with_decimal_result(self) -> None:
        """Test division resulting in decimal."""
        result = divide(Decimal(10), Decimal(3))
        # Check that result starts with 3.33
        assert str(result).startswith("3.33")

    def test_divide_by_zero_raises_error(self) -> None:
        """Test that division by zero raises ArithmeticError."""
        with pytest.raises(ArithmeticError, match="Cannot divide by zero"):
            divide(Decimal(10), Decimal(0))

    def test_divide_zero_by_number(self) -> None:
        """Test division of zero by a number."""
        assert divide(Decimal(0), Decimal(5)) == Decimal(0)


class TestOperationRouting:
    """Tests for operation routing function."""

    def test_get_add_operation(self) -> None:
        """Test getting add operation."""
        op = get_operation("add")
        assert op(Decimal(2), Decimal(3)) == Decimal(5)

    def test_get_add_alias(self) -> None:
        """Test getting add operation via + alias."""
        op = get_operation("+")
        assert op(Decimal(2), Decimal(3)) == Decimal(5)

    def test_get_subtract_operation(self) -> None:
        """Test getting subtract operation."""
        op = get_operation("subtract")
        assert op(Decimal(10), Decimal(3)) == Decimal(7)

    def test_get_multiply_operation(self) -> None:
        """Test getting multiply operation."""
        op = get_operation("multiply")
        assert op(Decimal(4), Decimal(5)) == Decimal(20)

    def test_get_divide_operation(self) -> None:
        """Test getting divide operation."""
        op = get_operation("divide")
        assert op(Decimal(20), Decimal(4)) == Decimal(5)

    def test_unsupported_operation(self) -> None:
        """Test that unsupported operation raises ValueError."""
        with pytest.raises(ValueError, match="Unsupported operation"):
            get_operation("power")
