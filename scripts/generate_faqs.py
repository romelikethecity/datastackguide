#!/usr/bin/env python3
"""
Generate missing FAQ entries for tools that have fewer than 5.

Uses actual data from tools.json, tool_content.json, tool_details.json,
and cooccurrence.json to create data-driven FAQ answers.

Each tool gets FAQs from this priority list (skipping any that already exist):
1. Pricing FAQ
2. Job demand FAQ
3. Alternatives FAQ
4. Top competitor comparison FAQ
5. Best-for/use-case FAQ
"""
import json
import sys
import re

DATA_DIR = "data"
TARGET_FAQ_COUNT = 5


def load(name):
    with open(f"{DATA_DIR}/{name}") as f:
        return json.load(f)


def has_faq_about(faqs, keywords):
    """Check if any existing FAQ covers a topic."""
    for faq in faqs:
        q = faq['q'].lower()
        if any(kw in q for kw in keywords):
            return True
    return False


def format_salary(val):
    if not val:
        return None
    return f"${val/1000:.0f}K"


def make_pricing_faq(slug, content, tool_meta):
    """Generate a pricing FAQ from existing pricing data."""
    name = content.get('display_name', slug)
    pricing = content.get('pricing', {})
    tiers = pricing.get('tiers', [])

    if not tiers:
        return None

    # Build answer from real tier data
    parts = []
    tier_strs = []
    for t in tiers:
        price = t.get('price', '')
        tier_name = t.get('name', '')
        notes = t.get('notes', '')
        if price and tier_name:
            s = f"{tier_name} at {price}"
            if notes:
                s += f" ({notes})"
            tier_strs.append(s)

    if tier_strs:
        parts.append(f"{name} offers {len(tiers)} tiers: {', '.join(tier_strs)}.")

    notes = pricing.get('notes', '')
    if notes:
        parts.append(notes)

    if not parts:
        return None

    answer = ' '.join(parts)
    # Keep it concise
    if len(answer) > 500:
        answer = answer[:497] + '...'

    return {
        'q': f"How much does {name} cost?",
        'a': answer
    }


def make_demand_faq(slug, content, tool_meta, detail):
    """Generate a job demand FAQ from job posting data."""
    name = content.get('display_name', slug)
    job_count = tool_meta.get('job_count', 0)
    companies = tool_meta.get('unique_companies', 0)
    sal_min = tool_meta.get('salary_min')
    sal_max = tool_meta.get('salary_max')

    if job_count == 0:
        return None

    parts = []
    parts.append(f"{name} appears in {job_count} job postings across {companies} companies in our database of 23,000+ analyzed postings.")

    if sal_min and sal_max:
        parts.append(f"The average salary range for roles requiring {name} experience is {format_salary(sal_min)}-{format_salary(sal_max)}.")

    # Add top titles if available
    top_titles = detail.get('top_titles', [])[:3]
    if top_titles:
        title_strs = [t['title'] for t in top_titles]
        parts.append(f"The most common job titles are {', '.join(title_strs)}.")

    # Add remote split if available
    remote = detail.get('remote_split', {})
    if remote.get('remote') and remote.get('onsite'):
        total = remote['remote'] + remote['onsite']
        pct = remote['remote'] / total * 100
        parts.append(f"About {pct:.0f}% of these roles are remote.")

    return {
        'q': f"How in-demand is {name} experience?",
        'a': ' '.join(parts)
    }


def make_alternatives_faq(slug, content, tool_meta):
    """Generate an alternatives FAQ."""
    name = content.get('display_name', slug)
    alts = content.get('alternatives', [])

    if not alts or len(alts) < 2:
        return None

    # Get display names for alternatives
    tc = load("tool_content.json")
    alt_names = []
    for alt_slug in alts[:5]:
        alt_content = tc.get(alt_slug, {})
        alt_name = alt_content.get('display_name', alt_slug)
        alt_names.append(alt_name)

    if not alt_names:
        return None

    answer = f"The top alternatives to {name} include {', '.join(alt_names)}."

    best_for = content.get('best_for', '')
    not_for = content.get('not_for', '')
    if best_for:
        answer += f" {name} is strongest for {best_for.lower()}."
    if not_for:
        answer += f" Consider alternatives if {not_for.lower()}."

    return {
        'q': f"What are the best {name} alternatives?",
        'a': answer
    }


