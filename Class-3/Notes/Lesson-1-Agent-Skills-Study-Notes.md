# Agent Skills: Teaching Claude New Capabilities - Study Notes

## Summary

Agent Skills are specialized instruction folders that transform Claude Code from a general-purpose assistant into an expert with domain-specific knowledge. A Skill teaches Claude how to perform particular tasks automatically through pattern recognition and trigger-based activation. Rather than repeating instructions for each task, Skills encode reasoning patterns that persist and activate whenever Claude detects relevant context. This paradigm shift from "command what exists" to "describe what you want" represents the fundamental evolution of AI-native development, where organizational intelligence becomes transferable across projects and teams.

---

## Key Terms and Definitions

### Foundational Concepts

- **Agent Skill:** A folder of structured instructions that teaches Claude Code to perform something specific really well; discovered autonomously through pattern recognition and user intent
- **SKILL.md:** The required main instruction file within a skill folder containing YAML frontmatter and detailed execution instructions
- **Skill Activation:** The automatic process by which Claude detects relevance and loads a skill without explicit user invocation
- **Context Window:** Claude's limited working memory; constraints that require skills to load on-demand rather than all at once
- **YAML Frontmatter:** Metadata header (between `---` delimiters) containing name, description, version, triggers, tags, and tool specifications

### Comparative Concepts

- **Subagent:** A separate agent running in isolated context with guaranteed invocation; suitable for complex, multi-step tasks
- **Skill vs. Subagent Trade-off:** Skills offer automatic activation in shared context (lightweight repetition); Subagents offer guaranteed invocation in isolated context (complex isolation)
- **Hard Invocation:** Explicit user command required (subagent model); "Use the blog-planner subagent"
- **Soft Invocation:** Claude autonomously decides when relevant (skill model); automatic discovery based on context
- **Organizational Intelligence:** Reasoning patterns encoded in skills that become transferable across projects and teams

### Architectural Components

- **Level 1 - Brief Summary:** Always-loaded descriptions of available skills (memory efficient)
- **Level 2 - Full Instructions:** On-demand loading of complete SKILL.md with detailed workflows
- **Level 3 - Supporting Files:** Optional scripts, reference documentation, or templates bundled with skills
- **Trigger Pattern:** Specific user requests, content types, or contexts that activate a skill
- **Skill Discovery:** The process by which Claude identifies and loads relevant skills based on user input and available metadata

### Skill Types

- **Foundational Skills:** Basic capabilities (docx, pptx, xlsx, PDF creation) - "life skills" for universal use
- **Third-Party Skills:** Integration tools for specific software or services (APIs, Notion, browser navigation) - specialized certifications
- **Enterprise/Custom Skills:** Organization-specific workflows, coding standards, documentation requirements - proprietary training manuals

---

## Detailed Content

### The Core Problem and Solution

Claude Code possesses brilliant general intelligence but lacks specialized, practical knowledge for repeated workflows. When working on similar tasks (multiple blog posts, recurring reports, repetitive analyses), users must re-explain preferences each session. Skills solve this by encoding preferences as persistent organizational intelligence.

**The Problem Cycle:**
1. Repeated task launches
2. User restates instructions (outline structure, headline format, revision approach)
3. Third repetition causes frustration
4. Recognition that manual invocation burden defeats efficiency gains

**The Skill Solution:**
- Encode preferences once in SKILL.md
- Claude detects task type automatically
- Skill loads and applies workflow without intervention
- Organizational knowledge persists across sessions

### Understanding Skills Through Analogy

#### The Recipe Book Model
A brilliant chef knows all cooking techniques but benefits from "Grandma's Secret Biryani" recipe because it ensures consistency, prevents ingredient guessing, eliminates mistakes, and guarantees authentic results every time. Similarly, Skills give Claude the perfect recipe for domain-specific tasks.

