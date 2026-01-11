#!/usr/bin/env python3
"""
Skill: Business-to-IT Mapping Tool
Creates complete traceability from Business Capabilities -> Applications -> Technology.

Generates traceability matrices showing how business capabilities are supported
through applications and technology infrastructure with gap identification.

Usage:
    python business_to_it_mapper.py interactive
    python business_to_it_mapper.py sample
"""

import json


def interactive_business_to_it_mapper():
    """Interactive mapping of business capabilities to IT infrastructure"""

    print("\n" + "="*120)
    print("BUSINESS-TO-IT TRACEABILITY MAPPER")
    print("="*120)
    print("\nThis tool creates complete traceability from Business Capabilities through")
    print("Applications to Technology Infrastructure.\n")

    # Step 1: Define Business Capabilities
    print("-"*120)
    print("STEP 1: Define Business Capabilities")
    print("-"*120)
    print("Enter business capabilities to be supported (e.g., Customer Management, Order Processing)\n")

    capabilities = []
    cap_count = 1

    while True:
        cap_name = input(f"Capability #{cap_count} (or 'done'): ").strip()
        if cap_name.lower() == 'done':
            break
        owner = input(f"  Owner: ").strip()
        capabilities.append({
            "id": cap_count,
            "name": cap_name,
            "owner": owner,
            "applications": [],
            "status": "Mapped"
        })
        cap_count += 1

    # Step 2: Define Applications
    print("\n" + "-"*120)
    print("STEP 2: Define Applications")
    print("-"*120)
    print("Enter applications in the IT portfolio (e.g., Salesforce, SAP, Custom App)\n")

    applications = []
    app_count = 1

    while True:
        app_name = input(f"Application #{app_count} (or 'done'): ").strip()
        if app_name.lower() == 'done':
            break
        app_type = input(f"  Type (COTS/Custom/SaaS): ").strip()
        applications.append({
            "id": app_count,
            "name": app_name,
            "type": app_type,
            "technologies": [],
            "capabilities_supported": []
        })
        app_count += 1

    # Step 3: Map Capabilities to Applications
    print("\n" + "-"*120)
    print("STEP 3: Map Capabilities to Applications")
    print("-"*120)
    print("For each capability, select which applications support it (comma-separated app IDs)\n")

    for cap in capabilities:
        print(f"\nCapability: {cap['name']}")
        print("Available applications:")
        for app in applications:
            print(f"  {app['id']} = {app['name']} ({app['type']})")

        app_ids_input = input("Support applications (e.g., 1,2,3): ").strip()
        if app_ids_input:
            try:
                app_ids = [int(x.strip()) for x in app_ids_input.split(',')]
                for app_id in app_ids:
                    for app in applications:
                        if app['id'] == app_id:
                            cap['applications'].append(app['id'])
                            app['capabilities_supported'].append(cap['id'])
            except ValueError:
                print("Invalid input - skipping")

    # Step 4: Map Applications to Technology
    print("\n" + "-"*120)
    print("STEP 4: Map Applications to Technology Infrastructure")
    print("-"*120)
    print("For each application, select which technology components it uses (comma-separated)\n")

    technologies = {}
    tech_counter = {}

    for app in applications:
        print(f"\nApplication: {app['name']}")
        print("Enter technology components (e.g., Java, PostgreSQL, Docker, Kubernetes)")

        tech_input = input("Technology components (comma-separated): ").strip()
        if tech_input:
            for tech in tech_input.split(','):
                tech_name = tech.strip()
                if tech_name not in technologies:
                    tech_counter[tech_name] = len(technologies) + 1
                    technologies[tech_name] = {
                        "id": tech_counter[tech_name],
                        "name": tech_name,
                        "applications": []
                    }

                if app['id'] not in technologies[tech_name]['applications']:
                    technologies[tech_name]['applications'].append(app['id'])

                app['technologies'].append(tech_name)

    # Display results
    results = calculate_traceability(capabilities, applications, technologies)
    display_traceability_matrix(capabilities, applications, technologies, results)

    # Export
    export_mapping(capabilities, applications, technologies, results)


