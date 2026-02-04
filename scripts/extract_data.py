#!/usr/bin/env python3
"""
DataStackGuide — Data extraction from jobs.db to JSON.
Reads the SQLite database and produces JSON files consumed by Astro at build time.

Usage:
    python3 scripts/extract_data.py
    python3 scripts/extract_data.py --db /path/to/jobs.db
"""

import sqlite3
import json
import sys
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Default DB path — override with --db flag
DEFAULT_DB = "/Users/rome/Documents/projects/scrapers/master/data/jobs.db"
OUTPUT_DIR = Path(__file__).parent.parent / "data"

# ── Site category taxonomy ──
# Maps our 12 site categories to database categories.
# A tool can appear in multiple site categories.
SITE_CATEGORIES = {
    "enrichment": {
        "name": "Data Enrichment",
        "slug": "enrichment",
        "description": "Tools that append firmographic, technographic, and contact data to your existing records. Fill the gaps in your CRM without manual research.",
        "color": "#14B8A6",
        "icon": "🔍",
        "db_categories": ["Data_Enrichment", "Data_Providers"],
    },
    "cleaning": {
        "name": "Data Cleaning & Hygiene",
        "slug": "cleaning",
        "description": "Deduplication, standardization, and formatting tools that keep your CRM data accurate and usable.",
        "color": "#10B981",
        "icon": "🧹",
        "db_categories": ["RevOps_Data_Quality"],
    },
    "validation": {
        "name": "Data Validation",
        "slug": "validation",
        "description": "Verify emails, phone numbers, and addresses before they enter your CRM. Catch bad data at the source.",
        "color": "#06B6D4",
        "icon": "✓",
        "db_categories": ["RevOps_Data_Quality", "Data_Providers"],
    },
    "intent": {
        "name": "Intent Data",
        "slug": "intent",
        "description": "Identify accounts actively researching solutions like yours. Know who's in-market before they fill out a form.",
        "color": "#8B5CF6",
        "icon": "📡",
        "db_categories": ["Intent_Data", "ABM_Signals", "Visitor_Identification"],
    },
    "orchestration": {
        "name": "Data Orchestration",
        "slug": "orchestration",
        "description": "Move data between systems, sync CRM fields, and automate data workflows across your stack.",
        "color": "#F59E0B",
        "icon": "⚡",
        "db_categories": ["Integration_iPaaS", "Reverse_ETL"],
    },
    "abm": {
        "name": "ABM & Targeting",
        "slug": "abm",
        "description": "Account-based marketing platforms for targeting, advertising, and engaging high-value accounts.",
        "color": "#EF4444",
        "icon": "🎯",
        "db_categories": ["ABM_Platforms", "ABM_Advertising"],
    },
    "healthcare": {
        "name": "Healthcare Data",
        "slug": "healthcare",
        "description": "NPI-verified provider data, practice intelligence, and healthcare-specific enrichment for medical sales teams.",
        "color": "#3B82F6",
        "icon": "🏥",
        "db_categories": [],  # Manual tools only (Provyx, Definitive Healthcare)
    },
    "technographic": {
        "name": "Technographic Data",
        "slug": "technographic",
        "description": "See what technology your prospects use. Target by tech stack, identify displacement opportunities.",
        "color": "#EC4899",
        "icon": "💻",
        "db_categories": ["Data_Enrichment", "Data_Providers"],
    },
    "list-building": {
        "name": "List Building & Prospecting",
        "slug": "list-building",
        "description": "Build targeted prospect lists from scratch. Search by industry, title, company size, and more.",
        "color": "#F97316",
        "icon": "📋",
        "db_categories": ["Sales_Engagement_Growth", "Sales_Engagement_Enterprise", "Data_Providers"],
    },
    "contact-databases": {
        "name": "Contact Databases",
        "slug": "contact-databases",
        "description": "Access millions of verified B2B contacts. Direct dials, emails, and professional profiles.",
        "color": "#6366F1",
        "icon": "📇",
        "db_categories": ["Data_Providers", "Data_Enrichment"],
    },
    "data-quality": {
        "name": "Data Quality & Governance",
        "slug": "data-quality",
        "description": "Monitor, score, and improve data quality across your systems. Prevent bad data from entering your pipeline.",
        "color": "#10B981",
        "icon": "📊",
        "db_categories": ["RevOps_Data_Quality", "Reverse_ETL"],
    },
    "crm": {
        "name": "CRM Platforms",
        "slug": "crm",
        "description": "Customer relationship management platforms where your data lives. The system of record for sales and marketing.",
        "color": "#3B82F6",
        "icon": "🗃️",
        "db_categories": ["CRM_Enterprise", "CRM_MidMarket"],
    },
}

