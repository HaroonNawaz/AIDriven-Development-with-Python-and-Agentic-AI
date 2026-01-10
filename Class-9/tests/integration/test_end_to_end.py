"""End-to-end integration tests for calculator."""

import subprocess
import sys
from pathlib import Path
from typing import Tuple


def run_calc(args: list) -> Tuple[str, str, int]:
    """Run calculator with arguments and return stdout, stderr, exit code."""
    project_root = Path(__file__).parent.parent.parent
    result = subprocess.run(
        [sys.executable, "-m", "src.cli"] + args,
        capture_output=True,
        text=True,
        cwd=str(project_root),
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


class TestBasicArithmetic:
    """Test basic arithmetic operations end-to-end."""

    def test_simple_addition(self) -> None:
        """Test: simple addition 2 + 3 = 5."""
        stdout, stderr, code = run_calc(["add", "2", "3"])
        assert code == 0
        assert stdout == "5"

    def test_simple_subtraction(self) -> None:
        """Test: simple subtraction 10 - 4 = 6."""
        stdout, stderr, code = run_calc(["subtract", "10", "4"])
        assert code == 0
        assert stdout == "6"

    def test_simple_multiplication(self) -> None:
        """Test: simple multiplication 3 * 4 = 12."""
        stdout, stderr, code = run_calc(["multiply", "3", "4"])
        assert code == 0
        assert stdout == "12"

    def test_simple_division(self) -> None:
        """Test: simple division 15 / 3 = 5."""
        stdout, stderr, code = run_calc(["divide", "15", "3"])
        assert code == 0
        assert stdout == "5"


class TestDecimalArithmetic:
    """Test decimal number operations end-to-end."""

    def test_decimal_addition(self) -> None:
        """Test: decimal addition 1.5 + 2.5 = 4.0."""
        stdout, stderr, code = run_calc(["add", "1.5", "2.5"])
        assert code == 0
        assert stdout == "4.0" or stdout == "4"

    def test_decimal_multiplication(self) -> None:
        """Test: decimal multiplication 0.5 * 4 = 2.0."""
        stdout, stderr, code = run_calc(["multiply", "0.5", "4"])
        assert code == 0
        assert stdout == "2.0" or stdout == "2"

    def test_repeating_decimal_division(self) -> None:
        """Test: repeating decimal division 1 / 3 ≈ 0.333..."""
        stdout, stderr, code = run_calc(["divide", "1", "3"])
        assert code == 0
        assert stdout.startswith("0.3")


class TestNegativeNumbers:
    """Test negative number operations end-to-end."""

    def test_negative_addition(self) -> None:
        """Test: negative addition -5 + 3 = -2."""
        stdout, stderr, code = run_calc(["add", "-5", "3"])
        assert code == 0
        assert stdout == "-2"

    def test_negative_multiplication(self) -> None:
        """Test: negative multiplication -3 * -4 = 12."""
        stdout, stderr, code = run_calc(["multiply", "-3", "-4"])
        assert code == 0
        assert stdout == "12"

    def test_negative_subtraction(self) -> None:
        """Test: negative subtraction -10 - 5 = -15."""
        stdout, stderr, code = run_calc(["subtract", "-10", "5"])
        assert code == 0
        assert stdout == "-15"


class TestErrorHandling:
    """Test error handling end-to-end."""

    def test_division_by_zero_error(self) -> None:
        """Test: division by zero raises error with exit code 2."""
        stdout, stderr, code = run_calc(["divide", "100", "0"])
        assert code == 2
        assert "Cannot divide by zero" in stderr

    def test_invalid_number_error(self) -> None:
        """Test: invalid number input raises error with exit code 1."""
        stdout, stderr, code = run_calc(["add", "abc", "5"])
        assert code == 1
        assert "Error" in stderr

    def test_missing_argument_error(self) -> None:
        """Test: missing argument raises error with exit code 1."""
        stdout, stderr, code = run_calc(["add", "5"])
        assert code == 1

    def test_invalid_operation_error(self) -> None:
        """Test: invalid operation raises error with exit code 1."""
        stdout, stderr, code = run_calc(["power", "2", "3"])
        assert code == 1
        assert "Error" in stderr


class TestOperationAliases:
    """Test operation aliases work correctly end-to-end."""

    def test_plus_alias(self) -> None:
        """Test: + alias for add operation."""
        stdout, stderr, code = run_calc(["+", "2", "3"])
        assert code == 0
        assert stdout == "5"

    def test_minus_alias(self) -> None:
        """Test: - alias for subtract operation."""
        stdout, stderr, code = run_calc(["-", "10", "3"])
        assert code == 0
        assert stdout == "7"

    def test_multiply_alias(self) -> None:
        """Test: * alias for multiply operation."""
        stdout, stderr, code = run_calc(["*", "4", "5"])
        assert code == 0
        assert stdout == "20"

    def test_divide_alias(self) -> None:
        """Test: / alias for divide operation."""
        stdout, stderr, code = run_calc(["/", "20", "4"])
        assert code == 0
        assert stdout == "5"


class TestComplexScenarios:
    """Test complex calculation scenarios end-to-end."""

    def test_large_number_addition(self) -> None:
        """Test: large number addition."""
        stdout, stderr, code = run_calc(["add", "999999999", "1"])
        assert code == 0
        assert stdout == "1000000000"

    def test_very_small_decimal(self) -> None:
        """Test: very small decimal arithmetic."""
        stdout, stderr, code = run_calc(
            ["multiply", "0.0001", "0.0001"]
        )
        assert code == 0
        # Decimal precision should handle this correctly
        assert float(stdout) == 0.00000001

    def test_zero_operations(self) -> None:
        """Test: operations with zero."""
        # Zero plus something
        stdout, stderr, code = run_calc(["add", "0", "5"])
        assert code == 0
        assert stdout == "5"

        # Zero times something
        stdout, stderr, code = run_calc(["multiply", "0", "999"])
        assert code == 0
        assert stdout == "0"

        # Zero divided by something
        stdout, stderr, code = run_calc(["divide", "0", "5"])
        assert code == 0
        assert stdout == "0"
