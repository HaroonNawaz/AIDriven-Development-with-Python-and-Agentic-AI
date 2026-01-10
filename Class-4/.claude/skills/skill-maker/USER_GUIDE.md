# Skill Maker User Guide

## Overview

The Skill Maker is a specialized Claude Code skill designed to generate new, high-quality skills that conform to official Claude Code documentation standards. It automates the creation process while ensuring consistency, completeness, and professional quality.

## Quick Start

### Basic Usage

1. **Activate the Skill**: Invoke the Skill Maker with your skill request
   ```
   I want to create a skill that [describe what you want]
   ```

2. **Answer Clarifying Questions**: The Skill Maker will ask questions about any gaps or ambiguities
   ```
   Question: What is the primary function of this skill?
   Your answer: [Provide details]
   ```

3. **Review Generated Skill**: Examine the created skill files
   ```
   Generated skill location: .claude/skills/[skill-name]/
   ```

4. **Use Your New Skill**: The skill is immediately available in your Claude Code environment

## How Skill Maker Works

### Phase 1: Requirements Gathering

When you provide a skill description, the Skill Maker analyzes your prompt to identify:

- **Core functionality**: What the skill does
- **Use cases**: When and why you'd use it
- **Inputs and outputs**: Data the skill processes
- **Required tools**: Claude Code tools needed
- **Integration points**: How it connects to other skills or resources

### Phase 2: Gap Identification

The Skill Maker identifies any missing information in your prompt:

| Gap Type | Example | Clarifying Question |
|----------|---------|-------------------|
| **Functionality** | How exactly does it work? | "What is the primary function?" |
| **Use Cases** | When would you use it? | "What are typical use scenarios?" |
| **Scope** | What's included/excluded? | "Is this focused on one capability?" |
| **Tools** | What tools are needed? | "Which Claude Code tools required?" |
| **Examples** | Can you show usage? | "Can you provide concrete examples?" |

### Phase 3: Clarification

For each identified gap, the Skill Maker asks focused questions:

- Questions are presented in priority order
- Each question is specific and actionable
- You can provide as much detail as needed
- Skill Maker adapts follow-up questions based on your answers

### Phase 4: Skill Generation

Once all critical requirements are understood, the Skill Maker:

1. Creates the skill directory structure
2. Generates the SKILL.md file with proper frontmatter
3. Creates supporting documentation and examples
4. Validates against Claude Code standards
5. Confirms successful generation

## Skill Maker Question Categories

### Category 1: Core Functionality (Priority: HIGHEST)

**These questions establish what the skill does:**

| Question | Purpose | Example Answer |
|----------|---------|-----------------|
| "What is the primary function?" | Define core capability | "Analyze code performance bottlenecks" |
| "What problem does it solve?" | Establish use case foundation | "Identify slow functions in Python code" |
| "What are inputs/outputs?" | Define data flow | "Input: Python file or code snippet; Output: Performance report" |

**When these are unclear**: Skill Maker cannot proceed; asks clarifying questions

### Category 2: Use Cases and Scope (Priority: HIGH)

**These questions establish when and how to use the skill:**

| Question | Purpose | Example Answer |
|----------|---------|-----------------|
| "What are typical use scenarios?" | Establish practical applications | "Code optimization, performance debugging, architecture review" |
| "Is this focused on one capability?" | Ensure focused scope | "Yes, specifically for performance analysis only" |
| "Are there scope limitations?" | Define boundaries | "Works with Python and JavaScript, up to 10MB files" |

**When these are unclear**: Limited effectiveness; Skill Maker asks for clarification

### Category 3: Tool Requirements (Priority: HIGH)

**These questions establish technical dependencies:**

| Question | Purpose | Example Answer |
|----------|---------|-----------------|
| "Which Claude Code tools needed?" | Define technical requirements | "Read, Bash, WebFetch for documentation" |
| "Any security considerations?" | Ensure safe tool usage | "Need to restrict Bash to read-only operations" |
| "Tool access restrictions?" | Define allowed-tools field | "Restrict to Read and Grep only" |

**When these are unclear**: Skill Maker documents assumed tool requirements

