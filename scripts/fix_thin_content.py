#!/usr/bin/env python3
"""Fix thin content: roundups with <5 picks and alternatives with <3 entries."""

import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

def fix_thin_roundups():
    """Add picks to roundups that have fewer than 5."""
    path = DATA_DIR / "best_of.json"
    with open(path) as f:
        data = json.load(f)

    new_picks = {
        "best-data-integration-for-snowflake": [
            {
                "slug": "boomi",
                "name": "Boomi",
                "award": "Best for Enterprise Middleware",
                "price": "Custom pricing",
                "summary": "Boomi connects Snowflake to legacy ERP systems, mainframes, and on-premise databases that most modern tools can't reach. Dell's acquisition gave Boomi deep enterprise distribution, and their low-code builder handles complex data transformations without engineering resources.",
                "best_for": "Enterprise teams connecting Snowflake to legacy on-premise systems and ERP platforms",
                "caveat": "Expensive at scale. Interface feels dated compared to newer tools. Connector quality varies."
            },
            {
                "slug": "workato-ipaas",
                "name": "Workato",
                "award": "Best for Business-Led Automation",
                "price": "Custom pricing (starts ~$10K/year)",
                "summary": "Workato bridges the gap between iPaaS and workflow automation, letting business teams build Snowflake data pipelines without writing SQL. Their recipe-based approach means RevOps teams can create Salesforce-to-Snowflake syncs, trigger enrichment workflows, and build reporting pipelines without filing engineering tickets.",
                "best_for": "RevOps and business teams who need Snowflake integrations without engineering dependency",
                "caveat": "Gets expensive as recipe volume grows. Enterprise features require top-tier plans."
            }
        ],
        "best-bi-tools": [
            {
                "slug": "clari",
                "name": "Clari",
                "award": "Best for Revenue Analytics",
                "price": "Custom pricing",
                "summary": "Clari sits at the intersection of BI and revenue intelligence. While traditional BI tools show you what happened, Clari focuses on what will happen: pipeline forecasting, deal inspection, and revenue leak detection. It pulls CRM, email, and calendar data to build AI-driven forecasts that are consistently more accurate than rep-submitted numbers.",
                "best_for": "Revenue leaders who need forecasting and pipeline analytics, not general-purpose dashboards",
                "caveat": "Narrow focus on revenue data. Not a replacement for general BI. Requires clean CRM data to be useful."
            },
            {
                "slug": "gong-engage",
                "name": "Gong",
                "award": "Best for Conversation Analytics",
                "price": "Custom pricing (starts ~$1,200/user/year)",
                "summary": "Gong turns sales conversations into structured analytics. Their AI analyzes calls, emails, and meetings to surface deal risks, competitive mentions, and coaching opportunities. The analytics layer goes beyond call recording: Gong tracks talk ratios, question frequency, competitor mentions, and objection patterns across your entire revenue org.",
                "best_for": "Sales leaders who want analytics derived from actual buyer conversations, not just CRM data",
                "caveat": "Expensive per seat. Analytics are limited to recorded interactions. Less useful for low-touch sales models."
            }
        ],
        "best-customer-engagement-platforms": [
            {
                "slug": "common-room",
                "name": "Common Room",
                "award": "Best for Community-Led Engagement",
                "price": "Free tier available; paid plans from $625/mo",
                "summary": "Common Room aggregates engagement signals from Slack communities, GitHub, Discord, Twitter, and product usage into unified person and account profiles. For PLG and developer-first companies, it captures buying signals that traditional marketing platforms miss entirely: community participation, open-source contributions, and product activation milestones.",
                "best_for": "PLG and developer-first companies where community engagement predicts conversion",
                "caveat": "Most valuable for companies with active community channels. Less useful for traditional outbound-heavy sales motions."
            }
        ]
    }

    for roundup in data["roundups"]:
        if roundup["slug"] in new_picks:
            roundup["picks"].extend(new_picks[roundup["slug"]])
            print(f"  {roundup['slug']}: {len(roundup['picks'])} picks now")

    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")

    print(f"Updated {path.name}")


