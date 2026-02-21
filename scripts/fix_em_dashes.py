#!/usr/bin/env python3
"""
Fix em-dash AI writing tells in tool_content.json.

Strategy:
1. Double em-dashes (— X —) → commas (, X,)
2. Em-dash before soft joiners (especially, particularly, etc.) → comma
3. Remaining em-dashes → period + capitalize next word (split into two sentences)

Reads tool_content.json, fixes all text fields, writes back.
"""
import json
import re
import sys

INPUT = "data/tool_content.json"

def fix_double_em_dashes(text):
    """Convert — X — parentheticals to , X, """
    # Match with spaces: word — some words — word
    text = re.sub(r' — ([^—]{3,80}) — ', r', \1, ', text)
    # Match without spaces: word—some words—word
    text = re.sub(r'(\w)—([^—]{3,80})—(\w)', r'\1, \2, \3', text)
    return text

def fix_em_dashes(text):
    """Replace remaining em-dashes with appropriate punctuation."""
    # First pass: double em-dashes
    text = fix_double_em_dashes(text)

    # Second pass: em-dash before soft joiners → comma (with and without spaces)
    soft_joiners = (
        'especially', 'particularly', 'including', 'notably', 'specifically',
        'like', 'such as', 'whether', 'meaning', 'making', 'allowing',
        'which', 'where', 'while', 'though', 'even', 'often', 'usually',
        'sometimes', 'typically', 'think', 'from', 'for example',
    )
    for joiner in soft_joiners:
        # With spaces
        text = re.sub(
            rf' — ({re.escape(joiner)})',
            rf', \1',
            text,
            flags=re.IGNORECASE
        )
        # Without spaces
        text = re.sub(
            rf'(\w)—({re.escape(joiner)})',
            rf'\1, \2',
            text,
            flags=re.IGNORECASE
        )

    # Third pass: em-dash before conjunctions → period (with and without spaces)
    conjunctions = ('but', 'and', 'so', 'or', 'nor', 'yet')
    for conj in conjunctions:
        text = re.sub(
            rf' — ({re.escape(conj)}\b)',
            rf'. {conj.capitalize()}',
            text,
            flags=re.IGNORECASE
        )
        text = re.sub(
            rf'(\w)—({re.escape(conj)}\b)',
            lambda m: m.group(1) + '. ' + m.group(2).capitalize(),
            text,
            flags=re.IGNORECASE
        )

    # Fourth pass: em-dash before short connectors → comma (with and without spaces)
    comma_words = (
        'not', 'no', 'most', 'all', 'both', 'each', 'every',
        'reducing', 'creating', 'enabling', 'driving', 'turning',
        'giving', 'letting', 'helping', 'building', 'adding',
        'tracking', 'covering', 'automating', 'routing', 'pulling',
        'pushing', 'syncing', 'feeding', 'connecting', 'combining',
        'limited', 'none', 'when', 'you', 'it', 'the', 'a', 'one',
        'company', 'person', 'display', 'contact', 'account',
        'coordinating', 'someone', 'expect', 'generous', 'basic',
    )
    for word in comma_words:
        text = re.sub(
            rf' — ({re.escape(word)}\b)',
            rf', \1',
            text,
            flags=re.IGNORECASE
        )
        text = re.sub(
            rf'(\w)—({re.escape(word)}\b)',
            rf'\1, \2',
            text,
            flags=re.IGNORECASE
        )

    # Fifth pass: remaining em-dashes → ". " + capitalize (with and without spaces)
    def period_replace_spaced(match):
        after = match.group(1)
        if after and after[0].isalpha():
            return '. ' + after[0].upper() + after[1:]
        return '. ' + after

    text = re.sub(r' — (.)', period_replace_spaced, text)

    def period_replace_nospace(match):
        before = match.group(1)
        after = match.group(2)
        if after and after[0].isalpha():
            return before + '. ' + after[0].upper() + after[1:]
        return before + '. ' + after

    text = re.sub(r'(\w)—(.)', period_replace_nospace, text)

    return text


def process_tool(slug, data):
    """Fix em-dashes in all text fields of a tool entry."""
    changes = 0

    # Overview paragraphs
    if 'overview' in data:
        for i, para in enumerate(data['overview']):
            fixed = fix_em_dashes(para)
            if fixed != para:
                data['overview'][i] = fixed
                changes += 1

    # Key features
    if 'key_features' in data:
        for feat in data['key_features']:
            fixed = fix_em_dashes(feat.get('description', ''))
            if fixed != feat.get('description', ''):
                feat['description'] = fixed
                changes += 1

    # Use cases
    if 'use_cases' in data:
        for uc in data['use_cases']:
            fixed = fix_em_dashes(uc.get('description', ''))
            if fixed != uc.get('description', ''):
                uc['description'] = fixed
                changes += 1

    # Pricing detail
    if 'pricing_detail' in data:
        fixed = fix_em_dashes(data['pricing_detail'])
        if fixed != data['pricing_detail']:
            data['pricing_detail'] = fixed
            changes += 1

    # Data quality
    if 'data_quality' in data:
        fixed = fix_em_dashes(data['data_quality'])
        if fixed != data['data_quality']:
            data['data_quality'] = fixed
            changes += 1

    # Verdict
    if 'verdict' in data:
        fixed = fix_em_dashes(data['verdict'])
        if fixed != data['verdict']:
            data['verdict'] = fixed
            changes += 1

    # Description fields
    for field in ('description', 'description_2'):
        if field in data:
            fixed = fix_em_dashes(data[field])
            if fixed != data[field]:
                data[field] = fixed
                changes += 1

    # FAQ answers
    if 'faq' in data:
        for faq in data['faq']:
            fixed = fix_em_dashes(faq.get('a', ''))
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

    # Count remaining em-dashes
    remaining = 0
    for slug, data in tc.items():
        texts = []
        texts.extend(data.get('overview', []))
        texts.extend(f.get('description', '') for f in data.get('key_features', []))
        texts.extend(u.get('description', '') for u in data.get('use_cases', []))
        texts.append(data.get('pricing_detail', ''))
        texts.append(data.get('data_quality', ''))
        texts.append(data.get('verdict', ''))
        texts.append(data.get('description', ''))
        texts.append(data.get('description_2', ''))
        for faq in data.get('faq', []):
            texts.append(faq.get('a', ''))
        remaining += sum(t.count('—') for t in texts)

    print(f"Remaining em-dashes: {remaining}")

    if dry_run:
        print("\n[DRY RUN] No changes written.")
    else:
        with open(INPUT, 'w') as f:
            json.dump(tc, f, indent=2, ensure_ascii=False)
        print(f"\nWritten to {INPUT}")


if __name__ == '__main__':
    main()
