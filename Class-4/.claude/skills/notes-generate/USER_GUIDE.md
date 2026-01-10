---
# Notes Generate - User Guide

Comprehensive guide to using the Notes Generate skill for creating Bloom's Taxonomy-organized study materials.

---

## Quick Start

### Three Simple Steps

**Step 1: Invoke Notes Generate**
```
"Generate comprehensive notes on [topic name]"

Example: "Generate comprehensive notes on the water cycle"
```

**Step 2: Receive Four Generated Files**
```
notes/[topic-name]/
├── [topic-name]-complete.md
├── [topic-name]-bloom-hierarchy.md
├── [topic-name]-learning-objectives.md
└── [topic-name]-practice-questions.md
```

**Step 3: Use Your Notes**
```
1. Review learning objectives
2. Study Remember level (facts and definitions)
3. Study Understand level (explanations)
4. Complete Apply level (practical examples)
5. Answer practice questions
```

---

## How Notes Generate Works

### The Complete Process

#### Phase 1: Input Analysis
- Analyzes topic title or reference material
- Determines scope and depth needed
- Identifies key concepts and relationships

#### Phase 2: Content Organization
- Structures content by Bloom's cognitive levels
- Organizes from Remember → Understand → Apply progression
- Creates connections between levels

#### Phase 3: Output Generation
- Generates four complementary documents
- Creates learning objectives for each level
- Develops practice assessments
- Establishes prerequisite mapping

#### Phase 4: Quality Assurance
- Verifies Bloom's Taxonomy compliance
- Ensures professional documentation standards
- Validates file organization
- Confirms CLAUDE.md alignment

---

## Understanding Bloom's Taxonomy Levels

### Remember Level (Foundation)
**Question**: What do students need to know first?

**Content**:
- Definitions of key terms
- Lists of important facts
- Basic formulas and rules
- Fundamental concepts

**Example**:
```markdown
## Remember Level - Key Facts

**Term**: Photosynthesis
**Definition**: Process by which plants convert light energy
into chemical energy stored in glucose

**Key Facts**:
- Occurs primarily in plant leaves
- Requires sunlight, water, and carbon dioxide
- Produces glucose and oxygen
```

**How to Learn**:
- Study definitions and key facts
- Create flashcards for terminology
- Memorize fundamental concepts
- Build foundation knowledge

### Understand Level (Comprehension)
**Question**: Can students explain why and how?

**Content**:
- Explanations of concepts
- Descriptions of processes
- Comparisons and contrasts
- Cause-and-effect relationships

**Example**:
```markdown
## Understand Level - Explanations

**Why Photosynthesis Matters**:
Photosynthesis is the fundamental process that converts
solar energy into biochemical energy, which powers
nearly all life on Earth...

**How It Connects**:
This process is directly related to:
- The carbon cycle (CO2 absorption and O2 release)
- Energy flow in ecosystems
- Plant nutrition and growth
```

**How to Learn**:
- Read explanatory paragraphs carefully
- Ask "Why?" and "How?" questions
- Draw concept maps showing relationships
- Explain concepts in your own words

### Apply Level (Application)
**Question**: Can students use this knowledge in new situations?

**Content**:
- Practical examples demonstrating concepts
- Real-world application scenarios
- Problem-solving approaches
- Case studies and practical problems

**Example**:
```markdown
## Apply Level - Practical Applications

**Scenario 1: Optimizing Plant Growth**
**Challenge**: A farmer wants to increase crop yield

**How to Apply**:
1. Analyze light availability in the field
2. Determine water and nutrient needs
3. Create optimal conditions for photosynthesis
4. Monitor and adjust as needed

**Expected Result**: Increased glucose production
leading to healthier plants and better harvest
```

**How to Learn**:
- Work through practical examples
- Solve application problems
- Create your own scenarios
- Practice with different contexts

---

## Input Methods

### Method 1: Topic Title Only

**Most Straightforward Approach**

```
"Generate comprehensive notes on [topic name]"
```

**Examples**:
```
- "Generate comprehensive notes on mitochondria"
- "Generate comprehensive notes on quadratic equations"
- "Generate comprehensive notes on the American Civil War"
```

**Best For**:
- Well-defined topics
- Broad subject areas
- When you want comprehensive coverage
- Standard academic topics

**What Happens**:
1. Notes Generate understands your topic
2. Creates structured content covering all Bloom's levels
3. Generates all four documents
4. Places them in `notes/[topic-name]/` directory

