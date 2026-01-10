"""Contract tests for CLI interface."""

import subprocess
import sys
from typing import Tuple


def run_calc(args: list) -> Tuple[str, str, int]:
    """Run calculator with arguments and return stdout, stderr, exit code."""
    from pathlib import Path

    project_root = Path(__file__).parent.parent.parent
    result = subprocess.run(
        [sys.executable, "-m", "src.cli"] + args,
        capture_output=True,
        text=True,
        cwd=str(project_root),
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


class TestArithmeticOperations:
    """Test contract for arithmetic operations."""

    def test_add_operation(self) -> None:
        """Test: calc add 5 3 returns 8."""
        stdout, stderr, code = run_calc(["add", "5", "3"])
        assert code == 0, f"Exit code: {code}, stderr: {stderr}"
        assert stdout == "8", f"Expected '8', got '{stdout}'"

    def test_subtract_operation(self) -> None:
        """Test: calc subtract 10 4 returns 6."""
        stdout, stderr, code = run_calc(["subtract", "10", "4"])
        assert code == 0, f"Exit code: {code}, stderr: {stderr}"
        assert stdout == "6", f"Expected '6', got '{stdout}'"

    def test_multiply_operation(self) -> None:
        """Test: calc multiply 7 6 returns 42."""
        stdout, stderr, code = run_calc(["multiply", "7", "6"])
        assert code == 0, f"Exit code: {code}, stderr: {stderr}"
        assert stdout == "42", f"Expected '42', got '{stdout}'"

    def test_divide_operation(self) -> None:
        """Test: calc divide 20 4 returns 5."""
        stdout, stderr, code = run_calc(["divide", "20", "4"])
        assert code == 0, f"Exit code: {code}, stderr: {stderr}"
        assert stdout == "5", f"Expected '5', got '{stdout}'"


class TestDecimalOperations:
    """Test contract for decimal operations."""

    def test_add_decimals(self) -> None:
        """Test: calc add 2.5 3.7 returns 6.2."""
        stdout, stderr, code = run_calc(["add", "2.5", "3.7"])
        assert code == 0, f"Exit code: {code}, stderr: {stderr}"
        assert stdout == "6.2", f"Expected '6.2', got '{stdout}'"

    def test_divide_decimals(self) -> None:
        """Test: calc divide 10 3 returns 3.333..."""
        stdout, stderr, code = run_calc(["divide", "10", "3"])
        assert code == 0, f"Exit code: {code}, stderr: {stderr}"
        assert stdout.startswith(
            "3.33"
        ), f"Expected starting with '3.33', got '{stdout}'"


class TestNegativeNumbers:
    """Test contract for negative numbers."""

    def test_add_negative(self) -> None:
        """Test: calc add -5 3 returns -2."""
        stdout, stderr, code = run_calc(["add", "-5", "3"])
        assert code == 0, f"Exit code: {code}, stderr: {stderr}"
        assert stdout == "-2", f"Expected '-2', got '{stdout}'"

    def test_multiply_negatives(self) -> None:
        """Test: calc multiply -4 -5 returns 20."""
        stdout, stderr, code = run_calc(["multiply", "-4", "-5"])
        assert code == 0, f"Exit code: {code}, stderr: {stderr}"
        assert stdout == "20", f"Expected '20', got '{stdout}'"


class TestErrorHandling:
    """Test contract for error handling."""

    def test_division_by_zero(self) -> None:
        """Test: calc divide 10 0 returns error with exit code 2."""
        stdout, stderr, code = run_calc(["divide", "10", "0"])
        assert code == 2, f"Expected exit code 2, got {code}"
        assert (
            "Cannot divide by zero" in stderr
        ), f"Expected error message in stderr: {stderr}"

    def test_invalid_input(self) -> None:
        """Test: calc add abc 3 returns error with exit code 1."""
        stdout, stderr, code = run_calc(["add", "abc", "3"])
        assert code == 1, f"Expected exit code 1, got {code}"
        assert "Error" in stderr, f"Expected error message in stderr: {stderr}"

    def test_missing_operand(self) -> None:
        """Test: calc add 5 returns error with exit code 1."""
        stdout, stderr, code = run_calc(["add", "5"])
        assert code == 1, f"Expected exit code 1, got {code}"

    def test_unsupported_operation(self) -> None:
        """Test: calc power 2 3 returns error with exit code 1."""
        stdout, stderr, code = run_calc(["power", "2", "3"])
        assert code == 1, f"Expected exit code 1, got {code}"
        assert "Error" in stderr, f"Expected error message in stderr: {stderr}"


class TestSuccessExitCode:
    """Test success exit code contract."""

    def test_success_returns_zero(self) -> None:
        """Test: successful operation returns exit code 0."""
        _, _, code = run_calc(["add", "1", "1"])
        assert code == 0, f"Expected exit code 0 for success, got {code}"
