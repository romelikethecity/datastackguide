#!/usr/bin/env python3
"""
Fix banned words and empty calorie phrases in tool_content.json.

Per the writing style guide:
- Remove: genuinely, truly, really, actually, quite, extremely
- Replace: robust → strong/thorough, leverage → use, continues to → [verb]s
- Remove: "game-changer", "paradigm shift", "cutting-edge", etc.
"""
import json
import re
import sys

INPUT = "data/tool_content.json"


def fix_banned_words(text):
    """Remove or replace banned words and phrases."""

    # Remove empty calorie modifiers (just delete the word + clean spacing)
    for word in ('genuinely', 'truly', 'really', 'quite', 'extremely'):
        text = re.sub(rf'\b{word}\s+', '', text, flags=re.IGNORECASE)

    # "actually" is trickier - sometimes it means "in fact" which is fine
    # But most uses are filler. Remove when it's modifying a verb/adjective.
    # "can actually exceed" → "can exceed"
    # "are actually engaging" → "are engaging"
    # "actually need" → "need"
    # "actually trust" → "trust"
    text = re.sub(r'\bactually\s+', '', text, flags=re.IGNORECASE)

    # "robust" → context-dependent replacement
    text = re.sub(r'\brobust\b', 'strong', text, flags=re.IGNORECASE)

    # "leverage" → "use" (or "uses" / "using")
    text = re.sub(r'\bleverages\b', 'uses', text, flags=re.IGNORECASE)
    text = re.sub(r'\bleveraged\b', 'used', text, flags=re.IGNORECASE)
    text = re.sub(r'\bleveraging\b', 'using', text, flags=re.IGNORECASE)
    text = re.sub(r'\bleverage\b', 'use', text, flags=re.IGNORECASE)

    # "continues to X" → "Xs" (present tense)
    # e.g., "continues to operate" → "still operates"
    text = re.sub(r'\bcontinues to\b', 'still', text, flags=re.IGNORECASE)

    # Banned phrases (outright remove or replace)
    text = re.sub(r'\bgame-?changer\b', 'significant shift', text, flags=re.IGNORECASE)
    text = re.sub(r'\bparadigm shift\b', 'fundamental change', text, flags=re.IGNORECASE)
    text = re.sub(r'\bcutting-edge\b', 'advanced', text, flags=re.IGNORECASE)
    text = re.sub(r'\bholistic\b', 'comprehensive', text, flags=re.IGNORECASE)
    text = re.sub(r'\bsynerg\w+\b', 'combined benefit', text, flags=re.IGNORECASE)
    text = re.sub(r", full stop\b", '', text, flags=re.IGNORECASE)

    # Clean up double spaces from removals
    text = re.sub(r'  +', ' ', text)

    return text


def process_tool(slug, data):
    """Fix banned words in all text fields."""
    changes = 0

    for field in ('overview',):
        if field in data:
            for i, para in enumerate(data[field]):
                fixed = fix_banned_words(para)
                if fixed != para:
                    data[field][i] = fixed
                    changes += 1

    if 'key_features' in data:
        for feat in data['key_features']:
            fixed = fix_banned_words(feat.get('description', ''))
            if fixed != feat.get('description', ''):
                feat['description'] = fixed
                changes += 1

    if 'use_cases' in data:
        for uc in data['use_cases']:
            fixed = fix_banned_words(uc.get('description', ''))
            if fixed != uc.get('description', ''):
                uc['description'] = fixed
                changes += 1

    for field in ('pricing_detail', 'data_quality', 'verdict', 'description', 'description_2'):
        if field in data:
            fixed = fix_banned_words(data[field])
            if fixed != data[field]:
                data[field] = fixed
                changes += 1

    if 'faq' in data:
        for faq in data['faq']:
            fixed = fix_banned_words(faq.get('a', ''))
            if fixed != faq.get('a', ''):
                faq['a'] = fixed
                changes += 1

    return changes


def main():
    dry_run = '--dry-run' in sys.argv

    with open(INPUT) as f:
        tc = json.load(f)

    total_changes = 0
    for slug in sorted(tc.keys()):
        changes = process_tool(slug, tc[slug])
        if changes > 0:
            print(f"  {slug}: {changes} fields fixed")
            total_changes += changes

    print(f"\nTotal fields changed: {total_changes}")

    if dry_run:
        print("\n[DRY RUN] No changes written.")
    else:
        with open(INPUT, 'w') as f:
            json.dump(tc, f, indent=2, ensure_ascii=False)
        print(f"\nWritten to {INPUT}")


if __name__ == '__main__':
    main()
