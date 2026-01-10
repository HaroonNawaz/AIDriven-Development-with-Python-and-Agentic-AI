---
name: skill-maker
description: Generate custom Claude Code skills with professional standards. Use when creating new skills, extending Claude capabilities, or automating skill development. Validates requirements, asks clarifying questions, and produces skills adhering to Claude Code documentation standards.
---

# Skill Maker

## Purpose

The Skill Maker is a meta-skill designed to generate new Claude Code skills with professional standards and consistency. It automates the creation of skills that adhere to the official Claude Code documentation specifications while ensuring quality through requirement validation and iterative clarification.

## When to Use This Skill

Use the Skill Maker when:

- Creating new custom skills for Claude Code
- Generating multiple skills with consistent standards
- Automating skill development for projects or teams
- Building specialized capabilities into the Claude Code environment
- Establishing new tools or automation workflows
- Developing skills that integrate with existing project infrastructure

## Skill Generation Standards

### Documentation Reference

All generated skills conform to the Claude Code official documentation standards located at https://code.claude.com/docs/en/skills

### Mandatory Requirements

Generated skills must include:

1. **SKILL.md file** with required YAML frontmatter containing:
   - `name`: Lowercase letters, numbers, hyphens only; maximum 64 characters
   - `description`: Concise explanation of capability and usage context; maximum 1024 characters

2. **File Structure** adhering to Claude Code conventions:
   ```
   .claude/skills/skill-name/
   ├── SKILL.md (required)
   ├── templates/ (if applicable)
   ├── scripts/ (if applicable)
   └── examples/ (if applicable)
   ```

3. **Content Standards**:
   - Clear, professional documentation
   - Comprehensive instructions
   - Concrete usage examples
   - Well-structured sections with Markdown headers
   - Academic and professional tone throughout

4. **Naming Conventions**:
   - Directory name matches the skill name in SKILL.md
   - All lowercase with hyphens for word separation
   - Maximum 64 characters
   - Descriptive of core functionality

5. **Tool Restrictions** (when applicable):
   - Include `allowed-tools` frontmatter field for security-sensitive workflows
   - Document tool access limitations explicitly

## Skill Generation Process

### Phase 1: Requirement Gathering

When a user provides a prompt describing their desired skill:

1. **Parse Initial Requirements** - Extract core functionality, use cases, and constraints
2. **Identify Gaps** - Determine missing information critical to skill development
3. **Ask Clarifying Questions** - Query the user on ambiguous or incomplete specifications

### Phase 2: Requirement Validation

Before skill generation, validate:

- **Scope Definition** - Is the skill focused on a single capability?
- **Trigger Terms** - Are discovery terms clear and specific?
- **Input/Output Specifications** - Are inputs and outputs well-defined?
- **Dependencies** - Are required tools or integrations documented?
- **Tool Restrictions** - Should tool access be limited for security?
- **Example Scenarios** - Are concrete usage examples provided?

### Phase 3: Skill Generation

Generate the complete skill package:

1. **Create Directory Structure** - Establish proper file organization
2. **Write SKILL.md** - Comprehensive frontmatter and documentation
3. **Develop Supporting Files** - Templates, scripts, or example files as needed
4. **Document Best Practices** - Include usage guidelines and conventions
5. **Validate Compliance** - Ensure adherence to Claude Code standards

### Phase 4: Quality Assurance

Review generated skills for:

- Documentation clarity and completeness
- Professional and academic tone
- Proper file structure and naming
- YAML frontmatter correctness
- Example relevance and accuracy
- Standards compliance with Claude Code documentation

## Clarifying Questions Template

The Skill Maker should ask clarifying questions regarding:

1. **Core Functionality**
   - What is the primary function of the skill?
   - What specific problem does it solve?
   - What are the main inputs and outputs?

2. **Discovery and Triggering**
   - What keywords should trigger this skill?
   - When should Claude use this skill automatically?
   - What are typical use case scenarios?

3. **Scope and Constraints**
   - Is this skill focused on a single capability?
   - Are there scope limitations or constraints?
   - What tools does the skill require?

4. **Tool Requirements**
   - Which Claude Code tools should the skill use?
   - Are there security considerations?
   - Should tool access be restricted (allowed-tools)?

5. **Integration Points**
   - Does this skill integrate with existing project infrastructure?
   - Are there dependencies on other skills or commands?
   - Does it require specific file structures or naming conventions?

6. **Documentation and Examples**
   - What are concrete usage examples?
   - Are there special configuration requirements?
   - What troubleshooting guidance should be included?

## Example Skill Generation

### User Prompt
> Create a skill for analyzing code performance bottlenecks

### Skill Maker Response
The Skill Maker would identify gaps and ask:

1. What types of code (Python, JavaScript, Go, etc.) should this analyze?
2. What performance metrics are most important (time, memory, CPU)?
3. Should the skill generate optimization recommendations?
4. Does it need to parse specific profiling tool outputs?
5. Should results be exportable in particular formats?

### Generated Output
After clarification, the Skill Maker generates:

```yaml
---
name: performance-analyzer
description: Analyze code performance bottlenecks and generate optimization recommendations. Use when profiling code, identifying performance issues, or analyzing algorithm efficiency across multiple languages.
---

# Performance Analyzer

## Instructions
[Comprehensive analysis methodology]

## Supported Languages
[Language-specific analysis approaches]

## Examples
[Concrete performance analysis scenarios]
```

## Interdirectory References

Generated skills should integrate with the project structure:

- Reference materials in the `notes/` directory for educational context
- Link to related `flashcards/` for concept reinforcement
- Align with quiz content in `quizes/` directory
- Maintain consistency with CLAUDE.md standards

## Best Practices for Generated Skills

1. **Focused Scope** - Each skill addresses one primary capability
2. **Clear Descriptions** - Include both "what" and "when" information
3. **Concrete Examples** - Provide realistic usage scenarios
4. **Professional Documentation** - Maintain academic and professional standards
5. **Tool Efficiency** - Use allowed-tools to restrict access when appropriate
6. **Version Tracking** - Document changes for team awareness

## Output Location

Generated skills are created in:
```
.claude/skills/[skill-name]/
```

Within the project directory structure, maintaining consistency with:
- CLAUDE.md configuration standards
- Project organizational conventions
- Claude Code documentation requirements

## Integration with Project Standards

All generated skills adhere to:

- Professional and academic tone (from CLAUDE.md)
- Directory organization standards (notes/, flashcards/, quizes/)
- Code quality and documentation standards
- Claude Code official specifications

## Support and Validation

The Skill Maker validates all generated skills against:

- Official Claude Code skill documentation (https://code.claude.com/docs/en/skills)
- CLAUDE.md project configuration standards
- Naming convention requirements
- YAML frontmatter specifications
- File structure standards

---

## Instructions for Using Skill Maker

1. **Describe Your Skill** - Provide a clear prompt describing the desired skill
2. **Answer Clarifying Questions** - Respond to questions about requirements, scope, and integration
3. **Review Generated Skill** - Examine the created skill files and structure
4. **Iterate if Needed** - Request modifications or regenerations as necessary

The Skill Maker ensures all generated skills meet professional standards and integrate seamlessly with your Claude Code environment.
