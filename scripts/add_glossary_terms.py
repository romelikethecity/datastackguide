#!/usr/bin/env python3
"""Add 18 new glossary terms to glossary.json."""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

NEW_TERMS = [
    {
        "slug": "demand-generation",
        "term": "Demand Generation",
        "short_definition": "The set of marketing activities designed to create awareness and interest in a product before buyers enter the sales pipeline.",
        "meta_description": "What is demand generation? Marketing activities that build awareness and pipeline before buyers raise their hand. See demand gen tools and strategies.",
        "full_definition": "Demand generation covers everything from content marketing and paid campaigns to webinars, events, and ABM programs. Unlike lead generation, which focuses on capturing contact information, demand gen aims to create genuine interest and educate potential buyers before they're ready to talk to sales. It operates across the entire funnel, from brand awareness at the top to pipeline acceleration at the bottom.",
        "why_it_matters": "B2B buying cycles are getting longer and more complex. Companies that only run lead capture campaigns miss the 95% of their market that isn't actively buying today. Demand generation builds familiarity and trust so that when prospects do enter a buying cycle, your brand is already on their shortlist.",
        "example": "A data enrichment vendor publishes a quarterly report on B2B data decay rates, promotes it through LinkedIn and paid search, and runs a webinar series on data hygiene best practices. None of these directly ask for a demo request, but they build category expertise and brand recognition.",
        "related_terms": ["lead-scoring", "abm", "mql-sql", "buyer-journey"],
        "related_tools": ["marketo", "hubspot-marketing-hub", "6sense"],
        "category_slug": "marketing-automation",
        "related_roundups": ["best-marketing-automation-platforms"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "marketing-ops",
        "term": "Marketing Operations (MOps)",
        "short_definition": "The function responsible for marketing technology, data, processes, and reporting infrastructure.",
        "meta_description": "What is marketing operations (MOps)? The team behind marketing tech stacks, data management, and campaign infrastructure. See MOps tools and trends.",
        "full_definition": "Marketing operations manages the systems and processes that make marketing campaigns work at scale. This includes marketing automation platforms, data integrations, lead routing rules, attribution models, campaign tracking, and reporting dashboards. MOps teams own the marketing tech stack and ensure data flows correctly between tools like CRMs, CDPs, email platforms, and analytics systems.",
        "why_it_matters": "As marketing tech stacks grow more complex (the average enterprise uses 90+ marketing tools), someone needs to keep everything connected and running. MOps prevents data silos, ensures lead handoffs work, maintains reporting accuracy, and enables marketing teams to execute campaigns without breaking integrations or losing data.",
        "example": "When a new lead fills out a form on your website, MOps ensures the record is enriched with firmographic data, scored against your ICP model, routed to the right sales rep based on territory rules, and attributed to the correct campaign in your reporting dashboard.",
        "related_terms": ["revops", "sales-ops-vs-revops", "data-orchestration", "marketing-attribution"],
        "related_tools": ["marketo", "hubspot-marketing-hub", "salesforce"],
        "category_slug": "marketing-automation",
        "related_roundups": ["best-marketing-automation-platforms"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "lead-generation",
        "term": "Lead Generation",
        "short_definition": "The process of identifying and capturing contact information from potential buyers who match your target market.",
        "meta_description": "What is lead generation? Identifying and capturing B2B prospect data through outbound, inbound, and data provider channels. See lead gen tools and data.",
        "full_definition": "Lead generation produces a list of contacts or companies that could become customers. In B2B, this happens through three main channels: inbound (content, SEO, paid ads that drive form fills), outbound (cold email, cold calling, LinkedIn outreach using prospecting databases), and third-party data (purchasing contact lists from providers like ZoomInfo, Apollo, or Cognism). The quality of leads depends heavily on how well they match your ideal customer profile.",
        "why_it_matters": "Without leads, there's no pipeline. But lead volume alone is meaningless if the leads don't convert. The shift in B2B is from maximizing lead count to maximizing lead quality, which means better targeting, better data, and tighter alignment between the criteria marketing uses to capture leads and the criteria sales uses to qualify them.",
        "example": "An SDR team uses Apollo to build a list of 500 VP-level contacts at SaaS companies with 200-1,000 employees. They enrich the list with verified emails and direct dials, then load it into Outreach for a multi-step email and call sequence.",
        "related_terms": ["icp", "mql-sql", "lead-scoring", "outbound-prospecting"],
        "related_tools": ["apollo", "zoominfo", "cognism", "leadiq"],
        "category_slug": "list-building",
        "related_roundups": ["best-lead-generation-tools", "best-b2b-prospecting-tools"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "b2b-data-providers",
        "term": "B2B Data Providers",
        "short_definition": "Companies that sell business contact and company data used for sales prospecting, enrichment, and market research.",
        "meta_description": "What are B2B data providers? Companies selling contact, company, and intent data for sales and marketing. Compare providers and accuracy rates.",
        "full_definition": "B2B data providers maintain databases of business contacts, company information, and buying signals. The major providers include ZoomInfo (largest database, 300M+ contacts), Apollo (strongest free tier), Cognism (best European mobile coverage), and Clearbit (API-first enrichment). Data types include contact info (email, phone, title), firmographics (revenue, employee count, industry), technographics (software used), and intent signals. Accuracy varies significantly between providers, typically ranging from 60-90% for emails and 40-70% for direct dial phone numbers.",
        "why_it_matters": "Your sales team's effectiveness is directly tied to data quality. Inaccurate emails mean bounces that hurt deliverability. Wrong phone numbers waste calling time. Outdated titles mean irrelevant messaging. Choosing the right data provider for your market (by geography, company size, and industry) has more impact on pipeline than almost any other sales tool decision.",
        "example": "A company selling to European mid-market evaluates three providers. ZoomInfo has the largest US database but weaker European mobile numbers. Cognism has GDPR-compliant European mobiles with 87% connect rates. Apollo offers the best value with a generous free tier but lower overall accuracy. They choose Cognism for European prospecting and Apollo for US outbound.",
        "related_terms": ["data-enrichment", "firmographic-data", "technographic-data", "direct-dial"],
        "related_tools": ["zoominfo", "apollo", "cognism", "clearbit"],
        "category_slug": "enrichment",
        "related_roundups": ["best-data-enrichment-tools", "best-b2b-contact-databases"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "data-decay",
        "term": "Data Decay",
        "short_definition": "The rate at which contact and company data in your CRM becomes inaccurate over time due to job changes, company moves, and market shifts.",
        "meta_description": "What is data decay? The rate B2B data becomes stale from job changes and company shifts. Learn decay rates, costs, and how to combat it.",
        "full_definition": "Data decay is the natural degradation of CRM and database accuracy over time. People change jobs (average tenure is 2-3 years), companies get acquired, phone numbers change, and email addresses stop working. Industry research suggests 25-30% of B2B contact data decays annually, meaning a CRM with no enrichment process loses a quarter of its accuracy every year. The decay rate is higher for certain fields (direct dials decay faster than work emails) and certain industries (tech has higher turnover than healthcare).",
        "why_it_matters": "Decayed data doesn't just sit there quietly. It actively costs money: bounced emails hurt your sender reputation, wrong phone numbers waste SDR time, outdated titles lead to irrelevant pitches, and bad data in your CRM corrupts lead scoring and reporting. The compounding effect means that without regular data maintenance, your CRM becomes progressively less useful.",
        "example": "A company with 100,000 contacts in Salesforce and no enrichment process loses roughly 25,000 accurate records per year. After two years, nearly half their database is unreliable. Running a quarterly enrichment cycle through ZoomInfo or Clearbit catches most changes before they compound.",
        "related_terms": ["data-hygiene", "crm-hygiene", "data-validation", "data-enrichment"],
        "related_tools": ["zoominfo", "clearbit", "demandtools"],
        "category_slug": "cleaning",
        "related_roundups": ["best-crm-data-cleaning-tools"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "ipaas",
        "term": "iPaaS (Integration Platform as a Service)",
        "short_definition": "A cloud-based platform that connects applications, automates workflows, and synchronizes data between different software systems.",
        "meta_description": "What is iPaaS? Cloud integration platforms connecting apps and automating B2B data workflows. Compare Workato, MuleSoft, Tray, and alternatives.",
        "full_definition": "iPaaS platforms provide a centralized way to build integrations between SaaS applications, on-premise systems, and databases without writing custom code for each connection. Enterprise iPaaS tools like Workato and MuleSoft handle complex multi-step workflows, data transformations, error handling, and API management. Lighter-weight tools like Zapier and Tray focus on simpler trigger-action automations. The distinction matters: Zapier connects two apps in one step, while Workato can orchestrate a 15-step process across six systems with conditional logic and data mapping.",
        "why_it_matters": "The average B2B company uses 100+ SaaS tools. Without iPaaS, data lives in silos and teams spend hours on manual data entry and CSV exports. iPaaS platforms automate the data flow between your CRM, marketing automation, enrichment tools, and analytics platforms. The ROI comes from eliminating manual work and ensuring data consistency across systems.",
        "example": "When a new deal closes in Salesforce, Workato automatically provisions the customer in your billing system, creates an onboarding project in Monday.com, adds the contact to a customer nurture campaign in Marketo, and updates the revenue dashboard in Tableau.",
        "related_terms": ["data-orchestration", "etl", "reverse-etl", "crm-integration"],
        "related_tools": ["workato-ipaas", "mulesoft", "tray", "celigo"],
        "category_slug": "orchestration",
        "related_roundups": ["best-data-orchestration-tools", "best-workflow-automation-tools"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "web-visitor-identification",
        "term": "Website Visitor Identification",
        "short_definition": "Technology that identifies which companies or individuals visit your website without them filling out a form.",
        "meta_description": "What is website visitor identification? Tools that reveal anonymous B2B visitors. Compare IP-based vs pixel-based identification and top tools.",
        "full_definition": "Website visitor identification tools match anonymous web traffic to known companies and, in some cases, individual contacts. There are two main approaches: IP-based identification (matching visitor IP addresses to company databases, used by Leadfeeder and 6sense) and pixel-based identification (using ad network cookies and device graphs to identify individuals, used by RB2B and Warmly). IP-based tools typically identify 20-30% of visitors at the company level. Pixel-based tools can identify individual people but have lower match rates and face increasing privacy restrictions.",
        "why_it_matters": "Roughly 98% of website visitors leave without filling out a form. Visitor identification recovers some of that dark funnel by telling sales teams which companies are actively looking at your website. This data can trigger real-time alerts, feed into ABM campaigns, or prioritize accounts in your CRM based on website engagement signals.",
        "example": "Warmly detects that three employees from a target account visited your pricing page and integration docs in the same week. It pushes an alert to the assigned account executive with the visitors' names, titles, and the pages they viewed, enabling a timely and relevant outreach.",
        "related_terms": ["dark-funnel", "buyer-intent", "intent-data", "first-party-data"],
        "related_tools": ["warmly", "rb2b", "leadfeeder", "6sense"],
        "category_slug": "intent",
        "related_roundups": ["best-b2b-intent-data-tools", "best-website-visitor-identification-tools"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "sales-dialer",
        "term": "Sales Dialer (Power Dialer)",
        "short_definition": "Software that automates phone dialing for sales teams, increasing the number of conversations reps can have per hour.",
        "meta_description": "What is a sales dialer? Automated calling software for B2B sales teams. Compare power dialers, parallel dialers, and AI-powered options.",
        "full_definition": "Sales dialers automate the mechanical parts of outbound calling: dialing numbers, leaving voicemails, logging calls, and advancing through call lists. Power dialers call one number at a time automatically. Parallel dialers (like Orum and Nooks) dial multiple numbers simultaneously and connect reps only when someone answers, dramatically increasing live conversation rates. AI-powered dialers can also detect voicemail vs. live answer, drop pre-recorded voicemails, and transcribe conversations for coaching.",
        "why_it_matters": "Manual dialing wastes 60-70% of an SDR's phone time on ringing, voicemails, and wrong numbers. A parallel dialer can increase live conversations from 8-12 per hour to 25-40 per hour. For teams where phone is a primary channel, that productivity gain directly translates to more pipeline generated per rep.",
        "example": "An SDR team of 10 switches from manual dialing to Orum's parallel dialer. Each rep goes from 12 live conversations per day to 35. Monthly pipeline generation increases by 180% with the same headcount because reps spend their time talking instead of waiting for someone to pick up.",
        "related_terms": ["sales-engagement", "sales-cadence", "sales-automation", "outbound-prospecting"],
        "related_tools": ["orum", "nooks"],
        "category_slug": "sales-engagement",
        "related_roundups": ["best-sales-dialer-tools", "best-sales-engagement-tools"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "ai-sales-tools",
        "term": "AI Sales Tools",
        "short_definition": "Sales software that uses artificial intelligence to automate research, personalize outreach, analyze conversations, or predict deal outcomes.",
        "meta_description": "What are AI sales tools? Software using AI to automate prospecting, personalize outreach, and predict pipeline. See top AI sales tools and trends.",
        "full_definition": "AI sales tools apply machine learning and large language models to sales workflows. Categories include: AI research agents (Clay, which pulls data from 50+ sources and synthesizes it per prospect), conversation intelligence (Gong, which records and analyzes sales calls), predictive forecasting (Clari, which uses engagement data to predict deal outcomes), and AI-powered outreach (tools that generate personalized email copy at scale). The common thread is replacing manual work with automated intelligence.",
        "why_it_matters": "Sales teams spend roughly 65% of their time on non-selling activities: researching prospects, updating CRMs, writing emails, and preparing for calls. AI tools automate the research and writing while providing intelligence that helps reps prioritize the right accounts and say the right things. The impact is measurable: teams using AI-powered tools report 20-40% increases in pipeline per rep.",
        "example": "Before a call, Clay automatically researches the prospect's company, recent news, tech stack, and hiring patterns, then generates a personalized talk track. After the call, Gong transcribes and analyzes the conversation, flagging follow-up items and coaching opportunities.",
        "related_terms": ["sales-intelligence", "conversation-intelligence", "signal-based-selling", "sales-automation"],
        "related_tools": ["clay", "gong-engage", "clari"],
        "category_slug": "enrichment",
        "related_roundups": ["best-ai-sales-tools", "best-data-enrichment-tools"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "data-normalization",
        "term": "Data Normalization",
        "short_definition": "The process of standardizing data formats, values, and structures across records to enable consistent reporting and analysis.",
        "meta_description": "What is data normalization? Standardizing CRM data formats for accurate reporting. Learn normalization techniques and tools for B2B sales data.",
        "full_definition": "Data normalization transforms inconsistent data into a standard format. In B2B contexts, this means standardizing company names ('IBM' vs 'International Business Machines' vs 'ibm corp'), job titles ('VP Sales' vs 'Vice President of Sales' vs 'VP, Sales'), phone number formats, state/country codes, and industry classifications. It also covers deduplication (matching records that refer to the same entity) and enrichment-driven standardization (replacing free-text fields with structured data from a reference database).",
        "why_it_matters": "Unnormalized data breaks everything downstream. Your territory assignment rules fail when 'California' and 'CA' and 'Calif.' are treated as different states. Lead routing breaks when job titles aren't standardized. Reports show inflated account counts when the same company appears under three different name variations. Normalization is the unglamorous foundation that makes CRM data actually usable.",
        "example": "DemandTools scans 50,000 Salesforce accounts and finds 3,200 duplicate pairs based on fuzzy name matching and domain comparison. It merges them into unique records, standardizes state abbreviations, and normalizes phone numbers to E.164 format.",
        "related_terms": ["data-deduplication", "data-hygiene", "crm-hygiene", "data-validation"],
        "related_tools": ["demandtools", "zoominfo", "clearbit"],
        "category_slug": "cleaning",
        "related_roundups": ["best-crm-data-cleaning-tools"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "direct-dial",
        "term": "Direct Dial",
        "short_definition": "A phone number that connects directly to a specific person's desk or mobile, bypassing the company switchboard or receptionist.",
        "meta_description": "What is a direct dial in B2B sales? Phone numbers that reach prospects directly. Compare direct dial accuracy across data providers.",
        "full_definition": "Direct dials are the most valuable phone data type in B2B sales because they bypass gatekeepers and connect reps directly to the prospect. Sources include corporate directories, published business records, data partnerships, and phone verification services. Mobile numbers are increasingly categorized as direct dials since remote work has made desk phones less relevant. Accuracy rates vary significantly: ZoomInfo reports 70%+ accuracy on verified direct dials, while lower-tier providers may deliver 40-50% connect rates.",
        "why_it_matters": "The difference between having and not having a direct dial is stark. Cold calls through a company switchboard connect to the target roughly 5% of the time. Direct dials connect 30-50% of the time. For SDR teams making 50+ calls per day, that's the difference between 2-3 conversations and 15-25 conversations. Direct dial coverage is often the deciding factor when companies choose between data providers.",
        "example": "An SDR team switches from ZoomInfo (strong US direct dials) to Cognism for their European territory because Cognism's mobile-verified European numbers connect at 2.5x the rate. Their European pipeline increases by 60% in the first quarter.",
        "related_terms": ["b2b-data-providers", "data-enrichment", "outbound-prospecting", "sales-dialer"],
        "related_tools": ["zoominfo", "cognism", "apollo", "seamless-ai"],
        "category_slug": "enrichment",
        "related_roundups": ["best-b2b-contact-databases", "best-data-enrichment-tools"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "buyer-persona",
        "term": "Buyer Persona",
        "short_definition": "A semi-fictional profile of your ideal buyer based on job title, responsibilities, pain points, and buying behavior.",
        "meta_description": "What is a buyer persona? A profile of your ideal B2B buyer based on role, pain points, and behavior. Learn how personas drive targeting and messaging.",
        "full_definition": "Buyer personas define who you're selling to within a target account. While your ideal customer profile (ICP) defines the right companies, buyer personas define the right people at those companies. A typical B2B sale involves 6-10 decision makers, each with different priorities: the VP of Sales cares about pipeline velocity, the CTO cares about integration complexity, and the CFO cares about total cost of ownership. Effective personas are built from actual customer interviews, CRM data analysis, and win/loss reviews, not from marketing brainstorms.",
        "why_it_matters": "Generic messaging fails because different buyers in the same deal care about completely different things. When your SDR team, marketing campaigns, and content strategy all target well-defined personas, conversion rates increase because prospects receive relevant information for their specific role and concerns.",
        "example": "A sales intelligence vendor defines three buyer personas: the VP of Sales (cares about pipeline generation and rep productivity), the RevOps Manager (cares about data accuracy and integration with existing tech stack), and the CRO (cares about ROI metrics and competitive differentiation). Each persona gets different email sequences, landing pages, and case studies.",
        "related_terms": ["icp", "buying-committee", "lead-scoring", "abm"],
        "related_tools": ["6sense", "clearbit", "hubspot-marketing-hub"],
        "category_slug": "abm",
        "related_roundups": ["best-abm-platforms"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "revenue-intelligence",
        "term": "Revenue Intelligence",
        "short_definition": "Software that captures and analyzes sales activity data to provide visibility into pipeline health, deal risk, and forecast accuracy.",
        "meta_description": "What is revenue intelligence? Software analyzing sales data for pipeline visibility and forecast accuracy. Compare Gong, Clari, and alternatives.",
        "full_definition": "Revenue intelligence platforms aggregate data from emails, calls, meetings, CRM updates, and other sales activities to build a complete picture of what's happening in your pipeline. Unlike CRM data (which depends on reps manually updating fields), revenue intelligence captures engagement signals automatically. Key capabilities include deal inspection (which deals are at risk), forecast accuracy (how likely you are to hit your number), and coaching insights (what top reps do differently).",
        "why_it_matters": "Sales forecasts are notoriously inaccurate because they rely on reps' subjective assessments of deal health. Revenue intelligence replaces guesswork with data: email response rates, meeting frequency, stakeholder engagement, and conversation sentiment all factor into deal scores. Companies using revenue intelligence report 15-25% improvements in forecast accuracy.",
        "example": "Clari's deal inspection shows that a $200K opportunity has had no executive engagement in three weeks, the champion hasn't responded to the last two emails, and the close date has been pushed twice. The platform flags it as high-risk despite the rep marking it as 'commit' in the CRM.",
        "related_terms": ["sales-forecasting", "conversation-intelligence", "sales-pipeline", "sales-velocity"],
        "related_tools": ["clari", "gong-engage"],
        "category_slug": "sales-engagement",
        "related_roundups": ["best-revenue-intelligence-tools", "best-sales-engagement-tools"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "customer-health-score",
        "term": "Customer Health Score",
        "short_definition": "A composite metric that predicts customer retention or churn risk based on usage, engagement, and satisfaction signals.",
        "meta_description": "What is a customer health score? A predictive metric for retention and churn risk. Learn scoring models, signals, and tools like Gainsight.",
        "full_definition": "Customer health scores combine multiple signals into a single indicator of account health. Common inputs include product usage (login frequency, feature adoption, depth of use), support interactions (ticket volume, sentiment, time to resolution), engagement (email opens, webinar attendance, community participation), contract details (renewal date, expansion potential), and NPS/survey responses. Scores are typically displayed as red/yellow/green or as a numeric scale, with thresholds triggering automated playbooks for at-risk accounts.",
        "why_it_matters": "By the time a customer says they want to cancel, it's usually too late. Health scores provide early warning by detecting declining engagement patterns weeks or months before churn. They also help customer success teams prioritize their time: instead of checking in equally with all accounts, they focus on accounts showing warning signs or expansion opportunities.",
        "example": "Gainsight calculates a health score for each account based on daily active users (weighted 40%), support ticket sentiment (20%), feature adoption breadth (20%), and executive sponsor engagement (20%). An account drops from green to yellow when DAU falls 30% over two weeks, triggering an automated CS outreach sequence.",
        "related_terms": ["churn-rate", "net-revenue-retention", "arr-mrr"],
        "related_tools": ["gainsight"],
        "category_slug": "customer-success",
        "related_roundups": ["best-customer-engagement-platforms"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "total-addressable-market",
        "term": "Total Addressable Market (TAM)",
        "short_definition": "The total revenue opportunity available if you captured 100% of the market for your product or service.",
        "meta_description": "What is total addressable market (TAM)? How to calculate TAM for B2B sales and use data tools to size your market. See TAM tools and methods.",
        "full_definition": "TAM represents the entire potential market for your product. In B2B, it's typically calculated using one of three methods: top-down (industry reports and analyst data), bottom-up (count of potential customers multiplied by average deal size), or value theory (estimated value your product delivers). Related metrics include SAM (serviceable addressable market, the portion you can reach) and SOM (serviceable obtainable market, what you can realistically capture). Data tools like ZoomInfo and Definitive Healthcare allow bottom-up TAM calculation using firmographic filters.",
        "why_it_matters": "TAM analysis drives strategic decisions: market entry, pricing, territory planning, and fundraising. Sales teams use TAM data to build target account lists and size territories fairly. Investors evaluate TAM to assess growth potential. Getting TAM right prevents two common mistakes: overestimating the market (leading to unrealistic projections) and underestimating it (leaving money on the table).",
        "example": "A sales intelligence startup targets VP-level buyers at B2B SaaS companies with 100-5,000 employees in the US. Using ZoomInfo's firmographic database, they count 14,200 companies matching their ICP. At an average deal size of $24,000/year, their bottom-up TAM is $341M.",
        "related_terms": ["icp", "firmographic-data", "sales-territory-planning", "account-scoring"],
        "related_tools": ["zoominfo", "definitive-healthcare", "clearbit"],
        "category_slug": "enrichment",
        "related_roundups": ["best-data-enrichment-tools", "best-b2b-contact-databases"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "outbound-prospecting",
        "term": "Outbound Prospecting",
        "short_definition": "The proactive process of reaching out to potential buyers through cold email, cold calling, and social selling.",
        "meta_description": "What is outbound prospecting? Proactive outreach to B2B buyers via email, phone, and LinkedIn. See outbound tools, strategies, and benchmarks.",
        "full_definition": "Outbound prospecting is the sales-driven approach to generating pipeline by reaching out to prospects who haven't expressed interest. It involves four steps: building a target list (using tools like Apollo, ZoomInfo, or LinkedIn Sales Navigator), researching accounts (identifying relevant pain points and triggers), crafting personalized outreach (email sequences, call scripts, LinkedIn messages), and managing multi-touch cadences (coordinating email, phone, and social touches over days or weeks). Modern outbound stacks typically combine a data provider, a sales engagement platform, and a dialer.",
        "why_it_matters": "Inbound marketing alone can't sustain most B2B companies' growth targets. Outbound prospecting gives sales teams control over pipeline generation, especially for upmarket motions where target accounts may not be searching for your category. It's also the fastest way to enter new markets or verticals where you have no brand awareness.",
        "example": "An SDR uses Apollo to build a list of 200 RevOps directors at mid-market SaaS companies, loads them into Outreach with a 14-day sequence (3 emails, 2 calls, 1 LinkedIn touch), and uses Orum's parallel dialer for the phone steps. The sequence generates 18 meetings from 200 prospects (9% conversion).",
        "related_terms": ["sales-cadence", "sales-engagement", "cold-email", "lead-generation"],
        "related_tools": ["apollo", "outreach", "salesloft", "orum"],
        "category_slug": "list-building",
        "related_roundups": ["best-b2b-prospecting-tools", "best-lead-generation-tools"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "crm-integration",
        "term": "CRM Integration",
        "short_definition": "Connecting your CRM to other sales, marketing, and data tools so that information flows automatically between systems.",
        "meta_description": "What is CRM integration? Connecting Salesforce, HubSpot, or Pipedrive to your tech stack. See integration tools, methods, and common pitfalls.",
        "full_definition": "CRM integration covers three approaches: native integrations (built-in connectors between vendors, like HubSpot's Salesforce sync), iPaaS platforms (Workato, Zapier, or Tray automating data flows between any two systems), and custom API integrations (code written to your CRM's REST API). Key integration patterns include bi-directional sync (CRM data flows both ways), enrichment push (data providers write to CRM records), activity logging (sales engagement platforms push email/call data to CRM), and reporting pull (analytics tools read CRM data).",
        "why_it_matters": "A CRM that doesn't connect to your other tools becomes a data entry burden that reps avoid. When integrations work properly, enrichment data flows in automatically, sales activity is logged without manual effort, marketing engagement is visible on the contact record, and reports reflect the full picture. When they break, you get data silos, stale records, and reps toggling between ten tabs.",
        "example": "A RevOps team integrates Salesforce with ZoomInfo (enrichment push), Outreach (activity sync), Gong (call recording attachment), Marketo (lead sync), and Tableau (reporting pull). Workato orchestrates the most complex flows, while native integrations handle the simpler connections.",
        "related_terms": ["ipaas", "data-orchestration", "revops", "etl"],
        "related_tools": ["salesforce", "hubspot-marketing-hub", "workato-ipaas", "zapier"],
        "category_slug": "orchestration",
        "related_roundups": ["best-data-orchestration-tools", "best-workflow-automation-tools"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    },
    {
        "slug": "enrichment-waterfall",
        "term": "Enrichment Waterfall Strategy",
        "short_definition": "A multi-provider enrichment approach that queries data sources in sequence, using the next provider only when the previous one returns no result.",
        "meta_description": "What is an enrichment waterfall? A multi-provider strategy to maximize data coverage. Learn how to build a waterfall with Clay, ZoomInfo, and others.",
        "full_definition": "An enrichment waterfall queries multiple data providers in a prioritized sequence to maximize coverage while controlling costs. For example, you might first check Clearbit (cheapest per lookup), then Apollo (broader coverage), then ZoomInfo (highest accuracy but most expensive). Each provider is only queried if the previous one didn't return a result for that specific field. This approach can increase email coverage from 60-70% (single provider) to 85-95% (three providers in waterfall). Tools like Clay have built-in waterfall logic, or you can build your own using Workato or custom scripts.",
        "why_it_matters": "No single data provider has 100% coverage. ZoomInfo might have 80% of your target contacts, but the missing 20% could be your best prospects. A waterfall approach fills those gaps by tapping multiple sources. The economics work because you only pay the expensive providers for records the cheaper ones miss, keeping per-record costs down while maximizing hit rates.",
        "example": "A waterfall for email enrichment: Step 1: Check Clearbit ($0.05/lookup, 65% hit rate). Step 2: For misses, check Apollo ($0.03/lookup, catches 15% more). Step 3: For remaining misses, check ZoomInfo ($0.15/lookup, catches another 10%). Total coverage: 90% at an average cost of $0.07/record instead of $0.15/record if you'd used ZoomInfo for everything.",
        "related_terms": ["waterfall-enrichment", "data-enrichment", "b2b-data-providers"],
        "related_tools": ["clay", "zoominfo", "clearbit", "apollo"],
        "category_slug": "enrichment",
        "related_roundups": ["best-data-enrichment-tools"],
        "date_published": "2026-02-15",
        "date_modified": "2026-02-15"
    }
]


def main():
    glossary_path = DATA_DIR / "glossary.json"
    with open(glossary_path) as f:
        data = json.load(f)

    existing_slugs = {t["slug"] for t in data["terms"]}
    added = 0

    for term in NEW_TERMS:
        if term["slug"] in existing_slugs:
            print(f"  SKIP {term['slug']} (already exists)")
            continue
        data["terms"].append(term)
        existing_slugs.add(term["slug"])
        print(f"  + {term['slug']}")
        added += 1

    with open(glossary_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"\nGlossary terms added: {added}")
    print(f"Total glossary terms now: {len(data['terms'])}")
    print(f"\nWritten to {glossary_path}")


if __name__ == "__main__":
    main()
