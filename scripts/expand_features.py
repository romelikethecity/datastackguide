#!/usr/bin/env python3
"""
Expand key_features descriptions for 6 tools in tool_content.json.
Target: 350-500 chars per feature description.
Only modifies key_features[].description for the specified tools.
"""

import json
import os

TOOL_CONTENT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data", "tool_content.json"
)

# New expanded descriptions keyed by tool slug -> feature name -> new description
EXPANDED = {
    "salesforce-marketing-cloud": {
        "Journey Builder": (
            "Design cross-channel customer journeys with real-time behavioral triggers, "
            "conditional branching, wait steps, and automated actions across email, SMS, push, "
            "and ads. Journey Builder is the primary reason enterprises choose SFMC over "
            "HubSpot or Marketo. It reacts to prospect behavior in real time, branching paths "
            "when a lead opens an email, clicks a link, or visits a pricing page. Orchestration "
            "depth is among the best available, but effective journeys require a trained admin."
        ),
        "Email Studio": (
            "Enterprise email marketing with drag-and-drop builders, dynamic content, A/B "
            "testing, deliverability tools, and advanced personalization powered by Salesforce "
            "data. Email Studio handles volumes that mid-market tools cannot, supporting sends "
            "to millions of contacts with sophisticated segmentation. Dynamic content blocks "
            "swap messaging based on recipient attributes from Data Extensions. The limitation "
            "is that Email Studio lives in its own interface, separate from Journey Builder."
        ),
        "Einstein AI": (
            "AI-powered features including predictive send-time optimization, engagement "
            "scoring, content recommendations, and automated audience segmentation. Einstein "
            "analyzes historical engagement data to predict when each contact is most likely "
            "to open an email and scores contacts by their conversion probability. These "
            "features require sufficient data to train on, so new deployments won't see "
            "meaningful AI output for several weeks. Included in Corporate tier and above."
        ),
        "Mobile Studio": (
            "SMS, MMS, and push notification capabilities that integrate into cross-channel "
            "journeys, extending marketing reach beyond email to mobile channels. Teams use "
            "Mobile Studio for appointment reminders, event confirmations, and time-sensitive "
            "promotions triggered by Journey Builder logic. SMS delivery rates typically exceed "
            "95%, making it a strong complement to email for high-priority messages. Mobile "
            "Studio is licensed separately, so adding SMS increases total contract cost."
        ),
        "Advertising Studio": (
            "Sync CRM audiences to Google, Facebook, and LinkedIn for targeted ad campaigns "
            "and retargeting using Salesforce data. Marketing teams suppress existing customers "
            "from acquisition campaigns, retarget leads who viewed pricing but didn't convert, "
            "or build lookalike audiences from top customer segments. Audience sync frequency "
            "depends on your tier, with Enterprise getting near-real-time updates. Advertising "
            "Studio is an add-on module with its own separate pricing."
        ),
        "Data Extensions & Segmentation": (
            "SFMC's relational data model for storing, segmenting, and querying marketing data "
            "with SQL-like capabilities for advanced audience building. Unlike Salesforce CRM's "
            "standard objects, Data Extensions use a completely separate database structure "
            "requiring its own data management approach. This disconnect is the most common "
            "source of implementation headaches. Teams that know SQL can build powerful "
            "segments, but the learning curve is steep compared to HubSpot or Mailchimp."
        ),
    },
    "amplemarket": {
        "AI-Powered Prospecting": (
            "Uses AI to analyze your ICP and suggest prospects from its built-in database, "
            "going beyond basic filters to identify prospects that match patterns from your "
            "best customers. The AI examines company size, tech stack, hiring signals, and "
            "role seniority to surface accounts you might miss through manual filtering. This "
            "is Amplemarket's core differentiator over traditional list-building in ZoomInfo "
            "or Apollo. Suggestion quality improves as the system learns from your engagement "
            "data."
        ),
        "AI Message Generation": (
            "Generates personalized outreach messages by analyzing prospect data, company "
            "information, and engagement context. The AI pulls from job title, funding stage, "
            "recent news, and tech stack to craft relevant opening lines. This goes beyond "
            "simple variable insertion (first name, company name) that most sequencing tools "
            "offer. BDR teams report cutting personalization time by 50-60%, though the best "
            "results still come from reps editing AI drafts rather than sending them raw."
        ),
        "Multichannel Sequences": (
            "Build automated sequences that coordinate email, LinkedIn, and phone touches in "
            "a single workflow, with AI-optimized timing and channel selection. Reps design a "
            "sequence that starts with email, follows up on LinkedIn if no reply, and queues a "
            "phone task if LinkedIn goes unanswered. The AI suggests which channel to prioritize "
            "based on each prospect's past behavior. Compared to separate tools for email and "
            "LinkedIn, the unified workflow eliminates duplicate tracking."
        ),
        "Built-In Contact Database": (
            "Integrated B2B contact database with email addresses, phone numbers, and company "
            "firmographics, eliminating the need for a separate data provider. The database "
            "covers standard roles at mid-market and enterprise companies but does not match "
            "dedicated providers in scale. ZoomInfo claims 300M+ contacts, Apollo covers 275M+, "
            "and Amplemarket does not disclose its size. For niche industries or small "
            "businesses, expect gaps requiring a supplemental data source."
        ),
        "Send-Time Optimization": (
            "AI analyzes engagement patterns to determine the optimal send time for each message "
            "to each prospect, improving open and reply rates without manual scheduling. The "
            "system tracks when each prospect has historically opened emails or engaged on "
            "LinkedIn and schedules future touches to match those windows. For teams sending "
            "hundreds of emails daily, this removes the guesswork. The optimization works best "
            "after several weeks of accumulated engagement data."
        ),
        "Engagement Analytics": (
            "Tracks email opens, replies, LinkedIn accepts, and call outcomes across all "
            "channels, providing a unified view of sequence performance. Managers can see which "
            "sequences produce the highest reply rates, which reps outperform, and which "
            "prospects are engaging across multiple channels. Cross-channel attribution is a "
            "clear advantage over separate tools where email and LinkedIn data live in different "
            "dashboards. Reporting covers sequence-level and rep-level metrics."
        ),
    },
    "rb2b": {
        "Person-Level Visitor Identification": (
            "Identifies individual website visitors by name, job title, company, and LinkedIn "
            "profile URL, not just the company they work for. This is the core difference "
            "between RB2B and reverse-IP tools like Leadfeeder or Clearbit Reveal that only "
            "resolve to the account level. Match rates fall between 15-30% of US visitors "
            "depending on traffic quality and audience demographics. International visitors "
            "are not matched. Identification relies on matching first-party data against "
            "identity resolution databases."
        ),
        "Real-Time Slack Notifications": (
            "Pushes instant notifications to Slack when visitors are identified, showing who "
            "visited, what pages they viewed, and their LinkedIn profile. This workflow drove "
            "RB2B's early viral growth: a rep sees 'Sarah Chen, VP Sales at Acme, just viewed "
            "your pricing page' and can reach out within minutes. The Slack integration is "
            "available on the free tier with up to 200 identified profiles per month. Teams "
            "typically route notifications to a dedicated channel with filters for ICP fit."
        ),
        "Page-Level Intent Signals": (
            "Shows which specific pages each visitor viewed (pricing, case studies, product "
            "pages), giving reps context to personalize outreach. A visitor who viewed three "
            "case studies and the pricing page signals stronger buying intent than someone who "
            "bounced off the homepage. Page data is included in Slack notifications and the "
            "RB2B dashboard. This context separates RB2B from a raw contact list, because "
            "reps know what the prospect was researching before they reach out."
        ),
        "Filtering & Segmentation": (
            "Filter identified visitors by job title, company size, industry, and behavior to "
            "focus on prospects that match your ICP. Without filters, a high-traffic site might "
            "surface hundreds of visitors per day, most not worth pursuing. Filtering narrows "
            "notifications to VP+ titles at 50-500 employee companies, for example. Filters "
            "are available on the Pro plan ($199/month). Free tier users receive all identified "
            "visitors without filtering, which creates noise for larger sales teams."
        ),
        "CRM Integration": (
            "Push identified visitors into Salesforce, HubSpot, or other CRMs with visit "
            "context, creating leads or enriching existing contacts with engagement data. When "
            "a known contact visits your site, RB2B updates their CRM record with the visit "
            "timestamp and pages viewed. For new visitors, it creates a lead with LinkedIn "
            "profile and company info. CRM integration is a Pro tier feature. RB2B only "
            "provides LinkedIn URLs, so you will need another source for email and phone."
        ),
        "Simple Pixel-Based Setup": (
            "Install a single tracking pixel on your website with no engineering resources "
            "required. Most teams are running in under 10 minutes. The pixel is a lightweight "
            "JavaScript snippet added to your site header, similar to Google Analytics or a "
            "Facebook pixel. No server-side requirements, no API configuration, no ongoing "
            "maintenance. This simplicity contrasts with enterprise visitor ID tools like "
            "6sense or Demandbase that require weeks of implementation."
        ),
    },
    "rollworks": {
        "Account-Based Advertising": (
            "Programmatic display ad targeting for your ABM account lists, powered by NextRoll's "
            "ad tech infrastructure with strong reach, frequency controls, and cross-device "
            "targeting. NextRoll also runs AdRoll, and that ad tech depth shows in targeting "
            "precision and inventory access. Marketing teams upload a target account list and "
            "RollWorks serves display ads to individuals at those companies. Compared to "
            "LinkedIn Ads for ABM, RollWorks delivers lower CPMs with broader reach."
        ),
        "Account Identification": (
            "Identifies which target accounts are visiting your website, researching your "
            "category, and showing intent signals. The identification combines reverse-IP "
            "resolution with third-party intent data to surface accounts worth pursuing. This "
            "works at the account level, not the individual level, so you see that Acme Corp "
            "visited but not which person. For person-level identification, you would need "
            "RB2B or Clearbit. Account identification is included in the free Starter tier."
        ),
        "Intent Data Integration": (
            "Surfaces intent signals indicating which accounts are researching solutions in "
            "your category, helping prioritize accounts in an active buying cycle. Intent data "
            "comes from third-party content consumption across the web, not just your own "
            "website visits. The scoring is useful for prioritizing outreach but less "
            "sophisticated than 6sense's predictive models. For teams new to ABM, RollWorks "
            "provides a meaningful starting point without the $50K+ commitment that enterprise "
            "intent platforms require."
        ),
        "Account Scoring": (
            "Scores and ranks target accounts based on fit and engagement signals, helping "
            "teams focus time and budget on accounts most likely to convert. Scoring combines "
            "firmographic fit (company size, industry, revenue) with behavioral engagement "
            "(ad interactions, website visits, intent signals) to produce a composite score. "
            "Sales teams use scores to decide which accounts get direct outreach versus nurture "
            "campaigns. Less granular than 6sense or Demandbase, but sufficient for first "
            "ABM programs."
        ),
        "CRM Integration": (
            "Direct integrations with Salesforce and HubSpot sync account lists, engagement "
            "data, and intent signals into your CRM for sales follow-up. Reps see which "
            "accounts are engaging with ads, visiting the website, and showing intent without "
            "leaving their CRM. The integration is bidirectional: CRM account lists feed "
            "RollWorks targeting, and engagement data flows back. Setup takes hours, not weeks, "
            "which is simpler than most enterprise ABM platform integrations."
        ),
        "Free Starter Tier": (
            "A functional free tier that includes account identification and basic intent "
            "signals, letting teams test ABM before committing to paid plans. This is a major "
            "differentiator in the ABM market, where 6sense and Demandbase both require "
            "$30K-$50K+ annual commitments. The free tier is limited (no advertising, basic "
            "intent, fewer accounts), but it gives marketing teams enough data to prove the "
            "concept to leadership before requesting budget. Most teams outgrow it within "
            "2-3 months."
        ),
    },
    "capterra": {
        "PPC Lead Generation": (
            "Bid on positions on category pages and pay per click when buyers visit your "
            "profile. This pay-as-you-go model is more accessible than G2's annual contracts, "
            "which start around $15K/year. CPCs range from $2-$5 in niche verticals to $5-$15 "
            "in competitive categories like CRM or project management. Most B2B software "
            "companies spend $2,000-$10,000/month. The top results on category pages are paid "
            "placements, not the highest-rated products."
        ),
        "Review Collection & Display": (
            "Collect and display verified user reviews on your product profile. Reviews build "
            "credibility with buyers and improve your organic ranking on the platform. Products "
            "with 50+ reviews appear more credible than those with 10. In mainstream B2B "
            "categories like CRM and marketing automation, G2 typically has deeper review "
            "volume, but Capterra leads in niche verticals where G2 has limited coverage. "
            "Reviews syndicate across GetApp and Software Advice automatically."
        ),
        "Broad Category Coverage": (
            "Covers thousands of software categories including niche verticals that G2 does "
            "not reach, making it valuable for vertical and specialized software companies. "
            "Categories like church management, veterinary practice tools, and construction "
            "project management often have stronger buyer traffic on Capterra than G2. For "
            "vendors in these niches, Capterra may be the primary platform where buyers "
            "research options. In mainstream categories, G2 has overtaken Capterra in buyer "
            "influence."
        ),
        "Gartner Digital Markets Distribution": (
            "Vendor profiles and reviews distribute across Capterra, GetApp, and Software "
            "Advice, giving vendors three platforms of buyer exposure from a single listing. "
            "All three are owned by Gartner Digital Markets, and reviews collected on Capterra "
            "appear on the sister sites automatically. GetApp focuses on cloud and SaaS "
            "products, while Software Advice provides more guided buyer matching. The combined "
            "monthly visitor count across all three exceeds what any single site delivers."
        ),
        "Comparison Tools": (
            "Side-by-side product comparison features let buyers evaluate features, pricing, "
            "and reviews across multiple products in a category. Buyers select 2-4 products "
            "and compare review scores, feature checklists, pricing tiers, and user sentiment "
            "in a single view. For vendors, appearing in comparisons increases visibility even "
            "without a top category ranking. Comparison data pulls from vendor profiles and "
            "reviews, so keeping your profile complete improves head-to-head evaluations."
        ),
        "Premium Profiles": (
            "Enhanced vendor profiles with custom content, featured placement, and priority "
            "visibility beyond the standard free listing. Premium profiles let you add custom "
            "screenshots, video demos, whitepapers, and case studies to your product page. "
            "Featured placement puts your listing above organic results on category pages. "
            "The premium tier is separate from PPC spend, so vendors often combine both for "
            "maximum visibility. In competitive categories, premium plus PPC produces the "
            "best conversion rates."
        ),
    },
    "nutshell": {
        "Pipeline Management": (
            "Visual pipeline with drag-and-drop deal tracking, multiple pipeline support on "
            "higher tiers, and customizable stages that map to your sales process without "
            "admin configuration. Reps drag deals between stages as conversations progress, "
            "and managers get a clear view of pipeline health. The Growth plan ($25/user/month) "
            "unlocks multiple pipelines for different products or segments. For straightforward "
            "B2B sales cycles with 4-7 stages, Nutshell is comparable to Pipedrive and "
            "HubSpot."
        ),
        "Built-In Email Marketing": (
            "Send broadcast emails, drip campaigns, and targeted sequences from the CRM using "
            "your contact data, no separate email tool required. Most CRMs in Nutshell's "
            "price range ($13-$79/user/month) require a separate Mailchimp or Constant Contact "
            "subscription. Nutshell bundles this in, saving small teams $30-$100/month and "
            "eliminating sync issues between tools. The email marketing is not as deep as "
            "HubSpot's, but it covers newsletters, drip sequences, and basic segmentation."
        ),
        "Sales Automation": (
            "Automate follow-up reminders, lead assignment, activity logging, and stage-based "
            "actions to keep reps focused on selling. When a deal moves to a new stage, "
            "Nutshell can assign a task, send a notification, or trigger an email. Lead "
            "assignment rules route inbound leads based on territory, round-robin, or custom "
            "criteria. The automation is rule-based and straightforward, which works well for "
            "small teams. It does not offer the branching logic or conditional workflows in "
            "Salesforce or HubSpot."
        ),
        "Email Sequences": (
            "Build personal email sequences for outbound prospecting with automatic follow-ups, "
            "open/click tracking, and reply detection that stops the sequence when a prospect "
            "responds. Reps create a 3-5 step sequence, enroll prospects, and Nutshell handles "
            "timing automatically. Reply detection prevents sending follow-ups after someone "
            "already responded. Available on the Growth plan and above. Compared to Outreach "
            "or SalesLoft, the feature set is basic but sufficient for small team outbound."
        ),
        "Reporting & Analytics": (
            "Built-in reports on pipeline value, conversion rates, sales activity, and team "
            "performance with enough depth for small team management. Managers track rep "
            "activity, deal progression through stages, and where deals stall or drop off. "
            "Reports are pre-built templates, not a custom report builder, so you get standard "
            "sales metrics out of the box. For teams of 5-25 reps, this covers weekly pipeline "
            "reviews and monthly performance checks. Teams needing custom dashboards will "
            "outgrow it."
        ),
        "Contact & Company Management": (
            "Unified contact database with company hierarchies, interaction history, email "
            "tracking, and custom fields. Every email, call, meeting, and note is logged on "
            "the contact record, so any rep can pick up where a colleague left off. Company "
            "records link to associated contacts, showing the full organizational picture. "
            "Custom fields let you track industry-specific data points. Solid for small teams, "
            "but it lacks the multi-entity relationship modeling and deduplication of "
            "enterprise CRMs."
        ),
    },
}


def main():
    with open(TOOL_CONTENT_PATH, "r") as f:
        data = json.load(f)

    changes_made = 0
    all_ok = True
    for tool_slug, features_map in EXPANDED.items():
        if tool_slug not in data:
            print(f"WARNING: Tool '{tool_slug}' not found in tool_content.json")
            continue

        tool = data[tool_slug]
        if "key_features" not in tool:
            print(f"WARNING: Tool '{tool_slug}' has no key_features")
            continue

        for feature in tool["key_features"]:
            name = feature.get("name", "")
            if name in features_map:
                old_len = len(feature["description"])
                feature["description"] = features_map[name]
                new_len = len(feature["description"])
                changes_made += 1
                if 350 <= new_len <= 500:
                    status = "OK"
                else:
                    status = "WARNING"
                    all_ok = False
                print(f"  [{status}] {tool_slug} / {name}: {old_len} -> {new_len} chars")

    print(f"\nTotal changes: {changes_made}")
    if all_ok:
        print("All descriptions within 350-500 char target!")
    else:
        print("Some descriptions are outside the 350-500 char target.")

    with open(TOOL_CONTENT_PATH, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print("File written successfully.")


if __name__ == "__main__":
    main()