# Manual tools that don't exist in DB but should be in the directory
MANUAL_TOOLS = [
    {
        "name": "Verum",
        "slug": "verum",
        "description": "Done-for-you data cleaning, enrichment, and validation services. Projects start at $500.",
        "website": "https://veruminc.com",
        "categories": ["enrichment", "cleaning", "validation", "abm", "list-building"],
        "is_service": True,
        "pricing_model": "Project-based",
        "pricing_note": "Starting at $500",
    },
    {
        "name": "Provyx",
        "slug": "provyx",
        "description": "NPI-verified healthcare provider data across 40+ specialties. Pay-per-record, no contracts.",
        "website": "https://getprovyx.com",
        "categories": ["healthcare", "enrichment", "technographic", "list-building", "contact-databases"],
        "is_service": True,
        "pricing_model": "Pay-per-record",
        "pricing_note": "No annual contracts",
    },
    {
        "name": "Definitive Healthcare",
        "slug": "definitive-healthcare",
        "description": "Healthcare commercial intelligence platform with provider, claims, and reference data.",
        "website": "https://www.definitivehc.com",
        "categories": ["healthcare", "contact-databases"],
        "is_service": False,
        "pricing_model": "Enterprise",
        "pricing_note": "Custom pricing",
    },
]


def get_db_path():
    """Get DB path from args or default."""
    for i, arg in enumerate(sys.argv):
        if arg == "--db" and i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return DEFAULT_DB


def slugify(name):
    """Convert tool name to URL slug."""
    return (
        name.lower()
        .replace(".", "")
        .replace("(", "")
        .replace(")", "")
        .replace("'", "")
        .replace(",", "")
        .replace("&", "and")
        .replace("/", "-")
        .replace(" ", "-")
        .replace("--", "-")
        .strip("-")
    )


def map_tool_to_site_categories(db_category, tool_name):
    """Map a database category to site categories."""
    site_cats = []
    for slug, cat in SITE_CATEGORIES.items():
        if db_category in cat["db_categories"]:
            site_cats.append(slug)
    return site_cats