def calculate_traceability(capabilities, applications, technologies):
    """Calculate traceability metrics and gaps"""

    # Mapped capabilities
    mapped_capabilities = [c for c in capabilities if c['applications']]
    unmapped_capabilities = [c for c in capabilities if not c['applications']]

    # Mapped applications
    mapped_applications = [a for a in applications if a['capabilities_supported']]
    unused_applications = [a for a in applications if not a['capabilities_supported']]

    # Orphan applications (no technology)
    orphan_applications = [a for a in applications if not a['technologies']]

    return {
        "mapped_cap_count": len(mapped_capabilities),
        "unmapped_cap_count": len(unmapped_capabilities),
        "mapped_app_count": len(mapped_applications),
        "unused_app_count": len(unused_applications),
        "orphan_app_count": len(orphan_applications),
        "total_mappings": sum(len(c['applications']) for c in capabilities),
        "technology_count": len(technologies),
        "unmapped_capabilities": unmapped_capabilities,
        "unused_applications": unused_applications,
        "orphan_applications": orphan_applications
    }


def display_traceability_matrix(capabilities, applications, technologies, results):
    """Display complete traceability matrix"""

    print("\n" + "="*140)
    print("BUSINESS-TO-IT TRACEABILITY MATRIX")
    print("="*140)

    # Summary statistics
    print(f"\nTRACEABILITY SUMMARY:")
    print(f"  Capabilities: {len(capabilities)} ({results['mapped_cap_count']} mapped, {results['unmapped_cap_count']} unmapped)")
    print(f"  Applications: {len(applications)} ({results['mapped_app_count']} used, {results['unused_app_count']} unused)")
    print(f"  Technology Components: {results['technology_count']}")
    print(f"  Total Capability-to-Application Mappings: {results['total_mappings']}\n")

    # Capability to Application Mapping
    print("-"*140)
    print("CAPABILITY-TO-APPLICATION MAPPINGS:")
    print("-"*140)
    print(f"{'Cap ID':<6} {'Capability':<30} {'Owner':<20} {'Applications':<70}")
    print("-"*140)

    for cap in sorted(capabilities, key=lambda x: x['id']):
        app_names = []
        for app_id in cap['applications']:
            for app in applications:
                if app['id'] == app_id:
                    app_names.append(f"{app['name']}({app['type'][0]})")

        if app_names:
            apps_str = ", ".join(app_names)
        else:
            apps_str = "[UNMAPPED]"

        print(f"{cap['id']:<6} {cap['name']:<30} {cap['owner']:<20} {apps_str:<70}")

    # Application to Technology Mapping
    print("\n" + "-"*140)
    print("APPLICATION-TO-TECHNOLOGY MAPPINGS:")
    print("-"*140)
    print(f"{'App ID':<6} {'Application':<25} {'Type':<10} {'Technology Stack':<90}")
    print("-"*140)

    for app in sorted(applications, key=lambda x: x['id']):
        tech_str = ", ".join(app['technologies']) if app['technologies'] else "[NO TECHNOLOGY]"
        print(f"{app['id']:<6} {app['name']:<25} {app['type']:<10} {tech_str:<90}")

    # Technology Layer
    print("\n" + "-"*140)
    print("TECHNOLOGY INFRASTRUCTURE LAYER:")
    print("-"*140)
    print(f"{'Tech ID':<8} {'Technology':<25} {'Supporting Applications':<100}")
    print("-"*140)

    for tech_name in sorted(technologies.keys()):
        tech = technologies[tech_name]
        app_names = []
        for app_id in tech['applications']:
            for app in applications:
                if app['id'] == app_id:
                    app_names.append(app['name'])
        apps_str = ", ".join(sorted(app_names))
        print(f"{tech['id']:<8} {tech_name:<25} {apps_str:<100}")

    print("="*140)

    # Gap Analysis
    print("\nGAP ANALYSIS:")
    print("-"*80)

    if results['unmapped_capabilities']:
        print("\n[CAPABILITY GAPS] - Capabilities without supporting applications:")
        for cap in results['unmapped_capabilities']:
            print(f"  • {cap['name']} (Owner: {cap['owner']}) - ACTION: Identify/Build application")

    if results['orphan_applications']:
        print("\n[APPLICATION GAPS] - Applications without technology infrastructure:")
        for app in results['orphan_applications']:
            print(f"  • {app['name']} ({app['type']}) - ACTION: Assign technology components")

    if results['unused_applications']:
        print("\n[UTILIZATION GAPS] - Applications not supporting any capability:")
        for app in results['unused_applications']:
            print(f"  • {app['name']} ({app['type']}) - ACTION: Retire or repurpose")

    if not results['unmapped_capabilities'] and not results['orphan_applications'] and not results['unused_applications']:
        print("\n[OK] Complete traceability achieved - No gaps identified")

    # Redundancy Analysis
    print("\n" + "-"*80)
    print("REDUNDANCY ANALYSIS:")
    capability_app_map = {}
    for cap in capabilities:
        capability_app_map[cap['id']] = len(cap['applications'])

    multiple_support = [c for c in capabilities if len(c['applications']) > 1]
    if multiple_support:
        print(f"\nCapabilities supported by multiple applications (redundancy/overlap):")
        for cap in multiple_support:
            print(f"  • {cap['name']}: {len(cap['applications'])} applications")
    else:
        print("\nNo redundant capability support - Each capability has single application")

    print("="*140)


