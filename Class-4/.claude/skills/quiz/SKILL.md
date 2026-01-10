---
name: quiz
description: Generate concise, visually attractive quiz assessment materials with scoring and report cards. Use to create knowledge assessments, practice tests, and performance evaluation reports from study materials.
---

# Quiz Skill

## Purpose

The Quiz skill generates comprehensive quiz assessments with professional formatting, detailed scoring systems, and visual report cards. Creates concise yet effective evaluation materials from study notes with minimal file overhead.

## When to Use This Skill

Use the Quiz skill when:

- Creating assessment materials from study notes
- Generating practice tests for knowledge evaluation
- Producing visual report cards with score tracking
- Building quiz materials without unnecessary documentation files
- Evaluating comprehension across foundational, intermediate, and advanced levels
- Creating concise quiz content with professional presentation

## Quiz Generation Standards

### Content Structure

Generated quizzes follow this structure:

1. **Quiz Header** - Topic, difficulty level, metadata
2. **Question Section** - Organized by difficulty (Foundation, Intermediate, Advanced)
3. **Answer Key** - Complete explanations with point values
4. **Score Calculation** - Clear scoring methodology
5. **Visual Report Card** - Professional performance summary

### Question Types

Supported question formats:

- **Multiple Choice** - 4 options with one correct answer
- **Short Answer** - Brief factual questions
- **Scenario-Based** - Application and analysis questions
- **True/False** - Quick comprehension checks
- **Definition** - Terminology verification

### Scoring System

- **Foundation Questions**: 2 points each
- **Intermediate Questions**: 3 points each
- **Advanced Questions**: 5 points each
- **Total Score Calculation**: Sum of earned points / Total available points × 100
- **Performance Levels**:
  - 90-100: Excellent
  - 80-89: Good
  - 70-79: Satisfactory
  - 60-69: Needs Improvement
  - Below 60: Inadequate

### Visual Report Card Format

Report cards include:

- Performance summary with percentage score
- Breakdown by difficulty level
- Strengths and areas for improvement
- Recommended next steps
- Professional visual presentation using ASCII formatting

### File Management

Quiz materials are organized as:

```
quizes/
├── [topic]-quiz.md (Single comprehensive quiz file)
└── [topic]-quiz-report.md (Performance report - optional)
```

**Important**: Minimize file creation - consolidate quiz and report card into single file when possible.

## Quiz Generation Process

### Phase 1: Content Analysis

1. Review study notes from `notes/` directory
2. Identify key concepts across difficulty levels
3. Extract learning objectives
4. Determine assessment scope

### Phase 2: Question Development

1. Create foundation-level questions (basic recall)
2. Develop intermediate questions (comprehension and application)
3. Design advanced questions (synthesis and analysis)
4. Ensure balanced distribution across topics
5. Maintain consistency in question phrasing

### Phase 3: Answer Key Creation

1. Provide correct answers with point values
2. Write concise explanations for all answers
3. Include rationale for correct answer selection
4. Reference related concepts from study materials

### Phase 4: Report Card Design

1. Create visual score summary
2. Display performance breakdown by level
3. Provide personalized feedback
4. Suggest improvement areas
5. Recommend next study steps

## Question Development Guidelines

### Foundation Level (Basic Recall)

- Focus on definitions and basic concepts
- Ask who, what, when, where questions
- Include recognition-type multiple choice
- Verify understanding of key terminology

### Intermediate Level (Comprehension & Application)

- Require explanation of concepts
- Ask how and why questions
- Include scenario-based problem solving
- Test application to new contexts

### Advanced Level (Analysis & Synthesis)

- Require integration of multiple concepts
- Ask evaluation and judgment questions
- Include complex problem-solving scenarios
- Test critical thinking and decision-making

## Example Question Structure

```markdown
## Question [Number]: [Topic Name]
**Difficulty**: [Foundation/Intermediate/Advanced]

**Question**: [Clear, unambiguous question text]

A) [Option A]
B) [Option B]
C) [Option C]
D) [Option D]

**Answer**: [Letter] - [Explanation with reference to study materials]

**Points**: [Point value]
```

## Report Card Format

```
╔════════════════════════════════════╗
║       QUIZ PERFORMANCE REPORT      ║
╠════════════════════════════════════╣
║ Topic: [Topic Name]                ║
║ Overall Score: [X]% - [Rating]     ║
║ Questions Answered: [X]/[Total]    ║
║ Correct Answers: [X]               ║
╠════════════════════════════════════╣
║ Performance by Level:              ║
║ Foundation:    [X]% ([X]/[X])      ║
║ Intermediate:  [X]% ([X]/[X])      ║
║ Advanced:      [X]% ([X]/[X])      ║
╠════════════════════════════════════╣
║ Strengths:                         ║
║ • [Key strength identified]        ║
║ • [Key strength identified]        ║
║ Areas for Improvement:             ║
║ • [Area needing work]              ║
║ • [Area needing work]              ║
╠════════════════════════════════════╣
║ Recommended Next Steps:            ║
║ 1. [Action item]                   ║
║ 2. [Action item]                   ║
║ 3. [Action item]                   ║
╚════════════════════════════════════╝
```

## Integration with Project Materials

Quizzes integrate with existing project structure:

- **Reference notes** from `notes/what-is-llm/` directory
- **Align with flashcards** in `flashcards/what-is-llm/` for concept reinforcement
- **Maintain consistency** with CLAUDE.md standards
- **Follow professional and academic tone** throughout

## Best Practices

1. **Conciseness** - Keep questions and explanations clear and focused
2. **Clarity** - Ensure questions are unambiguous and testable
3. **Balance** - Distribute questions evenly across difficulty levels
4. **Relevance** - Base all questions on covered material
5. **Engagement** - Use varied question types to maintain interest
6. **Feedback** - Provide actionable improvement recommendations
7. **Efficiency** - Minimize files; consolidate content appropriately

## Output Location

Generated quiz materials are created in:

```
quizes/[topic]-quiz.md
```

As a single comprehensive file containing:
- All quiz questions
- Complete answer key
- Visual performance report card
- Scoring instructions
- Feedback and recommendations

---

## Instructions for Using Quiz Skill

1. **Specify Topic** - Identify which study notes to base quiz on
2. **Define Scope** - Indicate question count and difficulty distribution
3. **Provide Format** - Request question types and structure
4. **Generate Quiz** - Create comprehensive, visually formatted assessment
5. **Review Output** - Examine questions, answers, and report card format
6. **Iterate if Needed** - Request modifications or additional quizzes

The Quiz skill ensures all generated assessment materials meet professional standards while maintaining concise, efficient file structure.
