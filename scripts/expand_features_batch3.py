#!/usr/bin/env python3
"""
Batch 3: Expand key_features descriptions for 6 tools to 350-500 chars each.
Tools: celigo, leadfeeder, oracle-cx, mutiny, airbyte, sap-sales-cloud
"""

import json
import sys
import fcntl

FILE_PATH = "/Users/rome/Documents/projects/datastackguide/data/tool_content.json"

# New expanded descriptions keyed by tool_id -> feature index -> new description
UPDATES = {
    "celigo": {
        0: (
            "Fully configured integration packages for Shopify-NetSuite, Amazon-NetSuite, "
            "Salesforce-NetSuite, and other common pairings with pre-mapped data flows, "
            "business logic, and error handling built in. The Shopify-NetSuite app ships "
            "with order sync, inventory updates, customer mapping, and fulfillment tracking "
            "preconfigured. E-commerce ops teams typically go live in days rather than the "
            "weeks required on general-purpose iPaaS platforms like Workato or Tray."
        ),
        1: (
            "Machine learning classifies and suggests resolutions for common integration "
            "errors automatically, reducing manual triage for operations teams managing "
            "high-volume transaction flows. This matters most for e-commerce operations "
            "processing thousands of orders daily, where a single failed sync can cascade "
            "into inventory mismatches. The system learns from past resolutions to improve "
            "over time, cutting the volume of errors requiring human review."
        ),
        2: (
            "Drag-and-drop interface for building custom integrations with data mapping, "
            "transformation steps, error handling, and scheduled syncs between connected "
            "systems. Most operations teams can build basic flows without developer support. "
            "The builder is less sophisticated than Tray or Workato for complex branching "
            "logic and multi-step orchestration. Teams with advanced automation needs may "
            "hit the ceiling, but for standard ERP sync workflows it handles the job well."
        ),
        3: (
            "Deep support for e-commerce workflows including order syncing, inventory "
            "management, fulfillment tracking, and customer data synchronization between "
            "storefronts and ERP systems. Celigo handles nuances that matter in high-volume "
            "commerce: partial shipments, split orders, returns processing, and multi-warehouse "
            "inventory allocation. This is where Celigo pulls ahead of general-purpose iPaaS "
            "tools that treat e-commerce as one use case among many."
        ),
        4: (
            "Built for high-volume transaction processing with retry logic, error queuing, "
            "and data integrity safeguards that ensure financial and order data stays "
            "consistent across systems. When a sync fails mid-batch, Celigo queues the failed "
            "records and retries without re-processing the entire dataset. Critical for ops "
            "teams processing thousands of transactions daily, where a single duplicate can "
            "create accounting discrepancies. Every transaction is logged for audit trails."
        ),
        5: (
            "A library of pre-built integration templates and apps that can be installed and "
            "configured rather than built from scratch, accelerating time to value for common "
            "integration patterns. The marketplace covers ERP, e-commerce, CRM, and logistics "
            "scenarios. Quality varies across contributors, and the catalog is smaller than "
            "Workato or Tray for non-ERP use cases. For NetSuite-centric integrations, the "
            "depth is strong and most templates are battle-tested by the NetSuite community."
        ),
    },
    "leadfeeder": {
        0: (
            "Uses reverse IP lookup to identify which companies are visiting your website, "
            "showing company name, industry, size, location, and visit details including pages "
            "viewed and time on site. Identification works at the company level, not individual "
            "level. Accuracy has declined in the remote work era since VPN and home IP traffic "
            "does not resolve to corporate addresses. Despite this, the signal is directionally "
            "valuable for outbound prioritization."
        ),
        1: (
            "Create filtered views of your visitor data based on company size, industry, "
            "behavior (e.g., visited pricing page), traffic source, or custom criteria to "
            "surface only the most relevant accounts. Sales teams typically set up feeds for "
            "target account lists, enterprise-size visitors, or specific page visits like "
            "pricing and case studies. Filters can be shared across the team so SDRs work "
            "from the same qualified visitor list."
        ),
        2: (
            "Direct integrations with Salesforce, HubSpot, Pipedrive, and other CRMs "
            "automatically sync identified companies and visit data into your sales workflow, "
            "creating leads or updating existing records. When a known account visits your "
            "site, the activity appears on the CRM record without manual entry. Most valuable "
            "for teams running ABM plays, where website visits from target accounts trigger "
            "rep follow-up directly from the CRM."
        ),
        3: (
            "Automated notifications when target companies or companies matching your criteria "
            "visit your website, so reps can follow up while interest is fresh. Alerts can be "
            "delivered via email or Slack and configured per feed, meaning an SDR covering "
            "enterprise accounts only gets pinged for enterprise visitors. For teams with "
            "low-to-moderate traffic, alerts keep the signal visible without requiring reps "
            "to check a dashboard throughout the day."
        ),
        4: (
            "See exactly which pages visitors viewed, how long they spent on each page, how "
            "many visits they made, and how they found your site (organic, paid, referral, "
            "direct). A prospect who read three case studies and visited the pricing page "
            "twice signals higher intent than one who bounced from the homepage. Sales teams "
            "use these patterns to tailor outreach, while marketing uses the data to measure "
            "which content drives engagement from target accounts."
        ),
        5: (
            "As part of the Dealfront platform (formed from the 2022 Leadfeeder-Echobot "
            "merger), access additional B2B company data, European market coverage, and "
            "GDPR-compliant prospecting tools that complement visitor identification. "
            "Particularly relevant for teams selling into European markets where data privacy "
            "regulations are stricter. If you only need visitor tracking, Leadfeeder works "
            "independently, but Dealfront adds prospecting depth that competitors like "
            "Clearbit Reveal offer separately."
        ),
    },
    "oracle-cx": {
        0: (
            "Enterprise sales platform with opportunity management, pipeline forecasting, "
            "territory planning, and mobile access, integrated with Oracle's AI for lead "
            "scoring and next-best-action recommendations. Covers standard B2B sales workflows "
            "competently, with forecasting tools that benefit from Oracle's data cloud "
            "enrichment. The UX trails Salesforce Lightning, and the admin talent pool is "
            "smaller. Makes strategic sense alongside Oracle ERP Cloud, where native data "
            "flow eliminates middleware."
        ),
        1: (
            "One of the strongest B2B marketing automation platforms available, with advanced "
            "campaign orchestration, granular lead scoring, multi-touch attribution, and complex "
            "nurture program capabilities. Eloqua competes directly with Marketo at the "
            "enterprise tier and often wins on multi-step, multi-channel campaign logic. It "
            "handles complex segmentation rules, dynamic content, and third-party data provider "
            "integration at a level that mid-market tools like HubSpot and Pardot cannot match."
        ),
        2: (
            "AI-powered sales and marketing intelligence including lead scoring, engagement "
            "predictions, recommended actions, and content optimization, powered by Oracle's "
            "data cloud and machine learning models. Lead scoring draws on third-party "
            "enrichment signals from Oracle's BlueKai data marketplace, adding behavioral and "
            "intent data beyond what your CRM captures natively. These capabilities are "
            "competent but still maturing compared to Salesforce Einstein."
        ),
        3: (
            "Seamless integration with Oracle ERP Cloud, Oracle Database, and Oracle Cloud "
            "Infrastructure for unified customer, financial, and operational data without "
            "middleware. Sales reps see real-time order status, inventory levels, and billing "
            "history in the CRM. Finance teams get a clean data path from opportunity to "
            "revenue recognition. Competitors like Salesforce require middleware platforms "
            "(MuleSoft, Dell Boomi) for the same connectivity, adding cost and latency."
        ),
        4: (
            "Customer service platform with case management, knowledge base, digital assistant, "
            "and cross-channel support built on the RightNow Technologies acquisition. Handles "
            "email, chat, phone, and social media interactions from a unified agent workspace. "
            "Functional for enterprise service operations in regulated industries where Oracle's "
            "compliance certifications matter. The feature set is narrower than Salesforce "
            "Service Cloud or Zendesk, but avoids the cost of integrating a separate vendor."
        ),
        5: (
            "Oracle Unity CDP aggregates customer data from sales, marketing, service, and "
            "commerce into a single profile, enabling personalized engagement across all "
            "touchpoints. The CDP stitches together identities from online, offline, and "
            "third-party sources. For enterprises with fragmented customer data across dozens "
            "of systems, Unity provides a centralized view powering segmentation and analytics. "
            "Competes with Segment and Salesforce CDP, with its edge being native Oracle "
            "connectivity."
        ),
    },
    "mutiny": {
        0: (
            "A point-and-click editor that lets marketers modify headlines, CTAs, images, "
            "testimonials, and any page element for specific audience segments without "
            "touching code. The editor overlays on your live site so you see exactly what "
            "each segment will experience. Marketing teams typically create 5-15 personalized "
            "variants per page targeting industries, company sizes, or ABM tiers. The no-code "
            "approach removes the engineering bottleneck that historically made website "
            "personalization impractical."
        ),
        1: (
            "Analyzes your traffic, conversion data, and visitor segments to recommend which "
            "audiences to personalize for and what changes are likely to drive the highest "
            "conversion lift. Particularly useful for teams starting their personalization "
            "program, where the question is not whether to personalize but where to begin. "
            "Mutiny's AI surfaces segments with enough traffic and conversion variance for "
            "statistically significant results. You need 10K+ monthly visitors before the "
            "suggestions become reliable."
        ),
        2: (
            "Define visitor segments based on company, industry, size, ABM list membership, "
            "firmographic data, or behavior. Integrations with 6sense, Demandbase, and "
            "Clearbit provide the visitor identification layer. You can target a named account "
            "list from Salesforce, visitors from 500+ employee companies in healthcare, or "
            "return visitors who viewed your pricing page twice. Segments update in real time "
            "as data flows from connected platforms."
        ),
        3: (
            "Test personalized experiences against your generic page to measure conversion "
            "lift with statistical significance. Each experience runs as a controlled "
            "experiment, with traffic split between personalized and default versions. Mutiny "
            "reports conversion rates, pipeline generated, and revenue influenced per variant. "
            "The testing framework is essential for justifying the platform's $10K-$50K annual "
            "cost, turning personalization from a gut-feel exercise into a measurable investment."
        ),
        4: (
            "Native integrations with 6sense, Demandbase, Clearbit, and Salesforce provide "
            "the visitor identification and account data needed to serve personalized "
            "experiences to the right segments. Mutiny uses reverse IP lookup as a baseline, "
            "then enriches with data from your connected ABM platform. If you run 6sense or "
            "Demandbase, Mutiny inherits your existing account scoring and intent data. Teams "
            "without an ABM platform can still use Mutiny, but precision drops with "
            "IP-only identification."
        ),
        5: (
            "Track how personalized experiences perform versus generic pages across segments, "
            "measuring conversion rates, pipeline generated, and revenue influenced. The "
            "dashboard breaks down performance by segment, page, and variant so you can "
            "identify which personalizations drive results and which fall flat. Mutiny "
            "connects to Salesforce to tie conversions to downstream pipeline. This closed-loop "
            "reporting is critical for B2B marketers proving personalization investments "
            "translate to pipeline dollars."
        ),
    },
    "airbyte": {
        0: (
            "One of the largest connector catalogs in the ELT space, covering databases, SaaS "
            "APIs, file systems, and more. Community contributions through the Connector "
            "Development Kit (CDK) keep the library growing faster than closed-source "
            "competitors. Connector quality varies: Airbyte-maintained connectors (Postgres, "
            "Snowflake, Stripe, HubSpot) are production-grade, while some community-built "
            "connectors may need testing before you depend on them for critical pipelines."
        ),
        1: (
            "Run the full platform on Docker or Kubernetes at zero cost with no artificial "
            "limits on connectors, rows, users, or sync frequency. The entire codebase is "
            "open-source and inspectable. For startups and budget-conscious data teams, this "
            "is the strongest differentiator against Fivetran, where costs scale with data "
            "volume and can reach five figures monthly. The trade-off is operational: you "
            "manage infrastructure, monitor sync health, and handle upgrades yourself."
        ),
        2: (
            "Real-time database replication using CDC for PostgreSQL, MySQL, MongoDB, and "
            "other supported databases, capturing inserts, updates, and deletes without full "
            "table scans. CDC reads the database transaction log directly, meaning minimal "
            "performance impact on production compared to query-based extraction. Essential "
            "for analytics teams needing near-real-time warehouse data. Setup requires "
            "enabling logical replication on the source, which may need DBA involvement."
        ),
        3: (
            "Build custom connectors in Python using the CDK when a source or destination "
            "is not in the catalog. Most API-based connectors can be built in a day or two "
            "and contributed back to the community. The CDK handles pagination, authentication, "
            "rate limiting, schema inference, and incremental sync state so you focus on "
            "API-specific logic. A significant advantage over Fivetran, where custom connectors "
            "require the partner program or the more constrained Functions feature."
        ),
        4: (
            "Automatically detects source schemas, propagates schema changes to destinations, "
            "and sends notifications when schemas change so you can handle breaking changes "
            "proactively. Schema drift is one of the biggest operational headaches in data "
            "pipelines, where a source API adds a field and downstream transformations break "
            "silently. Airbyte's detection catches changes at the extraction layer and lets "
            "you decide whether to auto-propagate or review manually."
        ),
        5: (
            "Managed cloud version for teams that want Airbyte's connector breadth without "
            "infrastructure overhead. Credit-based pricing with monitoring, auto-scaling, and "
            "support included. Eliminates the Kubernetes burden while keeping access to the "
            "full connector catalog. Pricing starts at $2.50 per credit, consumed based on "
            "data volume. At high volumes, costs can approach Fivetran's, narrowing the cost "
            "advantage. Best for mid-volume teams wanting connector flexibility with managed "
            "reliability."
        ),
    },
    "sap-sales-cloud": {
        0: (
            "Real-time bidirectional integration with SAP S/4HANA and ECC gives sales teams "
            "instant access to inventory levels, pricing, order status, and financial data "
            "without middleware. This is the core reason enterprises choose SAP Sales Cloud "
            "over Salesforce. A rep can check inventory and confirm delivery timelines during "
            "a customer call without switching systems. Equivalent Salesforce-SAP connectivity "
            "requires middleware like MuleSoft, adding significant cost and implementation time."
        ),
        1: (
            "Complex pricing and quoting capabilities that handle multi-tier pricing, volume "
            "discounts, approval chains, and product configuration rules for B2B manufacturing "
            "and industrial sales. SAP CPQ models pricing logic involving hundreds of variables: "
            "regional pricing, contract discounts, material costs, and custom configurations. "
            "For companies where a single quote contains 500 line items across product families, "
            "this depth matters. Salesforce CPQ competes but lacks native SAP pricing data."
        ),
        2: (
            "Territory and quota management that handles complex organizational structures "
            "across geographies, business units, and product lines with multi-currency and "
            "multi-language support built in. SAP Sales Cloud supports overlapping territories, "
            "team selling models, and quota rollups across multiple dimensions simultaneously. "
            "A company operating in 30 countries with regional, product, and vertical sales "
            "teams can model all three structures without workarounds or custom development."
        ),
        3: (
            "SAP Joule AI integration provides sales recommendations, deal scoring, and "
            "intelligent insights, though these capabilities are still maturing compared to "
            "Salesforce Einstein. Joule surfaces next-best-action suggestions, flags at-risk "
            "deals, and provides conversation intelligence. SAP is investing heavily in Joule "
            "across its product suite, with capabilities expanding each quarter. Einstein "
            "offers more proven AI features today, but the gap should narrow over the next "
            "12-18 months."
        ),
        4: (
            "CRM pipeline management with deal tracking, forecasting, and activity management, "
            "adapted for complex B2B sales cycles with long timelines and multiple "
            "decision-makers. Supports weighted pipeline stages, multi-stakeholder buying "
            "groups, and forecast categories aligned with revenue recognition. Integration "
            "with SAP ERP means pipeline connects to financial planning, so sales forecasts "
            "feed supply chain and production planning. This closed-loop visibility is hard "
            "to replicate with standalone CRMs."
        ),
        5: (
            "Part of the broader SAP Customer Experience suite, connecting CRM with commerce, "
            "marketing, and service for a unified customer view across the SAP ecosystem. "
            "The CX suite includes SAP Commerce Cloud (hybris), SAP Emarsys for marketing "
            "automation, and SAP Service Cloud. For enterprises committed to SAP, the full "
            "CX suite avoids vendor fragmentation and integration overhead from mixing "
            "Salesforce with Shopify, Marketo, and Zendesk. The trade-off is less flexibility "
            "and a smaller partner ecosystem."
        ),
    },
}