### Category 4: Documentation (Priority: MEDIUM)

**These questions ensure comprehensive documentation:**

| Question | Purpose | Example Answer |
|----------|---------|-----------------|
| "Can you provide examples?" | Enable user understanding | "[Provide 2-3 concrete examples]" |
| "What about edge cases?" | Document limitations | "Handles functions, not class methods; skips library code" |
| "Common issues/solutions?" | Support troubleshooting | "[List potential problems and fixes]" |

**When these are unclear**: Skill Maker generates examples based on inferred patterns

### Category 5: Integration (Priority: MEDIUM)

**These questions establish project integration:**

| Question | Purpose | Example Answer |
|----------|---------|-----------------|
| "Existing infrastructure?" | Ensure compatibility | "Integrates with testing framework in project" |
| "Related materials?" | Cross-reference project resources | "Related notes in notes/performance-analysis.md" |
| "Other skills needed?" | Establish dependencies | "Depends on code-analysis skill" |

**When these are unclear**: Skill Maker creates standalone skill

## Example Interaction

### User Prompt

> Create a skill that validates JSON files and provides detailed error reporting.

### Skill Maker Response

**Analysis**: Core functionality is clear, but scope and examples are missing.

**Clarifying Questions**:

1. **Scope Definition**:
   - "Should this skill validate against custom JSON schemas, or just basic JSON validity?"
   - "What error reporting detail level is needed (line numbers, suggestions, etc.)?"

2. **Use Cases**:
   - "What are typical scenarios? (Configuration validation, API response checking, data migration?)"

3. **Tool Requirements**:
   - "Should this integrate with external validation services, or use built-in JSON parsing?"

4. **Examples**:
   - "Can you provide an example of a JSON file that should fail validation and what error message you'd expect?"

### User Answers

> 1. Just basic JSON validity, with line numbers and error messages
> 2. Configuration files and API responses
> 3. Built-in only, no external services
> 4. Invalid JSON with trailing comma should show error at specific line

### Generated Skill

```
.claude/skills/json-validator/
├── SKILL.md (with complete documentation)
├── EXAMPLES.md (with concrete validation examples)
└── TEMPLATES/ (with sample JSON files)
```

## Standard Skill Naming

All generated skills follow naming conventions:

### Naming Rules

| Rule | Example |
|------|---------|
| Lowercase letters only | `json-validator` ✓ (not `JSONValidator` ✗) |
| Hyphens for word separation | `code-analyzer` ✓ (not `code_analyzer` ✗) |
| Maximum 64 characters | `performance-analysis-bottleneck-finder` (51 chars) ✓ |
| Descriptive of function | `pdf-merger` ✓ (not `tool-5` ✗) |

### Naming Examples

**Good Names**:
- `json-validator`
- `performance-profiler`
- `markdown-formatter`
- `sql-query-optimizer`
- `api-documentation-generator`

**Poor Names**:
- `utility` (too vague)
- `skill-1` (not descriptive)
- `super_tool` (underscore, mixed case)
- `toolForValidatingAndOptimizingAndAnalyzing` (too long, no hyphens)

## Skill File Structure

All generated skills follow this structure:

```
.claude/skills/skill-name/
│
├── SKILL.md
│   ├── YAML Frontmatter
│   ├── Purpose Section
│   ├── Use Cases Section
│   ├── Core Functionality
│   ├── Requirements
│   ├── Instructions
│   ├── Examples
│   ├── Troubleshooting
│   ├── Integration Points
│   └── References
│
├── EXAMPLES.md (optional)
│   ├── Example 1: Scenario
│   ├── Example 2: Scenario
│   └── Example 3: Scenario
│
├── TEMPLATES/ (optional)
│   ├── template-1.md
│   ├── template-2.md
│   └── template-3.md
│
└── SCRIPTS/ (optional)
    ├── helper-script-1.sh
    └── helper-script-2.sh
```

## YAML Frontmatter Requirements

All skills include YAML frontmatter with two required fields:

```yaml
---
name: skill-name
description: Brief description of skill capability and usage context.
---
```

### Field Specifications

