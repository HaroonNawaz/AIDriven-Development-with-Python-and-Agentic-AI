"""Core calculator arithmetic operations."""

from decimal import Decimal
from typing import Callable

from src.errors import ArithmeticError  # pylint: disable=redefined-builtin


def add(operand1: Decimal, operand2: Decimal) -> Decimal:
    """Add two numbers.

    Args:
        operand1: First numeric operand
        operand2: Second numeric operand

    Returns:
        Sum of operand1 and operand2
    """
    return operand1 + operand2


def subtract(operand1: Decimal, operand2: Decimal) -> Decimal:
    """Subtract two numbers.

    Args:
        operand1: First numeric operand
        operand2: Second numeric operand

    Returns:
        Difference of operand1 minus operand2
    """
    return operand1 - operand2


def multiply(operand1: Decimal, operand2: Decimal) -> Decimal:
    """Multiply two numbers.

    Args:
        operand1: First numeric operand
        operand2: Second numeric operand

    Returns:
        Product of operand1 and operand2
    """
    return operand1 * operand2


def divide(operand1: Decimal, operand2: Decimal) -> Decimal:
    """Divide two numbers.

    Args:
        operand1: First numeric operand (dividend)
        operand2: Second numeric operand (divisor)

    Returns:
        Quotient of operand1 divided by operand2

    Raises:
        ArithmeticError: If operand2 (divisor) is zero
    """
    if operand2 == 0:
        raise ArithmeticError("Cannot divide by zero")
    return operand1 / operand2


def get_operation(
    operation_name: str,
) -> Callable[[Decimal, Decimal], Decimal]:
    """Get the operation function by name.

    Args:
        operation_name: Name or alias of operation
            (add, +, subtract, -, multiply, *, divide, /)

    Returns:
        The corresponding operation function

    Raises:
        ValueError: If operation is not supported
    """
    operations = {
        "add": add,
        "+": add,
        "subtract": subtract,
        "-": subtract,
        "multiply": multiply,
        "*": multiply,
        "divide": divide,
        "/": divide,
    }

    if operation_name not in operations:
        raise ValueError(f"Unsupported operation: {operation_name}")

    return operations[operation_name]
