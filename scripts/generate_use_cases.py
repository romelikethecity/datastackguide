#!/usr/bin/env python3
"""
Generate new use case pages for underserved categories and personas.
"""
import json
import sys
from datetime import date

DATA = "/Users/rome/Documents/projects/datastackguide/data"
TODAY = date.today().isoformat()


def load(name):
    with open(f"{DATA}/{name}") as f:
        return json.load(f)


def save(name, data):
    with open(f"{DATA}/{name}", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_tool_meta(slug, tc, tools_meta):
    """Get display name and job count for a tool."""
    name = tc.get(slug, {}).get('display_name', slug)
    jobs = tools_meta.get(slug, {}).get('job_count', 0)
    return name, jobs


# New use case definitions
NEW_USE_CASES = [
    {
        "slug": "crm-for-enterprise",
        "title": "Enterprise CRM Selection: Salesforce, Dynamics 365 & Alternatives (2026)",
        "meta_description": "How to choose an enterprise CRM. Salesforce vs Dynamics 365 vs Oracle CX compared on customization, total cost, and integration depth.",
        "persona": "VP Sales, CRO, and IT leaders at companies with 200+ sales reps",
        "category_slug": "crm",
        "intro": "Enterprise CRM selection is a 3-5 year commitment that affects every revenue team. The wrong choice costs six figures in migration and retraining. At this scale, you're not evaluating features. You're evaluating ecosystems, admin talent availability, and how deeply the platform integrates with your ERP, marketing automation, and data warehouse.",
        "what_to_look_for": [
            {"criteria": "Customization depth",
             "why": "Enterprise sales processes are rarely standard. You need custom objects, complex approval workflows, territory management, and multi-currency support. Evaluate how much customization requires code vs. configuration."},
            {"criteria": "Admin talent availability",
             "why": "Your CRM is only as good as the team maintaining it. Check job posting volume for platform-specific admins. Salesforce admins are abundant; Oracle CX and SAP admins are harder to find and more expensive."},
            {"criteria": "Integration ecosystem",
             "why": "Enterprise stacks have 50-200 connected tools. Native integrations matter less than API maturity, middleware compatibility (Workato, MuleSoft), and iPaaS connector availability."},
            {"criteria": "Total cost of ownership",
             "why": "License cost is 30-40% of the real number. Add implementation consulting, admin salaries, app marketplace subscriptions, and ongoing customization. Get a 3-year TCO estimate before signing."},
        ],
        "recommended_tools": [
            {"slug": "salesforce", "why": "The default enterprise choice for a reason. 1,694 job postings in our dataset. Unmatched app ecosystem (5,000+ integrations), deepest customization, and the largest talent pool. Plan for $150K-250K/year all-in for a 50-person sales org."},
            {"slug": "dynamics-365", "why": "The strongest alternative for Microsoft-native organizations. Tight integration with Teams, Outlook, Power BI, and Azure. Lower admin talent pool than Salesforce, but growing. Best when your company already runs Microsoft 365 and Azure."},
            {"slug": "oracle-cx", "why": "Built for complex B2B and B2C sales cycles. Strong CPQ and subscription billing. Best fit for companies already on Oracle ERP or NetSuite. Smaller ecosystem and harder-to-find admins limit its appeal outside Oracle shops."},
            {"slug": "sap-sales-cloud", "why": "The CRM for SAP-dependent enterprises. Real-time ERP integration gives sales reps visibility into inventory, pricing, and order status. Not competitive on UX or ecosystem breadth, but unbeatable for SAP S/4HANA environments."},
        ],
        "bottom_line": "Salesforce wins on ecosystem and talent availability. Dynamics 365 wins on Microsoft integration. Oracle CX and SAP Sales Cloud only make sense if you're already deep in those vendor ecosystems. The biggest mistake is underestimating total cost of ownership. Budget 2-3x the license cost for the real number.",
        "faq": [
            {"q": "How much does an enterprise CRM cost per year?",
             "a": "For a 50-person sales org: Salesforce runs $150K-250K all-in (licenses, admin, integrations). Dynamics 365 is typically 20-30% less. Oracle CX and SAP Sales Cloud vary widely based on existing vendor relationships but expect $100K-300K."},
            {"q": "How long does enterprise CRM implementation take?",
             "a": "6-12 months for a full deployment. Plan 3-4 months for basic setup, 2-3 months for data migration, and 2-3 months for training and workflow optimization. Rushing implementation is the most common and most expensive mistake."},
            {"q": "Can I switch enterprise CRMs without losing data?",
             "a": "Yes, but plan for 3-6 months of parallel operation. Data migration is the easy part. The hard part is retraining users, rebuilding automations, and re-integrating connected tools. Budget $50K-150K for migration consulting."},
        ],
    },
    {
        "slug": "crm-for-startups",
        "title": "Best CRM for Startups: What to Pick Before You Scale (2026)",
        "meta_description": "CRM options for startups and SMBs under 50 reps. HubSpot, Pipedrive, Copper, and Freshsales compared on price, simplicity, and growth potential.",
        "persona": "Founders, first sales hires, and early-stage sales leaders",
        "category_slug": "crm",
        "intro": "Most startups don't need a CRM. They need pipeline visibility and a way to stop losing deals in email threads. The right CRM at this stage is the one your team will use without training. Pick based on adoption ease, not feature lists. You can always migrate later when your process justifies complexity.",
        "what_to_look_for": [
            {"criteria": "Time to value",
             "why": "If setup takes more than a day, reps won't use it. Look for guided onboarding, email integration that works immediately, and pipeline views that make sense without configuration."},
            {"criteria": "Price at your scale",
             "why": "Free tiers matter when you have 5 reps. But check what happens at 20 and 50 reps. Some CRMs (HubSpot) get expensive fast. Others (Pipedrive) scale linearly. Model your 2-year cost, not just the entry price."},
            {"criteria": "Built-in outreach",
             "why": "Startups can't afford separate CRM + sales engagement + enrichment tools. CRMs with built-in email sequences and basic prospecting (HubSpot, Freshsales) eliminate one or two additional vendors."},
            {"criteria": "Migration path",
             "why": "You will outgrow your first CRM. Pick one with clean data export and Salesforce migration tooling. Avoid platforms that lock your data into proprietary formats."},
        ],
        "recommended_tools": [
            {"slug": "hubspot", "why": "Free CRM tier is the most generous in the market. 432 job postings. Built-in email tracking, meeting scheduling, and basic sequences. The catch: once you need marketing automation (Marketing Hub Pro at $800/month), costs escalate fast."},
            {"slug": "pipedrive", "why": "The simplest pipeline CRM. Visual Kanban board that salespeople adopt without training. Starts at $14/user/month. Best for teams that want deal tracking without the complexity of a full platform."},
            {"slug": "freshsales", "why": "Full CRM with built-in phone, email, and chat. AI-powered lead scoring at lower tiers. Part of the Freshworks suite if you also need support and marketing tools. Good balance of features and simplicity."},
            {"slug": "copper", "why": "Built for Google Workspace teams. Lives inside Gmail, so reps never leave their inbox. Best for teams already committed to Google. Limited if you need deep customization or non-Google integrations."},
        ],
        "bottom_line": "Start with HubSpot's free tier if you want room to grow into marketing automation. Start with Pipedrive if you want the simplest possible pipeline view. Switch to Salesforce when you have 50+ reps and a dedicated admin. The worst choice is picking a complex CRM your team won't use.",
        "faq": [
            {"q": "When should a startup switch from spreadsheets to a CRM?",
             "a": "When you have more than 2 salespeople or more than 50 active deals. Before that, spreadsheets work fine. The trigger is usually losing track of follow-ups or lacking visibility into team pipeline."},
            {"q": "Is HubSpot's free CRM actually free?",
             "a": "Yes, for core CRM features (contact management, pipeline, email tracking, meetings). No user limit. The paid tiers ($45-$1,200/month per seat) add sequences, custom reports, and automation. Most startups outgrow the free tier within 12-18 months."},
            {"q": "Should a startup just start with Salesforce?",
             "a": "Not unless you have a dedicated admin and $50K+ annual budget for the platform. Salesforce is over-built for teams under 20 reps. You'll spend more time configuring than selling. Start simpler and migrate when complexity justifies it."},
        ],
    },
    {
        "slug": "ipaas-for-revops",
        "title": "Integration Platforms for RevOps: Connect Your GTM Stack (2026)",
        "meta_description": "How RevOps teams should evaluate iPaaS tools. Workato, Zapier, Make, and Tray compared for CRM sync, data pipelines, and workflow automation.",
        "persona": "RevOps managers and sales ops teams managing 10+ connected tools",
        "category_slug": "orchestration",
        "intro": "RevOps teams spend 30-40% of their time on data flow problems. Leads stuck between systems, duplicate records, broken automations, missing attribution data. An integration platform solves these at the infrastructure level instead of building one-off fixes in each tool. The question isn't whether you need one. It's which tier of complexity your stack requires.",
        "what_to_look_for": [
            {"criteria": "CRM connector depth",
             "why": "A basic Salesforce connector syncs contacts. A good one handles custom objects, formula fields, real-time triggers, and bulk operations. Test with your actual CRM configuration, not the demo instance."},
            {"criteria": "Error handling and monitoring",
             "why": "Integration failures are silent killers. Your platform needs retry logic, error alerts, and audit logs that non-engineers can read. When a sync breaks at 2 AM, you need to know before sales notices."},
            {"criteria": "Pricing model clarity",
             "why": "iPaaS pricing is notoriously confusing. Some charge per task (Zapier), per connector (Workato), or per operation (Make). Model your actual volume. A workflow that runs 10,000 times per month costs very different amounts across platforms."},
            {"criteria": "Self-service vs. IT dependency",
             "why": "Can your ops team build and maintain integrations without engineering? Zapier and Make are built for this. Workato and Tray lean toward technical users. MuleSoft requires developers. Match the tool to who will own it."},
        ],
        "recommended_tools": [
            {"slug": "zapier", "why": "The most accessible integration platform. 7,000+ app connectors, no-code builder, and the largest community. Best for simple point-to-point automations. Struggles with complex multi-step logic and high-volume data sync."},
            {"slug": "make", "why": "More powerful than Zapier at a lower price point. Visual workflow builder handles branching logic, loops, and error paths that Zapier can't. Steeper learning curve, but dramatically more flexible for complex RevOps workflows."},
            {"slug": "workato-ipaas", "why": "Enterprise-grade iPaaS with strong CRM connectors. Recipes handle complex business logic including conditional routing, data transformation, and multi-system orchestration. Higher price point justified for teams with 20+ integrations."},
            {"slug": "tray", "why": "Balances enterprise capability with visual building. Strong for marketing ops workflows and complex data routing. Less community content than Zapier or Make, so expect more reliance on documentation and support."},
        ],
        "bottom_line": "Start with Zapier for your first 5-10 integrations. Move to Make when you hit Zapier's logic limitations or cost ceiling. Move to Workato or Tray when you need enterprise governance, compliance, and 20+ connected systems. The migration gets harder the longer you wait, so choose a platform you can grow into.",
        "faq": [
            {"q": "How much does an iPaaS cost for a RevOps team?",
             "a": "Zapier: $69-599/month depending on volume. Make: $9-299/month for much higher limits. Workato: $10K-50K/year for enterprise. Tray: similar to Workato. Your cost depends on how many automations you run and how frequently they execute."},
            {"q": "Can I replace my iPaaS with native CRM integrations?",
             "a": "For 1-2 simple integrations, yes. For anything involving conditional logic, data transformation, or 5+ connected tools, a dedicated iPaaS saves 10-20 hours per month of manual work and maintenance."},
            {"q": "Do I need engineering help to set up an iPaaS?",
             "a": "Not for Zapier or Make. Most RevOps teams can build workflows independently. Workato, Tray, and MuleSoft benefit from technical support during initial setup, but ops teams can maintain them afterward."},
        ],
    },
    {
        "slug": "technographic-data-for-sales",
        "title": "Using Technographic Data to Target Better Accounts (2026)",
        "meta_description": "How sales teams use technographic data to find accounts running specific software. Tools, signals, and targeting strategies compared.",
        "persona": "Sales leaders and SDR managers targeting technology buyers",
        "category_slug": "technographic",
        "intro": "Technographic data tells you what software a company uses before you call them. It turns cold outreach into informed conversations. If you sell to companies running Salesforce, knowing which prospects use Salesforce (and which complementary tools they're missing) lets you personalize at scale. The data quality varies dramatically by provider, and freshness matters more than database size.",
        "what_to_look_for": [
            {"criteria": "Detection methodology",
             "why": "Some providers scan websites for JavaScript tags (fast but shallow). Others crawl job postings, analyze DNS records, or use receipt data. Each method catches different tools. No single source sees everything."},
            {"criteria": "Coverage by segment",
             "why": "Enterprise tech stacks are well-documented. SMB tech stacks are harder to detect. If you sell to mid-market, verify coverage specifically for your target company size. Ask for match rates on your existing account list."},
            {"criteria": "Freshness and update frequency",
             "why": "Companies change tools. A technographic record from 6 months ago is unreliable for fast-moving categories (marketing automation, sales engagement). Weekly or monthly refresh rates matter more for these segments."},
            {"criteria": "Integration with your outreach stack",
             "why": "Technographic data is useless if it sits in a separate portal. The best providers push signals into your CRM, enrich records in your sales engagement platform, and trigger alerts when target accounts adopt or drop specific tools."},
        ],
        "recommended_tools": [
            {"slug": "zoominfo", "why": "The broadest technographic coverage with 300M+ company profiles. Detects tech installs through web scanning, job postings, and partnership data. Strongest for US enterprise and mid-market. Intent data layer adds behavioral signals on top of install base data."},
            {"slug": "6sense", "why": "Combines technographic data with intent signals for ABM targeting. Identifies accounts researching specific technologies, not just those already using them. Best for teams running account-based marketing programs alongside sales."},
            {"slug": "clearbit", "why": "Real-time technographic enrichment that integrates cleanly with CRMs and marketing platforms. Detects 100+ technology categories. Free tier available for low-volume use. Strongest for enrichment workflows, not standalone prospecting."},
            {"slug": "demandbase", "why": "Enterprise ABM platform with technographic data layered into account intelligence. Best for companies with 1,000+ target accounts that need advertising, web personalization, and sales intelligence in one platform."},
        ],
        "bottom_line": "For standalone technographic data, ZoomInfo has the broadest coverage. For combining technographics with intent data and ABM workflows, 6sense and Demandbase are stronger. Clearbit wins for real-time enrichment in existing workflows. Whatever you choose, validate coverage against your actual target account list before committing.",
        "faq": [
            {"q": "How accurate is technographic data?",
             "a": "For well-known enterprise tools (Salesforce, HubSpot, Marketo), accuracy is 70-85%. For niche or self-hosted tools, accuracy drops to 40-60%. Always validate a sample against your known accounts before relying on it for targeting."},
            {"q": "What's the difference between technographic and intent data?",
             "a": "Technographic data tells you what tools a company currently uses. Intent data tells you what topics they're researching. Technographic is static (what they have). Intent is dynamic (what they're interested in buying). The best targeting combines both."},
            {"q": "Can I get technographic data for free?",
             "a": "Clearbit offers a free enrichment tier. BuiltWith has free website lookups. Wappalyzer has a free browser extension. For bulk data at scale, expect to pay $10K-50K/year depending on the provider and volume."},
        ],
    },
    {
        "slug": "contact-databases-for-outbound",
        "title": "Contact Databases for Outbound Sales Teams (2026)",
        "meta_description": "How to choose a B2B contact database for outbound prospecting. ZoomInfo, Apollo, Cognism, and others compared on accuracy, coverage, and price.",
        "persona": "SDR managers and outbound sales leaders building prospecting workflows",
        "category_slug": "contact-databases",
        "intro": "Every outbound team needs a contact database. The market has consolidated around a few major players, but they differ significantly on pricing, accuracy, and coverage by geography. The cheapest option isn't always the worst, and the most expensive isn't always the best. What matters is accuracy for your specific target market and whether the platform fits your outreach workflow.",
        "what_to_look_for": [
            {"criteria": "Email accuracy rate",
             "why": "Bounce rates above 5% damage sender reputation and tank deliverability. Ask for email verification rates, not just database size. A 200M contact database with 70% accuracy gives you more bounces than a 50M database with 95% accuracy."},
            {"criteria": "Direct dial coverage",
             "why": "If your outbound motion relies on cold calling, direct dial quality matters more than email. Coverage varies dramatically: 30-50% for US mid-market, 10-20% for international. Test before you commit."},
            {"criteria": "Built-in outreach vs. data-only",
             "why": "Some platforms (Apollo, Instantly) include email sequencing. Others (ZoomInfo, Cognism) are data-only and require a separate SEP. Bundled platforms save money. Standalone data providers offer more flexibility."},
            {"criteria": "Credit system and true cost per contact",
             "why": "Most databases use credits. Calculate your cost per usable contact, not cost per credit. If 30% of contacts bounce or are irrelevant, your effective cost is 1.4x the nominal rate."},
        ],
        "recommended_tools": [
            {"slug": "zoominfo", "why": "The largest B2B database. 260M+ professional profiles, 100M+ company profiles. Strongest accuracy for US enterprise contacts. Starts at $15K/year with annual contracts. The benchmark that every competitor prices against."},
            {"slug": "apollo", "why": "Best value for growth teams. 275M+ contacts with built-in email sequencing. Free tier with 250 emails/day. Paid plans start at $49/user/month. Email accuracy runs 80-85%, lower than ZoomInfo but at a fraction of the cost."},
            {"slug": "cognism", "why": "Strongest option for European and international outreach. Phone-verified Diamond Data for EMEA contacts. GDPR-compliant by design. Weaker US coverage than ZoomInfo, but the best international direct dial accuracy in the market."},
            {"slug": "seamless-ai", "why": "Real-time verified contact data with aggressive pricing. Searches and verifies contacts on demand rather than serving from a static database. Good accuracy for recently verified records. Higher bounce rates for older contacts."},
            {"slug": "linkedin-sales-navigator", "why": "Not a traditional contact database, but the most accurate source of current job titles and company associations. Use it for research and signal monitoring, then pull contact details from a data provider."},
        ],
        "bottom_line": "ZoomInfo for US enterprise with budget. Apollo for growth teams that want data plus outreach in one platform. Cognism for international and EMEA-focused teams. Test each provider against your actual ICP before signing an annual contract. Ask for a trial with your target accounts, not their demo data.",
        "faq": [
            {"q": "How much does a B2B contact database cost?",
             "a": "Apollo's free tier works for low-volume teams. Paid options range from $49/user/month (Apollo Basic) to $15K-50K/year (ZoomInfo). Cognism and Seamless AI fall in between. Your cost depends on how many contacts you need and whether you need phone-verified data."},
            {"q": "Which contact database has the best accuracy?",
             "a": "For US enterprise: ZoomInfo (85-90% email accuracy). For EMEA/international: Cognism Diamond Data. For breadth at low cost: Apollo (80-85%). No database is 100% accurate. Budget for email verification as an additional step."},
            {"q": "Should I use one database or multiple?",
             "a": "Start with one. If your outbound targets span US and international markets, consider pairing ZoomInfo (US) with Cognism (EMEA). Clay's waterfall approach queries multiple databases automatically, which works well for teams that need maximum coverage."},
        ],
    },
    {
        "slug": "website-visitor-identification",
        "title": "Website Visitor Identification for B2B Sales Teams (2026)",
        "meta_description": "How to identify anonymous B2B website visitors. Warmly, RB2B, Leadfeeder, and 6sense compared on identification methods, accuracy, and privacy.",
        "persona": "Demand gen managers and sales teams wanting to convert website traffic into pipeline",
        "category_slug": "intent",
        "intro": "97% of B2B website visitors leave without filling out a form. Visitor identification tools match anonymous traffic to companies or individual contacts, giving sales teams warm leads from existing traffic. The methods range from IP-to-company matching (account-level) to person-level identification (using email pixels and tracking), with very different privacy implications for each approach.",
        "what_to_look_for": [
            {"criteria": "Account-level vs. person-level identification",
             "why": "IP matching identifies the company but not the person (useful for ABM). Person-level tools identify individual visitors (more actionable for sales). Person-level tools face more regulatory scrutiny and require explicit consent mechanisms."},
            {"criteria": "Match rate for your traffic",
             "why": "Vendors quote 30-60% match rates, but your actual rate depends on your traffic mix. Enterprise traffic from known IP ranges matches well. Remote workers, mobile visitors, and VPN users don't match at all."},
            {"criteria": "CRM integration depth",
             "why": "Identified visitors need to reach sales reps fast. Look for real-time alerts, automatic CRM record creation, and Slack notifications. A visitor identified 3 days after their visit has already moved on."},
            {"criteria": "Privacy compliance",
             "why": "GDPR, CCPA, and evolving privacy regulations affect which identification methods are legal in your market. Account-level IP matching is generally accepted. Person-level tracking without consent is legally risky in the EU."},
        ],
        "recommended_tools": [
            {"slug": "warmly", "why": "Combines company identification with real-time sales rep alerts and meeting scheduling. Identifies visitors and routes them to available reps for live engagement. Strongest for teams that want to convert high-intent visitors in real time."},
            {"slug": "rb2b", "why": "Person-level visitor identification at an accessible price point. Matches individual contacts, not just companies. Growing fast in the startup and mid-market segment. More aggressive identification approach, so evaluate privacy implications for your market."},
            {"slug": "leadfeeder", "why": "Account-level identification that integrates with Google Analytics. Shows which companies visit, which pages they view, and how often. Conservative identification approach that works cleanly for GDPR-regulated markets."},
            {"slug": "6sense", "why": "Enterprise-grade visitor identification layered into a full ABM platform. Matches visitors to accounts, enriches with intent data, and orchestrates multi-channel engagement. Best for teams already running account-based programs."},
        ],
        "bottom_line": "Warmly for real-time visitor conversion. RB2B for person-level identification at mid-market prices. Leadfeeder for privacy-safe account-level matching. 6sense for enterprise ABM. Start by measuring your baseline match rate with a free trial. If fewer than 10% of your visitors match, the ROI math doesn't work.",
        "faq": [
            {"q": "Is website visitor identification legal?",
             "a": "Account-level identification (IP-to-company matching) is generally accepted under GDPR and CCPA. Person-level identification is more complex and may require consent mechanisms depending on your jurisdiction. Consult your legal team for your specific market."},
            {"q": "What match rate should I expect?",
             "a": "15-40% for account-level identification. 5-15% for person-level identification. Your actual rate depends on traffic composition. Enterprise B2B traffic from office IPs matches better than traffic from remote workers or mobile devices."},
            {"q": "How fast does identified visitor data reach sales?",
             "a": "Real-time with most modern tools. Warmly and RB2B push alerts within seconds. Leadfeeder updates daily. For high-intent pages (pricing, demo request), immediate routing matters. For blog traffic, daily batch processing is fine."},
        ],
    },
    {
        "slug": "ipaas-for-data-teams",
        "title": "Data Pipeline Tools: ELT, Reverse ETL & Warehouse Integration (2026)",
        "meta_description": "How data teams choose between Fivetran, Airbyte, Hightouch, and Census for data pipelines. ELT vs reverse ETL compared for B2B analytics stacks.",
        "persona": "Data engineers and analytics leads building warehouse-first architectures",
        "category_slug": "orchestration",
        "intro": "Modern B2B data teams run on a warehouse-first architecture. Raw data flows into Snowflake, BigQuery, or Redshift via ELT tools, gets modeled with dbt, then flows back out to business tools via reverse ETL. Choosing the right pipeline tools determines whether your data team spends time on analysis or plumbing. The category has matured fast, and pricing models differ enough that the wrong choice costs 2-5x at scale.",
        "what_to_look_for": [
            {"criteria": "Connector coverage for your sources",
             "why": "You need connectors for your CRM, marketing tools, billing system, and product database. Check that connectors support the specific objects and fields you need, not just a generic connection. Many connectors have partial coverage."},
            {"criteria": "ELT vs. reverse ETL (or both)",
             "why": "ELT moves data into your warehouse. Reverse ETL moves it back out to business tools. Some teams need both. Fivetran and Airbyte handle ELT. Hightouch and Census handle reverse ETL. Evaluate whether you need one tool or two."},
            {"criteria": "Pricing at your data volume",
             "why": "Fivetran charges by monthly active rows (MAR). Airbyte charges by rows synced. Census charges by synced records. Model your actual volume across all connectors. A small increase in volume can trigger a large pricing tier jump."},
            {"criteria": "Open source vs. managed service",
             "why": "Airbyte offers self-hosted open source. Fivetran is fully managed. Self-hosting saves money but requires DevOps capacity. If your team has fewer than 2 data engineers, managed services are worth the premium."},
        ],
        "recommended_tools": [
            {"slug": "fivetran", "why": "The market leader in managed ELT. 500+ pre-built connectors with automated schema management. Strongest for teams that want zero-maintenance data pipelines. Pricing scales with data volume, which gets expensive for high-volume sources."},
            {"slug": "airbyte", "why": "Open-source ELT alternative to Fivetran. 400+ connectors, self-hosted or cloud-managed. Dramatically lower cost for teams with DevOps capacity. Growing connector quality, but some lag behind Fivetran's managed equivalents."},
            {"slug": "hightouch", "why": "The leading reverse ETL platform. Takes warehouse models and syncs them to 200+ business tools. Enables marketing, sales, and support teams to use warehouse data without SQL access. Competes with Census."},
            {"slug": "census-data", "why": "Reverse ETL with strong CRM and marketing tool connectors. Composable CDP features let marketing teams build segments on warehouse data. Competitive with Hightouch on features, with different pricing structure."},
        ],
        "bottom_line": "Fivetran for managed ELT if budget allows. Airbyte for cost-sensitive teams with engineering resources. Hightouch or Census for reverse ETL, choose based on specific connector needs. Most mature data teams end up with an ELT tool plus a reverse ETL tool.",
        "faq": [
            {"q": "What's the difference between ELT and reverse ETL?",
             "a": "ELT (Extract, Load, Transform) moves data from business tools into your data warehouse. Reverse ETL moves modeled data from your warehouse back out to business tools. You typically need both: ELT to centralize data, reverse ETL to operationalize it."},
            {"q": "How much does a data pipeline stack cost?",
             "a": "Fivetran starts at $1/month per connector for the free tier, scaling to $1-2 per 1K MAR for growth plans. Airbyte self-hosted is free (plus infrastructure costs). Hightouch starts at $350/month. Budget $500-3,000/month total for a mid-market data stack."},
            {"q": "Should I use Fivetran or Airbyte?",
             "a": "Fivetran if you want zero maintenance and have the budget. Airbyte if you have engineering capacity and want lower costs. For most teams under 50 employees, Airbyte's cloud offering is the best value. For enterprise teams that can't afford connector downtime, Fivetran's SLAs justify the premium."},
        ],
    },
    {
        "slug": "review-platforms-for-buyers",
        "title": "G2 vs Capterra: Which Review Platform Matters for B2B Buyers (2026)",
        "meta_description": "How B2B buyers should use G2 and Capterra for software evaluation. Review quality, vendor influence, and what the ratings actually mean.",
        "persona": "B2B software buyers and procurement teams evaluating vendors",
        "category_slug": "review-platforms",
        "intro": "G2 and Capterra dominate B2B software reviews, but they serve different audiences and have different incentive structures. G2 skews toward mid-market and enterprise buyers with more detailed reviews. Capterra (owned by Gartner) casts a wider net with more SMB-focused reviews. Neither platform is unbiased. Understanding how vendors influence ratings helps you extract real signal from the noise.",
        "what_to_look_for": [
            {"criteria": "Review recency and volume",
             "why": "A tool with 500 reviews from 2023 tells you less than one with 50 reviews from the last 6 months. Software changes fast. Filter by date and look for patterns in recent reviews, not lifetime averages."},
            {"criteria": "Reviewer verification",
             "why": "G2 verifies reviewers through LinkedIn, making fake reviews harder (but not impossible). Capterra has less rigorous verification. In both cases, vendors incentivize reviews with gift cards. Read the negative reviews for the real signal."},
            {"criteria": "Category placement",
             "why": "Vendors pay for premium placement in G2 Grids and Capterra categories. The top-listed tool isn't necessarily the best. It may just have the largest marketing budget. Sort by user rating, not default order."},
            {"criteria": "Review depth and specificity",
             "why": "One-line reviews are useless. Look for reviews that mention specific use cases, team sizes, and implementation experiences. These tell you whether the tool works for your situation, not just whether it works in general."},
        ],
        "recommended_tools": [
            {"slug": "g2", "why": "The most trusted B2B review platform with the deepest review content. Grid reports are widely used in procurement. Stronger for mid-market and enterprise software. Vendors invest heavily in G2 presence, which means more reviews but also more vendor influence."},
            {"slug": "capterra", "why": "Broader coverage of SMB and niche tools. Part of the Gartner Digital Markets portfolio. Simpler interface for quick comparisons. Reviews tend to be shorter but cover a wider range of products than G2."},
        ],
        "bottom_line": "Use G2 for enterprise and mid-market software decisions where review depth matters. Use Capterra for quick comparisons of SMB tools. In both cases, focus on recent negative reviews for the most honest signal. Vendors game ratings on both platforms, so never make a buying decision based solely on review scores.",
        "faq": [
            {"q": "Are G2 reviews trustworthy?",
             "a": "More than most alternatives, but not unbiased. G2 verifies reviewers through LinkedIn, which reduces fake reviews. However, vendors incentivize reviews with gift cards ($25-50 per review), which skews toward satisfied users willing to invest time. Read the 2-3 star reviews for balanced perspective."},
            {"q": "What's the difference between G2 and Capterra?",
             "a": "G2 has deeper, more detailed reviews and is more popular with mid-market and enterprise buyers. Capterra (Gartner) has broader tool coverage and more SMB-focused reviews. G2's Grid methodology is more sophisticated. Capterra's is simpler to scan."},
            {"q": "Should vendors pay for G2 presence?",
             "a": "If you sell to mid-market or enterprise, yes. G2 appears in most procurement processes. The free tier lets you claim your profile and respond to reviews. Paid plans ($30K-100K/year) add intent data, competitive intelligence, and premium placement in Grid reports."},
        ],
    },
    {
        "slug": "sales-engagement-for-outbound",
        "title": "Sales Engagement Platforms for Outbound Teams (2026)",
        "meta_description": "How to choose a sales engagement platform. Salesloft, Outreach, Apollo, and Instantly compared for SDR productivity, automation, and pipeline impact.",
        "persona": "SDR managers and VP Sales running outbound-heavy teams",
        "category_slug": "list-building",
        "intro": "Sales engagement platforms automate the repetitive parts of outbound: email sequences, call scheduling, follow-up cadences, and activity logging. The right platform makes each rep 30-50% more productive. The wrong one becomes another tool they ignore. At this point the market has two tiers: enterprise platforms (Salesloft, Outreach) and growth-stage alternatives (Apollo, Instantly) that bundle data with outreach.",
        "what_to_look_for": [
            {"criteria": "Sequence intelligence",
             "why": "Basic sequencing is table stakes. Look for A/B testing, send-time optimization, and reply detection that pauses sequences when prospects respond. Smart sequencing improves reply rates by 15-25% over static cadences."},
            {"criteria": "CRM integration depth",
             "why": "Activity logging should be automatic and bidirectional. Every call, email, and meeting needs to appear in your CRM without rep input. If reps have to manually log activities, they won't, and your CRM data becomes unreliable."},
            {"criteria": "Deliverability management",
             "why": "Cold email at scale kills sender reputation fast. Look for domain rotation, warm-up features, bounce monitoring, and sending limits that protect your email domain. This matters more than feature lists."},
            {"criteria": "Data bundling vs. standalone",
             "why": "Apollo and Instantly include contact databases. Salesloft and Outreach don't. Bundled platforms save $10K-30K/year on a separate data provider. Standalone platforms offer better integration with premium data sources."},
        ],
        "recommended_tools": [
            {"slug": "salesloft", "why": "Enterprise-grade sales engagement with the deepest Salesforce integration. 43 job postings in our dataset. Strong analytics and coaching features for sales managers. Pricing starts around $125/user/month."},
            {"slug": "outreach-io", "why": "The other enterprise standard. More workflow automation features than Salesloft. Machine learning pipeline predictions. Similar pricing tier. Choose between Salesloft and Outreach based on CRM compatibility and which analytics features your managers need."},
            {"slug": "apollo", "why": "Data plus outreach in one platform. Built-in contact database with 275M+ contacts. Free tier includes basic sequencing. Best for growth teams that can't afford separate data and engagement tools."},
            {"slug": "instantly", "why": "Purpose-built for high-volume cold email. Unlimited email accounts, built-in warm-up, and deliverability monitoring. The lowest cost option for teams focused on email-first outbound. No phone or social features."},
        ],
        "bottom_line": "Salesloft or Outreach for enterprise teams with 20+ SDRs and Salesforce. Apollo for growth teams wanting data plus outreach. Instantly for pure cold email at scale. The biggest mistake is over-engineering sequences. Start with 3-step cadences and optimize from there.",
        "faq": [
            {"q": "What's the difference between Salesloft and Outreach?",
             "a": "Both are enterprise sales engagement platforms with similar core features. Salesloft has slightly better CRM integration and coaching tools. Outreach has more workflow automation and pipeline intelligence. Most teams pick based on their CRM and which UI their reps prefer during the trial."},
            {"q": "Can Apollo replace Salesloft?",
             "a": "For teams under 20 SDRs, yes. Apollo's sequencing covers 80% of what Salesloft does at a fraction of the cost, plus you get built-in contact data. Salesloft's advantages show at scale: enterprise security, advanced analytics, and deeper CRM integration."},
            {"q": "How many emails should an SDR send per day?",
             "a": "50-100 personalized emails per day is the practical ceiling for quality outreach. Tools like Instantly can send more, but reply rates drop sharply above 100/day. Focus on targeting accuracy and personalization over volume."},
        ],
    },
    {
        "slug": "data-enrichment-for-marketing",
        "title": "Data Enrichment for Marketing Teams: Lead Scoring, Segmentation & Personalization (2026)",
        "meta_description": "How marketing teams use data enrichment for lead scoring, segmentation, and personalization. Clearbit, ZoomInfo, and Apollo compared for marketing ops.",
        "persona": "Marketing ops managers and demand gen leads building automated lead workflows",
        "category_slug": "enrichment",
        "intro": "Marketing teams need enrichment for three things: scoring inbound leads fast, segmenting audiences for personalization, and keeping form fills short. The right enrichment tool appends firmographic and technographic data to every form submission, letting you route leads by company size, industry, and tech stack without asking 15 qualifying questions.",
        "what_to_look_for": [
            {"criteria": "Real-time form enrichment",
             "why": "The best enrichment happens the moment a lead fills out a form. Email address goes in, company name, size, industry, and revenue come back. This lets you route enterprise leads to sales immediately instead of waiting for SDR qualification."},
            {"criteria": "Marketing platform integration",
             "why": "Enrichment data needs to flow into your MAP (HubSpot, Marketo, Pardot) for segmentation and scoring. Check that the integration maps fields correctly and triggers workflow automations on enrichment completion."},
            {"criteria": "Match rate by segment",
             "why": "Enrichment accuracy varies by company size and geography. Enterprise US companies match at 80-90%. International SMBs match at 40-60%. Test with your actual lead flow before committing to an annual contract."},
            {"criteria": "Cost per enrichment",
             "why": "Some tools charge per API call, others per record per month, others bundle into platform fees. If you enrich 10,000 leads per month, the difference between $0.01 and $0.10 per enrichment is $12,000/year."},
        ],
        "recommended_tools": [
            {"slug": "clearbit", "why": "The gold standard for marketing enrichment. Real-time form enrichment, reveal (visitor identification), and advertising audience building. Now part of HubSpot. Strongest for product-led growth companies that need instant lead qualification."},
            {"slug": "zoominfo", "why": "The broadest database, but primarily built for sales. Marketing teams use ZoomInfo for audience building, display advertising, and form enrichment. More expensive than Clearbit for pure marketing use cases, but stronger if you also need sales prospecting."},
            {"slug": "apollo", "why": "Growing marketing enrichment capabilities alongside its sales platform. API-based enrichment at a fraction of ZoomInfo's cost. Best for teams that want enrichment plus outreach without managing two vendor relationships."},
            {"slug": "clay", "why": "Waterfall enrichment that queries 75+ data providers to maximize match rates. Best for teams frustrated by single-source accuracy limitations. Higher per-record cost, but significantly better results for hard-to-match segments."},
        ],
        "bottom_line": "Clearbit for real-time form enrichment if you're on HubSpot. ZoomInfo for the broadest database and combined sales/marketing use. Apollo for budget-conscious teams. Clay for maximum accuracy through waterfall enrichment. Start by measuring your current form abandonment rate and lead routing speed to quantify the ROI.",
        "faq": [
            {"q": "What's the ROI of marketing data enrichment?",
             "a": "Teams typically see 20-30% reduction in form abandonment (fewer fields), 40-60% faster lead routing (instant qualification), and 15-25% improvement in email campaign performance (better segmentation). The ROI math works if you enrich more than 500 leads per month."},
            {"q": "Should marketing and sales use the same enrichment tool?",
             "a": "Ideally yes. Shared data ensures consistent lead scoring and avoids duplicate vendor costs. If your sales team uses ZoomInfo, marketing should too. If budget is tight, Clearbit for marketing and Apollo for sales can work as a lower-cost combination."},
            {"q": "How does enrichment affect form conversion rates?",
             "a": "Reducing form fields from 8 to 3 (email, first name, last name) typically improves conversion by 30-50%. Enrichment fills in the rest automatically. The tradeoff is match rate: 10-20% of leads won't enrich, so you may still need fallback qualification."},
        ],
    },
    {
        "slug": "abm-for-small-teams",
        "title": "Account-Based Marketing on a Budget: ABM Without Enterprise Pricing (2026)",
        "meta_description": "How small marketing teams run ABM programs without 6sense or Demandbase budgets. Practical tools and strategies for teams under $5K/month.",
        "persona": "Marketing managers at companies with 1-3 person marketing teams",
        "category_slug": "abm",
        "intro": "Enterprise ABM platforms (6sense, Demandbase) cost $50K-150K/year. Most teams under 100 employees can't justify that spend. But the ABM methodology works at any scale: identify target accounts, personalize outreach, and coordinate sales and marketing efforts. You just need different tools to execute it. The core of ABM is account selection and coordination, not software.",
        "what_to_look_for": [
            {"criteria": "Account selection without intent data",
             "why": "You don't need AI-powered intent signals to pick target accounts. Your sales team already knows their top 50 accounts. Start with CRM data, closed-won attributes, and ICP criteria. Add intent data when you've proven the motion works."},
            {"criteria": "Personalization at small scale",
             "why": "With 50-200 target accounts, you can personalize manually. Custom landing pages, 1:1 emails, and LinkedIn outreach don't require a platform. Focus on quality over automation at this stage."},
            {"criteria": "Sales-marketing alignment tools",
             "why": "ABM fails without sales buy-in. Use shared account lists in your CRM, weekly pipeline reviews, and Slack alerts for target account activity. The tooling matters less than the coordination."},
            {"criteria": "Measurable account engagement",
             "why": "Track website visits, email engagement, and ad impressions at the account level. Basic tools (Google Analytics + CRM) can show account-level engagement without an ABM platform. Graduate to 6sense when you need predictive scoring."},
        ],
        "recommended_tools": [
            {"slug": "hubspot", "why": "Target account features built into the CRM. ABM dashboards, account scoring, and company-level reporting. Not as sophisticated as dedicated ABM platforms, but free to start and integrated with your existing marketing stack."},
            {"slug": "linkedin-marketing", "why": "LinkedIn's Matched Audiences lets you target specific companies with advertising. Upload your account list and run targeted campaigns for $500-2,000/month. The most cost-effective way to get ABM advertising without 6sense or Demandbase."},
            {"slug": "warmly", "why": "Website visitor identification shows which target accounts are visiting your site. Real-time alerts let sales engage while interest is high. More affordable than enterprise ABM platforms for the visitor identification use case."},
            {"slug": "apollo", "why": "Build target account lists, enrich contacts, and run outreach sequences in one platform. Not technically an ABM tool, but covers the core ABM workflow (identify, personalize, outreach) at a growth-stage price point."},
        ],
        "bottom_line": "Start with HubSpot's ABM features and LinkedIn advertising. Add visitor identification (Warmly or Leadfeeder) when you want to see which accounts engage with your content. Move to 6sense or Demandbase when you have 500+ target accounts and need predictive intent data. ABM is a strategy, not a software category.",
        "faq": [
            {"q": "How much does ABM cost for a small team?",
             "a": "You can run a basic ABM program for under $2K/month: HubSpot CRM (free), LinkedIn advertising ($500-1,500/month), and a visitor identification tool ($200-500/month). Enterprise ABM platforms (6sense, Demandbase) start at $40K-60K/year."},
            {"q": "When should I upgrade to an enterprise ABM platform?",
             "a": "When you have 500+ target accounts, need predictive intent data, and want to coordinate advertising, web personalization, and email across all accounts automatically. If you're managing fewer than 200 accounts, manual ABM with basic tools works fine."},
            {"q": "Does ABM work for companies selling to SMBs?",
             "a": "Traditional ABM works best with enterprise deal sizes ($50K+) that justify per-account investment. For SMB sales, use ABM principles (targeting, personalization) but at the segment level, not the individual account level. It's more like targeted demand gen than true 1:1 ABM."},
        ],
    },
]


def main():
    dry_run = '--dry-run' in sys.argv

    uc = load("use_cases.json")
    tc = load("tool_content.json")
    tools = load("tools.json")
    tools_meta = {t['slug']: t for t in tools['tools']}

    uc_list = uc.get('use_cases', [])
    existing_slugs = {u['slug'] for u in uc_list}

    added = 0
    for new_uc in NEW_USE_CASES:
        if new_uc['slug'] in existing_slugs:
            print(f"  {new_uc['slug']}: SKIPPED (already exists)")
            continue

        # Verify recommended tools exist
        valid_tools = [
            t for t in new_uc['recommended_tools']
            if t['slug'] in tc
        ]
        if len(valid_tools) < 2:
            print(f"  {new_uc['slug']}: SKIPPED (not enough valid tools)")
            continue

        new_uc['recommended_tools'] = valid_tools
        new_uc['date_published'] = TODAY
        new_uc['date_modified'] = TODAY

        uc_list.append(new_uc)
        print(f"  {new_uc['slug']}: {len(valid_tools)} tools, {len(new_uc['faq'])} FAQs")
        added += 1

    uc['use_cases'] = uc_list
    print(f"\nTotal use case pages added: {added}")
    print(f"Total use case pages now: {len(uc_list)}")

    if dry_run:
        print("\n[DRY RUN] No changes written.")
    else:
        save("use_cases.json", uc)
        print(f"\nWritten to {DATA}/use_cases.json")


if __name__ == '__main__':
    main()