def make_comparison_faq(slug, content, cooc):
    """Generate a comparison FAQ with the top co-occurring tool."""
    name = content.get('display_name', slug)
    tc = load("tool_content.json")

    if not cooc:
        return None

    # Find top co-occurring tool that has content
    comp_slug = None
    for c in cooc:
        if c['tool'] in tc and c['tool'] != slug:
            comp_slug = c['tool']
            break

    if not comp_slug:
        return None

    comp_name = tc[comp_slug].get('display_name', comp_slug)

    # Build comparison from pros/cons
    our_pros = content.get('pros', [])[:2]
    comp_pros = tc[comp_slug].get('pros', [])[:2]

    parts = [f"{name} and {comp_name} are frequently mentioned together in job postings."]
    if our_pros:
        parts.append(f"{name}'s strengths include {our_pros[0].lower()}.")
    if comp_pros:
        parts.append(f"{comp_name}'s strengths include {comp_pros[0].lower()}.")

    best_for = content.get('best_for', '')
    if best_for:
        parts.append(f"{name} is the better fit for teams focused on {best_for.lower()}.")

    return {
        'q': f"{name} vs {comp_name}: which should I choose?",
        'a': ' '.join(parts)
    }


def make_bestfor_faq(slug, content):
    """Generate a use-case/best-for FAQ."""
    name = content.get('display_name', slug)
    best_for = content.get('best_for', '')
    not_for = content.get('not_for', '')
    categories = []

    tc_cats = content.get('categories', [])

    parts = []
    if best_for:
        parts.append(f"{name} works best for {best_for}.")
    if not_for:
        parts.append(f"It's not the right fit if {not_for.lower()}.")

    # Add use case info if available
    use_cases = content.get('use_cases', [])
    if use_cases:
        uc_titles = [uc.get('title', '') for uc in use_cases[:3] if uc.get('title')]
        if uc_titles:
            parts.append(f"Common use cases include {', '.join(uc_titles).lower()}.")

    if not parts:
        return None

    return {
        'q': f"Who should use {name}?",
        'a': ' '.join(parts)
    }


def main():
    dry_run = '--dry-run' in sys.argv

    tc = load("tool_content.json")
    tools_data = load("tools.json")
    details = load("tool_details.json")
    cooc = load("cooccurrence.json")

    tools_meta = {t['slug']: t for t in tools_data['tools']}

    total_added = 0

    for slug in sorted(tc.keys()):
        content = tc[slug]
        existing_faqs = content.get('faq', [])

        if len(existing_faqs) >= TARGET_FAQ_COUNT:
            continue

        tool_meta = tools_meta.get(slug, {})
        detail = details.get('details', {}).get(slug, {})
        tool_cooc = cooc.get('cooccurrence', {}).get(slug, [])

        new_faqs = []

        # 1. Pricing FAQ
        if not has_faq_about(existing_faqs, ['cost', 'price', 'pricing', 'how much']):
            faq = make_pricing_faq(slug, content, tool_meta)
            if faq:
                new_faqs.append(faq)

        # 2. Job demand FAQ
        if not has_faq_about(existing_faqs, ['demand', 'job', 'salary', 'in-demand', 'popular']):
            faq = make_demand_faq(slug, content, tool_meta, detail)
            if faq:
                new_faqs.append(faq)

        # 3. Alternatives FAQ
        if not has_faq_about(existing_faqs, ['alternative', 'instead', 'replace']):
            faq = make_alternatives_faq(slug, content, tool_meta)
            if faq:
                new_faqs.append(faq)

        # 4. Comparison FAQ
        if not has_faq_about(existing_faqs, ['vs', 'versus', 'compare', 'better']):
            faq = make_comparison_faq(slug, content, tool_cooc)
            if faq:
                new_faqs.append(faq)

        # 5. Best-for FAQ
        if not has_faq_about(existing_faqs, ['who should', 'best for', 'right for', 'good for']):
            faq = make_bestfor_faq(slug, content)
            if faq:
                new_faqs.append(faq)

        # Add only enough to reach target
        needed = TARGET_FAQ_COUNT - len(existing_faqs)
        to_add = new_faqs[:needed]

        if to_add:
            content['faq'] = existing_faqs + to_add
            print(f"  {slug}: added {len(to_add)} FAQs (now {len(content['faq'])} total)")
            total_added += len(to_add)

    print(f"\nTotal FAQs added: {total_added}")

    # Verify final counts
    under_target = sum(1 for s in tc if len(tc[s].get('faq', [])) < TARGET_FAQ_COUNT)
    print(f"Tools still under {TARGET_FAQ_COUNT} FAQs: {under_target}")

    if dry_run:
        print("\n[DRY RUN] No changes written.")
    else:
        with open(f"{DATA_DIR}/tool_content.json", 'w') as f:
            json.dump(tc, f, indent=2, ensure_ascii=False)
        print(f"\nWritten to {DATA_DIR}/tool_content.json")


if __name__ == '__main__':
    main()
