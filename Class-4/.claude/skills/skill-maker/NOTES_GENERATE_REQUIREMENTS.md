# Notes-Generate Skill - Requirements Summary

## Skill Definition
**Skill Name**: `notes-generate`
**Purpose**: Generate comprehensive study notes organized according to Bloom's Taxonomy methodology
**Use Cases**: Educational content creation, study material generation, knowledge documentation

---

## Confirmed Requirements

### Priority 1: Core Functionality

#### Bloom's Taxonomy Coverage
✓ **Decision**: Foundational levels (Remember → Understand → Apply)
- Focus on basic learning progression
- Three primary cognitive levels
- Appropriate for comprehensive study material
- Foundation for advanced learners

**Implementation**:
- **Remember Level**: Definitions, key facts, fundamental concepts, terminology
- **Understand Level**: Explanations, descriptions, comprehension of concepts
- **Apply Level**: Examples, practice problems, practical applications, scenarios

#### File Format Support
✓ **Decision**: Markdown, Text, PDF
- Markdown (.md) - Primary format for notes creation
- Plain text (.txt) - Simple reference documents
- PDF - Scanned documents and reference materials
- Not including: Code files, images, Jupyter notebooks (can add later)

#### Content Structure
✓ **Decision**: Hybrid approach
- Structured paragraphs with explanations
- Practical examples for each concept
- Key takeaways and summary points
- Balanced depth and readability

**Structure per Bloom's Level**:
1. **Remember**: Bullet-point definitions and facts
2. **Understand**: Explanatory paragraphs with clarifications
3. **Apply**: Real-world examples and practice scenarios
4. **Summary**: Key concepts extraction across all levels

---

### Priority 2: Scope & Use Cases

#### Automatic Content Generation
✓ **Decision**: Fully featured package
- Summary points for quick review
- Key concepts and terminology definitions
- Learning objectives for each section
- Prerequisite knowledge requirements
- Cross-references and connections

**Auto-Generated Components**:
1. **Learning Objectives**: What students should know/do after each section
2. **Key Concepts**: Important terms with definitions
3. **Summary Points**: Condensed takeaways from each section
4. **Prerequisites**: Knowledge needed before studying each section
5. **Practice Questions**: Application-level comprehension checks

#### Cross-References and Context
✓ **Decision**: Basic references
- Include prerequisite knowledge sections
- Link to related concepts
- Reference connections between concepts
- Not including: External URLs, external resource links (can add later)

**Included Elements**:
- Prerequisites: "Before studying this, ensure you understand..."
- Related Concepts: "This builds on... and connects to..."
- Concept Flow: How topics relate within the document

---

### Priority 3: Tool Requirements

#### Directory Integration and Organization
✓ **Decision**: Topic-organized subdirectories under notes/
- Create subdirectory per topic under `notes/`
- Organize all related materials together
- Maintain project structure and conventions

**Directory Structure**:
```
notes/
├── [topic-name]/
│   ├── [topic-name]-complete.md
│   ├── [topic-name]-bloom-hierarchy.md
│   ├── [topic-name]-learning-objectives.md
│   └── [topic-name]-practice-questions.md
```

#### File Naming Conventions
✓ **Decision**: Topic-based with descriptive suffixes
- Main file: `[topic-name]-complete.md`
- Hierarchy breakdown: `[topic-name]-bloom-hierarchy.md`
- Learning objectives: `[topic-name]-learning-objectives.md`
- Practice content: `[topic-name]-practice-questions.md`
- Hyphenated lowercase (CLAUDE.md compliance)

---

## Implementation Specifications

### Input Requirements

**Option 1: Topic Title Only**
- User provides: Topic or subject name
- Skill generates: Complete notes from knowledge base
- Output: Full structured notes following Bloom's Taxonomy

**Option 2: Reference File Provided**
- User provides: Reference file (MD, TXT, or PDF)
- Skill generates: Notes based on reference content
- Output: Extracted and reorganized content in Bloom's structure

### Output Structure

Each generated note package includes:

#### 1. **Complete Notes** (main-complete.md)
```markdown
# [Topic Name] - Comprehensive Notes

## Learning Objectives
[What students will learn]

## Remember Level
[Definitions, facts, key terms]

## Understand Level
[Explanations and descriptions]

## Apply Level
[Examples and practical applications]

## Key Concepts
[Terminology and definitions]

## Summary and Takeaways
[Condensed review material]

## Prerequisites
[Knowledge needed before studying]

## Related Concepts
[Connections to other topics]
```

#### 2. **Bloom's Hierarchy** (bloom-hierarchy.md)
```markdown
# Bloom's Taxonomy Hierarchy: [Topic]

## Remember Level
### Concepts to Know
- [Definition-based items]

## Understand Level
### Concepts to Comprehend
- [Explanation-based items]

## Apply Level
### Concepts to Apply
- [Example-based scenarios]

## Cross-Level Connections
[How levels relate to each other]
```

