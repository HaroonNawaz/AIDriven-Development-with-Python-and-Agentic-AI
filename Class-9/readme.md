# Class 9: Professional Calculator with CLI & GUI

## Overview

This is a comprehensive calculator project demonstrating professional Python development practices, including both Command-Line Interface (CLI) and Graphical User Interface (GUI) implementations, complete with extensive testing, type safety, and production-ready code quality.

## Key Features

### Implementations
- **CLI Calculator** - Command-line interface using Click framework
- **GUI Calculator** - Graphical interface for user-friendly interaction
- **Core Calculator Engine** - Type-safe arithmetic operations library

### Quality Standards
- ✅ Comprehensive test coverage (59+ tests)
- ✅ Type-safe code (100% mypy strict mode)
- ✅ Production-quality code (10.00/10 pylint rating)
- ✅ Professional documentation
- ✅ Error handling and edge cases

### Challenge Implementation

The calculator handles all assignment challenges:

1. **Decimal Handling** - Proper floating-point arithmetic
2. **Division by Zero** - Safe error handling and user feedback
3. **Negative Numbers** - Full support for negative operands
4. **Invalid Input** - Comprehensive input validation and error messages

## Project Structure

```
Class-9/
├── src/
│   ├── __init__.py              # Package initialization
│   ├── calculator.py            # Core calculator engine
│   ├── cli.py                   # CLI interface with Click
│   ├── gui.py                   # GUI implementation (Tkinter)
│   └── errors.py                # Custom error types
├── tests/
│   └── test_*.py                # Comprehensive test suite (59+ tests)
├── .venv/                       # Virtual environment
├── .claude/                     # Claude Code configuration
│   └── skills/
│       └── cli-calculator-setup/  # Reusable skill for calculator creation
├── pyproject.toml               # Project configuration & dependencies
├── uv.lock                      # Dependency lock file
├── FINAL-SUMMARY.md             # Comprehensive project summary
├── SKILLS-AND-SUBAGENTS-SUMMARY.md  # Skills & subagents documentation
├── Designing_Skills_&_Subagents_with_PQP.md  # Design methodology
└── gui calculator.png           # Screenshot of GUI application
```

## Technology Stack

### Core
- **Python 3.10+** - Programming language
- **Click 8.x** - CLI framework
- **Tkinter** - GUI framework (included with Python)

### Development
- **pytest** - Testing framework
- **mypy** - Type checking
- **black** - Code formatting
- **isort** - Import sorting
- **pylint** - Code quality analysis
- **uv** - Fast Python package manager

## Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip or uv package manager

### Quick Start

```bash
# Navigate to Class-9 directory
cd "C:\D-Drive\PanaVersity\P300\Al-P300\AIDriven-Development-with-Python-and-Agentic-AI\Class-9"

# Create virtual environment (if not exists)
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

# Install dependencies using uv
uv pip install -e .

# Or using pip
pip install -e .
```

## Usage

### CLI Calculator

```bash
# Basic arithmetic operations
python -m src.cli add 5 3          # Output: 8
python -m src.cli subtract 10 4    # Output: 6
python -m src.cli multiply 6 7     # Output: 42
python -m src.cli divide 20 4      # Output: 5.0

# With decimal numbers
python -m src.cli add 3.14 2.86    # Output: 6.0

# Error handling
python -m src.cli divide 10 0      # Error: Cannot divide by zero
```

### GUI Calculator

```bash
# Launch the GUI application
python -m src.gui
```

The GUI provides an interactive interface with:
- Number input buttons
- Operation buttons (+, -, ×, ÷)
- Clear and equals buttons
- Display for operations and results
- Error handling with user-friendly messages

## Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_calculator.py -v

