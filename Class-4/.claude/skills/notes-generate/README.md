---
# Notes Generate Skill - Complete Documentation Index

Quick navigation guide to all notes-generate skill documentation.

---

## Overview

**Skill Name**: `notes-generate`
**Purpose**: Generate comprehensive study notes organized according to Bloom's Taxonomy methodology
**Status**: Production Ready
**Version**: 1.0

---

## Quick Navigation

### For Users Getting Started
- **[USER_GUIDE.md](USER_GUIDE.md)** - Complete user guide with examples and best practices
  - Quick start (3 steps)
  - How the skill works
  - Understanding Bloom's Taxonomy levels
  - Input methods and options
  - Output structure explained
  - Best practices for studying
  - Customization options
  - Troubleshooting guide

### For Skill Implementation
- **[SKILL.md](SKILL.md)** - Official skill definition and specifications
  - Purpose and when to use
  - Core functionality
  - Bloom's Taxonomy framework (three levels)
  - Output structure and organization
  - Instructions for using the skill
  - Best practices
  - Examples
  - Integration points

### For Developers and Reference
- **[REQUIREMENTS_CHECKLIST.md](REQUIREMENTS_CHECKLIST.md)** - Quality assurance and validation
  - Seven-phase validation process
  - Requirements verification
  - Standards compliance
  - Quality metrics
  - Approval checklist

### For Template Reference
- **[SKILL_TEMPLATE.md](SKILL_TEMPLATE.md)** - Complete template for generated notes
  - Complete notes structure
  - Bloom's hierarchy template
  - Learning objectives template
  - Practice questions template
  - Key features and usage notes

---

## File Organization

```
notes-generate/
├── README.md (this file)
│   └── Navigation and overview
│
├── SKILL.md
│   ├── Official skill definition
│   ├── Purpose and use cases
│   ├── Core functionality
│   ├── Bloom's Taxonomy implementation
│   ├── Output structure
│   ├── Instructions
│   ├── Best practices
│   └── Examples
│
├── USER_GUIDE.md
│   ├── Quick start (3 steps)
│   ├── How Notes Generate works
│   ├── Understanding Bloom's Taxonomy
│   ├── Input methods explained
│   ├── Output structure explained
│   ├── Best practices for studying
│   ├── Customization and modification
│   ├── Troubleshooting
│   ├── Integration with project
│   └── Example workflows
│
├── REQUIREMENTS_CHECKLIST.md
│   ├── Phase 1: Requirement Analysis
│   ├── Phase 2: Scope & Constraints
│   ├── Phase 3: Tool Requirements
│   ├── Phase 4: Documentation
│   ├── Phase 5: Integration
│   ├── Phase 6: Security & Performance
│   ├── Phase 7: Quality Assurance
│   └── Approval Checklist
│
└── SKILL_TEMPLATE.md
    ├── Complete notes template
    ├── Bloom's hierarchy template
    ├── Learning objectives template
    ├── Practice questions template
    └── Template features and usage
```

---

## Key Features

### Feature 1: Bloom's Taxonomy Organization
- Structures content using three foundational cognitive levels
- Progression: Remember → Understand → Apply
- Pedagogically sound learning pathway
- Builds foundational knowledge systematically

### Feature 2: Multi-Format Input
- Accept topic titles (simple text)
- Process reference files (Markdown, Text, PDF)
- Flexible input options for various scenarios
- Works with any subject area

### Feature 3: Comprehensive Output
- Four complementary documents per topic
- Complete notes with all elements
- Bloom's hierarchy breakdown
- Learning objectives for each level
- Practice questions with answers

### Feature 4: Automatic Generation
- Learning objectives creation
- Key concepts extraction
- Summary points generation
- Practice question development
- Prerequisite mapping

### Feature 5: Seamless Integration
- Topic-organized directory structure
- Consistent file naming conventions
- Integrates with project organization
- Compatible with CLAUDE.md standards

---

## How to Use Notes Generate

### Quick Start (3 Steps)

