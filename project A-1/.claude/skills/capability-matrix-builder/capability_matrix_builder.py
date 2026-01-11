#!/usr/bin/env python3
"""
Skill: Capability Matrix Builder
Generates business capability matrices with maturity assessment and visualization.

Creates professional capability matrices for Phase B planning, showing:
- Capability names and owners
- Current vs target maturity
- Investment level and status
- Color-coded heatmap

Usage:
    python capability_matrix_builder.py interactive
    python capability_matrix_builder.py sample
"""

import json
from enum import Enum


class MaturityLevel(Enum):
    INITIAL = (1, "Initial")
    REPEATABLE = (2, "Repeatable")
    DEFINED = (3, "Defined")
    MANAGED = (4, "Managed")
    OPTIMIZED = (5, "Optimized")


def get_maturity_color(score):
    """Get visual indicator for maturity level"""
    if score <= 1:
        return "[RED]"
    elif score == 2:
        return "[ORANGE]"
    elif score == 3:
        return "[YELLOW]"
    elif score == 4:
        return "[GREEN]"
    else:
        return "[BLUE]"


def get_gap_color(gap):
    """Classify gap size"""
    if gap <= 0:
        return "[OVER-MATURE]"
    elif gap <= 1:
        return "[SMALL]"
    elif gap <= 2:
        return "[MEDIUM]"
    else:
        return "[LARGE]"


def interactive_capability_builder():
    """Interactive capability matrix builder"""

    print("\n" + "="*100)
    print("CAPABILITY MATRIX BUILDER - Interactive Mode")
    print("="*100)
    print("\nFor each capability, rate current and target maturity (1-5):")
    print("  1=Initial, 2=Repeatable, 3=Defined, 4=Managed, 5=Optimized\n")

    capabilities = []
    cap_count = 1

    while True:
        print(f"\n--- Capability #{cap_count} ---")
        cap_name = input("Capability name (or 'done' to finish): ").strip()

        if cap_name.lower() == 'done':
            break

        owner = input("Owner/Department: ").strip()
        current = int(input("Current maturity (1-5): ").strip())
        target = int(input("Target maturity (1-5): ").strip())
        investment = input("Investment level (Low/Medium/High): ").strip()
        status = input("Status (On-Track/At-Risk/Off-Track): ").strip()

        gap = target - current

        capabilities.append({
            "id": cap_count,
            "name": cap_name,
            "owner": owner,
            "current": current,
            "target": target,
            "gap": gap,
            "investment": investment,
            "status": status
        })

        cap_count += 1

    if capabilities:
        display_capability_matrix(capabilities)
        export_matrix(capabilities)


def display_capability_matrix(capabilities):
    """Display formatted capability matrix"""

    print("\n" + "="*140)
    print("CAPABILITY MATURITY MATRIX - PHASE B ASSESSMENT")
    print("="*140)

    # Summary statistics
    total_caps = len(capabilities)
    avg_current = sum(c['current'] for c in capabilities) / total_caps
    avg_target = sum(c['target'] for c in capabilities) / total_caps
    avg_gap = sum(c['gap'] for c in capabilities) / total_caps

    print(f"\nSUMMARY:")
    print(f"  Total Capabilities: {total_caps}")
    print(f"  Average Current Maturity: {avg_current:.1f}/5")
    print(f"  Average Target Maturity: {avg_target:.1f}/5")
    print(f"  Average Gap: {avg_gap:.1f} levels\n")

    # Count by investment
    investment_counts = {}
    for cap in capabilities:
        inv = cap['investment']
        investment_counts[inv] = investment_counts.get(inv, 0) + 1

    print(f"Investment Distribution:")
    for inv, count in sorted(investment_counts.items()):
        print(f"  {inv}: {count} capabilities")

    # Main matrix
    print("\n" + "-"*140)
    print(f"{'ID':<4} {'Capability':<25} {'Owner':<20} {'Cur':<4} {'Tgt':<4} {'Gap':<12} {'Investment':<10} {'Status':<12}")
    print("-"*140)

    for cap in sorted(capabilities, key=lambda x: x['gap'], reverse=True):
        cap_name = cap['name'][:25]
        owner = cap['owner'][:20]
        current_str = f"{cap['current']}/5"
        target_str = f"{cap['target']}/5"
        gap_str = f"{cap['gap']:+d} {get_gap_color(cap['gap'])}"
        investment = cap['investment'][:10]
        status = cap['status'][:12]

        print(f"{cap['id']:<4} {cap_name:<25} {owner:<20} {current_str:<4} {target_str:<4} {gap_str:<12} {investment:<10} {status:<12}")

    print("="*140)

    # Heatmap visualization
    print("\nCAPABILITY MATURITY HEATMAP (Current State):")
    print("-"*60)
    for cap in sorted(capabilities, key=lambda x: x['current'], reverse=True):
        maturity_bar = "#" * cap['current'] + "-" * (5 - cap['current'])
        color = get_maturity_color(cap['current'])
        print(f"{cap['name'][:30]:<30} {maturity_bar} {color}")

    print("\nCAPABILITY MATURITY HEATMAP (Target State):")
    print("-"*60)
    for cap in sorted(capabilities, key=lambda x: x['target'], reverse=True):
        maturity_bar = "#" * cap['target'] + "-" * (5 - cap['target'])
        color = get_maturity_color(cap['target'])
        print(f"{cap['name'][:30]:<30} {maturity_bar} {color}")

    # Gap analysis
    print("\nGAP ANALYSIS (Priority Order):")
    print("-"*60)
    for cap in sorted(capabilities, key=lambda x: x['gap'], reverse=True):
        if cap['gap'] > 0:
            priority = "[HIGH]" if cap['gap'] >= 3 else "[MEDIUM]" if cap['gap'] >= 2 else "[LOW]"
            print(f"{cap['name']:<30} Gap: {cap['gap']} levels | Investment: {cap['investment']:<8} | {priority}")


def generate_sample_matrix():
    """Generate sample for demo"""

    sample_capabilities = [
        {
            "id": 1,
            "name": "Customer Management",
            "owner": "Sales",
            "current": 2,
            "target": 4,
            "gap": 2,
            "investment": "High",
            "status": "On-Track"
        },
        {
            "id": 2,
            "name": "Order Management",
            "owner": "Operations",
            "current": 2,
            "target": 4,
            "gap": 2,
            "investment": "High",
            "status": "On-Track"
        },
        {
            "id": 3,
            "name": "Billing",
            "owner": "Finance",
            "current": 3,
            "target": 4,
            "gap": 1,
            "investment": "Medium",
            "status": "On-Track"
        },
        {
            "id": 4,
            "name": "Product Management",
            "owner": "Product",
            "current": 1,
            "target": 3,
            "gap": 2,
            "investment": "High",
            "status": "At-Risk"
        },
        {
            "id": 5,
            "name": "Analytics & Reporting",
            "owner": "IT",
            "current": 2,
            "target": 4,
            "gap": 2,
            "investment": "High",
            "status": "On-Track"
        }
    ]

    display_capability_matrix(sample_capabilities)
    print("\n[This is a sample output]\n")


def export_matrix(capabilities):
    """Export to JSON"""
    export = input("\nExport matrix to JSON? (y/n): ").strip().lower()
    if export == 'y':
        with open('capability_matrix.json', 'w') as f:
            json.dump(capabilities, f, indent=2)
        print("[OK] Matrix exported to capability_matrix.json")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "sample":
        generate_sample_matrix()
    else:
        interactive_capability_builder()
