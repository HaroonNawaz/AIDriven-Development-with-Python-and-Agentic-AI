# How to Activate Skill Maker

## Instant Activation

The Skill Maker skill is already installed and ready to use.

### To Use Skill Maker:

Simply describe what skill you want to create:

```
I want to create a skill that [describe what you want]
```

### Example Activation Prompts:

1. **JSON Validator**
   ```
   I want to create a skill that validates JSON files and provides
   detailed error reporting with line numbers
   ```

2. **Code Analyzer**
   ```
   Create a skill that analyzes code quality, identifies issues,
   and provides improvement suggestions
   ```

3. **Documentation Generator**
   ```
   I need a skill that automatically generates comprehensive
   documentation from code comments and structure
   ```

4. **Performance Profiler**
   ```
   Create a skill that profiles Python code execution,
   identifies bottlenecks, and suggests optimizations
   ```

## Skill Maker Response Process

When you invoke Skill Maker:

1. **Analysis** → Skill Maker analyzes your description
2. **Gap Detection** → Identifies any missing information
3. **Clarification** → Asks targeted questions about gaps
4. **Generation** → Creates your new skill with all files
5. **Ready** → Your skill is immediately available

## What Happens Next

- Skill Maker identifies gaps in your specification
- Asks clarifying questions (in priority order)
- You provide detailed answers
- Skill Maker generates complete skill
- New skill appears in `.claude/skills/[skill-name]/`

## Getting Help While Using Skill Maker

If you need help understanding a question or the process:

- **User Guide**: Refer to USER_GUIDE.md in skill-maker directory
- **Examples**: Check section 5 of USER_GUIDE.md for interaction examples
- **Standards**: Review SKILL.md for complete process details
- **Troubleshooting**: Consult troubleshooting section in USER_GUIDE.md

## Important Notes

- The more detail you provide initially, the fewer clarification questions needed
- All generated skills follow Claude Code and project CLAUDE.md standards
- Generated skills are immediately available in Claude Code
- Skills are created in: `.claude/skills/[skill-name]/`

## Start Now

Simply invoke: "I want to create a skill that..."

Skill Maker is ready to help you!

---

**Status**: Active and Ready
**Location**: `.claude/skills/skill-maker/`
**Files**: 7 comprehensive documentation files
**Standards**: Claude Code + Project CLAUDE.md compliant
