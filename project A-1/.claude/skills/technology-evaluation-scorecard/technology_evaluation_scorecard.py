#!/usr/bin/env python3
"""
Skill: Technology Evaluation Scorecard Generator
Generates weighted evaluation matrices for technology selection decisions.

Creates scoring matrices for evaluating and comparing technologies
based on multiple criteria with adjustable weightings.

Usage:
    python technology_evaluation_scorecard.py interactive
    python technology_evaluation_scorecard.py sample
"""

import json


def get_recommendation_text(score):
    """Get recommendation based on score"""
    if score >= 85:
        return "[OK] STRONG RECOMMEND"
    elif score >= 75:
        return "[OK] RECOMMEND"
    elif score >= 65:
        return "[!] CONSIDER"
    else:
        return "[X] NOT RECOMMENDED"


def interactive_technology_evaluator():
    """Interactive technology evaluation"""

    print("\n" + "="*100)
    print("TECHNOLOGY EVALUATION SCORECARD GENERATOR")
    print("="*100)
    print("\nThis tool creates weighted scoring matrices for technology selection.")
    print("Rate each technology on each criterion (1-5 scale)\n")

    # Step 1: Define evaluation criteria
    print("-"*100)
    print("STEP 1: Define Evaluation Criteria")
    print("-"*100)
    print("Enter criteria to evaluate (e.g., Cost, Performance, Security, Scalability)")
    print("For each criterion, provide its importance weighting (total should = 100)\n")

    criteria = {}
    total_weight = 0

    while True:
        criterion = input("Criterion name (or 'done'): ").strip()
        if criterion.lower() == 'done':
            break

        weight = int(input(f"Weighting for {criterion} (1-100): ").strip())
        criteria[criterion] = weight
        total_weight += weight

    if total_weight != 100:
        print(f"\n[!] WARNING: Total weighting = {total_weight}% (should be 100%)")
        adjust = input("Adjust weightings? (y/n): ").strip().lower()
        if adjust == 'n':
            print("Continuing with unbalanced weights...\n")

    # Step 2: Define technologies to evaluate
    print("\n" + "-"*100)
    print("STEP 2: Technologies to Evaluate")
    print("-"*100)
    print("Enter technology names/options:\n")

    technologies = []
    while True:
        tech = input("Technology name (or 'done'): ").strip()
        if tech.lower() == 'done':
            break
        technologies.append(tech)

    # Step 3: Score each technology on each criterion
    print("\n" + "-"*100)
    print("STEP 3: Score Technologies (1-5 scale)")
    print("-"*100)
    print("For each technology, rate it on each criterion\n")

    scores = {}
    for tech in technologies:
        print(f"\n{tech}:")
        scores[tech] = {}
        for criterion in criteria.keys():
            score = int(input(f"  {criterion} (1-5): ").strip())
            scores[tech][criterion] = score

    # Calculate weighted scores
    results = calculate_scores(technologies, criteria, scores)

    # Display results
    display_evaluation_results(technologies, criteria, scores, results)

    # Export
    export_evaluation(technologies, criteria, scores, results)


def calculate_scores(technologies, criteria, scores):
    """Calculate weighted scores for each technology"""

    results = {}
    total_weight = sum(criteria.values())

    for tech in technologies:
        weighted_score = 0
        for criterion, weight in criteria.items():
            score = scores[tech][criterion]
            weighted_contribution = (score / 5) * (weight / total_weight) * 100
            weighted_score += weighted_contribution

        results[tech] = weighted_score

    return results


def display_evaluation_results(technologies, criteria, scores, results):
    """Display evaluation matrix and recommendations"""

    print("\n" + "="*120)
    print("TECHNOLOGY EVALUATION SCORECARD - RESULTS")
    print("="*120)

    # Scoring matrix
    print("\nDETAILED SCORING MATRIX:")
    print("-"*120)

    # Header
    header = "Technology".ljust(25)
    for criterion in criteria.keys():
        weight = criteria[criterion]
        header += f" | {criterion}({weight}%)"
    header += " | TOTAL SCORE | RECOMMENDATION"

    print(header)
    print("-"*120)

    # Data rows
    for tech in sorted(results.keys(), key=lambda x: results[x], reverse=True):
        row = tech[:25].ljust(25)

        # Individual scores
        for criterion in criteria.keys():
            score = scores[tech][criterion]
            row += f" | {score}/5"

        # Total score
        total = results[tech]
        row += f" | {total:.1f}/100"

        # Recommendation
        rec = get_recommendation_text(total)
        row += f" | {rec}"

        print(row)

    print("="*120)

    # Rankings
    print("\nRANKED RECOMMENDATIONS:")
    print("-"*60)
    ranking = sorted(results.items(), key=lambda x: x[1], reverse=True)
    for rank, (tech, score) in enumerate(ranking, 1):
        print(f"{rank}. {tech:<30} Score: {score:.1f}/100 {get_recommendation_text(score)}")

    # Detailed analysis
    print("\n" + "-"*60)
    print("DETAILED ANALYSIS:")
    print("-"*60)

    best_tech = ranking[0][0]
    best_score = ranking[0][1]

    print(f"\nBEST CHOICE: {best_tech}")
    print(f"Overall Score: {best_score:.1f}/100")

    # Strengths
    print(f"\nStrengths:")
    for criterion in criteria.keys():
        score = scores[best_tech][criterion]
        if score >= 4:
            print(f"  [+] {criterion}: {score}/5")

    # Weaknesses
    print(f"\nWeaknesses:")
    for criterion in criteria.keys():
        score = scores[best_tech][criterion]
        if score <= 2:
            print(f"  [-] {criterion}: {score}/5 (Consider improvement)")

    # Comparison with runner-up
    if len(ranking) > 1:
        runner_up = ranking[1][0]
        runner_score = ranking[1][1]
        print(f"\nComparison with {runner_up}:")
        print(f"  {best_tech}: {best_score:.1f}/100")
        print(f"  {runner_up}: {runner_score:.1f}/100")
        print(f"  Difference: {best_score - runner_score:.1f} points")


def generate_sample_evaluation():
    """Generate sample evaluation for demo"""

    technologies = ["Salesforce", "SAP Cloud", "Microsoft Dynamics"]
    criteria = {
        "Cost": 25,
        "Performance": 20,
        "Security": 25,
        "Scalability": 15,
        "Ease of Use": 15
    }

    scores = {
        "Salesforce": {
            "Cost": 3,
            "Performance": 4,
            "Security": 5,
            "Scalability": 5,
            "Ease of Use": 5
        },
        "SAP Cloud": {
            "Cost": 2,
            "Performance": 5,
            "Security": 5,
            "Scalability": 5,
            "Ease of Use": 2
        },
        "Microsoft Dynamics": {
            "Cost": 3,
            "Performance": 3,
            "Security": 4,
            "Scalability": 4,
            "Ease of Use": 4
        }
    }

    results = calculate_scores(technologies, criteria, scores)
    display_evaluation_results(technologies, criteria, scores, results)
    print("\n[This is a sample output]\n")


def export_evaluation(technologies, criteria, scores, results):
    """Export to JSON"""
    export = input("\nExport evaluation to JSON? (y/n): ").strip().lower()
    if export == 'y':
        export_data = {
            "technologies": technologies,
            "criteria": criteria,
            "scores": scores,
            "results": results
        }
        with open('technology_evaluation.json', 'w') as f:
            json.dump(export_data, f, indent=2)
        print("[OK] Evaluation exported to technology_evaluation.json")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "sample":
        generate_sample_evaluation()
    else:
        interactive_technology_evaluator()
