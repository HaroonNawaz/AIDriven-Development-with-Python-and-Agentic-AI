# Capability Matrix Builder Skill

## Overview
Generates business capability matrices with maturity assessment for TOGAF Phase B planning.

This skill automates the creation of professional capability assessment matrices that show the current and target maturity of business capabilities, calculate gaps, and prioritize investment areas.

## What It Does

**Input:** List of business capabilities with:
- Capability name and owner
- Current maturity level (1-5 scale)
- Target maturity level (1-5 scale)
- Investment level and status

**Processing:**
- Calculates maturity gaps (target - current)
- Generates visual heatmaps
- Prioritizes capabilities by gap size
- Provides investment distribution analysis

**Output:**
- Professional capability matrix table
- Visual maturity heatmaps (current and target state)
- Gap analysis with priority levels
- Summary statistics
- JSON export for further analysis

## Time Saved
**20-30 minutes per Phase B assessment** (vs. manual Excel/spreadsheet creation)

## Usage

### Quick Start (Demo Mode)
```bash
python capability_matrix_builder.py sample
```
See sample output without entering any data (2-3 seconds).

### Interactive Mode
```bash
python capability_matrix_builder.py interactive
```

**Steps:**
1. Enter each capability name and owner
2. Rate current maturity (1=Initial, 5=Optimized)
3. Rate target maturity (1=Initial, 5=Optimized)
4. Specify investment level (Low/Medium/High)
5. Specify status (On-Track/At-Risk/Off-Track)
6. Export to JSON (optional)

**Time to complete:** 10-15 minutes for 5 capabilities

### Expected Output

```
CAPABILITY MATURITY MATRIX - PHASE B ASSESSMENT
================================================

SUMMARY:
  Total Capabilities: 5
  Average Current Maturity: 2.4/5
  Average Target Maturity: 3.8/5
  Average Gap: 1.4 levels

[Detailed capability matrix]
[Current state heatmap]
[Target state heatmap]
[Gap analysis with priorities]
```

## Maturity Scale

| Level | Score | Definition |
|-------|-------|---|
| 1 | Initial | Ad-hoc, manual processes |
| 2 | Repeatable | Documented, some consistency |
| 3 | Defined | Standardized, well-understood |
| 4 | Managed | Measured, controlled |
| 5 | Optimized | Continuous improvement |

## Gap Interpretation

| Gap Size | Classification | Action |
|----------|---|---|
| +3 or more | [HIGH] | Significant investment needed |
| +2 to +3 | [MEDIUM] | Moderate improvement plan |
| +1 to +2 | [SMALL] | Minor enhancements |
| 0 or less | [OVER-MATURE] | Capability exceeds target |

## Use Cases

**Phase B Planning**
- Input: Capabilities identified from Phase A stakeholder interviews
- Output: Maturity gaps for work package definition in Phase E

**Investment Prioritization**
- Input: All business capabilities with current/target assessment
- Output: Ranked investment opportunities by gap and strategic importance

**Capability Roadmap**
- Input: Multi-year target maturity levels
- Output: Phased capability improvement roadmap

**Governance & Tracking**
- Input: Run quarterly with same capabilities
- Output: Progress tracking against maturity targets

## Key Features

✓ **Automated Calculations** - Gap analysis and statistics
✓ **Professional Format** - Ready for presentations and reports
✓ **Visual Heatmaps** - Quick pattern recognition with ASCII visualization
✓ **JSON Export** - Reusable data for PowerPoint, Excel, etc.
✓ **Flexible Scale** - Can assess 5-50+ capabilities
✓ **Multi-Dimension** - Tracks current, target, and gap simultaneously

## Integration with TOGAF ADM

**Phase B (Business Architecture)**
- Capability assessment is core Phase B deliverable
- Maturity gaps feed into Phase E work packages
- Results support business case development

**Related Outputs:**
- Business Capability Map
- Capability Gap Analysis
- Business Architecture baseline

## Requirements

- Python 3.6 or higher
- No external dependencies (uses Python standard library only)

## Common Questions

**Q: What's the difference between "current" and "target" maturity?**
A: Current = how mature the capability is today. Target = where you want it to be in 12-24 months.

**Q: Can I change the maturity scale?**
A: The code uses 1-5 scale by design. For different scales, modify the `MaturityLevel` enum.

**Q: What if a capability's current maturity exceeds target?**
A: The tool will show "OVER-MATURE" - this indicates the capability is performing above requirements (possible over-investment).

**Q: How do I use the JSON export?**
A: Open in Excel or import into PowerPoint. The structure is self-documenting.

**Q: Can I run this monthly or quarterly?**
A: Yes! Keep the same capability names and track maturity changes over time to monitor progress.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No output appears | Wait 1-2 seconds for processing; output is being generated |
| JSON export fails | Ensure you have write permissions in the current directory |
| Invalid input error | Use numeric scale 1-5; use exact keywords (Low/Medium/High) |
| Text display issues | Ensure terminal uses monospace font; increase font size if needed |

## Next Steps After Using This Skill

1. **Export the JSON** - Answer "y" to export prompt
2. **Create Visualizations** - Import JSON data into PowerPoint or Visio
3. **Share with Stakeholders** - Use exported data for governance meetings
4. **Set Targets** - Use assessment to establish 12-month capability roadmap
5. **Track Quarterly** - Rerun skill to measure progress against targets

---

**Skill Version:** 1.0
**Last Updated:** 2026-01-11
**Framework:** TOGAF ADM Phase B
**Created for:** Enterprise Architecture Skills Project
