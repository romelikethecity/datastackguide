#!/usr/bin/env python3
"""
Fix SEO dates across all data files:
1. Stagger date_published and date_modified so they're not all identical
2. Fix short meta descriptions on pricing pages
3. Generate sitemap_dates.json for the sitemap serializer
"""

import json
from datetime import date, timedelta
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def stagger_dates(items, start: date, end: date, slug_key="slug"):
    """Spread items across a date range with varied modification dates."""
    n = len(items)
    if n == 0:
        return
    days_span = (end - start).days

    for i, item in enumerate(items):
        if n <= 1:
            pub_date = start
        else:
            pub_date = start + timedelta(days=int(i * days_span / (n - 1)))

        # date_modified: 3-10 days after publish, deterministic per slug
        slug = item.get(slug_key, str(i))
        mod_offset = (sum(ord(c) for c in str(slug)) % 8) + 3
        mod_date = min(pub_date + timedelta(days=mod_offset), date(2026, 2, 27))

        item["date_published"] = pub_date.isoformat()
        item["date_modified"] = mod_date.isoformat()


def fix_pricing_meta_descriptions(pages):
    """Fix pricing pages with meta_description under 120 chars."""
    fixes = {
        "census-pricing": "Census pricing breakdown: reverse ETL costs, sync-based pricing, and how it compares to Hightouch. What data teams actually pay in 2026.",
        "smartlead-pricing": "Smartlead pricing breakdown: cold email platform costs, sender account limits, and comparison to Instantly. What outbound teams actually pay in 2026.",
        "gong-engage-pricing": "Gong Engage pricing breakdown: sales engagement costs, per-seat pricing, and how it compares to Salesloft and Outreach. Updated for 2026.",
        "gong-pricing": "Gong Engage pricing breakdown: sales engagement costs, per-seat pricing, and how it compares to Salesloft and Outreach. Updated for 2026.",
        "braze-pricing": "Braze pricing breakdown: MAU-based pricing model, typical contract ranges by company size, and what marketing teams actually pay. Updated for 2026.",
        "clearbit-pricing": "Clearbit pricing breakdown: what plans actually cost, API pricing, and hidden fees. Based on real buyer data. Updated with 2026 pricing changes.",
        "sugarcrm-pricing": "SugarCRM pricing breakdown: what each edition costs, user minimums, and total cost comparison to Salesforce and HubSpot. Updated for 2026.",
        "workato-pricing": "Workato pricing breakdown: enterprise iPaaS costs, recipe-based pricing, and comparison to MuleSoft and Tray.io. What IT teams actually pay in 2026.",
        "linkedin-marketing-pricing": "LinkedIn Marketing pricing breakdown: ad costs, Campaign Manager pricing, and what B2B marketers actually pay. CPM, CPC, and budget benchmarks for 2026.",
        "airbyte-pricing": "Airbyte pricing breakdown: self-hosted (free) vs Cloud costs, row-based pricing, and what data teams actually pay for ELT pipelines. Updated for 2026.",
        "hightouch-pricing": "Hightouch pricing breakdown: reverse ETL costs, row-based pricing, and total cost of ownership for data activation teams. Updated with 2026 rates.",
        "outreach-pricing": "Outreach.io pricing breakdown: what tiers actually cost, per-seat pricing, and total cost of ownership for sales teams. Updated for 2026.",
    }

    fixed = 0
    for page in pages:
        slug = page.get("slug", "")
        if slug in fixes:
            old = page["meta_description"]
            page["meta_description"] = fixes[slug]
            print(f"  Fixed {slug}: {len(old)} -> {len(fixes[slug])} chars")
            fixed += 1
    return fixed


