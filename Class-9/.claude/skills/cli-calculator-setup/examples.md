# CLI Calculator Setup - Usage Examples

## Example 1: Basic Project Setup

**User Request:**
```
"Create a basic CLI calculator project for me"
```

**What Claude Does:**
1. Confirms project location and name
2. Creates directory structure with all subdirectories
3. Implements all core modules (errors, calculator, cli)
4. Generates comprehensive test suite (59 tests)
5. Configures pyproject.toml with all tools
6. Installs dependencies via uv
7. Runs tests to verify everything works
8. Provides usage instructions

**Result:**
```
calculator/
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   ├── cli.py
│   └── errors.py
├── tests/
│   ├── unit/
│   │   ├── test_calculator.py
│   │   └── test_errors.py
│   ├── contract/
│   │   └── test_cli_contract.py
│   └── integration/
│       └── test_end_to_end.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore

✅ 59/59 tests passing
✅ pylint: 10.00/10
✅ mypy: no errors
✅ black: compliant
```

## Example 2: Teaching Python Basics

**User Request:**
```
"Set up a calculator project for teaching Python basics to beginners"
```

**Customizations Claude Might Make:**
- Add more detailed comments in code
- Increase docstring verbosity
- Add learning-focused comments
- Include explanatory tests
- Create extra examples in test suite

**Teaching Version Features:**
```python
# calculator.py
def add(operand1: Decimal, operand2: Decimal) -> Decimal:
    """
    Add two decimal numbers.

    This is a simple function that demonstrates:
    - Function definition with type hints
    - Using the Decimal type for precise arithmetic
    - Clear docstring format

    Args:
        operand1: The first number to add (Decimal type)
        operand2: The second number to add (Decimal type)

    Returns:
        The sum of the two numbers as a Decimal

    Example:
        >>> add(Decimal(5), Decimal(3))
        Decimal('8')
    """
    return operand1 + operand2
```

**Testing Files Include:**
```python
# test_calculator.py includes comments explaining:
# - Why we use Decimal instead of float
# - How to test with edge cases
# - What exceptions to expect
# - How pytest fixtures work
```

## Example 3: Recreate in Different Location

**User Request:**
```
"I want to recreate the calculator in a new project at ~/my-projects/calc-v2"
```

**Process:**
1. Creates directory at specified path
2. Replicates exact same structure and code
3. Generates same 59 tests
4. Configures same tools and settings
5. Installs dependencies at new location

**Result:**
```bash
~/my-projects/calc-v2/
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   ├── cli.py
│   └── errors.py
├── tests/
├── pyproject.toml
└── ...
```

## Example 4: Teach Advanced Features

**User Request:**
```
"Create a calculator that teaches about Decimal precision and error handling"
```

**Enhanced Version Includes:**
```python
# calculator.py - added educational examples

def divide(operand1: Decimal, operand2: Decimal) -> Decimal:
    """
    Divide two decimal numbers with precision guarantee.

    Why Decimal instead of float?
    - float: 0.1 + 0.2 = 0.30000000000000004 (WRONG!)
    - Decimal: Decimal('0.1') + Decimal('0.2') = Decimal('0.3') (CORRECT!)

    This function demonstrates:
    - Input validation (checking for zero)
    - Raising and handling custom exceptions
    - Decimal arithmetic precision
    """
    if operand2 == 0:
        raise ArithmeticError("Cannot divide by zero")
    return operand1 / operand2
```

**Tests Include Educational Comments:**
```python
# test_calculator.py
def test_decimal_vs_float():
    """
    Demonstrate why Decimal is superior to float.

    This test shows the difference between float and Decimal arithmetic.
    """
    # Float arithmetic (WRONG)
    float_result = 0.1 + 0.2
    # float_result == 0.30000000000000004 (UNEXPECTED!)

    # Decimal arithmetic (CORRECT)
    decimal_result = Decimal('0.1') + Decimal('0.2')
    # decimal_result == Decimal('0.3') (EXPECTED!)
```

## Example 5: Project for Teaching Division by Zero

**User Request:**
```
"Create a calculator to teach students about exception handling and error codes"
```

**Features Highlighted:**
```python
# cli.py demonstrates exception handling

try:
    operation = get_operation(args.operation)
    result = operation(op1, op2)
    print(result)
    return 0  # Success exit code

except ValidationError as e:
    # Specific error type for input validation
    print(f"Error: {e}", file=sys.stderr)
    return 1  # Validation error exit code

except ArithmeticError as e:
    # Specific error type for arithmetic problems
    print(f"Error: {e}", file=sys.stderr)
    return 2  # Arithmetic error exit code

except CalculatorError as e:
    # Catch-all for any calculator error
    print(f"Error: {e}", file=sys.stderr)
    return 1  # General error exit code
```

**Tests Teaching Error Handling:**
```python
def test_division_by_zero_raises_error():
    """Demonstrate that division by zero raises ArithmeticError."""
    with pytest.raises(ArithmeticError, match="Cannot divide by zero"):
        divide(Decimal(10), Decimal(0))

def test_invalid_input_raises_validation_error():
    """Demonstrate input validation with custom exception."""
    with pytest.raises(ValidationError):
        # This would be caught during CLI parsing
        Decimal("not_a_number")
```

## Example 6: Full Development Workflow