**Step 1: Invoke Skill**
```
"Generate comprehensive notes on [topic name]"
```

**Step 2: Receive Output**
```
notes/[topic-name]/
├── [topic]-complete.md
├── [topic]-bloom-hierarchy.md
├── [topic]-learning-objectives.md
└── [topic]-practice-questions.md
```

**Step 3: Start Learning**
- Review learning objectives
- Study Remember level
- Study Understand level
- Practice Apply level
- Answer practice questions

---

## Understanding Bloom's Taxonomy Levels

### Three Foundational Levels

#### Remember Level
**Goal**: Retrieve relevant knowledge from memory

**Content**:
- Definitions of key terms
- Lists of important facts
- Basic formulas and rules
- Fundamental concepts

#### Understand Level
**Goal**: Determine the meaning of concepts

**Content**:
- Explanations with examples
- Descriptions of processes
- Cause-and-effect relationships
- Comparisons and contrasts

#### Apply Level
**Goal**: Use information in new situations

**Content**:
- Practical examples
- Real-world scenarios
- Problem-solving approaches
- Case studies and applications

---

## Generated Output Examples

### Example 1: Photosynthesis

```
notes/photosynthesis/
├── photosynthesis-complete.md
│   (Learning objectives, 3 Bloom's levels, summaries)
│
├── photosynthesis-bloom-hierarchy.md
│   (Concepts organized by cognitive level)
│
├── photosynthesis-learning-objectives.md
│   (Measurable outcomes for each level)
│
└── photosynthesis-practice-questions.md
    (Assessment items with answers)
```

### Example 2: Data Structures

```
notes/data-structures/
├── data-structures-complete.md
├── data-structures-bloom-hierarchy.md
├── data-structures-learning-objectives.md
└── data-structures-practice-questions.md
```

---

## Project Integration

### Directory Structure

```
Class-4/
├── .claude/
│   └── skills/
│       ├── skill-maker/
│       │   └── [skill-maker files]
│       └── notes-generate/
│           └── [notes-generate files]
│
├── notes/
│   └── [topic-name]/
│       └── [generated files]
│
├── flashcards/
│   └── [future integration]
│
└── quizes/
    └── [future integration]
```

### Cross-References