#### The Phone Apps Architecture
Modern smartphones run 100+ apps efficiently by keeping most closed and loading only what's needed. Skills follow identical logic: Claude has access to many skills but loads only relevant ones on-demand, preventing memory exhaustion while maintaining comprehensive capability.

#### The Growing Garden Analogy
- Claude's base intelligence = soil (the foundation)
- Skills = seeds (potential capabilities)
- Your instructions = water & sunlight (activation energy)
- Output/results = flowers/vegetables (harvested value)

#### The IKEA Furniture Paradigm
- Skill folder = the box
- SKILL.md = instruction manual
- Helper scripts = included tools
- Templates/examples = assembly guide pictures

### How Skills Differ from Subagents

| Dimension | Skills | Subagents |
|-----------|--------|-----------|
| **Context** | Shared main conversation | Separate isolated conversation |
| **Invocation** | Soft (automatic discovery) | Hard (explicit user command) |
| **Best Use Case** | Simple, repeatable tasks | Complex, multi-step tasks |
| **Memory Model** | On-demand loading (efficient) | Full isolated context (complete) |
| **File Location** | `.claude/skills/name/SKILL.md` | `.claude/agents/name.md` |
| **Activation** | Content/intent recognition | Explicit command: "Use X subagent" |
| **Team Impact** | Lightweight shared patterns | Isolated specialized workflows |
| **Examples** | Blog planning, PDF extraction, note organizing | Comprehensive product launches, multi-step refactoring, system audits |

**Decision Framework:**
- Choose **Skills** for: Predictable repetition, automatic activation preference, multiple similar tasks per session
- Choose **Subagents** for: Complex variables, guaranteed execution requirement, multi-step specialized workflows

### The Three-Level Architecture in Practice

Claude Code uses a three-level skill loading system to balance capability breadth with memory constraints:

#### Level 1: Brief Summary (Always Loaded)
When Claude Code starts, all available skills appear as short descriptions. This metadata is minimal memory cost but sufficient for Claude to recognize when a skill might be relevant. The description is critical—it's the trigger for skill recognition.

**Example:** `blog-planner: "Help plan engaging blog posts: research topics, create outlines, suggest headlines, and draft compelling introductions."`

#### Level 2: Full Instructions (On-Demand Loading)
When Claude recognizes a skill's relevance, it loads the complete SKILL.md containing detailed instructions, workflows, examples, and execution steps. This only happens when needed, preserving context window for other tasks.

**Content includes:** Overview, usage instructions, output format, examples, best practices, step-by-step workflows

#### Level 3: Supporting Files (Conditional Loading)
Skills can bundle helper scripts (.py, .js), reference documentation (.md), or templates (.pptx, .docx). Claude accesses these only during skill execution if the workflow requires them.

**Example structure:**
```
.claude/skills/pdf-skill/
├── SKILL.md                 # Always accessible
├── scripts/pdf_extractor.py # On-demand
└── reference/pdf-standards.md # On-demand
```

**Strategic Implication:** This architecture allows skills to be comprehensive without bloating Claude's startup memory, enabling arbitrarily large skill ecosystems.

### Anatomy of SKILL.md: The Blueprint

Every SKILL.md file contains two essential parts:

#### Part 1: YAML Frontmatter (The Metadata Card)
```yaml
---
name: skill-identifier
description: What it does + WHEN to use it (critical for discovery)
version: "1.0.0"
trigger: |
  - Specific user phrases
  - Content type indicators
  - Intent patterns
tags:
  - domain1
  - domain2
activation_context:
  - content_type: text/markdown
  - user_intent: action_type
tool: primary-tool-category
capability: specific-capability
---
```

The description field is the discovery mechanism—Claude uses it to determine skill relevance.

#### Part 2: Markdown Body (The Instructions)
```markdown
# Skill Name

## Overview
[What this skill accomplishes]

## When to Use This Skill
[Specific scenarios for activation]

## How This Skill Works
[Step-by-step execution workflow]

## Output Format
[Expected structure of results]

## Example
[Input → Output demonstration]
```

