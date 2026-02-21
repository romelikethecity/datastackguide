"""
Expand key_features descriptions for batch 2 tools:
definitive-healthcare, marketo, terminus, g2, common-room, tray

Target: 350-500 chars per description (3-5 sentences).
Only modifies key_features[].description for these 6 tools. Nothing else.
"""

import json
import sys

INPUT_FILE = "/Users/rome/Documents/projects/datastackguide/data/tool_content.json"

# New expanded descriptions keyed by tool slug -> feature name -> new description
EXPANDED = {
    "definitive-healthcare": {
        "Healthcare Provider Database": (
            "Covers 9,000+ hospitals, 400,000+ physician groups, and 2.5 million+ individual physicians "
            "with facility demographics, bed counts, organizational hierarchy, and executive contacts. "
            "Sales teams filter by facility size, geography, specialty mix, and payer composition to build "
            "targeted account lists. The depth goes well beyond general-purpose B2B databases like ZoomInfo "
            "for healthcare, though contact freshness (emails, direct dials) lags behind dedicated contact "
            "tools. Data is U.S.-only."
        ),
        "Procedure Volume & Claims Data": (
            "Claims-based insights show procedure volumes by facility and department, letting you target "
            "hospitals that perform 500+ knee replacements per year or run high cardiac catheterization "
            "volumes. Medical device reps use this to prioritize accounts by clinical activity rather than "
            "guessing from facility size alone. Claims data inherently lags by 3-6 months, so numbers "
            "reflect recent historical patterns rather than real-time volumes. No general B2B database "
            "offers this clinical specificity."
        ),
        "Health IT Installation Data": (
            "Shows which EHR, imaging, lab, pharmacy, and other health IT systems are installed at each "
            "facility, including vendor names and deployment details. Health IT sales teams use this to "
            "identify hospitals running legacy or competitor systems ripe for displacement. Complementary "
            "sellers use it to confirm compatibility before outreach. Coverage is strongest for major "
            "systems at larger facilities and thins out for smaller clinics and niche categories."
        ),
        "Referral Network Analysis": (
            "Maps physician referral patterns derived from insurance claims, showing which PCPs refer to "
            "which specialists and facilities. Pharma field teams use this to identify key opinion leaders "
            "and referral hubs that influence patient flow across a region. Medical device reps can trace "
            "how surgical cases move from diagnosis through referral to procedure. The referral data runs "
            "on the same 3-6 month claims lag as procedure volumes."
        ),
        "CRM Integration": (
            "Salesforce and HubSpot integrations sync healthcare intelligence into your CRM, enriching "
            "account records with facility data, procedure volumes, technology installations, and executive "
            "contacts. Sales reps view Definitive Healthcare data alongside pipeline data without switching "
            "platforms. The integration supports field mapping and automated enrichment workflows. Most "
            "enterprise customers run the Salesforce integration; HubSpot works but sees less adoption."
        ),
        "Market Analytics": (
            "Dashboards and reports for analyzing market share, competitive positioning, geographic coverage, "
            "and procedure volume trends across healthcare markets and service lines. Strategy teams use "
            "this to assess total addressable market, identify underserved territories, and track how "
            "surgical volumes shift between competing facilities. The analytics layer sits on the same "
            "claims and facility data, so depth depends on which modules your contract includes."
        ),
    },
    "marketo": {
        "Smart Campaigns & Engagement Programs": (
            "Build multi-step nurture programs with conditional branching, behavioral triggers, wait steps, "
            "and dynamic content paths that respond to prospect behavior in real time. A single engagement "
            "program can manage dozens of content streams that fork based on email clicks, page visits, "
            "or form fills. This is where Marketo separates from HubSpot: the campaign logic handles "
            "complexity that simpler platforms force you to work around. Building these programs requires "
            "a dedicated marketing ops person."
        ),
        "Lead Scoring": (
            "Granular scoring models combine demographic attributes (title, company size, industry) with "
            "behavioral signals (page visits, email engagement, content downloads) to produce scores that "
            "feed directly into Salesforce. Teams typically run separate demographic and behavioral score "
            "fields so sales can distinguish a VP who hasn't engaged from a coordinator who is very active. "
            "Scores update in near real-time as prospects interact. Setup takes 2-4 weeks with marketing "
            "ops and sales collaborating."
        ),
        "Salesforce Integration": (
            "Best-in-class bidirectional sync with Salesforce, including field mapping, campaign member sync, "
            "lead routing rules, and activity logging. This is the deepest Salesforce integration of any "
            "marketing automation platform, and a primary reason enterprise teams choose Marketo over HubSpot. "
            "Sync runs on a configurable schedule and handles custom objects for complex data models. "
            "Initial setup typically takes 2-3 weeks during implementation."
        ),
        "Email Marketing & Personalization": (
            "Email builder with dynamic content, A/B testing, send-time optimization, and deliverability "
            "tools. Dynamic content blocks swap text, images, or entire sections based on lead attributes "
            "or segment membership, so one template can serve multiple personas. Engagement programs manage "
            "automated sequences with throttling and frequency caps. The builder's UI is functional but dated "
            "compared to HubSpot. Most teams use Marketo for automation logic and bring in a separate "
            "design tool for templates."
        ),
        "Multi-Touch Attribution": (
            "Revenue attribution reporting tracks which marketing touches influenced pipeline and closed deals "
            "across the full buyer journey. Marketo supports first-touch, last-touch, linear, and custom "
            "attribution models. VPs of Marketing use this to justify budget allocation and identify which "
            "programs produce pipeline versus activity without revenue impact. Advanced attribution requires "
            "the Prime tier ($3,195/mo) or an add-on."
        ),
        "Account-Based Marketing": (
            "ABM features include account scoring, named account targeting, and account-level engagement "
            "tracking layered on top of Marketo's lead-based engine. Teams can run lead-based demand gen "
            "and account-based programs simultaneously, using account scores to align marketing and sales. "
            "The ABM capabilities are functional but not as deep as dedicated platforms like 6sense or "
            "Demandbase. Most teams using Marketo for ABM combine it with a dedicated ABM tool for intent "
            "data and display advertising."
        ),
    },
    "terminus": {
        "Account-Based Display Advertising": (
            "Serves programmatic display ads to named accounts across the web with granular reach and "
            "frequency controls. You define a target account list, set your creative and budget, and "
            "Terminus handles ad delivery to people at those companies. Reporting shows engagement at the "
            "account level rather than just raw impressions. This was Terminus's original strength and "
            "remains its most competitive feature, even post-acquisition. Most customers start here before "
            "expanding into other channels."
        ),
        "Multichannel ABM Orchestration": (
            "Coordinate campaigns across display ads, email, chat, and web personalization from a single "
            "platform so target accounts receive consistent messaging across every touchpoint. In practice, "
            "orchestration quality depends on how many contacts you have at target accounts and how well "
            "content maps to each channel. 6sense and Demandbase offer similar multichannel coordination "
            "with stronger AI-driven timing and sequencing."
        ),
        "Account Engagement Scoring": (
            "Tracks and scores account-level engagement across all Terminus channels, surfacing which target "
            "accounts show increased activity. Marketing uses these scores to identify accounts ready for "
            "sales handoff, while sales uses them to prioritize outbound. Scoring aggregates ad impressions, "
            "email engagement, chat interactions, and web visits into a composite score per account. The "
            "approach is transparent but lacks the predictive modeling that 6sense applies to similar signals."
        ),
        "Chat Playbooks": (
            "Deploy conversational marketing playbooks that trigger personalized chat experiences when "
            "visitors from target accounts land on your website. Playbooks route visitors to the right reps "
            "based on account ownership, segment, or engagement level. This works well for high-value "
            "accounts where you want VIP treatment on site. The chat functionality is competent but less "
            "feature-rich than dedicated platforms like Drift or Qualified, which offer deeper routing "
            "and more sophisticated bot capabilities."
        ),
        "CRM & MAP Integration": (
            "Native integrations with Salesforce, HubSpot, and marketing automation platforms sync account "
            "lists, engagement data, and campaign performance into your existing workflows. Account lists "
            "from your CRM populate Terminus targeting, and engagement data flows back so reps see Terminus "
            "activity alongside CRM records. The Salesforce integration is the most mature. HubSpot "
            "integration works but has fewer configuration options."
        ),
        "Account-Level Analytics": (
            "Reporting dashboards show campaign performance, engagement trends, and pipeline influence at "
            "the account level, connecting marketing activity to revenue outcomes. You can track how ad "
            "spend, email sequences, and chat interactions correlate with deal progression for specific "
            "accounts. Reporting is less granular than 6sense's revenue AI or Demandbase's account journey "
            "mapping, but it covers the fundamentals that most mid-market ABM teams need."
        ),
    },
    "g2": {
        "Buyer Intent Data": (
            "Reveals which companies are visiting your G2 profile, comparing you to competitors, and "
            "researching your product category. These signals are high-quality because someone comparing "
            "vendors on G2 is further along in their buying journey than someone who downloaded a whitepaper. "
            "Sales teams use G2 intent to time outreach to active evaluators. The limitation: intent only "
            "covers activity on G2 itself, not research on TrustRadius, Capterra, or the broader web. "
            "It identifies companies, not individuals."
        ),
        "Review Management": (
            "Tools for soliciting, managing, and responding to customer reviews with workflows that integrate "
            "into your customer success process. Teams typically trigger review requests after onboarding "
            "milestones or QBRs to build a steady stream of fresh reviews. G2 weights recency, so older "
            "reviews count for less than recent ones. In competitive categories like CRM or marketing "
            "automation, you need 50+ reviews to rank well on G2's Grid. In smaller categories, 15-25 "
            "reviews can earn a leadership position."
        ),
        "G2 Badges & Social Proof": (
            "Category-specific badges (Leader, High Performer, Momentum Leader) that serve as recognized "
            "trust signals for your website, sales decks, and marketing content. These badges carry weight "
            "in B2B buying decisions because prospects recognize the G2 brand. Marketing teams embed them "
            "on homepages, in email signatures, and in competitive materials. Eligibility depends on review "
            "volume, ratings, and market presence, so maintaining them requires ongoing review generation. "
            "Available on the free tier."
        ),
        "Competitive Intelligence": (
            "Shows how buyers compare you to competitors, which alternative products they evaluate alongside "
            "yours, and how your ratings stack up across review criteria. Product marketing teams use this "
            "to build battlecards and adjust positioning based on where buyers see strengths and weaknesses. "
            "The data also reveals which competitors appear most often in comparisons, informing sales "
            "enablement priorities. Requires a paid plan and is most useful in categories with high "
            "comparison traffic."
        ),
        "CRM & ABM Integrations": (
            "Push buyer intent signals directly into Salesforce, HubSpot, 6sense, Demandbase, and other "
            "platforms so teams can act on G2 research activity within existing workflows. Integrations "
            "typically create tasks or alerts when target accounts show G2 activity, and some teams feed "
            "G2 intent into 6sense or Demandbase scoring models. Setup is straightforward for major CRMs. "
            "Requires a paid G2 plan, and signal volume depends on how much traffic your category receives."
        ),
        "Content Licensing": (
            "License G2 review content, comparison reports, and category rankings for use in marketing "
            "campaigns, sales collateral, and website pages. This lets you embed specific review quotes, "
            "star ratings, and grid placements as third-party validation without sending prospects to G2 "
            "where they might discover competitors. Content licensing is an add-on cost beyond the base "
            "plan. The most common use is embedding review widgets on product pages and including G2 data "
            "in competitive sales decks."
        ),
    },
    "common-room": {
        "Multi-Channel Signal Aggregation": (
            "Captures engagement signals from Slack, Discord, GitHub, Twitter/X, LinkedIn, product usage "
            "data, and other community channels into a single unified view of prospect activity. For "
            "developer tool companies, GitHub stars, issues, and pull requests feed into the same system "
            "as Slack messages and social mentions. Each signal is timestamped and attributed to a person "
            "and account. The value scales with your community's activity volume. Quiet channels produce "
            "minimal signal."
        ),
        "Identity Resolution": (
            "Connects anonymous community activity to real people and accounts by matching signals across "
            "channels. If someone stars your GitHub repo, asks a question in Slack, and engages on LinkedIn, "
            "Common Room links those actions to a single contact profile with name, title, company, and "
            "engagement history. Resolution accuracy is strongest when users share consistent identities "
            "(same email across platforms) and weaker with fragmented profiles. Firmographic enrichment "
            "is more reliable for known companies."
        ),
        "AI-Powered Signal Scoring": (
            "Scores prospects based on the volume, recency, and type of their community engagement to "
            "prioritize outreach toward the most active individuals. A developer who opens issues, joins "
            "your Slack, and mentions your product on Twitter scores higher than someone who starred a repo "
            "once six months ago. Scoring weights are configurable so teams can emphasize the signals that "
            "matter most for their business. Useful for surfacing the top 5-10% of community members who "
            "warrant direct sales engagement."
        ),
        "CRM & Outreach Integration": (
            "Syncs enriched contact data and engagement signals to Salesforce, HubSpot, Outreach, and other "
            "tools so teams can act on community signals within existing workflows. When Common Room flags "
            "a high-intent prospect, the data flows into your CRM with engagement context, so reps see what "
            "the person did in your community before reaching out. Setup is straightforward for major "
            "platforms. The free tier includes limited integrations, while the Team plan ($500/mo) adds "
            "full CRM sync."
        ),
        "Community Analytics": (
            "Dashboards and reporting on community health, growth trends, top contributors, and engagement "
            "patterns across all connected channels. Community managers track which channels drive the most "
            "engagement and which topics generate discussion. Marketing teams correlate community activity "
            "with pipeline creation. The analytics are most useful with 3-6 months of historical data to "
            "establish baselines, so expect a ramp-up period before trend analysis becomes meaningful."
        ),
        "Automated Alerts & Workflows": (
            "Configurable alerts that fire when high-value prospects engage in community channels, with "
            "workflow automation to route signals to the right team members in real time. When a developer "
            "from a target enterprise account opens a GitHub issue, the assigned sales rep gets a Slack "
            "notification with full context. Alerts can be filtered by account tier, engagement score, or "
            "specific actions to avoid noise. This is where Common Room converts passive community "
            "monitoring into active pipeline generation."
        ),
    },
    "tray": {
        "Visual Workflow Builder": (
            "Drag-and-drop interface for building complex automations with branching logic, loops, "
            "conditional paths, error handling, and parallel execution. Unlike Zapier's linear trigger-action "
            "chains, Tray workflows fork into multiple branches, run steps in parallel, and include retry "
            "logic for failed API calls. RevOps teams commonly build lead routing workflows with 20-30 "
            "steps and multiple decision points. The builder takes weeks to master, and complex workflows "
            "can be difficult to debug."
        ),
        "Enterprise-Grade Throughput": (
            "Designed for high-volume automation with millions of operations per month, handling scale that "
            "causes Zapier to hit both performance ceilings and pricing cliffs. Companies running thousands "
            "of daily lead enrichment jobs, CRM sync operations, or data transformation tasks need this "
            "headroom. Tray processes workflows asynchronously, so large batch operations don't block other "
            "running workflows. For teams processing fewer than a few hundred operations per day, this "
            "capacity is unnecessary."
        ),
        "Universal HTTP Connector": (
            "Connect to any REST API without a native connector, making it possible to integrate custom "
            "internal tools, niche SaaS applications, or new products before Tray builds a dedicated "
            "connector. You configure the HTTP method, headers, authentication, and payload mapping within "
            "the visual builder. Essential for RevOps teams integrating homegrown systems. The connector "
            "handles OAuth, API keys, and bearer tokens. Building against a raw API requires comfort with "
            "JSON and API documentation."
        ),
        "Environment Management": (
            "Dev/staging/production environment support with version control for workflows, enabling proper "
            "testing and deployment for business-critical automations. Teams test workflow changes against "
            "sandbox CRM instances before promoting to production, reducing the risk of breaking live "
            "processes. Version history lets you roll back if a deployment causes issues. This is a major "
            "differentiator from Zapier and Make, where workflows are either live or off with no formal "
            "staging capability."
        ),
        "Shared Workspaces": (
            "Team collaboration features including shared workflows, role-based access controls, and "
            "governance for managing automations across multiple team members. RevOps teams with 3-5 "
            "members building workflows need visibility into what exists and who owns what. Access controls "
            "prevent junior team members from modifying production workflows. Workspaces also enable "
            "workflow reuse, so a lead enrichment step built once can be referenced across multiple "
            "workflows as automation scales."
        ),
        "Merlin AI": (
            "AI-assisted workflow generation that converts natural language descriptions into starting "
            "workflow templates. Useful for accelerating builds when you describe a task like enriching "
            "new HubSpot contacts with Clearbit data and routing to Salesforce by company size. Generated "
            "workflows provide a structural starting point but need manual refinement for production use, "
            "especially around error handling and edge cases. Most helpful for experienced users who want "
            "to skip the blank-canvas stage."
        ),
    },
}