### Method 2: With Reference File

**Content-Based Approach**

```
"Generate notes from this reference: [file content or path]"
```

**Example**:
```
"Generate notes based on this chapter about cellular respiration"
[paste chapter text]
```

**Supported Formats**:
- Markdown (.md) files
- Plain text (.txt) files
- PDF documents

**Best For**:
- Extracting from existing materials
- Converting textbooks to study guides
- Processing lecture notes
- Organizing scattered information

**What Happens**:
1. Notes Generate reads your reference material
2. Extracts key concepts and relationships
3. Reorganizes into Bloom's Taxonomy structure
4. Generates comprehensive notes

### Method 3: Topic with Specifications

**Customized Approach**

```
"Generate notes on [topic] for [audience] covering [specific aspects]"
```

**Examples**:
```
- "Generate notes on photosynthesis for high school students
   focusing on the light-dependent reactions"

- "Generate notes on project management for professionals,
   emphasizing real-world application examples"

- "Generate notes on quantum mechanics for undergraduate physics,
   starting from basic concepts and building complexity"
```

**Specification Options**:
- **Audience**: High school, undergraduate, graduate, professional
- **Depth**: Introductory, intermediate, advanced
- **Focus**: Specific aspects or applications to emphasize
- **Context**: Academic, professional, personal interest

---

## Output Structure Explained

### Generated File 1: Complete Notes

**Filename**: `[topic-name]-complete.md`

**Purpose**: Comprehensive reference document with all elements