def extract_tools(conn):
    """Extract tool data from jobs.db."""
    cursor = conn.cursor()

    # Get tool stats
    cursor.execute("""
        SELECT
            jt.tool_name,
            jt.tool_category,
            COUNT(DISTINCT jt.job_id) as job_count,
            COUNT(DISTINCT j.company_name_normalized) as unique_companies,
            ROUND(AVG(CASE WHEN j.annual_salary_min > 30000 THEN j.annual_salary_min END)) as avg_salary_min,
            ROUND(AVG(CASE WHEN j.annual_salary_max > 30000 THEN j.annual_salary_max END)) as avg_salary_max
        FROM job_tools jt
        JOIN jobs j ON jt.job_id = j.id
        WHERE jt.tool_category NOT IN ('_none', 'AI_languages', 'AI_infrastructure', 'AI_techniques')
        GROUP BY jt.tool_name, jt.tool_category
        HAVING COUNT(DISTINCT jt.job_id) >= 1
        ORDER BY job_count DESC
    """)

    tools = {}
    for row in cursor.fetchall():
        tool_name, db_cat, job_count, companies, sal_min, sal_max = row
        slug = slugify(tool_name)
        site_cats = map_tool_to_site_categories(db_cat, tool_name)

        if not site_cats:
            continue  # Skip tools not in our categories

        if slug in tools:
            # Tool exists from another DB category — merge
            tools[slug]["job_count"] += job_count
            tools[slug]["unique_companies"] = max(tools[slug]["unique_companies"], companies)
            for cat in site_cats:
                if cat not in tools[slug]["categories"]:
                    tools[slug]["categories"].append(cat)
        else:
            tools[slug] = {
                "name": tool_name,
                "slug": slug,
                "description": "",
                "categories": site_cats,
                "primary_category": site_cats[0] if site_cats else "enrichment",
                "job_count": job_count,
                "unique_companies": companies,
                "salary_min": int(sal_min) if sal_min else None,
                "salary_max": int(sal_max) if sal_max else None,
                "is_service": False,
                "db_category": db_cat,
            }

    # Add manual tools
    for manual in MANUAL_TOOLS:
        slug = manual["slug"]
        if slug in tools:
            # Merge manual data with DB data
            tools[slug].update({
                "description": manual["description"],
                "website": manual.get("website"),
                "is_service": manual.get("is_service", False),
                "pricing_model": manual.get("pricing_model"),
                "pricing_note": manual.get("pricing_note"),
            })
            for cat in manual["categories"]:
                if cat not in tools[slug]["categories"]:
                    tools[slug]["categories"].append(cat)
        else:
            tools[slug] = {
                "name": manual["name"],
                "slug": slug,
                "description": manual["description"],
                "categories": manual["categories"],
                "primary_category": manual["categories"][0],
                "job_count": 0,
                "unique_companies": 0,
                "salary_min": None,
                "salary_max": None,
                "is_service": manual.get("is_service", False),
                "website": manual.get("website"),
                "pricing_model": manual.get("pricing_model"),
                "pricing_note": manual.get("pricing_note"),
                "db_category": None,
            }

    return tools


def extract_cooccurrence(conn):
    """Extract tool co-occurrence data."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            jt1.tool_name as tool_a,
            jt2.tool_name as tool_b,
            COUNT(*) as co_occurrences
        FROM job_tools jt1
        JOIN job_tools jt2 ON jt1.job_id = jt2.job_id AND jt1.tool_name < jt2.tool_name
        WHERE jt1.tool_category NOT IN ('AI_languages', 'AI_infrastructure', 'AI_techniques', '_none')
          AND jt2.tool_category NOT IN ('AI_languages', 'AI_infrastructure', 'AI_techniques', '_none')
        GROUP BY jt1.tool_name, jt2.tool_name
        HAVING COUNT(*) >= 3
        ORDER BY co_occurrences DESC
    """)

    pairs = {}
    for tool_a, tool_b, count in cursor.fetchall():
        slug_a = slugify(tool_a)
        slug_b = slugify(tool_b)

        if slug_a not in pairs:
            pairs[slug_a] = []
        if slug_b not in pairs:
            pairs[slug_b] = []

        pairs[slug_a].append({"tool": tool_b, "slug": slug_b, "count": count})
        pairs[slug_b].append({"tool": tool_a, "slug": slug_a, "count": count})

    # Sort each tool's pairs by count
    for slug in pairs:
        pairs[slug].sort(key=lambda x: x["count"], reverse=True)

    return pairs


def extract_trends(conn):
    """Extract monthly trend data."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            strftime('%Y-%m', j.date_posted) as month,
            jt.tool_name,
            COUNT(*) as mentions
        FROM job_tools jt
        JOIN jobs j ON jt.job_id = j.id
        WHERE j.date_posted >= date('now', '-12 months')
          AND jt.tool_category NOT IN ('AI_languages', 'AI_infrastructure', 'AI_techniques', '_none')
        GROUP BY month, jt.tool_name
        HAVING COUNT(*) >= 2
        ORDER BY month DESC, mentions DESC
    """)

    trends = {}
    for month, tool_name, mentions in cursor.fetchall():
        if month not in trends:
            trends[month] = []
        trends[month].append({
            "tool": tool_name,
            "slug": slugify(tool_name),
            "mentions": mentions,
        })

    return trends


