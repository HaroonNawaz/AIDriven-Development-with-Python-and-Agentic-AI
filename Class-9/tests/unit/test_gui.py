"""Tests for GUI calculator module."""

import tkinter as tk
from decimal import Decimal
from unittest.mock import MagicMock, patch

import pytest

from src.gui import CalculatorGUI


class TestCalculatorGUIInitialization:
    """Tests for GUI initialization."""

    def test_gui_initializes(self) -> None:
        """Test that GUI initializes properly."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            assert calc.display_value == "0"
            assert calc.first_operand is None
            assert calc.current_operation is None
            assert calc.should_reset_display is False
        finally:
            root.destroy()

    def test_display_created(self) -> None:
        """Test that display label is created."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            assert calc.display is not None
            assert calc.display.cget("text") == "0"
        finally:
            root.destroy()


class TestCalculatorGUIDigitInput:
    """Tests for digit input handling."""

    def test_single_digit_input(self) -> None:
        """Test single digit input."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("5")
            assert calc.display_value == "5"
        finally:
            root.destroy()

    def test_multiple_digit_input(self) -> None:
        """Test multiple digit input."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("1")
            calc._on_digit("2")
            calc._on_digit("3")
            assert calc.display_value == "123"
        finally:
            root.destroy()

    def test_decimal_point_input(self) -> None:
        """Test decimal point input."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("5")
            calc._on_digit(".")
            calc._on_digit("5")
            assert calc.display_value == "5.5"
        finally:
            root.destroy()

    def test_leading_zero_handling(self) -> None:
        """Test that leading zeros are handled properly."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("0")
            calc._on_digit("5")
            assert calc.display_value == "5"
        finally:
            root.destroy()

    def test_no_multiple_decimal_points(self) -> None:
        """Test that only one decimal point is allowed."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("5")
            calc._on_digit(".")
            calc._on_digit("5")
            calc._on_digit(".")
            assert calc.display_value == "5.5"
        finally:
            root.destroy()


class TestCalculatorGUIOperations:
    """Tests for calculator operations."""

    def test_addition(self) -> None:
        """Test addition operation."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("5")
            calc._on_operator("+")
            calc._on_digit("3")
            calc._on_equals()
            assert calc.display_value == "8"
        finally:
            root.destroy()

    def test_subtraction(self) -> None:
        """Test subtraction operation."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("1")
            calc._on_digit("0")
            calc._on_operator("−")
            calc._on_digit("4")
            calc._on_equals()
            assert calc.display_value == "6"
        finally:
            root.destroy()

    def test_multiplication(self) -> None:
        """Test multiplication operation."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("7")
            calc._on_operator("×")
            calc._on_digit("6")
            calc._on_equals()
            assert calc.display_value == "42"
        finally:
            root.destroy()

    def test_division(self) -> None:
        """Test division operation."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("2")
            calc._on_digit("0")
            calc._on_operator("÷")
            calc._on_digit("4")
            calc._on_equals()
            assert calc.display_value == "5"
        finally:
            root.destroy()

    @patch("src.gui.messagebox.showerror")
    def test_division_by_zero_error(self, mock_showerror: MagicMock) -> None:
        """Test that division by zero is caught."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("1")
            calc._on_operator("÷")
            calc._on_digit("0")
            # Should show error when trying to calculate
            # (messagebox.showerror will be called)
            calc._on_equals()
            # State should be reset after error
            assert calc.first_operand is None
            # Verify error was shown
            mock_showerror.assert_called_once()
        finally:
            root.destroy()


class TestCalculatorGUIFunctions:
    """Tests for calculator functions."""

    def test_square_root(self) -> None:
        """Test square root function."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("9")
            calc._on_function("sqrt")
            assert calc.display_value == "3"
        finally:
            root.destroy()

    @patch("src.gui.messagebox.showerror")
    def test_square_root_negative_error(self, mock_showerror: MagicMock) -> None:
        """Test that square root of negative number is caught."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("-")
            calc._on_digit("5")
            # Should show error
            calc._on_function("sqrt")
            # Verify error was shown
            mock_showerror.assert_called_once()
        finally:
            root.destroy()

    def test_percentage_simple(self) -> None:
        """Test simple percentage conversion."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("5")
            calc._on_digit("0")
            calc._on_function("percent")
            # 50% = 0.5
            assert calc.display_value == "0.5"
        finally:
            root.destroy()


class TestCalculatorGUIClear:
    """Tests for clear and backspace functions."""

    def test_clear_button(self) -> None:
        """Test clear button."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("5")
            calc._on_digit("5")
            calc._on_clear()
            assert calc.display_value == "0"
            assert calc.first_operand is None
            assert calc.current_operation is None
        finally:
            root.destroy()

    def test_backspace_button(self) -> None:
        """Test backspace button."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("5")
            calc._on_digit("5")
            calc._on_backspace()
            assert calc.display_value == "5"
        finally:
            root.destroy()

    def test_backspace_to_single_digit(self) -> None:
        """Test backspace reducing to single digit."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("5")
            calc._on_backspace()
            assert calc.display_value == "0"
        finally:
            root.destroy()


class TestCalculatorGUIChaining:
    """Tests for chained operations."""

    def test_chained_operations(self) -> None:
        """Test multiple operations in sequence."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            # 5 + 3 = 8
            calc._on_digit("5")
            calc._on_operator("+")
            calc._on_digit("3")
            calc._on_equals()
            assert calc.display_value == "8"

            # Continue with 8 * 2 = 16
            calc._on_operator("×")
            calc._on_digit("2")
            calc._on_equals()
            assert calc.display_value == "16"
        finally:
            root.destroy()

    def test_operation_replacement(self) -> None:
        """Test that operator can be changed before second operand."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("5")
            calc._on_operator("+")
            # Change operator before entering second operand
            calc._on_operator("×")
            calc._on_digit("3")
            calc._on_equals()
            # Should be 5 * 3 = 15
            assert calc.display_value == "15"
        finally:
            root.destroy()


class TestCalculatorGUIState:
    """Tests for calculator state management."""

    def test_reset_display_flag(self) -> None:
        """Test that display resets after operation."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("5")
            calc._on_operator("+")
            assert calc.should_reset_display is True

            calc._on_digit("3")
            assert calc.should_reset_display is False
        finally:
            root.destroy()

    def test_state_after_equals(self) -> None:
        """Test state is ready for new calculation after equals."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("5")
            calc._on_operator("+")
            calc._on_digit("3")
            calc._on_equals()

            # Should be ready for new operation
            assert calc.should_reset_display is True
            assert calc.first_operand is None
            assert calc.current_operation is None
        finally:
            root.destroy()


class TestCalculatorGUIDecimalOperations:
    """Tests for operations with decimal numbers."""

    def test_decimal_addition(self) -> None:
        """Test addition with decimals."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("2")
            calc._on_digit(".")
            calc._on_digit("5")
            calc._on_operator("+")
            calc._on_digit("3")
            calc._on_digit(".")
            calc._on_digit("7")
            calc._on_equals()
            assert calc.display_value == "6.2"
        finally:
            root.destroy()

    def test_decimal_division(self) -> None:
        """Test division with decimals."""
        root = tk.Tk()
        try:
            calc = CalculatorGUI(root)
            calc._on_digit("1")
            calc._on_digit("0")
            calc._on_operator("÷")
            calc._on_digit("3")
            calc._on_equals()
            # Result should start with 3.33
            assert calc.display_value.startswith("3.33")
        finally:
            root.destroy()