**Contains**:
1. Learning objectives (what you'll achieve)
2. Remember level (facts and definitions)
3. Understand level (explanations and connections)
4. Apply level (practical examples)
5. Key concepts (terminology reference)
6. Summary and takeaways (quick review)
7. Prerequisites (knowledge needed)
8. Related concepts (topic connections)

**How to Use**:
- Primary study document
- Reference for comprehensive understanding
- Source for creating flashcards
- Foundation for practice questions

**Example Structure**:
```markdown
# Photosynthesis - Comprehensive Notes

## Learning Objectives
Students will understand the process of photosynthesis
and be able to explain how it converts light energy...

## Remember Level - Key Facts and Definitions
[Definitions and facts]

## Understand Level - Explanations
[Comprehensive explanations]

## Apply Level - Practical Applications
[Real-world examples]

[Additional sections...]
```

### Generated File 2: Bloom's Hierarchy

**Filename**: `[topic-name]-bloom-hierarchy.md`

**Purpose**: Content organized explicitly by cognitive level

**Contains**:
1. Remember level concepts
2. Understand level concepts
3. Apply level concepts
4. Cross-level connections showing how levels relate

**How to Use**:
- Understand cognitive progression
- Track learning as you progress through levels
- See how concepts build on each other
- Navigate by cognitive complexity

**Example Structure**:
```markdown
# Bloom's Taxonomy Hierarchy: Photosynthesis

## Remember Level
### Concepts to Know
- Definition of photosynthesis
- Key raw materials
- Key products

## Understand Level
### Concepts to Comprehend
- How light energy is captured
- Why water is essential
- How chlorophyll functions

## Apply Level
### Concepts to Apply
- Optimizing growth conditions
- Predicting effects of changes
- Solving plant health problems

## Cross-Level Connections
[How concepts relate across levels]
```

### Generated File 3: Learning Objectives

**Filename**: `[topic-name]-learning-objectives.md`

**Purpose**: Measurable outcomes at each Bloom's level

**Contains**:
1. Remember level objectives (what you'll memorize)
2. Understand level objectives (what you'll explain)
3. Apply level objectives (what you'll do)
4. Prerequisite knowledge needed
5. Self-assessment checkpoints

**How to Use**:
- Check what you need to learn before starting
- Verify learning after each section
- Self-assessment of understanding
- Track progress through the material

**Example**:
```markdown
# Learning Objectives: Photosynthesis

## After Remember Level
Students will be able to:
- List the raw materials needed for photosynthesis
- Define key terms (photosynthesis, chlorophyll, glucose)
- Identify where photosynthesis occurs in plants

## After Understand Level
Students will be able to:
- Explain how light energy is converted to chemical energy
- Describe the role of each component
- Connect photosynthesis to plant growth

## After Apply Level
Students will be able to:
- Predict effects of changing light conditions
- Design experiments to test photosynthesis
- Solve real-world plant problems
```

### Generated File 4: Practice Questions

**Filename**: `[topic-name]-practice-questions.md`

**Purpose**: Assessment items organized by cognitive level

**Contains**:
1. Remember level questions (recall and recognition)
2. Understand level questions (comprehension and explanation)
3. Apply level questions (problem-solving and scenarios)
4. Complete answer guide with explanations
5. Assessment rubric

**How to Use**:
- Test your knowledge at each level
- Identify gaps in understanding
- Practice before assessments
- Review with provided answers

**Example**:
```markdown
# Practice Questions: Photosynthesis

## Remember Level - Recall Questions
1. What are the two main products of photosynthesis?
2. Define photosynthesis in one sentence
3. List the three raw materials needed

## Understand Level - Comprehension Questions
1. Explain why plants need light for photosynthesis
2. Describe how chlorophyll captures light energy
3. What would happen if a plant had no chlorophyll?

## Apply Level - Application Scenarios
1. A farmer wants to increase crop yield. What changes
   could they make to optimize photosynthesis?
2. Design an experiment to test how light intensity
   affects the rate of photosynthesis

## Answer Guide
[Complete answers with detailed explanations]
```

---

## File Organization

### Directory Structure

All generated notes are organized in topic-specific subdirectories:

```
notes/
├── photosynthesis/
│   ├── photosynthesis-complete.md
│   ├── photosynthesis-bloom-hierarchy.md
│   ├── photosynthesis-learning-objectives.md
│   └── photosynthesis-practice-questions.md
│
├── cellular-respiration/
│   ├── cellular-respiration-complete.md
│   ├── cellular-respiration-bloom-hierarchy.md
│   ├── cellular-respiration-learning-objectives.md
│   └── cellular-respiration-practice-questions.md
│
└── [additional topics]/
    └── [similar structure]
```

### Naming Convention

All files follow consistent naming patterns:

**Rules**:
- Lowercase letters only
- Hyphens separate words (no underscores or spaces)
- Topic name is descriptive and concise
- Suffix indicates document type
- Maximum 32 characters for topic name

**Examples**:
```
✓ photosynthesis-complete.md
✓ cell-division-learning-objectives.md
✓ quadratic-equations-practice-questions.md

✗ Photosynthesis.md (capital P)
✗ photosynthesis_complete.md (underscore)
✗ photosynthesis and cellular respiration.md (spaces)
```

---

## Best Practices for Using Generated Notes

### Study Progression

**Recommended Learning Path**:

1. **Review Learning Objectives First** (5-10 minutes)
   - Understand what you need to learn
   - Set learning goals
   - Check prerequisites

2. **Study Remember Level** (15-20 minutes)
   - Learn definitions and key facts
   - Create flashcards for terminology
   - Build foundational knowledge

3. **Study Understand Level** (20-30 minutes)
   - Read explanations carefully
   - Ask "why" and "how" questions
   - Create concept maps
   - Explain in your own words

4. **Study Apply Level** (15-25 minutes)
   - Work through practical examples
   - Practice problem-solving
   - Create your own scenarios
   - Connect to real-world contexts

5. **Answer Practice Questions** (20-30 minutes)
   - Test at each Bloom's level
   - Check answers with guide
   - Identify weak areas
   - Re-study as needed

6. **Review and Consolidate** (10-15 minutes)
   - Review summary points
   - Use Bloom's hierarchy for overview
   - Prepare for assessments

### Effective Study Techniques

**For Remember Level**:
- Create flashcards from definitions
- Make lists of key facts
- Use mnemonics for sequences
- Repeat and memorize

**For Understand Level**:
- Draw concept maps
- Write explanations in your own words
- Create comparison charts
- Discuss concepts with others
- Connect to previous knowledge

**For Apply Level**:
- Work through examples step-by-step
- Solve practice problems
- Create new scenarios
- Teach others the concept
- Find real-world applications

### Integration with Other Study Materials

**With Flashcards**:
- Create flashcards from Remember level facts
- Use learning objectives for question creation
- Focus flashcards on Remember and Understand levels

**With Quizzes**:
- Use practice questions from the notes
- Create quizzes from learning objectives
- Include Apply level problems in assessments

**With Related Topics**:
- Use prerequisite sections to guide learning order
- Follow topic connections for deeper understanding
- Link related notes in your organization system

---

## Customization and Modification

### Request Regeneration

If you need different notes:

```
"Regenerate notes on [topic] with [specific change]"

Examples:
- "Regenerate notes on photosynthesis for advanced students
   including the light-independent reactions"

- "Regenerate notes on the French Revolution focusing more
   on social and economic causes"

- "Regenerate notes on Python functions with more
   programming examples"
```

### Request Modifications

To modify existing notes:

```
"Modify the [topic] notes to [specific request]"

Examples:
- "Add more real-world examples to the Apply level"
- "Simplify the Understand level explanations"
- "Include more practice problems"
- "Expand the Prerequisites section"
```

### Request Additional Content

For supplementary material:

```
"Create [additional content] for the [topic] notes"

Examples:
- "Create a visual summary diagram for photosynthesis"
- "Create advanced practice problems for calculus"
- "Create real-world case studies for economics"
```

---

## Troubleshooting

### Issue: Notes Are Too Basic or Too Advanced

**Solution**:
```
"Regenerate notes on [topic] at [level] for [audience]"

Example: "Regenerate notes on genetics at intermediate level
         for high school students"
```

### Issue: Missing Examples or Applications

**Solution**:
```
"Regenerate notes on [topic] with more [type] examples"

Example: "Regenerate notes on quadratic equations with more
         engineering application examples"
```

### Issue: Insufficient Depth or Coverage

**Solution**:
```
"Expand the [specific section] of [topic] notes with more detail"

Example: "Expand the Understand level of cell division notes
         with more detailed process descriptions"
```

### Issue: Different Focus Needed

**Solution**:
```
"Regenerate notes on [topic] emphasizing [specific aspect]"

Example: "Regenerate notes on World War II emphasizing the
         Pacific theater and Pacific campaign strategies"
```

---

## Integration with Project Structure

### Directory Organization

Notes generated by Notes Generate integrate seamlessly with your project:

```
Class-4/
├── .claude/
│   └── skills/
│       ├── skill-maker/
│       └── notes-generate/
├── notes/
│   └── [topic-name]/
│       └── [4 generated files]
├── flashcards/
│   └── [can reference learning objectives]
└── quizes/
    └── [can use practice questions]
```

### Cross-Referencing

Link notes to other materials:

**In flashcards/[topic]-flashcards.md**:
```markdown
## Concept Definitions
[Reference: See notes/[topic]/[topic]-learning-objectives.md]
```

**In quizes/[topic]-quiz.md**:
```markdown
## Practice Problems
[Based on: notes/[topic]/[topic]-practice-questions.md]
```

---

## Example Workflows

### Workflow 1: Complete Self-Study

```
1. Invoke: "Generate comprehensive notes on DNA replication"
2. Receive: Four markdown files in notes/dna-replication/
3. Review: Learning objectives (understand goals)
4. Study: Remember level (1st pass)
5. Study: Understand level (2nd pass)
6. Practice: Apply level (3rd pass)
7. Assess: Practice questions (final check)
8. Create: Flashcards from Remember/Understand levels
9. Prepare: For assessments using all four files
```

### Workflow 2: Reference Material Conversion

```
1. Invoke: "Generate notes from this biology textbook chapter"
2. Provide: Chapter text or PDF
3. Receive: Four organized documents
4. Extract: Key concepts from each level
5. Create: Study guide from complete notes
6. Generate: Quiz from practice questions (future feature)
7. Review: Learning objectives for mastery checks
```

### Workflow 3: Multi-Topic Course

```
1. Generate notes for each course topic
2. Organize in notes/ with topic subdirectories
3. Create learning path using prerequisites
4. Study in logical progression
5. Use learning objectives to track progress
6. Answer practice questions for each topic
7. Integrate with project-wide assessments
```

---

## Summary

The Notes Generate skill transforms topics into comprehensive, pedagogically-sound study materials organized by Bloom's Taxonomy. By following the three-level cognitive progression (Remember → Understand → Apply), you can build deep knowledge and develop practical competency in any subject area.

**Key Takeaways**:
- Simple input (topic title or reference file)
- Comprehensive output (four complementary documents)
- Pedagogically sound structure (Bloom's Taxonomy)
- Easy integration (notes/ directory organization)
- Flexible customization (regenerate or modify)

Start generating notes today and build your comprehensive study library!

---

**Last Updated**: December 2024
**Status**: Production Ready
