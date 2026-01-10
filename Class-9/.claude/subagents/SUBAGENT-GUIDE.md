# Subagent Invocation Guide

## What is a Subagent?

A **Subagent** is an autonomous AI reasoning component that:
- Makes 5+ independent decisions
- Analyzes your specific context
- Provides expert recommendations
- Uses Persona + Questions + Principles (P+Q+P) to reason

Unlike Skills (which guide decisions), Subagents make autonomous recommendations.

---

## Available Subagent

### Calculator Logic Design Subagent

**Purpose**: Design optimal internal logic for calculator implementations

**Activation**: Ask Claude Code about calculator architecture

**Example Requests**:
```
"Design the logic for a scientific calculator"
"How should I architect operations in my calculator?"
"I need to extend my calculator with new operations"
"Design a calculator that supports arbitrary precision"
"Optimize my calculator's operation dispatch"
```

---

## How to Invoke the Subagent

### Method 1: Natural Language Request (Recommended)

Simply ask Claude Code about your calculator design:

```
"I'm building a calculator for financial calculations.
Design the logic architecture for precision and correctness."
```

**What Happens**:
1. Claude recognizes this is a calculator logic question
2. Activates the Calculator Logic Design Subagent
3. Analyzes your requirements using P+Q+P
4. Provides comprehensive design recommendations

---

### Method 2: Explicit Subagent Reference

If Claude doesn't automatically recognize the context:

```
"Using the Calculator Logic Design Subagent, design a
calculator for scientific engineering use cases."
```

---

### Method 3: Specific Design Question

Ask any of the 7 decision point questions:

```
"What numeric types should my calculator support?"
"How should I handle division by zero?"
"What's the best operation architecture?"
"How can I make operations extensible?"
"What's the optimal precision strategy?"
"How should I validate calculator inputs?"
"What performance characteristics should I optimize for?"
```

---

## What the Subagent Analyzes

The Calculator Logic Design Subagent uses **7 Decision Points** (P+Q+P):

| Decision | Options | Complexity |
|----------|---------|-----------|
| **1. Numeric Types** | Integers, Floats, Decimals, Complex | ⭐⭐ |
| **2. Precision Strategy** | Fixed, Arbitrary, Float, Configurable | ⭐⭐⭐ |
| **3. Operation Set** | Basic 4, Scientific, Advanced, Extensible | ⭐⭐ |
| **4. Error Handling** | Fail-fast, Graceful, Silent, Rich errors | ⭐⭐⭐ |
| **5. Operation Architecture** | Simple dispatch, Map, Visitor, Pluggable | ⭐⭐⭐ |
| **6. Type Validation** | Static, Runtime, Defense-in-depth | ⭐⭐ |
| **7. Performance Optimization** | Speed, Accuracy, Memory, Scalability | ⭐⭐⭐ |

**Total Complexity**: 5+ decision points = requires Subagent (not a simple Skill)

---

## Example: Full Subagent Interaction

### You Ask

```
"I'm designing a calculator for business accounting use cases.
It needs to handle:
- Money (to the cent)
- Business formulas (percentages, tax calculations)
- Large numbers (annual revenues, national totals)
- Extensibility (our company adds custom functions)

Design the calculator logic architecture."
```

### Subagent Activates

The subagent recognizes:
- **Persona needed**: Mathematical system architect (precision + extensibility)
- **Context**: Business/accounting (not scientific, not educational)
- **Key constraints**: Precision (cents), extensibility, large numbers

### Subagent Analyzes Each Decision Point

**Decision 1 - Numeric Types**:
```
Question: What numeric types must the calculator support?
Context: Business accounting needs exact decimal representation
Analysis:
  - $10.50 must be EXACT (not 10.50000000001 as float would give)
  - Large revenues (billions) need range support
  - No need for complex numbers or scientific notation
Recommendation: Use Decimal as primary type, reject floats
```

**Decision 2 - Precision Strategy**:
```
Question: How should decimal precision and rounding work?
Context: Business accounting demands accuracy to the cent
Analysis:
  - Display: 2 decimal places (standard for currency)
  - Internal: Arbitrary precision Decimal (no rounding until final)
  - Rounding: Use accounting rounding (round half to even)
Recommendation: Decimal with 28+ significant digits, round to 2 places for display
```

**Decision 3 - Operation Set**:
```
Question: What operations are needed?
Context: Business formulas, not scientific calculator
Analysis:
  - Core 4: +, -, *, / (obviously)
  - Percentage: x% of y
  - Rounding: round(), ceiling(), floor()
  - Aggregation: sum(), average()
  - Custom: Your company's proprietary functions
Recommendation: Core 7 operations + pluggable system for company functions
```

