---
name: cli-calculator-setup
description: Create a complete CLI calculator project in Python with test-first development. Use when setting up calculator projects, teaching calculator implementation, initializing calculator project structure, or recreating the calculator from scratch.
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
model: claude-haiku-4-5-20251001
user-invocable: true
---

# CLI Calculator Setup Skill

## Overview

This skill automates the creation and configuration of a production-ready CLI calculator project in Python. It recreates the complete calculator implementation with all necessary project structure, dependencies, core modules, comprehensive test suite, and code quality configuration.

The skill follows **test-first development (TDD)** discipline and creates a fully functional calculator that supports:
- Basic arithmetic operations (add, subtract, multiply, divide)
- Decimal precision using Python's `Decimal` module
- Comprehensive error handling
- CLI interface with argparse
- Complete test coverage (unit, contract, integration tests)
- Code quality gates (Black, isort, pylint, mypy)

## When to Use

Activate this skill when you need to:
- **Setup a new calculator project** from scratch
- **Recreate the calculator** for teaching or learning purposes
- **Duplicate the calculator** to another directory or system
- **Initialize a calculator environment** with all dependencies
- **Learn calculator implementation** with test-first discipline
- **Start a calculator module** as part of a larger application
- **Teach Python basics** using a practical calculator example

## Key Capabilities

### 1. Project Structure Creation
Generates a complete, organized project directory:
```
calculator-project/
├── src/
│   ├── __init__.py
│   ├── calculator.py      (core arithmetic operations)
│   ├── cli.py             (command-line interface)
│   └── errors.py          (exception hierarchy)
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_calculator.py    (25 unit tests)
│   │   └── test_errors.py        (4 error tests)
│   ├── contract/
│   │   ├── __init__.py
│   │   └── test_cli_contract.py  (13 CLI contract tests)
│   └── integration/
│       ├── __init__.py
│       └── test_end_to_end.py    (21 integration tests)
├── pyproject.toml         (comprehensive configuration)
├── README.md              (project documentation)
└── .gitignore
```

### 2. Core Module Implementation

**src/errors.py** - Exception hierarchy:
- `CalculatorError` (base exception)
- `ArithmeticError` (arithmetic operation errors)
- `ValidationError` (input validation errors)

**src/calculator.py** - Arithmetic operations:
- `add(Decimal, Decimal) → Decimal`
- `subtract(Decimal, Decimal) → Decimal`
- `multiply(Decimal, Decimal) → Decimal`
- `divide(Decimal, Decimal) → Decimal` (with zero check)
- `get_operation(str) → Callable` (operation routing)

**src/cli.py** - Command-line interface:
- ArgumentParser with operation, operand1, operand2
- Input validation with descriptive error messages
- Proper exit codes (0: success, 1: validation error, 2: arithmetic error)
- Output to stdout, errors to stderr

### 3. Comprehensive Test Suite (59 Tests)

**Unit Tests (25 tests):**
- Addition, subtraction, multiplication, division
- Positive integers, decimals, negative numbers, zero cases
- Operation routing with name and symbol aliases

**Contract Tests (13 tests):**
- CLI interface behavior
- Arithmetic operations through CLI
- Decimal number handling
- Negative number handling
- Error handling and exit codes
- Success exit code validation

**Integration Tests (21 tests):**
- Basic arithmetic operations
- Decimal arithmetic (including repeating decimals)
- Negative number operations
- Error handling and exit codes
- Operation aliases (+, -, *, /)
- Complex scenarios (large numbers, small decimals, zero operations)

**Error Tests (4 tests):**
- Exception hierarchy validation
- Error message verification

### 4. Dependencies Management

Configures project with:
- **Python 3.10+** with mandatory type hints
- **uv** package manager for dependency management
- **Development dependencies**:
  - pytest (testing)
  - black (code formatting)
  - isort (import sorting)
  - pylint (linting)
  - mypy (type checking)

### 5. Code Quality Configuration

Complete `pyproject.toml` with:
- Black: 88-character line limit formatting
- isort: Intelligent import sorting with black profile
- pylint: Detailed linting configuration
- mypy: Strict type checking with all checks enabled
- pytest: Test discovery and configuration

**Quality Standards:**
- Black: 100% compliance
- isort: All imports properly sorted
- pylint: 10.00/10 perfect rating
- mypy: Zero type errors, all functions annotated

## Process

When you request calculator setup, Claude will:

### Phase 1: Requirements Confirmation
- Clarify project location and name
- Confirm feature requirements (operations, precision, etc.)
- Discuss customization preferences

### Phase 2: Project Structure Creation
- Create directory structure (src/, tests/unit, tests/contract, tests/integration)
- Create all module files (__init__.py for each package)
- Establish test subdirectories

### Phase 3: Core Implementation
- Implement `errors.py` with exception hierarchy
- Implement `calculator.py` with arithmetic operations
- Implement `cli.py` with argparse interface
- Add comprehensive docstrings and type hints