#### 3. **Learning Objectives** (learning-objectives.md)
```markdown
# Learning Objectives: [Topic]

## After Remember Level
- Students will be able to list...
- Students will be able to identify...

## After Understand Level
- Students will be able to explain...
- Students will be able to describe...

## After Apply Level
- Students will be able to solve...
- Students will be able to demonstrate...
```

#### 4. **Practice Questions** (practice-questions.md)
```markdown
# Practice Questions: [Topic]

## Remember Level Questions
[Recall-based questions]

## Understand Level Questions
[Comprehension-based questions]

## Apply Level Questions
[Application-based scenarios]

## Answer Guide
[Explanations and correct answers]
```

---

## Bloom's Taxonomy Implementation Details

### Remember Level
**Cognitive Goal**: Retrieve relevant knowledge from memory
**Content Types**:
- Definitions of key terms
- Lists of facts
- Basic formulas or rules
- Fundamental concepts
- Important dates or sequences

**Example Output Format**:
```markdown
## Remember Level - Key Facts

**Term**: [Definition]
**Fact**: [Statement]
**Concept**: [Basic principle]
```

### Understand Level
**Cognitive Goal**: Determine the meaning of concepts
**Content Types**:
- Explanations with examples
- Comparisons and contrasts
- Cause-and-effect relationships
- Descriptions of processes
- Interpretations of material

**Example Output Format**:
```markdown
## Understand Level - Explanations

**Concept**: [Term]
[Comprehensive explanation paragraph]

**Why it matters**: [Significance explanation]
**Connects to**: [Related concepts]
```

### Apply Level
**Cognitive Goal**: Use information in a new situation
**Content Types**:
- Practical examples
- Problem-solving scenarios
- Real-world applications
- Case studies
- Practice problems with solutions

**Example Output Format**:
```markdown
## Apply Level - Practical Applications

**Scenario**: [Real-world situation]
**How to apply**: [Step-by-step application]
**Example**: [Concrete example]
**Result**: [Expected outcome]
```

---

## Quality Standards

### Documentation Standards
✓ Professional and academic tone throughout
✓ Clear hierarchical structure with proper Markdown
✓ Concrete examples for each Bloom's level
✓ Consistent formatting across all generated notes
✓ Complete coverage of topic material
✓ Proper code references where applicable

### Content Organization
✓ Logical progression from Remember → Understand → Apply
✓ Clear section headers for each Bloom's level
✓ Prerequisite knowledge clearly stated
✓ Related concepts identified
✓ Summary points for quick reference
✓ Practice questions for comprehension check

### File Organization
✓ Topic-based subdirectory structure
✓ Hyphenated lowercase naming convention
✓ Consistent file naming across all topics
✓ Descriptive suffixes for different content types
✓ Integration with notes/ directory structure
✓ CLAUDE.md compliance verified

---

## Integration Points

### Project Structure Integration
- **Directory**: `notes/[topic-name]/`
- **Naming**: Follows CLAUDE.md conventions
- **Standards**: Adheres to professional documentation standards
- **Cross-reference**: Can link to flashcards/ and quizes/ materials

### Related Skills and Tools
- Can integrate with **flashcard-generator** (when created) for spaced repetition
- Can support **quiz-generator** (when created) for assessment
- Works with existing **notes/** directory structure
- Follows established **CLAUDE.md** standards

### Future Enhancement Points
- Support for advanced Bloom's levels (Analyze, Evaluate, Create)
- Integration with more file formats
- Automatic flashcard generation from notes
- Quiz generation from practice questions
- Cross-topic linking system

---

## Summary of Confirmed Specifications

| Aspect | Specification |
|--------|---------------|
| **Skill Name** | `notes-generate` |
| **Bloom's Levels** | Remember, Understand, Apply (foundational) |
| **Input Formats** | Topic title OR Reference files (MD/TXT/PDF) |
| **Output Formats** | 4 Markdown files per topic |
| **Content Structure** | Hybrid (paragraphs + examples + summaries) |
| **Auto-Generated Content** | Objectives, summaries, definitions, prerequisites |
| **Cross-References** | Basic (prerequisites, related concepts) |
| **Directory Structure** | Topic-organized subdirs under `notes/` |
| **Naming Convention** | Hyphenated lowercase with descriptive suffixes |
| **Standards Compliance** | Claude Code + Project CLAUDE.md |
| **Quality Standards** | Professional, academic, complete documentation |

---

## Requirements Approval Checklist

Before skill generation, please confirm:

- [ ] Bloom's Taxonomy coverage (3 foundational levels) is correct
- [ ] File format support (Markdown, Text, PDF) meets your needs
- [ ] Hybrid content structure (paragraphs + examples + summaries) is appropriate
- [ ] Fully featured auto-generated content is desired
- [ ] Basic cross-references (prerequisites + related concepts) is sufficient
- [ ] Topic-organized subdirectory structure works for your workflow
- [ ] All specifications are clear and complete

**Ready to generate skill?** Please confirm approval.

---

**Generated**: December 2024
**Status**: Awaiting final approval for skill generation
**Next Step**: Confirm above checklist, then skill files will be created
