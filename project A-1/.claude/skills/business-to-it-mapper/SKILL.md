# Business-to-IT Mapper Skill

## Overview
Creates complete traceability matrices mapping business capabilities through applications to technology infrastructure.

This skill generates comprehensive visibility into how business capabilities are supported by the IT landscape. It identifies unmapped capabilities, unused applications, orphaned technologies, and redundancies—providing actionable insights for portfolio optimization and infrastructure planning.

## What It Does

**Input:**
- Business capabilities (from Phase B)
- Applications in IT portfolio (COTS, Custom, SaaS)
- Technology components (databases, platforms, infrastructure)
- Mappings between capabilities→applications and applications→technology

**Processing:**
- Creates capability-to-application traceability
- Creates application-to-technology mappings
- Calculates coverage percentages
- Identifies gaps and orphaned components
- Detects redundancy and overlap

**Output:**
- Capability-to-application mapping matrix
- Application-to-technology mapping matrix
- Technology infrastructure layer summary
- Gap analysis report with actionable recommendations
- Redundancy analysis highlighting overlaps
- JSON export for further analysis

## Time Saved
**45-60 minutes per complete traceability analysis** (vs. manual portfolio audit)

## Usage

### Quick Start (Demo Mode)
```bash
python business_to_it_mapper.py sample
```
See complete example with 4 capabilities, 5 applications, and 10 technologies (5-10 seconds).

### Interactive Mode
```bash
python business_to_it_mapper.py interactive
```

**4-Step Process:**

**Step 1: Define Business Capabilities (2-3 minutes)**
- Enter capability name and owner
- Example: "Customer Management" owned by "Sales"
- Can assess 5-50+ capabilities

**Step 2: Define Applications (1-2 minutes)**
- Enter application name and type (COTS/Custom/SaaS)
- Example: "Salesforce", type "SaaS"
- List all applications in current portfolio

**Step 3: Map Capabilities to Applications (2-3 minutes)**
- For each capability, enter which applications support it
- Example: "Customer Management" supported by applications 1,2
- Identifies unmapped capabilities

**Step 4: Map Applications to Technology (2-3 minutes)**
- For each application, enter technology components
- Example: Salesforce uses "AWS, REST API, PostgreSQL"
- Identifies applications without technology assignment

**Time to complete:** 10-15 minutes for 5 capabilities, 5 applications, 10 technologies

### Expected Output

```
BUSINESS-TO-IT TRACEABILITY MATRIX
====================================

TRACEABILITY SUMMARY:
  Capabilities: 4 (3 mapped, 1 unmapped)
  Applications: 5 (4 used, 1 unused)
  Technology Components: 10
  Total Capability-to-Application Mappings: 5

[Capability-to-Application Mappings Table]
[Application-to-Technology Mappings Table]
[Technology Infrastructure Layer]

GAP ANALYSIS:
  [CAPABILITY GAPS] - Capabilities without supporting applications
  [APPLICATION GAPS] - Applications without technology infrastructure
  [UTILIZATION GAPS] - Applications not supporting any capability

REDUNDANCY ANALYSIS:
  [Capabilities supported by multiple applications]
```

## What Each Matrix Shows

### Capability-to-Application Matrix
Maps which capabilities are supported by which applications.

**What to look for:**
- ✓ Green: Every capability has ≥1 supporting application
- ✗ Red: Unmapped capability = business function without IT support

### Application-to-Technology Matrix
Shows which technology components support each application.

**What to look for:**
- ✓ Green: Every application has assigned technologies
- ✗ Red: Application without technology = incomplete migration/planning

### Technology Infrastructure Layer
Lists all technologies and which applications use them.

**What to look for:**
- ✓ Shared technologies (used by 3+ apps) = consolidation opportunity
- ✓ Redundant technologies = where to standardize
- ✗ Single-use technologies = underutilized investments

## Gap Types and What They Mean

### Capability Gaps
**What:** Business capability without supporting application
**Why:** Potential manual workaround, shadow IT, or unmet business need
**Action:** Build application, acquire COTS, or SaaS contract

