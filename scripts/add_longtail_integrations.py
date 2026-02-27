#!/usr/bin/env python3
"""
Add 12 new longtail integration entries to data/integrations.json.

New pairs:
  apollo-clay, hubspot-clearbit, salesforce-cognism, hubspot-warmly,
  salesforce-bombora, clay-outreach-io, hubspot-gong-engage,
  salesforce-demandtools, apollo-instantly, zapier-clay,
  hubspot-leadiq, salesforce-common-room
"""
import json
from datetime import date
from pathlib import Path

DATA_DIR = Path("/Users/rome/Documents/projects/datastackguide/data")
INTEGRATIONS_FILE = DATA_DIR / "integrations.json"
TODAY = date.today().isoformat()


NEW_INTEGRATIONS = [
    # 1. apollo-clay (enrichment waterfall)
    {
        "slug": "apollo-clay",
        "tool_a": "apollo",
        "tool_b": "clay",
        "cooccurrence_count": 38,
        "title": "Apollo + Clay Integration Guide",
        "meta_description": "How to use Apollo and Clay together. Build enrichment waterfalls, layer multiple data sources, and create prospect lists with higher coverage.",
        "overview": "Apollo and Clay appear together frequently in growth and revenue operations roles. Both tools offer contact and company data, but they serve different purposes in a modern prospecting stack. Apollo provides a large B2B database with built-in sequencing. Clay is a data orchestration platform that pulls from 50+ providers, including Apollo, to build enrichment waterfalls that maximize coverage.\n\nThe typical setup uses Clay as the orchestration layer and Apollo as one of several data sources inside Clay's waterfall. When Apollo can't find an email or phone number, Clay automatically falls through to the next provider. Teams running this combination report 15-30% higher email coverage than using Apollo alone.\n\nThis pairing is popular with outbound teams that need high-volume prospecting with accurate contact data. Clay handles the enrichment logic, and Apollo provides both data and a sequencing engine for the output.",
        "how_they_work_together": [
            {
                "workflow": "Enrichment waterfall",
                "description": "Clay queries Apollo first for contact emails and phone numbers. If Apollo returns no result or low-confidence data, Clay automatically tries the next provider in the waterfall (Clearbit, Hunter, Prospeo, etc.). This layered approach fills gaps that any single provider would miss."
            },
            {
                "workflow": "List building with multi-source validation",
                "description": "Teams build prospect lists in Clay using firmographic filters, then enrich each record through Apollo and other providers simultaneously. Clay cross-references results across sources, flagging records where providers disagree on email or title. This validation step catches stale data before it enters your CRM."
            },
            {
                "workflow": "Apollo sequence loading",
                "description": "After Clay enriches and validates a prospect list, the cleaned data pushes directly into Apollo sequences for outreach. Reps get pre-enriched contacts loaded into their sequences without manual CSV imports or copy-pasting between tools."
            },
            {
                "workflow": "CRM enrichment pipeline",
                "description": "Clay pulls records from your CRM that have missing fields, runs them through Apollo and other providers to fill gaps, then writes the enriched data back. This keeps your CRM data fresh without burning Apollo credits on records that already have complete information."
            },
            {
                "workflow": "ICP scoring with combined data",
                "description": "Clay combines Apollo's technographic and firmographic data with signals from other sources (job postings, funding data, web traffic) to score prospects against your ideal customer profile. The composite score is more accurate than any single provider's data would produce."
            }
        ],
        "setup_considerations": [
            "Connect your Apollo API key inside Clay's integrations settings. Clay charges its own credits on top of Apollo's API usage, so budget for both. A typical enrichment waterfall with Apollo as the primary source costs $0.02-0.05 per record in combined credits.",
            "Set Apollo as the first provider in your waterfall for email and phone lookups if you already have an Apollo subscription. This maximizes value from your existing contract before spending Clay credits on secondary providers.",
            "Use Clay's deduplication features before pushing enriched records to Apollo sequences. Without dedup, you'll load duplicate contacts into sequences and waste outreach touches on the same person from different data sources.",
            "Define which fields each tool owns. Apollo is typically stronger on email addresses and direct dials. Clay's value is in combining multiple sources for company data, technographics, and validation. Don't pay for the same data twice."
        ],
        "faq": [
            {
                "q": "Why use Clay if Apollo already has a large contact database?",
                "a": "Apollo's database covers roughly 250M contacts, but no single provider has complete coverage. Clay's waterfall approach queries Apollo first, then fills gaps with other providers. Teams typically see 15-30% more valid emails by running a waterfall versus Apollo alone. Clay also adds data types Apollo doesn't carry, like job posting signals and web scraping."
            },
            {
                "q": "How much does the Apollo-Clay combination cost?",
                "a": "Apollo plans start at $49/month (Basic) with email credits included. Clay pricing starts at $149/month for the Explorer plan. The total cost depends on volume. A team running 5,000 enrichments per month through Clay with Apollo as the primary source typically spends $300-600/month combined across both platforms."
            },
            {
                "q": "Can Clay replace Apollo entirely?",
                "a": "For data enrichment, yes. Clay can pull from Apollo's database plus dozens of other sources. But Apollo also includes email sequencing, a dialer, and a CRM-like interface that Clay doesn't offer. Most teams keep Apollo for outreach execution and use Clay for the enrichment and orchestration layer."
            }
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },

    # 2. hubspot-clearbit (now Breeze)
    {
        "slug": "hubspot-clearbit",
        "tool_a": "hubspot",
        "tool_b": "clearbit",
        "cooccurrence_count": 45,
        "title": "HubSpot + Clearbit Integration Guide",
        "meta_description": "How to integrate Clearbit (now HubSpot Breeze Intelligence) with HubSpot. Enrich CRM records, identify website visitors, and score leads with firmographic data.",
        "overview": "HubSpot acquired Clearbit in late 2023 and rebranded it as Breeze Intelligence, making this one of the tightest CRM-enrichment integrations available. Clearbit's data enrichment, website visitor identification, and form shortening capabilities are now built directly into HubSpot's platform. Teams that previously ran Clearbit as a standalone integration now get native access.\n\nThe practical impact is significant. Clearbit enriches HubSpot contacts and companies with firmographic data (industry, employee count, revenue, tech stack) the moment a record is created. It also identifies anonymous website visitors at the company level and shortens forms by auto-filling known fields. These features help marketing qualify leads faster and give sales reps context before their first outreach.\n\nFor teams already on HubSpot, Breeze Intelligence is the path of least resistance for CRM enrichment. There's no middleware to configure, no field mapping to maintain, and no sync delays. The data lives natively in HubSpot properties.",
        "how_they_work_together": [
            {
                "workflow": "Automatic record enrichment",
                "description": "When a contact or company is created in HubSpot, Clearbit/Breeze enriches it with 100+ data attributes: employee count, revenue range, industry, tech stack, social profiles, and more. Enrichment happens in real time with no manual trigger needed. Empty fields get filled; existing data can be preserved or overwritten based on your rules."
            },
            {
                "workflow": "Website visitor identification",
                "description": "Clearbit's Reveal feature identifies companies visiting your website, even before they fill out a form. These anonymous visitor signals feed into HubSpot as company records with visit data, letting marketing and sales see which target accounts are researching your product."
            },
            {
                "workflow": "Form shortening",
                "description": "Clearbit pre-fills form fields for known visitors, reducing form length from 8+ fields to 2-3. Shorter forms increase conversion rates by 20-50%. The data that visitors would have typed manually (company, title, size) gets enriched automatically after submission."
            },
            {
                "workflow": "Lead scoring with firmographic data",
                "description": "HubSpot lead scoring models use Clearbit-enriched properties to qualify leads. A form fill from a 500-person SaaS company scores differently than one from a 5-person agency. Firmographic scoring runs automatically on enriched records without manual data entry."
            },
            {
                "workflow": "Dynamic list segmentation",
                "description": "Marketing builds HubSpot lists using Clearbit-enriched fields: companies with 200+ employees in healthcare using Salesforce. These segments drive targeted email campaigns, ad audiences, and personalized website content. Enrichment data keeps these lists accurate as company data changes."
            }
        ],
        "setup_considerations": [
            "Since HubSpot acquired Clearbit, the integration is native. Breeze Intelligence is available as an add-on to HubSpot Marketing Hub and Sales Hub Professional and Enterprise plans. Pricing is credit-based, starting at $30/month for 100 credits.",
            "Decide on enrichment rules before enabling. Choose whether Clearbit data should overwrite existing HubSpot property values or only fill empty fields. Most teams use 'fill empty only' to preserve manually entered data from sales reps.",
            "Clearbit enrichment credits are consumed per record. Set up enrichment filters to only process records that match your target market criteria. Enriching every form fill, including spam and competitors, wastes credits.",
            "If you were running Clearbit as a standalone product before the HubSpot acquisition, talk to your HubSpot rep about migration pricing. Some legacy Clearbit customers got Breeze Intelligence credits bundled into their HubSpot renewal.",
            "Website visitor identification works at the company level, not the individual level. You'll see 'Acme Corp visited your pricing page' but not which specific person at Acme Corp was browsing. Pair with form submissions and email engagement for individual-level identification."
        ],
        "faq": [
            {
                "q": "Is Clearbit still available as a standalone product?",
                "a": "Clearbit was rebranded to Breeze Intelligence after HubSpot's acquisition. New customers get it through HubSpot. Existing Clearbit standalone customers can continue using the product, but new features and development are focused on the HubSpot-native version. If you're not on HubSpot, alternatives like ZoomInfo, Apollo, or Clay offer similar enrichment capabilities."
            },
            {
                "q": "How does Breeze Intelligence pricing compare to standalone Clearbit?",
                "a": "Breeze Intelligence uses a credit-based model starting at $30/month for 100 credits. Standalone Clearbit priced by volume and feature tier, typically $12K-50K/year for mid-market companies. For teams already on HubSpot, Breeze Intelligence is usually cheaper since there's no separate platform fee. The per-record cost depends on your credit tier."
            },
            {
                "q": "Can I use Clearbit/Breeze with Salesforce instead of HubSpot?",
                "a": "Clearbit's standalone Salesforce integration still works for existing customers. But new investment is going into the HubSpot-native experience. If your CRM is Salesforce, ZoomInfo, Cognism, or Clay may be better-supported enrichment options long-term. HubSpot clearly wants Breeze Intelligence to be a reason teams choose HubSpot over other CRMs."
            }
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },

    # 3. salesforce-cognism (European data)
    {
        "slug": "salesforce-cognism",
        "tool_a": "salesforce",
        "tool_b": "cognism",
        "cooccurrence_count": 28,
        "title": "Salesforce + Cognism Integration Guide",
        "meta_description": "How to integrate Cognism with Salesforce. Enrich CRM records with GDPR-compliant European contact data, verified mobile numbers, and intent signals.",
        "overview": "Salesforce and Cognism appear together in 28 job postings, with heavy concentration in European and EMEA-focused sales teams. Cognism is a B2B data provider that differentiates on two fronts: GDPR-compliant European contact data and phone-verified mobile numbers. The Salesforce integration pushes enriched contacts directly into CRM records, giving reps verified direct dials and compliant email addresses for European prospects.\n\nFor teams selling into Europe, Cognism fills a gap that US-centric providers like ZoomInfo and Apollo struggle with. European mobile numbers are notoriously hard to source, and GDPR compliance adds complexity that most American data vendors handle as an afterthought. Cognism was built for this market from day one.\n\nThe integration works through a Chrome extension and Salesforce managed package. Reps can enrich individual records, bulk-enrich account lists, or set up automated enrichment for inbound leads. Intent data from Bombora (bundled with Cognism) also syncs to Salesforce account records.",
        "how_they_work_together": [
            {
                "workflow": "CRM record enrichment",
                "description": "Cognism enriches Salesforce leads, contacts, and accounts with verified emails, direct-dial mobile numbers, and firmographic data. Enrichment can run automatically on new records or manually through the Cognism sidebar in Salesforce. The emphasis is on data accuracy: Cognism's Diamond Data tier includes phone-verified mobile numbers with 98% connect rates."
            },
            {
                "workflow": "Prospecting from Salesforce",
                "description": "Reps search Cognism's database directly from the Salesforce interface, filtering by job title, seniority, department, industry, and geography. Matching contacts push into Salesforce as new leads with all available data fields pre-populated. No need to switch to a separate prospecting tool."
            },
            {
                "workflow": "Intent-based account prioritization",
                "description": "Cognism bundles Bombora intent data, which syncs to Salesforce account records as custom fields. Sales teams see which target accounts are researching relevant topics. Intent scores help reps prioritize accounts that are actively in-market over cold outbound targets."
            },
            {
                "workflow": "GDPR compliance tracking",
                "description": "Cognism flags the legal basis for each contact record (legitimate interest, consent status, DNC list checks). This compliance metadata syncs to Salesforce, giving legal and compliance teams an audit trail. For European outreach, this documentation is essential for GDPR compliance."
            },
            {
                "workflow": "Data refresh and hygiene",
                "description": "Cognism regularly re-verifies contact data and pushes updates to Salesforce. When a prospect changes jobs, Cognism flags the stale record and provides the updated information. This keeps bounce rates low and prevents reps from calling disconnected numbers."
            }
        ],
        "setup_considerations": [
            "Cognism installs as a Salesforce managed package with a Chrome extension. The package adds custom objects and fields for enrichment data and intent signals. Review your Salesforce data storage limits before installation, especially on Professional edition.",
            "Set up DNC (Do Not Call) list integration before enabling phone enrichment. Cognism checks against global DNC registries, but your organization may have additional suppression lists in Salesforce that need to be cross-referenced.",
            "Cognism credits work differently than ZoomInfo. You pay per record revealed (not per enrichment). Budget based on your monthly prospecting volume. Most mid-market teams use 500-2,000 reveals per month per rep.",
            "If your team sells into both North America and Europe, consider running Cognism alongside a US-focused provider like ZoomInfo. Cognism's European data is stronger, but its North American coverage is thinner. Some teams use Cognism for EMEA and ZoomInfo for North America.",
            "Train reps on the GDPR compliance fields that Cognism adds to Salesforce records. Understanding consent status and legal basis isn't optional for European outreach. Reps need to check compliance flags before reaching out to EU-based contacts."
        ],
        "faq": [
            {
                "q": "How does Cognism's data compare to ZoomInfo for European contacts?",
                "a": "Cognism is stronger in Europe, particularly for mobile phone numbers. ZoomInfo's European coverage has improved but still lags in direct dials and GDPR compliance documentation. For EMEA-focused teams, Cognism is the standard choice. For US-only teams, ZoomInfo typically has better coverage. Global teams often run both."
            },
            {
                "q": "How much does Cognism cost?",
                "a": "Cognism doesn't publish pricing. Based on market data, plans typically start around $15K-25K/year for a small team (3-5 users) with Diamond Data (phone-verified mobiles). Enterprise contracts with higher user counts and premium intent data run $40K-80K/year. Pricing is negotiable, especially for annual commitments."
            },
            {
                "q": "Does Cognism work with Salesforce Professional edition?",
                "a": "Yes, but you need API access enabled on Salesforce Professional, which is an add-on ($25/user/month). Cognism's managed package and enrichment features require API calls to read and write Salesforce records. Enterprise and Unlimited editions include API access by default."
            }
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },

    # 4. hubspot-warmly (visitor identification + CRM)
    {
        "slug": "hubspot-warmly",
        "tool_a": "hubspot",
        "tool_b": "warmly",
        "cooccurrence_count": 22,
        "title": "HubSpot + Warmly Integration Guide",
        "meta_description": "How to integrate Warmly with HubSpot. Identify anonymous website visitors, reveal buying committees, and route warm leads into your CRM pipeline.",
        "overview": "HubSpot and Warmly appear together in 22 job postings, concentrated in demand generation and inbound marketing operations. Warmly is a website visitor identification platform that de-anonymizes traffic at both the company and individual level, then pushes those signals into HubSpot for sales follow-up. The integration turns anonymous web traffic into actionable pipeline.\n\nWhat makes Warmly different from basic IP-based identification tools is its ability to identify individual visitors (not just companies) by combining first-party data, third-party enrichment, and intent signals. When someone from a target account visits your pricing page, Warmly can often identify the specific person, their title, and their contact information, then push that to HubSpot as a new contact or activity on an existing record.\n\nTeams use this combination to close the gap between website traffic and pipeline. Instead of waiting for visitors to fill out a form, sales gets notified when high-value prospects are browsing the site and can reach out while interest is high.",
        "how_they_work_together": [
            {
                "workflow": "Visitor-to-CRM identification",
                "description": "Warmly identifies anonymous website visitors and pushes identified contacts into HubSpot automatically. Records include the visitor's name, title, company, email, and which pages they viewed. Hot visitors at target accounts can trigger HubSpot workflows for immediate rep notification."
            },
            {
                "workflow": "Buying committee mapping",
                "description": "When Warmly identifies a visitor from a target account, it also surfaces other stakeholders at the same company. These buying committee members push to HubSpot as associated contacts, giving reps a map of who else to engage at the account beyond the initial visitor."
            },
            {
                "workflow": "Intent-based lead scoring",
                "description": "Warmly tracks which pages visitors view (pricing, case studies, competitor comparison pages) and passes this intent data to HubSpot. Marketing uses page-level intent signals in HubSpot lead scoring models to prioritize visitors showing buying behavior over casual browsers."
            },
            {
                "workflow": "Real-time sales alerts",
                "description": "Warmly sends real-time notifications (via Slack, email, or in-app) when target accounts visit high-intent pages. These alerts include HubSpot context: the visitor's CRM status, deal stage, last activity, and account owner. Reps can follow up within minutes of a prospect visiting the site."
            },
            {
                "workflow": "Automated outreach triggers",
                "description": "HubSpot workflows trigger based on Warmly's visitor data. When a visitor from an ICP-matching company views the pricing page, HubSpot can automatically enroll them in a personalized email sequence, assign the contact to a rep, and create a task for follow-up."
            }
        ],
        "setup_considerations": [
            "Install Warmly's JavaScript snippet on your website alongside HubSpot's tracking code. Both scripts need to load on every page for full visitor identification and CRM syncing. Test on a staging environment first to confirm there are no script conflicts.",
            "Define which visitor segments should sync to HubSpot. Sending every identified visitor to your CRM creates noise. Filter by company size, industry, or ICP match so only qualified visitors become HubSpot contacts. Most teams set a minimum employee count (50+) to filter out freelancers and students.",
            "Warmly's individual-level identification relies on cookie matching, email pixel data, and third-party data partnerships. Match rates vary: expect 10-30% of traffic identified at the individual level and 40-60% at the company level. Don't expect 100% identification.",
            "Review your HubSpot contact creation limits. Warmly can generate a high volume of new contacts if your site gets significant traffic. Make sure your HubSpot plan has room for additional contacts, or set stricter filtering rules in Warmly to control volume."
        ],
        "faq": [
            {
                "q": "How is Warmly different from HubSpot's built-in company identification?",
                "a": "HubSpot's native website analytics show company-level visitors based on IP lookup, but it doesn't identify individuals or provide contact details. Warmly goes further by identifying specific people, providing their email and phone number, and mapping buying committees. The individual-level identification is what makes Warmly valuable beyond HubSpot's native capabilities."
            },
            {
                "q": "How much does Warmly cost?",
                "a": "Warmly's pricing starts at $499/month for the startup tier with basic identification. The Business plan with orchestration and deeper identification runs $1,000-2,500/month depending on traffic volume. Enterprise pricing is custom. Most teams see ROI within 2-3 months if they have sales capacity to follow up on identified visitors."
            },
            {
                "q": "Is website visitor identification GDPR-compliant?",
                "a": "It depends on your implementation. Warmly's identification uses public business data and first-party cookie consent. For EU visitors, you need proper cookie consent banners and should only identify visitors who have accepted tracking cookies. Work with your legal team to ensure your specific configuration meets GDPR requirements for your market."
            }
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },

    # 5. salesforce-bombora (intent data sync)
    {
        "slug": "salesforce-bombora",
        "tool_a": "salesforce",
        "tool_b": "bombora",
        "cooccurrence_count": 32,
        "title": "Salesforce + Bombora Integration Guide",
        "meta_description": "How to integrate Bombora intent data with Salesforce. Surface in-market accounts, prioritize outreach with topic-level signals, and connect intent to pipeline.",
        "overview": "Salesforce and Bombora appear together in 32 job postings, primarily in demand generation, ABM, and sales development roles. Bombora is the leading standalone intent data provider, tracking content consumption signals across a co-op of 5,000+ B2B websites. The Salesforce integration pushes account-level intent signals directly into CRM records, letting sales teams see which target accounts are actively researching relevant topics.\n\nBombora's Company Surge data measures when an account's research activity on specific topics exceeds its normal baseline. A spike in 'CRM software' or 'data enrichment' research signals that the company may be in-market. This surge data syncs to Salesforce account records, giving reps a data-driven reason to reach out.\n\nThe integration is especially valuable for outbound teams that need to prioritize which accounts to work. Instead of spraying outreach across an entire territory, reps focus on accounts showing buying signals. Teams using intent-prioritized outreach typically see 2-3x higher meeting conversion rates compared to cold outbound.",
        "how_they_work_together": [
            {
                "workflow": "Account-level intent scoring",
                "description": "Bombora pushes Company Surge scores to Salesforce account records as custom fields. Each score indicates how much an account's research on a specific topic exceeds its baseline. Reps see a numeric surge score and the specific topics being researched, making it easy to spot accounts that are actively evaluating solutions."
            },
            {
                "workflow": "Topic-based prioritization",
                "description": "Bombora tracks intent across thousands of B2B topics. Sales teams configure which topics matter (CRM, sales automation, data quality, etc.) and Salesforce displays only relevant signals. A software company selling to sales teams would track 'sales engagement' and 'CRM implementation' topics, filtering out irrelevant research activity."
            },
            {
                "workflow": "ABM campaign triggers",
                "description": "When Bombora detects a surge at a target account, Salesforce workflows can trigger ABM actions: assign the account to a rep, create a task for outreach, update account tier, or enroll contacts in a Salesforce campaign. Intent signals become the starting gun for coordinated sales and marketing plays."
            },
            {
                "workflow": "Pipeline acceleration",
                "description": "For accounts already in the pipeline, Bombora intent data shows whether the buying committee is still actively researching. A deal stalling while the account researches competitor topics signals competitive risk. A surge in relevant topics during a deal cycle indicates the buyer is still engaged. Reps use these signals to time follow-ups and adjust messaging."
            },
            {
                "workflow": "Territory planning with intent overlay",
                "description": "Sales leaders overlay Bombora surge data on territory maps in Salesforce. Territories with more in-market accounts get more resources. Quarterly territory planning uses intent data to redistribute accounts based on current buying signals, not just static firmographics."
            }
        ],
        "setup_considerations": [
            "Bombora data syncs to Salesforce via a managed package or through middleware like a CDP or ABM platform (6sense, Demandbase). Direct Salesforce integration requires Bombora's Company Surge product, which is sold separately from their data co-op membership.",
            "Select your topic clusters carefully. Bombora tracks thousands of topics, but tracking too many creates noise. Start with 10-15 topics directly related to your product category and buying triggers. Refine quarterly based on which topics correlate with closed-won deals.",
            "Bombora scores update weekly, not in real time. Plan your workflow triggers around weekly refresh cycles. A surge score from Monday reflects the prior week's research activity. Don't expect same-day intent signals.",
            "Combine Bombora intent with other signals in your Salesforce scoring model. Intent alone isn't enough to qualify an account. Layer Bombora surge data with firmographic fit, existing CRM engagement, and website activity for a more complete picture.",
            "Bombora works at the account level, not the contact level. You'll know that Acme Corp is surging on 'data enrichment,' but not which individual at Acme Corp is doing the research. Pair with a contact-level tool like ZoomInfo or Cognism to find the right people at surging accounts."
        ],
        "faq": [
            {
                "q": "How much does Bombora cost?",
                "a": "Bombora doesn't publish pricing. Company Surge data contracts typically start at $25K-40K/year for mid-market companies, with enterprise deals running $60K-100K/year depending on account volume and topic coverage. Many teams access Bombora data bundled through ABM platforms like 6sense or Demandbase rather than buying direct."
            },
            {
                "q": "How is Bombora different from 6sense or Demandbase intent data?",
                "a": "Bombora is a pure-play intent data provider. It sells data, not a platform. 6sense and Demandbase are ABM platforms that bundle Bombora's data (and other sources) with their own analytics, orchestration, and advertising features. If you want intent data in Salesforce without a full ABM platform, Bombora direct is the simpler path."
            },
            {
                "q": "How accurate is Bombora's intent data?",
                "a": "Bombora's data comes from a co-op of 5,000+ B2B publisher websites, which gives it broad coverage. Accuracy depends on topic selection and your threshold settings. Not every surging account is in-market for your product. Teams that calibrate their topics and combine intent with firmographic fit report 2-3x better outbound conversion rates versus no intent data."
            }
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },

    # 6. clay-outreach-io (enrichment to sequences)
    {
        "slug": "clay-outreach-io",
        "tool_a": "clay",
        "tool_b": "outreach-io",
        "cooccurrence_count": 25,
        "title": "Clay + Outreach Integration Guide",
        "meta_description": "How to integrate Clay with Outreach. Build enriched prospect lists and push them directly into Outreach sequences for automated, personalized outreach at scale.",
        "overview": "Clay and Outreach appear together in 25 job postings, concentrated in sales development and growth operations roles. Clay handles the upstream work of finding, enriching, and qualifying prospects from multiple data sources. Outreach handles the downstream execution of multi-channel sales sequences. Together, they form a complete pipeline from raw prospect data to booked meetings.\n\nThe combination is especially powerful for teams running high-volume outbound. Clay's enrichment waterfall produces higher-quality contact data than any single provider. Outreach's sequencing engine automates the follow-up cadence across email, phone, and LinkedIn. The handoff between enrichment and execution is where most outbound teams lose efficiency, and this integration eliminates that gap.\n\nTeams that previously built prospect lists in spreadsheets, manually verified emails, and copy-pasted contacts into Outreach can now automate the entire flow. Clay enriches, scores, and personalizes. Outreach sequences and tracks.",
        "how_they_work_together": [
            {
                "workflow": "Enrichment to sequence pipeline",
                "description": "Clay builds prospect lists from multiple data sources, enriches each record with verified emails and firmographic data, then pushes qualified contacts directly into Outreach sequences. The entire flow from data sourcing to sequence enrollment can run automatically, triggered by ICP match criteria."
            },
            {
                "workflow": "AI-personalized outreach",
                "description": "Clay uses AI to generate personalized email snippets for each prospect based on enriched data points (recent company news, tech stack, job postings, funding rounds). These personalization fields push to Outreach as custom prospect attributes, and the sequence templates pull them in dynamically."
            },
            {
                "workflow": "Multi-source data validation",
                "description": "Before loading contacts into Outreach, Clay cross-references email addresses across multiple providers and runs deliverability checks. This pre-validation reduces Outreach bounce rates and protects sender reputation. Contacts with invalid or unverifiable emails get filtered out before they enter a sequence."
            },
            {
                "workflow": "Account-based sequence assignment",
                "description": "Clay enriches accounts with firmographic data and assigns them to segments (enterprise, mid-market, SMB). Different segments map to different Outreach sequences with tailored messaging, cadence timing, and channel mix. A mid-market SaaS company gets a different outreach experience than an enterprise manufacturer."
            },
            {
                "workflow": "Performance feedback loop",
                "description": "Outreach reply and meeting data can feed back into Clay to refine ICP scoring and enrichment priorities. If contacts from a specific industry or company size convert at higher rates, Clay adjusts the scoring model to prioritize similar prospects in future list builds."
            }
        ],
        "setup_considerations": [
            "Clay connects to Outreach via API. You'll need an Outreach admin to generate API credentials and whitelist Clay's integration. The connection allows Clay to create prospects and add them to sequences, but Outreach sequence configuration stays in the Outreach platform.",
            "Map Clay's enriched fields to Outreach custom prospect fields before your first data push. Personalization fields (company news snippet, tech stack, funding data) need corresponding Outreach fields to land correctly. Unmapped fields get dropped during the sync.",
            "Set up email deliverability guardrails in Outreach before loading high volumes from Clay. New sender domains should warm up gradually (50 emails/day, increasing weekly). Pushing 500 enriched contacts into sequences on day one will trigger spam filters.",
            "Use Clay's filtering to control which prospects enter Outreach sequences. Not every enriched contact should get sequenced. Filter by ICP score, email deliverability confidence, and recency of data. Loading stale or low-fit contacts into Outreach wastes sequence capacity and hurts reply rates.",
            "Coordinate with your CRM. Both Clay and Outreach connect to Salesforce or HubSpot. Decide whether Clay pushes to the CRM first (then Outreach pulls from CRM) or pushes directly to Outreach. Direct-to-Outreach is faster but may create CRM sync gaps if contacts don't exist in Salesforce yet."
        ],
        "faq": [
            {
                "q": "Can Clay replace Outreach's built-in prospect search?",
                "a": "For data sourcing and enrichment, yes. Clay's multi-provider waterfall and AI enrichment are more capable than Outreach's native prospect data. But Outreach is the execution layer: email sequencing, phone tasks, LinkedIn steps, analytics. Use Clay for the data, Outreach for the outreach."
            },
            {
                "q": "How does this compare to using Apollo or ZoomInfo with Outreach?",
                "a": "Apollo and ZoomInfo provide single-source data. Clay aggregates 50+ data sources into a waterfall, which typically produces 15-30% higher email coverage. Clay also adds AI personalization that Apollo and ZoomInfo don't offer. The tradeoff is complexity: Clay requires more setup than plugging Apollo directly into Outreach."
            },
            {
                "q": "How much does the Clay + Outreach stack cost?",
                "a": "Clay starts at $149/month (Explorer). Outreach doesn't publish pricing but typically runs $100-150/user/month for sales teams. For a 10-rep SDR team, expect $1,500-2,000/month for Outreach plus $300-500/month for Clay, depending on enrichment volume. The combined cost is competitive with all-in-one platforms like Apollo, with better data quality."
            }
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },

    # 7. hubspot-gong-engage (conversation intel + CRM)
    {
        "slug": "hubspot-gong-engage",
        "tool_a": "hubspot",
        "tool_b": "gong-engage",
        "cooccurrence_count": 35,
        "title": "HubSpot + Gong Engage Integration Guide",
        "meta_description": "How to integrate Gong with HubSpot. Sync call recordings, surface conversation insights in your CRM, and use deal intelligence to improve sales execution.",
        "overview": "HubSpot and Gong appear together in 35 job postings, spanning sales operations, enablement, and management roles. Gong Engage (formerly Gong's core revenue intelligence platform) records and analyzes sales conversations across calls, video meetings, and emails. The HubSpot integration syncs conversation data, deal insights, and coaching signals directly into CRM records, giving managers and reps a complete view of deal health.\n\nThe practical value is that HubSpot becomes the single pane of glass for deal information. Instead of checking Gong separately for call notes and HubSpot for deal stages, reps and managers see conversation highlights, risk signals, and next steps right on the deal record. This saves time and improves forecast accuracy because the data reflects what was said on calls, not just what reps entered into the CRM.\n\nGong's AI analyzes every recorded interaction for talk-to-listen ratio, competitor mentions, pricing discussions, next steps, and buyer sentiment. These insights push to HubSpot as deal properties and timeline activities, making deal reviews and pipeline inspections more data-driven.",
        "how_they_work_together": [
            {
                "workflow": "Call recording sync",
                "description": "Gong automatically records sales calls and video meetings, then syncs recordings and AI-generated summaries to HubSpot deal and contact timelines. Reps don't need to manually log call notes. Managers can review any conversation from within HubSpot."
            },
            {
                "workflow": "Deal risk detection",
                "description": "Gong analyzes conversation patterns to flag deal risks: declining engagement, competitor mentions, stalled next steps, or single-threaded deals (only one contact engaged). These risk signals push to HubSpot deal records as custom properties, making pipeline reviews more accurate."
            },
            {
                "workflow": "Forecasting with conversation data",
                "description": "HubSpot's pipeline reports become more reliable when supplemented with Gong's deal engagement scores. A deal in 'negotiation' stage where the buyer hasn't responded to three follow-ups scores differently than one with active back-and-forth. Gong's engagement data adds a layer of truth to CRM-based forecasting."
            },
            {
                "workflow": "Coaching and enablement",
                "description": "Managers identify coaching opportunities from Gong's conversation analytics: reps who talk too much, skip discovery questions, or don't confirm next steps. These metrics are visible alongside HubSpot performance data, connecting conversation quality to pipeline outcomes."
            },
            {
                "workflow": "Competitive intelligence aggregation",
                "description": "Gong tracks competitor mentions across all recorded sales conversations and aggregates them by frequency and context. This competitive intel syncs to HubSpot at the deal level, showing which competitors were discussed and how prospects framed the comparison. Product marketing uses this data to refine competitive positioning."
            }
        ],
        "setup_considerations": [
            "Gong requires calendar and conferencing tool access to auto-record calls. Connect Google Calendar or Outlook Calendar, plus Zoom, Microsoft Teams, or Google Meet. Recording starts automatically for external meetings unless you configure exclusions for internal calls.",
            "Set up contact and deal matching rules between Gong and HubSpot. Gong matches recorded calls to HubSpot records using email addresses and meeting participant data. Clean contact data in HubSpot improves match accuracy. Unmatched recordings don't sync to CRM records.",
            "Review call recording consent requirements for your market. Many US states and most European countries require two-party consent for call recording. Gong can display consent notices at the start of calls, but your legal team should approve the specific language and process.",
            "Gong's HubSpot integration requires admin access on both platforms. The initial setup maps Gong deal boards to HubSpot pipelines and configures which insights push as deal properties. Budget 1-2 weeks for configuration and testing before rolling out to the full team.",
            "Train managers to use Gong insights in HubSpot deal reviews. The value compounds when managers reference conversation data during pipeline inspections instead of relying solely on rep-entered CRM data. Without manager adoption, the integration generates data that nobody acts on."
        ],
        "faq": [
            {
                "q": "How much does Gong cost?",
                "a": "Gong doesn't publish pricing. Based on market data, plans typically start at $100-150/user/month with annual contracts. Enterprise deals with full platform access (recording, deal intelligence, forecasting, coaching) run $130-175/user/month. Minimum seat counts often apply. The HubSpot integration is included in all plans."
            },
            {
                "q": "Does HubSpot's built-in call recording replace Gong?",
                "a": "HubSpot's calling tools record calls made through HubSpot, but they don't analyze conversations with AI, detect deal risks, track competitor mentions, or provide coaching insights. Gong's value is in the intelligence layer on top of recording. Teams that just need basic call logging may not need Gong. Teams that want data-driven coaching and forecasting do."
            },
            {
                "q": "Can Gong work with HubSpot Free or Starter plans?",
                "a": "Gong's HubSpot integration works with Sales Hub Professional and Enterprise, which provide the custom properties and API access needed for full data sync. Free and Starter plans have limited custom properties and may not support all Gong sync features."
            }
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },

    # 8. salesforce-demandtools (data quality)
    {
        "slug": "salesforce-demandtools",
        "tool_a": "salesforce",
        "tool_b": "demandtools",
        "cooccurrence_count": 20,
        "title": "Salesforce + DemandTools Integration Guide",
        "meta_description": "How to integrate DemandTools with Salesforce. Deduplicate records, mass-update fields, standardize data, and maintain CRM hygiene at scale.",
        "overview": "Salesforce and DemandTools appear together in 20 job postings, primarily in Salesforce administration and revenue operations roles. DemandTools (by Validity, formerly a standalone product) is a data quality toolkit built specifically for Salesforce. It handles the data maintenance tasks that Salesforce admins deal with daily: deduplication, mass updates, data standardization, and import/export operations.\n\nSalesforce's native data management tools are limited. Built-in duplicate rules catch some matches, but they can't handle fuzzy matching, cross-object deduplication, or bulk merge operations. DemandTools fills this gap with a desktop application that connects directly to Salesforce and processes records in bulk.\n\nThis pairing is common in organizations with 50K+ Salesforce records where data entropy is a real problem. Bad data compounds: duplicate accounts fragment sales activity, incorrect fields break automation, and stale records waste outreach effort. DemandTools is the tool ops teams use to fight that entropy.",
        "how_they_work_together": [
            {
                "workflow": "Record deduplication",
                "description": "DemandTools identifies duplicate leads, contacts, accounts, and custom objects in Salesforce using fuzzy matching algorithms. It handles variations that Salesforce native rules miss: 'IBM' vs 'International Business Machines,' 'John Smith' vs 'J. Smith,' or records with transposed fields. Merge operations consolidate duplicates into master records while preserving the most complete data."
            },
            {
                "workflow": "Mass data updates",
                "description": "DemandTools updates thousands of Salesforce records in a single operation: standardizing state abbreviations, normalizing phone formats, backfilling missing fields from CSV imports, or reassigning records between owners. Bulk updates that would take hours of manual editing in Salesforce complete in minutes."
            },
            {
                "workflow": "Data standardization",
                "description": "DemandTools enforces data standards across Salesforce records. It normalizes company names ('Co.' to 'Company'), standardizes addresses, formats phone numbers, and cleans up free-text fields. Standardized data improves report accuracy, automation reliability, and duplicate matching."
            },
            {
                "workflow": "Import and migration support",
                "description": "When importing data from external sources (marketing lists, acquired company CRMs, enrichment providers), DemandTools previews matches against existing Salesforce records before loading. This prevents creating duplicates during import and lets admins review merge decisions before committing."
            },
            {
                "workflow": "Scheduled data quality jobs",
                "description": "DemandTools can run deduplication and standardization jobs on a schedule, catching new duplicates as they're created. Weekly or monthly hygiene jobs keep data quality from degrading between manual cleanup sessions."
            }
        ],
        "setup_considerations": [
            "DemandTools is a desktop application (Windows) that connects to Salesforce via API. Mac users need a Windows VM or cloud desktop. The application requires Salesforce admin credentials and sufficient API call allocation for bulk operations.",
            "Always run DemandTools operations in a Salesforce sandbox first. Bulk merge and mass update operations are difficult to reverse. Test your matching rules and update logic on a sandbox copy of production data before running against live records.",
            "Set up matching rules carefully for deduplication. Overly aggressive matching creates false positives (merging records that shouldn't be merged). Start with strict matching (exact email domain + similar name) and gradually loosen criteria as you gain confidence in the results.",
            "DemandTools operations consume Salesforce API calls. A large deduplication run on 100K records can use thousands of API calls. Monitor your org's daily API limit and schedule heavy operations during off-peak hours.",
            "Document your DemandTools processes. Data quality operations should be repeatable and auditable. Create saved job configurations for recurring tasks (monthly dedup, quarterly standardization) so any admin can run them consistently."
        ],
        "faq": [
            {
                "q": "How much does DemandTools cost?",
                "a": "DemandTools is part of Validity's data quality suite. Pricing isn't published, but market estimates put it at $15K-30K/year for a standard license. It's often bundled with Validity's other Salesforce tools (GridBuddy, Everest). Some organizations negotiate DemandTools access as part of a broader Validity contract."
            },
            {
                "q": "Can Salesforce's native duplicate management replace DemandTools?",
                "a": "For basic duplicate prevention on new records, Salesforce's built-in duplicate rules work. But Salesforce can't do bulk retroactive deduplication, fuzzy matching across objects, mass merges, or data standardization. If your org has existing duplicate problems or needs ongoing data hygiene at scale, you'll need DemandTools or a similar tool."
            },
            {
                "q": "Is DemandTools safe for production Salesforce orgs?",
                "a": "Yes, with precautions. DemandTools has been used on Salesforce production orgs for 15+ years. It includes preview modes, undo capabilities for some operations, and sandbox testing support. The risk comes from running bulk operations without testing. Always preview results, test in sandbox, and start with small batches before processing your full database."
            }
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },

    # 9. apollo-instantly (data + deliverability)
    {
        "slug": "apollo-instantly",
        "tool_a": "apollo",
        "tool_b": "instantly",
        "cooccurrence_count": 42,
        "title": "Apollo + Instantly Integration Guide",
        "meta_description": "How to use Apollo and Instantly together. Source contacts from Apollo's database and send cold outreach through Instantly's deliverability engine.",
        "overview": "Apollo and Instantly appear together in 42 job postings, making it one of the most common pairings in the outbound sales stack. Apollo provides the contact database and enrichment. Instantly provides the email sending infrastructure optimized for cold outreach deliverability. Teams use Apollo to find the right people and Instantly to reach their inbox.\n\nThe split makes sense because the two tools solve different problems. Apollo has a database of 250M+ contacts with verified emails, but its built-in email sending is limited in volume and deliverability features. Instantly doesn't have a contact database, but its email infrastructure supports unlimited sending accounts, automatic warmup, rotation, and deliverability monitoring. Combining them gives you the best data source with the best sending engine.\n\nThis stack is the default for teams running high-volume outbound (500+ emails per day). Apollo handles prospecting and data quality. Instantly handles email warmup, domain rotation, and inbox placement. The result is more emails landing in primary inboxes rather than spam folders.",
        "how_they_work_together": [
            {
                "workflow": "Prospect sourcing to sending",
                "description": "Reps build prospect lists in Apollo using firmographic and technographic filters (industry, company size, tech stack, job title). Verified contact data exports from Apollo as CSV and imports directly into Instantly campaigns. The handoff is manual (CSV export/import) but takes under five minutes for a list of 1,000 contacts."
            },
            {
                "workflow": "Email verification pipeline",
                "description": "Apollo provides email addresses, and Instantly runs additional deliverability verification before sending. Instantly flags risky addresses (catch-all domains, temporary emails, full inboxes) that would hurt sender reputation. This double verification layer catches addresses that pass Apollo's verification but would still bounce."
            },
            {
                "workflow": "Multi-domain sending at scale",
                "description": "Instantly supports unlimited sending accounts and domains, rotating emails across them automatically. A team sending 1,000 cold emails per day might use 10 domains with 5 mailboxes each, keeping per-account volume under spam thresholds. Apollo provides the contacts; Instantly distributes the sending load."
            },
            {
                "workflow": "Warmup and reputation management",
                "description": "Instantly's email warmup feature sends and receives emails between its network of accounts to build sender reputation before cold outreach begins. New domains warm up for 2-3 weeks before being added to campaign rotation. Apollo contacts don't receive warmup emails, only real campaign messages."
            },
            {
                "workflow": "Reply handling and CRM sync",
                "description": "Instantly detects positive replies and can forward them to your CRM or notify reps via Slack. Apollo's CRM integration tracks which contacts were sourced and enriched through Apollo. Together, the tools provide full attribution from data source through email engagement to booked meeting."
            }
        ],
        "setup_considerations": [
            "The Apollo-to-Instantly handoff is CSV-based. Export contacts from Apollo with email, first name, last name, company, and any personalization fields. Import into Instantly and map columns to campaign variables. There's no native API integration between the two platforms.",
            "Set up Instantly's email warmup 2-3 weeks before launching your first campaign. Warmup builds sender reputation with email providers (Gmail, Outlook). Skipping warmup is the most common mistake and leads to immediate spam folder placement.",
            "Use separate domains for cold outreach. Don't send cold emails from your primary company domain (yourcompany.com). Buy lookalike domains (getyourcompany.com, tryyourcompany.io) and use those in Instantly. This protects your primary domain's reputation.",
            "Apollo's email verification isn't perfect. Run Instantly's built-in verification on every list before adding contacts to a campaign. The 2-5% of emails that Apollo verifies but Instantly flags can make the difference between good and bad deliverability."
        ],
        "faq": [
            {
                "q": "Why not just use Apollo's built-in email sequencing?",
                "a": "Apollo's email sending works for low-to-moderate volume (under 200 emails/day). But it doesn't support unlimited sending accounts, automatic domain rotation, or the same level of warmup infrastructure that Instantly provides. If you're sending 500+ cold emails per day, Instantly's deliverability features are worth the additional cost."
            },
            {
                "q": "How much does the Apollo + Instantly stack cost?",
                "a": "Apollo Basic is $49/month with 900 email credits. Instantly's Growth plan starts at $30/month for 1,000 contacts and 5,000 emails. A typical SDR team running 1,000 emails/day spends $99-199/month on Apollo (Professional) and $77-97/month on Instantly (Hypergrowth). Total: $175-300/month, well under most sales engagement platform pricing."
            },
            {
                "q": "Can I use Instantly with data from providers other than Apollo?",
                "a": "Yes. Instantly accepts contacts from any source via CSV import. Teams commonly use ZoomInfo, Clay, Cognism, or even LinkedIn Sales Navigator exports alongside or instead of Apollo. Instantly doesn't care where the data comes from as long as the email addresses are valid."
            }
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },

    # 10. zapier-clay (automation + enrichment)
    {
        "slug": "zapier-clay",
        "tool_a": "zapier",
        "tool_b": "clay",
        "cooccurrence_count": 30,
        "title": "Zapier + Clay Integration Guide",
        "meta_description": "How to connect Zapier with Clay. Trigger enrichment workflows from any app, automate prospect research, and connect Clay's data to 5,000+ tools.",
        "overview": "Zapier and Clay appear together in 30 job postings, primarily in growth operations and marketing operations roles. Zapier is the general-purpose automation platform connecting 5,000+ apps. Clay is the data enrichment and research platform. Together, they let teams trigger Clay enrichment workflows from virtually any business event and push enriched data to any downstream tool.\n\nThe combination is powerful because Clay has deep enrichment capabilities but limited native integrations. Zapier extends Clay's reach to every tool in the stack. A new Typeform submission can trigger Clay enrichment. A new Salesforce lead can kick off a Clay waterfall. Enriched data from Clay can push to Outreach, Slack, Google Sheets, or any Zapier-connected app.\n\nThis pairing is popular with operations teams that don't have engineering resources to build custom API integrations. Zapier provides the no-code connectivity layer; Clay provides the data intelligence. Together, they create enrichment automation that would otherwise require a developer to build and maintain.",
        "how_they_work_together": [
            {
                "workflow": "Event-triggered enrichment",
                "description": "Zapier triggers Clay enrichment when specific events occur: a new form submission, a CRM record creation, a calendar booking, or a Slack message. The trigger passes basic data (email, company name) to Clay, which runs a full enrichment waterfall and returns 50+ data points."
            },
            {
                "workflow": "Multi-app data routing",
                "description": "After Clay enriches a record, Zapier routes the data to multiple destinations based on the results. High-ICP prospects go to the CRM and Outreach. Low-fit leads go to a nurture list. Unverified emails get flagged for review. Zapier handles the conditional routing that Clay doesn't natively support."
            },
            {
                "workflow": "Automated prospect research",
                "description": "Zapier monitors data sources (Google Sheets, Airtable, CRM reports) for new prospect entries. When a new row appears, Zapier sends it to Clay for enrichment: company data, tech stack, recent news, job postings, and decision-maker contacts. The enriched profile returns to the original source or pushes to a prospecting tool."
            },
            {
                "workflow": "Lead qualification automation",
                "description": "Zapier connects form submissions to Clay for instant enrichment, then uses the enriched data to qualify the lead. Company size under 50? Route to self-serve. Revenue over $10M and using a competitor? Fast-track to sales. The qualification logic runs in Zapier based on Clay's enrichment output."
            },
            {
                "workflow": "Scheduled bulk enrichment",
                "description": "Zapier's scheduled triggers can batch-process records through Clay on a recurring basis. Weekly CRM hygiene: pull stale records, enrich through Clay, update the CRM with fresh data. Monthly list refresh: re-enrich existing prospect lists to catch job changes and company updates."
            }
        ],
        "setup_considerations": [
            "Clay connects to Zapier as both a trigger (Clay enrichment completes) and an action (start Clay enrichment). Set up both directions to create full round-trip workflows: Zapier triggers Clay, Clay enriches, Zapier routes the results.",
            "Watch your Zapier task usage. Each step in a Zap consumes one Zapier task. A workflow with trigger, Clay enrichment, conditional logic, and CRM update uses 4+ tasks per record. High-volume enrichment pipelines can burn through Zapier's monthly task limit quickly.",
            "Clay's API rate limits and credit consumption apply when triggered via Zapier. Set up rate limiting in your Zaps to avoid overwhelming Clay's API during high-volume events. Zapier's built-in throttling feature can space out requests.",
            "Test enrichment latency. Clay's waterfall enrichment can take 10-60 seconds per record depending on complexity. Zapier workflows that expect instant responses may time out. Use Zapier's webhook-based approach with asynchronous callbacks for enrichment workflows that take longer than 30 seconds."
        ],
        "faq": [
            {
                "q": "Can Make (Integromat) work with Clay instead of Zapier?",
                "a": "Yes. Clay has an API that works with any automation platform, including Make, n8n, and Tray. Zapier has the broadest app library (5,000+), but Make is often cheaper at high volumes. The Clay connection works similarly across all platforms: trigger enrichment via API, receive results via webhook."
            },
            {
                "q": "How much does the Zapier + Clay combination cost?",
                "a": "Zapier Starter is $29.99/month for 750 tasks. Clay Explorer is $149/month. For a team running 1,000 enrichments per month with multi-step Zaps, expect $50-80/month for Zapier (Professional tier) plus $149-349/month for Clay depending on credit usage. Total: $200-430/month."
            },
            {
                "q": "Is this approach better than building custom API integrations?",
                "a": "For most teams, yes. Custom API integrations between Clay and other tools require engineering time to build and maintain. Zapier handles the connectivity with no code. The tradeoff is flexibility and cost at scale: custom integrations are cheaper per transaction at high volumes and can handle complex logic that Zapier can't. But for teams processing under 10,000 records per month, Zapier is faster to set up and easier to modify."
            }
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },

    # 11. hubspot-leadiq (prospecting + CRM)
    {
        "slug": "hubspot-leadiq",
        "tool_a": "hubspot",
        "tool_b": "leadiq",
        "cooccurrence_count": 24,
        "title": "HubSpot + LeadIQ Integration Guide",
        "meta_description": "How to integrate LeadIQ with HubSpot. Capture prospect data from LinkedIn, enrich contacts, and push verified leads directly into your HubSpot CRM.",
        "overview": "HubSpot and LeadIQ appear together in 24 job postings, concentrated in sales development and inside sales roles. LeadIQ is a prospecting tool that lets SDRs capture contact data (email, phone, title) from LinkedIn profiles and company websites with one click. The HubSpot integration pushes captured contacts directly into the CRM as new contacts or appends data to existing records.\n\nThe combination solves a specific workflow problem: SDRs find prospects on LinkedIn, but getting that data into HubSpot requires manual entry or CSV imports. LeadIQ eliminates that friction. Click a button on a LinkedIn profile, and the contact's verified email, phone number, and company details land in HubSpot within seconds.\n\nLeadIQ differentiates from larger platforms like ZoomInfo and Apollo by focusing tightly on the SDR prospecting workflow. It's lighter, cheaper, and faster for the specific use case of LinkedIn-to-CRM data capture. Teams that don't need a full data platform but want their SDRs to prospect efficiently find this pairing effective.",
        "how_they_work_together": [
            {
                "workflow": "LinkedIn-to-CRM capture",
                "description": "LeadIQ's Chrome extension sits on top of LinkedIn and Sales Navigator. When an SDR finds a prospect, one click captures the contact's email, phone, title, and company details. The data pushes to HubSpot as a new contact with all fields populated. No copy-pasting, no tab switching, no manual data entry."
            },
            {
                "workflow": "Account-aware prospecting",
                "description": "LeadIQ syncs with HubSpot to show which contacts and companies already exist in the CRM. When prospecting on LinkedIn, reps see a badge indicating whether the person is already a HubSpot contact. This prevents creating duplicates and helps reps focus on net-new prospects."
            },
            {
                "workflow": "Sequence enrollment from capture",
                "description": "After capturing a contact via LeadIQ, reps can immediately add them to a HubSpot sequence from the same interface. The contact is created in HubSpot and enrolled in the outreach sequence in one action, compressing the time from prospecting to first touch."
            },
            {
                "workflow": "Team prospecting analytics",
                "description": "LeadIQ tracks prospecting activity per rep: contacts captured, emails found, push-to-CRM rates. Managers compare this with HubSpot pipeline data to see which SDRs are generating the most pipeline from their prospecting activity. The data connects effort (contacts captured) to outcome (meetings booked)."
            },
            {
                "workflow": "Contact data enrichment",
                "description": "For existing HubSpot contacts with missing data, LeadIQ can fill gaps. Reps view a LinkedIn profile, and LeadIQ checks whether the corresponding HubSpot contact has a phone number or updated title. Missing fields get updated in HubSpot without creating a new record."
            }
        ],
        "setup_considerations": [
            "Install LeadIQ's Chrome extension and connect it to your HubSpot instance via OAuth. The connection requires HubSpot admin approval. Once connected, all team members using LeadIQ can push contacts to HubSpot under their own user permissions.",
            "Configure field mappings between LeadIQ and HubSpot. Default mappings cover standard fields (email, phone, company, title). Custom HubSpot properties need manual mapping in LeadIQ's settings. Unmapped fields from LeadIQ won't sync to HubSpot.",
            "Set duplicate handling rules. When LeadIQ pushes a contact that already exists in HubSpot, decide whether to update the existing record, skip the push, or create a new record. Most teams choose 'update existing' to keep data fresh without creating duplicates.",
            "LeadIQ's data comes from its own database and third-party sources. Email accuracy runs around 90-95% for business emails. Phone number coverage is lower, around 50-60% for direct dials. Set expectations with SDRs that not every capture will include a phone number."
        ],
        "faq": [
            {
                "q": "How does LeadIQ compare to Apollo for HubSpot users?",
                "a": "LeadIQ is focused on the SDR workflow: capture contacts from LinkedIn and push to CRM. Apollo is a broader platform with a larger database, built-in sequencing, and enrichment features. LeadIQ is simpler, cheaper ($39/user/month vs Apollo's $49+), and faster for the specific LinkedIn-to-CRM use case. Apollo is better if you need a database for list building beyond LinkedIn."
            },
            {
                "q": "Does LeadIQ require LinkedIn Sales Navigator?",
                "a": "No. LeadIQ works on regular LinkedIn as well as Sales Navigator. However, Sales Navigator gives access to more advanced search filters and a larger pool of profiles. SDRs using LeadIQ with regular LinkedIn can still capture contact data from any profile they can view."
            },
            {
                "q": "How much does LeadIQ cost?",
                "a": "LeadIQ offers a free plan with 20 verified emails per week. The Essential plan is $39/user/month with 500 verified emails. Pro is $79/user/month with unlimited email lookups and phone numbers. For SDR teams of 5-10 reps, expect $400-800/month total depending on the plan tier."
            }
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },

    # 12. salesforce-common-room (community signals + CRM)
    {
        "slug": "salesforce-common-room",
        "tool_a": "salesforce",
        "tool_b": "common-room",
        "cooccurrence_count": 20,
        "title": "Salesforce + Common Room Integration Guide",
        "meta_description": "How to integrate Common Room with Salesforce. Turn community engagement, product signals, and digital body language into CRM-ready sales intelligence.",
        "overview": "Salesforce and Common Room appear together in 18 job postings, primarily in product-led growth, developer relations, and revenue operations roles. Common Room is a digital signals platform that aggregates engagement data from community channels (Slack, Discord, GitHub, Stack Overflow), product usage, social media, and other digital touchpoints. The Salesforce integration pushes these signals into CRM records so sales teams can see who is engaged with your product ecosystem before they ever fill out a form.\n\nThis pairing is especially common at companies with product-led growth motions, open-source projects, or active developer communities. Traditional CRM data captures leads who raise their hand via forms or demo requests. Common Room captures the much larger group of people who are engaging with your product or community but haven't entered the sales funnel yet. These are your warmest prospects, and they're invisible without a tool like Common Room.\n\nThe integration surfaces community engagement as account and contact intelligence in Salesforce. A developer who starred your GitHub repo, asked questions in your Slack community, and commented on your blog post shows up in Salesforce with that full engagement history. Sales reps know who the champions are before making their first call.",
        "how_they_work_together": [
            {
                "workflow": "Community-to-CRM signal sync",
                "description": "Common Room aggregates engagement signals from Slack, Discord, GitHub, Twitter/X, LinkedIn, Stack Overflow, and other community channels. These signals sync to Salesforce as activities on contact and account records. Reps see community participation history alongside traditional CRM data."
            },
            {
                "workflow": "Product-qualified lead identification",
                "description": "Common Room identifies users who show buying signals through community and product engagement: frequent feature questions, integration requests, scaling discussions, or enterprise-tier interest. These product-qualified leads push to Salesforce with engagement scores and context, letting sales prioritize based on product interest."
            },
            {
                "workflow": "Champion identification",
                "description": "Common Room tracks which individuals at target accounts are most engaged with your community and content. These champions surface in Salesforce as contacts with high engagement scores. Reps can reference specific community interactions when reaching out, creating warm rather than cold first touches."
            },
            {
                "workflow": "Account intelligence enrichment",
                "description": "Common Room enriches Salesforce account records with community metrics: number of community members at the account, engagement trends (increasing or declining), and topics of interest. Sales leaders use this data to prioritize accounts where community engagement suggests expansion or churn risk."
            },
            {
                "workflow": "Automated lead routing based on signals",
                "description": "When Common Room detects high-value signals (enterprise pricing questions, competitive comparisons, integration requests), it can trigger Salesforce workflows that route the contact to the appropriate sales rep, create a task, or enroll the contact in a sales cadence. Digital body language becomes a pipeline trigger."
            }
        ],
        "setup_considerations": [
            "Common Room needs access to your community platforms (Slack workspace, Discord server, GitHub organization, etc.) to ingest engagement data. The Salesforce integration is separate and requires admin access on both platforms. Set up the community connections first, then configure the CRM sync.",
            "Define which community signals should sync to Salesforce. Not every Slack message or GitHub star needs to become a CRM activity. Configure Common Room to push high-value signals (pricing questions, enterprise-tier discussions, competitive mentions) and roll up lower-value signals as aggregate scores.",
            "Common Room identifies community members by email, username, and social profile matching. The accuracy of Salesforce record matching depends on how well community member emails align with CRM contact emails. Personal emails in community platforms vs. business emails in Salesforce can cause matching gaps.",
            "Set engagement score thresholds for sales alerts. Common Room assigns engagement scores to contacts and accounts. Work with sales to define what score warrants a rep notification versus passive enrichment. Setting the threshold too low creates alert fatigue; too high means missing warm prospects."
        ],
        "faq": [
            {
                "q": "What types of companies benefit most from Common Room + Salesforce?",
                "a": "Companies with active developer communities, open-source products, Slack/Discord user communities, or product-led growth motions get the most value. If your buyers engage with your product or community before talking to sales, Common Room captures that pre-sales engagement. B2B SaaS companies with self-serve or freemium tiers are the core use case."
            },
            {
                "q": "How much does Common Room cost?",
                "a": "Common Room offers a free Community tier with limited features. Paid plans start at $625/month (Team) with full CRM integration and signal routing. Enterprise pricing is custom and includes advanced analytics, custom integrations, and dedicated support. The Salesforce integration is included in paid plans."
            },
            {
                "q": "How is Common Room different from a CDP like Segment?",
                "a": "CDPs like Segment focus on product analytics and event tracking from your own application. Common Room focuses on external community and digital signals: Slack conversations, GitHub activity, social engagement, forum posts. There's some overlap in product usage tracking, but Common Room's strength is aggregating signals from places outside your product that CDPs don't monitor."
            }
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },
]


def main():
    # Load existing data
    with open(INTEGRATIONS_FILE, "r") as f:
        data = json.load(f)

    existing_slugs = {entry["slug"] for entry in data["integrations"]}

    added = []
    skipped = []

    for entry in NEW_INTEGRATIONS:
        slug = entry["slug"]
        if slug in existing_slugs:
            skipped.append(slug)
            print(f"  SKIP (already exists): {slug}")
        else:
            data["integrations"].append(entry)
            added.append(slug)
            print(f"  ADDED: {slug}")

    # Write back
    with open(INTEGRATIONS_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    # Summary
    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"  Added:   {len(added)} new integrations")
    print(f"  Skipped: {len(skipped)} (already existed)")
    print(f"  Total:   {len(data['integrations'])} integrations in file")

    if added:
        print(f"\nNew entries:")
        for slug in added:
            entry = next(e for e in NEW_INTEGRATIONS if e["slug"] == slug)
            print(f"  - {slug} (co-occurrence: {entry['cooccurrence_count']})")

    if skipped:
        print(f"\nSkipped entries:")
        for slug in skipped:
            print(f"  - {slug}")


if __name__ == "__main__":
    main()
