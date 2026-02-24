#!/usr/bin/env python3
"""
Add 14 new integration entries to data/integrations.json.

New pairs:
  salesforce-trustradius, salesforce-churnzero, salesforce-leandata,
  salesforce-chili-piper, salesforce-highspot, hubspot-chili-piper,
  hubspot-highspot, hubspot-churnzero, hubspot-leandata,
  zoominfo-leandata, zoominfo-highspot, g2-trustradius,
  clay-leandata, gainsight-churnzero
"""
import json
import sys
from pathlib import Path

DATA_DIR = Path("/Users/rome/Documents/projects/datastackguide/data")
INTEGRATIONS_FILE = DATA_DIR / "integrations.json"
DATE_PUBLISHED = "2026-02-20"
DATE_MODIFIED = "2026-02-20"


NEW_INTEGRATIONS = [
    # 1. salesforce-trustradius (8)
    {
        "slug": "salesforce-trustradius",
        "tool_a": "salesforce",
        "tool_b": "trustradius",
        "cooccurrence_count": 8,
        "title": "Salesforce + TrustRadius Integration Guide",
        "meta_description": "How to integrate TrustRadius with Salesforce. Route buyer intent signals into your CRM, prioritize in-market accounts, and connect review data to pipeline.",
        "overview": "Salesforce and TrustRadius appear together in 8 job postings, reflecting a growing pattern of connecting buyer intent data from review platforms into CRM workflows. TrustRadius captures purchase intent signals when buyers research products on the platform, and the integration pushes those signals into Salesforce so sales teams can prioritize accounts showing active buying behavior.",
        "how_they_work_together": [
            {
                "workflow": "Buyer intent alerts",
                "description": "TrustRadius detects when prospects research your product category, read reviews, or compare vendors. These intent signals push into Salesforce as activities or custom fields on the account record, giving reps real-time visibility into who is actively evaluating solutions."
            },
            {
                "workflow": "Account prioritization",
                "description": "Intent data from TrustRadius feeds Salesforce lead scoring models. Accounts that viewed your product page, read competitor comparisons, or downloaded TrustRadius reports score higher, helping reps focus on buyers who are already in-market."
            },
            {
                "workflow": "Competitive intelligence",
                "description": "TrustRadius tracks which competitor products a prospect researched before or after viewing yours. This competitive context syncs to Salesforce, letting reps tailor their pitch based on which alternatives the buyer is actively evaluating."
            },
            {
                "workflow": "Review-driven social proof",
                "description": "Sales reps pull relevant TrustRadius reviews and ratings into Salesforce-generated proposals and outreach. Industry-specific reviews can be matched to prospect segments for targeted social proof during the sales cycle."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "Data mapping",
                "detail": "Map TrustRadius intent categories to Salesforce account fields before enabling the sync. Decide which intent signals (product page views, comparison visits, review reads) warrant CRM alerts versus passive field updates."
            },
            {
                "consideration": "TrustRadius plan requirements",
                "detail": "Buyer intent data and CRM integrations are only available on TrustRadius for Vendors paid plans. Free profiles on TrustRadius do not include intent signal delivery or Salesforce connectors."
            },
            {
                "consideration": "Lead scoring adjustments",
                "detail": "Add TrustRadius intent signals as scoring criteria in your Salesforce lead scoring model. Most teams weight review platform research at 15-25 points, similar to pricing page visits, since it indicates active evaluation."
            },
            {
                "consideration": "Sales team enablement",
                "detail": "Train reps to interpret TrustRadius intent data on account records. A prospect who read three competitor reviews last week is a different conversation than one who briefly visited your profile page two months ago."
            }
        ],
        "faq": [
            {
                "q": "What kind of intent data does TrustRadius send to Salesforce?",
                "a": "TrustRadius tracks product page views, review reads, comparison page visits, feature research, and content downloads. The Salesforce integration delivers these as account-level intent signals with timestamps and category labels. You can filter which signal types trigger CRM actions."
            },
            {
                "q": "How does TrustRadius intent compare to other intent providers like 6sense or Bombora?",
                "a": "TrustRadius captures first-party intent from its own review platform, so the signals are highly specific: you know exactly which products a buyer researched. Third-party intent providers like 6sense and Bombora aggregate web-wide signals but with less product-level specificity. Many teams use both for layered coverage."
            },
            {
                "q": "Is TrustRadius worth it if we already use G2 for reviews?",
                "a": "TrustRadius tends to attract more enterprise and mid-market buyers, while G2 skews toward SMB. Running both gives broader buyer coverage. The Salesforce integration works similarly for both platforms, so the marginal effort is low if you already have one review platform connected."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
    },

    # 2. salesforce-churnzero (5)
    {
        "slug": "salesforce-churnzero",
        "tool_a": "salesforce",
        "tool_b": "churnzero",
        "cooccurrence_count": 5,
        "title": "Salesforce + ChurnZero Integration Guide",
        "meta_description": "How to integrate ChurnZero with Salesforce. Sync customer data, track product usage alongside CRM records, and automate retention workflows.",
        "overview": "Salesforce and ChurnZero appear together in 5 job postings, typically in customer success and post-sales operations roles. The integration connects Salesforce's CRM data (deals, contacts, revenue) with ChurnZero's product usage tracking and customer health scoring. This pairing lets CS teams see the full customer picture without switching between systems.",
        "how_they_work_together": [
            {
                "workflow": "Customer health visibility",
                "description": "ChurnZero calculates health scores from product usage, support ticket trends, and engagement patterns. These scores sync to Salesforce account records, giving account executives and renewal reps a quick read on customer risk without logging into ChurnZero."
            },
            {
                "workflow": "Renewal pipeline management",
                "description": "ChurnZero pushes renewal dates, expansion signals, and churn risk indicators into Salesforce opportunities. Sales leaders can forecast renewals using the same Salesforce reports and dashboards they use for new business."
            },
            {
                "workflow": "Onboarding tracking",
                "description": "ChurnZero tracks onboarding milestones (first login, feature activation, training completion) and syncs progress to Salesforce. Sales reps who handed off the deal can see whether their customer is successfully adopting the product."
            },
            {
                "workflow": "Expansion trigger automation",
                "description": "When ChurnZero detects usage patterns that suggest expansion readiness (hitting user limits, heavy feature adoption, department-level growth), it creates Salesforce tasks or opportunities for the account team to pursue upsells."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "Data ownership rules",
                "detail": "Salesforce should own account hierarchy, contacts, and revenue data. ChurnZero should own product usage, engagement metrics, and health scores. Define which system writes to which fields to prevent sync conflicts."
            },
            {
                "consideration": "Account matching",
                "detail": "ChurnZero matches customers by Salesforce Account ID. Ensure your Salesforce account records have clean, deduplicated data before enabling the sync. Orphaned or duplicate accounts cause health scores to land on the wrong records."
            },
            {
                "consideration": "Historical data import",
                "detail": "ChurnZero can import historical Salesforce data (closed-won dates, contract values, renewal dates) during initial setup. Budget 2-4 weeks for data mapping and validation on your first sync to get the foundation right."
            },
            {
                "consideration": "Custom object strategy",
                "detail": "ChurnZero's Salesforce managed package installs custom objects for health scores and usage data. Review your Salesforce object limits and data storage before installation, especially on Professional or Enterprise editions with storage caps."
            }
        ],
        "faq": [
            {
                "q": "Can ChurnZero replace Salesforce for customer success teams?",
                "a": "No. ChurnZero is built for CS-specific workflows like health scoring, playbooks, and in-app engagement. Salesforce remains the system of record for contracts, revenue, and cross-functional reporting. The two tools serve different purposes and work best together."
            },
            {
                "q": "How does ChurnZero compare to Gainsight for Salesforce integration?",
                "a": "Both integrate well with Salesforce. ChurnZero is generally faster to implement and more affordable for teams under 50 CS reps. Gainsight offers deeper analytics and more customization for enterprise teams managing thousands of accounts. ChurnZero's Salesforce connector is included in all plans; Gainsight may charge extra for advanced CRM sync features."
            },
            {
                "q": "What Salesforce edition do I need for the ChurnZero integration?",
                "a": "ChurnZero requires Salesforce Professional edition or higher with API access enabled. Professional edition users need the API add-on ($25/user/month). Enterprise and Unlimited editions include API access by default."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
    },

    # 3. salesforce-leandata (5)
    {
        "slug": "salesforce-leandata",
        "tool_a": "salesforce",
        "tool_b": "leandata",
        "cooccurrence_count": 5,
        "title": "Salesforce + LeanData Integration Guide",
        "meta_description": "How to integrate LeanData with Salesforce. Automate lead routing, match leads to accounts, and optimize your revenue operations workflow.",
        "overview": "Salesforce and LeanData appear together in 5 job postings, concentrated in revenue operations and marketing operations roles. LeanData runs natively inside Salesforce, providing visual lead-to-account matching, automated routing, and territory management. Unlike middleware tools, LeanData operates directly on Salesforce objects, which makes it one of the tightest CRM integrations in the RevOps stack.",
        "how_they_work_together": [
            {
                "workflow": "Lead-to-account matching",
                "description": "LeanData uses fuzzy matching algorithms to connect incoming Salesforce leads to existing accounts. This prevents duplicate outreach and ensures reps work leads associated with their assigned accounts. Matching runs in real time as leads are created."
            },
            {
                "workflow": "Automated lead routing",
                "description": "LeanData's visual flowchart builder routes Salesforce leads, contacts, and opportunities to the right owner based on territory, account assignment, round-robin rules, or capacity weighting. Routing logic updates without writing Salesforce code."
            },
            {
                "workflow": "Account-based handoff",
                "description": "When marketing generates a new lead at an existing account, LeanData routes it to the account owner instead of the default lead queue. This ensures inbound leads at named accounts go directly to the rep who owns the relationship."
            },
            {
                "workflow": "Merge and deduplication",
                "description": "LeanData identifies duplicate leads and contacts in Salesforce and merges them based on configurable rules. Surviving records retain the most complete data fields, and merge history is logged for audit purposes."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "Salesforce-native architecture",
                "detail": "LeanData installs as a Salesforce managed package and runs entirely inside the Salesforce platform. There is no external data sync to configure. However, the package consumes Salesforce API calls and may require monitoring on orgs near their daily API limits."
            },
            {
                "consideration": "Routing logic migration",
                "detail": "If you already have lead assignment rules in Salesforce, plan the cutover carefully. Run LeanData routing in parallel (audit mode) for 2-4 weeks before deactivating native Salesforce assignment rules to validate that leads route correctly."
            },
            {
                "consideration": "Matching rule tuning",
                "detail": "LeanData's lead-to-account matching uses company name, domain, and email domain. Out-of-the-box settings work for most teams, but companies with multiple subsidiaries or divisions may need custom matching rules to prevent incorrect account associations."
            },
            {
                "consideration": "Admin permissions",
                "detail": "The LeanData managed package requires a Salesforce admin with modify-all-data permissions for installation. Ongoing management needs a dedicated admin or RevOps user who understands both Salesforce and LeanData's flowchart builder."
            }
        ],
        "faq": [
            {
                "q": "Why not just use Salesforce's built-in lead assignment rules?",
                "a": "Salesforce native assignment rules are limited to basic field matching and round-robin. LeanData adds visual routing flows, lead-to-account matching, capacity-based assignment, and time-based routing that Salesforce can't do natively. Most teams outgrow native assignment rules around 10-15 reps."
            },
            {
                "q": "How much does LeanData cost?",
                "a": "LeanData pricing starts around $39/user/month for the routing module. Lead-to-account matching and deduplication are separate modules with additional cost. Enterprise pricing for full-platform access typically runs $75-100/user/month. All plans require Salesforce Enterprise edition or higher."
            },
            {
                "q": "Does LeanData work with HubSpot-sourced leads in Salesforce?",
                "a": "Yes. LeanData routes leads after they land in Salesforce, regardless of the source. Leads synced from HubSpot, web forms, third-party enrichment tools, or manual entry all flow through LeanData's routing engine identically."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
    },

    # 4. salesforce-chili-piper (3)
    {
        "slug": "salesforce-chili-piper",
        "tool_a": "salesforce",
        "tool_b": "chili-piper",
        "cooccurrence_count": 3,
        "title": "Salesforce + Chili Piper Integration Guide",
        "meta_description": "How to integrate Chili Piper with Salesforce. Automate meeting booking, route inbound leads to reps instantly, and eliminate scheduling friction.",
        "overview": "Salesforce and Chili Piper appear together in 3 job postings, typically in demand generation and inbound sales roles. Chili Piper converts inbound form submissions into booked meetings in real time and routes them to the right Salesforce rep. The integration eliminates the delay between a lead submitting a form and speaking with sales, which can cut inbound response time from hours to seconds.",
        "how_they_work_together": [
            {
                "workflow": "Instant meeting booking",
                "description": "When a prospect fills out a website form, Chili Piper displays available meeting times immediately. The booked meeting creates a Salesforce event, lead record, and activity in one action. No BDR follow-up email required for hot inbound leads."
            },
            {
                "workflow": "Inbound lead routing",
                "description": "Chili Piper checks Salesforce for existing accounts and contacts before routing. If the prospect's company already has an account owner, the meeting routes to that rep. New prospects route based on territory, round-robin, or segment rules."
            },
            {
                "workflow": "Handoff meetings",
                "description": "Chili Piper automates the BDR-to-AE handoff by booking meetings on the AE's calendar based on Salesforce account ownership. The BDR qualifies the lead, Chili Piper finds the right AE, and the meeting is scheduled without back-and-forth."
            },
            {
                "workflow": "Pipeline attribution",
                "description": "Every meeting booked through Chili Piper logs to Salesforce with source data: which form, page, and campaign drove the conversion. This gives marketing precise attribution for meetings-booked as a conversion metric."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "Form integration",
                "detail": "Chili Piper overlays on top of existing web forms (Marketo, HubSpot, Pardot, or custom). The form still submits to your marketing automation platform; Chili Piper intercepts the submission to display booking. No form rebuilding required."
            },
            {
                "consideration": "Calendar connectivity",
                "detail": "Each rep needs their Google Calendar or Outlook calendar connected to Chili Piper. Meeting availability checks happen in real time against the rep's calendar, so disconnected calendars result in scheduling conflicts."
            },
            {
                "consideration": "Routing rules alignment",
                "detail": "Align Chili Piper's routing rules with your Salesforce territory assignments. If you already use LeanData or Salesforce assignment rules, Chili Piper can defer to those systems or override them for inbound-specific routing."
            },
            {
                "consideration": "No-show handling",
                "detail": "Configure Chili Piper's automated reminders and rescheduling links to reduce no-show rates. Typical inbound meeting no-show rates run 15-25%; automated reminders and calendar holds can cut that to under 10%."
            }
        ],
        "faq": [
            {
                "q": "How much does Chili Piper cost?",
                "a": "Chili Piper Concierge (the inbound scheduling product) starts at $30/user/month for basic routing. The full platform with handoffs, distribution rules, and analytics runs $60-90/user/month. Custom enterprise pricing is available for large sales orgs."
            },
            {
                "q": "Does Chili Piper replace Calendly?",
                "a": "For inbound demand conversion, yes. Calendly is a general-purpose scheduling tool; Chili Piper is built specifically for B2B inbound sales. Chili Piper adds CRM routing, account matching, and form-level integration that Calendly doesn't offer. For internal or external meeting links, Calendly still works fine."
            },
            {
                "q": "Can Chili Piper work with Salesforce Professional edition?",
                "a": "Yes, but you need API access enabled on Salesforce Professional, which is an add-on. Chili Piper writes leads, contacts, events, and tasks to Salesforce via API, so this access is mandatory for the integration to function."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
    },

    # 5. salesforce-highspot (3)
    {
        "slug": "salesforce-highspot",
        "tool_a": "salesforce",
        "tool_b": "highspot",
        "cooccurrence_count": 3,
        "title": "Salesforce + Highspot Integration Guide",
        "meta_description": "How to integrate Highspot with Salesforce. Surface sales content in CRM, track content engagement, and connect enablement activities to pipeline outcomes.",
        "overview": "Salesforce and Highspot appear together in 3 job postings, typically in sales enablement and revenue operations roles. Highspot is a sales enablement platform that manages sales content, training materials, and rep coaching. The Salesforce integration puts relevant content directly inside the CRM workflow and tracks which materials influence deal progression.",
        "how_they_work_together": [
            {
                "workflow": "Content surfacing in CRM",
                "description": "Highspot displays recommended content (decks, case studies, one-pagers, videos) inside Salesforce opportunity and account records. Recommendations are based on deal stage, industry, company size, and persona, so reps see the most relevant materials without searching."
            },
            {
                "workflow": "Content engagement tracking",
                "description": "When a rep shares content through Highspot, engagement data (opens, time spent, pages viewed, forwards) syncs back to the Salesforce opportunity record. Sales managers can see which materials buyers consume during the deal cycle."
            },
            {
                "workflow": "Pitch building from CRM",
                "description": "Reps assemble and personalize Highspot pitches (curated collections of sales materials) directly from Salesforce. The pitch pulls in approved content templates and pre-populates prospect details from CRM fields."
            },
            {
                "workflow": "Content influence reporting",
                "description": "Highspot maps content usage to Salesforce pipeline and closed-won revenue. Enablement teams can report on which content assets contribute to deal velocity and win rates, connecting content investment to revenue outcomes."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "Content tagging strategy",
                "detail": "Highspot's Salesforce recommendations depend on content being properly tagged by industry, persona, deal stage, and use case. Invest in a tagging taxonomy before launch; poor tagging results in irrelevant recommendations that reps will ignore."
            },
            {
                "consideration": "Salesforce Lightning required",
                "detail": "Highspot's Salesforce integration uses Lightning Web Components. Classic Salesforce UI is not supported. If your org hasn't migrated to Lightning, that must happen first."
            },
            {
                "consideration": "Rep adoption planning",
                "detail": "Sales enablement platforms live or die on rep adoption. Roll out Highspot to a pilot group of 5-10 reps before full deployment. Track content sharing frequency and deal attachment rates to prove value before expanding."
            },
            {
                "consideration": "Permission configuration",
                "detail": "Set up Highspot content access rules to mirror Salesforce role hierarchies. Reps should only see content relevant to their segment or territory. Misconfigured permissions lead to content overload and lower adoption."
            }
        ],
        "faq": [
            {
                "q": "How much does Highspot cost?",
                "a": "Highspot does not publish pricing. Based on market data, plans typically start around $40-60/user/month for core enablement features. Enterprise deals with analytics, coaching, and advanced integrations run higher. Annual contracts are standard."
            },
            {
                "q": "How does Highspot compare to Seismic?",
                "a": "Both are enterprise sales enablement platforms. Highspot is generally considered easier to set up and has a stronger content management interface. Seismic has deeper analytics and more mature integration with content automation workflows. Both integrate with Salesforce. Choice often depends on which platform your reps find more intuitive."
            },
            {
                "q": "Does Highspot work with HubSpot as well as Salesforce?",
                "a": "Yes. Highspot has integrations for both Salesforce and HubSpot CRM. The feature set is comparable across both CRM platforms, though the Salesforce integration has been available longer and tends to be more mature."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
    },

    # 6. hubspot-chili-piper (4)
    {
        "slug": "hubspot-chili-piper",
        "tool_a": "hubspot",
        "tool_b": "chili-piper",
        "cooccurrence_count": 4,
        "title": "HubSpot + Chili Piper Integration Guide",
        "meta_description": "How to integrate Chili Piper with HubSpot. Convert inbound form fills into booked meetings instantly, route leads to reps, and accelerate your inbound pipeline.",
        "overview": "HubSpot and Chili Piper appear together in 4 job postings, concentrated in demand generation and marketing operations. Chili Piper sits on top of HubSpot forms and converts inbound submissions into instant meeting bookings. The integration routes qualified prospects to the right rep's calendar in real time, cutting inbound lead response time from hours or days to under a minute.",
        "how_they_work_together": [
            {
                "workflow": "Form-to-meeting conversion",
                "description": "Chili Piper fires after a HubSpot form submission, displaying available meeting times to the prospect immediately. The form data still flows to HubSpot normally, but the prospect can book a call before leaving the page. Conversion rates on demo request forms typically increase 30-50% with instant booking."
            },
            {
                "workflow": "Smart lead routing",
                "description": "Chili Piper checks HubSpot for existing contacts and company owners before routing. Returning leads route to their assigned rep; new leads distribute via round-robin, territory, or segment rules. The routing happens in milliseconds, invisible to the prospect."
            },
            {
                "workflow": "Lifecycle stage automation",
                "description": "When a prospect books a meeting through Chili Piper, HubSpot's lifecycle stage and lead status update automatically. Booked meetings can trigger HubSpot workflows for internal notifications, Slack alerts, or pre-meeting nurture sequences."
            },
            {
                "workflow": "Meeting-based attribution",
                "description": "Chili Piper logs each booked meeting as a HubSpot activity with source data: the form URL, referring page, UTM parameters, and campaign. Marketing teams can report on meetings booked per channel, not just form fills, for a more meaningful conversion metric."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "HubSpot form compatibility",
                "detail": "Chili Piper works with HubSpot's native forms, embedded forms, and pop-up forms. Non-HubSpot forms on your site need the Chili Piper JavaScript snippet installed separately. Test each form type during setup."
            },
            {
                "consideration": "Qualification logic",
                "detail": "Not every form fill should trigger a meeting offer. Configure Chili Piper to check qualification criteria (company size, job title, lead score) from HubSpot before showing booking options. Unqualified leads should still submit the form but skip the instant scheduling."
            },
            {
                "consideration": "Calendar sync reliability",
                "detail": "Chili Piper checks real-time calendar availability for each rep. Reps must have their Google or Outlook calendars connected and actively maintained. Block personal appointments and internal meetings to prevent double-booking."
            },
            {
                "consideration": "Timezone handling",
                "detail": "Chili Piper auto-detects the prospect's timezone and displays available slots accordingly. Verify that your reps' calendar timezones are set correctly in both their calendar app and Chili Piper profile to avoid scheduling mix-ups."
            }
        ],
        "faq": [
            {
                "q": "Does Chili Piper replace HubSpot's built-in meeting scheduler?",
                "a": "For inbound demand conversion, yes. HubSpot's meeting links work fine for one-off scheduling, but they don't do real-time form interception, smart routing, or rep-matching based on CRM data. Chili Piper handles the high-value use case of converting inbound form fills into booked meetings."
            },
            {
                "q": "What HubSpot plan do I need for Chili Piper?",
                "a": "Chili Piper works with any HubSpot plan that includes forms, including the free CRM. However, for full routing and lifecycle automation, you'll want Marketing Hub Professional or higher, which provides the workflows and automation features that maximize the integration."
            },
            {
                "q": "How does Chili Piper handle after-hours form submissions?",
                "a": "If no reps have available time slots during the prospect's preferred window, Chili Piper shows the next available time across all qualified reps. You can also configure it to offer a callback request or drop into a standard thank-you page flow for off-hours submissions."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
    },

    # 7. hubspot-highspot (4)
    {
        "slug": "hubspot-highspot",
        "tool_a": "hubspot",
        "tool_b": "highspot",
        "cooccurrence_count": 4,
        "title": "HubSpot + Highspot Integration Guide",
        "meta_description": "How to integrate Highspot with HubSpot. Surface sales content inside your CRM, track buyer engagement with materials, and tie enablement to pipeline.",
        "overview": "HubSpot and Highspot appear together in 4 job postings, mostly in sales enablement and marketing operations roles. Highspot brings structured sales content management into HubSpot's CRM, letting reps access approved collateral, track buyer engagement, and connect content usage to deal outcomes. The integration is especially common at companies that outgrow HubSpot's built-in document management.",
        "how_they_work_together": [
            {
                "workflow": "Content recommendations in CRM",
                "description": "Highspot surfaces relevant content inside HubSpot deal and company records based on deal stage, industry, and buyer persona. Reps see the most effective case studies, decks, and proposals without leaving HubSpot or searching a shared drive."
            },
            {
                "workflow": "Buyer engagement tracking",
                "description": "When reps share Highspot content via email or links, engagement data (opens, time on page, pages viewed, downloads) syncs back to the HubSpot contact and deal timeline. Sales and marketing both see which content buyers read."
            },
            {
                "workflow": "Email content insertion",
                "description": "Reps can insert Highspot-managed content directly into HubSpot email templates and sequences. Content links are tracked automatically, so every attachment and document share has full engagement analytics."
            },
            {
                "workflow": "Content performance analytics",
                "description": "Highspot correlates content usage with HubSpot deal outcomes. Enablement teams can identify which assets appear most frequently in won deals versus lost deals, and optimize the content library based on actual revenue impact rather than download counts."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "Content governance",
                "detail": "Before integrating, audit your existing sales content library. Archive outdated materials, standardize naming conventions, and set up approval workflows in Highspot. A cluttered content library undermines the value of CRM-integrated recommendations."
            },
            {
                "consideration": "HubSpot edition requirements",
                "detail": "The Highspot integration works with HubSpot Sales Hub Professional and Enterprise. Free and Starter plans lack the custom properties and API access needed for full integration functionality."
            },
            {
                "consideration": "Adoption metrics",
                "detail": "Track content sharing rates per rep from the first week. Reps who aren't using Highspot within 30 days rarely adopt it later without intervention. Set adoption benchmarks (e.g., 3+ content shares per rep per week) and follow up with non-adopters."
            },
            {
                "consideration": "Content tagging alignment",
                "detail": "Align Highspot's content tags with HubSpot's deal properties. If HubSpot tracks deal stages as Discovery, Demo, Proposal, Negotiation, tag content in Highspot to match. Misaligned taxonomy results in poor content recommendations."
            }
        ],
        "faq": [
            {
                "q": "Can HubSpot's built-in documents feature replace Highspot?",
                "a": "For small teams with fewer than 50 pieces of content, HubSpot's Documents tool may be sufficient. Highspot adds value when you have hundreds of assets, need role-based content access, want AI-driven recommendations, or need to correlate content to deal outcomes. Most teams reach this tipping point around 20-30 reps."
            },
            {
                "q": "Does Highspot content appear inside HubSpot on mobile?",
                "a": "Highspot has its own mobile app where reps can access content, but the embedded CRM integration currently works best on HubSpot's desktop experience. Mobile access to Highspot content is through the Highspot app rather than the HubSpot mobile interface."
            },
            {
                "q": "How long does the HubSpot-Highspot integration take to set up?",
                "a": "The technical connection takes a few hours. The real time investment is content migration, tagging, and governance setup, which typically takes 4-8 weeks for a library of 200+ assets. Plan for at least two weeks of pilot testing with a small rep group before full rollout."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
    },

    # 8. hubspot-churnzero (3)
    {
        "slug": "hubspot-churnzero",
        "tool_a": "hubspot",
        "tool_b": "churnzero",
        "cooccurrence_count": 3,
        "title": "HubSpot + ChurnZero Integration Guide",
        "meta_description": "How to integrate ChurnZero with HubSpot. Connect CRM deal data to customer success workflows, track product adoption, and reduce churn with unified customer visibility.",
        "overview": "HubSpot and ChurnZero appear together in 3 job postings, primarily in customer success and post-sales operations. This pairing is common at SaaS companies that use HubSpot as their CRM and need a dedicated customer success platform for health scoring, usage tracking, and retention automation. ChurnZero picks up where HubSpot's deal pipeline ends, managing the customer lifecycle after closed-won.",
        "how_they_work_together": [
            {
                "workflow": "Customer data sync",
                "description": "ChurnZero pulls closed-won deal data from HubSpot, including contract value, close date, product line, and contact roles. This creates customer records in ChurnZero automatically, eliminating manual data entry for CS teams during handoff."
            },
            {
                "workflow": "Health score visibility in CRM",
                "description": "ChurnZero calculates customer health scores based on product usage, support interactions, and engagement patterns, then pushes those scores to HubSpot company records. Sales and marketing teams see account health without needing ChurnZero access."
            },
            {
                "workflow": "Expansion opportunity creation",
                "description": "When ChurnZero identifies expansion signals (usage spikes, feature requests, growing user counts), it creates HubSpot deals in the expansion pipeline. Account managers get notified through their normal HubSpot workflow instead of monitoring a separate tool."
            },
            {
                "workflow": "Churn risk alerting",
                "description": "ChurnZero monitors for risk indicators (declining logins, support escalations, missed milestones) and pushes alerts to HubSpot. At-risk accounts trigger HubSpot workflows that notify the CS manager, schedule a check-in call, and escalate to leadership if needed."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "Handoff workflow design",
                "detail": "Define the exact point where a customer moves from HubSpot deal management to ChurnZero CS management. Most teams trigger the handoff on closed-won deal stage. Map which HubSpot deal properties transfer to ChurnZero and which CS actions fire automatically."
            },
            {
                "consideration": "Contact role mapping",
                "detail": "HubSpot deal contacts and their roles (decision maker, champion, end user) should map to ChurnZero contact types. Accurate role mapping ensures ChurnZero's in-app messages and outreach target the right people at the customer account."
            },
            {
                "consideration": "Product usage data source",
                "detail": "ChurnZero needs product usage data to calculate health scores. This comes from your application's event tracking (not from HubSpot). Plan the ChurnZero SDK or API integration with your product alongside the HubSpot CRM connection."
            },
            {
                "consideration": "Reporting boundary",
                "detail": "Decide which metrics live in HubSpot reporting and which live in ChurnZero. Revenue and pipeline metrics typically stay in HubSpot. Usage, health, and adoption metrics belong in ChurnZero. Overlap creates confusion about which system is the source of truth."
            }
        ],
        "faq": [
            {
                "q": "Does HubSpot Service Hub replace ChurnZero?",
                "a": "Partially. HubSpot Service Hub handles ticketing, knowledge bases, and basic customer feedback. ChurnZero adds product usage tracking, health scoring, automated playbooks, and in-app engagement that Service Hub doesn't provide. Companies with high-touch CS motions and SaaS products typically need ChurnZero's depth on top of HubSpot."
            },
            {
                "q": "What HubSpot plan is needed for the ChurnZero integration?",
                "a": "ChurnZero integrates via HubSpot's API, which is available on all paid plans. For full workflow automation (triggering actions based on ChurnZero data), you'll want HubSpot Professional or Enterprise for workflows and custom properties."
            },
            {
                "q": "How long does it take to see value from ChurnZero with HubSpot?",
                "a": "The CRM integration takes 1-2 weeks to configure. Product usage tracking setup adds another 2-4 weeks depending on engineering resources. Most teams start seeing actionable health scores and churn predictions within 60-90 days of initial data flowing in."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
    },

    # 9. hubspot-leandata (3)
    {
        "slug": "hubspot-leandata",
        "tool_a": "hubspot",
        "tool_b": "leandata",
        "cooccurrence_count": 3,
        "title": "HubSpot + LeanData Integration Guide",
        "meta_description": "How to integrate LeanData with HubSpot. Automate lead routing, match leads to target accounts, and optimize rep assignment for inbound and outbound leads.",
        "overview": "HubSpot and LeanData appear together in 3 job postings, primarily in marketing operations and revenue operations. LeanData's HubSpot integration brings enterprise-grade lead routing and lead-to-account matching to HubSpot CRM. This pairing is especially common at companies that have outgrown HubSpot's native rotation and assignment tools and need more sophisticated routing logic.",
        "how_they_work_together": [
            {
                "workflow": "Lead-to-account matching",
                "description": "LeanData matches incoming HubSpot contacts to existing companies using domain, company name, and email domain. Matched leads route to the company owner rather than entering a generic queue, ensuring named account leads reach the right rep."
            },
            {
                "workflow": "Advanced routing logic",
                "description": "LeanData's visual flow builder creates routing rules based on HubSpot properties: territory, company size, lead score, product interest, or custom fields. Complex routing that would require multiple HubSpot workflows can be managed in a single LeanData flow."
            },
            {
                "workflow": "Round-robin with capacity",
                "description": "LeanData distributes leads across reps based on capacity weighting, not just simple round-robin. Reps with lighter pipelines or fewer open deals receive more leads. Weighting adjusts dynamically based on HubSpot deal data."
            },
            {
                "workflow": "Routing analytics",
                "description": "LeanData tracks routing performance: time-to-assignment, lead acceptance rates, and routing errors. These metrics feed back into HubSpot dashboards, letting ops teams identify bottlenecks in the lead handoff process."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "HubSpot versus Salesforce architecture",
                "detail": "LeanData's HubSpot integration runs via API, not as a native app like it does in Salesforce. This means routing logic executes in LeanData's cloud, not inside HubSpot. The practical difference is minimal, but latency may be slightly higher than the Salesforce-native experience."
            },
            {
                "consideration": "Workflow overlap",
                "detail": "If you already use HubSpot workflows for lead assignment, plan to consolidate. Running both LeanData routing and HubSpot workflows for the same purpose creates conflicts and makes troubleshooting difficult. Migrate all routing logic to LeanData and remove duplicate HubSpot workflows."
            },
            {
                "consideration": "Contact versus company ownership",
                "detail": "HubSpot allows contacts to have different owners than their associated company. Define clear rules for whether LeanData should assign the contact owner, company owner, or both. Misalignment here causes confusion about who owns which relationships."
            },
            {
                "consideration": "HubSpot plan requirements",
                "detail": "LeanData's HubSpot integration requires API access, available on HubSpot Professional and Enterprise plans. Free and Starter plans have limited API access that may not support LeanData's real-time routing requirements."
            }
        ],
        "faq": [
            {
                "q": "Can HubSpot's native workflows handle lead routing without LeanData?",
                "a": "For simple round-robin and basic property-based assignment, yes. HubSpot workflows can rotate leads and assign based on form field values. LeanData becomes necessary when you need lead-to-account matching, capacity-based distribution, complex territory logic, or visual routing flows. Most teams hit this point around 15-20 reps."
            },
            {
                "q": "Is LeanData's HubSpot integration as mature as its Salesforce integration?",
                "a": "Not yet. LeanData was built Salesforce-first, and the Salesforce integration has more features and deeper native access. The HubSpot integration covers core routing and matching but may lack some advanced features available on Salesforce. Check current feature parity before purchasing."
            },
            {
                "q": "Can I use LeanData if my team is migrating from Salesforce to HubSpot?",
                "a": "Yes, and this is a common scenario. LeanData supports both CRMs, so you can maintain routing logic during migration. However, the routing flows need to be rebuilt for HubSpot's data model since Salesforce leads/contacts are structured differently than HubSpot contacts."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
    },

    # 10. zoominfo-leandata (4)
    {
        "slug": "zoominfo-leandata",
        "tool_a": "zoominfo",
        "tool_b": "leandata",
        "cooccurrence_count": 4,
        "title": "ZoomInfo + LeanData Integration Guide",
        "meta_description": "How to use ZoomInfo and LeanData together. Enrich leads with contact data, then route them to the right rep based on account matching and territory rules.",
        "overview": "ZoomInfo and LeanData appear together in 4 job postings, concentrated in revenue operations roles. The two tools address sequential steps in the inbound and outbound pipeline: ZoomInfo provides the contact data and enrichment, LeanData handles the routing and assignment. Together, they ensure that enriched leads reach the correct rep without manual intervention or routing errors.",
        "how_they_work_together": [
            {
                "workflow": "Enrich then route",
                "description": "ZoomInfo enriches new CRM leads with company data (revenue, employee count, industry) immediately after creation. LeanData then routes the enriched lead based on those firmographic fields. Without enrichment first, routing rules that depend on company size or industry would fail on incomplete records."
            },
            {
                "workflow": "Account matching with enriched data",
                "description": "LeanData's lead-to-account matching improves dramatically when ZoomInfo fills in company domain and standardized company names. Raw form submissions often have inconsistent company fields ('IBM' vs 'International Business Machines'); ZoomInfo normalizes this data before LeanData matches."
            },
            {
                "workflow": "Territory assignment accuracy",
                "description": "ZoomInfo appends headquarters location, SIC/NAICS codes, and revenue data to CRM records. LeanData uses these enriched fields for territory assignment, ensuring leads route based on verified company data rather than self-reported form fields."
            },
            {
                "workflow": "Target account identification",
                "description": "ZoomInfo identifies companies matching your ideal customer profile and pushes them into your CRM. LeanData then checks whether these accounts already have owners and routes new contacts to the assigned rep, preventing duplicate outreach to named accounts."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "Processing order",
                "detail": "ZoomInfo enrichment must fire before LeanData routing. If LeanData routes before ZoomInfo enriches, routing rules won't have the data they need. Configure your CRM automation to ensure enrichment completes first, typically using a trigger-based sequence or slight delay."
            },
            {
                "consideration": "Field dependency mapping",
                "detail": "Document which LeanData routing rules depend on ZoomInfo-enriched fields. If ZoomInfo fails to enrich a record (no match found), LeanData needs fallback routing logic. Build a default route for un-enriched records so leads don't get stuck."
            },
            {
                "consideration": "CRM as the integration point",
                "detail": "ZoomInfo and LeanData don't integrate directly with each other. Both connect through your CRM (Salesforce or HubSpot). Ensure both tools have proper API access and that field mappings are consistent across all three systems."
            },
            {
                "consideration": "Credit consumption awareness",
                "detail": "ZoomInfo enrichment burns credits for each record processed. If inbound lead volume spikes, enrichment costs spike too. Set up ZoomInfo enrichment filters to only enrich leads that meet basic qualification criteria before consuming credits."
            }
        ],
        "faq": [
            {
                "q": "Do ZoomInfo and LeanData have a direct integration?",
                "a": "No. Both tools connect to your CRM (Salesforce or HubSpot) independently. ZoomInfo enriches records in the CRM, then LeanData reads those enriched fields for routing decisions. Your CRM is the middleware that connects the two."
            },
            {
                "q": "What happens if ZoomInfo can't enrich a lead?",
                "a": "LeanData will still route the lead, but routing rules that depend on enriched fields (company size, industry, headquarters location) may not fire correctly. Build fallback routes in LeanData for un-enriched records, typically routing to a general queue or round-robin pool."
            },
            {
                "q": "Can I use Apollo instead of ZoomInfo with LeanData?",
                "a": "Yes. LeanData routes based on CRM fields, regardless of which enrichment tool populated them. Apollo, Clearbit, or any enrichment provider that writes to your CRM fields will work with LeanData's routing engine. The key is ensuring enrichment fires before routing."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
    },

    # 11. zoominfo-highspot (3)
    {
        "slug": "zoominfo-highspot",
        "tool_a": "zoominfo",
        "tool_b": "highspot",
        "cooccurrence_count": 3,
        "title": "ZoomInfo + Highspot Integration Guide",
        "meta_description": "How to use ZoomInfo and Highspot together. Combine prospect intelligence with sales content to deliver targeted, personalized outreach at scale.",
        "overview": "ZoomInfo and Highspot appear together in 3 job postings, typically in sales enablement and outbound sales roles. ZoomInfo provides the prospect intelligence (who to contact, what they care about), and Highspot provides the content (what to send them). The combination lets reps personalize outreach using data-driven prospect insights matched to the most effective sales materials.",
        "how_they_work_together": [
            {
                "workflow": "Data-informed content selection",
                "description": "ZoomInfo's firmographic and technographic data (industry, tech stack, company size) informs which Highspot content a rep should share. A manufacturing prospect gets a manufacturing case study; a company running a competitor's product gets competitive battle cards. The CRM connects the intelligence to the content."
            },
            {
                "workflow": "Intent-triggered content plays",
                "description": "When ZoomInfo detects that a target account is researching your product category, reps use Highspot to send relevant content at the right moment. Intent data identifies the 'when'; Highspot provides the 'what.' This combination produces higher engagement rates than generic outbound sequences."
            },
            {
                "workflow": "Persona-based outreach",
                "description": "ZoomInfo identifies the buying committee members (titles, seniority, department) at target accounts. Highspot provides persona-specific content for each stakeholder: technical docs for engineers, ROI calculators for finance, executive summaries for C-suite. Each outreach touchpoint is tailored to the recipient."
            },
            {
                "workflow": "Content engagement enrichment",
                "description": "Highspot tracks which content a prospect engages with (pages viewed, time spent, downloads). This engagement data, combined with ZoomInfo's contact profile, gives reps a fuller picture of buyer interest and intent before the first conversation."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "CRM as the connection layer",
                "detail": "ZoomInfo and Highspot don't integrate directly. Both connect through your CRM (Salesforce or HubSpot). ZoomInfo enriches CRM records, and Highspot surfaces content based on those enriched fields. Ensure consistent field naming and data hygiene in your CRM."
            },
            {
                "consideration": "Content mapping to segments",
                "detail": "Map your Highspot content library to the segments and personas you target with ZoomInfo. If ZoomInfo identifies five key industries and three buyer personas, you need content tagged for each combination. Gaps in content coverage reduce the value of personalized outreach."
            },
            {
                "consideration": "Rep workflow training",
                "detail": "Train reps on the complete workflow: research prospect in ZoomInfo, check CRM for enriched data, select relevant Highspot content, personalize, and send. Without clear workflow training, reps default to generic templates and bypass both tools."
            },
            {
                "consideration": "Engagement data consolidation",
                "detail": "Both ZoomInfo (intent data) and Highspot (content engagement) produce signals about buyer interest. Ensure both data streams land on the same CRM records so reps have a single view of prospect activity."
            }
        ],
        "faq": [
            {
                "q": "Do ZoomInfo and Highspot integrate directly?",
                "a": "Not directly. Both tools connect to your CRM, which serves as the integration layer. ZoomInfo enriches records in Salesforce or HubSpot, and Highspot recommends content based on those CRM fields. The workflow is connected through CRM data, not a point-to-point integration."
            },
            {
                "q": "Can I use ZoomInfo intent data to trigger Highspot content recommendations?",
                "a": "Yes, but indirectly. ZoomInfo pushes intent data to your CRM as account fields or activities. You can then configure Highspot's content recommendations to factor in those intent fields, surfacing relevant content when an account shows buying signals."
            },
            {
                "q": "Is this combination worth the cost for a small sales team?",
                "a": "For teams under 10 reps, the combined cost of ZoomInfo and Highspot (likely $30K-50K/year together) may be hard to justify. Smaller teams can get similar results with Apollo for data and Google Drive or Notion for content management. The ZoomInfo-Highspot combination pays off when personalization at scale becomes a bottleneck."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
    },

    # 12. g2-trustradius (11)
    {
        "slug": "g2-trustradius",
        "tool_a": "g2",
        "tool_b": "trustradius",
        "cooccurrence_count": 11,
        "title": "G2 + TrustRadius: Using Both Review Platforms Together",
        "meta_description": "How to use G2 and TrustRadius together for buyer intent, reviews, and market presence. Compare the platforms and learn when you need both.",
        "overview": "G2 and TrustRadius appear together in 11 job postings, the highest co-occurrence among review platform pairs. Rather than a technical integration, these platforms serve complementary roles in a vendor's review and intent data strategy. G2 has a larger SMB buyer audience and more reviews per category. TrustRadius attracts more enterprise and mid-market buyers with longer, more detailed reviews. Companies that invest in both platforms get broader buyer coverage and richer intent signals across market segments.",
        "how_they_work_together": [
            {
                "workflow": "Dual-platform review strategy",
                "description": "Marketing teams run review campaigns on both platforms to maximize coverage. G2 review volume drives category ranking and visibility among SMB buyers. TrustRadius reviews tend to be more detailed (600+ words on average versus 200 on G2), which carries more weight with enterprise buyers doing deep research."
            },
            {
                "workflow": "Layered intent data",
                "description": "Both G2 and TrustRadius provide buyer intent signals when prospects research your product or category. Running both gives broader intent coverage: G2 captures high-volume SMB browsing behavior, TrustRadius captures enterprise research patterns. Intent signals from both platforms can feed into your CRM and ABM tools."
            },
            {
                "workflow": "Competitive monitoring",
                "description": "Track competitor reviews, ratings, and sentiment across both platforms. G2's quarterly Grid reports show category positioning. TrustRadius TrustMaps offer a similar view with different methodology. Monitoring both surfaces competitive shifts that might only appear on one platform."
            },
            {
                "workflow": "Social proof content",
                "description": "Pull quotes, ratings, and badges from both platforms for use in sales decks, website pages, and ad copy. G2 badges ('Leader', 'Best Of') are widely recognized in the SMB market. TrustRadius 'Top Rated' awards carry weight with enterprise procurement teams."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "Review campaign coordination",
                "detail": "Avoid asking the same customers to review on both platforms simultaneously. Rotate: ask one cohort for G2 reviews in Q1, another for TrustRadius in Q2. Review fatigue from double-asking leads to lower response rates and lower-quality reviews."
            },
            {
                "consideration": "Intent data deduplication",
                "detail": "If you feed intent signals from both G2 and TrustRadius into your CRM, the same prospect may appear in both streams. Set up deduplication rules so account-level intent scores don't double-count a single buyer researching on two platforms."
            },
            {
                "consideration": "Budget allocation",
                "detail": "Both platforms charge for vendor profiles with intent data. G2 pricing starts around $20K/year for a paid profile. TrustRadius pricing is comparable. For tight budgets, start with the platform where your category has more buyer traffic, then add the second after proving ROI on intent-to-pipeline conversion."
            },
            {
                "consideration": "Response management",
                "detail": "Assign ownership for review response on each platform. Responding to reviews (both positive and negative) boosts your profile and signals engagement to potential buyers. Most teams assign a product marketer or customer marketing manager to handle both platforms."
            }
        ],
        "faq": [
            {
                "q": "Do I need both G2 and TrustRadius?",
                "a": "It depends on your target market. If you sell primarily to SMBs, G2 alone may be sufficient since it has the largest buyer audience in that segment. If you sell to enterprise and mid-market, TrustRadius has stronger penetration with those buyers. Companies selling across both segments get the most value from running both platforms."
            },
            {
                "q": "Which platform has better intent data?",
                "a": "Both provide account-level intent signals when buyers research your product or category. G2 has higher traffic volume, so you'll see more intent signals overall. TrustRadius intent signals tend to represent more serious enterprise research. The quality difference is less about the platform and more about where your buyers spend time."
            },
            {
                "q": "Can G2 and TrustRadius data feed into the same CRM?",
                "a": "Yes. Both platforms offer Salesforce and HubSpot integrations for pushing intent data into CRM records. You can also feed both into ABM platforms like 6sense or Demandbase. Set up deduplication rules to prevent the same account from being double-counted when they research on both platforms."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
    },

    # 13. clay-leandata (3)
    {
        "slug": "clay-leandata",
        "tool_a": "clay",
        "tool_b": "leandata",
        "cooccurrence_count": 3,
        "title": "Clay + LeanData Integration Guide",
        "meta_description": "How to use Clay and LeanData together. Enrich and build prospect lists with Clay, then route enriched leads to the right reps with LeanData.",
        "overview": "Clay and LeanData appear together in 3 job postings, typically in growth operations and revenue operations roles. Clay is a data enrichment and workflow automation platform that builds prospect lists from 50+ data providers. LeanData handles lead routing and account matching inside the CRM. Together, they form an enrichment-to-routing pipeline: Clay builds and enriches the lead, LeanData makes sure it reaches the right rep.",
        "how_they_work_together": [
            {
                "workflow": "List build to CRM routing",
                "description": "Clay builds targeted prospect lists using firmographic, technographic, and intent signals from multiple data sources. When Clay pushes these enriched contacts into the CRM, LeanData immediately routes them based on territory, account ownership, and segment rules. The prospect goes from data source to assigned rep without manual handoff."
            },
            {
                "workflow": "Waterfall enrichment for routing accuracy",
                "description": "Clay's waterfall enrichment checks multiple data providers (ZoomInfo, Apollo, Clearbit, and others) to fill in company domain, headquarters location, and revenue. LeanData's routing rules depend on these fields being accurate. Clay's multi-source approach reduces the 'unknown' records that would otherwise fall into default routing queues."
            },
            {
                "workflow": "Account matching with enriched domains",
                "description": "Clay normalizes company domains during enrichment, which directly improves LeanData's lead-to-account matching accuracy. A form fill with just 'john@company.co' gets enriched by Clay to include the company name, HQ, and size, giving LeanData the data it needs to match to the right account."
            },
            {
                "workflow": "Automated ICP scoring and routing",
                "description": "Clay scores prospects against your ideal customer profile using enriched data points (tech stack, headcount, funding stage). LeanData then routes based on ICP tier: Tier 1 accounts go directly to named account reps, Tier 2 enters round-robin, Tier 3 goes to an SDR queue."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "CRM as middleware",
                "detail": "Clay and LeanData connect through your CRM, not directly to each other. Clay pushes enriched records into Salesforce or HubSpot, and LeanData routes them from there. Ensure both tools write to and read from the same CRM fields to maintain data consistency."
            },
            {
                "consideration": "Enrichment before routing",
                "detail": "Configure your CRM automation so Clay's enrichment completes before LeanData's routing triggers. If routing fires on record creation but enrichment hasn't populated key fields yet, leads may route incorrectly. Use workflow delays or trigger sequencing to enforce the correct order."
            },
            {
                "consideration": "Credit management",
                "detail": "Clay charges per enrichment credit across its data waterfall. High-volume list building can burn through credits quickly. Set Clay's enrichment rules to only pull data needed for routing and qualification, not every possible field. Save deeper enrichment for records that pass initial qualification."
            },
            {
                "consideration": "Deduplication responsibility",
                "detail": "Decide whether Clay or LeanData handles deduplication. Clay can deduplicate against your CRM before pushing records. LeanData can merge duplicates after arrival. Running both dedup layers catches more duplicates but adds processing time. Most teams assign initial dedup to Clay and use LeanData for ongoing merge."
            }
        ],
        "faq": [
            {
                "q": "Can Clay replace LeanData for lead routing?",
                "a": "Clay can push records into a CRM and trigger basic workflows, but it doesn't have LeanData's routing engine: visual flow builder, lead-to-account matching, capacity-based distribution, or territory management. Clay is built for data enrichment and list building. LeanData is built for routing. They solve different problems."
            },
            {
                "q": "Do I need a CRM for Clay and LeanData to work together?",
                "a": "Yes. Both tools connect through Salesforce or HubSpot. Clay enriches and pushes data to your CRM. LeanData routes records within your CRM. Without a CRM as the central system, these tools can't communicate with each other."
            },
            {
                "q": "Is this stack overkill for a small team?",
                "a": "For teams under 10 reps, probably yes. Clay's value shines at scale (building lists of hundreds or thousands of prospects). LeanData is most useful when routing complexity exceeds what basic CRM assignment rules can handle. A small team can usually manage with a simpler enrichment tool and native CRM routing until they hit 15-20 reps."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
    },

    # 14. gainsight-churnzero (3)
    {
        "slug": "gainsight-churnzero",
        "tool_a": "gainsight",
        "tool_b": "churnzero",
        "cooccurrence_count": 3,
        "title": "Gainsight vs. ChurnZero: Using or Choosing Between Customer Success Platforms",
        "meta_description": "Gainsight and ChurnZero compared. How they differ, when you need which, and why they appear together in job postings.",
        "overview": "Gainsight and ChurnZero appear together in 3 job postings, usually in customer success leadership roles that require experience with multiple CS platforms. These are competing products, not complementary tools, so the integration story here is about choosing between them, migrating from one to the other, or building CS operations skills that translate across both platforms.",
        "how_they_work_together": [
            {
                "workflow": "Platform migration",
                "description": "Companies switching from Gainsight to ChurnZero (or vice versa) need to migrate health score models, playbooks, customer segments, and historical data. Job postings that mention both tools often seek someone who has managed this migration and can rebuild CS workflows in the new platform."
            },
            {
                "workflow": "Vendor evaluation",
                "description": "CS leaders evaluating customer success platforms frequently compare Gainsight and ChurnZero side-by-side. The evaluation typically includes health scoring flexibility, CRM integration depth, in-app engagement capabilities, and total cost of ownership. Experience with both tools is valued for this reason."
            },
            {
                "workflow": "Multi-product organizations",
                "description": "Some organizations with multiple business units use different CS platforms across divisions. One product line may run Gainsight while another uses ChurnZero, especially after acquisitions. CS ops roles in these companies manage both platforms and work toward consolidation."
            },
            {
                "workflow": "Best practice cross-pollination",
                "description": "CS operators who have used both platforms bring best practices from each. Gainsight's strength in data visualization and executive dashboards can inform ChurnZero implementations. ChurnZero's in-app engagement and real-time alerts can inspire Gainsight configurations."
            }
        ],
        "setup_considerations": [
            {
                "consideration": "Choosing between the two",
                "detail": "Gainsight is the enterprise standard, with deep customization, advanced analytics, and a larger partner ecosystem. ChurnZero is faster to implement, more affordable, and stronger for in-app engagement and real-time alerting. Most teams under 30 CS reps find ChurnZero's time-to-value better; larger enterprises lean toward Gainsight."
            },
            {
                "consideration": "Migration complexity",
                "detail": "Migrating between CS platforms typically takes 3-6 months. Health score models need to be rebuilt (they don't transfer directly). Historical engagement data may require ETL pipelines. Plan for a 30-60 day parallel-running period where both platforms are active before cutting over."
            },
            {
                "consideration": "CRM integration differences",
                "detail": "Gainsight has a Salesforce-native architecture option (installed as a managed package). ChurnZero connects via API. If you're on Salesforce, evaluate whether Gainsight's native approach or ChurnZero's API-based approach better fits your IT architecture and data governance requirements."
            },
            {
                "consideration": "Total cost comparison",
                "detail": "Gainsight enterprise contracts typically start at $40K-60K/year and can exceed $150K for large deployments. ChurnZero pricing starts around $20K-30K/year for mid-market teams. Factor in implementation costs: Gainsight often requires consulting partners ($30K-80K), while ChurnZero implementations are typically handled in-house."
            }
        ],
        "faq": [
            {
                "q": "Is Gainsight or ChurnZero better?",
                "a": "Neither is universally better. Gainsight wins on customization, analytics depth, and enterprise scale. ChurnZero wins on ease of use, implementation speed, and in-app engagement features. ChurnZero is generally better for mid-market SaaS companies. Gainsight is better for enterprise companies with complex CS operations and large data volumes."
            },
            {
                "q": "Can I run both Gainsight and ChurnZero simultaneously?",
                "a": "Technically yes, but practically no. Running two CS platforms doubles the cost and creates confusion about which system is the source of truth for health scores and customer data. The only scenario where both run simultaneously is during a migration period, which should last no more than 60 days."
            },
            {
                "q": "Why do job postings list both Gainsight and ChurnZero?",
                "a": "Employers want CS leaders who understand the category, not just one vendor's tool. Experience with both platforms signals that a candidate can evaluate, implement, and optimize CS operations regardless of which specific tool the company uses. It also indicates the candidate can manage a platform migration if needed."
            }
        ],
        "date_published": DATE_PUBLISHED,
        "date_modified": DATE_MODIFIED,
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