def main():
    # Pre-flight: verify all descriptions are in target range
    print("=== Pre-flight character count check ===")
    all_in_range = True
    for slug, features_map in EXPANDED.items():
        for name, desc in features_map.items():
            length = len(desc)
            status = "OK" if 350 <= length <= 500 else f"OUT OF RANGE ({length})"
            if length < 350 or length > 500:
                all_in_range = False
            print(f"  {slug} / {name}: {length} chars [{status}]")

    if not all_in_range:
        print("\nERROR: Some descriptions are outside the 350-500 char range. Fix before applying.")
        sys.exit(1)

    print("\nAll descriptions in range. Proceeding with update.\n")

    # Read the file
    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    # Verify all target tools exist
    for slug in EXPANDED:
        if slug not in data:
            print(f"ERROR: Tool '{slug}' not found in data")
            sys.exit(1)

    # Apply updates
    changes = 0
    for slug, features_map in EXPANDED.items():
        tool = data[slug]
        for feat in tool["key_features"]:
            if feat["name"] in features_map:
                old_len = len(feat["description"])
                feat["description"] = features_map[feat["name"]]
                new_len = len(feat["description"])
                print(f"  {slug} / {feat['name']}: {old_len} -> {new_len} chars")
                changes += 1
            else:
                print(f"  WARNING: Feature '{feat['name']}' in {slug} not in EXPANDED map")

    print(f"\nTotal features updated: {changes}")
    expected = sum(len(v) for v in EXPANDED.values())
    if changes != expected:
        print(f"WARNING: Expected {expected} updates, got {changes}")
        sys.exit(1)

    # Write back
    with open(INPUT_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\nFile written: {INPUT_FILE}")

    # Verify
    print("\n=== Post-write Verification ===")
    with open(INPUT_FILE, "r") as f:
        data2 = json.load(f)

    all_ok = True
    for slug in EXPANDED:
        tool = data2[slug]
        print(f"\n{slug}:")
        for feat in tool["key_features"]:
            length = len(feat["description"])
            status = "OK" if 350 <= length <= 500 else "OUT OF RANGE"
            if status != "OK":
                all_ok = False
            print(f"  {feat['name']}: {length} chars [{status}]")

    if all_ok:
        print("\nAll descriptions within 350-500 char target range.")
    else:
        print("\nWARNING: Some descriptions are outside the target range.")


if __name__ == "__main__":
    main()