def main():
    # Date ranges for each content type (staggered rollout)
    # Based on git history: initial tools Feb 1-3, expansions through Feb 23
    date_ranges = {
        "tool_content": (date(2026, 1, 28), date(2026, 2, 8)),
        "comparisons": (date(2026, 2, 1), date(2026, 2, 12)),
        "pricing_pages": (date(2026, 2, 3), date(2026, 2, 14)),
        "alternatives": (date(2026, 2, 5), date(2026, 2, 16)),
        "best_of": (date(2026, 2, 6), date(2026, 2, 18)),
        "glossary": (date(2026, 2, 8), date(2026, 2, 20)),
        "guides": (date(2026, 2, 10), date(2026, 2, 22)),
        "use_cases": (date(2026, 2, 12), date(2026, 2, 23)),
        "integrations": (date(2026, 2, 14), date(2026, 2, 24)),
    }

    sitemap_dates = {}

    # --- tool_content.json (dict keyed by slug) ---
    print("Fixing tool_content.json...")
    tc_path = DATA_DIR / "tool_content.json"
    tc = json.loads(tc_path.read_text())
    slugs = sorted(tc.keys())
    start, end = date_ranges["tool_content"]
    n = len(slugs)
    days_span = (end - start).days
    for i, slug in enumerate(slugs):
        pub_date = start + timedelta(days=int(i * days_span / max(n - 1, 1)))
        mod_offset = (sum(ord(c) for c in slug) % 8) + 3
        mod_date = min(pub_date + timedelta(days=mod_offset), date(2026, 2, 27))
        tc[slug]["date_published"] = pub_date.isoformat()
        tc[slug]["date_modified"] = mod_date.isoformat()
        sitemap_dates[f"/tools/{slug}/"] = mod_date.isoformat()
    tc_path.write_text(json.dumps(tc, indent=2, ensure_ascii=False))
    print(f"  Staggered {n} tools: {start} to {end}")

    # --- Array-based data files ---
    array_files = {
        "comparisons": ("comparisons.json", "comparisons", "/compare/{slug}/"),
        "pricing_pages": ("pricing_pages.json", "pages", "/pricing/{slug}/"),
        "alternatives": ("alternatives.json", "alternatives", "/alternatives/{slug}/"),
        "best_of": ("best_of.json", "roundups", "/best/{slug}/"),
        "glossary": ("glossary.json", "terms", "/glossary/{slug}/"),
        "guides": ("guides.json", "guides", "/guides/{slug}/"),
        "use_cases": ("use_cases.json", "use_cases", "/use-cases/{slug}/"),
        "integrations": ("integrations.json", "integrations", "/integrations/{slug}/"),
    }

    for key, (filename, array_key, url_pattern) in array_files.items():
        print(f"Fixing {filename}...")
        fpath = DATA_DIR / filename
        data = json.loads(fpath.read_text())
        items = data[array_key]
        start, end = date_ranges[key]
        stagger_dates(items, start, end)

        for item in items:
            slug = item.get("slug", "")
            url = url_pattern.replace("{slug}", slug)
            sitemap_dates[url] = item["date_modified"]

        # Fix pricing meta descriptions
        if key == "pricing_pages":
            print("  Fixing short meta descriptions...")
            fixed = fix_pricing_meta_descriptions(items)
            print(f"  Fixed {fixed} descriptions")

        fpath.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        print(f"  Staggered {len(items)} items: {start} to {end}")

    # --- Static pages ---
    sitemap_dates["/"] = "2026-02-27"
    sitemap_dates["/about/"] = "2026-02-01"
    sitemap_dates["/methodology/"] = "2026-02-01"
    sitemap_dates["/newsletter/"] = "2026-02-26"
    for section in ["tools", "compare", "best", "alternatives", "pricing",
                     "glossary", "guides", "use-cases", "integrations",
                     "categories", "reports"]:
        sitemap_dates[f"/{section}/"] = "2026-02-23"

    # Category pages
    sitemap_dates["/categories/enrichment/"] = "2026-02-05"
    sitemap_dates["/categories/cleaning/"] = "2026-02-05"
    sitemap_dates["/categories/validation/"] = "2026-02-06"
    sitemap_dates["/categories/intent/"] = "2026-02-07"
    sitemap_dates["/categories/abm/"] = "2026-02-08"
    sitemap_dates["/categories/healthcare/"] = "2026-02-09"

    # Report pages
    for r in ["most-in-demand-tools", "salary-report", "category-breakdown",
              "enterprise-vs-smb", "tool-cooccurrence"]:
        sitemap_dates[f"/reports/{r}/"] = "2026-02-14"

    # --- Write sitemap_dates.json ---
    sd_path = DATA_DIR / "sitemap_dates.json"
    sd_path.write_text(json.dumps(sitemap_dates, indent=2, sort_keys=True))
    print(f"\nWrote {len(sitemap_dates)} entries to sitemap_dates.json")

    # --- Verify ---
    print("\nVerification:")
    all_dates = set()
    for d in sitemap_dates.values():
        all_dates.add(d)
    print(f"  Unique lastmod dates: {len(all_dates)}")
    print(f"  Date range: {min(all_dates)} to {max(all_dates)}")


if __name__ == "__main__":
    main()
