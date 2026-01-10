# Skill Maker Requirements Checklist

This document outlines the comprehensive requirements validation checklist that the Skill Maker uses when generating new skills.

## Phase 1: Initial Requirement Analysis

### Core Functionality Definition

- [ ] **Primary Function Identified**: Clear statement of what the skill does
  - Question: "What is the main function of the skill?"
  - Validation: Skill addresses one primary capability

- [ ] **Problem Statement**: Clear identification of problem being solved
  - Question: "What specific problem does this skill solve?"
  - Validation: Problem is well-defined and focused

- [ ] **Input Specifications**: Clear definition of expected inputs
  - Question: "What are the primary inputs this skill will receive?"
  - Validation: Inputs are specific and well-documented

- [ ] **Output Specifications**: Clear definition of expected outputs
  - Question: "What outputs should the skill produce?"
  - Validation: Outputs are concrete and measurable

### Use Case Definition

- [ ] **Primary Use Cases Identified**: At least 3-4 distinct use cases
  - Question: "What are the typical scenarios where this skill would be used?"
  - Validation: Use cases are realistic and well-defined

- [ ] **Target Users Identified**: Who will use this skill
  - Question: "Who is the intended user of this skill?"
  - Validation: User personas are clear

- [ ] **Trigger Keywords Determined**: Terms that should activate the skill
  - Question: "What keywords should trigger this skill automatically?"
  - Validation: Keywords are specific and discoverable

## Phase 2: Scope and Constraints Validation

### Scope Definition

- [ ] **Skill Scope Confirmed**: Single focused capability (not overly broad)
  - Question: "Is this skill focused on one primary capability?"
  - Validation: Scope is narrow and focused

- [ ] **Scope Boundaries Established**: What is IN scope and OUT of scope
  - Question: "What are the boundaries of this skill's functionality?"
  - Validation: Clear definition of included/excluded functionality

- [ ] **Dependency Identification**: External skills or components required
  - Question: "Does this skill depend on other skills or components?"
  - Validation: Dependencies are documented

### Constraint Documentation

- [ ] **Performance Constraints Identified**: Speed, resource, or scalability limits
  - Question: "Are there performance constraints or limitations?"
  - Validation: Constraints are documented

- [ ] **Compatibility Constraints Identified**: OS, version, or environment requirements
  - Question: "Are there specific environment or compatibility requirements?"
  - Validation: Requirements are clearly stated

- [ ] **Integration Constraints Identified**: Integration points and limitations
  - Question: "Are there integration constraints with existing systems?"
  - Validation: Constraints are documented

## Phase 3: Tool and Technology Requirements

### Tool Requirements Validation

- [ ] **Required Tools Listed**: All tools the skill must use
  - Question: "What Claude Code tools does this skill require?"
  - Available tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, Task, and others
  - Validation: All required tools are supported

- [ ] **Optional Tools Identified**: Tools that enhance but are not required
  - Question: "Are there optional tools that enhance the skill?"
  - Validation: Optional tools clearly marked

- [ ] **Tool Restrictions Determined**: Security-sensitive tool limitations
  - Question: "Should any tools be restricted for security reasons?"
  - Validation: Restrictions are explicitly documented if needed

### Technology Stack

- [ ] **Programming Languages Identified**: Languages the skill works with (if applicable)
  - Question: "What programming languages should this skill support?"
  - Validation: Languages are clearly specified

- [ ] **File Format Support**: Formats the skill works with (if applicable)
  - Question: "What file formats should be supported?"
  - Validation: Format support is documented

- [ ] **External Dependencies**: Third-party libraries or services
  - Question: "Are there external dependencies or services required?"
  - Validation: Dependencies are documented

## Phase 4: Documentation and Examples

### Documentation Requirements

- [ ] **Clear Purpose Statement**: One-sentence skill purpose
  - Validation: Statement is concise and descriptive

- [ ] **Comprehensive Instructions**: Step-by-step workflow
  - Question: "What are the step-by-step instructions for using this skill?"
  - Validation: Instructions are clear and sequential

- [ ] **Best Practices Documented**: Recommended approaches
  - Question: "What best practices should users follow?"
  - Validation: Practices are specific and actionable

- [ ] **Troubleshooting Guide**: Common issues and solutions
  - Question: "What are common issues users might encounter?"
  - Validation: Solutions are documented

### Example Requirements

- [ ] **Minimum 2 Examples**: Realistic usage scenarios
  - Question: "Can you provide concrete usage examples?"
  - Validation: Examples are representative and realistic

- [ ] **Example Input Provided**: Sample input for each example
  - Validation: Input clearly demonstrates expected format

- [ ] **Example Output Provided**: Sample output for each example
  - Validation: Output demonstrates expected results

- [ ] **Example Process Described**: Steps taken in each example
  - Validation: Process is clear and reproducible

## Phase 5: Integration and Standards

### Project Integration

- [ ] **Directory Location Defined**: Where skill will be created
  - Validation: Location is `.claude/skills/[skill-name]/`

