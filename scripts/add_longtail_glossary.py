#!/usr/bin/env python3
"""Add 25 new long-tail glossary terms targeting buyer-intent search queries."""

import json
from pathlib import Path
from datetime import date

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TODAY = date.today().isoformat()

NEW_TERMS = [
    # --- Data Quality & Accuracy ---
    {
        "slug": "data-completeness",
        "term": "Data Completeness",
        "short_definition": "The percentage of records in your database that have all required fields filled in.",
        "meta_description": "What is data completeness? Measuring how many CRM records have all required fields. See benchmarks, tools, and how to fix gaps in your B2B data.",
        "full_definition": "Data completeness measures the proportion of records that contain values for every field your team considers essential. A contact with a name and email but no phone, title, or company counts as incomplete. Most B2B databases run at 40-60% completeness out of the box. The specific threshold depends on your use case: lead scoring needs title and company size, outbound calling needs direct dials, and account-based plays need firmographic fields.",
        "why_it_matters": "Incomplete records break automation. Lead scoring assigns wrong priorities when title or company size is missing. Routing rules fail when territory fields are blank. Marketing segmentation produces catch-all segments instead of targeted campaigns. Every downstream process that depends on data quality starts with completeness.",
        "example": "A SaaS company audits their 50,000-record Salesforce instance and finds 62% of contacts are missing direct dial numbers, 41% lack job titles, and 28% have no company size. They run a batch enrichment through Apollo to fill the gaps, bringing completeness above 85% for their ICP contacts.",
        "related_terms": ["data-hygiene", "data-enrichment", "data-validation", "data-decay"],
        "related_tools": ["zoominfo", "clearbit", "apollo", "demandtools"],
        "category_slug": "data-quality",
        "related_roundups": ["best-data-quality-tools", "best-data-enrichment-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "match-rate",
        "term": "Match Rate",
        "short_definition": "The percentage of records a data provider can find and return results for when you submit them for enrichment.",
        "meta_description": "What is match rate in B2B data? The percentage of records enriched successfully. See typical rates by provider, what affects matching, and how to improve it.",
        "full_definition": "Match rate is the core metric for evaluating enrichment providers. When you send 1,000 contacts to an enrichment API and get data back for 720, your match rate is 72%. Rates vary by provider (ZoomInfo typically matches 70-85%, Apollo 60-75%, Clearbit 55-70%), by data type (emails match higher than direct dials), and by segment (US enterprise matches better than EMEA SMB). The number providers advertise is usually their best-case scenario.",
        "why_it_matters": "Match rate directly determines your ROI on data spending. If you pay $15,000/year for a tool that matches 60% of your records, your effective cost per enriched record is much higher than the sticker price. Comparing match rates across providers on your specific data (not their marketing claims) is the single most important step in vendor evaluation.",
        "example": "A RevOps team tests three providers against the same 2,000-record sample from their CRM. ZoomInfo returns 78% with verified emails, Apollo returns 71%, and Cognism returns 65% but with higher European mobile coverage. They choose ZoomInfo for US accounts and Cognism for EMEA, based on where each provider matches best.",
        "related_terms": ["data-enrichment", "data-completeness", "enrichment-waterfall", "data-validation"],
        "related_tools": ["zoominfo", "apollo", "clearbit", "cognism"],
        "category_slug": "enrichment",
        "related_roundups": ["best-data-enrichment-tools", "best-b2b-contact-databases"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "record-deduplication",
        "term": "Record Deduplication",
        "short_definition": "The process of finding and merging duplicate records in your CRM or database.",
        "meta_description": "What is record deduplication? Finding and merging duplicate CRM records. See dedup strategies, tools, and common matching rules for B2B databases.",
        "full_definition": "Deduplication identifies records that represent the same person or company and merges them into a single source of truth. Duplicates creep in through multiple channels: web forms creating new records for existing contacts, list imports with slight name variations, sales reps entering records manually without checking. The average CRM has 10-30% duplicate records. Dedup tools use fuzzy matching on names, email domains, phone numbers, and company names to catch variations like 'Mike Smith' vs 'Michael Smith' or 'IBM' vs 'International Business Machines'.",
        "why_it_matters": "Duplicates corrupt everything downstream. Sales reps contact the same person twice from different records. Lead scores split across duplicates, so hot leads look lukewarm. Pipeline reports double-count opportunities. And marketing sends the same email twice to the same inbox, which tanks deliverability. Every percentage point of duplicates you eliminate compounds through your entire revenue operation.",
        "example": "After importing 10,000 records from a trade show, an ops team runs DemandTools dedup and finds 1,800 matches against existing Salesforce records. They merge on a 'most recently updated' rule, preserving the newest email and phone while keeping the oldest created date for attribution accuracy.",
        "related_terms": ["data-normalization", "data-hygiene", "crm-hygiene", "data-enrichment"],
        "related_tools": ["demandtools", "salesforce", "hubspot", "clay"],
        "category_slug": "cleaning",
        "related_roundups": ["best-data-quality-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "bounce-rate-email",
        "term": "Email Bounce Rate",
        "short_definition": "The percentage of emails that fail to deliver because the address is invalid, full, or blocked.",
        "meta_description": "What is email bounce rate? Why B2B emails fail to deliver and how to keep bounce rates under 2%. See validation tools and sender reputation impact.",
        "full_definition": "Email bounce rate tracks undelivered messages. Hard bounces mean the address doesn't exist (typo, person left the company, domain expired). Soft bounces mean temporary failures (full inbox, server down, message too large). Industry benchmark for B2B outbound is under 2% bounce rate. Above 5% and you risk being flagged by email providers, which damages deliverability for your entire domain. Bounce rates correlate directly with data age: a list that's 6 months old will bounce 3-4x more than a freshly verified list.",
        "why_it_matters": "High bounce rates trigger spam filters. Gmail, Outlook, and corporate email servers track sender reputation at the domain level. One bad campaign with a 10% bounce rate can land your next 10 campaigns in spam, even the ones sent to valid addresses. Prevention through email verification before sending is 100x cheaper than repairing a damaged sender reputation.",
        "example": "An SDR team loads 5,000 cold prospects into Outreach and sends the first email without verification. The campaign bounces at 8.3%. Their domain sender score drops from 92 to 74. For the next three weeks, even their replies to warm leads land in spam folders. They implement a mandatory ZeroBounce verification step before any list enters their sequences.",
        "related_terms": ["email-deliverability", "email-warmup", "data-validation", "data-decay"],
        "related_tools": ["instantly", "lemlist", "outreach-io", "apollo"],
        "category_slug": "validation",
        "related_roundups": ["best-email-deliverability-tools", "best-data-validation-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "data-freshness",
        "term": "Data Freshness",
        "short_definition": "How recently the data in your database or from a provider was verified or updated.",
        "meta_description": "What is data freshness? How recently B2B data was verified. See freshness benchmarks by provider, decay rates, and refresh strategies.",
        "full_definition": "Data freshness measures the recency of verification. A contact record verified 30 days ago is fresher than one last checked 6 months ago. The distinction matters because B2B data decays at roughly 2-3% per month. A provider claiming 300 million contacts means little if 40% of those records haven't been reverified in over a year. The best providers refresh high-value segments (enterprise accounts, recently funded companies) more frequently than their long tail.",
        "why_it_matters": "Stale data wastes money and time in proportion to its age. A 90-day-old email list will have roughly 6-9% bad addresses. A year-old list could be 25-30% degraded. When you're paying per-contact for enrichment or per-email for outbound tools, freshness determines whether you're spending on active prospects or ghosts. Ask every provider how often they reverify and what percentage of their database was checked in the last 90 days.",
        "example": "Two enrichment providers both claim 95% email accuracy. Provider A reverifies their top 50 million records monthly and the rest quarterly. Provider B runs a full database reverification every 6 months. On a test of 1,000 records, Provider A delivers 91% valid emails while Provider B delivers 79%. The accuracy claim was technically true at the moment of verification, but freshness made the real-world difference.",
        "related_terms": ["data-decay", "data-validation", "data-enrichment", "data-completeness"],
        "related_tools": ["zoominfo", "cognism", "apollo", "clearbit"],
        "category_slug": "data-quality",
        "related_roundups": ["best-data-enrichment-tools", "best-data-quality-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    # --- CRM & Operations ---
    {
        "slug": "field-mapping",
        "term": "Field Mapping",
        "short_definition": "The process of connecting data fields between two systems so information syncs to the right place.",
        "meta_description": "What is field mapping? Connecting data fields between CRM, enrichment, and marketing tools. See mapping strategies, common pitfalls, and automation options.",
        "full_definition": "Field mapping defines how data moves between systems. When you integrate HubSpot with Salesforce, you need to specify that HubSpot's 'Company Name' maps to Salesforce's 'Account Name', HubSpot's 'Job Title' maps to Salesforce's 'Title', and so on. Simple mappings are one-to-one, but real-world scenarios include many-to-one (multiple source fields into a single target), transformations (converting date formats or picklist values), and conditional logic (map differently based on record type).",
        "why_it_matters": "Bad field mapping is the #1 cause of integration failures. Data ends up in wrong fields, overwriting good values with bad ones. The worst cases are silent failures where data maps to the wrong field without errors, so nobody notices until a sales rep calls a prospect and references completely wrong information. Getting field mapping right during initial setup saves hundreds of hours of cleanup later.",
        "example": "A company integrating Clay with Salesforce discovers that Clay's 'company_headcount' field returns ranges like '51-200' while Salesforce's 'Employees' field expects a number. They add a transformation rule that maps '51-200' to 125 (midpoint), '201-500' to 350, and so on, preventing the sync from breaking on data type mismatches.",
        "related_terms": ["crm-integration", "data-normalization", "ipaas", "data-orchestration"],
        "related_tools": ["zapier", "workato-ipaas", "mulesoft", "clay"],
        "category_slug": "data-quality",
        "related_roundups": ["best-data-integration-tools", "best-ipaas-integration-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "api-rate-limiting",
        "term": "API Rate Limiting",
        "short_definition": "Restrictions on how many API calls you can make to a service within a given time period.",
        "meta_description": "What is API rate limiting? How data tools restrict API calls per minute/hour. See rate limits by tool, strategies for staying under limits, and workarounds.",
        "full_definition": "API rate limiting controls how fast you can request data from a service. Most B2B data tools impose limits: Salesforce allows 100,000 API calls per 24 hours on Enterprise, HubSpot gives 500,000/day on Professional, and enrichment APIs like Clearbit cap at 600 requests/minute. Exceeding limits returns 429 (Too Many Requests) errors and can temporarily block your access. Rate limits exist to protect service stability, but they create real constraints when you're running bulk operations like mass enrichment or large CRM syncs.",
        "why_it_matters": "Rate limits determine what's operationally possible. If your enrichment provider limits you to 100 calls/minute, enriching 50,000 records takes over 8 hours. If your CRM limits daily API calls and you have three integrations competing for that budget, something breaks. Understanding rate limits before you buy prevents discovering your workflow is impossible after you've signed an annual contract.",
        "example": "A RevOps team builds a real-time enrichment flow: form submission triggers Zapier, which calls Clearbit, then writes to Salesforce. During a webinar with 2,000 registrations in 30 minutes, they hit Clearbit's rate limit at 600/min. The remaining 1,400 records queue up and enrich over the next 90 minutes instead of instantly. They switch to batch processing for high-volume events.",
        "related_terms": ["ipaas", "data-orchestration", "data-enrichment", "crm-integration"],
        "related_tools": ["zapier", "clay", "clearbit", "salesforce"],
        "category_slug": "orchestration",
        "related_roundups": ["best-data-integration-tools", "best-workflow-automation-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "lead-to-account-matching",
        "term": "Lead-to-Account Matching",
        "short_definition": "Automatically linking new leads to the correct existing account in your CRM.",
        "meta_description": "What is lead-to-account matching? Automatically linking inbound leads to existing CRM accounts. See matching strategies, tools, and ABM implications.",
        "full_definition": "Lead-to-account matching connects incoming leads to their parent company record in your CRM. When someone from Acme Corp fills out a form, the system should recognize they belong to an existing Acme Corp account and route them to the account owner rather than creating an orphan lead. Matching uses email domain, company name fuzzy matching, IP lookup, and enrichment data. Native CRM matching is rudimentary (exact email domain match only). Dedicated tools like LeanData and Chili Piper handle edge cases: personal email domains (gmail.com), subsidiaries, and multiple domains for the same company.",
        "why_it_matters": "Without lead-to-account matching, your ABM strategy falls apart. Leads from target accounts get routed to the wrong reps. Account-level engagement scores miss activity from unmatched leads. And your CRM fills up with orphan leads that nobody works because they're not attached to any account or territory. Companies with proper matching report 30-40% faster speed-to-lead on target accounts.",
        "example": "A target account, Stripe, has 400 employees who might interact with your content. Without matching, leads from stripe.com, stripe.dev, and personal Gmail addresses scatter across your CRM. LeanData matches all Stripe leads to the single account record and routes them to the named account executive within 5 minutes of form submission.",
        "related_terms": ["lead-routing", "abm", "lead-scoring", "account-scoring"],
        "related_tools": ["leandata", "chili-piper", "hubspot", "salesforce"],
        "category_slug": "abm",
        "related_roundups": ["best-lead-scoring-tools", "best-abm-platforms"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "custom-objects",
        "term": "Custom Objects",
        "short_definition": "User-defined data structures in your CRM that extend beyond the default contacts, companies, and deals.",
        "meta_description": "What are CRM custom objects? User-defined data structures beyond standard contacts and deals. See when to use them, CRM limits, and common patterns.",
        "full_definition": "Custom objects let you model data that doesn't fit standard CRM entities. Salesforce was built on this flexibility: you can create objects for anything (products, subscriptions, locations, partners, compliance records). HubSpot added custom objects in 2020 for Enterprise plans. Custom objects have their own fields, relationships, and automation triggers. They're the boundary line between a CRM that adapts to your business and one that forces your business into a fixed template.",
        "why_it_matters": "Every B2B company has data that doesn't fit neatly into contacts, companies, and deals. A SaaS company needs subscription objects. A channel-driven business needs partner objects. A multi-product company needs product-specific pipeline objects. Without custom objects, teams resort to cramming data into text fields, creating parallel spreadsheets, or building workarounds that break when the team scales. Custom object support (and its cost) should be a top-3 CRM evaluation criterion.",
        "example": "A B2B software company with three products creates custom 'Subscription' objects in Salesforce linked to Accounts. Each subscription tracks product, tier, ARR, renewal date, and usage metrics. This lets them build renewal pipeline reports, trigger automated health checks 90 days before renewal, and calculate net revenue retention by product line.",
        "related_terms": ["crm-integration", "crm-hygiene", "data-governance", "field-mapping"],
        "related_tools": ["salesforce", "hubspot", "dynamics-365", "zoho-crm"],
        "category_slug": "crm",
        "related_roundups": ["best-crm-for-enterprise", "best-crm-for-saas"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "sandbox-environment",
        "term": "Sandbox Environment",
        "short_definition": "A copy of your production CRM or tool where you can test changes without affecting live data.",
        "meta_description": "What is a CRM sandbox? A safe testing copy of your production environment. See which tools include sandboxes, costs, and when you need one.",
        "full_definition": "A sandbox is an isolated copy of your production system used for testing. You can build workflows, modify field layouts, test integrations, and run data imports without any risk to your live data. Salesforce includes sandboxes on Professional and above (Developer, Developer Pro, Partial Copy, Full Copy at different tiers). HubSpot added sandboxes for Enterprise in 2023. Most iPaaS tools and data integration platforms offer test/staging environments. The quality of your sandbox depends on whether it includes production data (anonymized or actual) or starts empty.",
        "why_it_matters": "Testing in production is how teams break their CRM on a Tuesday afternoon and spend the rest of the week in recovery mode. A workflow that accidentally reassigns 10,000 records. A data import that overwrites phone numbers with fax numbers. An integration change that stops lead routing. Sandboxes prevent these disasters. If your CRM vendor charges extra for sandboxes (HubSpot Enterprise pricing is the common example), factor that cost into your evaluation because operating without one is a matter of when, not if, something goes wrong.",
        "example": "Before deploying a new lead routing workflow that touches every inbound lead, a RevOps team clones their Salesforce configuration to a Full Copy sandbox. They run 500 test leads through the new routing rules, discover an edge case where leads from acquired companies route to the wrong team, fix it in the sandbox, and deploy to production with confidence.",
        "related_terms": ["crm-hygiene", "data-governance", "crm-integration", "custom-objects"],
        "related_tools": ["salesforce", "hubspot", "dynamics-365", "zoho-crm"],
        "category_slug": "crm",
        "related_roundups": ["best-crm-for-enterprise"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    # --- Intent & Signals ---
    {
        "slug": "topic-clustering",
        "term": "Topic Clustering (Intent)",
        "short_definition": "Grouping related search and content consumption behaviors into themes that indicate buying interest.",
        "meta_description": "What is topic clustering for intent data? Grouping B2B research behavior into buying signal categories. See how intent providers detect topics and limitations.",
        "full_definition": "Topic clustering in the context of intent data groups web activity into categories that indicate buying interest. When someone at a target account reads articles about 'CRM migration', 'Salesforce alternatives', and 'CRM implementation timeline', an intent provider clusters those signals under a 'CRM Evaluation' topic. Providers like Bombora track content consumption across their co-op network (5,000+ B2B publishers). 6sense and Demandbase combine third-party topics with first-party web activity for a more complete view. The accuracy of clustering depends on how granular the topics are: 'Data Enrichment' is more useful than 'Sales Technology'.",
        "why_it_matters": "Generic intent signals are noisy. Knowing that a company is 'researching sales tools' is too broad to act on. Topic clusters narrow the signal to something your SDR team can use in outreach. If the cluster maps to your specific product category ('data enrichment' when you sell enrichment tools), it becomes a prioritization signal that separates research-stage accounts from the 95% of your TAM that isn't looking yet.",
        "example": "A data enrichment vendor sets up topic clusters in 6sense: 'Data Enrichment', 'CRM Data Quality', 'B2B Contact Database', and 'Data Vendor Evaluation'. When an account spikes on 3+ topics simultaneously, it triggers an alert to the account owner with the specific topics, letting them tailor outreach to the research the prospect is already doing.",
        "related_terms": ["intent-data", "buyer-intent", "dark-funnel", "signal-based-selling"],
        "related_tools": ["6sense", "bombora", "demandbase", "zoominfo"],
        "category_slug": "intent",
        "related_roundups": ["best-b2b-intent-data-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "buying-group",
        "term": "Buying Group",
        "short_definition": "The collection of stakeholders within a target account who influence or make a purchase decision.",
        "meta_description": "What is a buying group? The B2B stakeholders involved in purchase decisions. See group mapping strategies, average sizes by deal type, and multi-threading tools.",
        "full_definition": "A buying group is every person involved in a B2B purchase decision. Gartner research puts the average B2B buying group at 6-10 people. Enterprise deals can involve 15-20. The group typically includes a champion (who wants the product), an economic buyer (who controls budget), technical evaluators, end users, and a procurement team. Most CRMs track individual contacts attached to opportunities, but don't natively model the buying group as a unit. ABM platforms and sales engagement tools are starting to fill this gap.",
        "why_it_matters": "Selling to one contact is single-threading, and it's how most deals stall or die. If your champion leaves, gets overruled, or can't build internal consensus, the deal disappears. Identifying and engaging the full buying group (multi-threading) increases win rates by 20-30% in most B2B segments. The shift from lead-based to account-based and now buying-group-based go-to-market reflects this reality.",
        "example": "A sales team pursuing a $200K deal maps the buying group in Salesforce: VP of Sales (champion), CFO (economic buyer), two Sales Managers (end users), IT Director (technical evaluator), and Procurement Lead. They create separate engagement plans for each person using Outreach sequences tailored to their role's concerns. When the VP of Sales leaves the company mid-deal, the two Sales Managers they've already built relationships with keep the evaluation alive.",
        "related_terms": ["multi-threading", "abm", "buying-committee", "account-scoring"],
        "related_tools": ["6sense", "demandbase", "salesforce", "outreach-io"],
        "category_slug": "abm",
        "related_roundups": ["best-abm-platforms", "best-sales-intelligence-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "signal-stacking",
        "term": "Signal Stacking",
        "short_definition": "Combining multiple buying signals from different sources to prioritize accounts more accurately than any single signal alone.",
        "meta_description": "What is signal stacking? Combining intent, engagement, firmographic, and hiring signals for account prioritization. See stacking strategies and tools.",
        "full_definition": "Signal stacking layers multiple data points to create a composite account priority score. Instead of relying on a single signal (intent data says they're researching your category), you combine it with hiring signals (they're posting jobs for roles that use your product), engagement signals (they've visited your pricing page 3 times), and firmographic signals (they match your ICP on size and industry). Each individual signal has a false positive rate of 30-50%. Stacking 3-4 signals together drops false positives dramatically.",
        "why_it_matters": "Any single buying signal is noisy. Intent data fires on competitors doing market research. Website visits could be job candidates browsing. Hiring signals lag actual need by months. But when an ICP account shows intent signals AND visits your pricing page AND is hiring the role that uses your product, that convergence is rare and highly predictive. Teams that stack signals report 2-3x higher conversion rates on outbound compared to single-signal targeting.",
        "example": "A sales team builds a signal stack in Clay: (1) Bombora intent surge on 'data enrichment' topics, (2) company posted a RevOps Director role on LinkedIn, (3) visited the pricing page in the last 14 days, (4) matches ICP (100-500 employees, B2B SaaS, North America). Accounts hitting 3 of 4 signals get routed to senior AEs. Accounts hitting 2 go into automated nurture sequences.",
        "related_terms": ["signal-based-selling", "intent-data", "lead-scoring", "account-scoring"],
        "related_tools": ["clay", "6sense", "common-room", "warmly"],
        "category_slug": "intent",
        "related_roundups": ["best-b2b-intent-data-tools", "best-sales-intelligence-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    # --- Enrichment & Waterfall ---
    {
        "slug": "credit-based-pricing",
        "term": "Credit-Based Pricing",
        "short_definition": "A pricing model where each data lookup, enrichment, or action consumes credits from a prepaid balance.",
        "meta_description": "What is credit-based pricing for data tools? Pay-per-lookup pricing models. See credit costs by provider, hidden gotchas, and how to estimate real spend.",
        "full_definition": "Credit-based pricing charges you per action rather than per seat or per month. Apollo charges 1 credit per email export and 5 per mobile number. ZoomInfo bundles credits into tiers that vary by contract. Clay charges per enrichment step in a workflow. The model sounds simple, but the math gets complicated: different actions cost different credit amounts, credits expire at year-end, usage varies by campaign, and providers count 'no result found' lookups against your balance too. Understanding your actual credit consumption patterns before signing a contract is worth more than any discount negotiation.",
        "why_it_matters": "Credit-based pricing can be the cheapest or most expensive model depending on your usage pattern. A team that runs a few hundred enrichments per month does well on credits. A team doing bulk list building burns through credits fast and pays more than they would on an unlimited seat license. The biggest trap is buying a large credit package for a volume discount, then discovering your team only uses 40% before they expire.",
        "example": "A startup evaluating Apollo and ZoomInfo calculates their monthly need: 2,000 email lookups and 500 mobile numbers. Apollo's $99/month plan includes 2,400 credits (enough for 2,000 emails + 80 mobiles). Getting 500 mobiles needs 2,500 additional credits. ZoomInfo's bundled plan at $15K/year includes unlimited lookups within their UI. The math favors ZoomInfo for heavy mobile number usage, Apollo for email-heavy workflows.",
        "related_terms": ["data-enrichment", "enrichment-waterfall", "match-rate", "b2b-data-providers"],
        "related_tools": ["apollo", "zoominfo", "clay", "cognism"],
        "category_slug": "enrichment",
        "related_roundups": ["best-data-enrichment-tools", "best-data-enrichment-tools-for-smb"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "email-verification",
        "term": "Email Verification",
        "short_definition": "Checking whether an email address is valid, deliverable, and safe to send to before you hit send.",
        "meta_description": "What is email verification? Validating B2B email addresses before sending. See verification methods, accuracy rates, and top tools for keeping bounce rates low.",
        "full_definition": "Email verification checks addresses through multiple layers: syntax validation (is the format correct), domain verification (does the domain exist and accept mail), mailbox verification (does this specific address exist on the server), and risk assessment (is it a catch-all domain, a role address like info@, or a known spam trap). Verification tools ping mail servers without sending actual emails. Accuracy ranges from 95-99% for major providers. The gap between 95% and 99% matters when you're sending thousands of emails because even 1% false negatives at scale means dozens of bounces.",
        "why_it_matters": "Every bounced email damages your sender reputation. Email providers like Google and Microsoft track bounce rates at the domain and IP level. Sustained bounce rates above 2% trigger spam filtering. Verification before sending is the simplest, cheapest protection for your deliverability infrastructure. At $0.003-0.01 per verification, it's negligible compared to the cost of rebuilding a burned domain.",
        "example": "Before launching a 15,000-contact cold email campaign, a sales team runs the list through NeverBounce. Results: 12,100 valid (80.7%), 1,900 invalid (12.7%), 600 catch-all/risky (4%), and 400 unknown (2.7%). They send to the 12,100 valid addresses and achieve a 0.8% bounce rate. Without verification, the 12.7% invalid addresses would have pushed bounce rate past acceptable thresholds.",
        "related_terms": ["bounce-rate-email", "email-deliverability", "data-validation", "data-freshness"],
        "related_tools": ["apollo", "instantly", "lemlist", "clearbit"],
        "category_slug": "validation",
        "related_roundups": ["best-data-validation-tools", "best-email-deliverability-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "catch-all-domain",
        "term": "Catch-All Domain",
        "short_definition": "An email domain configured to accept messages sent to any address, whether the specific mailbox exists or not.",
        "meta_description": "What is a catch-all email domain? Why B2B email verification can't confirm addresses on catch-all domains. See detection strategies and sending risks.",
        "full_definition": "A catch-all (or accept-all) domain is configured to receive email sent to any address at that domain, even if the specific mailbox doesn't exist. So test@catchall-company.com and fake123@catchall-company.com both get accepted. This makes email verification impossible for that domain because the server always says 'yes' regardless of the address. About 20-30% of B2B domains are configured as catch-all. Some companies do it intentionally (to capture mistyped addresses), others inherit the setting from their email provider's defaults.",
        "why_it_matters": "Catch-all domains are the gray zone of email outreach. Verification tools can't confirm whether the specific person's mailbox exists, only that the domain accepts everything. Sending to unverified addresses on catch-all domains carries risk: if the address doesn't route to a real inbox, it may silently fail (no bounce, no read), or it may eventually bounce when the company changes their email configuration. Best practice is to send to catch-all addresses cautiously and monitor bounce rates separately.",
        "example": "A sales team verifies 5,000 emails and gets 3,800 valid, 700 invalid, and 500 catch-all. They send to the 3,800 valid addresses immediately and set up a separate sending domain for the 500 catch-all addresses, monitoring bounce rates daily. If the catch-all batch stays under 3% bounce after the first send, they continue. If it spikes, they pull the batch before it damages their primary domain reputation.",
        "related_terms": ["email-verification", "bounce-rate-email", "email-deliverability", "data-validation"],
        "related_tools": ["instantly", "lemlist", "smartlead", "apollo"],
        "category_slug": "validation",
        "related_roundups": ["best-email-deliverability-tools", "best-cold-email-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    # --- Compliance & Privacy ---
    {
        "slug": "ccpa",
        "term": "CCPA (California Consumer Privacy Act)",
        "short_definition": "California's data privacy law giving residents the right to know what data companies collect and to request its deletion.",
        "meta_description": "What is CCPA? California's data privacy law for B2B. See how it affects sales prospecting, data providers, and compliance requirements for outbound teams.",
        "full_definition": "The CCPA (and its 2023 amendment, CPRA) gives California residents the right to know what personal data businesses collect, request deletion of that data, and opt out of its sale. For B2B teams, CCPA applies to business contacts because it covers 'consumers', defined broadly as California residents regardless of whether they're acting in a personal or business capacity. This means your prospect database containing California-based contacts falls under CCPA. Data providers like ZoomInfo and Apollo handle opt-out requests at scale, but the legal responsibility extends to any company using that data.",
        "why_it_matters": "CCPA violations carry penalties of $2,500 per unintentional violation and $7,500 per intentional one. Those numbers multiply fast when you're sending thousands of outbound emails. The practical impact for B2B teams: you need an opt-out mechanism for California contacts, your data providers should demonstrate CCPA compliance, and your privacy policy needs to disclose your data collection and sharing practices. Most companies handle this through their data provider's built-in compliance features, but you can't outsource the legal liability.",
        "example": "A SaaS company receives a CCPA deletion request from a California prospect. They need to delete the contact from Salesforce, Outreach sequences, marketing automation (HubSpot), and notify their enrichment provider (ZoomInfo) to suppress the record. They also need to confirm deletion within 45 days. Companies without a documented process for handling these requests scramble. Those with CRM automation and a deletion workflow complete it in hours.",
        "related_terms": ["gdpr", "data-privacy", "data-governance", "first-party-data"],
        "related_tools": ["zoominfo", "apollo", "cognism", "salesforce"],
        "category_slug": "data-quality",
        "related_roundups": [],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "consent-management",
        "term": "Consent Management",
        "short_definition": "Tracking and honoring prospect preferences for how their data is collected, stored, and used in outreach.",
        "meta_description": "What is consent management? Tracking B2B prospect data preferences and opt-outs. See consent requirements for outbound sales and recommended tools.",
        "full_definition": "Consent management tracks whether and how a prospect has agreed to receive communications. In B2B, this spans explicit consent (they filled out a form and checked a box), implicit consent (they're a customer or have an existing business relationship), and opt-outs (they clicked unsubscribe or submitted a GDPR/CCPA request). Managing consent across multiple tools (CRM, marketing automation, outbound sequences, enrichment providers) requires a centralized record, usually in the CRM, that all other tools respect. Getting this wrong means sending emails to people who've opted out, which violates regulations and burns your sender reputation.",
        "why_it_matters": "Consent isn't a checkbox exercise. Sending cold outbound to a GDPR-protected European contact without legitimate interest grounds can result in fines up to 4% of global revenue. Even in the US, CAN-SPAM requires honoring opt-outs within 10 business days. The real-world risk isn't usually massive fines for B2B companies. It's the operational damage: blacklisted domains, spam complaints that tank deliverability, and the trust cost of contacting people who explicitly said 'stop'. Building consent tracking into your data infrastructure from day one is significantly easier than retrofitting it later.",
        "example": "A company syncs consent status from HubSpot's subscription preferences to a custom field in Salesforce. When a prospect opts out of marketing emails, the field updates across both systems. Outreach sequences check this field before adding new contacts, and ZoomInfo enrichment skips opted-out records. The workflow handles 95% of consent cases automatically, with a quarterly manual audit catching edge cases.",
        "related_terms": ["gdpr", "ccpa", "data-privacy", "email-deliverability"],
        "related_tools": ["hubspot", "salesforce", "marketo", "dynamics-365"],
        "category_slug": "data-quality",
        "related_roundups": [],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    # --- Sales Process ---
    {
        "slug": "speed-to-lead",
        "term": "Speed to Lead",
        "short_definition": "The time between a prospect taking action (form fill, demo request) and a sales rep making first contact.",
        "meta_description": "What is speed to lead? Response time from form fill to sales contact. See benchmarks, why minutes matter, and tools that reduce response time.",
        "full_definition": "Speed to lead measures the gap between when a prospect raises their hand and when your team responds. Harvard Business Review research found that companies responding within 5 minutes are 100x more likely to connect than those responding within 30 minutes. Despite this, the average B2B response time is still 42 hours. The bottleneck is usually routing: the lead sits in a queue, gets assigned to a rep who's in a meeting, or routes to the wrong person because territory rules are outdated.",
        "why_it_matters": "By the time most companies respond to an inbound lead, the prospect has already moved on to evaluating a competitor who responded faster. Speed to lead is one of the few metrics where improvement has an immediate, measurable impact on pipeline. Reducing response time from 30 minutes to 5 minutes typically increases connection rates by 50-80%. And in competitive categories like CRM or data enrichment, the first vendor to get a demo scheduled often wins the evaluation.",
        "example": "A SaaS company installs Chili Piper on their demo request form. Instead of routing to a queue, the form immediately shows the assigned rep's calendar. The prospect books a time before they leave the page. Average speed to lead drops from 4.5 hours (manual routing through Salesforce assignment rules) to under 60 seconds (automated scheduling). Demo-to-opportunity conversion increases from 35% to 52%.",
        "related_terms": ["lead-routing", "lead-scoring", "sales-velocity", "pipeline-velocity"],
        "related_tools": ["chili-piper", "leandata", "hubspot", "salesforce"],
        "category_slug": "crm",
        "related_roundups": ["best-lead-scoring-tools", "best-sales-tools-for-startups"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "sales-tech-stack",
        "term": "Sales Tech Stack",
        "short_definition": "The collection of software tools a sales organization uses across prospecting, engagement, CRM, and analytics.",
        "meta_description": "What is a sales tech stack? The tools sales teams use for prospecting, CRM, engagement, and analytics. See stack examples by company size and budget.",
        "full_definition": "A sales tech stack is the combination of tools a sales team uses daily. A typical enterprise stack includes: a CRM (Salesforce, HubSpot), a sales engagement platform (Outreach, Salesloft), a data provider (ZoomInfo, Apollo), an intent data tool (6sense, Bombora), a conversation intelligence tool (Gong), and various point solutions for scheduling, routing, and analytics. The average enterprise sales team uses 10-15 tools. The average rep uses 5-6 daily. The stack grows organically as teams add tools for specific problems, which is how you end up with $200K/year in sales tech spending and reps who spend 30% of their time logging data across systems instead of selling.",
        "why_it_matters": "The right stack amplifies rep productivity. The wrong stack (or too many tools with overlapping functionality) creates data silos, workflow friction, and administrative overhead that slows everything down. The trend is toward consolidation: platforms like HubSpot and Apollo are adding features that replace point solutions, and orchestration tools like Clay let you chain multiple data sources without separate subscriptions. Evaluating your stack as a system (how do these tools work together?) matters more than evaluating any individual tool in isolation.",
        "example": "A 50-person sales team audits their stack and finds they're paying for Salesforce ($180K), Outreach ($65K), ZoomInfo ($50K), Gong ($45K), 6sense ($40K), Chili Piper ($12K), LeanData ($18K), and three point solutions ($25K combined). Total: $435K/year. They consolidate by replacing ZoomInfo + three point solutions with Apollo ($24K), saving $51K while maintaining 90% of the data coverage. The remaining savings fund a RevOps hire who optimizes the stack further.",
        "related_terms": ["revops", "sales-engagement", "sales-intelligence", "sales-ops-vs-revops"],
        "related_tools": ["salesforce", "hubspot", "outreach-io", "apollo"],
        "category_slug": "sales-engagement",
        "related_roundups": ["best-sales-tools-for-startups", "best-free-sales-tools", "best-revops-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "territory-management",
        "term": "Territory Management",
        "short_definition": "Dividing your total addressable market into segments assigned to specific sales reps or teams.",
        "meta_description": "What is territory management? Dividing accounts and leads among sales reps. See territory models, assignment tools, and common mistakes to avoid.",
        "full_definition": "Territory management assigns ownership of accounts and leads based on defined rules: geography, company size, industry vertical, named accounts, or round-robin. Good territory design balances opportunity across reps so nobody has too many or too few accounts to work effectively. Salesforce Enterprise includes Territory Management as a feature. Other CRMs require add-ons or custom configuration. The challenge isn't the initial setup, it's maintaining territories as your team grows, reps leave, and your ICP shifts. Quarterly territory rebalancing is standard at companies with 20+ reps.",
        "why_it_matters": "Unbalanced territories are the silent killer of sales performance. Rep A has 500 ICP accounts in a hot market and can't keep up. Rep B has 200 accounts in a slow segment and hits quota by accident in good quarters. Territory imbalance explains a surprising amount of quota attainment variance. Companies that invest in data-driven territory design (using firmographic data, intent signals, and historical conversion rates to size territories) consistently outperform those using geography-only models.",
        "example": "A 30-rep sales team segments territories by company size and industry instead of geography. Reps specialize in either mid-market (100-500 employees) or enterprise (500+), within one of four verticals: tech, healthcare, financial services, and manufacturing. Each territory contains roughly equal pipeline potential based on historical conversion rates and total addressable market in that segment. Top-performing reps consistently cite 'knowing my territory's problems deeply' as the reason they outperform.",
        "related_terms": ["lead-routing", "sales-territory-planning", "icp", "sales-pipeline"],
        "related_tools": ["salesforce", "hubspot", "leandata", "clari"],
        "category_slug": "crm",
        "related_roundups": ["best-crm-for-enterprise", "best-revops-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    # --- Analytics & Reporting ---
    {
        "slug": "cohort-analysis",
        "term": "Cohort Analysis",
        "short_definition": "Grouping accounts or contacts by a shared characteristic (signup month, source, segment) and tracking their behavior over time.",
        "meta_description": "What is cohort analysis in B2B? Tracking groups of accounts or contacts by shared traits over time. See use cases for sales, marketing, and customer success.",
        "full_definition": "Cohort analysis groups records by a common attribute (month they became a lead, acquisition channel, company size tier) and compares how each group performs over time. In B2B, common cohorts are monthly sign-up cohorts (do January leads convert differently from March leads?), source cohorts (do inbound leads have higher LTV than outbound?), and segment cohorts (do enterprise accounts retain better than mid-market?). The analysis reveals trends that aggregate metrics hide. Your overall conversion rate might look flat while one cohort improves 20% and another declines 30%.",
        "why_it_matters": "Aggregate metrics lie by averaging. If your Q1 leads convert at 25% and Q2 leads convert at 15%, your overall rate might show a stable 20%. Cohort analysis surfaces the drop immediately, letting you investigate what changed: did lead quality decline, did the sales process change, or did a market shift affect conversion? Revenue teams that run cohort analysis monthly catch problems 2-3 quarters earlier than those relying on aggregate dashboards.",
        "example": "A SaaS company runs monthly cohort analysis on customer retention. They discover January 2026 sign-ups have 30% higher churn than December 2025 sign-ups. Investigation reveals a January promotion attracted price-sensitive customers who cancel after the discount period. They adjust the promotion to require annual commitment and the next cohort's retention returns to baseline.",
        "related_terms": ["revenue-attribution", "net-revenue-retention", "churn-rate", "pipeline-velocity"],
        "related_tools": ["tableau", "looker", "power-bi", "clari"],
        "category_slug": "analytics",
        "related_roundups": ["best-analytics-for-sales-teams", "best-bi-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "win-loss-analysis",
        "term": "Win/Loss Analysis",
        "short_definition": "Systematically studying why deals were won or lost to improve sales strategy and product positioning.",
        "meta_description": "What is win/loss analysis? Studying closed deals to improve sales strategy. See frameworks, data sources, and how to turn losses into competitive intelligence.",
        "full_definition": "Win/loss analysis examines closed deals to identify patterns in why you win and why you lose. Quantitative analysis pulls from CRM data: win rate by segment, competitor, deal size, sales cycle length, and number of stakeholders involved. Qualitative analysis comes from structured interviews with buyers (both won and lost) to understand decision criteria, competitive positioning, and process friction. The combination reveals actionable patterns: 'We lose 70% of deals against Competitor X when the evaluation includes technical stakeholders' is specific enough to drive change.",
        "why_it_matters": "Most sales teams know their win rate but not their loss reasons at a granular level. Without win/loss analysis, you're guessing at what to fix. Is it pricing? Product gaps? Sales process? Competitive positioning? Each requires a different response, and investing in the wrong one wastes quarters of effort. Companies that run structured win/loss programs improve win rates by 15-30% within two quarters because they stop guessing and start fixing specific, documented problems.",
        "example": "A CRM vendor interviews 20 recent losses and discovers a pattern: they lose 80% of deals where the prospect's team has fewer than 3 people because their platform is too complex for small teams. They create a 'Quick Start' configuration, reduce required fields by 60%, and build a guided setup wizard. The next quarter, win rate in the under-5-person segment improves from 15% to 38%.",
        "related_terms": ["sales-forecasting", "revenue-intelligence", "conversation-intelligence", "pipeline-velocity"],
        "related_tools": ["gong-engage", "clari", "salesforce", "hubspot"],
        "category_slug": "sales-engagement",
        "related_roundups": ["best-revenue-intelligence-tools", "best-conversation-intelligence-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    # --- Integration & Automation ---
    {
        "slug": "webhook",
        "term": "Webhook",
        "short_definition": "An automated HTTP callback that sends data from one system to another when a specific event occurs.",
        "meta_description": "What is a webhook? Event-triggered data transfer between B2B tools. See webhook use cases for CRM, enrichment, and sales automation workflows.",
        "full_definition": "A webhook is a push-based integration method. Instead of polling an API repeatedly to check for changes, you configure a webhook URL and the source system sends data to it whenever an event occurs. 'New contact created in HubSpot' triggers a webhook to your enrichment tool. 'Deal stage changed to Closed Won' triggers a webhook to your billing system. Webhooks are faster than scheduled syncs (near-instant vs every 5-60 minutes) and more efficient (only fires when something happens). Most B2B tools support outbound webhooks; the receiving end typically requires Zapier, a custom endpoint, or an iPaaS tool.",
        "why_it_matters": "Webhooks enable real-time workflows that batch processing can't match. When a high-intent prospect fills out your demo form, a webhook-triggered flow can enrich the record, score it, route it, and notify the rep within seconds. The same flow on a 15-minute sync schedule means the rep gets notified after the prospect has closed the browser tab and moved on. In competitive sales cycles, minutes matter, and webhooks are what make sub-minute response times possible.",
        "example": "A company sets up a webhook flow: when a target account visits the pricing page (detected by Warmly), a webhook fires to Clay, which enriches the visitor with LinkedIn data and company info, then sends a Slack alert to the account owner with the enriched profile. The entire flow runs in under 10 seconds. The rep reaches out while the prospect is still evaluating.",
        "related_terms": ["ipaas", "api-rate-limiting", "data-orchestration", "sales-automation"],
        "related_tools": ["zapier", "n8n", "make", "clay"],
        "category_slug": "orchestration",
        "related_roundups": ["best-workflow-automation-tools", "best-ipaas-integration-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "batch-enrichment",
        "term": "Batch Enrichment",
        "short_definition": "Enriching a large set of records at once rather than one at a time through real-time API calls.",
        "meta_description": "What is batch enrichment? Bulk data enrichment for CRM databases. See batch vs real-time enrichment, costs, and when to use each approach.",
        "full_definition": "Batch enrichment processes records in bulk, typically by uploading a CSV or running a job against your CRM database. You send 10,000 contacts, the provider enriches them over minutes to hours, and you get back a file or sync with appended data. This contrasts with real-time enrichment, where each record is enriched individually as it enters your system (form fill, API call). Batch is cheaper per record and better for database-wide refreshes. Real-time is faster and better for inbound lead flows. Most teams use both: batch for quarterly CRM refreshes, real-time for new inbound leads.",
        "why_it_matters": "The choice between batch and real-time enrichment affects your budget, your data freshness, and your workflow design. Batch enrichment at $0.01-0.05/record lets you refresh your entire database quarterly for a fraction of what real-time would cost. But if an inbound lead waits 24 hours to be enriched, your lead scoring and routing run on incomplete data. The right answer is usually a hybrid approach: real-time for inbound (instant enrichment on form fill) and batch for maintenance (monthly or quarterly database refresh).",
        "example": "A company with 200,000 contacts in Salesforce runs quarterly batch enrichment through ZoomInfo. Each batch costs $4,000-8,000 depending on match rate and field coverage. Between batch runs, new inbound leads are enriched in real-time via a Clearbit API integration on their web forms. Total annual enrichment cost: $25,000 (4 batch runs + real-time credits). This keeps their database above 80% completeness year-round.",
        "related_terms": ["data-enrichment", "enrichment-waterfall", "match-rate", "credit-based-pricing"],
        "related_tools": ["zoominfo", "apollo", "clearbit", "clay"],
        "category_slug": "enrichment",
        "related_roundups": ["best-data-enrichment-tools", "best-data-quality-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "no-code-automation",
        "term": "No-Code Automation",
        "short_definition": "Building automated workflows between tools using visual interfaces instead of writing code.",
        "meta_description": "What is no-code automation? Building B2B workflows without code. See Zapier vs Make vs n8n, use cases for RevOps, and when you outgrow no-code.",
        "full_definition": "No-code automation tools let non-technical users build workflows between applications using drag-and-drop interfaces. Zapier, Make (formerly Integromat), and n8n are the main platforms. A typical workflow: 'When a new lead is created in HubSpot, look up the company in Clearbit, update the record with firmographic data, and notify the assigned rep in Slack.' No code required. These tools connect to 3,000+ applications and handle the API authentication, data transformation, and error handling behind a visual builder.",
        "why_it_matters": "RevOps and marketing ops teams don't have unlimited engineering resources. No-code automation lets them build and iterate on workflows in hours instead of waiting weeks for developer capacity. The trade-off is scale: no-code tools work for workflows running hundreds to thousands of times per month. When you need to process millions of records, handle complex error recovery, or maintain dozens of interconnected workflows, you'll outgrow basic no-code and need either an enterprise iPaaS (Workato, Tray) or custom code.",
        "example": "A RevOps team uses Make to automate their outbound enrichment: new prospects added to a Google Sheet trigger a Clay enrichment, results sync to HubSpot, and qualified leads (matching ICP criteria) automatically enter an Outreach sequence. The entire 5-step workflow took 3 hours to build in Make versus an estimated 2-week development sprint for a custom solution. It processes 200 records/day with no maintenance.",
        "related_terms": ["ipaas", "data-orchestration", "webhook", "sales-automation"],
        "related_tools": ["zapier", "make", "n8n", "clay"],
        "category_slug": "orchestration",
        "related_roundups": ["best-workflow-automation-tools", "best-ipaas-integration-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    # --- Market & Strategy ---
    {
        "slug": "competitive-displacement",
        "term": "Competitive Displacement",
        "short_definition": "Selling to prospects who already use a competitor's product, targeting their pain points for a switch.",
        "meta_description": "What is competitive displacement? Targeting accounts using a competitor's product. See displacement strategies, technographic data sources, and win rate benchmarks.",
        "full_definition": "Competitive displacement targets accounts that currently use a rival product. Instead of selling to greenfield accounts (no existing solution), you're convincing someone to switch. Displacement campaigns use technographic data (from providers like ZoomInfo, Clearbit, or BuiltWith) to identify which companies use which tools, then tailor messaging to the specific pain points of that competitor's product. Win rates on displacement deals are typically 15-25% lower than greenfield, but deal sizes are 20-40% larger because the buyer already has budget allocated.",
        "why_it_matters": "In mature B2B categories (CRM, enrichment, sales engagement), most of your total addressable market already uses something. If you only sell to greenfield accounts, you're limited to new companies and companies outgrowing their current tool. Displacement expands your addressable market by 3-5x. The key is specificity: 'You should switch to us' is weak. 'We know Competitor X doesn't support custom objects, and here's how that limits your RevOps team' is strong because it demonstrates understanding of their specific situation.",
        "example": "A CRM vendor identifies 2,000 companies using a competitor whose contract renewal cycle is Q4. Starting in Q3, they run a displacement campaign: SDRs reference specific pain points ('we hear your team struggles with X feature limitation'), offer a parallel proof-of-concept, and provide a migration playbook. They close 60 accounts (3% conversion) at an average deal size 35% above their typical greenfield deal because these are established buyers with existing budget.",
        "related_terms": ["technographic-data", "sales-intelligence", "total-addressable-market", "win-loss-analysis"],
        "related_tools": ["zoominfo", "clearbit", "6sense", "gong-engage"],
        "category_slug": "sales-engagement",
        "related_roundups": ["best-sales-intelligence-tools", "best-technographic-data-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "data-silo",
        "term": "Data Silo",
        "short_definition": "When data is trapped in one system and inaccessible to other teams or tools that need it.",
        "meta_description": "What is a data silo? When B2B data is trapped in one system. See common silos in sales orgs, costs of fragmentation, and integration strategies to fix them.",
        "full_definition": "A data silo exists when information is locked in one system and unavailable to other parts of the organization. Marketing has engagement data in HubSpot that sales can't see. Sales has conversation notes in Gong that customer success can't access. Finance has renewal data in their billing system that nobody else can query. The average B2B company has data fragmented across 10-20 tools, and most of those tools don't share information natively. Integration (through iPaaS, APIs, or platforms like Clay) is the solution, but most companies integrate their tools reactively, connecting them one at a time as problems arise rather than designing a connected data architecture upfront.",
        "why_it_matters": "Data silos cost revenue. Sales reps waste 5-8 hours per week searching for information across systems. Marketing sends campaigns to accounts that sales is already working, creating friction. Customer success misses churn signals because product usage data lives in a separate analytics tool. The compounding cost of fragmented data is estimated at 20-30% of a revenue team's productivity. Breaking silos through integration doesn't require one unified platform. It requires a data strategy that defines which systems are sources of truth for which data and how they share information.",
        "example": "A 100-person sales org uses Salesforce (CRM), Outreach (email), Gong (calls), ZoomInfo (data), and Slack (communication). None are natively connected. A rep preparing for a call has to check 4 tools to see the account's email engagement, last conversation notes, company data, and internal Slack threads. They build a unified view using Salesforce as the hub: Outreach syncs engagement data, Gong syncs call summaries, and ZoomInfo auto-enriches new records. Prep time drops from 15 minutes to 3 minutes per call.",
        "related_terms": ["data-orchestration", "ipaas", "crm-integration", "revops"],
        "related_tools": ["zapier", "workato-ipaas", "mulesoft", "salesforce"],
        "category_slug": "data-quality",
        "related_roundups": ["best-data-integration-tools", "best-revops-tools"],
        "date_published": TODAY,
        "date_modified": TODAY
    },
]


def main():
    path = DATA_DIR / "glossary.json"
    data = json.loads(path.read_text())
    existing_slugs = {t["slug"] for t in data["terms"]}

    added = 0
    skipped = 0
    for term in NEW_TERMS:
        if term["slug"] in existing_slugs:
            print(f"  SKIP (exists): {term['slug']}")
            skipped += 1
            continue
        data["terms"].append(term)
        existing_slugs.add(term["slug"])
        added += 1
        print(f"  ADD: {term['slug']}")

    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"\nDone: {added} added, {skipped} skipped. Total: {len(data['terms'])} terms.")


if __name__ == "__main__":
    main()