**Decision 4 - Error Handling**:
```
Question: How to handle errors?
Context: Accounting errors have financial consequences
Analysis:
  - Division by zero: Would corrupt calculations → ArithmeticError (fail fast)
  - Invalid operation: Should raise error (not silently fail)
  - Type errors: Immediately detect (int ÷ string should error)
Recommendation: Strict exception-based errors, prevent silent failures at all costs
```

**Decision 5 - Operation Architecture**:
```
Question: How to dispatch and extend operations?
Context: Company will add custom functions later
Analysis:
  - 7 core operations: Map-based dispatch is efficient
  - Future: 20+ operations including custom ones
  - Need: Operations addable without modifying core
Recommendation: Registry pattern - company can register new operations at runtime
```

**Decision 6 - Type Validation**:
```
Question: Where should validation happen?
Context: Accounting requires inputs to be correct
Analysis:
  - Boundary (user input): Validate numeric format, convert to Decimal
  - Operation layer: Validate operation exists and args are valid
  - Execution: Validate domain (e.g., can't divide by zero)
Recommendation: Three-layer validation (CLI → operation → execution)
```

**Decision 7 - Performance**:
```
Question: What performance targets?
Context: Business calculations are typically small-scale
Analysis:
  - Typical use: 1-10 operations in sequence
  - Scale: 100s-1000s of calculations per session
  - Speed requirement: <100ms per calculation acceptable
Recommendation: Optimize for code clarity and correctness over speed
```

### Subagent Recommendations

The subagent produces something like:

```
CALCULATOR LOGIC DESIGN FOR BUSINESS ACCOUNTING
===============================================

Numeric System:
  - Use Decimal exclusively (arbitrary precision)
  - All inputs converted to Decimal from strings
  - Reject floats (precision errors unacceptable in accounting)

Precision Strategy:
  - Internal: 28+ significant digits (Decimal default)
  - Display: 2 decimal places for currency
  - Rounding: Banker's rounding (round half to even)
  - Document: "All calculations use arbitrary precision internally"

Operation Set (Core 7):
  - Basic: +, -, *, /
  - Utility: %, round(x, places)
  - Aggregation: sum(), avg()
  - Extensible: registry.register("company_tax_formula", impl)

Error Handling:
  - ArithmeticError: "Cannot divide by zero" (fail fast)
  - ValidationError: "Input '123.45.6' is not valid number"
  - ValueError: "Operation 'multiply3' not found, available: [+, -, *, /]"
  - Strategy: Exceptions propagate up, CLI formats for user

Operation Architecture:
  - Core operations in map: operations = {"+": add, "-": subtract, ...}
  - Registry for extensibility: Calculator.register_operation(name, impl)
  - All operations: (Decimal, Decimal) → Decimal
  - All operations validate inputs before execution

Type Validation (Three Layers):
  1. CLI: Convert string inputs to Decimal (validate format)
  2. Operation: Verify operation exists, arg count, types
  3. Execution: Validate domain (e.g., log of positive only)

Performance Targets:
  - Single operation: <1ms
  - Chain of 10 operations: <10ms
  - No caching needed (operations are stateless)
  - Focus: Code clarity over raw speed

Implementation Checklist:
  ✅ Use Decimal exclusively (not float)
  ✅ Validate at all three layers
  ✅ Clear error messages (accountants need to understand errors)
  ✅ Operation registry (company can extend)
  ✅ Test edge cases (0, negative, very large numbers)
  ✅ Document precision assumptions
  ✅ No silent failures (all errors raise exceptions)

Next Steps:
  1. Implement core 7 operations with validation
  2. Create operation registry system
  3. Build comprehensive test suite
  4. Document precision behavior
  5. Plan for company function registration
```

### You Implement

You now have a detailed design to implement:
- Clear numeric type strategy (Decimal only)
- Precision expectations (28 digits internal, 2 for display)
- Operation list (7 core + extensible)
- Error handling (three layers, exceptions)
- Architecture (map + registry for extensibility)
- Performance targets (<1ms per operation)

---

## What to Expect from Subagent Output

### 1. Decision Analysis
- For each of the 5-7 decision points
- Clear explanation of options
- Specific recommendation based on YOUR context
- Explicit tradeoffs (what you're optimizing for, what you're not)

### 2. Implementation Guidance
- Specific code patterns
- What to validate and where
- Error messages to implement
- Extensibility hooks

