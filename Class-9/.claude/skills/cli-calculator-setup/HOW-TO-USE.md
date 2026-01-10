# How to Use the CLI Calculator Skill

## Quick Start (30 Seconds)

Just ask Claude Code naturally:

```
"Create a CLI calculator project"
```

Claude will automatically recognize this request, activate the skill, and create a complete working calculator project with:
- ✅ 4 core modules (errors, calculator, cli, __init__)
- ✅ 59 comprehensive tests
- ✅ Complete configuration (pyproject.toml, pytest, Black, isort, mypy, pylint)
- ✅ Full documentation
- ✅ Perfect code quality (10.00/10 pylint rating)

## Detailed Usage Examples

### Example 1: Basic Setup

**You ask:**
```
"Create a CLI calculator project"
```

**Claude does:**
1. Creates project directory structure
2. Generates all source files
3. Creates 59 tests across 3 layers
4. Configures tools and dependencies
5. Verifies everything works
6. Provides instructions

**You get:**
- Ready-to-use calculator project
- All tests passing
- Perfect code quality

**Run it:**
```bash
python -m src.cli add 5 3
# Output: 8
```

---

### Example 2: Teaching Context

**You ask:**
```
"Set up a calculator project for teaching Python basics to beginners"
```

**Claude customizes:**
- Adds extra-detailed comments
- Enhances docstrings with examples
- Includes learning-focused test organization
- Explains why Decimal is used
- Shows error handling patterns

**You get:**
- Same 59 tests and complete structure
- Enhanced with educational content
- Perfect for teaching/learning

---

### Example 3: Specific Location

**You ask:**
```
"Create a calculator project in ~/my-projects/my-calculator"
```

**Claude creates:**
- Project at specified location
- Same complete structure
- Same 59 tests
- Same perfect quality

**Run it:**
```bash
cd ~/my-projects/my-calculator
python -m src.cli multiply 7 6
# Output: 42
```

---

### Example 4: Integration into Larger Project

**You ask:**
```
"I need a calculator module to integrate into my application"
```

**Claude creates:**
- Self-contained calculator package
- Structured for easy import
- Ready to use as submodule
- All tests isolated

**Use it:**
```python
from calculator.calculator import add, divide
from calculator.errors import ArithmeticError
from decimal import Decimal

result = add(Decimal("10.5"), Decimal("20.3"))
```

---

## Skill Activation

### Automatic Keywords (No Slash Command Needed)

The skill activates automatically when you mention:
- "Create a calculator"
- "Set up a calculator"
- "Build a CLI calculator"
- "Calculator project"
- "Recreate the calculator"
- "I want a calculator"

### What NOT to Ask

These won't activate the skill:
- "What is a calculator?" (informational, not setup)
- "How do I use a calculator?" (usage question, not creation)
- "Debug my calculator" (troubleshooting, not creation)

---

## What Gets Created

### Directory Structure
```
my-calculator/
├── src/                    # Source code
│   ├── __init__.py
│   ├── calculator.py      # Core arithmetic
│   ├── cli.py             # Command-line interface
│   └── errors.py          # Exception hierarchy
├── tests/                 # Comprehensive tests
│   ├── unit/              # 29 unit tests
│   ├── contract/          # 13 CLI tests
│   └── integration/       # 17 e2e tests
├── pyproject.toml         # Complete configuration
├── uv.lock                # Locked dependencies
├── README.md              # Documentation
└── .gitignore             # Git ignore
```

### Test Coverage
- **Unit Tests (25)**: Core logic, edge cases, operations
- **Contract Tests (13)**: CLI behavior, exit codes, output
- **Integration Tests (21)**: End-to-end scenarios, real usage
- **Total: 59 tests (100% passing)**

### Code Quality
- **Black**: 100% compliant (88-char limit)
- **isort**: All imports properly sorted
- **pylint**: 10.00/10 perfect rating
- **mypy**: Zero type errors (strict mode)

---

## Using Your Calculator

### Run Operations

```bash
# Addition
python -m src.cli add 5 3
# Output: 8

# Subtraction
python -m src.cli subtract 10 4
# Output: 6

# Multiplication
python -m src.cli multiply 7 6
# Output: 42

# Division
python -m src.cli divide 20 4
# Output: 5

# Using aliases
python -m src.cli + 2 3        # Addition
python -m src.cli - 10 3       # Subtraction
python -m src.cli \* 4 5       # Multiplication
python -m src.cli / 15 3       # Division
```

### Decimal Precision

```bash
# Works with decimals
python -m src.cli add 2.5 3.7
# Output: 6.2

# Shows full precision
python -m src.cli divide 10 3
# Output: 3.333333333333333333333333333

# Handles negative numbers
python -m src.cli add -5 3
# Output: -2
```

### Error Handling