### Application Gaps
**What:** Application without technology infrastructure assigned
**Why:** Incomplete planning, transitional state, or legacy system
**Action:** Assign technology stack, plan migration, or decommission

### Utilization Gaps
**What:** Application supporting zero capabilities
**Why:** Obsolete system, wrong portfolio assessment, or transition limbo
**Action:** Retire application, repurpose, or identify missing capability

## Redundancy Analysis

### What It Shows
Applications that support the same capability (intentional redundancy = resilience).

### Why It Matters
- **Resilience:** Multiple apps supporting one capability = high availability
- **Consolidation:** Opportunity to retire duplicate applications
- **Cost:** Redundancy may be intentional but expensive

### Questions to Ask
- Is redundancy intentional (disaster recovery)?
- Can we consolidate to reduce licensing costs?
- Which is the preferred application going forward?

## Use Cases

**Phase C-D Planning (Application & Technology Architecture)**
- Input: Capabilities from Phase B + current application portfolio
- Output: Application gaps and technology architecture roadmap

**Portfolio Rationalization**
- Input: Complete IT application inventory with capability mappings
- Output: Candidates for retirement, consolidation, or investment

**Infrastructure Optimization**
- Input: Current application-to-technology mappings
- Output: Common technology dependencies and consolidation targets

**Migration Planning**
- Input: Current state mappings
- Output: Dependencies, sequencing requirements, impact analysis

**Governance & Planning**
- Input: Quarterly snapshots of the same landscape
- Output: Track architecture evolution and strategic alignment

## Key Features

✓ **Complete Visibility** - See business-to-IT alignment end-to-end
✓ **Gap Identification** - Actionable insights on unmet needs
✓ **Redundancy Detection** - Optimize for cost and resilience
✓ **Professional Format** - Ready for executive presentations
✓ **JSON Export** - Data reusable in other tools
✓ **Flexible Scale** - Works with 5-100+ capabilities and applications

## Integration with TOGAF ADM

**Phase B (Business Architecture)**
- Input: Business capabilities from Phase A
- Provides: Basis for application architecture in Phase C

**Phase C-D (Application & Technology Architecture)**
- Shows: How business is supported by current IT
- Identifies: Gaps and improvement opportunities for target architecture

**Phase E (Opportunities & Solutions)**
- Enables: Work package definition based on gaps
- Supports: Business case for application/technology investments

**Phase G (Implementation Governance)**
- Tracks: Progress of architectural changes
- Monitors: Alignment between business capabilities and IT

## Common Patterns

### Pattern 1: Healthy Coverage
- All capabilities have ≥1 application
- All applications support ≥1 capability
- Technology fully assigned
- **Action:** Optimize and maintain

### Pattern 2: Capability Gap
- Business capability without supporting application
- **Action:** Plan new application investment or SaaS contract

### Pattern 3: Application Overflow
- Many unused applications in portfolio
- **Action:** Retirement or consolidation planning

### Pattern 4: Technology Overlap
- Multiple applications using redundant technologies
- **Action:** Standardization and consolidation opportunity

### Pattern 5: Shadow IT
- Unmapped capabilities but mature business processes
- **Action:** Investigate shadow IT systems; consider application investment

## Requirements

- Python 3.6 or higher
- No external dependencies (uses Python standard library only)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Application appears both used and unused | Check mapping - app must support ≥1 capability |
| Too many gaps identified | Expected if migrating or building new IT landscape |
| Redundancy seems high | May be intentional (disaster recovery); document rationale |
| JSON export fails | Ensure write permissions in current directory |
| Output shows [NO TECHNOLOGY] | Application technology components not entered in Step 4 |

## Next Steps After Using This Skill

1. **Export the JSON** - Answer "y" to save complete mapping
2. **Identify Quick Wins** - Address capability gaps first
3. **Plan Rationalization** - Retire unused applications
4. **Optimize Infrastructure** - Consolidate redundant technologies
5. **Update Quarterly** - Track changes in business-IT alignment

---

**Skill Version:** 1.0
**Last Updated:** 2026-01-11
**Framework:** TOGAF ADM Phases C-E
**Use Case:** Portfolio Management & Architecture Planning
**Created for:** Enterprise Architecture Skills Project
