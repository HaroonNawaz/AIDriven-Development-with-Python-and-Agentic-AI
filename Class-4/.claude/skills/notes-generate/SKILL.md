---
name: notes-generate
description: Generate comprehensive study notes organized according to Bloom's Taxonomy methodology. Use when creating educational materials, generating study content from topics or reference files, and developing structured learning materials for foundational knowledge progression (Remember → Understand → Apply).
---

# Notes Generate

## Purpose

The Notes Generate skill automates the creation of comprehensive, pedagogically-structured study notes using Bloom's Taxonomy methodology. It transforms topic descriptions or reference materials into well-organized learning documents that progress through foundational cognitive levels, enabling systematic knowledge acquisition and deep comprehension.

## When to Use This Skill

Use the Notes Generate skill when:

- Creating comprehensive study materials from topic titles
- Converting reference documents into structured educational content
- Generating learning materials organized by cognitive complexity
- Developing materials that require foundational knowledge progression
- Creating content with explicit learning objectives
- Generating practice questions and comprehension checks
- Organizing educational content with prerequisite knowledge mapping
- Producing content suitable for self-study or classroom instruction

## Core Functionality

### Primary Capabilities

- **Bloom's Taxonomy Organization**: Structures content using foundational cognitive levels (Remember, Understand, Apply)
- **Multi-Format Input Processing**: Accepts topic titles or reference files in Markdown, Text, or PDF formats
- **Comprehensive Output Generation**: Creates four integrated note documents per topic
- **Learning Objectives Generation**: Automatically produces measurable learning outcomes
- **Cross-Reference Creation**: Links prerequisites and related concepts
- **Practice Question Generation**: Creates application-level comprehension assessments

### Supported Inputs

- **Topic Title**: Simple text description of subject matter
- **Markdown Reference**: Existing .md files containing reference material
- **Text Documents**: Plain text files with source material
- **PDF Documents**: Scanned or formatted PDF reference materials

### Expected Outputs

For each topic, the skill generates four integrated Markdown files:

1. **Complete Notes** (`[topic]-complete.md`): Comprehensive notes across all Bloom's levels with summaries and references
2. **Bloom's Hierarchy** (`[topic]-bloom-hierarchy.md`): Content organized by cognitive level with cross-level connections
3. **Learning Objectives** (`[topic]-learning-objectives.md`): Measurable outcomes for each Bloom's level
4. **Practice Questions** (`[topic]-practice-questions.md`): Recall, comprehension, and application assessments with solutions

## Requirements and Dependencies

### Required Tools

- **Read Tool**: For processing reference files (Markdown, Text, PDF)
- **Write Tool**: For creating generated note files
- **Bash Tool**: For directory creation and file organization

### Optional Dependencies

- Existing project `notes/` directory structure
- Related flashcard or quiz materials (for cross-referencing)

### File Format Support

**Primary Formats**:
- Markdown (.md) - Primary reference format with full support
- Text (.txt) - Plain text reference documents
- PDF (.pdf) - Document and scanned material processing

**Not Currently Supported** (available in future versions):
- Code files with syntax preservation
- Image processing and diagram integration
- Jupyter notebooks
- External API references

## Bloom's Taxonomy Framework

The Notes Generate skill implements the foundational three levels of Bloom's Taxonomy, specifically designed for comprehensive learning material creation.

### Remember Level
**Cognitive Objective**: Retrieve relevant knowledge from long-term memory

**Content Components**:
- Definitions of essential terminology
- Lists of key facts and information
- Fundamental concepts and principles
- Basic formulas and rules
- Important sequences and chronologies

**Output Characteristics**:
- Concise, factual presentation
- Bullet-point format for quick reference
- Clear terminology definitions
- Foundational building blocks for higher-order thinking

### Understand Level
**Cognitive Objective**: Determine the meaning of instructional messages

**Content Components**:
- Comprehensive explanations of concepts
- Descriptions of processes and procedures
- Comparisons and contrasts with related concepts
- Cause-and-effect relationships
- Interpretations of material and significance