**Critical Design Principle:** Descriptions drive discovery. Write descriptions that explicitly state WHEN to use the skill, not just what it does.

### Skill Creation Best Practices

#### DO ✓
- **Be concise:** Claude is intelligent; don't over-explain obvious concepts
- **Use clear examples:** Show patterns through concrete input/output demonstrations
- **Write descriptive triggers:** Explicitly state when the skill should activate
- **Focus on domain specifics:** Encode what Claude doesn't know by default (your preferences, workflows, standards)
- **Include activation phrases:** Common user requests that should trigger the skill

#### DON'T ✗
- **Create README files:** Unnecessary duplication; put everything in SKILL.md
- **Include installation guides:** Claude doesn't need setup instructions
- **Write verbose explanations:** Excessive text wastes context window
- **Add irrelevant information:** Keep focus tight and purposeful
- **Assume implicit triggers:** Explicitly state the skill's discovery conditions

### When Claude Code Invokes Skills Automatically

Three primary patterns trigger skill activation:

#### Pattern 1: Content Type Recognition
- **Trigger:** User uploads or references specific file types
- **Example:** Upload PDF → pdf-extraction-skill activates
- **Mechanism:** MIME type or file extension matching activation_context

#### Pattern 2: Task Request Recognition
- **Trigger:** User describes a task matching skill's domain
- **Example:** "Write a blog post" → blog-planner-skill activates
- **Mechanism:** Natural language pattern matching against trigger descriptions

#### Pattern 3: Explicit Request
- **Trigger:** User directly names the skill
- **Example:** "Use the blog-writer skill" → Direct activation
- **Mechanism:** Explicit command parsing and invocation

**Discovery Process:**
1. Claude reads brief skill descriptions (Level 1 metadata)
2. Analyzes user input for relevance signals
3. Matches input against trigger patterns
4. Loads full SKILL.md if relevance detected
5. Applies skill workflow automatically
6. No explicit invocation required

### Types of Skills: The Ecosystem

#### 1. Foundational Skills
**Purpose:** Universal capabilities every user needs
- Creating Word documents (.docx)
- Making PowerPoint presentations (.pptx)
- Working with Excel spreadsheets (.xlsx)
- Creating and extracting PDFs

**Analogy:** Basic life skills (cooking, cleaning, driving) everyone develops
**Impact:** These ship with Claude Code; form the capability baseline

#### 2. Third-Party Skills
**Purpose:** Integration with external tools and services
- Browser navigation and web content extraction
- Notion workspace integration and database operations
- API interaction and integration workflows
- SaaS platform automation (Slack, Zapier, etc.)

**Analogy:** Professional certifications (Photoshop expertise, forklift license, software-specific training)
**Impact:** Extend Claude's reach into existing tool ecosystems users rely on

#### 3. Enterprise/Custom Skills
**Purpose:** Organization-specific workflows and standards
- Company coding style guides and architectural patterns
- Internal documentation standards and formatting
- Domain-specific business workflows and procedures
- Proprietary analysis frameworks and methodologies

**Analogy:** Company training manuals reflecting organizational culture and processes
**Impact:** Encode institutional knowledge so every team member benefits automatically

### Skill Activation in Practice: The Invoice Extraction Example

**Scenario:** Extract specific data from a PDF invoice

**What the user does:**
```
Extract these fields from invoice.pdf:
- Invoice number
- Date
- Total amount
- Vendor name
```

**What happens behind the scenes:**
1. Claude reads system prompt: "pdf-extraction-skill available"
2. Recognizes PDF content type + extraction intent
3. Loads full pdf-extraction-skill SKILL.md
4. Executes skill's extraction workflow:
   - Parse PDF structure
   - Locate field patterns
   - Extract matching values
   - Format as structured data
5. Returns results

**What the user sees:**
```
Extracted Invoice Details:
- Invoice #: INV-2024-00531
- Date: November 13, 2024
- Total: $2,450.00
- Vendor: Tech Solutions Inc.
```