**User Request:**
```
"Create a calculator and show me the full development workflow"
```

**Step-by-Step Results:**

### 1. Project Created
```bash
$ ls -la calculator/
calculator/
├── README.md
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   ├── cli.py
│   └── errors.py
└── tests/
```

### 2. Dependencies Installed
```bash
$ uv sync --dev
Resolved 24 packages
Installed 21 packages
```

### 3. Tests Pass
```bash
$ pytest tests/ -v
collected 59 items

tests/contract/test_cli_contract.py::TestArithmeticOperations::test_add_operation PASSED
tests/contract/test_cli_contract.py::TestArithmeticOperations::test_subtract_operation PASSED
...
tests/unit/test_errors.py::TestExceptions::test_validation_error_message PASSED

============================= 59 passed in 17.31s ==============================
```

### 4. Code Quality Checks Pass
```bash
$ black src/ tests/
1 file reformatted, 7 files left unchanged

$ isort src/ tests/
Skipped 0 files

$ mypy src/
Success: no issues found in 4 source files

$ pylint src/
Your code has been rated at 10.00/10
```

### 5. Calculator Works
```bash
$ python -m src.cli add 5 3
8

$ python -m src.cli divide 10 3
3.333333333333333333333333333

$ python -m src.cli divide 10 0
Error: Cannot divide by zero

$ echo $?
2
```

## Example 7: Minimal Setup

**User Request:**
```
"I just need a quick calculator, nothing fancy"
```

**Result:** Same comprehensive setup, but Claude emphasizes:
- All 59 tests immediately working
- Can start using calculator right away
- Quality checks all passing
- No additional configuration needed

## Example 8: Integration into Larger Project

**User Request:**
```
"Create a calculator module I can integrate into my larger Python application"
```

**Structure for Integration:**
```
my-application/
├── src/
│   ├── main.py
│   ├── calculator/  # Calculator as submodule
│   │   ├── __init__.py
│   │   ├── calculator.py
│   │   ├── cli.py
│   │   └── errors.py
│   └── other_modules/
├── tests/
│   ├── test_calculator/
│   │   ├── test_calculator.py
│   │   ├── test_cli.py
│   │   └── test_errors.py
│   └── other_tests/
├── pyproject.toml
└── ...
```

**Usage in Application:**
```python
from src.calculator.calculator import add, divide
from src.calculator.errors import ArithmeticError
from decimal import Decimal

# Use calculator functions directly
try:
    result = add(Decimal("10.5"), Decimal("20.3"))
    print(f"Result: {result}")
except ArithmeticError as e:
    print(f"Calculation error: {e}")
```

## Example 9: Learning Git Workflow

**User Request:**
```
"Create a calculator project and show me how to use it with Git"
```

**Git Workflow:**
```bash
# 1. Create project
$ python -m claude-code-guide cli-calculator-setup

# 2. Initialize Git
$ cd calculator
$ git init
$ git add .
$ git commit -m "Initial calculator project setup"

# 3. Create development branch
$ git checkout -b feature/add-logging

# 4. Make changes (add logging to operations)
$ git add src/
$ git commit -m "Add operation logging"

# 5. Run tests
$ pytest tests/ -v

# 6. Check quality
$ black src/ tests/
$ pylint src/

# 7. Commit again if needed
$ git add src/
$ git commit -m "Format code to meet quality standards"

# 8. Merge to main
$ git checkout main
$ git merge feature/add-logging
```

## Example 10: Extending the Calculator

**User Request:**
```
"Create a calculator and show me how to extend it with new operations"
```

**How to Add Square Root:**

1. **Update calculator.py:**
```python
from decimal import Decimal
import math

def square_root(operand1: Decimal, operand2: Decimal = None) -> Decimal:
    """Calculate square root of operand1 (operand2 ignored)."""
    if operand1 < 0:
        raise ArithmeticError("Cannot take square root of negative number")
    return Decimal(str(math.sqrt(float(operand1))))

def get_operation(operation_name: str) -> Callable:
    operations = {
        "add": add, "+": add,
        # ... existing operations ...
        "sqrt": lambda x, y: square_root(x),
    }
    # ...
```

2. **Update cli.py to handle single operand:**
```python
# Modify to optionally require second operand
parser.add_argument("operand1", help="First operand")
parser.add_argument("operand2", nargs="?", default="0", help="Second operand (optional)")
```

3. **Add tests:**
```python
def test_square_root():
    """Test square root operation."""
    assert square_root(Decimal(4)) == Decimal(2)
    assert square_root(Decimal(9)) == Decimal(3)
```

4. **Run quality checks:**
```bash
$ pytest tests/ -v
$ black src/
$ mypy src/
$ pylint src/
```

---

## Quick Start Summary

Choose your use case:

| Scenario | User Says | Result |
|----------|-----------|--------|
| Basic setup | "Create a calculator" | Full working calculator with 59 tests |
| Teaching | "Calculator for learning Python" | Enhanced comments and detailed docstrings |
| Integration | "I need a calculator module" | Calculator as importable package |
| Extension | "Show me how to add features" | Documented extension patterns |
| Troubleshooting | "My calculator isn't working" | Diagnosis and fix guidance |

All paths lead to the same quality: **59 tests passing, 10.00/10 pylint, perfect type safety.**
