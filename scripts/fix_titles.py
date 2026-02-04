#!/usr/bin/env python3
"""
fix_titles.py

Shortens page titles in comparisons.json, best_of.json, and pricing_pages.json
so that every title is <= 53 characters. The site appends " | DataStackGuide"
(17 chars), keeping the full <title> tag at <= 70 characters.
"""

import json
import os
import re

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
MAX_TITLE_LEN = 53


# ---------------------------------------------------------------------------
# Comparison titles
# ---------------------------------------------------------------------------
def shorten_comparison_title(title: str) -> str:
    """
    Strategy:
    1. Extract the "Tool A vs Tool B" base (everything before the colon).
    2. Try "{base}: Short Suffix" options that fit within 53 chars.
    3. Try "{base} (2026)" or "{base} Compared".
    4. Fall back to just the base.
    """
    if len(title) <= MAX_TITLE_LEN:
        return title

    # Split at colon to get the base "X vs Y" part
    colon_idx = title.find(":")
    if colon_idx > -1:
        base = title[:colon_idx].strip()
    else:
        # No colon -- try to keep what we can
        base = title.strip()

    # Attempt a hierarchy of suffixes (most descriptive first)
    suffix_candidates = [
        " (2026) Compared",
        " Compared (2026)",
        " (2026)",
        " Compared",
    ]

    for suffix in suffix_candidates:
        candidate = base + suffix
        if len(candidate) <= MAX_TITLE_LEN:
            return candidate

    # If even the base alone is too long (unlikely), truncate cleanly
    if len(base) <= MAX_TITLE_LEN:
        return base

    return base[:MAX_TITLE_LEN]


# ---------------------------------------------------------------------------
# Pricing page titles
# ---------------------------------------------------------------------------
def shorten_pricing_title(title: str) -> str:
    """
    Strategy:
    1. Extract the tool name and standardize to "{Tool} Pricing (2026): Plans & Costs"
    2. If that's too long, use "{Tool} Pricing (2026)"
    """
    if len(title) <= MAX_TITLE_LEN:
        return title

    # Try to extract the tool name from patterns like "Tool Pricing (2026): ..."
    m = re.match(r"^(.+?)\s+Pricing\s*\(2026\)", title)
    if m:
        tool_name = m.group(1).strip()
    else:
        # Fallback: grab everything before "Pricing"
        m2 = re.match(r"^(.+?)\s+Pricing", title)
        tool_name = m2.group(1).strip() if m2 else title

    # Try adding suffixes from most descriptive to least
    candidates = [
        f"{tool_name} Pricing (2026): Plans & Costs",
        f"{tool_name} Pricing (2026): Full Breakdown",
        f"{tool_name} Pricing (2026): What It Costs",
        f"{tool_name} Pricing (2026): Real Costs",
        f"{tool_name} Pricing (2026): All Plans",
        f"{tool_name} Pricing (2026)",
        f"{tool_name} Pricing",
    ]

    for candidate in candidates:
        if len(candidate) <= MAX_TITLE_LEN:
            return candidate

    return candidates[-1][:MAX_TITLE_LEN]


# ---------------------------------------------------------------------------
# Best-of / roundup titles
# ---------------------------------------------------------------------------
def shorten_best_of_title(title: str) -> str:
    """
    Only one entry is over 53 chars:
      "5 Best Data Enrichment Tools for Small Business (2026)" -> 54 chars
    Shorten "Small Business" to "SMBs".
    """
    if len(title) <= MAX_TITLE_LEN:
        return title

    # Generic approach: try common shortenings
    shortened = title.replace("for Small Business", "for SMBs")
    if len(shortened) <= MAX_TITLE_LEN:
        return shortened

    # If still too long, try removing parenthetical year
    shortened = re.sub(r"\s*\(\d{4}\)\s*$", "", shortened).strip()
    if len(shortened) <= MAX_TITLE_LEN:
        return shortened

    return title[:MAX_TITLE_LEN]


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------
def process_file(filepath, entries_key, shorten_fn):
    """Read a JSON file, shorten titles, write back. Return change stats."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    entries = data[entries_key]
    changes = []

    for entry in entries:
        old_title = entry.get("title", "")
        if len(old_title) > MAX_TITLE_LEN:
            new_title = shorten_fn(old_title)
            entry["title"] = new_title
            changes.append((old_title, new_title))

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")  # trailing newline

    return changes


def main():
    files_config = [
        ("comparisons.json", "comparisons", shorten_comparison_title),
        ("best_of.json", "roundups", shorten_best_of_title),
        ("pricing_pages.json", "pages", shorten_pricing_title),
    ]

    total_changed = 0

    for filename, key, fn in files_config:
        filepath = os.path.join(DATA_DIR, filename)
        print(f"\n{'='*70}")
        print(f"Processing: {filename}")
        print(f"{'='*70}")

        changes = process_file(filepath, key, fn)

        if not changes:
            print("  No titles over 53 characters. Nothing to change.")
        else:
            for old, new in changes:
                print(f"\n  BEFORE [{len(old):>2}]: {old}")
                print(f"  AFTER  [{len(new):>2}]: {new}")

        total_changed += len(changes)

    # Final summary
    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"  Total titles shortened: {total_changed}")
    print(f"  Max allowed length:     {MAX_TITLE_LEN} chars")
    print(f"  Full <title> budget:    70 chars (53 + ' | DataStackGuide')")

    # Verification pass
    print(f"\n{'='*70}")
    print(f"VERIFICATION: Checking all titles are <= {MAX_TITLE_LEN} chars")
    print(f"{'='*70}")
    violations = 0
    for filename, key, _ in files_config:
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        for entry in data[key]:
            t = entry.get("title", "")
            if len(t) > MAX_TITLE_LEN:
                print(f"  VIOLATION [{len(t)}]: {t}  (in {filename})")
                violations += 1

    if violations == 0:
        print("  All titles are within the 53-character limit.")
    else:
        print(f"  {violations} title(s) still exceed the limit!")


if __name__ == "__main__":
    main()
