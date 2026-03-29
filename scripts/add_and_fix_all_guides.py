#!/usr/bin/env python3
"""Add 10 new guides, fix banned words, and ensure 1500+ word counts. Single pass."""

import json
import sys

# First, run the add script
exec(open('scripts/add_comparison_guides.py').read())

# Now load the result and apply all fixes
with open('data/guides.json', 'r') as f:
    data = json.load(f)

new_slugs = [
    'fivetran-vs-airbyte', 'census-vs-hightouch', 'snowflake-vs-bigquery-for-revops',
    'dbt-vs-matillion', 'hubspot-vs-salesforce-data-model', 'segment-vs-rudderstack',
    'clay-vs-clearbit-enrichment', 'best-crm-integrations-2026',
    'best-etl-tools-small-teams', 'best-data-quality-tools-2026'
]

for g in data['guides']:
    if g['slug'] not in new_slugs:
        continue

    # ---- Fix banned words ----
    for s in g['sections']:
        s['content'] = s['content'].replace('Setup is genuinely simple.', 'Setup is simple.')
        s['content'] = s['content'].replace("they don't actually need", "they don't need")
        s['content'] = s['content'].replace('For teams with truly no budget,', 'For teams with zero budget,')
        s['content'] = s['content'].replace('what was actually said in meetings', 'what was said in meetings')
        if s['heading'] == 'What Small Teams Actually Need from ETL':
            s['heading'] = 'What Small Teams Need from ETL'

    for f in g.get('faq', []):
        f['q'] = f['q'].replace('Is Airbyte really free?', 'Is Airbyte free to use?')
        f['a'] = f['a'].replace(
            "its explicit relational model actually maps more cleanly",
            "its explicit relational model maps more cleanly"
        )

    # ---- Add content to reach 1500+ words per guide ----

    if g['slug'] == 'fivetran-vs-airbyte':
        for s in g['sections']:
            if s['heading'] == 'Our Verdict: Who Should Pick What':
                s['content'] += "\n\nOne factor worth considering is long-term vendor stability. Fivetran is publicly traded and well-capitalized. Airbyte has strong VC backing and a growing open-source community. Both are likely to be around in 5 years. The risk profile is comparable, so base your decision on technical and financial fit rather than vendor viability concerns."
            if s['heading'] == 'Pricing: Where the Math Gets Interesting':
                s['content'] += "\n\nOne negotiation tip: Fivetran offers significant discounts for annual commitments and multi-year deals. If you're confident in your choice, pushing for an annual contract can reduce the per-MAR rate by 20-30%. Airbyte Cloud doesn't typically offer comparable discounts because their baseline pricing is already lower."
            if s['heading'] == 'The Core Difference: Managed vs Open-Source':
                s['content'] += "\n\nA middle ground exists. Airbyte Cloud offers a managed version of the open-source platform, handling infrastructure while keeping costs below Fivetran. This option didn't exist in Airbyte's early days but has matured into a viable production choice for teams that want managed convenience without Fivetran's pricing."
            if s['heading'] == 'Connector Coverage and Quality':
                s['content'] += "\n\nWorth noting: both platforms are expanding connector counts rapidly. Check the current connector catalog for your specific sources before deciding. A tool with 300 connectors that covers your 8 sources is better than one with 500 connectors that's missing the one you need."
            if s['heading'] == 'Reliability and Monitoring':
                s['content'] += "\n\nA practical approach to evaluating reliability: ask each vendor for their incident history over the past 6 months. Check their status pages and community forums for user reports. Marketing materials will always claim 99.9% uptime. Real-world experience may differ, especially for specific connectors."

    if g['slug'] == 'census-vs-hightouch':
        for s in g['sections']:
            if s['heading'] == 'Our Verdict: Census for Data Teams, Hightouch for Ops Teams':
                s['content'] += "\n\nOne additional consideration: evaluate where each tool is heading. Hightouch has been expanding toward composable CDP territory, adding more marketing-centric features. Census has been deepening its data infrastructure integrations. Your roadmap alignment with the vendor's product direction matters for long-term satisfaction."
            if s['heading'] == 'What Reverse ETL Solves for RevOps Teams':
                s['content'] += "\n\nThe adoption curve for reverse ETL has accelerated in 2025-2026. What was a niche category three years ago is now standard infrastructure for data-forward companies. Both Census and Hightouch have grown their customer bases significantly, with Hightouch crossing 1,000 customers and Census reaching similar scale. The category is proven."
            if s['heading'] == 'Sync Performance and Reliability':
                s['content'] += "\n\nOne practical tip: run a parallel evaluation. Set up both tools on the same warehouse with the same sync targets. Run them side-by-side for two weeks and compare sync times, error rates, and ease of troubleshooting. Both offer free tiers sufficient for this evaluation. Real-world performance on your data matters more than benchmark claims."
            if s['heading'] == "Census: The Data Team's Tool":
                s['content'] += "\n\nCensus also offers a dbt integration that surfaces model documentation and freshness directly in the Census UI. Data teams using dbt can see which models power which syncs, creating a natural lineage view from transformation to activation."
            if s['heading'] == 'Hightouch: The Marketing-Friendly Option':
                s['content'] += "\n\nHightouch's Audience overlap analysis lets marketing teams see how segments intersect before activating them. This prevents the common mistake of targeting the same users across multiple campaigns, which wastes ad spend and annoys customers."
            if s['heading'] == 'Integration Ecosystem and Destinations':
                s['content'] += "\n\nBoth platforms are adding AI-powered features. Census introduced AI-generated sync suggestions. Hightouch added AI-powered audience building. These features are early-stage but signal where the category is heading: less manual configuration, more intelligent automation."
            if s['heading'] == 'Governance and Security':
                s['content'] += "\n\nFor teams evaluating governance needs, ask this question: who in your organization will configure and manage reverse ETL syncs? If the answer includes non-technical users, Hightouch's permission model is easier to set up. If only data engineers will touch it, Census's granular controls give you more precision."

    if g['slug'] == 'snowflake-vs-bigquery-for-revops':
        for s in g['sections']:
            if s['heading'] == 'Our Verdict: Snowflake for Most, BigQuery for Google Shops':
                s['content'] += "\n\nA third option worth mentioning: Databricks is gaining traction for teams with both analytics and ML/AI workloads. For pure RevOps analytics, Snowflake or BigQuery is simpler. But if your company is investing in AI-powered lead scoring or predictive analytics, Databricks' unified analytics and ML platform deserves evaluation alongside the other two."
            if s['heading'] == 'Cost: The Real Comparison':
                s['content'] += "\n\nFor accurate cost comparison, run the same workload on both platforms using free credits. Both Snowflake and BigQuery offer enough free compute to simulate a realistic RevOps analytics environment. Track query costs, storage costs, and any data transfer charges over a two-week period. Extrapolate from there."
            if s['heading'] == 'Architecture and How It Affects You':
                s['content'] += "\n\nOne practical consideration: Snowflake runs on top of AWS, Azure, or GCP. You choose your cloud provider when setting up your Snowflake account. If your company is standardized on AWS, running Snowflake on AWS keeps data within the same network, reducing latency and data transfer costs."
            if s['heading'] == 'Ecosystem and Tool Compatibility':
                s['content'] += "\n\nAnother ecosystem consideration: Snowflake's native app framework lets vendors build applications that run inside Snowflake. This means some analytics and enrichment tools can operate on your data without it ever leaving your Snowflake account. For security-conscious teams, this architecture is compelling."
            if s['heading'] == 'Team Skills and Learning Curve':
                s['content'] += "\n\nBoth platforms offer free online training. Snowflake University and Google Cloud Skills Boost provide self-paced courses that can get a new user productive in 1-2 weeks. Factor training into your timeline but don't let it be a deciding factor. Either platform's SQL dialect is learnable quickly."

    if g['slug'] == 'dbt-vs-matillion':
        for s in g['sections']:
            if s['heading'] == 'Our Verdict: dbt for Most Data Teams':
                s['content'] += "\n\nIf your team is currently on Matillion and considering a switch, don't rush it. Migration from visual pipelines to dbt SQL models is time-consuming. Plan for 2-4 months of parallel operation. Prioritize migrating your most critical transformations first and validate that dbt outputs match Matillion outputs before cutting over."
            if s['heading'] == 'Pricing and Total Cost':
                s['content'] += "\n\nFactor in the cost of community resources. dbt's free Slack community, extensive documentation, and blog content reduce the cost of learning and troubleshooting. Matillion's documentation is adequate but the community is smaller, which means more time spent solving problems independently or relying on paid support."
            if s['heading'] == 'Approach: Code-First vs Visual-First':
                s['content'] += "\n\nA common pattern for mixed teams: use dbt for core transformation models that are well-defined and change infrequently, and Matillion for ad-hoc data preparation tasks where visual building is faster. This hybrid approach is unusual but works for organizations with both engineering and analyst personas working on data."
            if s['heading'] == 'Testing and Data Quality':
                s['content'] += "\n\nA practical recommendation: start with dbt's built-in generic tests (not_null, unique, accepted_values, relationships) on every model. These catch 80% of common data quality issues with minimal configuration. Add custom tests as you discover model-specific edge cases in production."
            if s['heading'] == 'Version Control and Collaboration':
                s['content'] += "\n\nTeam onboarding is another consideration. A new hire who knows SQL can contribute to a dbt project on day one by reading existing models and understanding the logic. A new hire on Matillion needs to learn the visual interface conventions and component library before being productive. SQL is a more transferable skill."

    if g['slug'] == 'hubspot-vs-salesforce-data-model':
        for s in g['sections']:
            if s['heading'] == 'Our Verdict: Match the CRM to Your Team':
                s['content'] += "\n\nOne overlooked factor: the talent market. Salesforce administrators and developers command $80,000-$140,000/year in salary. HubSpot specialists command $60,000-$100,000/year. If you're hiring a dedicated CRM admin, the salary savings on HubSpot can offset a year of software costs."
            if s['heading'] == 'Object Architecture: Flexible vs Opinionated':
                s['content'] += "\n\nA concrete example: modeling a multi-product company on HubSpot requires creative use of line items and deal pipelines to approximate what Salesforce handles with custom objects and junction relationships. If your business sells multiple products to the same account with different sales cycles, Salesforce's data model handles this natively."

    if g['slug'] == 'segment-vs-rudderstack':
        for s in g['sections']:
            if s['heading'] == 'Our Verdict: RudderStack for Value, Segment for Ecosystem':
                s['content'] += "\n\nThe market trend favors warehouse-native approaches. As more companies adopt Snowflake and BigQuery as central data platforms, the argument for running CDP logic on top of your warehouse (RudderStack's model) strengthens. Segment recognizes this trend and has added warehouse-native features, but RudderStack was built for this architecture from day one."
            if s['heading'] == 'Pricing: Where RudderStack Wins Decisively':
                s['content'] += "\n\nA practical note on cost management: both platforms charge based on event volume. The most effective cost control is tracking plan hygiene. Audit your tracked events quarterly. Remove events nobody queries or uses in destinations. Most companies track 2-3x more events than they use, inflating CDP costs unnecessarily."
            if s['heading'] == 'Core Philosophy: Cloud CDP vs Warehouse-Native CDP':
                s['content'] += "\n\nThe warehouse-native trend extends beyond CDPs. Reverse ETL tools, audience builders, and even some analytics platforms are moving toward warehouse-native architectures. Choosing RudderStack aligns with this broader industry direction. Segment's cloud-first approach works but creates an additional data copy outside your warehouse."
            if s['heading'] == 'Event Collection and SDK Quality':
                s['content'] += "\n\nOne implementation tip: regardless of which CDP you choose, start with a tracking plan. Document every event you intend to track, its properties, and which destinations need it. Both Segment and RudderStack support tracking plan enforcement, but the plan itself is your responsibility. Sloppy instrumentation creates downstream headaches that no tool can fix."
            if s['heading'] == 'Identity Resolution and Profiles':
                s['content'] += "\n\nFor B2B companies specifically, identity resolution across accounts (not just individuals) matters. Connecting multiple contacts at the same company, linking anonymous website sessions to known accounts, and building account-level engagement scores require identity resolution that thinks beyond individual users. Evaluate how each platform handles account-level identity, not just person-level."

    if g['slug'] == 'clay-vs-clearbit-enrichment':
        for s in g['sections']:
            if s['heading'] == 'Our Verdict: Clay for Outbound, Clearbit for Passive Enrichment':
                s['content'] += "\n\nThe broader trend in enrichment is moving toward multi-source waterfalls and away from single-provider dependency. Clay represents where the market is heading. Clearbit represents the previous generation. For teams making a new investment, Clay is the forward-looking choice. For existing Clearbit users on HubSpot, there's no urgency to switch."
            if s['heading'] == 'Pricing: Complex vs Simple':
                s['content'] += "\n\nBudget planning tip: run a small test batch through Clay before committing to a plan. Enrich 100 contacts and track credit consumption per contact. Multiply by your expected monthly volume to estimate real costs. The per-contact credit usage varies significantly based on how many waterfall providers you enable."
            if s['heading'] == 'Data Quality and Coverage':
                s['content'] += "\n\nOne quality consideration often overlooked: data freshness. Clearbit maintains a single dataset and controls update frequency. Clay's waterfall pulls from providers with varying update cadences. A phone number from one provider might be current while another returns a number from 18 months ago. Cross-referencing multiple sources helps, but freshness varies."

    if g['slug'] == 'best-crm-integrations-2026':
        for s in g['sections']:
            if s['heading'] == 'Integration Strategy: Less Is More':
                s['content'] += "\n\nDocument every integration in a central inventory. Track: what data flows between which systems, who owns the integration, when it was last audited, and what breaks if it fails. This integration map saves hours of debugging when something inevitably goes wrong. A simple spreadsheet works. Update it every time you add or modify an integration."
            if s['heading'] == 'How We Evaluated CRM Integrations':
                s['content'] += "\n\nWe weighted data quality impact highest because it compounds. An integration that improves CRM data quality benefits every other system that reads from your CRM. Enrichment tools scored highest on this dimension, which is why they lead our ranking."
            if s['heading'] == '1. Enrichment: Clay':
                s['content'] += "\n\nAlternative for smaller teams: Apollo offers built-in CRM enrichment at a lower price point. Coverage isn't as broad as Clay's waterfall, but for teams with straightforward enrichment needs (US-based, B2B tech), Apollo provides good value."
            if s['heading'] == '4. Data Warehouse Sync: Fivetran':
                s['content'] += "\n\nBudget alternative: Airbyte Cloud handles the same warehouse sync workflow at 40-60% lower cost. Connector quality is slightly below Fivetran's for edge cases, but the core CRM connectors work well. For cost-conscious teams, Airbyte Cloud is the better ETL integration choice."
            if s['heading'] == '2. Sales Engagement: Salesloft':
                s['content'] += "\n\nAlternative: Outreach.io offers comparable functionality with a slightly different user experience. The choice between Salesloft and Outreach often comes down to which UI your reps prefer and which negotiates better pricing for your team size. Both integrate deeply with Salesforce and HubSpot."
            if s['heading'] == '6-10: Essential Supporting Integrations':
                s['content'] += "\n\nHonorable mentions that didn't make the top 10: Drift/Qualified for conversational marketing and pipeline acceleration, Clari for revenue forecasting and pipeline inspection, and Demandbase for ABM orchestration. Each serves a specific use case well but is more niche than the top 10 picks."

    if g['slug'] == 'best-etl-tools-small-teams':
        for s in g['sections']:
            if s['heading'] == 'Our Recommendation: Start with Fivetran Free Tier':
                s['content'] += "\n\nOne common objection: 'We'll outgrow the free tier quickly.' Good. That means you're using the tool and getting value from it. When you hit paid tiers, you'll have usage data to evaluate whether to stay on Fivetran or switch to a cheaper alternative. Making that decision with data is better than making it in theory."
            if s['heading'] == 'What Small Teams Need from ETL':
                s['content'] += "\n\nAvoid the trap of evaluating tools for your future scale. A 10-person company doesn't need to optimize for the data volumes they'll have at 500 people. Pick the simplest tool that works today. You can re-evaluate in 12-18 months when your needs are clearer and your budget is larger."
            if s['heading'] == '2. Airbyte Cloud (Best for Budget-Conscious Teams)':
                s['content'] += "\n\nOne practical advantage of Airbyte: if your small team grows into a larger data team, Airbyte's self-hosted option gives you a migration path to zero-license-cost ETL without changing tools. You start on Airbyte Cloud and move to self-hosted when you have engineering capacity."
            if s['heading'] == '4. Zapier / Make (Best for Non-Data-Warehouse Workflows)':
                s['content'] += "\n\nn8n is a self-hosted alternative to Zapier and Make that costs nothing for the software license. If your team has a developer who can deploy and maintain it, n8n provides workflow automation comparable to Make without recurring subscription fees. The trade-off is self-hosting responsibility."

    if g['slug'] == 'best-data-quality-tools-2026':
        for s in g['sections']:
            if s['heading'] == 'Data Quality ROI: Making the Business Case':
                s['content'] += "\n\nPresent the ROI case with your own data. Pull your current bounce rates, connect rates, and duplicate record counts. Calculate the cost of each metric at current levels. Then project the improvement from a data quality tool based on vendor benchmarks (discount them by 30% for conservative estimates). The numbers sell the investment better than any vendor pitch deck."
            if s['heading'] == 'Why Data Quality Matters More in 2026':
                s['content'] += "\n\nAI and machine learning adoption in RevOps makes data quality even more critical. AI-powered lead scoring, forecasting, and personalization are only as good as the data they're trained on. Teams adopting AI tools without clean data are building on a broken foundation. Fix the data before investing in AI."

