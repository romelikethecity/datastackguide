#!/usr/bin/env python3
"""
Generate integration pages for high-cooccurrence tool pairs.
Uses cooccurrence data, tool categories, and tool content to create
integration guides with relevant workflows, setup considerations, and FAQs.
"""
import json
import sys
from datetime import date

DATA = "/Users/rome/Documents/projects/datastackguide/data"
TODAY = date.today().isoformat()
MIN_COOCCURRENCE = 5


def load(name):
    with open(f"{DATA}/{name}") as f:
        return json.load(f)


def save(name, data):
    with open(f"{DATA}/{name}", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# Category-based workflow templates
# Each key is a tuple of (category_a, category_b) patterns
WORKFLOW_TEMPLATES = {
    # CRM + Enrichment
    ("crm", "enrichment"): [
        {"workflow": "CRM record enrichment",
         "description": "New and existing {b_name} contact data flows into {a_name} records automatically. Firmographic, technographic, and contact details populate CRM fields without manual data entry."},
        {"workflow": "Prospecting pipeline",
         "description": "Reps search {b_name}'s database, identify target contacts, and push them directly into {a_name} as leads. Records arrive with verified emails and direct dials already attached."},
        {"workflow": "Data decay management",
         "description": "{b_name} monitors {a_name} records for job changes, company moves, and stale contact info. Automated updates keep bounce rates low and outreach reaching the right people."},
        {"workflow": "Account scoring enrichment",
         "description": "{b_name} appends firmographic and technographic data to {a_name} accounts, feeding lead scoring models with company size, tech stack, and industry signals."},
    ],
    # CRM + Sales engagement
    ("crm", "list-building"): [
        {"workflow": "Sequence enrollment",
         "description": "Leads created or updated in {a_name} automatically enroll in {b_name} sequences based on lead score, deal stage, or segment. Reps see engagement data without switching tools."},
        {"workflow": "Activity logging",
         "description": "{b_name} logs all email opens, clicks, calls, and meeting bookings back to {a_name}. Sales managers get full activity visibility in CRM reports and dashboards."},
        {"workflow": "Pipeline updates",
         "description": "Deal stage changes in {a_name} trigger sequence adjustments in {b_name}. Won deals stop outreach automatically. Lost deals can re-enter nurture sequences."},
        {"workflow": "Lead routing",
         "description": "New inbound leads in {a_name} route to the right rep and trigger personalized {b_name} sequences based on territory, company size, or lead source."},
    ],
    # CRM + ABM
    ("crm", "abm"): [
        {"workflow": "Account intent sync",
         "description": "{b_name} pushes intent signals and account scores into {a_name} records. Sales reps see which target accounts are actively researching relevant topics."},
        {"workflow": "Campaign orchestration",
         "description": "{b_name} ABM campaigns pull audience segments from {a_name} and push engagement data back. Marketing and sales see the same account-level view."},
        {"workflow": "Pipeline influence tracking",
         "description": "{b_name} attribution data flows into {a_name} opportunities, showing which ABM campaigns influenced pipeline creation and deal velocity."},
        {"workflow": "Target account alignment",
         "description": "Sales selects target accounts in {a_name} and {b_name} automatically builds matched audiences for advertising, web personalization, and intent monitoring."},
    ],
    # CRM + iPaaS/Automation
    ("crm", "orchestration"): [
        {"workflow": "Multi-system sync",
         "description": "{b_name} keeps {a_name} data synchronized with marketing automation, billing systems, support tools, and data warehouses. Changes propagate across all connected systems."},
        {"workflow": "Custom workflow automation",
         "description": "Complex business logic (approval chains, conditional routing, multi-step processes) runs in {b_name} with {a_name} as the trigger and data source."},
        {"workflow": "Data transformation",
         "description": "{b_name} transforms data between {a_name}'s format and other systems. Field mappings, value translations, and data cleansing happen automatically during sync."},
        {"workflow": "Error handling and monitoring",
         "description": "{b_name} catches sync failures, data conflicts, and API errors between {a_name} and connected systems. Ops teams get alerts before data quality degrades."},
    ],
    # CRM + Marketing Automation
    ("crm", "marketing-automation"): [
        {"workflow": "Lead lifecycle management",
         "description": "{b_name} nurtures leads through email sequences and scores engagement. When leads hit MQL threshold, they sync to {a_name} for sales follow-up with full engagement history."},
        {"workflow": "Revenue attribution",
         "description": "{b_name} tracks which marketing campaigns, content, and channels influenced {a_name} opportunities. Closed-loop reporting shows marketing's real pipeline impact."},
        {"workflow": "Audience segmentation",
         "description": "{a_name} deal stages and account data feed {b_name} segmentation. Marketing targets different messages to prospects, active opportunities, and existing customers."},
        {"workflow": "Campaign sync",
         "description": "{a_name} campaign members sync with {b_name} lists. Sales enrollment in {a_name} triggers automated nurture sequences in {b_name}."},
    ],
    # Enrichment + Sales engagement
    ("enrichment", "list-building"): [
        {"workflow": "Pre-outreach enrichment",
         "description": "{a_name} enriches contact records before {b_name} sequences begin. Verified emails and direct dials improve deliverability and connect rates."},
        {"workflow": "Signal-triggered outreach",
         "description": "{a_name} identifies buying signals (job changes, funding, tech installs) and triggers personalized {b_name} sequences for the right contacts at the right time."},
        {"workflow": "List building to sequencing",
         "description": "Reps build prospect lists in {a_name} and push contacts directly into {b_name} sequences. The handoff includes verified contact info and personalization data."},
    ],
    # ABM + Marketing Automation
    ("abm", "marketing-automation"): [
        {"workflow": "Account-based nurturing",
         "description": "{a_name} identifies in-market accounts and pushes them to {b_name} for targeted email nurture sequences. Engagement data flows back to update account scores."},
        {"workflow": "Intent-driven campaigns",
         "description": "{a_name} intent signals trigger {b_name} campaign enrollment. Accounts researching specific topics receive relevant content automatically."},
        {"workflow": "Multi-channel orchestration",
         "description": "{a_name} coordinates advertising and web personalization while {b_name} handles email nurture. Both platforms share the same account list and engagement data."},
    ],
    # iPaaS + iPaaS or automation pairs
    ("orchestration", "orchestration"): [
        {"workflow": "Complementary integration patterns",
         "description": "{a_name} handles enterprise-grade API management and complex transformations while {b_name} manages simpler point-to-point automations. Teams use both for different integration tiers."},
        {"workflow": "Migration pathway",
         "description": "Teams often start with {b_name} for simple automations and move complex workflows to {a_name} as integration requirements grow. Both can coexist during the transition."},
        {"workflow": "Departmental separation",
         "description": "IT manages {a_name} for core system integrations (ERP, finance, HR) while marketing and sales ops use {b_name} for their own tool connections without IT bottlenecks."},
    ],
}

# Default workflows for uncategorized pairs
DEFAULT_WORKFLOWS = [
    {"workflow": "Data synchronization",
     "description": "{a_name} and {b_name} share data bidirectionally to keep records consistent. Contact updates, status changes, and activity data flow between both systems."},
    {"workflow": "Workflow automation",
     "description": "Events in {a_name} trigger automated actions in {b_name}. Teams eliminate manual handoffs and reduce the time between data entry and action."},
    {"workflow": "Reporting consolidation",
     "description": "Data from both {a_name} and {b_name} feeds into unified dashboards. Leadership gets a complete view without switching between platforms."},
]


def build_category_map(categories_data):
    """Build slug -> primary category mapping from categories.json."""
    cat_map = {}
    cats = categories_data.get('categories', categories_data)
    for cat in cats:
        cat_slug = cat.get('slug', '')
        for tool in cat.get('tools', []):
            tool_slug = tool.get('slug', tool) if isinstance(tool, dict) else tool
            if tool_slug not in cat_map:
                cat_map[tool_slug] = cat_slug
    return cat_map


# Module-level category map, set in main()
_category_map = {}


def get_tool_categories(slug, tools_meta=None):
    """Get the primary category for a tool."""
    return _category_map.get(slug, 'general')


def get_workflows(tool_a, tool_b, tools_meta, a_name, b_name):
    """Get relevant workflows for a tool pair based on categories."""
    cat_a = get_tool_categories(tool_a, tools_meta)
    cat_b = get_tool_categories(tool_b, tools_meta)

    # Try both orderings
    templates = WORKFLOW_TEMPLATES.get((cat_a, cat_b))
    if templates:
        return [
            {"workflow": t["workflow"],
             "description": t["description"].format(a_name=a_name, b_name=b_name)}
            for t in templates[:4]
        ]

    templates = WORKFLOW_TEMPLATES.get((cat_b, cat_a))
    if templates:
        return [
            {"workflow": t["workflow"],
             "description": t["description"].format(a_name=b_name, b_name=a_name)}
            for t in templates[:4]
        ]

    # Default
    return [
        {"workflow": t["workflow"],
         "description": t["description"].format(a_name=a_name, b_name=b_name)}
        for t in DEFAULT_WORKFLOWS
    ]


def get_setup_considerations(tool_a, tool_b, a_name, b_name, tools_meta):
    """Generate setup considerations for a tool pair."""
    cat_a = get_tool_categories(tool_a, tools_meta)
    cat_b = get_tool_categories(tool_b, tools_meta)

    considerations = []

    # Field ownership
    considerations.append(
        f"Decide which system owns each data field before connecting. "
        f"When {a_name} and {b_name} both store the same data, sync conflicts "
        f"are inevitable without clear ownership rules."
    )

    # Integration method
    if cat_a == 'orchestration' or cat_b == 'orchestration':
        considerations.append(
            f"Check whether the native connector between these tools handles your "
            f"use case before building custom automations. Native integrations are "
            f"easier to maintain and less likely to break during platform updates."
        )
    else:
        considerations.append(
            f"Start with the native integration if available. If you need custom "
            f"field mappings or conditional logic, consider an iPaaS tool like "
            f"Workato or Zapier as middleware."
        )

    # Testing
    considerations.append(
        f"Test the integration with a small subset of records before enabling "
        f"full sync. Watch for duplicate records, field mapping errors, and "
        f"API rate limit issues during the first week."
    )

    return considerations


def get_faqs(tool_a, tool_b, a_name, b_name, count, tc, tools_meta):
    """Generate 3 FAQs for an integration page."""
    a_jobs = tools_meta.get(tool_a, {}).get('job_count', 0)
    b_jobs = tools_meta.get(tool_b, {}).get('job_count', 0)

    faqs = []

    # FAQ 1: Do I need both?
    faqs.append({
        "q": f"Do I need both {a_name} and {b_name}?",
        "a": f"It depends on your team's workflows. These tools appear together "
             f"in {count} job postings in our dataset, suggesting many companies "
             f"use both. Evaluate whether one platform can cover the other's "
             f"core functionality before committing to two vendor relationships."
    })

    # FAQ 2: Integration cost/complexity
    faqs.append({
        "q": f"How difficult is the {a_name}-{b_name} integration to set up?",
        "a": f"Most teams can get a basic integration running in a few hours "
             f"using native connectors or standard iPaaS tools. Complex setups "
             f"with custom field mappings, conditional sync rules, and multi-object "
             f"relationships typically take 1-2 weeks of ops work."
    })

    # FAQ 3: Job market context
    faqs.append({
        "q": f"How common is the {a_name} and {b_name} combination in job postings?",
        "a": f"We found {count} job postings mentioning both tools together. "
             f"{a_name} appears in {a_jobs} total postings and {b_name} in "
             f"{b_jobs}. The co-occurrence rate suggests this is a "
             f"{'well-established' if count >= 15 else 'growing'} pairing "
             f"in B2B tech stacks."
    })

    return faqs


def main():
    dry_run = '--dry-run' in sys.argv
    limit = None
    for arg in sys.argv[1:]:
        if arg.startswith('--limit='):
            limit = int(arg.split('=')[1])

    global _category_map
    tc = load("tool_content.json")
    tools = load("tools.json")
    cooc = load("cooccurrence.json")
    integ = load("integrations.json")
    cats = load("categories.json")
    tools_meta = {t['slug']: t for t in tools['tools']}
    _category_map = build_category_map(cats)

    # Get existing pairs
    existing_pairs = set()
    for i in integ['integrations']:
        existing_pairs.add((i['tool_a'], i['tool_b']))
        existing_pairs.add((i['tool_b'], i['tool_a']))

    # Collect all candidate pairs
    cooc_data = cooc.get('cooccurrence', cooc)
    pair_counts = {}
    for tool_slug, co_tools in cooc_data.items():
        if tool_slug not in tc:
            continue
        if isinstance(co_tools, list):
            for entry in co_tools:
                other = entry.get('slug', entry.get('tool', ''))
                count = entry.get('count', entry.get('cooccurrence_count', 0))
                if other and other in tc and count >= MIN_COOCCURRENCE:
                    pair = tuple(sorted([tool_slug, other]))
                    pair_counts[pair] = max(pair_counts.get(pair, 0), count)
        elif isinstance(co_tools, dict):
            for other, count in co_tools.items():
                if other in tc and count >= MIN_COOCCURRENCE:
                    pair = tuple(sorted([tool_slug, other]))
                    pair_counts[pair] = max(pair_counts.get(pair, 0), count)

    # Sort by count, exclude existing
    candidates = [
        (pair, count) for pair, count in sorted(pair_counts.items(), key=lambda x: -x[1])
        if pair not in existing_pairs
    ]

    if limit:
        candidates = candidates[:limit]

    added = 0
    for (a, b), count in candidates:
        a_name = tc[a].get('display_name', a)
        b_name = tc[b].get('display_name', b)

        # Put higher-job-count tool first for consistency
        a_jobs = tools_meta.get(a, {}).get('job_count', 0)
        b_jobs = tools_meta.get(b, {}).get('job_count', 0)
        if b_jobs > a_jobs:
            a, b = b, a
            a_name, b_name = b_name, a_name

        slug = f"{a}-{b}"

        overview = (
            f"{a_name} and {b_name} appear together in {count} job postings "
            f"in our dataset. "
        )

        # Add context based on what each tool does
        a_best = tc.get(a, {}).get('best_for', '')
        b_best = tc.get(b, {}).get('best_for', '')
        if a_best and b_best:
            overview += (
                f"{a_name} is typically used for {a_best.lower()}, "
                f"while {b_name} handles {b_best.lower()}. "
            )
        overview += (
            f"The combination gives teams a connected workflow between both platforms."
        )

        workflows = get_workflows(a, b, tools_meta, a_name, b_name)
        setup = get_setup_considerations(a, b, a_name, b_name, tools_meta)
        faqs = get_faqs(a, b, a_name, b_name, count, tc, tools_meta)

        entry = {
            "slug": slug,
            "tool_a": a,
            "tool_b": b,
            "cooccurrence_count": count,
            "title": f"{a_name} + {b_name} Integration Guide",
            "meta_description": (
                f"How to integrate {a_name} and {b_name}. Common workflows, "
                f"setup guide, and data from {count} job postings mentioning both tools."
            )[:160],
            "overview": overview,
            "how_they_work_together": workflows,
            "setup_considerations": setup,
            "faq": faqs,
            "date_published": TODAY,
            "date_modified": TODAY,
        }

        integ['integrations'].append(entry)
        print(f"  {slug}: {count} co-mentions, {len(workflows)} workflows")
        added += 1

    print(f"\nTotal integration pages added: {added}")
    print(f"Total integration pages now: {len(integ['integrations'])}")

    if dry_run:
        print("\n[DRY RUN] No changes written.")
    else:
        save("integrations.json", integ)
        print(f"\nWritten to {DATA}/integrations.json")


if __name__ == '__main__':
    main()