- [ ] **Naming Convention Compliance**: Skill name follows standards
  - Rules: Lowercase letters, numbers, hyphens only; max 64 characters
  - Validation: Name matches pattern: `^[a-z0-9-]{1,64}$`

- [ ] **Related Resources Identified**: Links to notes, flashcards, quizzes
  - Question: "Are there related materials in notes/, flashcards/, or quizes/?
  - Validation: Cross-references are documented

### Standards Compliance

- [ ] **YAML Frontmatter Correct**: Proper SKILL.md frontmatter
  - Required fields: `name`, `description`
  - Validation: Frontmatter is valid YAML

- [ ] **Description Compliance**: Description meets requirements
  - Max 1024 characters
  - Includes both "what" and "when" information
  - Validation: Description is complete and within limits

- [ ] **File Structure Proper**: Correct directory organization
  - Required: SKILL.md
  - Optional: templates/, scripts/, examples/, supporting files
  - Validation: Structure matches Claude Code standards

- [ ] **CLAUDE.md Alignment**: Adherence to project standards
  - Professional and academic tone
  - Clear documentation
  - Proper file organization
  - Validation: All project standards met

## Phase 6: Security and Performance

### Security Validation

- [ ] **Tool Access Reviewed**: Determine if tool restrictions needed
  - Question: "Should tool access be restricted for security?"
  - Validation: Security implications documented

- [ ] **Data Handling Documented**: How sensitive data is handled
  - Question: "Does this skill handle sensitive data?"
  - Validation: Data handling practices documented

- [ ] **Input Validation Specified**: How inputs are validated
  - Validation: Input validation approach documented

### Performance Validation

- [ ] **Performance Expectations Set**: Expected speed/resource usage
  - Question: "What are expected performance characteristics?"
  - Validation: Expectations are documented

- [ ] **Scalability Considerations**: How skill scales
  - Question: "How does this skill scale with input size?"
  - Validation: Scaling behavior documented

## Phase 7: Final Quality Assurance

### Content Quality

- [ ] **Professional Tone**: Academic and professional language
  - Validation: No colloquialisms or casual expressions

- [ ] **Clarity and Precision**: Clear, unambiguous language
  - Validation: All technical terms properly defined

- [ ] **Completeness**: All required sections present
  - Validation: No missing critical documentation

- [ ] **Consistency**: Consistent formatting and terminology
  - Validation: Consistent throughout

### Technical Validation

- [ ] **YAML Syntax Valid**: SKILL.md frontmatter is valid YAML
  - Validation: No syntax errors

- [ ] **Markdown Formatting Correct**: Proper Markdown structure
  - Validation: Headers, lists, code blocks properly formatted

- [ ] **Links and References Valid**: All cross-references work
  - Validation: Internal and external links are accurate

- [ ] **Code Examples Functional**: Examples are accurate
  - Validation: Examples can be executed as documented

## Clarifying Questions Template

When gaps are identified in the user's prompt, the Skill Maker asks clarifying questions in this order:

### Priority 1: Core Functionality (MUST ASK)
1. "What is the primary function of this skill?"
2. "What specific problem does it solve?"
3. "What are the main inputs and outputs?"

### Priority 2: Scope and Use Cases (MUST ASK)
4. "What are the typical use case scenarios?"
5. "Is this skill focused on a single capability?"
6. "Are there scope limitations or constraints?"

### Priority 3: Tool Requirements (MUST ASK)
7. "Which Claude Code tools should this skill use?"
8. "Are there security considerations or tool restrictions needed?"

### Priority 4: Documentation (SHOULD ASK)
9. "Can you provide 2-3 concrete usage examples?"
10. "What are common issues or edge cases?"

### Priority 5: Integration (SHOULD ASK)
11. "Does this skill integrate with existing project infrastructure?"
12. "Are there related materials in notes/, flashcards/, or quizes/?"

## Decision Tree for Gap Identification

```
User provides skill prompt
│
├─ Core functionality clear? → NO → Ask Priority 1 questions
│
├─ Use cases defined? → NO → Ask Priority 2 questions
│
├─ Tool requirements specified? → NO → Ask Priority 3 questions
│
├─ Examples provided? → NO → Ask Priority 4 questions
│
├─ Integration points clear? → NO → Ask Priority 5 questions
│
└─ All critical gaps filled? → YES → Generate skill
                             → NO → Ask remaining questions
```

## Generation Approval Checklist

Before generating the skill, verify:

- [ ] All Priority 1 questions have been answered
- [ ] All Priority 2 questions have been answered
- [ ] All Priority 3 questions have been answered
- [ ] At least 2 Priority 4 questions have been answered
- [ ] At least 1 Priority 5 question has been answered (if applicable)
- [ ] All answers are clear and unambiguous
- [ ] Generated skill structure is planned and reviewed
- [ ] Naming convention compliance verified
- [ ] Standards alignment confirmed

**Only proceed with skill generation after approval checklist is complete.**

---

This checklist ensures all generated skills meet professional standards and integrate seamlessly with the Claude Code environment and project infrastructure.