def generate_sample_mapping():
    """Generate sample traceability mapping for demo"""

    capabilities = [
        {"id": 1, "name": "Customer Management", "owner": "Sales", "applications": [1, 2], "status": "Mapped"},
        {"id": 2, "name": "Order Processing", "owner": "Operations", "applications": [2, 3], "status": "Mapped"},
        {"id": 3, "name": "Financial Reporting", "owner": "Finance", "applications": [4], "status": "Mapped"},
        {"id": 4, "name": "HR & Payroll", "owner": "HR", "applications": [], "status": "Unmapped"},
    ]

    applications = [
        {"id": 1, "name": "Salesforce", "type": "SaaS", "technologies": ["AWS", "REST API", "PostgreSQL"], "capabilities_supported": [1]},
        {"id": 2, "name": "SAP ECC", "type": "COTS", "technologies": ["On-Premise", "Oracle DB", "Java"], "capabilities_supported": [1, 2]},
        {"id": 3, "name": "Order API", "type": "Custom", "technologies": ["Kubernetes", "Python", "PostgreSQL", "Redis"], "capabilities_supported": [2]},
        {"id": 4, "name": "BI Dashboard", "type": "SaaS", "technologies": ["AWS", "Tableau", "PostgreSQL"], "capabilities_supported": [3]},
        {"id": 5, "name": "Legacy HR System", "type": "COTS", "technologies": [], "capabilities_supported": []},
    ]

    technologies = {
        "AWS": {"id": 1, "name": "AWS", "applications": [1, 4]},
        "Kubernetes": {"id": 2, "name": "Kubernetes", "applications": [3]},
        "PostgreSQL": {"id": 3, "name": "PostgreSQL", "applications": [1, 2, 3, 4]},
        "Oracle DB": {"id": 4, "name": "Oracle DB", "applications": [2]},
        "Java": {"id": 5, "name": "Java", "applications": [2]},
        "Python": {"id": 6, "name": "Python", "applications": [3]},
        "REST API": {"id": 7, "name": "REST API", "applications": [1]},
        "Tableau": {"id": 8, "name": "Tableau", "applications": [4]},
        "Redis": {"id": 9, "name": "Redis", "applications": [3]},
        "On-Premise": {"id": 10, "name": "On-Premise", "applications": [2]},
    }

    results = calculate_traceability(capabilities, applications, technologies)
    display_traceability_matrix(capabilities, applications, technologies, results)
    print("\n[This is a sample output]\n")


def export_mapping(capabilities, applications, technologies, results):
    """Export traceability mapping to JSON"""
    export = input("\nExport mapping to JSON? (y/n): ").strip().lower()
    if export == 'y':
        export_data = {
            "capabilities": capabilities,
            "applications": applications,
            "technologies": {k: v for k, v in technologies.items()},
            "results": {
                "mapped_capabilities": results['mapped_cap_count'],
                "unmapped_capabilities": results['unmapped_cap_count'],
                "used_applications": results['mapped_app_count'],
                "unused_applications": results['unused_app_count'],
                "orphan_applications": results['orphan_app_count'],
                "total_mappings": results['total_mappings'],
                "technology_count": results['technology_count']
            }
        }
        with open('business_to_it_mapping.json', 'w') as f:
            json.dump(export_data, f, indent=2)
        print("[OK] Mapping exported to business_to_it_mapping.json")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "sample":
        generate_sample_mapping()
    else:
        interactive_business_to_it_mapper()
