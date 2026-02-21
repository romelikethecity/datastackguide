#!/usr/bin/env python3
"""
Fix broken tool slug references across all data files.

Strategy:
- Remove best-of picks that reference non-existent tools
- Remove comparisons that reference non-existent tools
- Remove integrations that reference non-existent tools
"""
import json
import sys

DATA_DIR = "data"


def load(name):
    with open(f"{DATA_DIR}/{name}") as f:
        return json.load(f)


def save(name, data):
    with open(f"{DATA_DIR}/{name}", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    dry_run = '--dry-run' in sys.argv

    tools = load("tools.json")
    tool_slugs = {t['slug'] for t in tools['tools']}
    tc = load("tool_content.json")
    tc_slugs = set(tc.keys())
    valid_slugs = tool_slugs & tc_slugs  # must exist in both

    # Fix best-of picks
    bof = load("best_of.json")
    bof_removed = 0
    for roundup in bof['roundups']:
        original_count = len(roundup.get('picks', []))
        roundup['picks'] = [
            p for p in roundup.get('picks', [])
            if p.get('slug', '') in valid_slugs
        ]
        removed = original_count - len(roundup['picks'])
        if removed > 0:
            print(f"  best-of/{roundup['slug']}: removed {removed} picks")
            bof_removed += removed

    # Fix comparisons
    comps = load("comparisons.json")
    original_comp_count = len(comps['comparisons'])
    comps['comparisons'] = [
        c for c in comps['comparisons']
        if c.get('tool_a', '') in valid_slugs and c.get('tool_b', '') in valid_slugs
    ]
    comp_removed = original_comp_count - len(comps['comparisons'])
    if comp_removed > 0:
        print(f"  comparisons: removed {comp_removed} entries")

    # Fix integrations
    integ = load("integrations.json")
    original_integ_count = len(integ['integrations'])
    integ['integrations'] = [
        i for i in integ['integrations']
        if i.get('tool_a', '') in valid_slugs and i.get('tool_b', '') in valid_slugs
    ]
    integ_removed = original_integ_count - len(integ['integrations'])
    if integ_removed > 0:
        print(f"  integrations: removed {integ_removed} entries")

    # Remove roundups with <3 picks (thin content)
    original_roundup_count = len(bof['roundups'])
    thin_roundups = [r['slug'] for r in bof['roundups'] if len(r.get('picks', [])) < 3]
    bof['roundups'] = [r for r in bof['roundups'] if len(r.get('picks', [])) >= 3]
    roundups_removed = original_roundup_count - len(bof['roundups'])
    if roundups_removed > 0:
        print(f"  best-of: removed {roundups_removed} thin roundups: {thin_roundups}")

    total = bof_removed + comp_removed + integ_removed
    print(f"\nTotal broken references removed: {total}")
    print(f"  Best-of picks: {bof_removed}")
    print(f"  Thin roundups removed: {roundups_removed}")
    print(f"  Comparisons: {comp_removed}")
    print(f"  Integrations: {integ_removed}")

    if dry_run:
        print("\n[DRY RUN] No changes written.")
    else:
        save("best_of.json", bof)
        save("comparisons.json", comps)
        save("integrations.json", integ)
        print("\nWritten to data files.")


if __name__ == '__main__':
    main()