**Key Insight:** User described intent; Claude discovered the right skill and applied it automatically. No explicit skill command required. This exemplifies the "describe what you want" rather than "command what exists" paradigm.

### Building Custom Skills: Step-by-Step Process

#### Step 1: Identify the Repeatable Pattern
- What task do you perform repeatedly?
- What instructions do you give each time?
- What are your specific preferences?
- When should this automation trigger?

#### Step 2: Create Directory Structure
```bash
mkdir -p .claude/skills/your-skill-name
```

#### Step 3: Write SKILL.md Frontmatter
```yaml
---
name: your-skill-name
description: "Clear description of what it does and WHEN to use it"
version: "1.0.0"
trigger: |
  - User phrase 1
  - User phrase 2
  - Specific context indicators
tags:
  - relevant
  - domains
tool: primary-tool-type
capability: specific-capability
---
```

#### Step 4: Write Skill Instructions
```markdown
# Skill Name

## Overview
[Comprehensive explanation]

## When to Use This Skill
[Specific activation scenarios]

## How This Skill Works
[Step-by-step workflow]

## Output Format
[Expected result structure]

## Examples
[Input/output demonstrations]
```

#### Step 5: Test and Refine
1. Ask Claude to describe the skill
2. Test trigger scenarios
3. Verify skill activates appropriately
4. Refine descriptions based on activation results
5. Update examples if needed

#### Step 6: Iterate Through Co-Learning
Ask Claude: "Review this skill. What could be improved? Suggest 2-3 enhancements."

**Collaborative Process:**
- Claude suggests improvements to descriptions and structure
- You specify constraints ("headlines must be curiosity-driven, not clickbait")
- Together refine the skill to match your exact workflow
- Test updated version to validate improvements

---

## Review Questions

### Comprehension Questions
1. What is the primary difference between a Skill and a Subagent in Claude Code?
2. Explain the three-level architecture of skill loading and why it's necessary.
3. What is the role of the YAML frontmatter in SKILL.md files?
4. Name three types of skills and provide an example for each.
5. How does Claude Code automatically discover when to use a skill?

### Application Questions
6. You're working on code reviews repetitively. Should you create a Skill or a Subagent? Justify your answer.
7. Design a skill for your most repetitive task. What would the trigger patterns be?
8. A skill description states: "Helps with writing documents." Why is this description insufficient? Rewrite it better.
9. When would you choose a Third-Party Skill over a Foundational Skill?
10. How would you test whether your custom skill activates correctly?

### Critical Thinking Questions
11. The lesson states skills encode "reasoning patterns" not just "commands." What is the difference, and why does it matter?
12. Explain how the three-level skill architecture relates to the "context window" constraint. Why is this design elegant?
13. How does the "Describe what you want vs. Command what exists" paradigm shift represent AI-native development?
14. What organizational benefits emerge from Enterprise Skills? How might this change team workflows?
15. Compare the growth potential of an organization using Skills vs. one using only direct prompting.

### Synthesis Questions
16. Design a complete skill ecosystem (3-5 skills) for your primary work domain. Explain how they interconnect.
17. How would you decide whether a repeated task deserves a custom skill?
18. A developer creates a skill with perfect instructions but poor trigger descriptions. Why might it fail in practice?
19. Explain how Skills represent "persistent organizational intelligence." Provide concrete examples.
20. How does the skill system enable team-wide improvements through shared patterns?

---

## Quick Review Checklist

### Essential Concepts
- ☐ Skills are folders of instructions that teach Claude domain-specific expertise
- ☐ Skills activate automatically when Claude detects relevant context (soft invocation)
- ☐ Subagents require explicit user commands and provide isolated context (hard invocation)
- ☐ Three-level architecture (summaries, full instructions, supporting files) balances capability with memory efficiency
- ☐ YAML frontmatter metadata (name, description, triggers, tags) drives skill discovery

