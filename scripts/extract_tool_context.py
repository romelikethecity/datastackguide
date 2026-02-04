#!/usr/bin/env python3
"""
Extract all available context for tool slugs from the data files.
Outputs a structured brief that Claude Code uses when writing expanded reviews.

Usage:
  python3 scripts/extract_tool_context.py apollo clay instantly
  python3 scripts/extract_tool_context.py --next 5          # next 5 unexpanded tools
  python3 scripts/extract_tool_context.py --all-remaining    # all unexpanded tools (list only)
"""
import json
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(name):
    with open(os.path.join(ROOT, "data", name)) as f:
        return json.load(f)

def get_unexpanded_slugs():
    tc = load("tool_content.json")
    return [slug for slug in tc if "overview" not in tc[slug]]

def extract_context(slug):
    tc = load("tool_content.json")
    tools = load("tools.json")
    details = load("tool_details.json")
    cooc = load("cooccurrence.json")

    if slug not in tc:
        return None

    content = tc[slug]
    tool_meta = next((t for t in tools["tools"] if t["slug"] == slug), {})
    detail = details.get("details", {}).get(slug, {})
    cooc_list = cooc.get("cooccurrence", {}).get(slug, [])

    brief = {
        "slug": slug,
        "already_expanded": "overview" in content,
        "existing_content": {
            "display_name": content.get("display_name", ""),
            "tagline": content.get("tagline", ""),
            "description": content.get("description", ""),
            "description_2": content.get("description_2", ""),
            "website": content.get("website", ""),
            "founded": content.get("founded"),
            "hq": content.get("hq", ""),
            "pricing": content.get("pricing", {}),
            "pros": content.get("pros", []),
            "cons": content.get("cons", []),
            "best_for": content.get("best_for", ""),
            "not_for": content.get("not_for", ""),
            "alternatives": content.get("alternatives", []),
            "faq": content.get("faq", []),
        },
        "job_market_data": {
            "job_count": tool_meta.get("job_count", 0),
            "unique_companies": tool_meta.get("unique_companies", 0),
            "salary_min": tool_meta.get("salary_min"),
            "salary_max": tool_meta.get("salary_max"),
            "categories": tool_meta.get("categories", []),
            "primary_category": tool_meta.get("primary_category", ""),
            "db_category": tool_meta.get("db_category", ""),
        },
        "detail_data": {
            "company_stages": detail.get("company_stages", {}),
            "seniority": detail.get("seniority", {}),
            "functions": detail.get("functions", {}),
            "top_companies": detail.get("top_companies", [])[:5],
            "top_titles": detail.get("top_titles", [])[:5],
            "remote_split": detail.get("remote_split", {}),
        },
        "cooccurrence_top8": [
            {"tool": c["tool"], "count": c["count"]}
            for c in cooc_list[:8]
        ],
    }
    return brief


def format_brief(brief):
    """Format a tool brief as readable text for a prompt."""
    lines = []
    ec = brief["existing_content"]
    jm = brief["job_market_data"]
    dd = brief["detail_data"]

    lines.append(f"=== {ec['display_name']} ({brief['slug']}) ===")
    lines.append(f"Tagline: {ec['tagline']}")
    lines.append(f"Description: {ec['description']}")
    if ec["description_2"]:
        lines.append(f"Description 2: {ec['description_2']}")
    lines.append(f"Website: {ec['website']}  |  Founded: {ec.get('founded', '?')}  |  HQ: {ec.get('hq', '?')}")
    lines.append("")

    # Pricing
    pricing = ec.get("pricing", {})
    if pricing.get("tiers"):
        lines.append("Pricing tiers:")
        for t in pricing["tiers"]:
            lines.append(f"  - {t['name']}: {t['price']} ({t.get('notes', '')})")
        if pricing.get("notes"):
            lines.append(f"  Notes: {pricing['notes']}")
    lines.append("")

    # Pros/Cons
    lines.append("Pros: " + " | ".join(ec.get("pros", [])))
    lines.append("Cons: " + " | ".join(ec.get("cons", [])))
    lines.append(f"Best for: {ec.get('best_for', '')}")
    lines.append(f"Not for: {ec.get('not_for', '')}")
    lines.append(f"Alternatives: {', '.join(ec.get('alternatives', []))}")
    lines.append("")

    # FAQ
    if ec.get("faq"):
        lines.append("Existing FAQ:")
        for faq in ec["faq"]:
            lines.append(f"  Q: {faq['q']}")
            lines.append(f"  A: {faq['a'][:200]}...")
    lines.append("")

    # Job market
    sal_min = f"${jm['salary_min']/1000:.0f}K" if jm.get("salary_min") else "N/A"
    sal_max = f"${jm['salary_max']/1000:.0f}K" if jm.get("salary_max") else "N/A"
    lines.append(f"Job Market: {jm['job_count']} postings across {jm['unique_companies']} companies  |  Salary: {sal_min}-{sal_max}")
    lines.append(f"Categories: {', '.join(jm.get('categories', []))}  |  Primary: {jm.get('primary_category', '')}")
    lines.append("")

    # Details
    if dd.get("company_stages"):
        lines.append("Company stages: " + ", ".join(f"{k}: {v}" for k, v in dd["company_stages"].items()))
    if dd.get("functions"):
        lines.append("Functions: " + ", ".join(f"{k}: {v}" for k, v in list(dd["functions"].items())[:6]))
    if dd.get("top_titles"):
        lines.append("Top titles: " + ", ".join(t["title"] for t in dd["top_titles"][:5]))
    if dd.get("top_companies"):
        lines.append("Top companies: " + ", ".join(f"{c['name']}({c['jobs']})" for c in dd["top_companies"][:5]))
    if dd.get("remote_split"):
        lines.append(f"Remote: {dd['remote_split'].get('remote', 0)} | Onsite: {dd['remote_split'].get('onsite', 0)}")
    lines.append("")

    # Cooccurrence
    if brief.get("cooccurrence_top8"):
        lines.append("Most co-mentioned tools: " + ", ".join(
            f"{c['tool']}({c['count']})" for c in brief["cooccurrence_top8"]
        ))
    lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    args = sys.argv[1:]

    if not args:
        print("Usage:")
        print("  python3 scripts/extract_tool_context.py slug1 slug2 ...")
        print("  python3 scripts/extract_tool_context.py --next N")
        print("  python3 scripts/extract_tool_context.py --all-remaining")
        sys.exit(1)

    if args[0] == "--all-remaining":
        remaining = get_unexpanded_slugs()
        print(f"{len(remaining)} tools remaining:\n")
        for s in remaining:
            print(f"  {s}")
        sys.exit(0)

    if args[0] == "--next":
        n = int(args[1]) if len(args) > 1 else 5
        remaining = get_unexpanded_slugs()
        slugs = remaining[:n]
        print(f"Next {n} unexpanded tools: {', '.join(slugs)}\n")
    else:
        slugs = args

    for slug in slugs:
        brief = extract_context(slug)
        if brief is None:
            print(f"ERROR: slug '{slug}' not found in tool_content.json\n")
            continue
        if brief["already_expanded"]:
            print(f"SKIP: '{slug}' is already expanded\n")
            continue
        print(format_brief(brief))
        print("---\n")
