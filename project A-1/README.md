# Enterprise Architecture Skills: Extract Your Job Into Reusable Tools

Professional Python skills for automating critical enterprise architecture analysis tasks. **Save 95-135 minutes per analysis cycle** while ensuring objective, auditable decision-making.

**Project Status:** Production-Ready EA Automation Skills
**Last Updated:** January 11, 2026
**Framework:** TOGAF ADM Aligned

---

## Watch Demo (90 Seconds)

**[▶ Watch on Loom](https://www.loom.com/embed/20a5f98a1c264097a5872e2cced4cf65)** - See all three skills in action



---

## Overview

This project contains **three production-ready Claude Code skills** that automate critical enterprise architecture analysis tasks. Each skill saves 20-60 minutes and provides professional, auditable outputs ready for stakeholder presentations.

**What You Get:**
- ✅ **Three automation skills** - Ready to use immediately
- ✅ **950+ lines of production code** - Tested and verified
- ✅ **95-135 minutes saved** per complete analysis cycle
- ✅ **Professional documentation** - Step-by-step guides included
- ✅ **TOGAF ADM Aligned** - Supports enterprise architecture planning
- ✅ **Zero setup required** - Just Python 3.6+, no external dependencies

---

## The Three Skills

### Skill 1: Capability Matrix Builder
**Location:** `.claude/skills/capability-matrix-builder/`

Generates business capability matrices with maturity assessment for Phase B planning.
- **Creates:** Capability matrices with current/target maturity levels
- **Produces:** Professional heatmaps, gap analysis, and investment priorities
- **Time Saved:** 20-30 minutes per Phase B assessment
- **Use:** Quarterly capability roadmaps, investment prioritization

```bash
# See sample output
python .claude/skills/capability-matrix-builder/capability_matrix_builder.py sample

# Use with your data
python .claude/skills/capability-matrix-builder/capability_matrix_builder.py interactive
```

**Documentation:** [Full Skill Guide](./.claude/skills/capability-matrix-builder/SKILL.md)

---

### Skill 2: Technology Evaluation Scorecard
**Location:** `.claude/skills/technology-evaluation-scorecard/`

Makes objective technology selection decisions using weighted evaluation criteria.
- **Creates:** Scoring matrices for comparing technology options
- **Produces:** Ranked recommendations with detailed justification
- **Time Saved:** 30-45 minutes per technology evaluation
- **Use:** Build vs Buy decisions, vendor selection, technology refresh

```bash
# See sample output
python .claude/skills/technology-evaluation-scorecard/technology_evaluation_scorecard.py sample

# Use with your data
python .claude/skills/technology-evaluation-scorecard/technology_evaluation_scorecard.py interactive
```

**Documentation:** [Full Skill Guide](./.claude/skills/technology-evaluation-scorecard/SKILL.md)

---

### Skill 3: Business-to-IT Mapper
**Location:** `.claude/skills/business-to-it-mapper/`

Creates complete traceability from business capabilities through applications to technology infrastructure.
- **Creates:** Three-matrix mapping of capabilities → applications → technology
- **Produces:** Gap analysis and redundancy report
- **Time Saved:** 45-60 minutes per complete traceability analysis
- **Use:** Portfolio rationalization, Phase C-D planning, infrastructure optimization

```bash
# See sample output
python .claude/skills/business-to-it-mapper/business_to_it_mapper.py sample

# Use with your data
python .claude/skills/business-to-it-mapper/business_to_it_mapper.py interactive
```

**Documentation:** [Full Skill Guide](./.claude/skills/business-to-it-mapper/SKILL.md)

---

## Quick Start (3 Minutes)

### Try All Three Skills Immediately

```bash
# Skill 1: Generate a capability matrix
python .claude/skills/capability-matrix-builder/capability_matrix_builder.py sample

# Skill 2: Generate a technology scorecard
python .claude/skills/technology-evaluation-scorecard/technology_evaluation_scorecard.py sample

# Skill 3: Generate a business-to-IT mapping
python .claude/skills/business-to-it-mapper/business_to_it_mapper.py sample
```

Each sample produces professional, ready-to-present output in 5-10 seconds.

---

## Use Cases by Role

### For Enterprise Architects
- **Capability Roadmapping:** Use Skill 1 quarterly to assess and plan capability maturity
- **Technology Decisions:** Use Skill 2 to objectively compare platform options
- **Portfolio Analysis:** Use Skill 3 to identify capability gaps and application rationalization opportunities

### For Program Managers
- **Planning & Prioritization:** Use Skill 1 outputs to prioritize capability investments
- **Investment Justification:** Use Skill 2 to demonstrate objective technology selection criteria
- **Dependency Mapping:** Use Skill 3 to understand application interdependencies

### For IT Leaders
- **Strategic Planning:** Use all three skills to inform technology roadmap decisions
- **Cost Optimization:** Use Skill 3 to identify redundant applications and technologies
- **Risk Management:** Use Skill 3 gap analysis to identify capability risks

---

## Detailed Documentation

Each skill has comprehensive documentation for learning and reference:

| Skill | SKILL.md Location | Contents |
|-------|------------------|----------|
| Capability Matrix | `.claude/skills/capability-matrix-builder/SKILL.md` | Usage, maturity scale, examples, TOGAF alignment |
| Technology Scorecard | `.claude/skills/technology-evaluation-scorecard/SKILL.md` | Scoring methodology, best practices, troubleshooting |
| Business-to-IT Mapper | `.claude/skills/business-to-it-mapper/SKILL.md` | 4-step process, gap analysis, portfolio patterns |

**Additional Guides in `docs/guides/`:**
- `GETTING_STARTED.md` - Step-by-step walkthrough for first use
- `SKILLS_USAGE_GUIDE.md` - Comprehensive guide with real examples
- `VIDEO_RECORDING_GUIDE.md` - How to record a demo
- `SCREENSHOT_GUIDE.md` - How to capture output for presentations
- `POWERPOINT_TEMPLATE.md` - Slide specifications for presentations

---

## FAQ: Quick Answers

### Q: What do I need to run these skills?
**A:** Just Python 3.6 or higher. No external dependencies - all three skills use Python's standard library only.

### Q: Can I use these without the TOGAF framework?
**A:** Yes! These are practical enterprise architecture tools. TOGAF ADM context is provided for reference, but the skills work with any EA methodology.

### Q: How long does each skill take to use?
**A:** Sample mode (demo): 10 seconds. Interactive mode (with your data): 10-20 minutes depending on data size.

### Q: Can I export the results?
**A:** Yes, each skill exports to JSON format for further analysis in Excel, visualization tools, or other systems.

### Q: What if I need help using a skill?
**A:** Start with the skill's SKILL.md file in `.claude/skills/[skill-name]/SKILL.md` for complete documentation and troubleshooting.

### Q: Can I modify or extend these skills?
**A:** Yes! Each skill is a standalone Python file in `.claude/skills/[skill-name]/`. You can modify the code for your specific needs.

### Q: Are these skills suitable for governance/compliance?
**A:** Yes. Each skill produces professional, auditable outputs with complete traceability from inputs to analysis to recommendations.

---

## Project Structure

The project follows Claude Code standards for organization:

```
.claude/skills/                          # All production skills
├── capability-matrix-builder/           # Capability assessment
├── technology-evaluation-scorecard/     # Technology selection
└── business-to-it-mapper/              # Business-IT traceability

docs/                                    # Documentation
├── guides/                              # How-to guides
├── skills/                              # Extended skill documentation
├── architecture/                        # Design documentation
└── reference/                           # TOGAF context

README.md                                # This file
PROJECT_STRUCTURE.md                     # Detailed directory guide
```

For a complete project overview, see [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md).

---

## Features & Benefits

### Built for Enterprise Use
- ✅ **Professional Format** - Outputs ready for executive presentations
- ✅ **Auditable** - Complete traceability of analysis steps
- ✅ **Flexible Scale** - Works with 5-100+ capabilities, applications, technologies
- ✅ **Extensible** - Modify code for organization-specific needs

### Time-Saving Automation
- ✅ **Capability assessment:** 20-30 minutes saved per analysis
- ✅ **Technology evaluation:** 30-45 minutes saved per selection
- ✅ **Business-IT mapping:** 45-60 minutes saved per complete analysis
- ✅ **Total:** 95-135 minutes saved per architecture planning cycle

### Aligned with Enterprise Standards
- ✅ **TOGAF ADM Framework** - Each skill references relevant phases (A-E)
- ✅ **Industry Best Practices** - Incorporates weighted scoring, gap analysis, redundancy detection
- ✅ **Professional Standards** - Output suitable for architecture governance and decision-making

---

## Getting Started

### Step 1: Try a Sample (1 minute)
```bash
python .claude/skills/capability-matrix-builder/capability_matrix_builder.py sample
```

### Step 2: Read the Skill Guide (5 minutes)
Open `.claude/skills/capability-matrix-builder/SKILL.md` to understand what the skill does and when to use it.

### Step 3: Run Interactive Mode (10-15 minutes)
```bash
python .claude/skills/capability-matrix-builder/capability_matrix_builder.py interactive
```

### Step 4: Explore the Other Skills
Follow the same pattern with Skill 2 and Skill 3.

### Step 5: Read Extended Documentation
For comprehensive guides, see `docs/guides/GETTING_STARTED.md`.

---

## Support & Community

### Documentation
- **Quick Reference:** Skill's SKILL.md file (e.g., `.claude/skills/[skill]/SKILL.md`)
- **How-To Guides:** `docs/guides/` directory
- **Project Structure:** [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md)

### Troubleshooting
Each skill's SKILL.md file includes a troubleshooting section with common issues and solutions.

### Contributing
These skills are designed to be extended. To customize:
1. Review the Python code in `.claude/skills/[skill]/`
2. Modify as needed for your organization
3. Update the SKILL.md documentation accordingly

---

## About This Project

**Enterprise Architecture Skills** is a collection of practical Python tools for automating critical EA tasks. Created for professionals who need fast, objective, auditable analysis—not for exam preparation.

**Philosophy:** Extract repeatable cognitive work from your daily EA job and automate it. Save 95-135 minutes per analysis cycle while improving consistency and auditability.

**Target Users:**
- Enterprise architects planning architecture initiatives
- IT leaders making technology investment decisions
- Program managers prioritizing capability development
- Organizations implementing architecture governance

---

## Version & Updates

**Current Version:** 1.0
**Last Updated:** January 11, 2026
**Status:** Production Ready

All three skills are tested, documented, and ready for immediate use.

---

## License & Attribution

This project follows Claude Code standards for organization and distribution.

Each skill includes sample data and interactive modes for learning and demonstration purposes.

---

**Created for Enterprise Architecture Automation**
**Practical Tools for Architecture Professionals**