### 3. Testing Strategy
- Edge cases to test
- Performance expectations
- Type validation tests

### 4. Documentation Needs
- What to document in specs
- Limitations to communicate
- Future extensibility points

---

## Using Subagent Recommendations

### ✅ Good Usage

```
"The subagent recommends using Decimal for precision.
Let me implement the calculator with that approach."
```

### ✅ Critical Thinking

```
"The subagent recommends fail-fast exceptions.
Does that match our system's overall error strategy?
Yes, it does. Let me implement accordingly."
```

### ✅ Asking for Clarification

```
"The subagent recommends a registry pattern for operations.
Can you explain the implementation details?"
```

### ❌ Not Questioning Recommendations

```
"The subagent said to use Decimal, but our company always uses floats.
I'll just ignore the recommendation."
(Missing opportunity to align architecture with company standard)
```

### ❌ Over-Engineering

```
"The subagent mentioned performance optimization as one consideration.
I'll spend a week optimizing micro-milliseconds."
(Subagent recommended clarity over speed - unnecessary optimization)
```

---

## When NOT to Use This Subagent

- **Simple feature**: "Add a subtract button to my calculator" (use Skill instead)
- **Bug fix**: "Division by zero returns wrong error" (debugging, not design)
- **Implementation details**: "How do I write the add function in Python?" (coding help)
- **Testing**: "Write tests for my calculator" (use testing subagent instead)

---

## Integration with Other Subagents

The Calculator Logic Design Subagent works with:

- **Input Validation Skill**: Defines WHAT to validate, skill implements HOW
- **Error Handling Skill**: Defines error categories, skill formats messages
- **API Design Skill**: If exposing calculator via API
- **Testing Subagent**: Uses design recommendations to create test plans
- **Performance Subagent**: If optimization becomes critical

---

## Frequently Asked Questions

### Q: How does this differ from asking Claude directly?

**A**: The P+Q+P framework forces systematic analysis of 7 decision points, considering context-specific constraints. Direct questions might get generic answers. Subagent ensures:
- All decision points considered
- Context analysis instead of pattern-matching
- Explicit tradeoff reasoning
- Domain-specific persona thinking

### Q: Should I always follow the subagent's recommendations?

**A**: Use critical thinking:
- ✅ Do the recommendations match YOUR constraints?
- ✅ Have you stated all constraints clearly?
- ✅ Do tradeoffs align with project priorities?
- ❌ Don't blindly follow without understanding reasoning
- ❌ Don't ignore constraints you know matter

### Q: What if the subagent recommends something different than last time?

**A**: You probably asked a different question or had different context. Subagent decisions depend on:
- Your specific requirements
- Performance targets
- Extensibility needs
- Type safety vs flexibility tradeoffs

Different calculator (scientific vs financial) → different recommendations.

### Q: Can I combine multiple subagents?

**A**: Absolutely! Example:
1. **Calculator Logic Design** → Recommends architecture
2. **Performance Subagent** → Optimizes hot paths
3. **Testing Subagent** → Plans comprehensive tests

Each contributes expertise in their domain.

### Q: What if I disagree with the subagent?

**A**: That's fine! The subagent provides reasoning, you make the final decision. Examples where you might disagree:
- Company standards that differ from recommendation
- Constraints not mentioned (legacy system compatibility)
- Different priorities (speed vs precision for your use case)

The value is in the reasoning, not blind obedience.

---

## Getting Started

### Step 1: Review the Subagent Document
Read: `calculator-logic-design.md`
- Understand the P+Q+P framework
- See what 7 decision points matter
- Review example activation

### Step 2: Ask a Question
Ask Claude Code about YOUR calculator design:
```
"I'm building [type] calculator for [use case].
Design the logic architecture considering:
- [constraint 1]
- [constraint 2]
- [constraint 3]"
```

### Step 3: Analyze the Output
- Read each decision point analysis
- Understand the tradeoffs
- Check if recommendations match your constraints

### Step 4: Implement
Use the subagent's recommendations as an implementation guide.

---

## Success Indicators

You've successfully used the subagent when:

✅ **Clear architecture**: You can describe calculator design in terms of the 7 decisions
✅ **Explicit tradeoffs**: You understand what's being optimized for
✅ **Implementation ready**: Recommendations translate directly to code
✅ **Confident decisions**: You can justify each major design choice
✅ **Future-proof**: Architecture supports planned extensions

---

**Status**: Calculator Logic Design Subagent Ready to Use ✅

You can now invoke it whenever you need to design, extend, or optimize calculator logic.
