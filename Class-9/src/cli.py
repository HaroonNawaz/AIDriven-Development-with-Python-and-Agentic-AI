"""Command-line interface for the calculator."""

import argparse
import sys
from decimal import Decimal, InvalidOperation

from src.calculator import get_operation
from src.errors import (  # pylint: disable=redefined-builtin
    ArithmeticError,
    CalculatorError,
    ValidationError,
)


def main() -> int:
    """Main entry point for the calculator CLI.

    Returns:
        Exit code: 0 on success, 1 on validation error, 2 on arithmetic error
    """
    parser = argparse.ArgumentParser(
        description="Basic CLI calculator supporting add, subtract, multiply, divide"
    )
    parser.add_argument(
        "operation",
        help="Arithmetic operation: add (+), subtract (-), multiply (*), divide (/)",
    )
    parser.add_argument("operand1", help="First numeric operand")
    parser.add_argument("operand2", help="Second numeric operand")

    try:
        args = parser.parse_args()
    except SystemExit:
        return 1

    try:
        # Convert operands to Decimal
        try:
            op1 = Decimal(args.operand1)
            op2 = Decimal(args.operand2)
        except InvalidOperation as e:
            raise ValidationError(
                f"Invalid input. '{args.operand1}' and '{args.operand2}' "
                "must be numeric"
            ) from e

        # Get and execute operation
        operation = get_operation(args.operation)
        result = operation(op1, op2)

        # Output result
        print(result)
        return 0

    except ValidationError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except ArithmeticError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    except CalculatorError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
