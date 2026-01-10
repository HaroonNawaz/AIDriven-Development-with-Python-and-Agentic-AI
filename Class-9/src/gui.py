"""GUI Calculator module using tkinter."""

import tkinter as tk
from decimal import Decimal, InvalidOperation
from tkinter import messagebox
from typing import Callable, Optional

from src.calculator import get_operation
from src.errors import ArithmeticError as CalcArithmeticError
from src.errors import ValidationError


class CalculatorGUI:  # pylint: disable=too-few-public-methods
    """Graphical User Interface for the calculator."""

    def __init__(self, root: tk.Tk) -> None:
        """Initialize the GUI calculator.

        Args:
            root: The tkinter root window
        """
        self.root = root
        self.root.title("Calculator - Python Edition")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Calculator state
        self.display_value: str = "0"
        self.first_operand: Optional[Decimal] = None
        self.current_operation: Optional[str] = None
        self.should_reset_display: bool = False

        # Configure style
        self.root.configure(bg="#2b2b2b")

        # Create UI components
        self._create_display()
        self._create_buttons()
        self._setup_keyboard_bindings()

    def _create_display(self) -> None:
        """Create the calculator display."""
        display_frame = tk.Frame(self.root, bg="#1e1e1e", relief=tk.SUNKEN)
        display_frame.pack(fill=tk.X, padx=10, pady=10)

        self.display = tk.Label(
            display_frame,
            text=self.display_value,
            font=("Arial", 32, "bold"),
            bg="#1e1e1e",
            fg="#00ff00",
            anchor="e",
            padx=10,
            pady=10,
        )
        self.display.pack(fill=tk.BOTH, expand=True)

    def _create_buttons(self) -> None:
        """Create calculator buttons."""
        button_frame = tk.Frame(self.root, bg="#2b2b2b")
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Button layout
        buttons = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "−"],
            ["0", ".", "=", "+"],
            ["⌫", "C", "√", "%"],
        ]

        # Color schemes
        number_color = "#3b3b3b"
        operator_color = "#ff9500"
        equals_color = "#4CAF50"
        function_color = "#2196F3"

        for row_idx, row in enumerate(buttons):
            for col_idx, char in enumerate(row):
                # Determine button color and command
                if char == "=":
                    bg_color = equals_color
                    command: Callable[[], None] = self._on_equals
                elif char in ["÷", "×", "−", "+"]:
                    bg_color = operator_color
                    # Lambda needed for capturing loop variable
                    command = lambda c=char: self._on_operator(c)  # pylint: disable=unnecessary-lambda-assignment
                elif char in ["C", "⌫", "√", "%"]:
                    bg_color = function_color
                    if char == "C":
                        command = self._on_clear
                    elif char == "⌫":
                        command = self._on_backspace
                    elif char == "√":
                        # Lambda needed for functional programming style
                        command = lambda: self._on_function("sqrt")  # pylint: disable=unnecessary-lambda-assignment
                    else:  # %
                        # Lambda needed for functional programming style
                        command = lambda: self._on_function("percent")  # pylint: disable=unnecessary-lambda-assignment
                else:
                    bg_color = number_color
                    # Lambda needed for capturing loop variable
                    command = lambda c=char: self._on_digit(c)  # pylint: disable=unnecessary-lambda-assignment

                button = tk.Button(
                    button_frame,
                    text=char,
                    font=("Arial", 18, "bold"),
                    bg=bg_color,
                    fg="white",
                    activebackground="#555555",
                    activeforeground="white",
                    command=command,
                    relief=tk.RAISED,
                    bd=2,
                )

                button.grid(
                    row=row_idx,
                    column=col_idx,
                    sticky="nsew",
                    padx=5,
                    pady=5,
                )

        # Configure grid weights for resizing
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

    def _setup_keyboard_bindings(self) -> None:
        """Setup keyboard bindings for calculator."""
        self.root.bind("<Return>", lambda e: self._on_equals())
        self.root.bind("<BackSpace>", lambda e: self._on_backspace())
        self.root.bind("c", lambda e: self._on_clear())
        self.root.bind("C", lambda e: self._on_clear())

        # Number bindings
        for i in range(10):
            digit = i
            self.root.bind(str(i), lambda e, d=digit: self._on_digit(str(d)))

        # Operator bindings
        self.root.bind("+", lambda e: self._on_operator("+"))
        self.root.bind("-", lambda e: self._on_operator("−"))
        self.root.bind("*", lambda e: self._on_operator("×"))
        self.root.bind("/", lambda e: self._on_operator("÷"))
        self.root.bind(".", lambda e: self._on_digit("."))

    def _on_digit(self, digit: str) -> None:
        """Handle digit button press.

        Args:
            digit: The digit or decimal point pressed
        """
        if self.should_reset_display:
            self.display_value = digit
            self.should_reset_display = False
        else:
            # Handle decimal point
            if digit == ".":
                if "." not in self.display_value:
                    self.display_value += digit
            else:
                # Avoid leading zeros
                if self.display_value == "0" and digit != ".":
                    self.display_value = digit
                else:
                    self.display_value += digit

        self._update_display()

    def _on_operator(self, operator: str) -> None:
        """Handle operator button press.

        Args:
            operator: The operator pressed (+, −, ×, ÷)
        """
        try:
            # Convert current display to Decimal
            current_value = Decimal(self.display_value)

            # If we already have a pending operation, calculate it first
            if self.current_operation and not self.should_reset_display:
                self._calculate_result()

            self.first_operand = current_value
            self.current_operation = operator
            self.should_reset_display = True

        except (ValueError, InvalidOperation) as e:  # pylint: disable=broad-except
            self._show_error(f"Invalid input: {e}")

    def _on_equals(self) -> None:
        """Handle equals button press."""
        if self.current_operation is None or self.first_operand is None:
            return

        self._calculate_result()

    def _calculate_result(self) -> None:
        """Calculate the result of the current operation."""
        try:
            second_operand = Decimal(self.display_value)

            # Map display operators to operation names
            op_map = {"+": "add", "−": "subtract", "×": "multiply", "÷": "divide"}

            if self.current_operation is None:
                self._show_error("Invalid operation")
                return

            operation_name = op_map.get(self.current_operation)
            if operation_name is None:
                self._show_error("Invalid operation")
                return

            # Get the operation function
            operation = get_operation(operation_name)

            # Execute the operation
            if self.first_operand is None:
                self._show_error("Invalid state: no first operand")
                return
            result = operation(self.first_operand, second_operand)

            # Update display with result
            self.display_value = str(result)
            self._update_display()

            # Reset state
            self.first_operand = None
            self.current_operation = None
            self.should_reset_display = True

        except CalcArithmeticError as e:
            self._show_error(f"Math Error: {e}")
            self._reset_state()
        except ValidationError as e:
            self._show_error(f"Validation Error: {e}")
            self._reset_state()
        except (ValueError, InvalidOperation) as e:  # pylint: disable=broad-except
            self._show_error(f"Error: {e}")
            self._reset_state()

    def _on_function(self, func: str) -> None:
        """Handle function button press.

        Args:
            func: The function to apply (sqrt, percent)
        """
        try:
            value = Decimal(self.display_value)

            if func == "sqrt":
                # Calculate square root
                if value < 0:
                    self._show_error("Cannot take square root of negative number")
                    return
                result = value.sqrt()
                self.display_value = str(result)

            elif func == "percent":
                # Convert to percentage
                if self.first_operand is not None:
                    # Calculate percentage of first operand
                    result = (self.first_operand * value) / Decimal(100)
                else:
                    # Otherwise, just divide by 100
                    result = value / Decimal(100)
                self.display_value = str(result)

            self._update_display()
            self.should_reset_display = True

        except (ValueError, InvalidOperation) as e:  # pylint: disable=broad-except
            self._show_error(f"Error: {e}")

    def _on_clear(self) -> None:
        """Clear the calculator."""
        self._reset_state()
        self.display_value = "0"
        self._update_display()

    def _on_backspace(self) -> None:
        """Handle backspace button press."""
        if len(self.display_value) > 1:
            self.display_value = self.display_value[:-1]
        else:
            self.display_value = "0"

        self._update_display()

    def _update_display(self) -> None:
        """Update the display label."""
        self.display.config(text=self.display_value)

    def _show_error(self, message: str) -> None:
        """Show an error message.

        Args:
            message: The error message to display
        """
        messagebox.showerror("Calculator Error", message)

    def _reset_state(self) -> None:
        """Reset calculator state."""
        self.first_operand = None
        self.current_operation = None
        self.should_reset_display = False


def main() -> None:
    """Main entry point for GUI calculator."""
    root = tk.Tk()
    _calculator = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