**Output Characteristics**:
- Explanatory paragraphs with depth
- Why and how information matters
- Connections to foundational knowledge
- Clarification of misconceptions
- Real-world relevance and applications

### Apply Level
**Cognitive Objective**: Use information in a new situation

**Content Components**:
- Practical examples demonstrating concepts
- Real-world application scenarios
- Problem-solving approaches with step-by-step guidance
- Case studies relevant to the topic
- Practice problems with worked solutions

**Output Characteristics**:
- Concrete scenarios and examples
- Step-by-step application procedures
- Expected outcomes and results
- Multiple perspectives on application
- Connection to professional or academic contexts

## Output Structure and Organization

### Directory Organization

Generated notes are organized in topic-specific subdirectories under `notes/`:

```
notes/
├── [topic-name]/
│   ├── [topic-name]-complete.md
│   ├── [topic-name]-bloom-hierarchy.md
│   ├── [topic-name]-learning-objectives.md
│   └── [topic-name]-practice-questions.md
```

### File Naming Convention

All generated files follow consistent naming patterns:

- **Complete Notes**: `[topic-name]-complete.md`
- **Bloom's Hierarchy**: `[topic-name]-bloom-hierarchy.md`
- **Learning Objectives**: `[topic-name]-learning-objectives.md`
- **Practice Questions**: `[topic-name]-practice-questions.md`

**Naming Rules**:
- Lowercase letters only
- Hyphens separate words (no underscores)
- Descriptive topic names (maximum 32 characters)
- No special characters except hyphens

### Complete Notes Structure

The comprehensive notes document contains:

```markdown
# [Topic Name] - Comprehensive Notes

## Learning Objectives
[Students will understand and achieve these goals]

## Remember Level - Key Facts and Definitions
[Essential terminology and foundational facts]

## Understand Level - Explanations and Descriptions
[Comprehensive explanations with significance]

## Apply Level - Practical Applications
[Real-world examples and practical scenarios]

## Key Concepts and Terminology
[Definitions and explanations of critical terms]

## Summary and Takeaways
[Condensed review and main points]

## Prerequisites
[Knowledge required before studying]

## Related Concepts
[Topics that connect and build on this material]
```

### Bloom's Hierarchy Structure

The hierarchy document presents content organized by cognitive level with explicit connections:

```markdown
# Bloom's Taxonomy Hierarchy: [Topic]

## Remember Level
### Concepts to Know and Retrieve
- [Definition-based items]
- [Factual knowledge]

## Understand Level
### Concepts to Comprehend and Explain
- [Explanation-based items]
- [Relationship descriptions]

## Apply Level
### Concepts to Apply and Use
- [Example-based scenarios]
- [Application procedures]

## Cross-Level Connections
[How concepts relate across levels and build progressively]
```

### Learning Objectives Document

Measurable outcomes presented per Bloom's level:

```markdown
# Learning Objectives: [Topic]

## After Remember Level
Students will be able to:
- List [specific items or facts]
- Identify [specific concepts]
- Define [key terminology]

## After Understand Level
Students will be able to:
- Explain [concepts and relationships]
- Describe [processes or phenomena]
- Discuss [significance and implications]

## After Apply Level
Students will be able to:
- Solve [problems using learned knowledge]
- Demonstrate [practical application]
- Create [solutions or examples]

## Prerequisite Knowledge
[Knowledge essential before beginning this topic]
```

### Practice Questions Document

Assessment items organized by cognitive level:

```markdown
# Practice Questions: [Topic]

## Remember Level - Recall Questions
[Basic recall and recognition questions]

## Understand Level - Comprehension Questions
[Questions requiring explanation and description]

## Apply Level - Application Scenarios
[Problems requiring application of knowledge]

## Answer Guide
[Complete answers with explanations]

## Assessment Rubric
[Criteria for evaluating responses]
```

## Instructions

### Step 1: Determine Input Type

Identify whether you are providing:

- **Option A**: A topic title (simple text description)
- **Option B**: A reference file (existing document)