### Practical Knowledge
- ☐ SKILL.md contains both metadata (YAML) and instructions (Markdown)
- ☐ Skill descriptions must explicitly state WHEN to use them for proper activation
- ☐ Three skill types exist: Foundational (universal), Third-Party (integrations), Enterprise (custom)
- ☐ Content type recognition, task request recognition, and explicit requests trigger skills
- ☐ Custom skills follow: identify pattern → create directory → write frontmatter → write instructions → test → refine

### Strategic Understanding
- ☐ Skills transform "command what exists" to "describe what you want" paradigm
- ☐ Skills encode reasoning patterns transferable across projects and teams
- ☐ Organizational intelligence accumulates through shared skill collections
- ☐ Skills are superior for repeatable, predictable tasks; subagents for complex, isolated work
- ☐ The skill system enables team-wide capability improvements through shared reasoning patterns

### Design Principles
- ☐ Be concise—Claude is intelligent; focus on domain-specific preferences
- ☐ Use clear examples—Show patterns through input/output demonstrations
- ☐ Write for discovery—Explicit trigger descriptions enable automatic activation
- ☐ Focus on specifics—Encode what Claude doesn't know by default
- ☐ Test and refine—Iterate through co-learning to optimize skill effectiveness

---

## Study Tips for Long-Term Retention

1. **Create a Personal Skill:** Build your first custom skill for a repetitive task in your workflow. Hands-on experience embeds understanding better than passive reading.

2. **Map Your Workflow:** Identify 3-5 repeatable tasks in your domain. For each, assess whether a Skill or Subagent would serve better. Justify each choice.

3. **Analyze Provided Examples:** Study the Blog-Planner and Study-Notes-Creator examples in detail. How do their descriptions enable activation? What makes their structures effective?

4. **Design Scenarios:** When you encounter repetitive tasks, pause and think: "Would a skill improve this?" Practice making intentional skill/subagent decisions.

5. **Review Others' Skills:** When you encounter new skills, read their SKILL.md files carefully. What makes discovery descriptions effective? How are workflows structured?

6. **Co-Learn with Claude:** Take your custom skills to Claude Code and ask for improvement suggestions. Understand the iteration process that refines organizational intelligence.

7. **Connect to Paradigm Shift:** Regularly remind yourself: Skills represent the fundamental shift from "command what exists" to "describe what you want." This conceptual foundation explains all technical details.

8. **Build Skill Suites:** Rather than creating isolated skills, think about how skills interconnect in your domain. This higher-level thinking prepares you for enterprise-scale implementations.

---

## Connection to Broader Learning

This lesson establishes the foundation for understanding Claude Code's extensibility architecture:

- **Foundation:** Base Claude intelligence (general brilliance)
- **Skills Layer:** Organizational reasoning patterns (domain expertise)
- **Plugin Layer (Lesson 9):** Packaged skill collections for marketplace distribution (team-scale intelligence)

Skills represent the middle tier where individual preferences become persistent organizational knowledge. Mastering skills prepares you for the plugin system and the complete vision of AI-native development where reasoning patterns, not just implementations, become shareable intellectual property.

---

## Additional Resources and References

- **Official Repository:** https://github.com/anthropics/skills
- **Key Concepts:** YAML frontmatter, context window limitations, pattern-based activation
- **Related Skills:** blog-planner, study-notes-creator, meeting-notes-organizer, learning-path-designer, code-reviewer
- **Future Learning:** Lesson 9 covers plugins and skill packaging for marketplace distribution

---

## Self-Assessment Rubric

**Mastery Level Indicators:**

- **Novice:** Can explain what skills are and their basic purpose
- **Intermediate:** Can create a custom skill with proper SKILL.md structure and metadata
- **Advanced:** Can design skill ecosystems, optimize trigger descriptions, and guide others through skill creation
- **Expert:** Understand skills as reasoning pattern encoders; can architect organization-wide skill systems; advise on skill vs. subagent trade-offs strategically

Where are you on this progression? What's your next learning step?