Generated notes integrate with:
- **flashcards/**: Reference learning objectives
- **quizes/**: Use practice questions
- **skill-maker**: Generate this and other skills
- **CLAUDE.md**: Follow project standards

---

## Standards Compliance

### Claude Code Official Documentation
✓ Skill structure: Directory with SKILL.md
✓ File format: YAML frontmatter + Markdown
✓ Naming convention: `notes-generate` (valid)
✓ YAML frontmatter: name + description present

### Project CLAUDE.md Standards
✓ Professional and academic tone throughout
✓ Clear, hierarchical documentation
✓ Proper file organization
✓ Consistent naming conventions
✓ High quality standards

### Educational Standards
✓ Bloom's Taxonomy correctly implemented
✓ Three foundational cognitive levels
✓ Pedagogically sound structure
✓ Learning objectives aligned with levels
✓ Assessment items properly categorized

---

## Best Practices

### For Using Generated Notes

1. **Review Learning Objectives First**
   - Understand what you're learning
   - Check prerequisites
   - Set goals

2. **Progress Through Bloom's Levels**
   - Remember: Learn facts and definitions
   - Understand: Learn explanations and connections
   - Apply: Practice real-world applications

3. **Use All Four Documents**
   - Complete notes: Comprehensive reference
   - Bloom's hierarchy: Cognitive organization
   - Learning objectives: Self-assessment
   - Practice questions: Comprehension checks

4. **Integrate with Study Materials**
   - Create flashcards from Remember level
   - Use learning objectives for quizzes
   - Reference practice questions for exams

5. **Customize as Needed**
   - Request regeneration for different depth
   - Add more examples if needed
   - Modify for specific audience

---

## Quick Reference

### Most Common Tasks

| Task | How to Do It |
|------|------------|
| **Create notes on a topic** | "Generate comprehensive notes on [topic]" |
| **Convert document to notes** | "Generate notes from this reference: [file]" |
| **Get different depth/focus** | "Regenerate notes on [topic] for [audience]" |
| **Add more examples** | "Add more [type] examples to [topic] notes" |
| **Find learning objectives** | Check `[topic]-learning-objectives.md` |
| **Practice your knowledge** | Answer questions in `[topic]-practice-questions.md` |

---

## Common Use Cases

### Workflow 1: Self-Study
1. Generate notes on topic
2. Review learning objectives
3. Study Remember level
4. Study Understand level
5. Practice Apply level
6. Answer practice questions
7. Self-assess using learning objectives

### Workflow 2: Course Material
1. Generate notes from textbook chapter
2. Create study guide
3. Use practice questions for assignments
4. Reference in studying for exams

### Workflow 3: Professional Development
1. Generate notes on professional topic
2. Study to build competency
3. Apply learning in work context
4. Track progress with learning objectives

---

## Support and Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **Notes too basic** | Request regeneration for higher level |
| **Missing examples** | Provide more detailed reference material |
| **Wrong focus** | Request regeneration with specific focus |
| **Need more depth** | Request expansion of specific sections |

### Getting Help

1. **For quick start**: Read USER_GUIDE.md
2. **For process details**: Review SKILL.md
3. **For quality standards**: Check REQUIREMENTS_CHECKLIST.md
4. **For examples**: Use SKILL_TEMPLATE.md

### Request Regeneration

```
"Regenerate notes on [topic] [specific request]"

Examples:
- "for advanced students"
- "with more engineering applications"
- "focusing on the mathematical approach"
```

---

## File Descriptions

### SKILL.md
**Size**: ~6 KB
**Purpose**: Official skill documentation and specifications
**Contains**: Purpose, functionality, Bloom's framework, instructions, examples, integration
**Best for**: Understanding what the skill does and how it works

### USER_GUIDE.md
**Size**: ~12 KB
**Purpose**: User-focused comprehensive guide
**Contains**: Quick start, how it works, Bloom's explanation, usage, best practices, workflows
**Best for**: Learning how to use the skill effectively

### REQUIREMENTS_CHECKLIST.md
**Size**: ~10 KB
**Purpose**: Quality assurance and validation criteria
**Contains**: Seven-phase validation, requirements verification, quality metrics
**Best for**: Understanding quality standards and validation process

### SKILL_TEMPLATE.md
**Size**: ~15 KB
**Purpose**: Complete template for generated notes
**Contains**: All four document templates with full structure
**Best for**: Understanding output format and using as template for customization

### README.md
**Size**: ~6 KB (this file)
**Purpose**: Navigation and overview
**Contains**: Quick links, feature summaries, integration information
**Best for**: Finding the right documentation for your needs

---

## Version Information

**Skill Name**: notes-generate
**Version**: 1.0
**Status**: Production Ready
**Last Updated**: December 2024
**Standards**: Claude Code + Project CLAUDE.md

---

## Quick Summary

The Notes Generate skill transforms topics into comprehensive, pedagogically-structured study materials using Bloom's Taxonomy. With simple input (topic or reference file), it generates four integrated documents supporting progressive learning from foundational facts through practical applications.

**Key Points**:
- Three Bloom's cognitive levels (Remember, Understand, Apply)
- Four complementary documents per topic
- Topic-organized file structure
- Professional documentation standards
- Complete integration with project

---

## Next Steps

1. **Read USER_GUIDE.md** (10 minutes) - Get started quickly
2. **Review SKILL.md** (15 minutes) - Understand in detail
3. **Invoke the skill** with your first topic
4. **Review generated notes** in notes/[topic]/
5. **Follow the learning path** through Bloom's levels

---

**Start generating notes today!**

For detailed guidance, consult the appropriate documentation:
- **Getting Started**: USER_GUIDE.md
- **Technical Details**: SKILL.md
- **Quality Standards**: REQUIREMENTS_CHECKLIST.md
- **Output Examples**: SKILL_TEMPLATE.md