### Step 2: Provide Source Material

**For Topic Title Input**:
```
"I want notes on [Topic Name]"

Example: "I want notes on photosynthesis"
```

**For Reference File Input**:
```
"Generate notes from this reference file: [file path or content]"

Example: "Generate notes from this PDF about cellular biology"
```

### Step 3: Clarify Scope (if needed)

Provide additional context:
- Depth level (introductory, intermediate, advanced)
- Target audience (students, professionals, self-learners)
- Subject area (biology, chemistry, mathematics, etc.)
- Any specific aspects to emphasize or exclude

### Step 4: Review Generated Output

The skill generates four files in `notes/[topic-name]/`:
- Complete notes document
- Bloom's Taxonomy hierarchy
- Learning objectives
- Practice questions

### Step 5: Customize if Needed

Generated notes can be customized:
- Adjust depth or complexity
- Add or remove examples
- Expand specific sections
- Modify practice questions

## Best Practices

### For Topic Specification

- **Be Specific**: "Data structures in Python" rather than "Programming"
- **Provide Context**: Indicate academic level or professional context
- **Specify Scope**: Clarify what aspects are most important
- **Include Constraints**: Note any prerequisites or limitations

### For Reference Materials

- **Clear Organization**: Ensure reference materials are well-structured
- **Legible Format**: Use readable fonts and clear formatting
- **Focused Content**: Remove extraneous information before processing
- **Complete Information**: Ensure reference includes depth needed for all levels

### For Using Generated Notes

- **Progressive Learning**: Follow the Bloom's progression for optimal learning
- **Active Engagement**: Use practice questions to assess comprehension
- **Cross-Reference**: Link to related topics and prerequisites
- **Regular Review**: Use learning objectives as self-assessment checkpoints
- **Iterative Refinement**: Request regeneration if coverage is insufficient

## Examples

### Example 1: Topic-Based Note Generation

**Input Request**:
```
"Generate comprehensive notes on photosynthesis for high school biology students"
```

**Generated Output**:
- Location: `notes/photosynthesis/`
- Files: Four markdown documents covering the topic progression
- Content: From basic facts to practical applications
- Assessment: Practice questions aligned with learning objectives

**Usage**:
1. Student reviews learning objectives
2. Studies Remember level (terminology and facts)
3. Works through Understand level (explanations)
4. Completes Apply level (practice problems)
5. Assesses learning using practice questions

### Example 2: Reference File Processing

**Input Request**:
```
"Generate notes from the attached biology textbook chapter on cell division"
```

**Processing**:
- Skill extracts content from reference
- Organizes content by cognitive complexity
- Generates learning objectives from content
- Creates practice questions from examples

**Generated Output**:
- `notes/cell-division/cell-division-complete.md`
- `notes/cell-division/cell-division-bloom-hierarchy.md`
- `notes/cell-division/cell-division-learning-objectives.md`
- `notes/cell-division/cell-division-practice-questions.md`

### Example 3: Integration with Study Materials

**Generated Notes Workflow**:

```
notes/
├── data-structures/
│   ├── data-structures-complete.md
│   ├── data-structures-bloom-hierarchy.md
│   ├── data-structures-learning-objectives.md
│   └── data-structures-practice-questions.md
│
├── algorithms/
│   └── [similar structure]
│
└── complexity-analysis/
    └── [similar structure]

Cross-Reference in flashcards/:
├── data-structures-flashcards.md
│   └── References notes/data-structures/learning-objectives.md

Cross-Reference in quizes/:
├── data-structures-quiz.md
│   └── Uses questions from notes/data-structures/practice-questions.md
```

## Troubleshooting

### Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| **Notes lack depth** | Topic too broad or vague | Request regeneration with specific scope |
| **Missing examples** | Insufficient source material | Provide more detailed reference documents |
| **Incomplete coverage** | Topic complexity underestimated | Request expansion for specific Bloom's level |
| **Poor organization** | Unclear topic boundaries | Redefine topic scope more precisely |
| **Low-quality questions** | Reference material lacks examples | Supplement with better source materials |