| Field | Requirements | Example |
|-------|---|---------|
| `name` | Lowercase, hyphens, 1-64 chars, alphanumeric + hyphens only | `json-validator` |
| `description` | Max 1024 chars, includes both "what" and "when" info | "Validate JSON files against schemas. Use when checking configuration files or API responses." |

### Description Best Practices

**Good Description** (includes what + when):
> "Analyze code performance bottlenecks and generate optimization recommendations. Use when profiling code, identifying inefficiencies, or optimizing algorithm performance across multiple languages."

**Poor Description** (only what):
> "Analyzes code performance."

## Quality Standards

All generated skills adhere to these standards:

### Documentation Quality

- ✓ Professional and academic tone throughout
- ✓ Clear, precise language without colloquialisms
- ✓ Proper grammar and punctuation
- ✓ Technical terms defined on first use
- ✓ Hierarchical structure with clear headers
- ✓ Concrete examples demonstrating functionality

### Technical Quality

- ✓ Valid YAML frontmatter
- ✓ Proper Markdown formatting
- ✓ Accurate code examples
- ✓ Working cross-references
- ✓ Complete file structure

### Standards Compliance

- ✓ Follows Claude Code documentation standards
- ✓ Adheres to project CLAUDE.md requirements
- ✓ Uses established naming conventions
- ✓ Integrates with project directory structure
- ✓ Professional communication standards

## Troubleshooting Skill Maker

### Issue: "Too Many Clarifying Questions"

**Solution**: Provide more detail in initial prompt
```
INSTEAD OF: "Create a skill for analyzing code"
USE: "Create a skill that analyzes Python code performance, identifies bottlenecks,
     and suggests optimization strategies for functions and algorithms"
```

### Issue: "Generated Skill Doesn't Meet Expectations"

**Solution**: Regenerate with additional clarification
```
Skill Maker can regenerate based on:
- "Please regenerate with support for JavaScript in addition to Python"
- "Modify the generated skill to include caching functionality"
```

### Issue: "Need to Modify Generated Skill"

**Solution**: Edit SKILL.md directly or request Skill Maker to modify
```
"Update the json-validator skill to also validate YAML files"
```

## Best Practices for Skill Requests

### DO:

✓ **Be Specific**: "Create a skill for extracting metadata from PDF documents"
✓ **Provide Context**: "This skill should integrate with our document processing workflow"
✓ **Include Examples**: "The skill should handle PDFs with scanned images"
✓ **Mention Constraints**: "Must work offline without external APIs"
✓ **Reference Standards**: "Follow the CLAUDE.md standards for academic tone"

### DON'T:

✗ **Be Vague**: "Create a general utility skill"
✗ **Scope Creep**: "Create a skill that does everything with documents"
✗ **Skip Details**: Assuming Skill Maker knows what you need
✗ **Request Non-Skills**: "Create a full application" (use Task tool instead)
✗ **Ignore Feedback**: Dismissing clarifying questions as unnecessary

## Integration with Project Structure

Generated skills integrate with your project:

### Cross-Directory References

**In SKILL.md**, reference related materials:

```markdown
## Related Materials

- **Notes**: Detailed explanations in `/notes/json-schema-validation.md`
- **Flashcards**: Key concepts in `/flashcards/json-validation-flashcards.md`
- **Quizzes**: Knowledge assessment in `/quizes/json-validator-quiz.md`
```

### Directory Organization

```
Class-4/
├── notes/
│   └── json-schema-validation.md
├── flashcards/
│   └── json-validation-flashcards.md
├── quizes/
│   └── json-validator-quiz.md
├── .claude/
│   ├── CLAUDE.md
│   └── skills/
│       └── json-validator/
│           ├── SKILL.md
│           └── EXAMPLES.md
```

## Conclusion

The Skill Maker streamlines the creation of professional, standards-compliant Claude Code skills. By asking clarifying questions and validating requirements, it ensures every generated skill meets quality standards and integrates seamlessly with your project infrastructure.

For questions or feedback about Skill Maker, refer to the SKILL.md documentation or REQUIREMENTS_CHECKLIST.md for comprehensive guidelines.