with open('data/guides.json', 'w') as f:
    json.dump(data, f, indent=2)

# Final verification
banned = ['genuinely','truly','really','actually','robust','leverage','synergy','holistic','cutting-edge','game-changer','paradigm shift','continues to',"in today's market"]

print("\n=== FINAL VERIFICATION ===")
all_pass = True
for g in data['guides']:
    if g['slug'] in new_slugs:
        text = g['intro'] + ' '
        for s in g['sections']:
            text += s['heading'] + ' ' + s['content'] + ' '
        for f in g.get('faq', []):
            text += f['q'] + ' ' + f['a'] + ' '
        wc = len(text.split())
        found_banned = [b for b in banned if b.lower() in text.lower()]
        has_em = '\u2014' in text or '\u2013' in text
        tl = len(g['title'])
        ml = len(g['meta_description'])
        fc = len(g.get('faq', []))
        issues = []
        if wc < 1500: issues.append(f'LOW ({wc})')
        if has_em: issues.append('EM DASH')
        if found_banned: issues.append(f'BANNED: {found_banned}')
        if tl > 60: issues.append(f'TITLE {tl}')
        if ml < 120 or ml > 160: issues.append(f'META {ml}')
        if fc < 4: issues.append(f'FAQ {fc}')
        status = ', '.join(issues) if issues else 'PASS'
        if issues: all_pass = False
        print(f'  {g["slug"]}: {wc} words, title={tl}, meta={ml}, faq={fc} -> {status}')

if all_pass:
    print("\nAll 10 guides pass all checks.")
else:
    print("\nSome guides have issues.")
