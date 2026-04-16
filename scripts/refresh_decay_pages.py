#!/usr/bin/env python3
"""Refresh stale titles/descriptions on content-decay pages (2026-04-15)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data'
TODAY = '2026-04-15'

# -----------------------------
# tool_content.json updates
# -----------------------------
tool_updates = {
    'linkedin-sales-navigator': {
        'meta_description': "LinkedIn Sales Navigator in 2026: $99/user/mo Core, $149 Advanced, $1,600/seat Enterprise. 50 InMails, 1B+ profiles, real ROI math for SDR teams.",
    },
    'tableau': {
        'meta_description': "Tableau in 2026: Creator $75/user/mo, Explorer $42, Viewer $15. Salesforce-owned BI with drag-and-drop dashboards. Real pricing and job demand data.",
    },
    'cognism': {
        'meta_description': "Cognism in 2026: $15K to $25K/yr for GDPR-compliant B2B data. Diamond-verified mobiles, strongest EU coverage, honest accuracy numbers vs ZoomInfo.",
    },
    'g2': {
        'meta_description': "G2 in 2026: free vendor profile plus paid buyer intent tiers from $15K to $100K+/yr. 2M reviews, 100K+ products, when intent data is worth the spend.",
    },
}

with open(DATA / 'tool_content.json') as f:
    tool_content = json.load(f)

for slug, fields in tool_updates.items():
    if slug not in tool_content:
        print(f'  MISSING tool_content: {slug}')
        continue
    for k, v in fields.items():
        tool_content[slug][k] = v
    tool_content[slug]['date_modified'] = TODAY
    print(f'  tool_content updated: {slug}')

with open(DATA / 'tool_content.json', 'w') as f:
    json.dump(tool_content, f, indent=2, ensure_ascii=False)


# -----------------------------
# alternatives.json updates
# -----------------------------
alt_updates = {
    'linkedin-sales-navigator-alternatives': {
        'title': 'Best LinkedIn Sales Navigator Alternatives (2026)',
        'meta_description': "6 LinkedIn Sales Navigator alternatives in 2026: Apollo ($49/user), ZoomInfo, Clay, and more. Full pricing and when to switch from the $99/seat Core plan.",
    },
    'dynamics-365-alternatives': {
        'title': 'Best Dynamics 365 Alternatives (2026)',
        'meta_description': "6 Dynamics 365 alternatives in 2026: Salesforce, HubSpot (free tier), Zoho from $14/user, Pipedrive. Pricing and fit for teams leaving the Microsoft stack.",
    },
    'braze-alternatives': {
        'title': 'Best Braze Alternatives (2026)',
        'meta_description': "3 Braze alternatives in 2026 with real pricing and job-market adoption data from 23K+ postings. When Iterable, Customer.io, or Salesforce Marketing Cloud wins.",
    },
}

with open(DATA / 'alternatives.json') as f:
    alts = json.load(f)

for item in alts['alternatives']:
    slug = item.get('slug')
    if slug in alt_updates:
        for k, v in alt_updates[slug].items():
            item[k] = v
        item['date_modified'] = TODAY
        print(f'  alternatives updated: {slug}')

with open(DATA / 'alternatives.json', 'w') as f:
    json.dump(alts, f, indent=2, ensure_ascii=True)


# -----------------------------
# integrations.json updates
# -----------------------------
int_updates = {
    'salesforce-dynamics-365': {
        'title': 'Salesforce + Dynamics 365 Integration (2026)',
        'meta_description': "Salesforce + Dynamics 365 integration in 2026: workflows, setup steps, and adoption data from 16 overlapping job postings. When companies run both CRMs.",
    },
}

with open(DATA / 'integrations.json') as f:
    ints = json.load(f)

for item in ints['integrations']:
    slug = item.get('slug')
    if slug in int_updates:
        for k, v in int_updates[slug].items():
            item[k] = v
        item['date_modified'] = TODAY
        print(f'  integrations updated: {slug}')

with open(DATA / 'integrations.json', 'w') as f:
    json.dump(ints, f, indent=2, ensure_ascii=False)


# -----------------------------
# glossary.json updates
# -----------------------------
gloss_updates = {
    'sales-intelligence': {
        'meta_description': "Sales intelligence in 2026: data platforms that surface ICP accounts, buying signals, and decision-makers. Top tools, typical pricing, and hiring demand.",
    },
    'revenue-attribution': {
        'meta_description': "Revenue attribution in 2026: models that tie closed deals to the exact marketing and sales touches. First-touch, last-touch, W-shaped, and top tools.",
    },
}

with open(DATA / 'glossary.json') as f:
    gloss = json.load(f)

for item in gloss['terms']:
    slug = item.get('slug')
    if slug in gloss_updates:
        for k, v in gloss_updates[slug].items():
            item[k] = v
        item['date_modified'] = TODAY
        print(f'  glossary updated: {slug}')

with open(DATA / 'glossary.json', 'w') as f:
    json.dump(gloss, f, indent=2, ensure_ascii=True)


# -----------------------------
# comparisons.json updates
# -----------------------------
comp_updates = {
    'orum-vs-nooks': {
        'title': 'Orum vs Nooks (2026): Parallel Dialer Showdown',
        'meta_description': "Orum vs Nooks in 2026: parallel dialer pricing from $300 to $600/user/mo, connect rates, AI features, and which one SDR teams pick more often.",
    },
    'braze-vs-salesforce-marketing-cloud': {
        'title': 'Braze vs Salesforce Marketing Cloud (2026)',
        'meta_description': "Braze vs Salesforce Marketing Cloud in 2026: real-time engagement vs enterprise suite. Pricing from $25K to $500K+/yr, Snowflake tie-ins, and fit by team size.",
    },
    'instantly-vs-apollo': {
        'title': 'Instantly vs Apollo (2026): Outbound Tool Compared',
        'meta_description': "Instantly vs Apollo in 2026: Instantly at $37/mo for cold email, Apollo at $49/user/mo for full prospecting. Which outbound stack fits your SDR motion.",
    },
}

with open(DATA / 'comparisons.json') as f:
    comps = json.load(f)

for item in comps['comparisons']:
    slug = item.get('slug')
    if slug in comp_updates:
        for k, v in comp_updates[slug].items():
            item[k] = v
        item['date_modified'] = TODAY
        print(f'  comparisons updated: {slug}')

with open(DATA / 'comparisons.json', 'w') as f:
    json.dump(comps, f, indent=2, ensure_ascii=False)


# -----------------------------
# pricing_pages.json updates
# -----------------------------
price_updates = {
    'power-bi-pricing': {
        'title': 'Power BI Pricing (2026): Pro, PPU, and Premium Capacity',
        'meta_description': "Power BI pricing in 2026: Pro at $10/user/mo, PPU at $20/user/mo, Premium Capacity from $4,995/mo. Real Microsoft BI costs and hidden Fabric fees.",
    },
}

with open(DATA / 'pricing_pages.json') as f:
    prices = json.load(f)

for item in prices['pages']:
    slug = item.get('slug')
    if slug in price_updates:
        for k, v in price_updates[slug].items():
            item[k] = v
        item['date_modified'] = TODAY
        print(f'  pricing_pages updated: {slug}')

with open(DATA / 'pricing_pages.json', 'w') as f:
    json.dump(prices, f, indent=2, ensure_ascii=False)


# -----------------------------
# best_of.json updates
# -----------------------------
best_updates = {
    'best-partner-ecosystem-tools': {
        'title': '6 Best Partner Ecosystem Tools (2026)',
        'meta_description': "6 best partner ecosystem and PRM tools in 2026: Crossbeam, Reveal, PartnerStack, and more. Pricing from free to $50K+/yr and co-sell feature depth.",
    },
    'best-data-integration-for-snowflake': {
        'title': '5 Best Data Integration Tools for Snowflake (2026)',
        'meta_description': "5 best ELT tools for Snowflake in 2026: Fivetran, Airbyte, dbt, Matillion, Stitch. Pricing from $0 to $100K+/yr and when each fits your data volume.",
    },
}

with open(DATA / 'best_of.json') as f:
    bests = json.load(f)

for item in bests['roundups']:
    slug = item.get('slug')
    if slug in best_updates:
        for k, v in best_updates[slug].items():
            item[k] = v
        item['date_modified'] = TODAY
        print(f'  best_of updated: {slug}')

with open(DATA / 'best_of.json', 'w') as f:
    json.dump(bests, f, indent=2, ensure_ascii=False)


# -----------------------------
# sitemap_dates.json updates
# -----------------------------
sitemap_urls = [
    '/',
    '/use-cases/',
    '/tools/linkedin-sales-navigator/',
    '/tools/tableau/',
    '/tools/cognism/',
    '/tools/g2/',
    '/alternatives/linkedin-sales-navigator-alternatives/',
    '/alternatives/dynamics-365-alternatives/',
    '/alternatives/braze-alternatives/',
    '/integrations/salesforce-dynamics-365/',
    '/glossary/sales-intelligence/',
    '/glossary/revenue-attribution/',
    '/compare/orum-vs-nooks/',
    '/compare/braze-vs-salesforce-marketing-cloud/',
    '/compare/instantly-vs-apollo/',
    '/pricing/power-bi-pricing/',
    '/best/best-partner-ecosystem-tools/',
    '/best/best-data-integration-for-snowflake/',
]

with open(DATA / 'sitemap_dates.json') as f:
    sm = json.load(f)

for u in sitemap_urls:
    if u in sm:
        sm[u] = TODAY
        print(f'  sitemap updated: {u}')
    else:
        sm[u] = TODAY
        print(f'  sitemap ADDED: {u}')

with open(DATA / 'sitemap_dates.json', 'w') as f:
    json.dump(sm, f, indent=2, ensure_ascii=False)

print('\nDone.')