def main():
    # Read the file with a lock to avoid conflicts
    with open(FILE_PATH, "r") as f:
        fcntl.flock(f, fcntl.LOCK_SH)
        data = json.load(f)
        fcntl.flock(f, fcntl.LOCK_UN)

    # Apply updates
    for tool_id, features in UPDATES.items():
        if tool_id not in data:
            print(f"ERROR: Tool '{tool_id}' not found in JSON!")
            sys.exit(1)

        tool = data[tool_id]
        if "key_features" not in tool:
            print(f"ERROR: Tool '{tool_id}' has no key_features!")
            sys.exit(1)

        for idx, new_desc in features.items():
            if idx >= len(tool["key_features"]):
                print(f"ERROR: Tool '{tool_id}' feature index {idx} out of range!")
                sys.exit(1)

            old_desc = tool["key_features"][idx]["description"]
            tool["key_features"][idx]["description"] = new_desc
            feature_name = tool["key_features"][idx]["name"]
            print(f"  {tool_id}[{idx}] {feature_name}: {len(old_desc)} -> {len(new_desc)} chars")

    # Write back with exclusive lock
    with open(FILE_PATH, "w") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        json.dump(data, f, indent=2)
        f.write("\n")
        fcntl.flock(f, fcntl.LOCK_UN)

    print("\nDone! File updated successfully.")


if __name__ == "__main__":
    main()