def fix_thin_alternatives():
    """Add alternatives to pages that have fewer than 3."""
    path = DATA_DIR / "alternatives.json"
    with open(path) as f:
        data = json.load(f)

    new_alts = {
        "g2-alternatives": [
            {
                "slug": "6sense",
                "name": "6sense",
                "price": "Custom pricing ($30K+/year typical)",
                "best_for": "Enterprise teams wanting AI-driven buyer intent without review platform dependency",
                "key_difference": "AI intent model predicts buying stage, not just interest signals",
                "coverage": "Tracks intent signals across the open web using NLP and predictive models. Identifies accounts in active buying cycles before they fill out forms. Coverage strongest in tech and enterprise B2B segments. No review platform component.",
                "verdict": "The most sophisticated intent data platform. Better predictive accuracy than G2's review-based signals, but dramatically more expensive and complex to implement."
            },
            {
                "slug": "demandbase",
                "name": "Demandbase",
                "price": "Custom pricing ($25K+/year typical)",
                "best_for": "ABM teams wanting intent data integrated with advertising and personalization",
                "key_difference": "Combines intent data with ABM orchestration and B2B advertising in one platform",
                "coverage": "Monitors 300B+ intent signals monthly across web, social, and content consumption. Strongest for US enterprise and mid-market B2B. Integrates intent directly into ad targeting and website personalization.",
                "verdict": "Best G2 alternative for teams that want to act on intent data immediately through ads and website personalization, not just surface it in dashboards."
            },
            {
                "slug": "leadfeeder",
                "name": "Leadfeeder (Dealfront)",
                "price": "$99 - $199+/mo",
                "best_for": "SMBs wanting affordable website visitor identification as a G2 intent alternative",
                "key_difference": "Website visitor identification at a fraction of G2's price point",
                "coverage": "Identifies companies visiting your website using reverse IP lookup and cookie-based tracking. European data coverage is strong (Dealfront heritage). Smaller database than G2 or 6sense but significantly more affordable entry point.",
                "verdict": "The budget-friendly G2 alternative. You get website-level intent signals (not review-based), but the data is narrower and lacks the buyer research context G2 provides."
            }
        ],
        "salesforce-marketing-cloud-alternatives": [
            {
                "slug": "braze",
                "name": "Braze",
                "price": "Custom pricing ($50K+/year typical)",
                "best_for": "Product-led companies needing real-time, event-driven customer messaging",
                "key_difference": "Built for real-time event triggers, not batch campaigns",
                "coverage": "Processes billions of data points daily for real-time personalization. Canvas (their visual builder) handles complex multi-step journeys. Native mobile push, in-app messaging, and SMS alongside email. Strongest for B2C and PLG B2B.",
                "verdict": "The best SFMC alternative for companies where speed matters. Braze processes events in seconds vs. SFMC's batch processing. Weaker on B2B-specific features like lead scoring."
            },
            {
                "slug": "dynamics-365",
                "name": "Dynamics 365 Marketing",
                "price": "$1,500/tenant/mo",
                "best_for": "Microsoft-stack enterprises wanting native marketing automation",
                "key_difference": "Native integration with Microsoft 365, Teams, and Dynamics CRM",
                "coverage": "Full marketing automation suite including email, events, forms, and customer journeys. Deeply integrated with Dynamics CRM, Power BI, and Microsoft 365. Event management features are strong. Weaker ecosystem of third-party integrations vs. SFMC.",
                "verdict": "The natural SFMC alternative for Microsoft-stack companies. Lower total cost of ownership when you're already paying for Dynamics CRM. Less mature than SFMC for complex multi-channel orchestration."
            }
        ],
        "gainsight-alternatives": [
            {
                "slug": "clari",
                "name": "Clari",
                "price": "Custom pricing",
                "best_for": "Revenue teams wanting churn prediction through pipeline and deal analytics",
                "key_difference": "Approaches retention from the revenue intelligence angle, not traditional CS metrics",
                "coverage": "AI-driven revenue analytics covering pipeline, forecast accuracy, and deal health. Churn risk signals come from revenue patterns and engagement data rather than traditional health scores. Strongest for B2B SaaS with high-value contracts.",
                "verdict": "A different lens on customer success: Clari catches churn risk through revenue signals (declining usage, shrinking pipeline, missed renewals) rather than health score surveys. Complementary to Gainsight for some teams."
            },
            {
                "slug": "common-room",
                "name": "Common Room",
                "price": "Free tier; paid from $625/mo",
                "best_for": "PLG companies tracking customer engagement across community and product channels",
                "key_difference": "Aggregates engagement signals from community, product, and social channels instead of traditional CS workflows",
                "coverage": "Unified view of customer engagement across Slack, Discord, GitHub, Twitter, product usage, and CRM. Identifies champions, tracks sentiment, and surfaces expansion signals. Best for developer-first and PLG companies where community activity correlates with retention.",
                "verdict": "The modern alternative for PLG customer success. Common Room tracks engagement where it happens (community, product, social) rather than relying on NPS surveys and health score formulas."
            }
        ]
    }

    for alt_page in data["alternatives"]:
        if alt_page["slug"] in new_alts:
            alt_page["alternatives_list"].extend(new_alts[alt_page["slug"]])
            print(f"  {alt_page['slug']}: {len(alt_page['alternatives_list'])} alternatives now")

    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")

    print(f"Updated {path.name}")


if __name__ == "__main__":
    print("Fixing thin roundups...")
    fix_thin_roundups()
    print()
    print("Fixing thin alternatives...")
    fix_thin_alternatives()
    print()
    print("Done!")