def build_categories(tools):
    """Build category data with tool counts and tool lists."""
    categories = {}

    for slug, cat_def in SITE_CATEGORIES.items():
        # Find tools in this category
        cat_tools = []
        for tool_slug, tool in tools.items():
            if slug in tool.get("categories", []):
                cat_tools.append({
                    "name": tool["name"],
                    "slug": tool["slug"],
                    "job_count": tool["job_count"],
                    "description": tool.get("description", ""),
                    "is_service": tool.get("is_service", False),
                })

        cat_tools.sort(key=lambda x: x["job_count"], reverse=True)

        categories[slug] = {
            "name": cat_def["name"],
            "slug": slug,
            "description": cat_def["description"],
            "color": cat_def["color"],
            "icon": cat_def["icon"],
            "tool_count": len(cat_tools),
            "tools": cat_tools,
        }

    return categories


def extract_tool_details(conn, tools):
    """Extract detailed per-tool data: company stages, seniority, functions, top companies."""
    cursor = conn.cursor()
    details = {}

    for slug, tool in tools.items():
        tool_name = tool["name"]

        # Company stage distribution
        cursor.execute("""
            SELECT j.company_stage, COUNT(DISTINCT jt.job_id) as cnt
            FROM job_tools jt
            JOIN jobs j ON jt.job_id = j.id
            WHERE jt.tool_name = ? AND j.company_stage IS NOT NULL AND j.company_stage != 'Unknown'
            GROUP BY j.company_stage
            ORDER BY cnt DESC
        """, (tool_name,))
        company_stages = {row[0]: row[1] for row in cursor.fetchall()}

        # Seniority distribution
        cursor.execute("""
            SELECT j.seniority_tier, COUNT(DISTINCT jt.job_id) as cnt
            FROM job_tools jt
            JOIN jobs j ON jt.job_id = j.id
            WHERE jt.tool_name = ? AND j.seniority_tier IS NOT NULL AND j.seniority_tier != 'unknown'
            GROUP BY j.seniority_tier
            ORDER BY cnt DESC
        """, (tool_name,))
        seniority = {row[0]: row[1] for row in cursor.fetchall()}

        # Function category distribution
        cursor.execute("""
            SELECT j.function_category, COUNT(DISTINCT jt.job_id) as cnt
            FROM job_tools jt
            JOIN jobs j ON jt.job_id = j.id
            WHERE jt.tool_name = ? AND j.function_category IS NOT NULL
            GROUP BY j.function_category
            ORDER BY cnt DESC
        """, (tool_name,))
        functions = {row[0]: row[1] for row in cursor.fetchall()}

        # Top hiring companies
        cursor.execute("""
            SELECT j.company_name_normalized, COUNT(DISTINCT jt.job_id) as cnt
            FROM job_tools jt
            JOIN jobs j ON jt.job_id = j.id
            WHERE jt.tool_name = ? AND j.company_name_normalized IS NOT NULL
            GROUP BY j.company_name_normalized
            ORDER BY cnt DESC
            LIMIT 10
        """, (tool_name,))
        top_companies = [{"name": row[0], "jobs": row[1]} for row in cursor.fetchall()]

        # Remote vs onsite
        cursor.execute("""
            SELECT
                SUM(CASE WHEN j.is_remote = 1 THEN 1 ELSE 0 END) as remote,
                SUM(CASE WHEN j.is_remote = 0 OR j.is_remote IS NULL THEN 1 ELSE 0 END) as onsite
            FROM job_tools jt
            JOIN jobs j ON jt.job_id = j.id
            WHERE jt.tool_name = ?
        """, (tool_name,))
        row = cursor.fetchone()
        remote_split = {"remote": row[0] or 0, "onsite": row[1] or 0}

        # Top job titles
        cursor.execute("""
            SELECT j.title, COUNT(*) as cnt
            FROM job_tools jt
            JOIN jobs j ON jt.job_id = j.id
            WHERE jt.tool_name = ?
            GROUP BY j.title
            ORDER BY cnt DESC
            LIMIT 5
        """, (tool_name,))
        top_titles = [{"title": row[0], "count": row[1]} for row in cursor.fetchall()]

        details[slug] = {
            "company_stages": company_stages,
            "seniority": seniority,
            "functions": functions,
            "top_companies": top_companies,
            "remote_split": remote_split,
            "top_titles": top_titles,
        }

    return details