### Request Regeneration

If generated notes need improvement:

```
"Regenerate notes on [topic] focusing more on [specific aspect]"

Example: "Regenerate notes on thermodynamics
         with more practical engineering applications"
```

### Customization Options

```
"Modify the [topic] notes to include more [element]"

Examples:
- "Include more real-world examples"
- "Expand the Apply level with more scenarios"
- "Simplify explanations for introductory level"
- "Add more complex applications for advanced students"
```

## Integration Points

### Project Directory Structure

Generated notes integrate seamlessly with the project organization:

```
Class-4/
├── notes/
│   └── [topic-name]/
│       └── [generated files]
├── flashcards/
│   └── Can reference learning objectives
├── quizes/
│   └── Can use practice questions
└── .claude/
    └── skills/
        ├── skill-maker/
        └── notes-generate/
```

### Related Skills and Tools

- **flashcard-generator** (future): Create spaced-repetition flashcards from learning objectives
- **quiz-generator** (future): Generate assessments from practice questions
- **skill-maker**: Use this skill to generate new skills
- **Project CLAUDE.md**: Maintains standards for all generated materials

### Cross-Reference Standards

Generated notes include:

- **Prerequisites Section**: Links to prerequisite topics
- **Related Concepts**: References to connected material
- **Summary Points**: Key takeaways for quick review
- **Learning Pathways**: Suggested sequence for topic progression

## Quality Standards

### Content Quality

✓ **Accuracy**: Information is factually correct and pedagogically sound
✓ **Clarity**: Explanations are clear and appropriate for target audience
✓ **Completeness**: Covers foundational knowledge at appropriate depth
✓ **Consistency**: Maintains consistent formatting and terminology
✓ **Relevance**: Examples and applications are meaningful and current

### Documentation Standards

✓ **Professional Tone**: Academic and formal language throughout
✓ **Structure**: Clear hierarchical organization with appropriate headers
✓ **Examples**: Concrete examples for each Bloom's level
✓ **Formatting**: Proper Markdown with consistent style
✓ **References**: Clear citations and source attributions

### Organization Standards

✓ **Directory Structure**: Topic-organized subdirectories under `notes/`
✓ **Naming Conventions**: Hyphenated lowercase following CLAUDE.md
✓ **File Organization**: Four complementary files per topic
✓ **Integration**: Seamless integration with project structure
✓ **Accessibility**: Clear, organized, easy to navigate

## Standards Compliance

This skill adheres to:

- **Claude Code Official Documentation Standards**: https://code.claude.com/docs/en/skills
- **Project CLAUDE.md Standards**: Professional tone, clear documentation, file organization
- **Educational Standards**: Bloom's Taxonomy methodology correctly implemented
- **Quality Standards**: Comprehensive, well-organized, accessible content

---

## Instructions for Using Notes Generate

1. **Describe Your Topic** - Provide a topic title or reference material
2. **Specify Scope** - Indicate depth, audience, and any special requirements
3. **Receive Generated Notes** - Four complementary Markdown files organized in topic subdirectory
4. **Use in Learning** - Follow Bloom's progression for optimal comprehension
5. **Customize as Needed** - Request modifications or regeneration

The Notes Generate skill transforms topic descriptions into structured, pedagogically-sound study materials that support progressive knowledge acquisition.

---

## Version History

### Version 1.0 (December 2024)
- **Initial Release**: Complete implementation of Bloom's Taxonomy-based note generation
- **Features**:
  - Three foundational Bloom's levels (Remember, Understand, Apply)
  - Multi-format input processing (Topic title, MD, TXT, PDF)
  - Four-document output structure per topic
  - Learning objectives and practice questions generation
  - Prerequisite and cross-reference mapping
  - Topic-organized file structure
  - Full CLAUDE.md and Claude Code standards compliance

---

**Status**: Production Ready
**Last Updated**: December 2024
**Maintainer**: Claude Code
