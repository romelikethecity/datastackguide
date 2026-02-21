#!/usr/bin/env python3
"""
Generate alternatives pages for tools that don't have one yet.

Creates entries in alternatives.json using data from tool_content.json,
tools.json, and cooccurrence.json.

Only generates for tools with tool_content entries and >= MIN_JOBS job postings.
"""
import json
import sys
from datetime import date

DATA_DIR = "data"
MIN_JOBS = 0  # Generate for all tools with content
TODAY = date.today().isoformat()


def load(name):
    with open(f"{DATA_DIR}/{name}") as f:
        return json.load(f)


def save(name, data):
    with open(f"{DATA_DIR}/{name}", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_alt_entry(slug, tc, tools_meta, cooc):
    """Build an alternatives page entry for a tool."""
    content = tc.get(slug)
    if not content:
        return None

    name = content.get('display_name', slug)
    alts_slugs = content.get('alternatives', [])

    # Filter to alternatives that have tool_content entries
    valid_alts = [s for s in alts_slugs if s in tc]
    if len(valid_alts) < 2:
        return None

    # Build alternatives list
    alt_list = []
    for alt_slug in valid_alts[:7]:
        alt = tc[alt_slug]
        alt_meta = tools_meta.get(alt_slug, {})
        alt_name = alt.get('display_name', alt_slug)

        # Get pricing summary
        pricing = alt.get('pricing', {})
        tiers = pricing.get('tiers', [])
        if tiers:
            prices = [t.get('price', '') for t in tiers if t.get('price')]
            price_str = ' - '.join([prices[0], prices[-1]]) if len(prices) > 1 else (prices[0] if prices else 'Contact for pricing')
        else:
            price_str = 'Contact for pricing'

        best_for = alt.get('best_for', '')
        pros = alt.get('pros', [])
        cons = alt.get('cons', [])

        # Key difference: first pro that distinguishes from main tool
        key_diff = pros[0] if pros else ''

        # Coverage/verdict
        verdict_parts = []
        if best_for:
            verdict_parts.append(f"Best for {best_for.lower()}.")
        if cons:
            verdict_parts.append(f"Watch out for: {cons[0].lower()}.")

        alt_list.append({
            "slug": alt_slug,
            "name": alt_name,
            "price": price_str,
            "best_for": best_for[:100] if best_for else f"Teams looking for a {name} alternative",
            "key_difference": key_diff[:150] if key_diff else '',
            "coverage": '',
            "verdict": ' '.join(verdict_parts)[:300] if verdict_parts else ''
        })

    # Opening paragraph
    pricing = content.get('pricing', {})
    tiers = pricing.get('tiers', [])
    price_context = ''
    if tiers:
        prices = [t.get('price', '') for t in tiers if t.get('price')]
        if prices:
            price_context = f" At {prices[-1]} for the top tier," if len(prices) > 1 else f" At {prices[0]},"

    best_for = content.get('best_for', '')
    not_for = content.get('not_for', '')

    opening = f"{name} is a strong choice for {best_for.lower() if best_for else 'its target market'}."
    if price_context:
        opening += f"{price_context} it's not the right fit for every team."
    if not_for:
        opening += f" If {not_for.lower()}, these alternatives are worth evaluating."
    else:
        opening += f" Here are the alternatives worth evaluating based on your specific needs."

    meta_desc = f"{len(alt_list)} {name} alternatives compared with real pricing and job market data from 23K+ postings. Find the right tool for your team."

    return {
        "slug": f"{slug}-alternatives",
        "tool_slug": slug,
        "title": f"Best {name} Alternatives in 2026",
        "meta_description": meta_desc[:160],
        "opening": opening,
        "methodology": f"We evaluated these alternatives based on feature overlap with {name}, pricing, job market demand from our database of 23,000+ job postings, and real user feedback.",
        "alternatives_list": alt_list,
        "faq": [],
        "date_published": TODAY,
        "date_modified": TODAY
    }


def main():
    dry_run = '--dry-run' in sys.argv

    tc = load("tool_content.json")
    tools_data = load("tools.json")
    cooc = load("cooccurrence.json")
    alts_data = load("alternatives.json")

    tools_meta = {t['slug']: t for t in tools_data['tools']}
    existing_tool_slugs = {a['tool_slug'] for a in alts_data['alternatives']}

    # Find tools that need alternatives pages
    candidates = []
    for slug in tc:
        if slug in existing_tool_slugs:
            continue
        meta = tools_meta.get(slug, {})
        job_count = meta.get('job_count', 0)
        if job_count >= MIN_JOBS:
            candidates.append((slug, job_count))

    candidates.sort(key=lambda x: -x[1])

    added = 0
    for slug, job_count in candidates:
        entry = get_alt_entry(slug, tc, tools_meta, cooc.get('cooccurrence', {}))
        if entry and len(entry['alternatives_list']) >= 2:
            alts_data['alternatives'].append(entry)
            print(f"  {slug}: {len(entry['alternatives_list'])} alternatives ({job_count} jobs)")
            added += 1
        else:
            print(f"  {slug}: SKIPPED (not enough valid alternatives)")

    print(f"\nTotal alternatives pages added: {added}")
    print(f"Total alternatives pages now: {len(alts_data['alternatives'])}")

    if dry_run:
        print("\n[DRY RUN] No changes written.")
    else:
        save("alternatives.json", alts_data)
        print(f"\nWritten to {DATA_DIR}/alternatives.json")


if __name__ == '__main__':
    main()
