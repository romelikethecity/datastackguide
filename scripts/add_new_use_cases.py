#!/usr/bin/env python3
"""
Add 10 new persona-based use case pages to data/use_cases.json.

New use cases:
1. customer-success-for-saas (customer-success)
2. sales-enablement-for-enterprise (sales-engagement)
3. analytics-for-revenue-teams (bi-analytics)
4. crm-for-agencies (crm)
5. lead-routing-for-high-volume (sales-engagement)
6. enrichment-for-abm (enrichment)
7. conversation-intelligence-for-coaching (conversation-intelligence)
8. marketing-automation-for-enterprise (marketing-automation)
9. data-integration-for-warehouses (ipaas)
10. review-management-for-vendors (review-platforms)
"""
import json
import sys

DATA = "/Users/rome/Documents/projects/datastackguide/data"


def load(name):
    with open(f"{DATA}/{name}") as f:
        return json.load(f)


def save(name, data):
    with open(f"{DATA}/{name}", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


VALID_TOOL_SLUGS = {
    "salesforce", "hubspot", "zoominfo", "apollo", "outreach-io", "salesloft",
    "6sense", "gong-engage", "clari", "marketo", "braze",
    "salesforce-marketing-cloud", "gainsight", "clearbit", "lusha",
    "seamless-ai", "linkedin-sales-navigator", "pipedrive", "copper",
    "freshsales", "zoho-crm", "monday-sales", "dynamics-365", "sugarcrm",
    "clay", "demandtools", "leadiq", "warmly", "rb2b", "provyx",
    "definitive-healthcare", "capterra", "g2", "verum", "common-room",
    "mutiny", "oracle-cx", "sap-sales-cloud", "mulesoft", "tray", "celigo",
    "airbyte", "workato-ipaas", "fivetran", "n8n", "zapier", "tableau",
    "power-bi", "looker", "leadfeeder", "boomi", "trustradius",
    "chili-piper", "leandata", "highspot", "churnzero",
}

VALID_CATEGORIES = {
    "crm", "enrichment", "sales-engagement", "abm",
    "conversation-intelligence", "marketing-automation", "customer-success",
    "data-quality", "ipaas", "bi-analytics", "healthcare",
    "review-platforms", "visitor-identification",
}

NEW_USE_CASES = [
    # 1. Customer Success for SaaS
    {
        "slug": "customer-success-for-saas",
        "title": "Customer Success Platforms for SaaS Companies",
        "meta_description": "Which CS platforms work best for SaaS teams managing recurring revenue. Gainsight, ChurnZero, and HubSpot compared on health scoring, playbooks, and churn prevention.",
        "persona": "SaaS customer success teams and CS leaders",
        "category_slug": "customer-success",
        "intro": "Churn is the quiet killer of SaaS businesses. A 5% monthly churn rate cuts your customer base in half every year, and most CS teams don't see it coming until the cancellation email arrives. Customer success platforms give you early warning systems: health scores that flag at-risk accounts, automated playbooks that trigger intervention before it's too late, and expansion signals that help you grow revenue from your existing base.\n\nThe category has matured into a clear hierarchy. Gainsight dominates enterprise deployments. ChurnZero owns the mid-market. And HubSpot's Service Hub has become a credible option for teams already running HubSpot across sales and marketing. The right choice depends on your account count, average contract value, and how deeply you need to integrate product usage data into your CS workflows.\n\nWhat separates good CS platforms from spreadsheet tracking is automation at scale. When you have 200+ accounts per CSM, nobody can manually monitor login frequency, support ticket trends, and feature adoption across every customer. The platform should surface the accounts that need attention and let your team focus on high-value conversations instead of data gathering.",
        "what_to_look_for": [
            {
                "criteria": "Health score configurability",
                "why": "Every SaaS product has different signals for account health: login frequency, feature adoption, support tickets, NPS responses. Your platform needs to let you weight these signals by what predicts churn in your business, not a generic formula."
            },
            {
                "criteria": "Product usage data integration",
                "why": "CS platforms that only track CRM activity miss the most important signal: how customers use your product. Look for native integrations with Segment, Mixpanel, or Amplitude, or a flexible API that can ingest event data from your product."
            },
            {
                "criteria": "Playbook automation",
                "why": "Manual check-ins don't scale past 50 accounts per CSM. Automated playbooks trigger email sequences, task assignments, and escalations based on health score changes. This lets a 5-person team manage 500+ accounts without dropping balls."
            },
            {
                "criteria": "Revenue and expansion tracking",
                "why": "Modern CS isn't just retention. Teams own net revenue retention, which means tracking upsell and cross-sell pipeline alongside renewals. Your platform should tie CS activity to ARR impact, not just engagement metrics."
            }
        ],
        "recommended_tools": [
            {
                "slug": "gainsight",
                "why": "The category leader for mid-market and enterprise SaaS. Deepest health scoring engine, journey orchestration, and product analytics integration in the market. Appears in more CS job postings than any other platform. Pricing starts around $30K/year and scales with customer count."
            },
            {
                "slug": "churnzero",
                "why": "Built specifically for SaaS with strong in-app engagement features like walkthroughs and surveys. Real-time usage alerts, automated playbooks, and usage tracking at a lower price point than Gainsight. Best for teams managing 200-2,000 accounts with $5K-50K ACV."
            },
            {
                "slug": "hubspot",
                "why": "Service Hub includes customer success tools (health scores, playbooks, feedback surveys) integrated with the CRM. Not as deep as dedicated CS platforms, but eliminates the need for a separate vendor if you already run HubSpot for sales and marketing. Starts at $100/user/month for Professional tier."
            }
        ],
        "bottom_line": "Gainsight for enterprise SaaS with 1,000+ accounts and complex health scoring needs. ChurnZero for mid-market SaaS that wants dedicated CS tooling at a lower price point. HubSpot Service Hub if you're already on HubSpot and want one platform. The biggest ROI comes from reducing churn by even 1-2 percentage points, which at scale pays for any platform on this list.",
        "faq": [
            {
                "q": "When does a SaaS company need a customer success platform?",
                "a": "When you have more than 100 accounts and at least 2 CSMs. Before that, CRM tasks and spreadsheet tracking work fine. The trigger is usually when churn surprises start happening because no one noticed declining usage or missed renewal dates."
            },
            {
                "q": "How much does a customer success platform cost?",
                "a": "ChurnZero starts around $12K-20K/year for smaller teams. Gainsight starts at $30K/year and scales to $100K+ for enterprise. HubSpot Service Hub Pro is $100/user/month. Budget 0.5-1.5% of your ARR for CS tooling as a general rule."
            },
            {
                "q": "Can I use my CRM instead of a dedicated CS platform?",
                "a": "For basic renewal tracking and task management, yes. Salesforce and HubSpot both handle that. Where dedicated platforms win is product usage integration, automated health scoring, and playbook orchestration. If your churn rate is above 10% annually and you can't explain why, you've outgrown CRM-based CS."
            }
        ]
    },

    # 2. Sales Enablement for Enterprise
    {
        "slug": "sales-enablement-for-enterprise",
        "title": "Sales Enablement Tools for Enterprise Teams",
        "meta_description": "How enterprise sales teams choose enablement platforms. Content management, training, and buyer engagement tools compared for organizations with 100+ reps.",
        "persona": "VP Sales, enablement directors, and revenue leaders at companies with 100+ reps",
        "category_slug": "sales-engagement",
        "intro": "Enterprise sales teams have a content problem and a coaching problem. Reps can't find the right deck, send outdated case studies, and spend 30% of their time searching for materials instead of selling. Sales enablement platforms solve this by centralizing content, tracking what buyers engage with, and providing structured coaching workflows.\n\nThe category now spans three overlapping areas: content management (organizing and recommending the right materials), buyer engagement (tracking how prospects interact with shared content), and coaching (using call recordings and performance data to improve rep skills). Most enterprise teams need at least two of these three.\n\nThe build vs. buy decision here is straightforward. Google Drive plus tribal knowledge works until you have about 30 reps. After that, reps can't find what they need, marketing has no idea which content gets used, and managers have no consistent coaching framework. The cost of enablement tools is small compared to the revenue lost when enterprise reps send the wrong deck to a $200K deal.",
        "what_to_look_for": [
            {
                "criteria": "Content management and search",
                "why": "Enterprise teams produce hundreds of decks, one-pagers, and case studies. If reps can't find the right asset in under 30 seconds, they'll build their own (off-brand, outdated) or skip it entirely. AI-powered search and content recommendations matter at scale."
            },
            {
                "criteria": "Buyer engagement tracking",
                "why": "Knowing which slides a prospect spent time on tells you more about deal health than the rep's self-reported notes. Digital sales rooms and content analytics show what buyers care about, which feeds back into content strategy and deal forecasting."
            },
            {
                "criteria": "CRM activity capture",
                "why": "Every buyer interaction should log to Salesforce or your CRM automatically. Manual logging means 40-60% of activity goes unrecorded. Look for platforms that capture email opens, content views, and meeting engagement without rep input."
            },
            {
                "criteria": "Coaching and training modules",
                "why": "Onboarding a new enterprise rep takes 6-9 months. Structured learning paths with call recordings, role-play exercises, and certification tracking reduce ramp time by 20-30%. This is where enablement platforms overlap with conversation intelligence."
            }
        ],
        "recommended_tools": [
            {
                "slug": "highspot",
                "why": "The most-adopted enterprise enablement platform. AI-powered content recommendations, buyer engagement analytics, and training modules in one product. Appears in job postings across Fortune 500 companies. Pricing starts around $40/user/month for enterprise contracts."
            },
            {
                "slug": "gong-engage",
                "why": "Started as conversation intelligence and expanded into full enablement. Call recording, coaching scorecards, and deal intelligence from buyer conversations. Best for teams that want coaching driven by real call data rather than generic training content."
            },
            {
                "slug": "salesforce",
                "why": "Sales Cloud's enablement features (content sharing, training paths, coaching tools) are growing. Not a dedicated enablement platform, but useful for teams that want everything in Salesforce without adding another vendor. Requires Sales Cloud Enterprise or higher."
            }
        ],
        "bottom_line": "Highspot for content management and buyer engagement if your primary problem is reps can't find or share the right materials. Gong for coaching-first enablement driven by conversation data. Most enterprise teams end up with Highspot for content plus Gong for coaching as the core enablement stack.",
        "faq": [
            {
                "q": "What's the difference between sales enablement and sales engagement?",
                "a": "Sales engagement (Salesloft, Outreach) automates outreach: emails, calls, sequences. Sales enablement (Highspot, Seismic) manages content, training, and buyer engagement analytics. They overlap on coaching features. Enterprise teams often use both."
            },
            {
                "q": "How do you measure sales enablement ROI?",
                "a": "Track rep ramp time (target: 20-30% reduction), content usage rates (what percentage of assets get used), win rates by content shared, and quota attainment for enabled vs. non-enabled cohorts. The clearest metric is time-to-first-deal for new hires."
            },
            {
                "q": "Do I need a separate enablement platform if I have Salesforce?",
                "a": "Salesforce stores CRM data but doesn't manage sales content, track buyer engagement with materials, or provide structured coaching workflows. Some add-ons (like Highspot's native Salesforce integration) extend it, but the core enablement functionality comes from a dedicated platform."
            }
        ]
    },

    # 3. Analytics for Revenue Teams
    {
        "slug": "analytics-for-revenue-teams",
        "title": "BI and Analytics Tools for Revenue Teams",
        "meta_description": "How RevOps and revenue teams choose analytics tools. Clari, Salesforce reporting, and HubSpot analytics compared for pipeline visibility, forecasting, and revenue intelligence.",
        "persona": "RevOps leaders, revenue analysts, and CROs who need pipeline and forecast visibility",
        "category_slug": "bi-analytics",
        "intro": "Revenue teams drown in dashboards but starve for answers. Salesforce reports show you what happened. Revenue intelligence platforms show you what's about to happen. The analytics stack for a revenue team depends on whether your biggest problem is reporting (backward-looking), analysis (understanding patterns), or forecasting (forward-looking). Most teams need at least two of these three.\n\nThe challenge isn't access to data. It's getting trustworthy data in front of the right people at the right time. Executives want a single pipeline number. Managers want stage-by-stage conversion rates. Reps want their own deals. If each audience requires a different tool or a different analyst to build the dashboard, your analytics are already broken.\n\nRevenue analytics has split into two camps: general-purpose BI tools (Tableau, Power BI, Looker) that can answer any question but require analyst expertise, and purpose-built revenue platforms (Clari, Gong) that answer sales-specific questions out of the box. The first approach is more flexible. The second is faster to deploy.",
        "what_to_look_for": [
            {
                "criteria": "CRM data modeling",
                "why": "Raw CRM data is messy: duplicate records, inconsistent stages, missing fields. Your analytics tool needs to handle data cleaning and modeling, or integrate with a transformation layer like dbt. Garbage in, garbage out applies doubly to revenue analytics."
            },
            {
                "criteria": "Pipeline visualization and drill-down",
                "why": "A single pipeline number is useless without the ability to drill into it. Stage-by-stage conversion, deal aging, and rep-level performance should all be accessible from the same view without switching tools or waiting for an analyst to build a new report."
            },
            {
                "criteria": "Forecast accuracy tracking",
                "why": "The difference between a 65% and 85% accurate forecast is millions in hiring, spending, and investor reporting decisions. Look for tools that track forecast accuracy over time and show you where human judgment diverges from the data."
            },
            {
                "criteria": "Self-service vs. analyst-dependent",
                "why": "If every dashboard change requires an analyst, your BI tool is a bottleneck. Revenue teams need self-service exploration for ad hoc questions while analysts own the core data models and KPI definitions."
            }
        ],
        "recommended_tools": [
            {
                "slug": "clari",
                "why": "Purpose-built for revenue forecasting and pipeline inspection. Pulls CRM data automatically and applies AI to predict deal outcomes. Not a general BI tool, but the fastest path to forecast accuracy for CROs who need answers without building custom dashboards. Starts around $30K/year."
            },
            {
                "slug": "salesforce",
                "why": "Native reports and dashboards handle standard pipeline metrics and are included with your license. You hit limits when you need cross-object analysis, data blending with non-CRM sources, or historical trend analysis. Still the starting point for most revenue teams."
            },
            {
                "slug": "hubspot",
                "why": "Built-in analytics cover pipeline, deal velocity, and rep activity for teams on HubSpot CRM. Custom report builder handles most mid-market needs without a separate BI tool. Falls short on complex cross-source analysis and advanced forecasting models."
            }
        ],
        "bottom_line": "Clari for forecasting if your biggest pain is unpredictable quarterly calls. Salesforce or HubSpot native reporting for standard pipeline metrics. Many revenue orgs run a purpose-built forecasting tool alongside CRM reporting and add a BI platform only when cross-source analysis becomes a priority.",
        "faq": [
            {
                "q": "Can I use Salesforce reports instead of a BI tool?",
                "a": "For basic pipeline reporting, yes. Salesforce reports and dashboards handle standard funnel metrics. You hit limits when you need cross-object analysis, data blending with non-CRM sources (marketing, product usage, finance), or historical trend analysis."
            },
            {
                "q": "What's the difference between BI tools and revenue intelligence?",
                "a": "BI tools (Tableau, Power BI, Looker) are general-purpose analytics platforms you configure for any data. Revenue intelligence tools (Clari, Gong) are pre-built for sales data with opinionated models for forecasting and deal inspection. BI is more flexible. Revenue intelligence is faster to deploy."
            },
            {
                "q": "How much does a revenue analytics stack cost?",
                "a": "CRM native reporting is included with your license. Clari starts around $30K/year for mid-market teams. General BI tools range from $10/user/month (Power BI) to $70/user/month (Tableau). Budget $500-5,000/month depending on team size and tool mix."
            }
        ]
    },

    # 4. CRM for Agencies
    {
        "slug": "crm-for-agencies",
        "title": "CRM for Marketing and Sales Agencies",
        "meta_description": "How agencies and professional services firms choose CRMs. Project-aware pipeline management, client relationship tracking, and tools built for services businesses.",
        "persona": "Agency owners, professional services leaders, and account directors managing client relationships",
        "category_slug": "crm",
        "intro": "Agencies don't sell products. They sell relationships, expertise, and project outcomes. A CRM built for SaaS sales pipelines doesn't map well to how agencies win and retain clients. Agency deals involve proposals, SOWs, multiple stakeholders, and ongoing retainers rather than one-time closes.\n\nThe best CRM for your agency depends on whether your bigger problem is winning new business or managing existing client relationships. HubSpot gives you marketing tools to attract leads alongside the CRM. Pipedrive gives you the cleanest pipeline view for tracking active pitches. Copper lives inside Gmail for teams that manage everything through email.\n\nThe worst mistake agencies make is overbuying. A CRM your team ignores is worse than a spreadsheet they use. Start with a tool that matches your team's workflow today. You can migrate to something more powerful when you outgrow it, but you can't recover the months lost to an adoption failure.",
        "what_to_look_for": [
            {
                "criteria": "Project and deal lifecycle tracking",
                "why": "Agency sales don't end at 'Closed Won.' They transition from pitch to SOW to project to retainer. Your CRM needs to track the full lifecycle. Otherwise you end up managing active clients in spreadsheets or project management tools disconnected from revenue."
            },
            {
                "criteria": "Relationship mapping across accounts",
                "why": "Agency business comes from relationships, not inbound leads. Your CRM should track who knows whom, which contacts have moved between companies, and when to re-engage past clients. Relationship history is your most valuable sales asset."
            },
            {
                "criteria": "Proposal and SOW management",
                "why": "Agencies send proposals, not quotes. Your CRM should integrate with proposal tools or handle document creation natively. Tracking proposal status, win rates by service line, and average deal cycle length helps you forecast revenue accurately."
            },
            {
                "criteria": "Time and revenue tracking integration",
                "why": "Agency profitability depends on utilization rates and project margins. A CRM that integrates with your time tracking or PSA tool gives you visibility into whether the clients you're winning are profitable, not just numerous."
            }
        ],
        "recommended_tools": [
            {
                "slug": "hubspot",
                "why": "The most popular CRM for agencies under 50 people. Free tier covers basic pipeline management. Custom deal properties let you track proposal status, retainer value, and service type. HubSpot's agency partner program includes additional features and support for qualifying agencies."
            },
            {
                "slug": "pipedrive",
                "why": "Visual pipeline management that agencies adopt quickly. Simple enough that account directors will use it without training. Custom fields track project type, retainer value, and client industry. Starts at $14/user/month with no minimum seats."
            },
            {
                "slug": "copper",
                "why": "Built for Google Workspace teams, which describes most small agencies. Lives inside Gmail, so relationship tracking happens automatically from email activity. Best for agencies under 20 people that want minimal CRM overhead and maximum adoption."
            }
        ],
        "bottom_line": "HubSpot for agencies that want a CRM plus marketing tools to attract new clients. Pipedrive for agencies that want the simplest possible pipeline view with high adoption rates. Copper for Google-native small agencies where email is the primary communication channel.",
        "faq": [
            {
                "q": "Do agencies need a CRM?",
                "a": "If you have more than 3 active pitches and 10 client relationships, yes. Before that, a spreadsheet or Notion database works fine. The trigger is usually when you lose a deal because nobody followed up, or you miss a renewal because the account director was too busy on project delivery."
            },
            {
                "q": "Should agencies use a CRM or a project management tool?",
                "a": "Both, for different stages. CRM tracks the sales process (lead to proposal to signed SOW). Project management tracks delivery (kickoff to completion). The integration between them matters: when a deal closes in your CRM, it should trigger project setup in your PM tool."
            },
            {
                "q": "How much should an agency spend on CRM?",
                "a": "Under $50/user/month for teams under 30 people. HubSpot free and Pipedrive ($14-49/user) cover most agency needs. Don't spend more than 1% of revenue on CRM software. If your agency bills $2M/year, cap CRM spending at $20K/year."
            }
        ]
    },

    # 5. Lead Routing for High Volume
    {
        "slug": "lead-routing-for-high-volume",
        "title": "Lead Routing and Matching for High-Volume Inbound Teams",
        "meta_description": "How to route inbound leads at scale. Lead-to-account matching, round-robin distribution, and territory-based routing tools compared for high-volume B2B teams.",
        "persona": "Marketing ops and RevOps teams processing 1,000+ inbound leads per month",
        "category_slug": "sales-engagement",
        "intro": "When you generate 1,000+ leads per month, routing becomes a revenue problem. A lead that sits unassigned for 5 minutes converts at half the rate of one touched in under 60 seconds. Manual assignment breaks down within weeks at this volume.\n\nLead routing involves three distinct problems. Lead-to-account matching ensures inbound leads from target accounts reach the account owner, not the round-robin queue. Territory routing prevents overlapping outreach from reps covering the same geography or segment. And round-robin distribution balances workloads across the team so no one is overwhelmed or idle.\n\nMost teams start with native CRM assignment rules and outgrow them around 500 leads per month. The limitations hit when you need fuzzy matching on company names (IBM vs. International Business Machines), complex territory overlap resolution, or real-time routing that books meetings instantly from form submissions.",
        "what_to_look_for": [
            {
                "criteria": "Lead-to-account matching accuracy",
                "why": "An inbound lead from a target account needs to reach the account owner, not the round-robin queue. Matching requires fuzzy logic for company name variations, email domain mapping, and handling of personal email addresses. Accuracy above 95% is the target."
            },
            {
                "criteria": "Speed of assignment",
                "why": "Response time correlates directly with conversion. The best routing tools assign leads in under 30 seconds from form submission. If your current process takes hours because it runs on a scheduled Salesforce flow, you're losing conversions every day."
            },
            {
                "criteria": "Territory and segment rules",
                "why": "Enterprise teams route by geography, company size, industry, or named accounts. Your routing engine needs to layer these rules without conflicts. When rules contradict (account owner vs. territory vs. round-robin), the priority order must be clear and configurable."
            },
            {
                "criteria": "Visibility and audit trail",
                "why": "When a rep complains they didn't get a lead, you need to see exactly why it was routed elsewhere. Routing audit logs show the matching logic, rule priority, and assignment timestamp. This is essential for resolving territory disputes without guesswork."
            }
        ],
        "recommended_tools": [
            {
                "slug": "chili-piper",
                "why": "Combines lead routing with instant meeting scheduling. When a qualified lead fills out a form, Chili Piper matches them to the right rep and books a meeting in real time. Reduces speed-to-lead from hours to seconds. Starts at $30/user/month with quick implementation."
            },
            {
                "slug": "leandata",
                "why": "The market leader in Salesforce lead routing. Lead-to-account matching, round-robin, territory-based routing, and a visual flow builder for complex logic. Used by the majority of companies that mention lead routing in RevOps job postings. Starts around $25K/year."
            },
            {
                "slug": "salesforce",
                "why": "Native lead assignment rules handle basic round-robin and territory routing at no additional cost. Works for simple routing with under 10 reps. Breaks down when you need lead-to-account matching, complex prioritization, or visual workflow building."
            }
        ],
        "bottom_line": "LeanData for complex Salesforce-based routing with territory management and lead-to-account matching. Chili Piper for instant meeting scheduling on inbound forms. Native CRM routing works until you exceed 10 reps or need account-based matching. The speed improvement alone typically pays for dedicated routing tools within one quarter.",
        "faq": [
            {
                "q": "What's lead-to-account matching and why does it matter?",
                "a": "It connects inbound leads to existing CRM accounts. When a director at a target account fills out a form, matching ensures that lead goes to the account owner, not a random SDR. Without it, reps work the same account without knowing it."
            },
            {
                "q": "How fast should lead routing be?",
                "a": "Under 5 minutes for best conversion rates. Under 60 seconds is ideal. Studies consistently show that leads contacted within 5 minutes are 21x more likely to convert than those contacted after 30 minutes. Chili Piper and LeanData achieve real-time routing."
            },
            {
                "q": "Can I build lead routing in Salesforce without additional tools?",
                "a": "Basic round-robin and field-based assignment, yes. Use assignment rules and Flow. Lead-to-account matching, complex territory overlap resolution, and routing audit trails require LeanData or a similar tool. Most teams outgrow native routing at around 500 leads/month."
            }
        ]
    },

    # 6. Enrichment for ABM
    {
        "slug": "enrichment-for-abm",
        "title": "Data Enrichment for ABM Programs",
        "meta_description": "How ABM teams enrich target account lists with firmographic, technographic, and contact data. Enrichment strategies that improve account coverage and personalization.",
        "persona": "ABM managers, demand gen leads, and marketing ops teams running account-based programs",
        "category_slug": "enrichment",
        "intro": "ABM programs fail when account data is incomplete. You can't personalize outreach to a buying committee you can't identify, target companies you don't understand, or coordinate campaigns across channels with inconsistent firmographic data. ABM-specific enrichment goes beyond basic contact lookup.\n\nThe goal is to fill in the account-level picture: org structure, technology stack, financial signals, and the 6-10 contacts in the buying committee you need to reach. Single-source enrichment providers leave gaps. A target list of 500 accounts will have 70-80% match rates from any one provider. Waterfall enrichment across multiple sources pushes that to 90%+.\n\nTiming matters too. ABM target lists sit for months. In that time, people change jobs, companies get acquired, and tech stacks shift. One-time enrichment degrades at 2-3% per month. If your list is 6 months old, 15-20% of your contact data is wrong. Ongoing refresh is not optional for serious ABM programs.",
        "what_to_look_for": [
            {
                "criteria": "Buying committee coverage",
                "why": "B2B purchases involve 6-10 decision makers. Enriching just the primary contact isn't enough for ABM. You need to identify and enrich the full buying committee: economic buyer, technical evaluator, end users, and legal/procurement. Coverage of director-and-above titles matters most."
            },
            {
                "criteria": "Firmographic depth beyond basics",
                "why": "Company name, size, and industry are table stakes. ABM personalization requires revenue trends, funding rounds, tech stack, hiring velocity, and organizational changes. The more account context your reps have, the more relevant their outreach becomes."
            },
            {
                "criteria": "Account-level data refresh",
                "why": "Contact data decays at 2-3% per month as people change jobs and companies evolve. Look for enrichment providers that offer ongoing refresh schedules, not one-time data dumps. Monthly or quarterly refresh prevents campaigns from hitting stale contacts and bouncing."
            },
            {
                "criteria": "CRM and ABM platform integration",
                "why": "Enriched data needs to flow directly into your ABM platform (6sense, Demandbase) and CRM. Manual CSV imports create data lag and formatting mismatches. API-based enrichment that writes directly to account records eliminates the gap between enrichment and activation."
            }
        ],
        "recommended_tools": [
            {
                "slug": "zoominfo",
                "why": "The broadest contact and account database for ABM enrichment with 260M+ contacts and org chart data for identifying buying committees. Intent data overlay shows which target accounts are researching your category. Starts at $15K/year with ABM-focused packages available."
            },
            {
                "slug": "clearbit",
                "why": "Real-time firmographic and technographic enrichment via API. Strong for enriching account lists programmatically and keeping CRM data fresh with automatic refresh. Now part of HubSpot. Best for teams that want automated enrichment workflows rather than manual list building."
            },
            {
                "slug": "6sense",
                "why": "Combines intent data with account enrichment and ABM orchestration in one platform. Identifies which target accounts are in-market before they fill out a form. Best for teams that want enrichment, intent signals, and ABM execution from a single vendor."
            }
        ],
        "bottom_line": "ZoomInfo for the broadest US coverage and buying committee identification. Clearbit for automated, API-driven account enrichment with ongoing refresh. 6sense if you want enrichment tied directly to intent signals and ABM orchestration. Budget for ongoing data refresh, not just initial enrichment. Stale data is worse than no data because your team trusts it.",
        "faq": [
            {
                "q": "How is ABM enrichment different from regular sales enrichment?",
                "a": "Regular enrichment focuses on individual contacts: email, phone, title. ABM enrichment focuses on accounts: full buying committee, org structure, tech stack, and firmographic depth. ABM also requires higher match rates because you're targeting a defined list, not casting a wide net."
            },
            {
                "q": "How often should I refresh ABM account data?",
                "a": "Monthly for contact data (people change jobs at 15-20% annual rates). Quarterly for firmographic and technographic data. Most teams set up automated enrichment that refreshes records when accounts hit certain engagement thresholds or approach renewal dates."
            },
            {
                "q": "What match rate should I expect for ABM enrichment?",
                "a": "For US enterprise accounts (1,000+ employees): 85-95% firmographic match, 60-80% buying committee coverage. For mid-market: 70-85% firmographic, 40-60% buying committee. For international accounts, expect 10-20% lower across the board. Waterfall enrichment across multiple providers adds 15-25% coverage above single-source results."
            }
        ]
    },

    # 7. Conversation Intelligence for Coaching
    {
        "slug": "conversation-intelligence-for-coaching",
        "title": "Conversation Intelligence for Sales Coaching",
        "meta_description": "How sales leaders use conversation intelligence to coach reps. Call recording, AI analysis, and deal insights from Gong, Clari, and alternatives compared for coaching workflows.",
        "persona": "Sales managers, VP Sales, and enablement leaders responsible for rep performance",
        "category_slug": "conversation-intelligence",
        "intro": "Sales managers spend 20% of their time in 1:1 coaching sessions and have no idea what happened on the other 80% of their team's calls. Conversation intelligence records every call, transcribes it, and surfaces patterns: talk-to-listen ratio, competitor mentions, pricing objections, and next-step commitments. It turns coaching from guesswork into data.\n\nThe best platforms don't just record calls. They tell managers which deals need attention and which reps need help on specific skills. A frontline manager with 8 direct reports can't listen to 40+ hours of calls per week. AI-powered call scoring surfaces the 3-5 calls worth reviewing and tells you what to listen for before you hit play.\n\nThe category has consolidated around a few major players. Gong dominates enterprise. Clari has expanded from forecasting into conversation capture. And the sales engagement platforms (Salesloft, Outreach) have added conversation intelligence features to reduce vendor sprawl. The standalone vs. bundled decision depends on how deep you need the coaching analytics to go.",
        "what_to_look_for": [
            {
                "criteria": "AI-powered call analysis",
                "why": "Recording calls is easy. Analyzing them is where value lives. Look for automatic identification of topics discussed, objections raised, competitor mentions, and next steps promised. This saves managers from listening to full recordings and surfaces coaching moments automatically."
            },
            {
                "criteria": "Deal-level insight aggregation",
                "why": "Individual call analysis is useful. Aggregating all conversations across a deal's lifecycle is where the real insights emerge. You should see every interaction, who attended, what was discussed, and how sentiment changed over time."
            },
            {
                "criteria": "Coaching workflows and scorecards",
                "why": "Raw call data without a coaching framework doesn't change behavior. Look for platforms with scoring rubrics, skill-specific feedback tools, and structured coaching templates. The best tools recommend which calls to review based on where reps underperform."
            },
            {
                "criteria": "Integration with your meeting and dialer stack",
                "why": "Conversation intelligence only works if it captures every conversation. Check compatibility with your video conferencing (Zoom, Teams, Google Meet), dialer, and phone system. Gaps in recording mean gaps in coaching data."
            }
        ],
        "recommended_tools": [
            {
                "slug": "gong-engage",
                "why": "The category leader with the deepest AI analysis. Records calls, emails, and web conferences, then surfaces deal risk, competitor mentions, and coaching opportunities automatically. Appears in more CI job postings than any other tool. Pricing starts around $100/user/month for annual contracts."
            },
            {
                "slug": "clari",
                "why": "Revenue intelligence platform with conversation capture that combines call analysis with pipeline inspection and forecasting. Best for CROs who want deal intelligence and forecast accuracy from the same data, not just call coaching. Starts around $30K/year for mid-market."
            },
            {
                "slug": "hubspot",
                "why": "Call tracking and conversation intelligence features built into Sales Hub. Records calls, provides transcriptions, and offers coaching tools at no additional cost for Sales Hub users. Not as deep as Gong, but eliminates vendor sprawl for HubSpot-native teams."
            }
        ],
        "bottom_line": "Gong for teams that want the deepest conversation analysis and are willing to pay for a standalone tool. Clari for revenue leaders who want conversation data feeding directly into forecasting. HubSpot if you're already on the platform and want coaching features without adding another vendor. The ROI shows up in reduced ramp time for new hires and improved win rates on competitive deals.",
        "faq": [
            {
                "q": "How does conversation intelligence improve win rates?",
                "a": "Teams using conversation intelligence typically see 5-15% improvement in win rates. The gains come from three places: managers coach on real call behavior instead of assumptions, reps learn from top performers' recordings, and deal reviews catch risk signals (missing next steps, new stakeholders, competitor mentions) earlier."
            },
            {
                "q": "Do I need a standalone CI tool if I already use Salesloft or Outreach?",
                "a": "Both Salesloft and Outreach include conversation intelligence features. They're sufficient for basic call recording, transcription, and coaching. Gong's advantage is deeper AI analysis, cross-deal insights, and more sophisticated coaching workflows. If coaching is a top priority and you have the budget, Gong adds value on top."
            },
            {
                "q": "Are there legal concerns with recording sales calls?",
                "a": "Yes. US states vary between one-party and two-party consent laws. California requires all-party consent. Most CI tools add recording notifications automatically, but check your specific jurisdiction. International calls add complexity with GDPR and local privacy laws."
            }
        ]
    },

    # 8. Marketing Automation for Enterprise
    {
        "slug": "marketing-automation-for-enterprise",
        "title": "Enterprise Marketing Automation: Marketo, SFMC, and Braze Compared",
        "meta_description": "How enterprise marketing teams choose automation platforms. Marketo, Salesforce Marketing Cloud, and Braze compared on scale, personalization, and multi-channel orchestration.",
        "persona": "VP Marketing, marketing ops directors, and CMOs at companies with 100K+ contact databases",
        "category_slug": "marketing-automation",
        "intro": "Enterprise marketing automation is a different category from what mid-market tools offer. When your database hits 100K+ contacts, your campaigns span 5+ channels, and your scoring models need to account for product usage, intent data, and offline events, you need platforms built for that complexity.\n\nThe tradeoff is clear: enterprise MAPs are powerful but require dedicated ops teams to run. Marketo needs 1-2 full-time admins. Salesforce Marketing Cloud needs a certified specialist. Braze needs a developer comfortable with Liquid templating. Choosing the wrong platform locks you into a 2-3 year migration cycle because moving 500K contacts, hundreds of campaigns, and years of engagement history is a massive project.\n\nThe decision often comes down to your existing ecosystem. Salesforce shops lean toward Marketo or SFMC. Product-led companies with mobile apps gravitate to Braze. HubSpot Enterprise has become a credible alternative for teams that want enterprise scale without enterprise complexity, though it makes tradeoffs on channel depth.",
        "what_to_look_for": [
            {
                "criteria": "Multi-channel orchestration",
                "why": "Enterprise marketing spans email, SMS, push notifications, in-app messaging, direct mail, and advertising. Your MAP needs to coordinate journeys across all channels with unified audience segmentation and trigger logic. Single-channel email tools don't cut it at this scale."
            },
            {
                "criteria": "Advanced segmentation and personalization",
                "why": "Sending the same email to 500K contacts isn't marketing. You need dynamic segmentation by behavior, firmographic attributes, product usage, and engagement score. Real-time segment evaluation (not overnight batch processing) enables triggered campaigns that respond to buyer behavior within minutes."
            },
            {
                "criteria": "Salesforce integration depth",
                "why": "Most enterprise marketing teams sync with Salesforce. The quality of that integration determines whether marketing and sales see the same data. Check for bidirectional sync frequency, custom object support, and campaign member tracking. A 15-minute sync delay might be unacceptable for your lead scoring model."
            },
            {
                "criteria": "Scalability and sending performance",
                "why": "Sending 1M emails on a Tuesday morning is different from sending 10K. Check deliverability infrastructure, sending speed, and database query performance at your volume. Ask vendors for throughput benchmarks and SLAs on send completion times."
            }
        ],
        "recommended_tools": [
            {
                "slug": "marketo",
                "why": "The most-adopted enterprise MAP in B2B, now part of Adobe. Advanced lead scoring, nurture programs, and the deepest Salesforce integration in the category. Appears in more marketing ops job postings than any other MAP. Pricing starts around $50K/year and scales with database size."
            },
            {
                "slug": "salesforce-marketing-cloud",
                "why": "The strongest choice for companies deep in the Salesforce ecosystem. Journey Builder handles complex multi-channel flows across email, SMS, push, and advertising. Native CRM integration eliminates sync issues. Best for B2C and B2B2C use cases. Pricing starts around $25K/year."
            },
            {
                "slug": "braze",
                "why": "Built for real-time, cross-channel engagement with strength in mobile push, in-app messaging, and SMS alongside email. The strongest choice for product-led companies where user behavior triggers marketing campaigns in real time. Growing adoption in B2B SaaS for PLG motions."
            }
        ],
        "bottom_line": "Marketo for traditional B2B enterprise marketing with Salesforce integration. Salesforce Marketing Cloud for companies embedded in the Salesforce platform, especially B2C. Braze for product-led companies prioritizing real-time mobile and in-app engagement. Plan for 6-12 months of migration and $50K-150K in implementation costs at this tier.",
        "faq": [
            {
                "q": "When should a company move from HubSpot to Marketo?",
                "a": "When you need complex multi-touch attribution, advanced lead scoring with custom objects, or your database exceeds 500K contacts and HubSpot's pricing becomes prohibitive. Also when your marketing ops team is large enough (3+ people) to justify the operational overhead."
            },
            {
                "q": "How much does enterprise marketing automation cost?",
                "a": "Marketo: $50K-200K/year depending on database size and features. Salesforce Marketing Cloud: $25K-150K/year. Braze: custom pricing, typically $50K-200K/year. Add 50-100% for implementation consulting in year one. Ongoing admin costs $80K-120K/year for a dedicated marketing ops hire."
            },
            {
                "q": "Can I use Salesforce Marketing Cloud for B2B?",
                "a": "Yes, but it was built for B2C and it shows. Journey Builder handles complex consumer journeys well. For B2B lead scoring, nurture campaigns, and CRM integration, Marketo or Account Engagement (Pardot) are more natural fits. SFMC works best for B2B companies with large consumer-facing components."
            }
        ]
    },

    # 9. Data Integration for Warehouses
    {
        "slug": "data-integration-for-warehouses",
        "title": "iPaaS and ELT Tools for Data Warehouse Loading",
        "meta_description": "How data teams choose ELT and iPaaS tools for loading data into Snowflake, BigQuery, and Redshift. Fivetran, Airbyte, and Workato compared on connectors, pricing, and reliability.",
        "persona": "Data engineers, analytics engineers, and data platform leads building warehouse infrastructure",
        "category_slug": "ipaas",
        "intro": "Your data warehouse is only as useful as the data that flows into it. ELT tools handle the plumbing: extracting data from SaaS tools, databases, and APIs, then loading it into Snowflake, BigQuery, or Redshift for analysis. The market has split between managed platforms that prioritize reliability and open-source alternatives that prioritize cost control.\n\nYour choice depends on how much engineering time you can afford to spend on data pipelines versus analysis. Fivetran's pitch is zero-maintenance: connectors work, schemas update, and your team focuses on modeling and dashboards. Airbyte's pitch is cost savings: self-host the platform, skip per-row pricing, and keep control. Workato bridges application integration with data movement for teams that need both.\n\nThe hidden cost in this category isn't the tool itself. It's the maintenance burden when connectors break. SaaS vendors change their APIs without warning, and someone has to fix the pipeline at 2 AM when your Salesforce sync stops loading. Managed platforms absorb that cost. Self-hosted tools pass it to your engineering team.",
        "what_to_look_for": [
            {
                "criteria": "Connector quality, not just quantity",
                "why": "Every vendor claims 300+ connectors. What matters is whether the connectors you need support full historical sync, incremental updates, custom fields, and schema changes. Test your top 5 critical connectors during evaluation, not just the count on the marketing page."
            },
            {
                "criteria": "Schema change handling",
                "why": "SaaS vendors change their APIs without warning. When Salesforce adds a field or HubSpot renames a property, your pipeline should handle it gracefully. Look for automatic schema migration, alerting on breaking changes, and the ability to replay historical data after fixes."
            },
            {
                "criteria": "Cost predictability at scale",
                "why": "Data volumes grow faster than budgets. Managed platforms charge by rows synced, which can surprise you when a high-volume source spikes. Self-hosted options shift cost to infrastructure. Model your cost at 2x and 5x current volume before committing."
            },
            {
                "criteria": "Transformation and orchestration support",
                "why": "ELT tools load raw data. You still need a transformation layer (dbt is the standard) to model it for analysis. Some platforms offer bundled transformation. Others leave it to you. Evaluate the full pipeline from extraction to serving, not just the ELT step in isolation."
            }
        ],
        "recommended_tools": [
            {
                "slug": "fivetran",
                "why": "The market leader in managed ELT with 500+ connectors and zero-maintenance pipelines. Automated schema management, monitoring, and the highest reliability SLAs in the category. Best for teams that want to spend engineering time on analysis, not pipeline maintenance. Pricing scales with data volume."
            },
            {
                "slug": "airbyte",
                "why": "Open-source ELT with 400+ connectors. Self-hosted option eliminates per-row pricing entirely (you pay only for compute). Cloud-managed version offers reliability at lower cost than Fivetran. Best for teams with DevOps capacity who want cost control as data volume grows."
            },
            {
                "slug": "workato-ipaas",
                "why": "Enterprise iPaaS that handles both application integration and data warehouse loading. Recipe-based automation for teams that need to move data between SaaS apps and load it into the warehouse from the same platform. Best when data movement is part of a broader integration strategy."
            }
        ],
        "bottom_line": "Fivetran for teams that prioritize reliability and have budget for managed services. Airbyte for cost-conscious teams with engineering capacity to self-manage. Workato when data warehouse loading is part of a broader iPaaS need. All three need a transformation layer (dbt is standard) for a complete data stack.",
        "faq": [
            {
                "q": "What's the difference between ETL and ELT?",
                "a": "ETL transforms data before loading it into the warehouse. ELT loads raw data first, then transforms it inside the warehouse. ELT has become the standard because modern warehouses (Snowflake, BigQuery) handle transformation efficiently, and loading raw data preserves the original for future use cases."
            },
            {
                "q": "Should I use Fivetran or Airbyte?",
                "a": "Fivetran for zero-maintenance pipelines with enterprise SLAs. Airbyte if you have DevOps capacity and want cost savings at scale. For teams under 20 employees, Airbyte Cloud is usually the best value. For enterprise teams where pipeline downtime costs revenue, Fivetran's reliability premium is worth paying."
            },
            {
                "q": "How much does a modern data stack cost?",
                "a": "Entry level: Airbyte (free self-hosted) + dbt Core (free) + Snowflake ($500/month) = under $1K/month. Mid-market: Fivetran ($1K-5K/month) + dbt Cloud ($100-500/month) + warehouse ($2K-10K/month) = $4K-16K/month. Enterprise scales with data volume and user count."
            }
        ]
    },

    # 10. Review Management for Vendors
    {
        "slug": "review-management-for-vendors",
        "title": "Review Platforms for Software Vendors",
        "meta_description": "How software vendors choose review platforms to collect and manage customer reviews. G2, TrustRadius, and Capterra compared on buyer traffic, review quality, and ROI.",
        "persona": "Product marketers, demand gen leaders, and CMOs at B2B software companies",
        "category_slug": "review-platforms",
        "intro": "B2B buyers check review sites before they talk to sales. Over 80% of software purchases now include review site research, and the vendors who show up with strong profiles, recent reviews, and verified customer quotes have a measurable advantage in deal cycles. The three major platforms (G2, TrustRadius, Capterra) each serve different buyer audiences and offer different vendor programs.\n\nThe vendor side of review platforms involves two investments: building your review profile (collecting reviews, responding to them, keeping data current) and paying for premium features (intent data, buyer leads, advertising). The free tiers give you a listing. The paid tiers give you the data and leads that make review platforms a demand gen channel.\n\nThe biggest mistake vendors make is spreading thin across all three platforms with minimal investment in each. A strong profile with 50+ recent reviews on one platform outperforms mediocre presence across three. Pick your primary platform based on where your buyers research, then expand once that foundation is solid.",
        "what_to_look_for": [
            {
                "criteria": "Buyer traffic and relevance to your category",
                "why": "G2 leads in overall B2B software traffic. Capterra dominates SMB buyer searches. TrustRadius attracts enterprise buyers doing deep research. Check which platform ranks highest in Google for your category keywords. That's where your buyers are looking."
            },
            {
                "criteria": "Review collection and management tools",
                "why": "Getting customers to write reviews is the hardest part. Look for platforms with in-app review prompts, email campaign templates, and incentive programs that make collecting reviews part of your customer lifecycle, not a quarterly scramble."
            },
            {
                "criteria": "Intent data and buyer signals",
                "why": "Paid vendor tiers on G2 and TrustRadius provide intent data: which companies are viewing your profile, comparing you to competitors, and reading specific feature reviews. This data feeds your ABM and outbound programs with high-intent leads."
            },
            {
                "criteria": "Integration with your marketing stack",
                "why": "Review badges, quotes, and ratings should flow into your website, sales decks, and nurture campaigns. Check for embeddable widgets, CRM integrations for intent data, and API access for pulling review content into your marketing assets."
            }
        ],
        "recommended_tools": [
            {
                "slug": "g2",
                "why": "The largest B2B software review platform with the most buyer traffic. Grid reports and category rankings are widely referenced in sales cycles. Buyer intent data shows which companies are researching your category. Free profile available; paid plans start around $15K/year for enhanced features and leads."
            },
            {
                "slug": "trustradius",
                "why": "Focused on verified, in-depth reviews that enterprise buyers trust. No anonymous reviews allowed. TrustQuotes let you embed customer quotes on your website. Stronger with enterprise and mid-market buyers doing thorough evaluations. Free and paid tiers available."
            },
            {
                "slug": "capterra",
                "why": "Part of the Gartner Digital Markets network (includes GetApp, Software Advice). Dominates SMB buyer search traffic with strong Google rankings for 'best X software' queries. Pay-per-click advertising model lets vendors bid on category placement. Best for products targeting small business buyers."
            }
        ],
        "bottom_line": "G2 for the largest audience and buyer intent data if your category is well-represented there. TrustRadius for enterprise credibility with verified, in-depth reviews. Capterra for SMB buyer traffic through Gartner's distribution network. Start with the platform where your buyers research, build 50+ reviews, then expand to a second platform.",
        "faq": [
            {
                "q": "How many reviews do I need to be competitive on G2?",
                "a": "At minimum 10 to appear in the G2 Grid. To be competitive in most categories, aim for 50+ reviews with at least 10 from the past 6 months. Leaders in popular categories often have 200-500+ reviews. Freshness matters as much as quantity since buyers filter for recent reviews."
            },
            {
                "q": "Is it worth paying for premium vendor features?",
                "a": "Depends on your deal size. If your ACV is over $10K, the buyer intent data from G2 or TrustRadius paid plans can identify in-market accounts that justify the $15K-50K/year investment. For lower-ACV products, Capterra's pay-per-click model lets you pay only for traffic you receive."
            },
            {
                "q": "How do I get customers to write reviews?",
                "a": "Ask at the right moment: after a support win, a successful onboarding, or a renewal. In-app prompts convert better than email campaigns. Offer a small incentive (gift card, donation to charity) but never ask for positive-only reviews. G2 and TrustRadius both provide review collection tools to automate the process."
            }
        ]
    },
]


def main():
    dry_run = "--dry-run" in sys.argv

    uc = load("use_cases.json")
    tc = load("tool_content.json")

    uc_list = uc.get("use_cases", [])
    existing_slugs = {u["slug"] for u in uc_list}

    added = 0
    skipped = 0

    for new_uc in NEW_USE_CASES:
        slug = new_uc["slug"]

        # Skip if already exists
        if slug in existing_slugs:
            print(f"  SKIP  {slug}: already exists")
            skipped += 1
            continue

        # Validate category_slug
        if new_uc["category_slug"] not in VALID_CATEGORIES:
            print(f"  ERROR {slug}: invalid category_slug '{new_uc['category_slug']}'")
            skipped += 1
            continue

        # Verify recommended tools exist in tool_content.json
        valid_tools = []
        invalid_tools = []
        for t in new_uc["recommended_tools"]:
            if t["slug"] in tc and t["slug"] in VALID_TOOL_SLUGS:
                valid_tools.append(t)
            else:
                invalid_tools.append(t["slug"])

        if invalid_tools:
            print(f"  WARN  {slug}: removed invalid tool slugs: {', '.join(invalid_tools)}")

        if len(valid_tools) < 2:
            print(f"  SKIP  {slug}: not enough valid tools ({len(valid_tools)} found)")
            skipped += 1
            continue

        new_uc["recommended_tools"] = valid_tools

        # Validate structure
        assert len(new_uc["what_to_look_for"]) >= 3, (
            f"{slug}: expected 3-5 what_to_look_for, got {len(new_uc['what_to_look_for'])}"
        )
        assert 3 <= len(new_uc["recommended_tools"]) <= 5, (
            f"{slug}: expected 3-5 recommended_tools, got {len(new_uc['recommended_tools'])}"
        )
        assert len(new_uc["faq"]) == 3, (
            f"{slug}: expected 3 FAQs, got {len(new_uc['faq'])}"
        )
        # Validate FAQ uses q/a keys
        for faq_item in new_uc["faq"]:
            assert "q" in faq_item and "a" in faq_item, (
                f"{slug}: FAQ items must use 'q' and 'a' keys"
            )

        uc_list.append(new_uc)
        print(f"  ADD   {slug}: {len(valid_tools)} tools, "
              f"{len(new_uc['what_to_look_for'])} criteria, "
              f"{len(new_uc['faq'])} FAQs")
        added += 1

    uc["use_cases"] = uc_list
    print(f"\nAdded: {added}")
    print(f"Skipped: {skipped}")
    print(f"Total use cases: {len(uc_list)}")

    if dry_run:
        print("\n[DRY RUN] No changes written.")
    else:
        save("use_cases.json", uc)
        print(f"\nWritten to {DATA}/use_cases.json")


if __name__ == "__main__":
    main()
