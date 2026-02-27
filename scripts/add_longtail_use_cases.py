#!/usr/bin/env python3
"""Add 12 new long-tail use case pages targeting vertical/persona queries."""

import json
from pathlib import Path
from datetime import date

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TODAY = date.today().isoformat()

NEW_USE_CASES = [
    {
        "slug": "data-enrichment-for-financial-services",
        "title": "Data Enrichment for Financial Services Sales Teams",
        "meta_description": "Which data enrichment tools work for financial services. Compliance requirements, SOC 2 providers, and industry-specific data coverage compared.",
        "persona": "Financial services sales teams, FinTech companies selling to banks, insurance, and asset managers",
        "category_slug": "enrichment",
        "intro": "Financial services sales has a unique constraint: your data tools need to pass a compliance review before anyone evaluates features. Banks and insurance companies run vendor security assessments that can take 2-6 months. If your enrichment provider doesn't have SOC 2 Type II certification, the conversation ends before it starts.\n\nThe data needs are specific too. Financial services buying committees include roles you won't find in generic prospecting databases: Chief Risk Officers, Treasury Managers, Compliance Directors, and Heads of Commercial Lending. Coverage of these specialized titles varies dramatically between providers.\n\nThe regulatory environment adds another layer. GLBA (Gramm-Leach-Bliley Act) restricts how financial institutions share customer data, which affects what data you can store about bank contacts. Your enrichment provider's data sourcing practices need to align with your legal team's interpretation of applicable regulations.",
        "what_to_look_for": [
            {"criteria": "SOC 2 Type II certification", "why": "The minimum security certification for any tool touching financial services prospect data. Without it, your compliance team won't approve the vendor, regardless of data quality."},
            {"criteria": "Financial services title coverage", "why": "Generic databases are strong on VP Sales and Marketing Director. Financial services needs coverage of CRO (Chief Risk Officer), Treasury, Compliance, Commercial Banking, and Wealth Management titles. Ask providers for match rates on your specific target titles."},
            {"criteria": "Data residency options", "why": "Some financial institutions require that prospect data stays within specific geographic regions. Check whether the provider offers US-only or EU-only data storage if your compliance team requires it."},
            {"criteria": "Audit trail and access controls", "why": "Banks need to know who accessed what data and when. Look for tools with role-based access, export tracking, and audit logging that satisfies your information security team."}
        ],
        "recommended_tools": [
            {"slug": "zoominfo", "why": "Broadest adoption in financial services. SOC 2 Type II certified with enterprise security features. Strongest coverage of senior financial services titles. Track record of passing bank procurement reviews."},
            {"slug": "apollo", "why": "SOC 2 compliant at a fraction of ZoomInfo's cost. Financial services coverage is adequate for mid-market targets. Best option for FinTech startups that need compliant data without enterprise pricing."},
            {"slug": "salesforce", "why": "Financial Services Cloud includes industry-specific data modeling: households, financial accounts, advisor-client relationships. The CRM layer that purpose-built for how financial services sales teams work."},
            {"slug": "linkedin-sales-navigator", "why": "Relationship mapping is critical in financial services. Sales Navigator shows warm paths through existing connections, which matters more in relationship-driven FinServ sales than in product-led sales."}
        ],
        "bottom_line": "Start with the compliance review. Submit vendor security questionnaires to ZoomInfo and Apollo simultaneously (the process takes months). While waiting for approval, use LinkedIn Sales Navigator for prospecting (lower compliance friction since the data is publicly published). Once a data provider is approved, build your target account list with financial services-specific titles and run a test enrichment before committing to an annual contract.",
        "faq": [
            {"q": "Can I use general-purpose data tools for financial services?", "a": "Yes, if they pass compliance review. ZoomInfo and Apollo both have SOC 2 certification. The review process takes 2-6 months at large banks. Start early."},
            {"q": "Are there financial services-specific data providers?", "a": "A few, like RelPro and PitchBook (for investment banking). For general B2B financial services sales, ZoomInfo and Apollo provide the broadest coverage. Specialized providers are better for niche use cases (hedge fund contacts, insurance broker data)."},
            {"q": "What's the typical data budget for a FinServ sales team?", "a": "Mid-market teams spend $50K-$100K/year on data tools. Enterprise teams at major banks spend $200K-$500K+. FinTech startups can start with Apollo at $600-$1,400/year per user."}
        ],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "data-enrichment-for-manufacturing",
        "title": "Data Enrichment for Manufacturing Sales Teams",
        "meta_description": "Best data tools for manufacturing sales. Finding plant managers, procurement contacts, and operations leaders at manufacturers.",
        "persona": "Industrial and manufacturing sales teams, supply chain technology vendors",
        "category_slug": "enrichment",
        "intro": "Manufacturing sales is built on relationships that take years to develop. Plant managers, procurement directors, and operations VPs don't respond to generic cold emails. They respond to informed outreach from people who understand their specific production challenges, supply chain constraints, and technology environment.\n\nThe data challenge: manufacturing contacts are harder to find than tech company contacts. Plant managers aren't posting on LinkedIn daily. Procurement directors at mid-size manufacturers may not have a digital presence at all. The major data providers have their strongest coverage in technology and professional services; manufacturing coverage is thinner and requires validation.\n\nTechnographic data matters differently in manufacturing. Instead of SaaS stack detection, you need to know what ERP they run (SAP, Oracle, NetSuite), what MES system is in their plants, and whether they've adopted Industry 4.0 technologies. This data isn't in standard enrichment databases.",
        "what_to_look_for": [
            {"criteria": "Manufacturing title coverage", "why": "You need Plant Manager, VP Operations, Procurement Director, Quality Manager, and Supply Chain VP coverage. Test match rates on these titles specifically because generic providers optimize for Sales and Marketing contacts."},
            {"criteria": "SIC and NAICS code filtering", "why": "Manufacturing spans thousands of subsectors. You need to target specific manufacturing types: food processing, automotive parts, aerospace components. SIC/NAICS filtering is how you avoid spray-and-pray across all manufacturing."},
            {"criteria": "Company size accuracy for manufacturers", "why": "Employee count for manufacturers is harder to verify because it includes plant workers, not just office staff. Revenue data is more reliable for sizing manufacturers than headcount."},
            {"criteria": "Technographic data for industrial systems", "why": "Knowing what ERP, MES, or SCADA system a manufacturer runs helps qualify and personalize outreach. ZoomInfo and Clearbit offer some technographic coverage, but specialized providers like Enlyft or HG Insights go deeper."}
        ],
        "recommended_tools": [
            {"slug": "zoominfo", "why": "Broadest overall coverage, including manufacturing titles that smaller providers miss. The intent data layer can detect when manufacturers research specific technology categories."},
            {"slug": "apollo", "why": "Adequate manufacturing coverage at a much lower price point. The SIC/NAICS filtering works for basic manufacturing targeting. Best starting point for industrial sales teams on a budget."},
            {"slug": "linkedin-sales-navigator", "why": "The 'Manufacturing' industry filter combined with title targeting is the most reliable way to find operations and plant-level contacts. Many manufacturing professionals maintain LinkedIn profiles even if they're not active on the platform."},
            {"slug": "clearbit", "why": "Strong firmographic data including industry classification, employee count, and revenue estimates. Useful for enriching manufacturing account data rather than individual contact discovery."}
        ],
        "bottom_line": "Manufacturing sales teams should expect lower match rates than technology-sector teams. Run a sample enrichment of 200-500 manufacturing contacts through your top two provider candidates and compare match rates on your specific target titles before committing to an annual contract. Supplement data provider results with LinkedIn Sales Navigator for contacts that don't appear in databases.",
        "faq": [
            {"q": "Why is manufacturing data harder to find?", "a": "Manufacturing employees have lower digital presence than tech workers. Plant managers don't blog, tweet, or maintain active LinkedIn profiles at the same rate. Data providers that source from web scraping and social signals naturally have weaker coverage in industries with lower online activity."},
            {"q": "Are there manufacturing-specific data providers?", "a": "Thomas Net (thomasnet.com) is the largest manufacturing supplier directory. IndustryNet and MFG.com provide manufacturing company data. For contact-level enrichment, ZoomInfo and Apollo remain the best general options with their manufacturing filters."},
            {"q": "How should I target manufacturers by size?", "a": "Use revenue instead of employee count. A manufacturer with $50M revenue and 200 employees (mostly plant workers) is a different prospect than a SaaS company with the same revenue and 500 employees. Revenue is a better sizing proxy for manufacturing."}
        ],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "crm-for-real-estate-teams",
        "title": "CRM Tools for Real Estate Sales Teams",
        "meta_description": "Best CRM platforms for real estate teams. Contact management, deal tracking, and automation tools compared for brokerages and property tech companies.",
        "persona": "Real estate brokerages, commercial real estate teams, property technology companies",
        "category_slug": "crm",
        "intro": "Real estate CRM needs are different from standard B2B sales. Deals involve properties (not products), multiple parties per transaction (buyer, seller, agents, lawyers, lenders), and timelines measured in months. A CRM built for SaaS sales (Salesforce, HubSpot) can work, but it requires significant customization. Purpose-built real estate CRMs handle these patterns natively.\n\nThe choice depends on team size and specialization. A 5-agent residential brokerage needs something different from a 50-person commercial real estate firm. Residential needs fast lead response and drip campaigns. Commercial needs relationship tracking across long deal cycles and complex property portfolios.\n\nIntegration matters: MLS feeds, property databases, e-signature tools, and marketing platforms all need to connect to whatever CRM you choose. Native real estate integrations save months of custom development.",
        "what_to_look_for": [
            {"criteria": "Property-centric data model", "why": "Standard CRMs model contacts and deals. Real estate needs properties as a first-class entity: address, type, value, listing status, associated contacts. This is the difference between a CRM that works for real estate and one you're forcing to work."},
            {"criteria": "MLS integration", "why": "If your CRM can pull listing data from MLS, your agents don't have to manually enter property details. This saves hours per week per agent and keeps your data current with real-time listing changes."},
            {"criteria": "Multi-party transaction tracking", "why": "A real estate deal involves buyer, seller, buyer's agent, seller's agent, lender, attorney, and inspector. Your CRM needs to track all parties and their roles without creating a confusing mess of contacts associated with a single deal."},
            {"criteria": "Automated drip campaigns", "why": "Real estate lead nurturing is long (6-18 months for most buyers). Automated drip campaigns keep prospects warm without manual follow-up. The best real estate CRMs include templates designed for property market updates, new listing alerts, and seasonal check-ins."}
        ],
        "recommended_tools": [
            {"slug": "hubspot", "why": "The best general-purpose CRM option for real estate teams that want to grow beyond basic tools. Custom properties handle real estate data, marketing automation drives lead nurturing, and the free tier lets small brokerages start without cost."},
            {"slug": "salesforce", "why": "The enterprise option for large commercial real estate firms. Custom objects model properties, transactions, and multi-party deals. The AppExchange has real estate-specific packages. Overkill for small residential teams, essential for firms with 50+ agents."},
            {"slug": "pipedrive", "why": "Simple, visual deal pipeline that adapts well to real estate transaction stages. The contact and deal management works for small residential teams without the complexity of Salesforce. Integration with popular tools through Zapier."},
            {"slug": "freshsales", "why": "Affordable CRM with built-in phone, email, and chat. The AI-powered lead scoring helps agents prioritize high-intent buyers. Custom fields and pipelines adapt to real estate workflows without heavy configuration."}
        ],
        "bottom_line": "For residential brokerages under 20 agents, start with a real estate-specific CRM (Follow Up Boss, kvCORE, or LionDesk) that includes MLS integration and automated drip campaigns out of the box. For commercial real estate or large operations, Salesforce with a real estate package gives you the flexibility to model complex transactions. HubSpot sits in the middle: more capable than niche tools, less complex than Salesforce, and free to start.",
        "faq": [
            {"q": "Should I use a general CRM or a real estate-specific one?", "a": "Real estate-specific CRMs (Follow Up Boss, kvCORE) are better for residential agents because they include MLS integration and property-centric workflows. General CRMs (HubSpot, Salesforce) are better for commercial real estate and property tech companies that need custom data models and enterprise features."},
            {"q": "How much should a real estate team spend on CRM?", "a": "Residential: $20-$50/agent/month for basic CRM. Commercial: $75-$150/user/month for Salesforce-class tools. Free options (HubSpot) work for solo agents or small teams testing CRM for the first time."},
            {"q": "What's the most important CRM feature for real estate?", "a": "Speed to lead response. Real estate leads go cold in minutes. The CRM needs to notify agents immediately on new inquiries and ideally enable instant response (call back, text, or automated email) within 60 seconds."}
        ],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "data-tools-for-series-a-revops",
        "title": "Building Your RevOps Data Stack After Series A",
        "meta_description": "How to build a RevOps data stack after raising Series A. Tool recommendations, budget allocation, and common mistakes at the growth stage.",
        "persona": "First RevOps hire at Series A-B stage companies ($2M-$15M ARR)",
        "category_slug": "enrichment",
        "intro": "You just got hired as the first RevOps person at a company that closed their Series A. The CRM is a mess. Nobody owns the data. Sales reps are buying their own data tools on corporate cards. Marketing and sales aren't looking at the same numbers. Your job is to build the infrastructure that lets this company scale from 10 to 50 reps without the data falling apart.\n\nThe budget is real but finite. Your CEO approved $30K-$60K for your first-year tool stack. That's enough for a solid foundation, but not enough for the enterprise tools that companies 3x your size use. Every dollar needs to justify itself in pipeline impact.\n\nThe biggest mistake first RevOps hires make: buying too many tools at once. You don't need intent data when you have 8 reps. You don't need Clari when your CEO can review every deal in a 30-minute meeting. Start with the foundation (clean CRM + good data + reliable sequencing) and add layers as the team grows.",
        "what_to_look_for": [
            {"criteria": "CRM that scales from 10 to 50 users", "why": "You'll likely stay on your current CRM for 2-3 years. Choose one that handles your current team size without being overkill, but won't hit walls at 30-50 reps. HubSpot Professional or Salesforce Professional both work."},
            {"criteria": "Data provider with good mid-market coverage", "why": "Series A companies sell to mid-market (100-2,000 employees). Your data provider needs strong coverage in this segment. Test match rates on your specific ICP before committing to an annual contract."},
            {"criteria": "Integration reliability over feature count", "why": "At this stage, you don't have engineering support for custom integrations. Every tool needs to connect to your CRM with native or Zapier integration. Broken syncs create data problems that take weeks to untangle."},
            {"criteria": "Flexible pricing that grows with you", "why": "Avoid annual contracts with 3x usage estimates. You don't know your usage patterns yet. Monthly or quarterly billing with the ability to scale up (and down) matters more than getting the best per-unit price."}
        ],
        "recommended_tools": [
            {"slug": "hubspot", "why": "If you're not already on Salesforce, HubSpot Professional ($1,600/mo for Marketing + Sales + Service Hub bundle) gives you CRM, marketing automation, and basic operations in one platform. Less complex to manage solo than Salesforce."},
            {"slug": "salesforce", "why": "If you're already on Salesforce or your leadership insists on it, stay and invest in proper configuration. Salesforce Professional ($80/user/mo) handles 10-50 users. Budget $5K-$15K for a consultant to fix the setup."},
            {"slug": "apollo", "why": "Best data value for Series A budgets. Professional at $119/user/month gives your team prospecting + enrichment + sequences. For a 10-person sales team: $14,280/year. Compare to ZoomInfo at $30K+ for similar functionality."},
            {"slug": "zapier", "why": "Your integration layer until you can afford Workato or hire an engineer. Zapier Professional ($19/mo) connects your CRM, data tools, and communication channels. It's not perfect, but it's operational within an hour."}
        ],
        "bottom_line": "Allocate your first-year budget roughly: 40% CRM ($12K-$24K for HubSpot Professional or Salesforce + configuration), 30% data ($8K-$18K for Apollo or similar), 15% integration + automation ($3K-$6K for Zapier + other connectors), 15% reserve for tools you discover you need in months 3-6. Resist the urge to buy intent data, revenue intelligence, or advanced analytics in year one. Get the foundation right first.",
        "faq": [
            {"q": "Should I clean the CRM before buying new tools?", "a": "Yes. Spend your first 2-3 weeks auditing and cleaning the CRM before adding any new data. Enriching dirty records (duplicates, wrong titles, deceased contacts) wastes enrichment credits and creates more mess. Run DemandTools or manual dedup first."},
            {"q": "What tool should I buy first?", "a": "CRM configuration first (even if it means hiring a consultant for a week). Then data (Apollo or equivalent). Then integration (Zapier). Then everything else. The CRM is the foundation; if it's broken, nothing built on top works."},
            {"q": "When should I add intent data?", "a": "When you have 20+ reps and can't manually prioritize accounts effectively. At 10 reps, your sales manager can review accounts weekly. At 25+ reps across territories, intent data becomes the scalable way to prioritize. This typically happens 12-18 months after Series A for fast-growing companies."}
        ],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "data-cleaning-for-crm-migration",
        "title": "Data Cleaning Before a CRM Migration",
        "meta_description": "How to clean your data before migrating CRMs. Dedup, standardization, and enrichment steps that prevent carrying bad data into your new system.",
        "persona": "RevOps and ops teams preparing to migrate from one CRM to another",
        "category_slug": "cleaning",
        "intro": "CRM migrations are the one time your data gets a fresh start. Every record you move into the new system carries its problems with it: duplicates, outdated titles, wrong phone numbers, and standardization inconsistencies. Cleaning before migration is 10x easier than cleaning after, because you control the import process.\n\nMost migration projects underestimate data cleaning. The timeline typically runs: 2 weeks planned for data prep, 8 weeks actually spent. The scope creep comes from discovering how bad the data is once you start auditing. Twenty percent duplicates. Forty percent incomplete records. Picklist values with 15 variations of the same state name. Starting the cleanup early prevents it from becoming the bottleneck that delays your go-live.\n\nThe goal is to migrate clean, complete, standardized data so your team starts in the new CRM with a database they can trust from day one.",
        "what_to_look_for": [
            {"criteria": "Deduplication before export", "why": "Migrating duplicates into a new CRM doubles your problem. Dedup in the source system first, then export clean records. DemandTools (Salesforce) or Operations Hub (HubSpot) handle this."},
            {"criteria": "Field standardization", "why": "Before import, normalize every picklist: state abbreviations (California vs CA vs Calif.), country names, industry codes, and job title formats. Your new CRM's validation rules will reject inconsistent data."},
            {"criteria": "Enrichment to fill gaps", "why": "Migration is the ideal time to enrich. You're touching every record anyway. Run batch enrichment through Apollo or ZoomInfo to fill missing emails, phones, titles, and company data before import."},
            {"criteria": "Validation of contact data", "why": "Verify emails and phone numbers before loading into the new CRM. Why migrate 50,000 contacts when 15,000 of them have invalid emails? Start clean."}
        ],
        "recommended_tools": [
            {"slug": "demandtools", "why": "The gold standard for Salesforce data cleaning. Dedup, mass update, and import management. If you're migrating FROM Salesforce, use DemandTools to clean before export."},
            {"slug": "apollo", "why": "Batch enrichment to fill missing fields on your contact database. Run a bulk enrichment on the export file before importing into the new CRM."},
            {"slug": "clay", "why": "Build a custom cleaning workflow: standardize titles, validate emails, enrich missing fields, and flag records below a quality threshold, all in one pipeline before import."},
            {"slug": "hubspot", "why": "If you're migrating TO HubSpot, use Operations Hub's formatting automation to standardize data on import. Set up the rules before your first import so every record enters clean."}
        ],
        "bottom_line": "Budget 4-8 weeks for data cleaning before any CRM migration. The sequence: (1) audit your current data quality (duplicates, completeness, standardization), (2) dedup and standardize in the source system, (3) run batch enrichment on the export to fill gaps, (4) validate emails and phones, (5) import clean records into the new CRM with field mapping verified in a test import first.",
        "faq": [
            {"q": "How long does data cleaning for migration take?", "a": "Plan 4-8 weeks. Small databases (under 10,000 records) can be cleaned in 2-3 weeks. Large migrations (100K+ records) with significant data quality issues need 6-8 weeks. The timeline depends on how many duplicates and standardization issues exist."},
            {"q": "Should I enrich during or after migration?", "a": "During (before import). Enriching before migration means every record enters the new CRM with complete data. Enriching after migration means your team starts with incomplete records and has to work around gaps until the enrichment catches up."},
            {"q": "What records should I NOT migrate?", "a": "Don't migrate: contacts with no email AND no phone (unreachable), records that haven't been touched in 3+ years (likely decayed beyond recovery), obvious test records and internal contacts, and contacts who've opted out of all communication (migrate their suppression status, not their full record)."}
        ],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "visitor-identification-for-b2b",
        "title": "Website Visitor Identification for B2B Sales",
        "meta_description": "How to identify anonymous B2B website visitors. Tools, accuracy rates, and practical workflows for turning traffic into pipeline.",
        "persona": "Marketing and sales teams that want to convert anonymous website traffic into identified accounts and contacts",
        "category_slug": "visitor-identification",
        "intro": "97% of your website visitors leave without filling out a form. In B2B, that means potential buyers are researching your product, reading your pricing page, and comparing you to competitors, all anonymously. Visitor identification tools reverse this: they match anonymous traffic to companies and, in some cases, individual contacts.\n\nThe technology works by matching IP addresses to company databases, using browser fingerprinting combined with device graphs, or leveraging first-party cookies from ad networks. Accuracy varies: company-level identification typically matches 30-70% of B2B traffic, while individual contact identification matches 5-20%. The gap between company-level and person-level ID is where most buyer expectations diverge from reality.\n\nThe real value depends on what you do with identified visitors. Knowing that 'Acme Corp visited your pricing page' is useful only if that insight triggers a workflow: routing to the account owner, enriching the account, or starting an outbound sequence. Identification without action is just interesting data.",
        "what_to_look_for": [
            {"criteria": "Company vs person identification", "why": "Company-level ID (who works there) is mature and fairly accurate (30-70% match). Person-level ID (the specific individual) is newer and less reliable (5-20% match). Know which you're buying and set expectations accordingly."},
            {"criteria": "CRM and sequence tool integration", "why": "Visitor data needs to trigger action. The tool should push identified visitors to your CRM, alert account owners in Slack, or add contacts to sequences automatically. Without integration, you're checking a dashboard that nobody checks."},
            {"criteria": "Page-level activity tracking", "why": "Knowing a company visited your site is mildly useful. Knowing they visited your pricing page three times in a week and downloaded a case study is actionable. Look for page-level activity tracking, not just domain-level identification."},
            {"criteria": "Traffic volume requirements", "why": "Visitor identification tools have minimum traffic thresholds for effectiveness. Below 1,000 unique visitors per month, the identified visitor count may be too small to build workflows around. Check whether your traffic volume justifies the investment."}
        ],
        "recommended_tools": [
            {"slug": "warmly", "why": "Real-time visitor identification with automated outreach triggers. Identifies companies and individuals, then can trigger Slack alerts, CRM updates, and sequence enrollment. The most complete workflow from identification to action."},
            {"slug": "rb2b", "why": "Person-level identification using first-party identity resolution. Provides individual contact details (name, title, LinkedIn, email) for a portion of visitors. Best for teams that want to reach the specific person who visited, not just the company."},
            {"slug": "leadfeeder", "name": "Leadfeeder", "why": "Company-level identification with Google Analytics integration. Identifies which companies visit your site and which pages they view. Integrates with major CRMs for account-level activity tracking. More affordable than alternatives for company-level only."},
            {"slug": "6sense", "why": "Account identification combined with intent data. Goes beyond 'they visited your site' to 'they're also researching your category across the web.' The combination of first-party (website) and third-party (intent) signals provides the most complete picture."}
        ],
        "bottom_line": "Start with company-level identification (Leadfeeder or Warmly) and build a workflow: identified visitor on pricing page triggers account owner alert in Slack. Measure conversion rate from identified visitor to meeting. If the workflow produces pipeline, add person-level identification (RB2B) for higher-intent pages. Don't buy intent data (6sense) until you've proven that acting on visitor identification generates ROI.",
        "faq": [
            {"q": "Is website visitor identification legal?", "a": "Company-level identification (matching IP to company) is widely accepted. Person-level identification requires compliance with applicable privacy laws (CCPA, GDPR). US-focused B2B identification is generally compliant under existing law. European identification has stricter requirements. Consult your legal team for your specific use case."},
            {"q": "What percentage of visitors can be identified?", "a": "Company-level: 30-70% of B2B visitors (higher for enterprise traffic, lower for SMB). Person-level: 5-20% (depends heavily on the tool's identity graph). Consumer traffic (personal IPs, VPNs) cannot be identified."},
            {"q": "What website traffic volume do I need?", "a": "Below 500 unique B2B visitors per month, the number of identified visitors will be too small to build meaningful workflows. Between 500-2,000, company-level identification produces useful signals. Above 2,000, person-level identification and automated workflows become worthwhile."}
        ],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "data-stack-for-outbound-agencies",
        "title": "Data Stack for B2B Outbound Agencies",
        "meta_description": "How outbound sales agencies and lead gen firms build their data stacks. Multi-client tools, deliverability, and cost management.",
        "persona": "B2B outbound agencies, lead generation firms, and sales development companies running campaigns for multiple clients",
        "category_slug": "list-building",
        "intro": "Running outbound for multiple clients creates data challenges that in-house teams don't face. You need separate sending domains per client, flexible data sourcing that works across industries, and deliverability infrastructure that scales without burning any single client's reputation. The wrong tool choice multiplies across every client engagement.\n\nMargin pressure is real. Clients expect 'qualified meetings' at $200-$500 each. Your data costs need to stay under 10-15% of campaign revenue, which means enterprise pricing from ZoomInfo ($15K/year for one team) doesn't work when you're running 10 client campaigns. The economic model demands volume pricing or credit-based tools that flex across clients.\n\nThe deliverability stack is critical. One client's bad campaign can poison the infrastructure for all clients if sending domains and IP addresses aren't properly isolated. Agencies that invest in deliverability infrastructure outperform those that treat it as an afterthought.",
        "what_to_look_for": [
            {"criteria": "Multi-workspace or multi-client support", "why": "You need isolated data environments for each client. Look for tools with workspace separation, separate API keys, or team-level access controls that prevent data cross-contamination between clients."},
            {"criteria": "Credit-based pricing that pools across clients", "why": "Per-seat pricing multiplied by 10 clients gets expensive fast. Credit-based tools (Apollo credits, Clay credits) let you allocate from a shared pool to whichever client needs capacity in a given month."},
            {"criteria": "Multi-domain email infrastructure", "why": "Every client should send from their own domain (or dedicated agency domains per client). Your sending tool needs to manage 10-50+ sending domains with individual warmup and reputation tracking for each."},
            {"criteria": "Industry-agnostic data coverage", "why": "Your next client could sell to healthcare, manufacturing, or SaaS. Your data provider needs coverage across industries, not just tech. Test match rates on diverse segments before committing."}
        ],
        "recommended_tools": [
            {"slug": "apollo", "why": "Credit-based pricing with 275M+ contacts across industries. Multiple workspaces for client separation. The best balance of cost, coverage, and flexibility for agencies running 5-15 client campaigns simultaneously."},
            {"slug": "instantly", "why": "Purpose-built for multi-domain cold email. Unlimited mailbox connections, automated warmup across all accounts, and multi-domain management from a single dashboard. The agency plan supports 25,000+ emails/month with inbox rotation."},
            {"slug": "clay", "why": "Build reusable enrichment workflows that adapt to each client's ICP. The workflow template approach means you build the pipeline once and swap in different targeting criteria per client. Per-credit pricing pools across all client work."},
            {"slug": "smartlead", "why": "Alternative to Instantly for multi-inbox management. Unlimited mailbox connections with automated rotation. Some agencies prefer Smartlead's unified inbox for managing replies across all client campaigns in one view."}
        ],
        "bottom_line": "The agency data stack: Apollo (data, $49-$119/user/month) + Instantly or Smartlead (sending, $30-$94/month) + Clay (enrichment workflows, $149+/month). Total infrastructure cost for 10 client campaigns: $3,000-$5,000/month. Invest in sending domain hygiene: separate domains per client, minimum 2-week warmup before any campaign, and daily deliverability monitoring. Your sending reputation is your most valuable agency asset.",
        "faq": [
            {"q": "How many sending domains do I need per client?", "a": "Minimum 2-3 domains per client. This allows inbox rotation and provides redundancy if one domain gets flagged. Enterprise clients may require 5-10 domains for high-volume campaigns. Budget $10-$15/domain/year for registration plus email hosting."},
            {"q": "Should agencies use their own data tools or clients' tools?", "a": "Use your own. You need consistent workflows across clients, volume pricing that pools across engagements, and the ability to start new client campaigns immediately. Using client tools creates dependency, inconsistency, and onboarding delays."},
            {"q": "What data cost per meeting is normal for agencies?", "a": "Industry benchmark: $15-$40 in data and tool costs per qualified meeting. If you're spending more than $50 in data costs per meeting, your targeting or data quality needs work. At $200-$500/meeting client pricing, data costs should be 10-15% of revenue."}
        ],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "enrichment-for-product-led-growth",
        "title": "Data Enrichment for Product-Led Growth Companies",
        "meta_description": "How PLG companies use enrichment to qualify free users, trigger sales assist, and route high-value signups to reps. Tools and workflows compared.",
        "persona": "Growth and product teams at PLG companies that need to identify and route high-value free users to sales",
        "category_slug": "enrichment",
        "intro": "Product-led growth companies face a specific enrichment challenge: you have thousands of free signups, and somewhere in that pile are enterprise buyers who signed up with personal emails, gave fake company names, and look identical to individual hobbyists in your database.\n\nEnrichment is the bridge between self-serve signup and sales-assisted conversion. When a user signs up, real-time enrichment reveals: Is this a VP at a 2,000-person company (route to sales immediately) or a student building a side project (keep in self-serve)? The enrichment decision happens in seconds and determines whether a potential enterprise deal gets the attention it needs or dies in a free tier.\n\nThe workflow matters as much as the data. Enrichment needs to happen at signup (not in a nightly batch), route qualified signups to sales within minutes (not days), and update product usage data with firmographic context so your PQL scoring model has the signals it needs.",
        "what_to_look_for": [
            {"criteria": "Real-time enrichment API", "why": "Batch enrichment is too slow for PLG. When a VP of Engineering signs up for your free tier, your sales team needs to know within minutes, not tomorrow morning. Look for sub-second API response times and webhook-triggered enrichment."},
            {"criteria": "Email-to-company matching", "why": "50%+ of B2B signups use personal email addresses (Gmail, Yahoo). Your enrichment tool needs to match personal emails to companies through device graphs, IP lookup, or historical data. This is the hardest problem in PLG enrichment."},
            {"criteria": "PQL scoring integration", "why": "Enrichment data (company size, industry, title) combines with product usage data (features used, frequency, depth) to create Product Qualified Lead scores. Your enrichment tool needs to push data to wherever PQL scoring runs (CRM, CDP, or product analytics)."},
            {"criteria": "Volume pricing for free tier signups", "why": "PLG companies may have 10,000+ free signups per month. At $0.05-$0.10 per enrichment, that's $500-$1,000/month just for enrichment. Look for volume pricing or enrichment-on-match (only pay when data is found)."}
        ],
        "recommended_tools": [
            {"slug": "clearbit", "why": "The original PLG enrichment tool. Real-time API, email-to-company matching (including personal emails), and native integration with most product analytics and CRM tools. The Reveal feature identifies anonymous visitors before they even sign up."},
            {"slug": "apollo", "why": "API enrichment at a lower cost than Clearbit. The real-time lookup returns company and contact data for signup emails. Match rates on personal emails are lower than Clearbit, but the per-record cost makes it viable for high-volume free tier enrichment."},
            {"slug": "clay", "why": "Build a multi-source enrichment waterfall: try Clearbit first for company match, fall back to Apollo for contact data, then use LinkedIn lookup for personal emails. The waterfall approach maximizes match rates on the hardest cases (personal emails at enterprise companies)."},
            {"slug": "warmly", "why": "Identifies website visitors before signup using IP and device fingerprinting. Combined with signup enrichment, this gives your sales team two signals: which companies are browsing your product pages AND which employees have signed up for free accounts."}
        ],
        "bottom_line": "Build the enrichment into your signup flow, not as an afterthought. The architecture: user signs up, webhook triggers enrichment API, enriched data writes to CRM, PQL scoring runs against enrichment + usage data, and qualified signups route to sales within 5 minutes. The entire flow should be automated. The best PLG companies respond to high-value signups faster than their competitors respond to inbound demo requests.",
        "faq": [
            {"q": "What percentage of free signups can be enriched?", "a": "Work email signups: 70-85% enrichment rate. Personal email signups: 20-40% enrichment rate. The gap is the biggest challenge in PLG enrichment. Clearbit handles personal email matching better than most alternatives."},
            {"q": "How much should PLG enrichment cost?", "a": "Budget $0.03-$0.10 per signup for enrichment. At 10,000 signups/month, that's $300-$1,000/month. Only enrich signups where a match is found (most APIs charge on success, not attempt). The ROI calculation: if enrichment helps you identify and convert 5 enterprise accounts per month, $1,000 in enrichment costs generates $50K+ in pipeline."},
            {"q": "Should I enrich all free signups or just some?", "a": "Enrich all signups at the company level (it's cheap and fast). Only invest in deeper enrichment (phone numbers, org charts) for signups that match your ICP criteria. This two-tier approach keeps costs manageable at high signup volumes."}
        ],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "data-integration-for-bi-teams",
        "title": "Data Integration Tools for BI and Analytics Teams",
        "meta_description": "Best data integration tools for BI teams. ETL, ELT, and reverse ETL compared for connecting CRM, marketing, and sales data to your warehouse.",
        "persona": "BI teams, data analysts, and analytics engineers building reporting infrastructure",
        "category_slug": "ipaas",
        "intro": "Your BI team needs data from 10-20 sources in one place: CRM data from Salesforce, marketing data from HubSpot, ad spend from Google and LinkedIn, usage data from your product, and financial data from your billing system. The integration layer that moves this data into your warehouse is the unglamorous foundation that makes every dashboard and report possible.\n\nThe market has split into three approaches: ETL (extract, transform, load), ELT (extract, load, transform in-warehouse), and reverse ETL (push transformed data back to operational tools). Most teams need ELT for warehouse ingestion plus reverse ETL for activating insights. Traditional ETL tools are declining because modern cloud warehouses (Snowflake, BigQuery, Databricks) handle transformation better than pipeline tools.\n\nThe choice between tools comes down to: managed vs self-hosted (Fivetran vs Airbyte), connector coverage for your specific sources, and how much engineering time you have for maintenance. Managed tools cost more but eliminate pipeline ops. Self-hosted tools cost less but require engineering capacity.",
        "what_to_look_for": [
            {"criteria": "Connector coverage for your sources", "why": "Check that the tool has production-ready connectors for every data source you need. Having 300+ connectors means nothing if they don't include your specific CRM, marketing platform, or billing system. Test the specific connectors you'll use."},
            {"criteria": "Incremental sync support", "why": "Full syncs of large tables (millions of rows) are slow and expensive. Look for incremental sync that only moves changed records. This reduces warehouse compute costs and keeps data fresher with more frequent sync intervals."},
            {"criteria": "Schema change handling", "why": "When someone adds a custom field in Salesforce, does your integration tool detect the schema change and add the column, or does the pipeline break? Automatic schema evolution prevents the most common integration failures."},
            {"criteria": "Managed vs self-hosted", "why": "Fivetran and Airbyte Cloud are fully managed (no infrastructure to run). Airbyte Open Source is self-hosted (you run it on your servers). The managed option costs 2-5x more but eliminates pipeline ops. Choose based on whether you have engineering capacity for maintenance."}
        ],
        "recommended_tools": [
            {"slug": "fivetran", "why": "The market leader in managed ELT. 500+ pre-built connectors with automatic schema detection and incremental sync. Zero pipeline maintenance. The price (usage-based on monthly active rows) is higher than alternatives, but the reliability and connector quality justify it for teams without dedicated data engineers."},
            {"slug": "airbyte", "why": "Open-source alternative to Fivetran with 300+ connectors. Self-hosted option is free (you run it on your infrastructure). Cloud version is managed with per-connector pricing. Best for teams with engineering capacity that want to avoid Fivetran's pricing at scale."},
            {"slug": "census-data", "name": "Census", "why": "The leading reverse ETL tool. Pushes data from your warehouse back to operational tools: enriched segments to HubSpot, lead scores to Salesforce, usage metrics to Intercom. Essential for activating warehouse data in the tools your team actually uses."},
            {"slug": "hightouch", "why": "Reverse ETL alternative to Census. Pushes warehouse data to 140+ destinations. Audience building and segmentation features let marketing teams define segments in the warehouse and sync them to ad platforms, email tools, and CRM without writing SQL."}
        ],
        "bottom_line": "For most BI teams: Fivetran for warehouse ingestion (or Airbyte if you have engineering capacity) plus Census or Hightouch for reverse ETL. The combination handles the full data lifecycle: source systems to warehouse to operational tools. Budget $1,000-$5,000/month for Fivetran and $500-$2,000/month for reverse ETL, depending on data volumes and connector count.",
        "faq": [
            {"q": "What's the difference between ETL, ELT, and reverse ETL?", "a": "ETL transforms data before loading into the warehouse. ELT loads raw data first, then transforms in the warehouse (the modern standard). Reverse ETL pushes transformed data from the warehouse back to operational tools like CRM and marketing platforms."},
            {"q": "How much does data integration cost?", "a": "Fivetran: $1-$5/MAR (monthly active row) across connectors. A mid-size deployment (500K-2M MAR) runs $2,000-$8,000/month. Airbyte Cloud: per-connector pricing starting at $300-$500/month. Airbyte self-hosted: free (plus your infrastructure costs)."},
            {"q": "Do I need reverse ETL?", "a": "If your team builds reports in the warehouse but then manually exports CSVs to update CRM fields or marketing segments, you need reverse ETL. It automates the 'last mile' of analytics: pushing insights from dashboards into the tools where people work."}
        ],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "sales-engagement-for-mid-market",
        "title": "Sales Engagement Platforms for Mid-Market Teams",
        "meta_description": "Best sales engagement platforms for 10-50 rep teams. Outreach vs Salesloft vs Apollo compared on sequences, analytics, and pricing for mid-market budgets.",
        "persona": "Sales leaders and RevOps at mid-market companies (10-50 reps, $5M-$50M ARR)",
        "category_slug": "sales-engagement",
        "intro": "Your team outgrew manual email tracking. Reps are running 3-5 sequences simultaneously, managers need activity analytics, and your CRM data is suffering because reps log calls inconsistently. A sales engagement platform centralizes email, phone, and social outreach into managed workflows with automatic CRM logging.\n\nThe category is dominated by two enterprise players (Outreach and Salesloft) and one fast-growing challenger (Apollo, which bundles data + engagement). The enterprise tools cost $100-$150/user/month. Apollo costs $49-$119/user/month. The question for mid-market teams: does the extra $50-$100/user/month for Outreach or Salesloft deliver enough additional value over Apollo's integrated approach?\n\nThe answer depends on your sales motion. If reps run complex multi-channel sequences (email + phone + LinkedIn + tasks) and managers need granular analytics on rep performance, Outreach or Salesloft justify the premium. If your motion is primarily email-based outbound with some calling, Apollo's built-in sequences cover 80% of what you need at 40% of the cost.",
        "what_to_look_for": [
            {"criteria": "Sequence sophistication", "why": "Basic sequences (send email, wait, send email) work for simple outbound. Complex sequences (if email opened, then call; if not, LinkedIn connect; escalate to manager after 3 no-replies) need Outreach or Salesloft."},
            {"criteria": "CRM sync reliability", "why": "Every email sent, every call made, every meeting scheduled should log to CRM automatically. Test the sync with your specific CRM. Broken sync means reps either double-enter data or (more likely) stop logging entirely."},
            {"criteria": "Analytics depth", "why": "At 10+ reps, you need more than 'emails sent.' You need: sequence conversion rates by stage, rep performance comparisons, optimal send times, and A/B test results. This data drives coaching and sequence optimization."},
            {"criteria": "Per-user vs platform pricing", "why": "Outreach and Salesloft charge per user ($100-$150/user/month). Apollo charges per user ($49-$119) but includes data credits. For a 20-rep team, the annual difference is $24K-$48K. Make sure the premium features justify the premium price."}
        ],
        "recommended_tools": [
            {"slug": "outreach-io", "why": "The enterprise standard with the deepest sequence capabilities. Multi-channel automation, advanced A/B testing, sentiment analysis, and the most granular analytics in the category. 1,200+ job postings confirm it's the most demanded sales engagement skill."},
            {"slug": "salesloft", "why": "Comparable to Outreach with a slightly cleaner interface. The Cadence feature handles multi-channel sequences, and the Conversations feature records and analyzes calls. Some teams find Salesloft easier to admin and configure than Outreach."},
            {"slug": "apollo", "why": "Data + sequences in one platform at 40-60% less cost. Sequences are simpler than Outreach/Salesloft but handle email-based outbound well. The built-in data eliminates the need for a separate enrichment subscription, which changes the total cost comparison."},
            {"slug": "hubspot", "why": "If you're already on HubSpot Sales Hub Professional, sequences are included. They're less sophisticated than dedicated platforms, but they're free (within your existing subscription) and natively integrated with HubSpot CRM. Start here before adding another tool."}
        ],
        "bottom_line": "Try HubSpot sequences first if you're on HubSpot CRM (it's included). If you need more sophistication, evaluate Apollo Professional ($119/user/month, includes data) against Outreach ($100-$150/user/month, data separate). For a 20-rep team, Apollo saves $36K-$72K/year compared to Outreach + ZoomInfo. The premium tools justify their cost when you need complex multi-channel sequences, advanced analytics, and phone/social automation at the platform level.",
        "faq": [
            {"q": "Is Outreach or Salesloft better?", "a": "Feature parity is high. Outreach has a slight edge in analytics depth and AI features. Salesloft has a slight edge in usability and admin simplicity. Most teams choose based on which interface their reps prefer in a pilot. Pick whichever gets higher adoption in a 2-week trial."},
            {"q": "Can Apollo replace Outreach?", "a": "For email-based outbound, yes. For complex multi-channel sequences with phone, LinkedIn, and task automation, Apollo's sequencing is simpler than Outreach. The decision: do you need 100% of Outreach's features, or will 80% at 40% of the cost work for your team?"},
            {"q": "When should a mid-market team invest in sales engagement?", "a": "When you have 10+ reps and manual email tracking is creating inconsistency. Below 10 reps, HubSpot sequences or even Gmail + spreadsheet tracking can work. Above 10, you need platform-level analytics and CRM sync to maintain visibility and coaching capability."}
        ],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "intent-data-for-outbound-prospecting",
        "title": "Using Intent Data for Outbound Prospecting",
        "meta_description": "How to use B2B intent data for outbound sales. Signal types, vendor comparison, and practical workflows that turn intent into pipeline.",
        "persona": "SDR managers, outbound sales leaders, and demand gen teams evaluating intent data for prospecting",
        "category_slug": "intent",
        "intro": "Intent data promises to tell you which accounts are ready to buy before they fill out a form. The reality is more nuanced: intent signals are probabilistic, noisy, and require operational infrastructure to act on. When used well, intent data increases outbound conversion rates 2-3x. When used poorly, it's an expensive dashboard nobody checks.\n\nThe market splits into three signal types: third-party intent (Bombora, 6sense tracking content consumption across publisher networks), first-party intent (your website visitors, identified by tools like Warmly or Leadfeeder), and hiring intent (companies posting jobs for roles that use your product type). Each signal has different accuracy, freshness, and actionability.\n\nThe teams that get ROI from intent data have one thing in common: they built the workflow before they bought the data. 'What happens when an account shows intent?' needs a clear answer (who gets notified, what outreach starts, how quickly) before the data source matters.",
        "what_to_look_for": [
            {"criteria": "Signal freshness", "why": "Intent data decays fast. A buying signal from 30 days ago is old news. Look for weekly or daily signal updates. Monthly batch updates are too slow for outbound prospecting where timing matters."},
            {"criteria": "Topic granularity", "why": "'Researching sales technology' is too broad. 'Researching CRM migration' is actionable. The more specific the topic taxonomy, the more useful the signal for personalized outreach. Ask providers how many topics they track and how granular they get."},
            {"criteria": "CRM integration for workflow automation", "why": "Intent data needs to trigger actions: account owner alerts, sequence enrollment, lead score bumps. If the integration requires manual export/import, adoption will die within a month. Native CRM push is essential."},
            {"criteria": "Noise filtering and scoring", "why": "Raw intent signals fire on 20-30% of your TAM in any given week. Most are false positives (competitors researching, analysts writing reports, employees of your existing customers). Look for scoring that separates genuine buying interest from background noise."}
        ],
        "recommended_tools": [
            {"slug": "bombora", "why": "The largest intent data co-op (5,000+ B2B publishers). Standalone product that integrates with your existing CRM and tools. Best for teams that want intent data without committing to a full ABM platform like 6sense or Demandbase."},
            {"slug": "6sense", "why": "Combines third-party intent, first-party web activity, and AI-driven buying stage predictions. The most complete intent picture, but also the most expensive and complex to implement. Worth it for teams with dedicated ABM ops."},
            {"slug": "warmly", "why": "First-party intent (website visitor identification) is the highest-quality signal: someone at a target account is on your website right now. Warmly turns this into real-time alerts and automated outreach triggers."},
            {"slug": "common-room", "why": "Community and social intent signals: who's engaging with your open-source project, mentioning your category on Twitter, or asking questions on Stack Overflow. A different signal type that complements traditional content consumption intent."}
        ],
        "bottom_line": "Start with first-party intent (website visitor identification via Warmly or Leadfeeder) because it's the highest-fidelity signal and the cheapest to implement. Add third-party intent (Bombora or 6sense) once you've proven that acting on first-party signals generates pipeline. The workflow matters more than the data source: define what happens when intent fires before you buy the data.",
        "faq": [
            {"q": "Is intent data worth it for a small team?", "a": "Under 10 reps, probably not. Intent data requires ops capacity to configure, tune, and build workflows around. Small teams get better ROI from basic ICP targeting and good messaging. Intent data becomes worthwhile at 15-20+ reps when manual account prioritization breaks down."},
            {"q": "How accurate is intent data?", "a": "Expect 60-70% of high-intent accounts to be legitimate prospects when you reach out. The other 30-40% are competitors, analysts, employees of existing customers, or false positives. This is still 2-3x better than cold outbound without intent. Perfection isn't the benchmark; improvement over baseline is."},
            {"q": "What's the ROI timeline for intent data?", "a": "Plan 2-3 months to implement, tune, and build workflows. Expect measurable pipeline impact by month 4-6. Full ROI (the tool pays for itself in additional pipeline) typically takes 6-9 months. Teams that buy intent data expecting immediate results are usually disappointed. Teams that invest in the operational infrastructure see compounding returns."}
        ],
        "date_published": TODAY,
        "date_modified": TODAY
    },
    {
        "slug": "data-tools-for-recruiting-firms",
        "title": "Data Tools for Recruiting and Staffing Firms",
        "meta_description": "Best data and CRM tools for recruiting firms. Candidate sourcing, client prospecting, and ATS integration compared for staffing agencies.",
        "persona": "Recruiting firms, staffing agencies, and executive search firms that need tools for both candidate sourcing and client development",
        "category_slug": "list-building",
        "intro": "Recruiting firms have a double data problem: you need to find candidates AND find clients. Most B2B data tools focus on one side. LinkedIn is great for candidates but expensive for client prospecting at scale. CRM tools designed for sales don't model the candidate-client-job relationship that recruiting requires.\n\nThe tech stack for a recruiting firm looks different from a typical B2B sales stack. Your CRM needs to handle three entity types (candidates, clients, jobs) with many-to-many relationships. Your data tools need to source both candidate profiles and business development contacts. Your outreach tools need separate workflows for candidate sourcing and client sales.\n\nThe market is split between purpose-built recruiting tools (ATS/CRM combos like Bullhorn, Greenhouse, Lever) and general-purpose B2B tools adapted for recruiting. The right choice depends on whether you're a dedicated recruiting firm (purpose-built) or a company that does recruiting alongside other services (general-purpose with customization).",
        "what_to_look_for": [
            {"criteria": "Candidate AND client data sourcing", "why": "You need to find candidates (LinkedIn Recruiter, Indeed, GitHub) and prospect for client companies (Apollo, ZoomInfo). The data tool needs to handle both workflows or you need two separate tools."},
            {"criteria": "ATS/CRM integration", "why": "Candidate data needs to flow into your Applicant Tracking System. Client data needs to flow into your CRM. If these are separate systems (Bullhorn for candidates, HubSpot for clients), they need to sync. If it's one system (Bullhorn with CRM module), data management is simpler."},
            {"criteria": "Boolean search capability", "why": "Recruiting sourcing relies on complex Boolean searches across multiple databases. 'Java developer AND (AWS OR Azure) NOT junior NOT intern' style queries. Your data tools need to support this or integrate with tools that do."},
            {"criteria": "Candidate email and phone verification", "why": "Candidate data decays even faster than B2B data (people change jobs every 2-3 years, and that's the trigger event you're trying to capitalize on). Real-time verification prevents you from reaching out to numbers that don't work."}
        ],
        "recommended_tools": [
            {"slug": "linkedin-sales-navigator", "why": "The primary sourcing platform for both candidates and clients. Recruiter Lite ($170/month) or full Recruiter ($835/month) for candidate sourcing. Sales Navigator ($99-$169/month) for client business development. Most recruiting firms need both."},
            {"slug": "apollo", "why": "Client prospecting data at a fraction of ZoomInfo's price. Find hiring managers, VPs of Talent, and CHROs at target companies. The sequences feature works for both candidate outreach and client business development campaigns."},
            {"slug": "zoominfo", "why": "The broadest contact database for client prospecting. ZoomInfo's company data (headcount, revenue, funding, technology) helps qualify client prospects. The TalentOS product is purpose-built for recruiting sourcing."},
            {"slug": "hubspot", "why": "Free CRM for client relationship management. Custom objects can model candidates, jobs, and placements if you don't have a dedicated ATS. The marketing features handle client nurture campaigns and job marketing."}
        ],
        "bottom_line": "For small recruiting firms (under 10 recruiters): LinkedIn Recruiter Lite + Apollo (client prospecting) + HubSpot CRM (free). For mid-size firms: LinkedIn Recruiter + purpose-built ATS (Bullhorn, Loxo) + Apollo or ZoomInfo (client data). The biggest ROI comes from separating candidate sourcing workflows from client BD workflows and using the right tool for each side.",
        "faq": [
            {"q": "Should recruiting firms use LinkedIn Recruiter or Sales Navigator?", "a": "Both, for different purposes. Recruiter for candidate sourcing (InMail credits, applicant tracking, candidate search filters). Sales Navigator for client business development (company insights, lead lists, warm introduction paths). Most firms buy both."},
            {"q": "What CRM should a recruiting firm use?", "a": "Purpose-built ATS/CRM combos (Bullhorn, Loxo, Recruiter Flow) for firms focused exclusively on recruiting. General-purpose CRM (HubSpot, Salesforce) for firms that do recruiting plus other services, or for very small firms that want a free starting point."},
            {"q": "How do recruiting firms verify candidate contact data?", "a": "LinkedIn InMail for initial contact, then verify email and phone through Apollo or Lusha. Candidate contact data changes with job changes, so verify within 30 days of any outreach. Stale candidate data (older than 6 months) should be re-verified before use."}
        ],
        "date_published": TODAY,
        "date_modified": TODAY
    },
]


def main():
    path = DATA_DIR / "use_cases.json"
    data = json.loads(path.read_text())
    existing_slugs = {uc["slug"] for uc in data["use_cases"]}

    added = 0
    skipped = 0
    for uc in NEW_USE_CASES:
        if uc["slug"] in existing_slugs:
            print(f"  SKIP (exists): {uc['slug']}")
            skipped += 1
            continue
        data["use_cases"].append(uc)
        existing_slugs.add(uc["slug"])
        added += 1
        print(f"  ADD: {uc['slug']}")

    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"\nDone: {added} added, {skipped} skipped. Total: {len(data['use_cases'])} use cases.")


if __name__ == "__main__":
    main()