# Run with coverage
pytest tests/ --cov=src
```

Expected result: **59+ tests passing**

## Code Quality

### Type Checking
```bash
mypy src/
```
Result: **100% type-safe, 0 errors**

### Code Style
```bash
black src/ tests/
isort src/ tests/
```

### Linting
```bash
pylint src/
```
Result: **10.00/10 rating**

## Project Architecture

### Calculator Engine (calculator.py)
Core arithmetic operations with:
- Type-safe operations
- Comprehensive error handling
- Support for integers and floats
- Extensible design for additional operations

### CLI Interface (cli.py)
Command-line interface using Click framework:
- User-friendly command syntax
- Proper error messages
- Exit codes
- Help documentation

### GUI Interface (gui.py)
Tkinter-based graphical interface:
- Intuitive button layout
- Real-time display updates
- Error notifications
- Clean, professional design

### Error Handling (errors.py)
Custom exception hierarchy:
- Calculator-specific errors
- Clear error messages
- Graceful failure handling

## Key Learning Areas

1. **Professional Python Development**
   - Project structure best practices
   - Type safety with mypy
   - Comprehensive testing strategies

2. **Software Design**
   - Separation of concerns (core, CLI, GUI)
   - Error handling patterns
   - Extensible architecture

3. **Testing & Quality**
   - Unit testing with pytest
   - Test-driven development
   - Code quality metrics

4. **User Interfaces**
   - CLI design with Click
   - GUI design with Tkinter
   - User experience considerations

## Additional Resources

### Documentation Files
- **FINAL-SUMMARY.md** - Complete overview and usage guide
- **SKILLS-AND-SUBAGENTS-SUMMARY.md** - Reusable components documentation
- **Designing_Skills_&_Subagents_with_PQP.md** - Design methodology and framework

### Skills & Subagents
Located in `.claude/skills/cli-calculator-setup/`:
- **SKILL.md** - Skill definition
- **HOW-TO-USE.md** - Complete user guide
- **reference.md** - Technical reference
- **examples.md** - Usage examples
- **setup-calculator.py** - Automation script

## Configuration

Project configuration is defined in **pyproject.toml**:
- Build system (hatchling)
- Dependencies and versions
- Testing configuration (pytest)
- Code formatting (black, isort)
- Type checking (mypy)
- Linting (pylint)

## Challenges Addressed

✅ **Decimal Handling**
- Proper floating-point arithmetic
- Precision handling
- Clear result formatting

✅ **Division by Zero**
- Custom ZeroDivisionError handling
- User-friendly error messages
- Graceful error recovery

✅ **Negative Numbers**
- Full support for negative operands
- Correct sign handling in operations
- Negative result calculations

✅ **Invalid Input**
- Type validation
- Range checking
- Clear error messages for invalid inputs

## Development Workflow

1. **Design Phase**
   - Use subagent for architecture decisions (7 decision points)
   - Define interfaces and contracts
   - Plan test coverage

2. **Implementation Phase**
   - Follow type-driven development
   - Write tests alongside code
   - Maintain code quality standards

3. **Quality Assurance**
   - Run full test suite (59+ tests)
   - Type check with mypy (strict mode)
   - Format with black and isort
   - Lint with pylint (10.00/10 target)

4. **Documentation**
   - Clear code comments where needed
   - Docstrings for public APIs
   - Usage examples
   - README documentation

## Running the Project

### Full Quality Check
```bash
# Run all quality checks
python -m pytest tests/ -v          # Run tests
mypy src/                            # Type check
black --check src/                   # Check formatting
pylint src/                          # Lint code
```

### Quick Run
```bash
# CLI usage
python -m src.cli add 10 5

# GUI launch
python -m src.gui
```

## Assignment Completion

This project successfully demonstrates:
1. ✅ Basic calculator implementation
2. ✅ Challenge handling (decimals, div by zero, negatives, validation)
3. ✅ Professional code quality
4. ✅ Comprehensive testing
5. ✅ Both CLI and GUI interfaces
6. ✅ Production-ready documentation
7. ✅ Reusable skills for future projects

## Screenshots

The project includes visual demonstrations of the working GUI application:

### GUI Calculator Application
![GUI Calculator](./gui%20calculator.png)

## Author

Haroon Nawaz
P300 - AI Driven Development with Python and Agentic AI
PanaVersity

---

**Last Updated:** January 10, 2026
**Project Status:** Complete and Production-Ready
**Code Quality:** 10.00/10 (pylint) | 100% Type-Safe (mypy) | 59+ Tests
**Documentation:** Comprehensive with examples and guides
