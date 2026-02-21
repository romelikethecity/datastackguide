#!/usr/bin/env python3
"""
Generate new guide pages for underserved topics.
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


NEW_GUIDES = [
    {
        "slug": "crm-data-hygiene-playbook",
        "title": "CRM Data Hygiene Playbook: Keep Your Pipeline Clean (2026)",
        "meta_description": "A practical guide to CRM data hygiene. How to identify, fix, and prevent dirty data in Salesforce, HubSpot, and other B2B CRMs.",
        "intro": "Dirty CRM data costs B2B companies an average of 12% of revenue through wasted sales effort, missed opportunities, and bad forecasting. Most teams know their data is messy. Few have a systematic process for fixing it. This playbook gives you one.",
        "sections": [
            {"heading": "The Real Cost of Dirty Data",
             "content": "Dirty CRM data doesn't announce itself. It shows up as reps working stale leads, marketing sending emails to invalid addresses, and forecasts that miss by 20-30%. The symptoms feel like sales execution problems, but they're data problems.\n\nThe math is straightforward. If 25% of your contact records have incorrect emails, stale job titles, or wrong company associations, your outbound team is wasting 25% of their time. At a $75K fully loaded SDR cost, that's $18,750 per rep per year in lost productivity.\n\nThe compounding effect is worse. Bad data degrades lead scoring accuracy, which means marketing sends unqualified leads to sales, which erodes trust between the teams, which leads to sales ignoring marketing leads entirely. One data quality problem creates three organizational problems."},
            {"heading": "Common Data Quality Issues and How to Detect Them",
             "content": "Duplicate records are the most visible problem. Two records for the same person at the same company mean split activity history, inconsistent outreach, and inaccurate pipeline reporting. Most CRMs have built-in duplicate detection, but it only catches exact matches. Variations (Bob vs. Robert, Inc. vs. Incorporated) slip through.\n\nStale contacts are harder to spot. Job tenure averages 2.5 years in B2B sales roles. If your database hasn't been refreshed in 18 months, roughly 30% of contacts have changed jobs. Emails bounce silently. Calls reach the wrong person. Sales blames the leads.\n\nMissing fields seem harmless until they break automations. A lead without an industry field skips your lead routing rules. A contact without a phone number can't enter your calling sequence. Audit your required fields quarterly and measure fill rates.\n\nFormatting inconsistencies corrupt reporting. 'United States' vs 'US' vs 'USA' vs 'U.S.A.' creates four separate values in your country field. Standardize on picklists over free-text entry wherever possible."},
            {"heading": "Building a Data Hygiene Process",
             "content": "Start with an audit. Export your CRM data and measure: duplicate rate, email validity rate, phone validity rate, field fill rate for critical fields, and data age distribution. This baseline tells you where to focus.\n\nSet up ongoing monitoring. Schedule monthly data quality reports that track these metrics. Most enrichment tools (ZoomInfo, Apollo, Clearbit) can flag stale records automatically. Set up alerts when bounce rates spike or duplicate rates climb above your threshold.\n\nDefine data ownership. Every field should have a clear owner: which system is the source of truth, and which direction does data flow. Marketing owns lead source. Sales owns deal stage. The enrichment tool owns company firmographics. Document this and enforce it in your integration layer.\n\nAutomate what you can. Email verification on form submission prevents bad data from entering the system. Enrichment on record creation fills missing fields automatically. Duplicate detection rules should run daily, not monthly."},
            {"heading": "Enrichment as a Hygiene Tool",
             "content": "Data enrichment isn't just for prospecting. It's the most effective hygiene tool available. Regular enrichment passes update job titles, verify email addresses, correct company associations, and fill missing firmographic fields.\n\nSchedule enrichment runs quarterly for your full database and on-demand for new records. The cost of enriching 10,000 records quarterly ($500-2,000 depending on provider) is trivial compared to the productivity loss from stale data.\n\nZoomInfo, Apollo, and Clearbit all offer CRM hygiene features that scan existing records and flag changes. Clay's waterfall enrichment can cross-reference multiple providers for higher accuracy on critical accounts. Choose based on your existing data provider and CRM integration."},
            {"heading": "Preventing Data Decay",
             "content": "Prevention is cheaper than cleanup. Three mechanisms reduce data decay by 50-70%.\n\nForm standardization eliminates formatting issues at the source. Use dropdown menus instead of text fields for country, industry, company size, and job title. Progressive profiling (showing different form fields on each visit) fills gaps over time without long forms.\n\nIntegration hygiene prevents sync conflicts. When two systems disagree about a field value, clear ownership rules determine which one wins. Without these rules, systems overwrite each other and data quality degrades with every sync cycle.\n\nRegular purges remove dead weight. Contacts who haven't engaged in 12+ months, companies that have closed, and duplicate records that escaped detection all need to be archived or merged. Schedule quarterly purges and measure database health before and after."},
            {"heading": "Measuring Data Quality Over Time",
             "content": "Track five metrics monthly to measure data hygiene progress.\n\nEmail bounce rate should stay below 3%. Above 5% indicates systemic data quality issues that damage sender reputation. Track this at the campaign level and investigate spikes immediately.\n\nDuplicate rate should trend downward. Measure as a percentage of total records. Industry benchmark is under 5% for well-maintained databases.\n\nField fill rate for critical fields (email, phone, company, title, industry) should be above 85%. Measure by segment: new leads, active opportunities, and customer records may have different fill rates.\n\nData age distribution shows what percentage of records were last enriched or verified within 3, 6, 12, and 18 months. Records older than 12 months should be flagged for re-verification.\n\nEnrichment match rate measures how many records your enrichment provider can match and update. Declining match rates may indicate that your data is drifting away from the provider's coverage or that your ICP has shifted."},
        ],
        "related_tools": ["zoominfo", "apollo", "clearbit", "clay"],
        "related_categories": ["data-quality", "enrichment", "validation"],
        "faq": [
            {"q": "How often should I clean my CRM data?",
             "a": "Monthly monitoring with quarterly deep cleans. Set up automated hygiene rules (duplicate detection, email verification) that run daily. Do manual audits and enrichment passes every 90 days. Budget 4-8 hours per quarter for a database under 50,000 records."},
            {"q": "What's the best CRM data hygiene tool?",
             "a": "Your existing enrichment provider is usually the best starting point. ZoomInfo, Apollo, and Clearbit all offer CRM hygiene features. For dedicated hygiene, RingLead (now ZoomInfo) and Validity (DemandTools) specialize in deduplication and standardization. Choose based on your CRM platform."},
            {"q": "How much does CRM data decay each year?",
             "a": "B2B data decays at roughly 25-30% per year. This means a quarter of your contacts change jobs, companies, or email addresses annually. For fast-moving industries (tech, startups), decay rates are higher. For stable industries (healthcare, government), lower."},
        ],
    },
    {
        "slug": "evaluating-abm-platforms",
        "title": "How to Evaluate ABM Platforms: 6sense vs Demandbase and Beyond (2026)",
        "meta_description": "A buyer's guide to ABM platforms. How to evaluate 6sense, Demandbase, Terminus, and alternatives based on your team size, budget, and GTM motion.",
        "intro": "ABM platforms are expensive, complex, and transformative when they work. The challenge is figuring out whether your organization is ready for one and which platform fits your specific go-to-market motion. This guide helps you make that decision without a 6-month evaluation process.",
        "sections": [
            {"heading": "Are You Ready for an ABM Platform?",
             "content": "Most companies buy ABM platforms before they need them. If you're managing fewer than 200 target accounts, don't have dedicated marketing ops capacity, or can't articulate your ideal customer profile in specific firmographic terms, you're not ready. You'll spend $50K-150K/year on a platform that sits underutilized.\n\nThe readiness checklist: You have a defined ICP with at least 500 target accounts. You have sales and marketing alignment on account prioritization. You have at least one person who can build and maintain workflows in a marketing automation platform. You have a Salesforce or HubSpot CRM with clean account data. If you check all four, proceed. If not, start with basic ABM using HubSpot and LinkedIn advertising."},
            {"heading": "Understanding the ABM Platform Landscape",
             "content": "The market has consolidated around two enterprise leaders (6sense and Demandbase) and a mid-market tier (Terminus, RollWorks). Each platform bundles intent data, advertising, web personalization, and sales intelligence in different proportions.\n\n6sense leads on predictive analytics and AI-powered account scoring. Its Revenue AI platform identifies accounts showing buying signals before they fill out forms. Strongest for teams that want the platform to surface accounts automatically rather than working from a static list.\n\nDemandbase leads on advertising and B2B display capabilities. Its One Platform combines account identification, advertising, sales intelligence, and intent data. Strongest for teams where ABM advertising is the primary channel.\n\nTerminus offers a more accessible entry point with display advertising, email signatures, and chat. Less AI-powered than 6sense or Demandbase, but simpler to operationalize for mid-market teams.\n\nRollWorks (owned by NextRoll) focuses on advertising and account-based programs. Most affordable option for teams that primarily need ABM advertising without the full platform."},
            {"heading": "The Intent Data Question",
             "content": "Intent data is the core differentiator of enterprise ABM platforms. It tells you which accounts are researching topics related to your product, theoretically letting you reach them before competitors.\n\nThe reality is more nuanced. First-party intent (website visits, content engagement) is reliable but limited in scope. Third-party intent (6sense, Bombora, Demandbase) covers more accounts but has accuracy challenges. Research topics are inferred from content consumption patterns, and the signal-to-noise ratio varies by industry and company size.\n\nTest intent data before you buy the platform. Both 6sense and Demandbase offer intent data trials. Feed the output to your sales team for 30 days and measure whether intent-flagged accounts convert at a higher rate than your baseline. If the lift is under 20%, the intent data may not justify the platform cost."},
            {"heading": "Evaluating Platform Capabilities",
             "content": "Score each platform across five dimensions.\n\nAccount identification: How well does the platform match anonymous web traffic to target accounts? Test with your actual website traffic, not demo data. Match rates typically range from 20-40% depending on your traffic composition.\n\nIntent signal quality: Are the intent topics relevant to your business? Can you create custom intent topics? How frequently is data refreshed? Ask for a sample intent feed and validate against accounts you know are actively evaluating solutions.\n\nAdvertising capabilities: What display networks does the platform access? Can you run LinkedIn, programmatic display, and connected TV from one platform? What's the minimum ad spend the platform requires? Most enterprise ABM platforms require $5K-15K/month in ad spend to be effective.\n\nSales activation: Does the platform push actionable insights to sales reps in their CRM? Alert quality matters more than alert volume. If sales gets 50 alerts per day, they ignore all of them.\n\nReporting and attribution: Can you measure ABM's pipeline influence at the account level? Multi-touch attribution across advertising, web, and email is the baseline requirement. Ask for example attribution reports during the evaluation."},
            {"heading": "The Pricing Conversation",
             "content": "ABM platform pricing is opaque by design. Expect to negotiate and expect the initial quote to be significantly higher than what other customers pay.\n\n6sense pricing typically starts at $40K-60K/year for mid-market and $100K-200K+ for enterprise. The price depends on your target account list size, number of users, and which modules you include (advertising, intent data, sales intelligence).\n\nDemandbase follows a similar structure: $40K-80K for mid-market, $120K-250K for enterprise. Advertising spend is additional. Implementation consulting can add $20K-50K in year one.\n\nTerminus is more accessible: $25K-50K/year for most mid-market deployments. Simpler feature set means faster implementation.\n\nNegotiation tips: Push for a pilot period (90 days at reduced cost). Request intent data validation before committing to the full platform. Ask for references from companies at your stage and industry, not just enterprise logos. Get multi-year discounts in writing, and negotiate a cap on annual price increases."},
            {"heading": "Implementation and Time to Value",
             "content": "ABM platforms take 3-6 months to show results. Plan for it.\n\nMonth 1: Account list setup, CRM integration, basic intent data configuration. Your sales team should start seeing account-level insights by week 3-4.\n\nMonth 2: Advertising campaigns launch. First intent data signals start flowing. Begin A/B testing ad creative and intent topic configurations.\n\nMonth 3-4: Enough data to evaluate intent signal quality and advertising performance. First pipeline influence reports become meaningful. Sales feedback loop should be established.\n\nMonth 5-6: Optimize based on data. Refine intent topics, adjust account scoring weights, expand or contract target account lists. This is when you know whether the platform is working.\n\nThe biggest implementation risk is organizational, not technical. If sales doesn't trust or use the account insights, the platform fails regardless of data quality. Invest as much in sales enablement as you do in technical setup."},
        ],
        "related_tools": ["6sense", "demandbase", "terminus", "rollworks"],
        "related_categories": ["abm", "intent"],
        "faq": [
            {"q": "When should a company invest in an ABM platform?",
             "a": "When you have 500+ target accounts, $50K+ annual budget for ABM technology, dedicated marketing ops capacity, and CRM data clean enough to match against. If you're managing fewer than 200 accounts, basic ABM with HubSpot and LinkedIn advertising is more cost-effective."},
            {"q": "What's the difference between 6sense and Demandbase?",
             "a": "6sense leads on AI-powered predictive analytics and automatic account surfacing. Demandbase leads on B2B advertising capabilities and account-based display. Both offer intent data, sales intelligence, and web personalization. Choose 6sense for intent-driven account discovery. Choose Demandbase for advertising-led ABM programs."},
            {"q": "How long does an ABM platform take to show ROI?",
             "a": "3-6 months for initial pipeline influence. 9-12 months for meaningful revenue attribution. The first 90 days are setup and baseline establishment. Months 3-6 produce early results. Full ROI measurement requires a complete sales cycle, which is 6-18 months for most B2B companies."},
        ],
    },
    {
        "slug": "crm-migration-planning",
        "title": "CRM Migration Guide: How to Switch Without Losing Pipeline (2026)",
        "meta_description": "How to plan and execute a CRM migration. Data mapping, timeline, team training, and the common mistakes that derail B2B CRM switches.",
        "intro": "CRM migration is the most disruptive technology change a sales organization can make. Done well, it improves productivity within 90 days. Done poorly, it costs months of pipeline visibility and sales team trust. This guide covers the practical steps most migration plans skip.",
        "sections": [
            {"heading": "Deciding Whether to Migrate",
             "content": "Not every CRM frustration justifies a migration. The switching cost for a 50-person sales team is $100K-300K when you factor in software, implementation, data migration, retraining, and the productivity dip during transition.\n\nMigrate when your current CRM fundamentally can't support your sales process. If you need custom objects, multi-currency, advanced reporting, or API capabilities that your current platform doesn't offer, migration makes sense.\n\nDon't migrate because of UI preferences, minor feature gaps, or because a new vendor gave you a compelling demo. These problems are cheaper to solve with customization, integrations, or admin training on your current platform."},
            {"heading": "Building the Migration Plan",
             "content": "A CRM migration has five phases: assessment, data mapping, configuration, data migration, and training. Plan 3-6 months for the full process, longer for enterprise Salesforce deployments.\n\nAssessment (2-4 weeks): Document every custom field, workflow automation, report, dashboard, and integration in your current CRM. This inventory is your migration checklist. Anything you miss will break silently.\n\nData mapping (2-3 weeks): Map every field from the old system to the new one. Some fields will map directly. Others will need transformation. Some won't have equivalents. The mapping document becomes your data migration spec.\n\nConfiguration (3-6 weeks): Build the new CRM to match your mapped requirements. Resist the temptation to redesign your sales process during migration. Get the new system working like the old one first. Optimize after your team has stabilized."},
            {"heading": "Data Migration: The Critical Path",
             "content": "Data migration is where most CRM switches fail. The problems are rarely technical. They're about data quality issues that were invisible in the old system.\n\nClean before you migrate. Run deduplication, standardize field values, archive stale records, and verify email addresses in the old system before exporting. Moving dirty data to a clean CRM just makes a new mess.\n\nMigrate in stages, not all at once. Start with accounts and contacts. Verify. Then opportunities. Verify. Then activities and notes. Verify. Each stage should pass a quality check before the next one begins.\n\nPreserve activity history. Sales reps rely on interaction history to contextualize relationships. If you lose email logs, call notes, and meeting records during migration, reps lose context on every active deal. This is the number one complaint from migrated teams. Verify that activity data transfers correctly for your top 20 accounts before doing the full migration."},
            {"heading": "Managing the Parallel Period",
             "content": "Run both CRMs in parallel for 2-4 weeks. This is painful but necessary. The parallel period catches data mapping errors, integration failures, and workflow gaps that testing didn't reveal.\n\nDuring the parallel period, all new activities should be logged in the new CRM. The old CRM becomes read-only reference. Set a hard cutover date and communicate it repeatedly. Without a firm deadline, teams will cling to the familiar system indefinitely.\n\nDesignate CRM champions (one per team of 10 reps) who help peers troubleshoot in the new system. Champions should get training 2-3 weeks before the broader team. They become the first line of support during transition."},
            {"heading": "Re-integrating Your Tech Stack",
             "content": "Every tool connected to your old CRM needs to be reconnected to the new one. Map your integration dependencies before migration starts.\n\nPriority 1 (day one): Email integration, calendar sync, and your sales engagement platform. Reps can't work without these.\n\nPriority 2 (week one): Marketing automation, enrichment tools, and lead routing. These affect pipeline flow.\n\nPriority 3 (weeks 2-4): Analytics, forecasting, CPQ, and secondary tools. These can tolerate a brief gap.\n\nIf you use an iPaaS (Workato, Zapier, Tray), update the CRM connector in your iPaaS and all downstream workflows. A single broken Zapier workflow can silently corrupt data for weeks before anyone notices."},
            {"heading": "Training and Adoption",
             "content": "Technical migration is half the project. User adoption is the other half, and it's the half that determines success.\n\nDon't train on features. Train on workflows. Show reps how to do their daily tasks in the new system: log a call, move a deal, run their pipeline report. If they can do their job in the new CRM by the end of training, adoption follows.\n\nRecord the training sessions. Make them available on-demand. Reps will forget steps and need to reference them. A 15-minute recorded walkthrough of common workflows prevents 50 support tickets.\n\nMeasure adoption weekly for the first 60 days. Track login frequency, activity logging rate, and pipeline update frequency. If any metric drops below 70% of pre-migration levels, investigate immediately. Early intervention prevents the death spiral of non-adoption."},
        ],
        "related_tools": ["salesforce", "hubspot", "dynamics-365", "pipedrive"],
        "related_categories": ["crm"],
        "faq": [
            {"q": "How long does a CRM migration take?",
             "a": "3-6 months for most mid-market companies. 6-12 months for enterprise Salesforce deployments with complex customization. Plan for 1-2 months of assessment and mapping, 1-2 months of configuration, 1-2 months of data migration and testing, and 2-4 weeks of parallel operation."},
            {"q": "How much does CRM migration cost?",
             "a": "For a 50-person sales team: $50K-150K for implementation consulting, $20K-50K in productivity loss during transition, plus the new CRM license cost. DIY migrations save on consulting but take longer and carry higher risk of data loss."},
            {"q": "What data should I migrate to the new CRM?",
             "a": "Active accounts, contacts with recent activity, open opportunities, and 12-18 months of activity history. Don't migrate closed-lost opportunities older than 2 years, duplicate records, or contacts that bounced. Clean data migrates faster and gives the new system a strong foundation."},
        ],
    },
    {
        "slug": "intent-data-buyers-guide",
        "title": "Intent Data Buyer's Guide: What to Know Before You Buy (2026)",
        "meta_description": "How B2B intent data works, what it costs, and whether it's worth it. First-party vs third-party intent compared for demand gen and sales teams.",
        "intro": "Intent data promises to tell you which accounts are actively researching your solution. The reality is more complicated. Some intent signals are powerful buying indicators. Others are noise. This guide helps you separate the signal from the marketing hype and evaluate whether intent data justifies its cost for your team.",
        "sections": [
            {"heading": "How Intent Data Actually Works",
             "content": "Intent data tracks content consumption patterns across the B2B web. When employees at a target account read articles, download whitepapers, or visit review sites about topics relevant to your product, intent providers detect these signals and flag the account as 'in-market.'\n\nThe detection methods vary. Bombora's Data Co-op aggregates content consumption across 5,000+ publisher sites. 6sense combines web activity, content engagement, and firmographic signals through AI models. Demandbase uses its own ad network data plus third-party content signals. Each approach has different coverage and accuracy trade-offs.\n\nFirst-party intent (your website visitors, your content engagement) is the most reliable but narrowest in scope. Third-party intent (Bombora, 6sense) is broader but noisier. The best programs combine both: third-party signals identify accounts to target, first-party signals confirm and prioritize them."},
            {"heading": "Types of Intent Signals and Their Value",
             "content": "Not all intent signals are equal. Topic-level intent ('CRM evaluation') is useful but broad. Competitor-specific intent ('Salesforce pricing') is much more actionable. Product-category intent ('sales engagement platform') falls in between.\n\nSurge intent measures when an account's research activity on a topic spikes above its baseline. This is more valuable than absolute volume because it indicates a change in behavior. An account that suddenly starts researching 'data enrichment tools' after months of no activity is a stronger signal than one that reads data-related content regularly.\n\nBuying group signals identify when multiple people at the same account research the same topics. One person reading about CRM migration is casual interest. Three people from different departments researching CRM options is a buying committee forming. Platforms like 6sense and Demandbase are building buying group detection, though accuracy is still evolving."},
            {"heading": "Evaluating Intent Data Quality",
             "content": "Before committing to an intent data provider, run a validation test. Take 50 accounts you know are actively evaluating solutions (from recent inbound demos or sales conversations) and check whether the intent provider flags them. If fewer than 30-40% match, the data doesn't cover your market well enough.\n\nAlso test the false positive rate. Take 50 accounts you know are not evaluating (existing customers, companies too small for your product) and check if the intent data flags them. High false positive rates mean your sales team will waste time chasing phantom signals.\n\nData freshness matters. Intent signals are perishable. An account showing intent 30 days ago has likely moved on. Weekly data refreshes are the minimum for actionable intent. Daily refreshes are better for high-velocity sales motions.\n\nGeographic coverage varies dramatically. US coverage is strongest across all providers. European coverage is weaker. APAC coverage is often sparse. If you sell internationally, validate coverage by region during your trial period."},
            {"heading": "What Intent Data Costs",
             "content": "Standalone intent data feeds (Bombora) typically cost $25K-60K/year depending on the number of topics, accounts, and users. This gives you raw intent signals without a platform to act on them.\n\nPlatform-bundled intent (6sense, Demandbase) costs $40K-200K/year because intent is packaged with advertising, sales intelligence, and orchestration capabilities. You're paying for the platform, not just the data.\n\nBombora intent data is also available through integration partners (Salesforce, HubSpot, several enrichment tools) at a lower price point, typically $10K-30K/year. The coverage is the same, but you lose the standalone reporting and custom topic creation.\n\nThe ROI calculation is straightforward but hard to measure precisely. If intent data helps you close 3-5 additional enterprise deals per year that you would have otherwise missed, it pays for itself. The challenge is attributing those deals to intent signals vs. other factors."},
            {"heading": "Building Intent into Your Workflow",
             "content": "Intent data creates value only when it triggers action. The most common mistake is buying intent data, pushing it to a dashboard nobody checks, and declaring it ineffective six months later.\n\nFor marketing: Intent signals should trigger advertising campaigns, content syndication, and email nurture sequences. When a target account shows intent, increase ad spend against that account and enroll known contacts in relevant drip campaigns. Measure lift in engagement and pipeline creation.\n\nFor sales: Intent signals should appear as CRM alerts or Slack notifications, not in a separate portal. When a rep's target account shows intent, they should see it in their daily workflow. Include the specific topics the account is researching so reps can personalize outreach.\n\nFor SDRs: Intent should inform prioritization, not replace prospecting. SDRs should focus outbound effort on intent-flagged accounts and personalize messages around the topics being researched. This increases connect rates by 20-40% compared to cold outreach."},
            {"heading": "When Intent Data Isn't Worth It",
             "content": "Intent data is not worth the investment for every team.\n\nIf your average deal size is under $20K, the cost of intent data relative to deal value is hard to justify. The math works better for enterprise sales with $50K+ deal sizes.\n\nIf you sell to SMBs, intent data coverage is thin. Most providers detect signals from mid-market and enterprise accounts. Small company research behavior is harder to track and less reliable.\n\nIf your sales cycle is under 30 days, intent signals may arrive too late. By the time third-party data processes and delivers the signal, the buyer has already made a decision. Fast-cycle sales benefit more from first-party intent (website behavior, product usage) than third-party signals.\n\nIf you lack the operational capacity to act on intent data, don't buy it. Intent is a workflow input, not a product. Without marketing automation, CRM integration, and a team to build and maintain workflows, the data sits unused."},
        ],
        "related_tools": ["6sense", "demandbase", "bombora", "terminus"],
        "related_categories": ["intent", "abm"],
        "faq": [
            {"q": "What's the best intent data provider?",
             "a": "Depends on your use case. Bombora for standalone intent data feeds at the lowest cost. 6sense for AI-powered account scoring and predictive analytics. Demandbase for advertising-led ABM with intent signals. All three use different methodologies, so test each against your known in-market accounts."},
            {"q": "How accurate is B2B intent data?",
             "a": "Accuracy varies by provider, industry, and company size. In our testing, 6sense and Bombora correctly flag 30-50% of known in-market accounts. False positive rates run 10-20%. The data is directional, not precise. Use it for prioritization, not as the sole outreach trigger."},
            {"q": "Can I get intent data without buying an ABM platform?",
             "a": "Yes. Bombora sells intent data feeds separately ($25K-60K/year). Several tools integrate Bombora data at lower price points (Salesforce, some enrichment platforms). You can also build first-party intent tracking with Google Analytics, CRM website tracking, and marketing automation engagement scoring at no additional cost."},
        ],
    },
    {
        "slug": "b2b-data-compliance-guide",
        "title": "B2B Data Compliance: GDPR, CCPA, and Outbound Prospecting Rules (2026)",
        "meta_description": "How B2B sales and marketing teams stay compliant with GDPR, CCPA, and CAN-SPAM while running outbound programs. Practical rules, not legal theory.",
        "intro": "Every B2B sales team sends cold emails. Most aren't fully compliant with data privacy regulations. This guide covers the practical compliance requirements for outbound prospecting, data enrichment, and marketing automation without requiring a law degree. It's not legal advice. Consult your legal team for specifics.",
        "sections": [
            {"heading": "The Regulatory Landscape for B2B Data",
             "content": "Three regulations matter most for B2B sales and marketing teams.\n\nGDPR (EU/UK) applies when you contact anyone in Europe, regardless of where your company is based. It requires a legal basis for processing personal data, the right to access and delete data, and strict consent requirements for marketing communications. B2B cold email is possible under 'legitimate interest' but requires careful documentation.\n\nCCPA/CPRA (California) gives California residents the right to know what data you collect, opt out of data sales, and request deletion. It applies to B2B data since 2023. Most B2B data providers classify their activities as 'data sharing' rather than 'data selling' to navigate this.\n\nCAN-SPAM (US) is the most lenient. It allows unsolicited commercial email as long as you include an unsubscribe mechanism, a physical address, and accurate sender information. There's no opt-in requirement for B2B email in the US."},
            {"heading": "Cold Email Compliance by Region",
             "content": "US cold email: Legal under CAN-SPAM with few restrictions. Include an unsubscribe link, your company address, and don't use deceptive subject lines. You can email any business contact without prior consent. This is why US-focused outbound teams have more freedom.\n\nEU cold email: Legal under GDPR's 'legitimate interest' basis if you can demonstrate that the email is relevant to the recipient's professional role and you've documented your legitimate interest assessment. Practically, this means emailing a VP of Sales about your sales tool is defensible. Emailing a random employee about an irrelevant product is not.\n\nCanada: CASL (Canadian Anti-Spam Legislation) is the strictest major market. Express consent is required before sending commercial email. Implied consent exists for existing business relationships (up to 2 years after a purchase or 6 months after an inquiry). Cold outbound to Canadian prospects requires extra caution.\n\nUK: Post-Brexit, the UK follows its own version of GDPR (UK GDPR + PECR). Practically identical to EU rules for B2B outbound."},
            {"heading": "Data Provider Compliance",
             "content": "When you buy data from ZoomInfo, Apollo, Cognism, or any B2B data provider, you inherit some of their compliance obligations.\n\nVerify that your provider has a legal basis for the data they sell. Ask about their data sourcing methodology, GDPR compliance documentation, and CCPA data processing agreements. Reputable providers will have these readily available.\n\nCognism is notable for building GDPR compliance into its core product. Its Diamond Data is phone-verified with consent acknowledgment. For teams targeting European prospects, this reduces compliance risk.\n\nWhen enriching records, you're processing personal data under GDPR. Document your enrichment as a data processing activity in your records of processing activities (ROPA). Include the legal basis, data categories, and retention period."},
            {"heading": "Practical Compliance Steps for Sales Teams",
             "content": "Honor unsubscribe requests within 10 business days (CAN-SPAM) or immediately (best practice). Build suppression lists that sync across all your outreach tools. An unsubscribe from your marketing emails should also suppress cold outreach from your SDR tools.\n\nMaintain a records of processing activities document. GDPR requires this for any organization processing EU personal data. List every system that stores personal data, what data it holds, why you have it, and how long you keep it. Update it annually.\n\nRespond to data subject access requests (DSARs) within 30 days. Under GDPR, any EU resident can request to see all data you hold on them and ask for deletion. Build a process for finding and exporting all data about a person across CRM, marketing automation, enrichment tools, and sales engagement platforms.\n\nUse legitimate interest assessments (LIAs) for B2B cold outreach in the EU. An LIA documents why your outreach is relevant to the recipient's professional interests, how you balance their privacy rights against your business need, and what safeguards you've put in place. Template LIAs are available from most B2B data compliance consultants."},
            {"heading": "Data Retention and Deletion",
             "content": "Keep data only as long as you need it. Under GDPR, indefinite retention is not acceptable. Define retention periods for each data category.\n\nProspect data (no response after outreach): Delete or anonymize after 12-24 months. Keeping records of people who never engaged with you indefinitely is hard to justify under legitimate interest.\n\nCustomer data: Retain for the duration of the business relationship plus any legally required period (typically 7 years for financial records in the US).\n\nMarketing consent records: Keep as long as the consent is active. Delete within 30 days of consent withdrawal.\n\nAutomate deletion where possible. Most CRMs support time-based archival rules. Set up automated workflows that flag records approaching their retention deadline and archive or delete them after review."},
        ],
        "related_tools": ["cognism", "apollo", "zoominfo"],
        "related_categories": ["enrichment", "contact-databases", "list-building"],
        "faq": [
            {"q": "Can I send cold emails to EU businesses under GDPR?",
             "a": "Yes, using legitimate interest as your legal basis. The email must be relevant to the recipient's professional role, include an unsubscribe mechanism, and you must document your legitimate interest assessment. It's not as permissive as US CAN-SPAM, but B2B cold outreach is legal with proper documentation."},
            {"q": "Do I need consent to store B2B contact data in my CRM?",
             "a": "In the US, no. Under GDPR, you need a legal basis (legitimate interest or consent). Most B2B CRM storage falls under legitimate interest if you can justify it. Under CCPA, you need to disclose what data you collect and allow opt-out. Consent is the safest option globally, but not always required for B2B."},
            {"q": "What happens if I violate GDPR with B2B data?",
             "a": "Fines can reach 4% of global revenue or 20 million euros, whichever is higher. In practice, most B2B enforcement actions result in warnings and corrective orders. Actual fines for B2B data violations have been rare but are increasing. The reputational risk and legal costs of an investigation often exceed the fine itself."},
        ],
    },
    {
        "slug": "marketing-ops-tool-selection",
        "title": "Building a Marketing Ops Stack: Tool Selection for B2B Teams (2026)",
        "meta_description": "How to choose marketing ops tools. Email, automation, analytics, and data management platforms compared for B2B marketing teams at every stage.",
        "intro": "Marketing ops is the infrastructure that makes campaigns work at scale. The stack you build determines whether your team spends time on strategy or firefighting data issues. This guide covers tool selection by function, how to avoid over-buying, and when to add complexity vs. keep it simple.",
        "sections": [
            {"heading": "Start With the Core: MAP + CRM",
             "content": "Every marketing ops stack starts with two tools: a marketing automation platform (MAP) and a CRM. Everything else is optional until these two work well together.\n\nFor HubSpot shops: HubSpot's Marketing Hub is the natural MAP. It shares the same database as the CRM, eliminating sync issues. The trade-off is less flexibility than standalone tools and escalating costs at scale.\n\nFor Salesforce shops: Marketo (Adobe) is the enterprise standard. Pardot (Salesforce Marketing Cloud Account Engagement) is simpler but less powerful. HubSpot Marketing Hub also integrates well with Salesforce if you want to avoid the Adobe/Salesforce ecosystem lock-in.\n\nThe most common mistake is buying the MAP before defining your marketing workflows. Document your lead lifecycle stages, scoring criteria, and nurture sequences first. Then pick the tool that supports them with the least customization."},
            {"heading": "Enrichment and Data Quality Layer",
             "content": "Marketing ops teams need enrichment for three reasons: shorter forms, better segmentation, and accurate lead scoring. Without enrichment, you're asking prospects to fill in 10 fields or accepting leads with missing data that breaks your automations.\n\nClearbit is the standard for marketing enrichment. Real-time form enrichment, reveal for anonymous visitor identification, and audience building for ads. Now part of HubSpot, which makes it even more natural for HubSpot shops.\n\nFor teams on Salesforce with ZoomInfo, use ZoomInfo's enrichment features rather than adding a second data provider. Consolidating reduces cost and data conflicts.\n\nApollo works as a budget-friendly enrichment option for smaller teams. The API is capable, the data quality is acceptable (80-85% email accuracy), and the pricing is dramatically lower than ZoomInfo or Clearbit."},
            {"heading": "Analytics and Attribution",
             "content": "Attribution in B2B marketing is never perfectly accurate. But directionally useful attribution beats no attribution every time.\n\nFirst-touch and last-touch models are built into most MAPs and CRMs. They're simple but misleading for long sales cycles. A lead that found you through a blog post 6 months ago and converted after a webinar deserves credit for both touchpoints.\n\nMulti-touch attribution requires either an enterprise MAP (Marketo, HubSpot Enterprise) or a dedicated attribution platform (Dreamdata, Bizible). These tools track every touchpoint across channels and assign weighted credit. Expect to spend $500-2,000/month for standalone attribution.\n\nThe pragmatic approach: Start with first-touch and last-touch in your CRM. Add multi-touch when you're spending enough on marketing ($500K+/year) that attribution accuracy directly affects budget allocation decisions."},
            {"heading": "Integration and Automation Layer",
             "content": "Marketing ops teams are integration teams. You connect the MAP to the CRM, the CRM to the data warehouse, the data warehouse to the BI tool, and dozens of point tools to each other.\n\nZapier handles simple integrations (form submission triggers, lead routing, Slack notifications) for under $100/month. Every marketing ops team should have a Zapier account for quick wins.\n\nMake replaces Zapier when you need branching logic, loops, or complex data transformations. The visual builder handles workflows that would require multiple Zapier zaps. Costs less per operation at scale.\n\nWorkato or Tray are justified when you manage 15+ integrations, need enterprise governance, or handle sensitive data that requires audit trails. The $30K-50K/year cost is offset by the operations time saved on maintaining point-to-point connections."},
            {"heading": "When to Add and When to Subtract",
             "content": "The biggest marketing ops mistake is tool sprawl. Every new tool adds complexity, cost, and maintenance overhead. Before adding a tool, ask: Can I do this with a tool I already have? Is the problem a tool problem or a process problem?\n\nAdd tools when you've outgrown a legitimate capability gap. Your MAP can't handle your email volume. Your analytics can't show multi-touch attribution. Your integration layer can't handle the sync frequency you need. These are real tool problems.\n\nDon't add tools to fix process problems. If your lead scoring isn't working, the answer is usually better scoring criteria, not a new scoring tool. If your campaigns aren't converting, the answer is usually better content and targeting, not a new personalization platform.\n\nAudit your stack annually. If a tool hasn't been used in 90 days, cancel it. If two tools overlap in functionality, consolidate to the one with broader coverage. Most marketing ops teams can reduce their stack by 20-30% without losing capability."},
        ],
        "related_tools": ["hubspot", "marketo", "salesforce-marketing-cloud", "clearbit", "zapier", "make"],
        "related_categories": ["marketing-automation", "orchestration", "enrichment"],
        "faq": [
            {"q": "How much should a marketing ops stack cost?",
             "a": "For a 5-person marketing team: $2K-5K/month (HubSpot Marketing Pro + enrichment + analytics). For a 15-person team: $5K-15K/month (enterprise MAP + enrichment + attribution + iPaaS). For enterprise: $15K-50K/month. Marketing ops spend typically runs 15-25% of the total marketing budget."},
            {"q": "Should marketing ops report to marketing or revenue ops?",
             "a": "Either works. Marketing ops under marketing is more common in companies under 200 employees. Revenue ops (spanning marketing, sales, and CS ops) is more common in companies over 200 employees. The key is alignment with the CRM and data teams, regardless of reporting structure."},
            {"q": "What's the first hire for a marketing ops team?",
             "a": "A marketing automation specialist who can manage your MAP, build email campaigns, configure lead scoring, and maintain basic integrations. This person should be comfortable with light SQL, API concepts, and project management. Typical salary: $70K-100K depending on market."},
        ],
    },
]


def main():
    dry_run = '--dry-run' in sys.argv

    guides = load("guides.json")
    tc = load("tool_content.json")

    guide_list = guides.get('guides', [])
    existing_slugs = {g['slug'] for g in guide_list}

    added = 0
    for new_guide in NEW_GUIDES:
        if new_guide['slug'] in existing_slugs:
            print(f"  {new_guide['slug']}: SKIPPED (already exists)")
            continue

        # Validate related tools exist
        valid_tools = [s for s in new_guide.get('related_tools', []) if s in tc]
        new_guide['related_tools'] = valid_tools
        new_guide['date_published'] = TODAY
        new_guide['date_modified'] = TODAY

        section_chars = sum(len(s['content']) for s in new_guide['sections'])
        guide_list.append(new_guide)
        print(f"  {new_guide['slug']}: {len(new_guide['sections'])} sections ({section_chars} chars), {len(new_guide['faq'])} FAQs")
        added += 1

    guides['guides'] = guide_list
    print(f"\nTotal guide pages added: {added}")
    print(f"Total guide pages now: {len(guide_list)}")

    if dry_run:
        print("\n[DRY RUN] No changes written.")
    else:
        save("guides.json", guides)
        print(f"\nWritten to {DATA}/guides.json")


if __name__ == '__main__':
    main()