```bash
# Division by zero (exit code 2)
python -m src.cli divide 10 0
# stderr: Error: Cannot divide by zero
# exit code: 2

# Invalid input (exit code 1)
python -m src.cli add abc 3
# stderr: Error: Invalid input. 'abc' and '3' must be numeric
# exit code: 1

# Missing operand (exit code 1)
python -m src.cli add 5
# stderr: error: the following arguments are required: operand2
# exit code: 1

# Unsupported operation (exit code 1)
python -m src.cli power 2 3
# stderr: Error: Unsupported operation: power
# exit code: 1
```

---

## Testing Your Calculator

### Run All Tests
```bash
pytest tests/ -v
# 59 passed in ~17 seconds
```

### Run Specific Test Layer
```bash
# Unit tests
pytest tests/unit/ -v

# Contract tests (CLI)
pytest tests/contract/ -v

# Integration tests
pytest tests/integration/ -v
```

### Run Specific Test
```bash
pytest tests/unit/test_calculator.py::TestAddition::test_add_positive_integers -v
```

---

## Code Quality Checks

### Format Code
```bash
black src/ tests/
# 1 file reformatted, 7 files left unchanged
```

### Sort Imports
```bash
isort src/ tests/
# All imports properly sorted
```

### Type Checking
```bash
mypy src/
# Success: no issues found in 4 source files
```

### Linting
```bash
pylint src/
# Your code has been rated at 10.00/10
```

---

## Integration with Git

### Initialize Repository
```bash
cd my-calculator
git init
git add .
git commit -m "Initial calculator project setup"
git branch -M main
```

### Create Remote Repository
```bash
# Create on GitHub, GitLab, etc.
git remote add origin <your-repo-url>
git push -u origin main
```

### Team Sharing
```bash
# Team members can clone
git clone <repo-url>
cd my-calculator
uv sync --dev
pytest tests/ -v
```

---

## Extending the Calculator

### Add New Operation

1. **Update calculator.py:**
```python
def square_root(operand1: Decimal, operand2: Decimal = None) -> Decimal:
    """Calculate square root of operand1."""
    if operand1 < 0:
        raise ArithmeticError("Cannot take square root of negative")
    return Decimal(str(float(operand1) ** 0.5))
```

2. **Update get_operation():**
```python
operations = {
    # ... existing operations ...
    "sqrt": lambda x, y: square_root(x),
}
```

3. **Add tests:**
```python
def test_square_root():
    assert square_root(Decimal(4)) == Decimal(2)
    assert square_root(Decimal(9)) == Decimal(3)
```

4. **Verify quality:**
```bash
pytest tests/ -v
black src/
mypy src/
pylint src/
```

---

## Troubleshooting

### "Calculator project not created"
- Ask more explicitly: "Create a CLI calculator"
- Include "calculator" and "create" keywords
- Try: "Set up a calculator project for me"

### "Tests won't run"
```bash
# Install dependencies first
uv sync --dev

# Then run tests
pytest tests/ -v
```

### "Python not found"
- Ensure Python 3.10+: `python --version`
- Use `python3` if `python` doesn't work
- Update Python if version < 3.10

### "ModuleNotFoundError: No module named 'src'"
```bash
# Make sure you're in project root
cd my-calculator

# Install project
uv sync --dev

# Then run
python -m src.cli add 5 3
```

### "Code quality checks fail"
```bash
# Auto-format with Black
black src/ tests/

# Auto-sort imports
isort src/ tests/

# Then run tests again
pytest tests/ -v
```

---

## Customization Options

When creating a calculator, you can ask for:

| Request | Result |
|---------|--------|
| "Basic calculator" | Standard 4 operations |
| "For teaching" | Enhanced comments, docstrings |
| "Production-ready" | Extra logging, configuration |
| "With CI/CD" | GitHub Actions, tests automation |
| "Minimal version" | Just essentials, no extras |
| "Extended version" | More operations, advanced features |

---

## Where to Find Information

| Question | File |
|----------|------|
| "How do I use the skill?" | **HOW-TO-USE.md** (this file) |
| "What are the technical details?" | **reference.md** |
| "Show me examples" | **examples.md** |
| "What's in the skill?" | **SKILL-SUMMARY.md** |
| "Full skill definition" | **SKILL.md** |
| "How to create project?" | **scripts/setup-calculator.py** |

---

## Success Checklist

Your calculator project is set up correctly when:

- ✅ Directory structure exists
- ✅ All source files present
- ✅ 59 tests exist
- ✅ All tests pass: `pytest tests/ -v`
- ✅ pylint rating 10.00/10: `pylint src/`
- ✅ Type check passes: `mypy src/`
- ✅ Black compliance: `black --check src/`
- ✅ Calculator works: `python -m src.cli add 5 3` → `8`

---

## Questions?

Refer to the skill files:
- **SKILL.md** - Complete skill documentation
- **reference.md** - Technical architecture
- **examples.md** - Practical examples
- **SKILL-SUMMARY.md** - Overview and summary

Or ask Claude: "Help me use the calculator skill"

---

**Status:** Skill Ready to Use ✅

You can now create a perfect calculator project anytime!