### Phase 4: Test Suite Creation
- Create unit tests (25 tests for core logic)
- Create contract tests (13 tests for CLI behavior)
- Create integration tests (21 tests for end-to-end scenarios)
- Create error tests (4 tests for exception hierarchy)

### Phase 5: Configuration Setup
- Create `pyproject.toml` with tool configurations
- Configure pytest with proper discovery and markers
- Setup Black, isort, pylint, mypy configurations
- Create `.gitignore` for Python projects

### Phase 6: Dependency Installation
- Install project with development dependencies
- Create/update `uv.lock` for reproducible builds

### Phase 7: Validation
- Run complete test suite (verify 59/59 passing)
- Run code quality checks (Black, isort, pylint, mypy)
- Verify exit codes and error handling
- Test all operations and edge cases

### Phase 8: Documentation
- Create README.md with usage instructions
- Document all operations and examples
- Provide testing and development instructions
- Include troubleshooting guide

## Example Invocations

**Basic Setup:**
```
User: "Create a CLI calculator project"
Claude: Creates complete working calculator in current directory
```

**Teaching Context:**
```
User: "Set up a calculator project for teaching Python to beginners"
Claude: Creates calculator with detailed comments, docstrings, clear structure
```

**Specific Location:**
```
User: "Create a calculator project in /path/to/my-calculator"
Claude: Sets up calculator at specified location
```

**Feature Request:**
```
User: "Create a calculator that handles large numbers and decimals"
Claude: Configures Decimal module for arbitrary precision arithmetic
```

## Usage After Setup

### Running the Calculator

```bash
# Using Python module syntax
python -m src.cli add 5 3
# Output: 8

python -m src.cli divide 10 3
# Output: 3.333333333333333333333333333

python -m src.cli + -5 3
# Output: -2
```

### Running Tests

```bash
# All tests
pytest tests/ -v

# Specific test category
pytest tests/unit/ -v
pytest tests/contract/ -v
pytest tests/integration/ -v
```

### Code Quality Checks

```bash
# Format code
black src/ tests/

# Check imports
isort src/ tests/

# Type checking
mypy src/

# Linting
pylint src/
```

## Integration with Other Skills/Tools

This skill works well alongside:
- **Project initialization skills** (setup git, create README, etc.)
- **Python environment skills** (virtual environment setup, version management)
- **Testing and validation skills** (CI/CD setup, test coverage analysis)
- **Documentation skills** (API documentation, tutorial creation)
- **Code quality skills** (automated linting, formatting)

## Technical Details

### Decimal Precision
- Uses Python's `Decimal` module for unlimited precision arithmetic
- Eliminates floating-point rounding errors
- Supports very large numbers and very small decimals

### Error Handling Strategy
- Hierarchical exception structure for precise error categorization
- Descriptive error messages for user guidance
- Exit codes follow conventions: 0 (success), 1 (validation error), 2 (arithmetic error)

### Testing Discipline
- Test-first development (TDD): tests written before or alongside code
- Three-layer testing strategy:
  - **Unit tests**: Core function behavior
  - **Contract tests**: CLI interface compliance
  - **Integration tests**: End-to-end scenarios
- 100% test pass rate (59/59 tests)

### Type Safety
- Mandatory type hints on all functions
- Strict mypy checking (no untyped defs)
- Complete function signatures with return types

## Troubleshooting

### Tests Fail After Setup
1. Verify Python 3.10+ is installed: `python --version`
2. Ensure dependencies installed: `uv sync --dev`
3. Check current directory is project root
4. Run individual test files to isolate issues

### Code Quality Checks Fail
1. Run Black to auto-format: `black src/ tests/`
2. Run isort to fix imports: `isort src/ tests/`
3. Review pylint output for specific issues
4. Run mypy for type errors: `mypy src/`

### CLI Not Found
1. Verify src/ directory exists with __init__.py
2. Check you're in project root directory
3. Use full module path: `python -m src.cli`
4. Ensure src/ is importable Python package

### Division by Zero Error
- This is expected behavior: `divide 10 0` correctly returns error (exit code 2)
- Message: "Cannot divide by zero"

## Success Criteria

Your calculator setup is complete when:
- ✅ All 59 tests pass
- ✅ Code quality: Black, isort, pylint (10.00/10), mypy all pass
- ✅ CLI accepts operations: add, subtract, multiply, divide, +, -, *, /
- ✅ Error handling works: division by zero (exit code 2), invalid input (exit code 1)
- ✅ Decimal precision works: `divide 10 3` shows full precision
- ✅ Negative numbers work: `add -5 3` returns -2
- ✅ Project structure follows specification

## Related Skills/Commands

Once your calculator is set up, you might want to:
- Create a slash command to run the calculator
- Add CI/CD pipeline for automated testing
- Create Jupyter notebook tutorials using the calculator
- Build calculator with additional operations (sqrt, power, etc.)