def get_total_jobs(conn):
    """Get total job count."""
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM jobs")
    return cursor.fetchone()[0]


def get_total_companies(conn):
    """Get total unique companies."""
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT company_name_normalized) FROM jobs WHERE company_name_normalized IS NOT NULL")
    return cursor.fetchone()[0]


def main():
    db_path = get_db_path()
    print(f"Connecting to {db_path}...")

    conn = sqlite3.connect(db_path)
    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / "reports").mkdir(exist_ok=True)

    total_jobs = get_total_jobs(conn)
    total_companies = get_total_companies(conn)
    print(f"Database: {total_jobs:,} jobs, {total_companies:,} companies")

    # Extract tools
    print("Extracting tools...")
    tools = extract_tools(conn)
    tools_list = sorted(tools.values(), key=lambda x: x["job_count"], reverse=True)

    with open(OUTPUT_DIR / "tools.json", "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "total_jobs_analyzed": total_jobs,
            "total_companies": total_companies,
            "tool_count": len(tools_list),
            "tools": tools_list,
        }, f, indent=2)
    print(f"  → {len(tools_list)} tools exported")

    # Build categories
    print("Building categories...")
    categories = build_categories(tools)
    cats_list = sorted(categories.values(), key=lambda x: x["tool_count"], reverse=True)

    with open(OUTPUT_DIR / "categories.json", "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "categories": cats_list,
        }, f, indent=2)
    print(f"  → {len(cats_list)} categories exported")

    # Co-occurrence
    print("Extracting co-occurrence data...")
    cooc = extract_cooccurrence(conn)

    with open(OUTPUT_DIR / "cooccurrence.json", "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "cooccurrence": cooc,
        }, f, indent=2)
    print(f"  → co-occurrence data for {len(cooc)} tools")

    # Trends
    print("Extracting trends...")
    trends = extract_trends(conn)

    with open(OUTPUT_DIR / "trends.json", "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "trends": trends,
        }, f, indent=2)
    print(f"  → trends for {len(trends)} months")

    # Per-tool details
    print("Extracting per-tool details...")
    tool_details = extract_tool_details(conn, tools)

    with open(OUTPUT_DIR / "tool_details.json", "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "details": tool_details,
        }, f, indent=2)
    print(f"  → details for {len(tool_details)} tools")

    # Market signals (for homepage)
    print("Building market signals...")
    top_tools = tools_list[:20]
    signals = {
        "generated_at": datetime.now().isoformat(),
        "total_jobs_analyzed": total_jobs,
        "total_companies": total_companies,
        "total_tools_tracked": len(tools_list),
        "top_tools": [
            {"name": t["name"], "slug": t["slug"], "job_count": t["job_count"],
             "categories": t["categories"]}
            for t in top_tools
        ],
    }

    with open(OUTPUT_DIR / "market_signals.json", "w") as f:
        json.dump(signals, f, indent=2)
    print(f"  → market signals with top {len(top_tools)} tools")

    # Metadata
    with open(OUTPUT_DIR / "metadata.json", "w") as f:
        json.dump({
            "last_updated": datetime.now().isoformat(),
            "total_jobs": total_jobs,
            "total_companies": total_companies,
            "total_tools": len(tools_list),
            "data_files": [
                "tools.json",
                "categories.json",
                "cooccurrence.json",
                "trends.json",
                "tool_details.json",
                "market_signals.json",
            ],
        }, f, indent=2)

    conn.close()
    print("\nExtraction complete.")


if __name__ == "__main__":
    main()
