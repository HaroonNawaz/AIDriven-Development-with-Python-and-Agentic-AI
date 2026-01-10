# Calculator Subagent Suite

## 🎯 Overview

This directory contains **reusable intelligence components** for calculator design using the **Persona + Questions + Principles (P+Q+P)** framework.

**What's Inside:**
- ✅ **Calculator Logic Design Subagent** (5+ decision points)
- ✅ **Subagent Invocation Guide** (how to use it)
- ✅ **P+Q+P Framework** documentation

---

## 📁 Files in This Directory

### 1. calculator-logic-design.md (PRIMARY)

**Purpose**: The main subagent definition using P+Q+P framework

**Contains**:
- **Persona**: Mathematical System Architect (specific cognitive stance)
- **Questions**: 7 decision points requiring deep analysis
  1. Numeric Type System (integers, floats, decimals, complex)
  2. Precision and Rounding Strategy (fixed, arbitrary, user-configurable)
  3. Supported Operations Set (basic, scientific, advanced, extensible)
  4. Edge Case and Error Handling (fail-fast, graceful, silent, rich)
  5. Operation Architecture (dispatch system, extensibility)
  6. Type Safety & Validation (static, runtime, defense-in-depth)
  7. Performance & Scalability (speed, accuracy, memory, scalability)
- **Principles**: 6 decision frameworks guiding consistent choices
- **Example Activation**: Full walkthrough of scientific calculator design

**Length**: ~500 lines
**Complexity**: Comprehensive, covers all aspects of calculator architecture

### 2. SUBAGENT-GUIDE.md (USER GUIDE)

**Purpose**: How to invoke and use the subagent effectively

**Contains**:
- What is a subagent? (vs Skills)
- How to invoke the subagent (3 methods)
- What the subagent analyzes (7 decision points)
- Full example interaction (business accounting calculator)
- Expected output format
- When to use (and NOT use)
- FAQ and troubleshooting
- Success indicators

**Length**: ~400 lines
**Complexity**: Accessible, practical usage guide

### 3. README.md (THIS FILE)

**Purpose**: Quick reference and navigation

---

## 🚀 Quick Start

### For Designers/Architects

If you need to **design calculator logic**:

1. **Read**: Start with `SUBAGENT-GUIDE.md` (10 min read)
2. **Understand**: What are the 7 decision points?
3. **Ask Claude**: Invoke the subagent with your requirements
4. **Get Recommendations**: Detailed design guidance
5. **Implement**: Use recommendations as architecture blueprint

### For Developers Implementing

If you're **coding the calculator**:

1. **Get Design**: Have architecture from subagent
2. **Reference**: Check `calculator-logic-design.md` for principles
3. **Validate**: Ensure implementation matches design
4. **Extend**: Use patterns from subagent to add features

### For Educators/Learners

If you want to **understand calculator design patterns**:

1. **Read**: Both documents to see P+Q+P in action
2. **Study**: The 7 decision points and how they interact
3. **Apply**: Use framework to analyze other systems
4. **Practice**: Design your own calculator variant

---

## 🧠 Understanding P+Q+P

### The Three Components

#### 1. **Persona (P)** - Cognitive Stance
```
"You are a mathematical system architect designing arithmetic engines.
Think about calculator logic the way a CPU architect thinks about
instruction sets: What numeric abstractions enable correctness AND
efficiency?"
```

**Why not just "expert"?** Because specific personas activate specific thinking patterns.

#### 2. **Questions (Q)** - Context Analysis
```
1. What numeric types must the calculator support?
2. How should the calculator handle decimal precision and rounding?
3. What mathematical operations should be supported?
4. How should the calculator handle edge cases and errors?
5. How should operations be organized and extended?
6. Where should type validation happen?
7. What performance characteristics should be optimized?
```

**Why these questions?** Because they force your specific situation to be analyzed, not generic patterns retrieved.

#### 3. **Principles (P)** - Decision Frameworks
```
1. Type system enables correctness without sacrificing flexibility
2. Errors should fail fast with context, not propagate silently
3. Operations should be composable and extensible
4. Precision should be explicit, not assumed
5. Scalability should be designed in, not bolted on
6. Layers should have clear boundaries and responsibilities
```

**Why principles?** Because when tradeoffs appear (speed vs precision), principles guide consistent decisions.

---

## 📊 Key Decision Matrix

| Decision Point | Determines | Examples |
|---|---|---|
| **1. Numeric Types** | What numbers you can represent | Decimal for finance, Float for physics |
| **2. Precision Strategy** | Accuracy of results | 2 decimals for money, 28 for arbitrary |
| **3. Operations Set** | What calculator can do | 4 ops for basic, 20+ for scientific |
| **4. Error Handling** | How failures are managed | Exceptions, null returns, or error codes |
| **5. Operation Architecture** | How to add new operations | Map dispatch, registry, visitor pattern |
| **6. Type Validation** | Where to catch errors | CLI, operation layer, or both |
| **7. Performance** | What matters most | Speed, accuracy, memory, scalability |

---

## 💡 When to Use This Subagent

### ✅ DO Use When:
- Designing a new calculator from scratch
- Extending calculator with new operations
- Optimizing calculator performance
- Evaluating calculator architecture
- Learning calculator design patterns
- Troubleshooting calculator issues
- Planning for future extensibility

### ❌ DON'T Use When:
- Writing simple utility functions
- Debugging specific bugs
- Implementing well-known operations
- Quick one-off calculations
- Writing tests (use testing subagent)

---

## 🔗 Integration with Other Components

This subagent works alongside:

| Component | Purpose | Integration |
|---|---|---|
| **CLI Skill** | Input parsing | Subagent recommends validation strategy |
| **Error Handling** | Error management | Subagent specifies error types needed |
| **Type System** | Type safety | Subagent defines type constraints |
| **Testing Subagent** | Test planning | Subagent guides what to test |
| **Performance Subagent** | Optimization | If performance becomes critical |

---

## 📚 Full Example: Business Accounting Calculator

**Scenario**: Design a calculator for business accounting (precision, extensibility, large numbers)

**Subagent Analysis**:

| Decision Point | Analysis | Recommendation |
|---|---|---|
| **Numeric Types** | Business needs exact cents (not floats) | Use Decimal exclusively |
| **Precision** | Accounting demands 2 decimal places | 28 digits internal, 2 for display |
| **Operations** | Basic 4 + percentage, rounding, aggregation | Core 7 + pluggable registry |
| **Error Handling** | Errors corrupt calculations → must fail-fast | Exception-based, descriptive messages |
| **Architecture** | Company will add custom functions | Registry pattern for extensibility |
| **Validation** | Three boundaries (CLI, operation, execution) | Layered validation throughout |
| **Performance** | 1-10 operations per calculation typical | Optimize for clarity over speed |

**Result**: Detailed architecture ready for implementation

---

## 🎓 Learning the P+Q+P Framework

### Study Path

1. **Foundations** (5 min)
   - Read PQP description above
   - Understand why it works

2. **Framework Details** (15 min)
   - Read Persona section in `calculator-logic-design.md`
   - Read Questions section (all 7 decision points)
   - Read Principles section (all 6 principles)

3. **Example Analysis** (10 min)
   - Read "Example Activation" section
   - See how persona → questions → principles → design

4. **Practice** (20 min)
   - Design YOUR own calculator variant using P+Q+P
   - Ask Claude to activate the subagent for your use case

5. **Mastery** (ongoing)
   - Use framework for other systems (APIs, databases, etc.)
   - Create your own subagents following this pattern

---

## ✨ What Makes This Subagent Effective

### 1. **Specific Persona**
- Not just "expert," but "mathematical system architect"
- Activates specific thinking patterns (CPU architecture analogy, boundary thinking)
- Forces analysis of precision, scalability, extensibility

### 2. **Deep Questions**
- 7 decision points (not generic "what should we do?")
- Each question forces context-specific analysis
- Together they cover the complete design space

### 3. **Actionable Principles**
- Each principle guides a specific decision
- No vague aspirations ("be efficient"), but concrete guidance
- Helps resolve tradeoffs when they appear

### 4. **Context-Aware Reasoning**
- Subagent adapts based on YOUR constraints
- Financial calculator = different design than scientific
- Education calculator = different than embedded system

---

## 🔧 How to Invoke the Subagent

### Natural Language (Recommended)

```
"I'm building a [type] calculator for [use case].
It needs to handle [constraints].
Design the logic architecture."
```

### Specific Questions

Ask any of the 7 decision point questions:
```
"Should my calculator use floats or decimals?"
"How should I handle division by zero?"
"What's the best way to support new operations?"
```

### Explicit Reference

```
"Using the Calculator Logic Design Subagent,
design a [type] calculator for [use case]"
```

---

## 📖 Files Overview

```
.claude/subagents/
├── README.md (you are here)
│   └─ Quick reference and navigation
│
├── calculator-logic-design.md (PRIMARY)
│   ├─ Subagent definition with P+Q+P
│   ├─ 7 decision points with deep analysis
│   ├─ 6 guiding principles
│   ├─ Example activation (scientific calculator)
│   └─ Output format specification
│
└── SUBAGENT-GUIDE.md (USER GUIDE)
    ├─ How to invoke the subagent
    ├─ What it analyzes
    ├─ Full example interaction
    ├─ Integration with other components
    ├─ FAQ and troubleshooting
    └─ Getting started steps
```

---

## 🎯 Success Metrics

You're using the subagent successfully when:

✅ **Clear Decisions**: You can explain calculator design in terms of the 7 decisions
✅ **Explicit Tradeoffs**: You understand what's being optimized for
✅ **Implementation Ready**: Recommendations translate directly to code
✅ **Confident Choices**: You can justify each major design decision
✅ **Future-Proof**: Architecture supports planned extensions

---

## 🚀 Next Steps

### Step 1: Read
- SUBAGENT-GUIDE.md (10 minutes)
- calculator-logic-design.md Persona section (5 minutes)

### Step 2: Understand
- What are the 7 decision points?
- How does P+Q+P activate reasoning?
- When would you use this?

### Step 3: Ask
Ask Claude about your calculator:
```
"Design the logic for a [your calculator type]"
```

### Step 4: Implement
Use the subagent's recommendations as your architecture blueprint.

---

## 📞 Questions?

Refer to:
- **SUBAGENT-GUIDE.md** for usage questions
- **calculator-logic-design.md** for design questions
- Invoke the subagent directly for specific recommendations

---

## 📝 Document Statistics

| Document | Lines | Purpose |
|---|---|---|
| calculator-logic-design.md | ~550 | Subagent definition (P+Q+P) |
| SUBAGENT-GUIDE.md | ~400 | User guide (how to use) |
| README.md | ~300 | Navigation and quick reference |
| **Total** | **~1,250** | **Comprehensive subagent documentation** |

---

## ✅ Status

- ✅ Subagent definition complete
- ✅ User guide complete
- ✅ Example activation documented
- ✅ Integration with other components mapped
- ✅ FAQ and troubleshooting covered
- ✅ Ready for production use

**Status**: Calculator Logic Design Subagent Ready ✅

---

**Last Updated**: January 10, 2026
**Framework**: Persona + Questions + Principles (P+Q+P)
**Type**: Autonomous Reasoning Subagent (5+ decision points)
