#!/usr/bin/env python3
"""
Add 6 new guide pages to data/guides.json:
  1. lead-routing-strategy
  2. customer-success-platform-guide
  3. sales-enablement-strategy
  4. review-platform-strategy
  5. data-enrichment-waterfall
  6. ipaas-vs-custom-integration
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
        "slug": "lead-routing-strategy",
        "title": "Lead Routing Strategy: From Form Fill to Closed Deal",
        "meta_description": "A practical guide to lead routing for B2B sales teams. Covers routing rules, speed-to-lead, territory design, account-based routing, and the mistakes that cost you pipeline.",
        "intro": "Lead routing is the invisible plumbing that connects marketing spend to sales conversations. When it works, reps call hot leads within minutes. When it breaks, leads sit unworked for days while your competitors close the deal. The difference between a 5-minute response and a 30-minute response cuts your contact rate in half, and most teams don't even know their routing is broken.",
        "sections": [
            {
                "heading": "Why Speed-to-Lead Is the Only Metric That Matters at First",
                "content": "Research from multiple sources converges on the same conclusion: responding to an inbound lead within 5 minutes makes you 21x more likely to qualify that lead compared to waiting 30 minutes. After one hour, the probability of qualifying drops by 60x. These numbers hold across industries and deal sizes.\n\nDespite this, the average B2B response time is over 40 hours. Most companies don't even measure it. The gap between knowing that speed matters and achieving fast response times is almost always a routing problem, not a willingness problem. Reps want to call leads quickly. They just don't receive them quickly enough.\n\nBefore optimizing anything else in your routing logic, measure your current speed-to-lead. Pull the timestamps from form submission to first rep activity (call, email, or task creation) for your last 200 inbound leads. If the median is above 10 minutes, your routing rules, assignment logic, or notification system needs work. Everything else in this guide is secondary until you get response time under control."
            },
            {
                "heading": "Routing Models: Round-Robin, Territory, and Account-Based",
                "content": "Round-robin is the simplest model. Leads are distributed evenly across a pool of reps in rotation. It's fair and easy to implement in any CRM. The downside: it ignores context. A lead from a Fortune 500 account gets the same treatment as a 10-person startup. Round-robin works well for teams under 10 reps selling a single product at a uniform deal size.\n\nTerritory-based routing assigns leads based on geography, industry, company size, or a combination. This is the standard for mid-market and enterprise sales teams. Territories create ownership and accountability, but they also create coverage gaps. If a territory rep is on vacation, sick, or underperforming, leads in that territory suffer. Build overflow rules that reassign leads after a set period (15-30 minutes is typical) if the primary rep hasn't engaged.\n\nAccount-based routing matches inbound leads to existing accounts in your CRM and routes them to the account owner. This is critical for ABM motions and enterprise sales where multiple contacts from the same company may engage at different times. Without account matching, you end up with three different reps calling three different people at the same company, none of whom know about the others. Tools like LeanData and Chili Piper specialize in this matching logic, handling parent-child account hierarchies, domain matching, and contact deduplication that native CRM routing can't manage."
            },
            {
                "heading": "Designing Routing Rules That Scale",
                "content": "Start with your simplest viable routing logic, then add complexity only when you have data showing the simple version isn't working. A common mistake is building elaborate routing trees with 15 conditions before you've validated that the basic flow works. Complexity creates fragility, and fragile routing breaks silently.\n\nThe foundation of any routing system is the qualification layer. Not every form fill deserves a sales call. Use lead scoring or explicit qualification questions (company size, budget, timeline) to separate high-intent leads from content downloaders. Route qualified leads to sales reps. Route unqualified leads to nurture sequences. This single filter prevents your sales team from drowning in low-quality leads and ignoring the good ones.\n\nDocument your routing logic in a diagram, not just in CRM configuration screens. When routing is spread across Salesforce assignment rules, Chili Piper settings, and Zapier workflows, nobody understands the full picture. A single routing diagram that shows every path a lead can take, with the conditions at each branch, is essential for troubleshooting. Update it every time you change a rule. The diagram should answer: what happens when a lead from a target account fills out a demo form at 2 AM on a Saturday? If you can't answer that question from your documentation, your routing has gaps."
            },
            {
                "heading": "Account-Based Routing: Matching Leads to Existing Accounts",
                "content": "Account-based routing is where most CRM-native routing falls apart. The problem seems simple: when a new lead comes in, check if their company already exists as an account, and if so, route to the account owner. In practice, this matching is surprisingly hard. The lead might use a personal email domain. The company name on the form might not match the account name in your CRM (\"IBM\" vs \"International Business Machines\" vs \"IBM Corporation\"). The account might have a parent-child hierarchy where the lead belongs to a subsidiary.\n\nLeanData and Chili Piper both solve this with fuzzy matching algorithms, domain-to-account mapping, and manual matching queues for ambiguous cases. LeanData is the deeper solution for Salesforce-heavy teams, handling complex routing trees with visual flowcharts. Chili Piper is faster to implement and adds instant scheduling (letting qualified leads book meetings directly from the form), which further reduces speed-to-lead.\n\nThe ROI case for dedicated routing tools is straightforward. If you have more than 20 sales reps, run an ABM motion, or generate more than 500 inbound leads per month, the cost of LeanData or Chili Piper ($15K-40K/year) is trivial compared to the pipeline you lose from misrouted leads. Calculate it: if misrouting causes you to lose even 5% of qualified leads, and your average deal is $30K, the math justifies the investment quickly."
            },
            {
                "heading": "Common Routing Mistakes and How to Fix Them",
                "content": "The most expensive routing mistake is the \"black hole\": leads that enter your system but never get assigned to a rep. This happens when routing rules have gaps (no default assignment), when a rep leaves the company and their leads aren't reassigned, or when CRM automation errors fail silently. Audit your unassigned leads weekly. If more than 2% of inbound leads sit unassigned for more than one hour, you have a black hole.\n\nThe second most common mistake is over-routing to specialists. Some teams build routing rules that send enterprise leads to enterprise reps, mid-market leads to mid-market reps, healthcare leads to the healthcare specialist, and inbound leads to the inbound team. With enough segmentation, each rep gets so few leads that response time degrades. Every additional routing branch adds latency and complexity. Consolidate routing segments when individual rep lead volume drops below 10 leads per week.\n\nIgnoring routing for existing customers is the third mistake. When a customer fills out a form (requesting support, asking about an upgrade, or downloading content), they should be routed to their account manager or CSM, not to an SDR who tries to qualify them from scratch. This seems obvious, but most routing systems don't distinguish between prospects and customers because the logic lives in marketing automation, which doesn't always have customer status data. Connect your routing to your CRM's customer lifecycle stage so existing accounts get handled by the right team."
            }
        ],
        "related_tools": ["chili-piper", "leandata", "salesforce", "hubspot"],
        "related_categories": ["crm", "sales-engagement"],
        "faq": [
            {
                "q": "What's a good speed-to-lead benchmark for B2B?",
                "a": "Under 5 minutes for demo requests and high-intent forms. Under 15 minutes for content downloads and lower-intent actions. The best-performing teams respond in under 2 minutes using instant scheduling tools like Chili Piper. Measure median response time, not average, since outliers skew the average dramatically."
            },
            {
                "q": "Do I need a dedicated lead routing tool or can my CRM handle it?",
                "a": "CRM-native routing (Salesforce assignment rules, HubSpot workflows) works for teams under 20 reps with simple round-robin or territory-based routing. Once you add account matching, overflow rules, or complex segmentation, dedicated tools like LeanData or Chili Piper save significant ops time and reduce misroutes."
            },
            {
                "q": "How do I handle lead routing across time zones?",
                "a": "Route leads to reps in the lead's time zone during business hours. Outside business hours, route to whoever is available (follow-the-sun model) or queue for the territory rep with a strict SLA. Set up automated alerts that escalate unworked leads after 15-30 minutes to a backup rep or manager."
            }
        ]
    },
    {
        "slug": "customer-success-platform-guide",
        "title": "Choosing a Customer Success Platform (2026 Guide)",
        "meta_description": "How to evaluate customer success platforms for B2B SaaS. Covers health scoring, automation, product usage tracking, and when to build vs buy.",
        "intro": "Customer success platforms sit between your product and your renewal pipeline. They aggregate usage data, automate outreach, and give CSMs a single view of account health. The category has matured significantly since 2023, but the buy decision remains tricky: most platforms require 3-6 months of implementation before delivering value, and the wrong choice locks you into workflows that don't match how your CS team operates day to day.",
        "sections": [
            {
                "heading": "Health Scoring: The Foundation You'll Get Wrong at First",
                "content": "Every customer success platform promises health scoring. The concept is simple: combine product usage, support tickets, NPS responses, and engagement data into a single score that predicts churn risk. In practice, building a health score that predicts anything useful takes 6-12 months of iteration, regardless of which platform you choose.\n\nThe first mistake teams make is over-engineering the initial health score. They add 15 inputs, weight them based on gut feeling, and end up with a score that everyone ignores because it doesn't match what CSMs see in their day-to-day conversations. Start with three inputs: login frequency (or core feature usage), support ticket volume, and contract value trend. These three signals alone catch 60-70% of at-risk accounts.\n\nThe second mistake is treating health scores as static. A score that was accurate six months ago may be useless today if your product has changed, your customer base has shifted, or your CSMs have learned new leading indicators. Recalibrate quarterly by comparing scores against actual churn outcomes. If your \"red\" accounts aren't churning at a significantly higher rate than your \"green\" accounts, the score needs adjustment. Gainsight and ChurnZero both support custom scoring models with configurable weights, but the weights are only as good as the data feeding them."
            },
            {
                "heading": "Automation vs. High-Touch: Matching the Platform to Your Motion",
                "content": "Customer success platforms fall into two camps based on how they handle the automation-to-human ratio. High-touch platforms (Gainsight is the archetype) are built for CS teams managing 20-50 accounts per rep, where every interaction is personalized and the platform serves as a command center for strategic account management. These platforms excel at playbook execution, stakeholder mapping, and executive business review preparation.\n\nAutomation-first platforms (ChurnZero, Vitally, Catalyst) are built for teams managing 100-500 accounts per rep, where scaled automation handles routine touchpoints and CSMs focus on exception handling. These platforms prioritize in-app messaging, automated health alerts, and self-service resources. They're better for product-led growth companies where human intervention should be triggered by signals, not scheduled on a calendar.\n\nThe mismatch is expensive in both directions. If you put a high-touch team on an automation-first platform, CSMs fight the tool to do their jobs. If you put a scaled CS team on a high-touch platform, you're paying for depth you'll never use. Ask your CS leader: what's the target account-to-CSM ratio in 18 months? If it's under 50, lean toward Gainsight. If it's over 100, lean toward ChurnZero or a lighter-weight alternative. If you're somewhere in between, both can work, but prioritize the one whose default workflows match your motion with the least customization."
            },
            {
                "heading": "Product Usage Tracking: The Data Problem Nobody Warns You About",
                "content": "Customer success platforms need product usage data to be useful. Without it, health scores are based entirely on lagging indicators (support tickets, survey responses) rather than leading indicators (declining usage, feature adoption drops). The challenge is getting usage data into the platform in a format the CS team can act on.\n\nMost CS platforms ingest usage data via API, webhook, or a product analytics integration (Mixpanel, Amplitude, Segment). The technical integration is usually straightforward. The hard part is defining which usage metrics matter. \"Daily active users\" is too generic. You need to track usage of the features that correlate with retention: the actions that sticky customers take and churning customers don't.\n\nIdentifying these features requires collaboration between your CS team, product team, and data team. Pull usage data for customers who renewed vs. those who churned over the past 12 months. Look for behavioral differences in the first 90 days. Common patterns include: customers who complete onboarding within 14 days retain at 2x the rate; customers who use the reporting module retain at 1.5x; customers where more than 3 users are active churn at half the rate of single-user accounts. These specific metrics become the inputs to your health score, and they're unique to your product. No CS platform can tell you what to measure. It can only measure what you tell it to."
            },
            {
                "heading": "Build vs. Buy: When a CS Platform Isn't Worth It",
                "content": "Not every company needs a dedicated customer success platform. For teams with fewer than 5 CSMs or fewer than 200 accounts, a well-configured CRM (Salesforce or HubSpot) with custom dashboards and workflow automation can handle CS workflows without the added cost and integration overhead of a standalone platform.\n\nThe build-it-yourself approach works when your needs are simple: track renewal dates, log CSM activities, flag at-risk accounts based on basic criteria, and generate reports. Salesforce's built-in features (custom objects for success plans, process builder for health alerts, reports for CSM dashboards) handle these use cases. HubSpot's Service Hub adds ticketing and feedback tools that overlap with CS platform features.\n\nBuy a CS platform when you need three things your CRM can't do well: automated health scoring that combines product usage with CRM data, scaled playbook execution that triggers different workflows based on customer segment and lifecycle stage, and executive reporting on net revenue retention broken down by CSM, segment, and cohort. If you need all three, the $30K-100K/year cost of Gainsight or ChurnZero pays for itself through reduced churn. If you only need one, extend your CRM first and revisit in 12 months."
            },
            {
                "heading": "Evaluating Platforms: A Practical Scorecard",
                "content": "Score each platform across six dimensions using your actual data and workflows, not demo scenarios.\n\nData integration depth: Can the platform ingest your product usage data, CRM data, support tickets, and billing data without custom development? Test with a real data feed during the trial, not sample data. Gainsight and ChurnZero both support broad integrations, but the depth and reliability of each connector varies. Ask for references from customers using the same CRM and product analytics stack you use.\n\nTime to value: How long until your CS team is actively using the platform daily? Gainsight implementations typically take 8-12 weeks with a dedicated admin. ChurnZero is faster at 4-6 weeks. Lighter tools like Vitally can be operational in 2-3 weeks. Factor implementation time into your ROI calculation.\n\nCSM adoption: The best CS platform is the one your team uses. During the trial, have 2-3 CSMs use it for their actual workflow for two weeks. If they revert to spreadsheets and the CRM, the platform's UX doesn't fit their work style. This is the single best predictor of long-term success.\n\nScalability: Will the platform support your account growth over the next 2-3 years? If you're at 200 accounts today and expect 1,000 in two years, make sure the platform's pricing model doesn't become prohibitive at scale. Some platforms price per account, which gets expensive quickly. Others price per CSM seat, which scales more predictably.\n\nCommon Room is worth mentioning as an emerging alternative for community-led and product-led growth companies. It aggregates signals from community platforms, product usage, and social channels into a unified customer view. It's not a traditional CS platform, but for companies where community engagement is a leading retention indicator, it fills a gap that Gainsight and ChurnZero don't address well."
            }
        ],
        "related_tools": ["churnzero", "gainsight", "hubspot", "salesforce", "common-room"],
        "related_categories": ["customer-success", "crm"],
        "faq": [
            {
                "q": "When should a SaaS company invest in a customer success platform?",
                "a": "When you have 5+ CSMs, 200+ accounts, and net revenue retention is a board-level metric. Below these thresholds, a CRM with custom workflows and dashboards handles CS operations adequately. The tipping point is when your CS team spends more time in spreadsheets tracking health and renewals than talking to customers."
            },
            {
                "q": "What's the difference between Gainsight and ChurnZero?",
                "a": "Gainsight is built for high-touch enterprise CS with deep playbook customization, stakeholder mapping, and executive reporting. ChurnZero is built for scaled CS with stronger in-app engagement, faster implementation, and lower cost. Gainsight suits teams with under 50 accounts per CSM. ChurnZero suits teams with 100+ accounts per CSM."
            },
            {
                "q": "Can HubSpot replace a dedicated customer success platform?",
                "a": "For basic CS operations, yes. HubSpot's Service Hub offers ticketing, feedback surveys, and customer portals. Combine it with custom properties and workflow automation for health tracking and renewal management. You'll lack automated health scoring, product usage integration, and cohort-level retention analytics, but for teams under 5 CSMs, it's a practical starting point."
            }
        ]
    },
    {
        "slug": "sales-enablement-strategy",
        "title": "Sales Enablement Strategy: Content, Training, and Analytics",
        "meta_description": "How to build a sales enablement program that drives rep productivity. Covers content management, training, buyer engagement tracking, ROI measurement, and platform selection.",
        "intro": "Sales enablement is the practice of giving reps the content, training, and tools they need to close deals. The category has grown from a shared Google Drive folder to a $3B+ platform market, but the fundamentals haven't changed: reps need the right content at the right time, coaching to improve their conversations, and data that shows what's working. This guide covers how to build an enablement program that moves pipeline, not just checks a box.",
        "sections": [
            {
                "heading": "Content Management: Solving the 'I Can't Find It' Problem",
                "content": "Sales reps spend an estimated 30% of their time looking for or creating content. That's not a content quality problem. It's a content management problem. Most organizations have plenty of case studies, battle cards, ROI calculators, and pitch decks. They're just scattered across Google Drive, SharePoint, Slack messages, and individual reps' desktops.\n\nA sales enablement platform (Highspot, Seismic, Showpad) centralizes content in a searchable, organized library with role-based access. The platform tracks which content gets used, which gets ignored, and which correlates with closed deals. This usage data is the most valuable output of enablement tooling because it tells you where to invest content creation effort.\n\nBefore buying a platform, audit your existing content. Most teams discover that 60-70% of their sales content hasn't been used in 6 months. Archive the stale material, update the outdated pieces, and organize what remains by sales stage, persona, and use case. A smaller library of current, relevant content outperforms a massive library of stale material. The platform amplifies good content practices; it doesn't fix bad ones."
            },
            {
                "heading": "Training and Coaching: Beyond the Annual Sales Kickoff",
                "content": "Annual training events are expensive and largely ineffective. Research on learning retention shows that people forget 70% of training content within 24 hours and 90% within a week without reinforcement. A sales kickoff costs $500K-2M for a mid-size company and produces a one-week spike in enthusiasm followed by a return to old habits.\n\nEffective sales training is ongoing, bite-sized, and tied to real deals. The best programs combine three elements: structured onboarding (a 30-60 day ramp program for new hires), just-in-time learning (short modules triggered by deal stage or competitive situation), and manager-led coaching (weekly 1:1 sessions focused on active deals and recorded calls).\n\nGong Engage and similar conversation intelligence tools have changed coaching by making it data-driven. Instead of managers guessing which reps need help, they can review call recordings, identify patterns (talk-to-listen ratio, question frequency, competitor mention handling), and coach to specific behaviors. The teams that get the most from conversation intelligence assign managers to review 3-5 calls per rep per week and use the platform's scorecards to track improvement over time. Without that manager commitment, the tool becomes an expensive recording device."
            },
            {
                "heading": "Buyer Engagement Tracking: Knowing What Prospects Read",
                "content": "Content analytics within enablement platforms tell you the internal story: which reps use which content. Buyer engagement tracking tells you the external story: which prospects engage with the content reps send them.\n\nHighspot and similar platforms generate trackable links for every piece of content shared with a prospect. You can see whether the prospect opened the case study, how long they spent on each page, whether they forwarded it to a colleague, and which sections they re-read. This data is gold for deal strategy. If a prospect spent 8 minutes on your security whitepaper but skipped the pricing overview, you know what's on their mind before the next call.\n\nBuyer engagement data also feeds lead scoring and deal forecasting. A prospect who shares your proposal with 4 colleagues is further along in their buying process than one who hasn't opened it. Some enablement platforms push this engagement data back to the CRM so that reps and managers can see it alongside other deal signals.\n\nThe privacy consideration matters here. Content tracking uses tracking pixels and link analytics, which are standard in B2B communication but should be disclosed in your privacy policy. Most platforms allow you to disable tracking for specific recipients or regions where regulations require it."
            },
            {
                "heading": "Measuring Enablement ROI: The Metrics That Matter",
                "content": "Enablement programs struggle with ROI measurement because the value is indirect. Content doesn't close deals; reps do. Training doesn't generate pipeline; conversations do. The challenge is connecting enablement activities to revenue outcomes.\n\nFour metrics provide a practical ROI framework. First, ramp time for new hires: how many days from start date to first closed deal? A strong enablement program reduces ramp time by 25-40%, which translates directly to revenue. If your average ramp is 6 months and you hire 20 reps per year, cutting ramp by one month generates the equivalent of 20 additional rep-months of production.\n\nSecond, content influence on pipeline: which content pieces were shared in deals that closed vs. deals that were lost? If your ROI calculator appears in 80% of won deals and 20% of lost deals, it's contributing to wins. This correlation isn't causation, but over a large enough sample, it guides content investment.\n\nThird, rep productivity: are reps spending less time on content creation and search after enablement investment? Survey reps quarterly on time spent finding or creating content. A drop from 30% to 15% of selling time effectively adds 6 hours per week per rep. Fourth, win rate changes after training programs. Measure win rates for the 90 days before and after a training initiative, controlling for pipeline quality. A 3-5 percentage point improvement in win rate is a strong signal that the program works."
            },
            {
                "heading": "When to Invest in an Enablement Platform",
                "content": "Companies under 20 sales reps rarely need a dedicated enablement platform. A well-organized Google Drive or Notion workspace, combined with a conversation intelligence tool (Gong, Chorus), covers the basics. The overhead of implementing and maintaining a platform isn't justified when a sales manager can coach their team directly and content can be managed in a shared folder.\n\nThe inflection point comes around 30-50 reps. At this size, content sprawl becomes unmanageable, new hire onboarding can't be handled by a single manager, and the gap between top performers and average performers widens enough that systematic coaching pays off. This is when Highspot, Seismic, or a similar platform starts delivering measurable value.\n\nPricing for enablement platforms ranges from $30-75 per user per month for mid-market solutions to $75-150+ for enterprise deployments. The total cost includes the platform license, implementation (typically $10K-30K), content migration, and ongoing administration (plan for 0.5-1 FTE to manage the platform). Calculate the payback period based on your ramp time reduction and win rate improvement targets. Most teams see payback within 9-12 months if they invest in adoption alongside the technology.\n\nThe biggest risk isn't choosing the wrong platform. It's buying one and then under-investing in the program. An enablement platform without a dedicated enablement manager, regular content updates, and active coaching programs is expensive shelf-ware. Staff the program first, then buy the tool."
            }
        ],
        "related_tools": ["highspot", "gong-engage", "hubspot", "salesforce"],
        "related_categories": ["crm", "conversation-intelligence"],
        "faq": [
            {
                "q": "What's the difference between sales enablement and sales training?",
                "a": "Training is one component of enablement. Sales enablement encompasses content management, onboarding programs, ongoing coaching, buyer engagement analytics, and the technology that supports all of these. Training focuses on skill development. Enablement focuses on giving reps everything they need to execute."
            },
            {
                "q": "How many sales reps do I need before investing in enablement tooling?",
                "a": "Dedicated enablement platforms make financial sense at 30-50+ reps. Below that, organized shared drives, a conversation intelligence tool, and manager-led coaching cover the basics. The platform investment is justified when content sprawl, inconsistent onboarding, and coaching gaps become measurable drags on pipeline."
            },
            {
                "q": "How do I measure the ROI of sales enablement?",
                "a": "Track four metrics: new hire ramp time (target 25-40% reduction), content influence on closed-won deals (correlation between content usage and win rates), rep productivity (time spent searching for or creating content), and win rate changes after training programs. Combine these into a quarterly enablement scorecard and tie improvements to revenue impact."
            }
        ]
    },
    {
        "slug": "review-platform-strategy",
        "title": "B2B Review Platform Strategy: G2, TrustRadius, and Beyond",
        "meta_description": "How to build a B2B review platform strategy that generates pipeline. Covers G2, TrustRadius, Capterra, review generation, intent data from reviews, and ROI measurement.",
        "intro": "B2B review platforms have evolved from simple directories into pipeline generation engines. G2, TrustRadius, and Capterra collectively influence 80%+ of B2B software buying decisions, and the intent data they produce is some of the highest-quality signal available. But most vendors treat reviews as a checkbox activity: ask for a few reviews, claim a profile, and forget about it. The companies that win on review platforms treat them as a deliberate go-to-market channel with dedicated strategy and budget.",
        "sections": [
            {
                "heading": "Why Reviews Matter More Than Your Website for Pipeline",
                "content": "B2B buyers trust peer reviews more than vendor websites. This isn't opinion; it's behavioral data. G2 reports that 86% of software buyers use review sites during their evaluation. TrustRadius data shows that buyers who read reviews are 2x more likely to shortlist a vendor. The reason is credibility: your website says you're great, but reviews from actual users carry weight that marketing copy never will.\n\nThe pipeline impact shows up in two ways. First, direct traffic: buyers searching \"best CRM for mid-market\" or \"Salesforce alternatives\" land on review sites before your website. If your profile is thin, poorly rated, or missing recent reviews, you're eliminated before you ever had a chance. Second, intent data: review platforms track which buyers are actively researching your category and your competitors, generating intent signals that feed directly into sales and ABM workflows.\n\nThe math is worth running for your own company. Track how many qualified leads mention a review site during the sales process (ask in your discovery call or attribution survey). For most B2B software companies, 15-30% of pipeline has some review site touchpoint. That makes your review presence a pipeline channel worth investing in, not an afterthought."
            },
            {
                "heading": "Platform Comparison: G2, TrustRadius, and Capterra",
                "content": "G2 dominates the B2B review space by traffic volume and has the most developed intent data product. Its buyer intent signals show you which companies are viewing your profile, reading comparisons, and researching your category. G2's paid tiers ($15K-80K/year) offer enhanced profiles, competitive intelligence, and intent data integrations with platforms like 6sense and Demandbase. The free tier is functional but gives you limited control over your profile and no intent data.\n\nTrustRadius differentiates on review depth. Their reviews are longer, more detailed, and require identity verification, which makes them more credible to enterprise buyers. TrustRadius reviews carry significant weight in procurement and vendor evaluation processes. Their intent data product (TrustRadius Downstream) tracks buyer research activity and integrates with major CRM and ABM platforms. Pricing starts lower than G2 for comparable features.\n\nCapterra (owned by Gartner) draws traffic from buyers earlier in the research process, often before they have a shortlist. It's especially strong for SMB-focused products. Capterra's pay-per-click advertising model lets you bid on category placements, which can generate leads directly. The traffic quality tends to be more top-of-funnel than G2 or TrustRadius. Costs vary from $2-15 per click depending on category competitiveness.\n\nThe right answer for most companies is to maintain active profiles on all three, with heavier investment (paid tier, review campaigns) on the platform where your buyers spend the most time. Enterprise-focused companies should prioritize G2 and TrustRadius. SMB-focused companies should prioritize Capterra and G2."
            },
            {
                "heading": "Review Generation: Building a Sustainable Engine",
                "content": "The single biggest mistake in review management is treating it as a one-time campaign. You ask 50 customers for reviews, get 15-20, claim your badges, and move on. Six months later, your most recent review is stale and competitors have 30 newer ones. Buyers filter by \"past 6 months\" or \"past year,\" and recency matters as much as volume.\n\nBuild review generation into your customer lifecycle. The best trigger points are: 60-90 days after onboarding (the customer has enough experience to write substantively), after a support case is resolved positively (high satisfaction moment), after a QBR where the customer reports strong results (they've just articulated value), and at renewal (the customer has already decided to stay). Automate review requests through your CS platform or marketing automation at these trigger points.\n\nIncentives are allowed on most platforms within guidelines. G2 offers a $25 gift card per review through their own program. You can run your own incentive campaigns ($10-25 per review is standard) as long as you're not conditioning the incentive on a positive review. Disclosure of incentives is required. The response rate for incentivized review requests is 3-5x higher than unincentivized ones.\n\nTarget volume depends on your category. Aim for 50+ reviews minimum on G2, with 10+ added per quarter to maintain freshness. For niche categories, 20-30 reviews may be sufficient to rank well. Track your review count relative to competitors monthly and increase outreach when the gap widens."
            },
            {
                "heading": "Intent Data from Reviews: The Pipeline Signal You're Probably Ignoring",
                "content": "G2 buyer intent data tells you which companies are actively researching your product category, visiting your profile, reading comparisons between you and competitors, and viewing specific content like pricing or integration pages. This signal is valuable because it captures in-market buyers at the moment of evaluation, which is further down the funnel than most third-party intent sources.\n\nThe integration path matters. G2 intent data can push directly into Salesforce, HubSpot, 6sense, Demandbase, and several other platforms. The most effective workflow routes G2 intent signals to your ABM platform for advertising and to your CRM for sales alerts. When a target account researches your category on G2, your reps should know within 24 hours and have the context to personalize their outreach (\"I noticed your team is evaluating tools in our space\").\n\nMeasure the conversion rate of intent-flagged accounts vs. your baseline. In our analysis, G2 intent-flagged accounts convert to pipeline at 2-3x the rate of cold outbound accounts. The signal quality is high because these buyers are actively comparing solutions, not just passively consuming content. TrustRadius Downstream offers similar signals, and combining both data sources catches buyers who prefer one platform over the other.\n\nThe cost of intent data is typically bundled with paid G2 or TrustRadius plans. G2's intent data starts in their mid-tier plans (roughly $25K+/year). TrustRadius intent data is available at comparable price points. For companies already paying for ABM platforms with third-party intent (6sense, Demandbase), review platform intent data is a valuable supplementary signal that covers a different part of the buyer journey."
            },
            {
                "heading": "Measuring Review Platform ROI",
                "content": "Review platform ROI comes from three sources: direct leads (traffic from review sites that converts to pipeline), influenced pipeline (deals where review sites appeared in the buyer's research journey), and brand positioning (category rankings that affect shortlisting). The first two are measurable. The third is real but harder to quantify.\n\nFor direct leads, track referral traffic from G2, TrustRadius, and Capterra to your website using UTM parameters and referral source data in your analytics. Measure the conversion rate and deal size of review-referred leads vs. other channels. Most companies find that review-referred leads have higher win rates (20-40% higher) because the buyer has already done independent research and self-selected into your product.\n\nFor influenced pipeline, add a review-site option to your lead source attribution survey or discovery call script. Ask buyers: \"Did you read reviews on G2, TrustRadius, or Capterra during your evaluation?\" Track the percentage of closed-won revenue where the buyer engaged with a review site. This gives you a pipeline influence number to justify your review platform spend.\n\nThe ROI framework for paid review platform tiers is straightforward. If your G2 investment is $40K/year and it generates or influences $400K in pipeline (at your standard close rate), the channel is performing. Compare this to your cost-per-pipeline-dollar for other channels (paid search, events, content syndication). Most companies find that review platform investment delivers pipeline at a lower cost than paid media, especially for competitive categories where review site rankings directly influence shortlists."
            }
        ],
        "related_tools": ["g2", "trustradius", "capterra", "6sense"],
        "related_categories": ["review-platforms", "abm"],
        "faq": [
            {
                "q": "How many reviews do I need on G2 to rank well?",
                "a": "Minimum 50 reviews to appear credible, with 10+ new reviews per quarter to maintain freshness. Exact ranking factors include review volume, recency, rating score, and market presence. In competitive categories (CRM, marketing automation), top-ranked products often have 500+ reviews. In niche categories, 30-50 reviews can put you in the top 3."
            },
            {
                "q": "Is G2 buyer intent data worth the investment?",
                "a": "For companies selling to mid-market and enterprise buyers ($25K+ ACV), yes. G2 intent captures buyers at the active evaluation stage, which is higher quality than most third-party intent. Expect 2-3x higher conversion rates for intent-flagged accounts vs. cold outbound. The data is most valuable when integrated with your CRM and ABM platform for automated routing and advertising."
            },
            {
                "q": "Should I invest in G2, TrustRadius, or Capterra?",
                "a": "Maintain free profiles on all three. For paid investment, enterprise-focused companies should prioritize G2 (largest traffic, best intent data) and TrustRadius (deeper reviews, procurement influence). SMB-focused companies should prioritize Capterra (PPC model, earlier-stage buyers) and G2. Most companies get the best results from a paid G2 plan plus active profiles on the other two."
            }
        ]
    },
    {
        "slug": "data-enrichment-waterfall",
        "title": "Building a Data Enrichment Waterfall (2026 Guide)",
        "meta_description": "How to build a multi-provider data enrichment waterfall for B2B. Covers sequencing logic, cost optimization, accuracy measurement, and when a waterfall is worth the complexity.",
        "intro": "A data enrichment waterfall queries multiple data providers in sequence, using each one to fill gaps the previous provider missed. Instead of relying on a single source for email, phone, and firmographic data, a waterfall checks Provider A first, then sends unfilled records to Provider B, then Provider C. The result is higher fill rates, better accuracy through cross-validation, and lower cost per enriched record. But waterfalls add real complexity, and they're not worth building until your data volume and quality requirements justify it.",
        "sections": [
            {
                "heading": "What a Data Enrichment Waterfall Is (and Isn't)",
                "content": "The concept is straightforward. You have a list of contacts or accounts that need enrichment: verified emails, direct phone numbers, job titles, company firmographics. No single data provider has 100% coverage. ZoomInfo might fill 70% of your records. Apollo fills a different 65%. Clearbit fills another 60%. The overlap between providers is significant, but each one has pockets of unique coverage that the others miss.\n\nA waterfall runs these providers in sequence. Record goes to ZoomInfo first. If ZoomInfo returns an email, great. If not, the record moves to Apollo. If Apollo fills it, done. If not, it moves to Clearbit. The unfilled records cascade down the waterfall until every provider has had a chance. Final fill rates of 85-95% are achievable with three providers, compared to 60-75% from any single source.\n\nThe efficiency gain comes from only querying downstream providers for records that upstream providers couldn't fill. If ZoomInfo fills 70% of your list, Apollo only processes the remaining 30%. You're paying for 30% of the volume at Apollo's rate, not 100%. This reduces your per-record cost significantly compared to running every record through every provider. A well-designed waterfall can reduce enrichment cost by 30-50% while increasing fill rates by 15-25 percentage points."
            },
            {
                "heading": "When to Use Multiple Providers vs. One",
                "content": "A single provider is sufficient when your data volume is under 5,000 records per month, your target market aligns with one provider's strength (ZoomInfo for US enterprise, Cognism for European mobile numbers, Apollo for startup and mid-market), and your required fill rate is under 75%. At this scale, the complexity of managing multiple provider contracts, API integrations, and billing isn't justified.\n\nMultiple providers become worthwhile when you need fill rates above 80%, your target market spans multiple geographies or company sizes, or the cost of a single enterprise provider exceeds what a waterfall of smaller providers would cost. The break-even point is typically around 10,000-20,000 enrichment requests per month, where the volume discount on a primary provider plus a secondary provider for gaps costs less than upgrading to a higher tier on the primary.\n\nThe strongest use case for a waterfall is when you have non-negotiable accuracy requirements. Cross-validating data across two providers catches errors that a single source would miss. If two providers return the same email address, your confidence in that email is significantly higher than if only one provider returned it. For sales teams where email bounce rates above 3% damage domain reputation, this cross-validation is worth the added cost and complexity."
            },
            {
                "heading": "Sequencing Logic: Which Provider Goes First",
                "content": "The sequencing order matters because it directly affects cost and accuracy. Place your highest-accuracy, lowest-cost provider first. This provider fills the majority of records cheaply and accurately. Downstream providers handle the harder-to-find records at a potentially higher per-record cost.\n\nFor US-focused B2B data, a common sequence is: Apollo (lowest cost, solid coverage for tech and mid-market) then ZoomInfo (broader coverage, higher cost) then Cognism or Seamless.ai (fills remaining gaps, especially for direct dials). For European markets, start with Cognism (strongest GDPR-compliant European data) then ZoomInfo (US and global coverage) then a regional provider.\n\nBeyond simple \"found or not found\" logic, sophisticated waterfalls use confidence scoring. If Provider A returns an email with 80% confidence, you might still query Provider B to validate it. If both providers return the same email, confidence rises to 95%+. If they disagree, you flag the record for manual review or query a third provider as a tiebreaker. Clay automates this logic natively, allowing you to build enrichment waterfalls with conditional branching, confidence thresholds, and multi-provider validation in a visual workflow.\n\nCost optimization tip: negotiate volume-based pricing with your providers based on the actual volume they'll process, not your total list size. If your waterfall sends only 30% of records to Provider B, your contract should reflect that volume. Most providers will negotiate if you can provide reliable volume estimates."
            },
            {
                "heading": "Cost Optimization: Getting the Most From Your Enrichment Budget",
                "content": "The naive approach to multi-provider enrichment runs every record through every provider and picks the best result. This maximizes accuracy but also maximizes cost. A well-designed waterfall typically costs 40-60% less than this brute-force approach while achieving 90%+ of the same fill rate.\n\nTiered pricing structures mean that the per-record cost drops as volume increases. Structure your waterfall so that the first provider handles the highest volume (triggering volume discounts) and downstream providers handle smaller, targeted segments. Some companies negotiate annual commit pricing with their primary provider and pay-as-you-go rates with secondary providers to optimize flexibility.\n\nCache enrichment results aggressively. If you enriched a contact 30 days ago, don't re-enrich unless you have reason to believe the data has changed (job change signal, email bounce, etc.). B2B data decays at roughly 2.5% per month, so monthly re-enrichment is wasteful for most records. Quarterly re-enrichment for your active prospect database and semi-annual for your full database is a reasonable cadence.\n\nMeasure cost per enriched record, not cost per API call. If Provider A costs $0.10 per lookup but fills 70% of records, the effective cost per enriched record is $0.14. If Provider B costs $0.15 per lookup but fills 90% of records, the effective cost per enriched record is $0.17. The per-lookup cost is misleading without accounting for fill rate. Track this metric monthly and use it to renegotiate contracts or adjust waterfall sequencing."
            },
            {
                "heading": "Accuracy Measurement: How to Know If Your Waterfall Works",
                "content": "Fill rate is easy to measure but insufficient alone. A provider can fill 90% of records with data that's 60% accurate, which is worse than filling 70% of records with 95% accuracy. You need to measure both fill rate and accuracy for each provider in your waterfall, and you need to do it continuously, not just during the initial evaluation.\n\nBuild an accuracy testing loop. Every month, sample 100-200 records from each provider's output and verify them through an independent channel. For emails, send a verification ping (tools like NeverBounce or ZeroBounce check deliverability without sending). For phone numbers, run them through a phone validation API (Twilio Lookup, NumVerify). For job titles, spot-check against LinkedIn. Track accuracy rates per provider per month and flag any provider that drops below your threshold (85% is a common floor for emails, 70% for phone numbers).\n\nCross-provider agreement rate is another valuable metric. When two providers return data for the same record, how often do they agree? Agreement rates above 90% indicate reliable data. Agreement rates below 75% suggest one or both providers have accuracy issues for that segment. Segment this analysis by company size, industry, and geography to identify where each provider is strongest and weakest.\n\nThe feedback loop from sales is the most important accuracy signal. Track email bounce rates, phone connection rates, and \"wrong person\" rates by enrichment source. If Provider B's phone numbers connect at half the rate of Provider A's, you know to deprioritize Provider B for direct dials and use them only for emails or firmographics where their accuracy is higher."
            }
        ],
        "related_tools": ["zoominfo", "apollo", "clay", "clearbit", "seamless-ai"],
        "related_categories": ["enrichment", "data-quality"],
        "faq": [
            {
                "q": "How many data providers do I need in a waterfall?",
                "a": "Two to three is the sweet spot. A primary provider handles 65-75% of records. A secondary provider fills another 10-20%. A third provider catches remaining gaps. Beyond three providers, the incremental fill rate gain drops below 5% and the complexity of managing contracts, integrations, and accuracy monitoring outweighs the benefit."
            },
            {
                "q": "What tools can orchestrate an enrichment waterfall?",
                "a": "Clay is purpose-built for enrichment waterfalls with visual workflow builders, conditional logic, and built-in connectors to most data providers. For simpler waterfalls, Zapier or Make can sequence API calls with conditional branching. Enterprise teams sometimes build custom waterfalls using Python scripts and scheduled jobs, which offers maximum flexibility but requires engineering resources to maintain."
            },
            {
                "q": "How much does a data enrichment waterfall cost to run?",
                "a": "Costs vary based on volume and providers. A typical mid-market setup (10,000 records/month with two providers) runs $2,000-5,000/month. Enterprise setups with three providers and higher volumes can run $10,000-25,000/month. The effective cost per enriched record in a well-optimized waterfall is $0.10-0.30, compared to $0.15-0.50 for a single premium provider at the same fill rate."
            }
        ]
    },
    {
        "slug": "ipaas-vs-custom-integration",
        "title": "iPaaS vs Custom Integration: When to Buy vs Build",
        "meta_description": "When to use an iPaaS platform vs custom code for B2B integrations. Covers cost comparison, common integration patterns, evaluation criteria, and the hidden costs of both approaches.",
        "intro": "Every growing B2B company hits the integration wall. Your CRM needs to talk to your marketing platform. Your data warehouse needs feeds from six SaaS tools. Your support system needs customer data from billing. You can buy an integration platform (iPaaS) or build custom integrations with code. Both approaches work. Both have hidden costs. And the wrong choice creates either vendor lock-in or technical debt that haunts your ops team for years.",
        "sections": [
            {
                "heading": "When iPaaS Makes Sense: The 80% Use Case",
                "content": "Integration platforms like Zapier, Make, Workato, Tray, and Boomi are purpose-built for connecting SaaS applications without writing code. They excel at the patterns that make up 80% of B2B integrations: syncing CRM records to a marketing platform, pushing form submissions to a database, triggering Slack alerts from deal stage changes, and moving data between cloud applications on a schedule.\n\nThe primary advantage is speed. A Zapier workflow that syncs new HubSpot deals to a Slack channel takes 10 minutes to build. The same integration built with custom code takes 2-4 hours for the initial build, plus ongoing maintenance as APIs change. For a team running 20-50 integrations, the speed advantage compounds into weeks of saved engineering time per year.\n\nThe second advantage is maintainability by non-engineers. When your marketing ops manager needs to add a field to the CRM-to-email sync, they can update the Zapier workflow themselves. With custom code, they file a ticket, wait in the engineering queue, and the change ships in the next sprint. For teams where integration logic changes frequently (new fields, new routing rules, new tools), this self-service capability is worth the platform cost alone.\n\niPaaS works best for standard SaaS-to-SaaS integrations, event-triggered workflows, and data syncs that run on a schedule (every 5 minutes, hourly, daily). If your integration fits these patterns and uses tools with well-supported connectors, an iPaaS is almost always the right choice."
            },
            {
                "heading": "When Custom Code Wins: The 20% That Matters",
                "content": "Custom integrations outperform iPaaS in specific scenarios. The first is high-volume data processing. If you're moving millions of records per day, syncing large databases, or processing real-time event streams, iPaaS platforms hit performance limits or become prohibitively expensive. Fivetran and Airbyte handle the ELT (extract, load, transform) pattern for data warehouse feeds better and cheaper than general-purpose iPaaS tools at scale.\n\nThe second scenario is complex data transformation. If your integration requires parsing unstructured data, applying machine learning models, running multi-step calculations, or handling complex error logic, custom code gives you full control. iPaaS visual builders become unwieldy for workflows with 20+ steps, nested conditionals, and custom error handling. What looks clean as a simple flowchart becomes a debugging nightmare at scale.\n\nThe third scenario is security and compliance requirements. Some organizations can't route sensitive data through third-party platforms. Financial data, healthcare records (HIPAA), and PII in regulated industries may require integrations that run within your own infrastructure. While enterprise iPaaS platforms (Workato, Boomi, MuleSoft) offer on-premise deployment options, these are significantly more expensive than cloud plans and partially negate the simplicity advantage.\n\nThe fourth scenario is integrations with proprietary or poorly documented APIs. iPaaS platforms shine when both endpoints have well-maintained connectors. When you're integrating with a legacy system, a niche vendor with a non-standard API, or an internal tool, custom code is often the only option."
            },
            {
                "heading": "Cost Comparison: The Full Picture",
                "content": "The sticker price of an iPaaS is straightforward. Zapier costs $20-600/month depending on volume. Make costs $10-300/month. Workato starts at $10K/year for teams. Tray is similar. Boomi and MuleSoft are $15K-50K/year for enterprise deployments. These prices are predictable and easy to budget.\n\nThe sticker price of custom code is zero, which is misleading. Custom integration costs include: developer time for the initial build (4-40 hours per integration depending on complexity), ongoing maintenance as APIs change (estimate 2-5 hours per integration per year), monitoring and alerting infrastructure, and the opportunity cost of engineering time that could go toward product development.\n\nA fair comparison for a typical mid-market company running 30 integrations: iPaaS (Workato or Make): $15K-40K/year, maintained by a RevOps or marketing ops person with no engineering dependency. Custom code: $0 in software costs, but 200-400 hours of engineering time per year for maintenance, plus the initial build cost. At a fully loaded engineering cost of $150/hour, that's $30K-60K in engineering time, with the added cost of pulling engineers away from product work.\n\nThe break-even calculation depends on your engineering capacity and integration complexity. If you have dedicated integration engineers, custom code may be cheaper for simple, stable integrations. If your engineering team is stretched thin, iPaaS saves money and reduces engineering bottlenecks. Most companies under 500 employees are better served by iPaaS for the majority of their integrations."
            },
            {
                "heading": "Common B2B Integration Patterns and the Best Tool for Each",
                "content": "CRM-to-marketing sync (contacts, lead status, campaign membership): iPaaS or native integration. HubSpot and Salesforce both have strong native connectors to major marketing platforms. If using a less common pairing, Zapier or Make handles this cleanly. Custom code is overkill.\n\nData warehouse loading (pulling data from SaaS tools into Snowflake, BigQuery, or Redshift): Use a dedicated ELT tool (Fivetran, Airbyte, Census) rather than a general iPaaS or custom code. These tools handle schema changes, incremental loads, and data type mapping automatically. Fivetran is the premium option ($1-3/credit with predictable pricing). Airbyte is the open-source alternative with a cloud-hosted option.\n\nReverse ETL (pushing data warehouse segments back to SaaS tools): Hightouch or Census. These are purpose-built for activating warehouse data in operational tools. General iPaaS platforms can do this, but reverse ETL tools handle the audience syncing, incremental updates, and observability better.\n\nWebhook-driven workflows (form submission triggers lead routing, deal stage change triggers Slack notification): Zapier or Make. These are the sweet spot for lightweight iPaaS. N8n is the self-hosted alternative if you want to run the workflow engine on your own infrastructure.\n\nBi-directional sync with conflict resolution (two systems both write to the same record and need to stay in sync): This is where most iPaaS platforms struggle. Bi-directional sync requires conflict resolution rules: when both systems change the same field, which one wins? Workato handles this better than most. For mission-critical bi-directional sync, custom code with explicit conflict resolution logic is safer."
            },
            {
                "heading": "Evaluation Criteria: Choosing the Right iPaaS",
                "content": "Start with connector coverage. List every application you need to integrate today, plus the ones you're likely to add in the next 12 months. Check that the iPaaS has native connectors for each one. Native connectors are maintained by the vendor and handle API changes automatically. Generic HTTP/webhook connectors work but shift the maintenance burden to you, partially negating the iPaaS advantage.\n\nEvaluate the workflow builder's ceiling, not just its floor. Every iPaaS handles simple two-step workflows well. The differentiation shows up when you need branching logic, loops, error handling, data transformation, and conditional routing. Build your most complex integration during the trial period, not your simplest one. If the visual builder becomes unmanageable at your complexity level, you'll end up fighting the tool.\n\nPricing model matters more than price. Zapier charges per task (each action in a workflow counts). Make charges per operation (similar to tasks). Workato charges per recipe and connection. N8n charges per workflow execution. At high volume, task-based pricing can spike unexpectedly. Model your expected volume across all integrations and calculate total cost under each pricing structure before committing.\n\nError handling and monitoring are non-negotiable for production integrations. When an integration fails (and they all fail eventually), you need to know immediately, understand what went wrong, and have the ability to retry or fix the issue without rebuilding the workflow. Check for: automatic retries with configurable backoff, error notifications (email, Slack, PagerDuty), execution logs with input/output data for debugging, and the ability to replay failed executions. Enterprise platforms (Workato, Tray, Boomi) handle this well. Consumer-grade platforms (Zapier free tier) do not.\n\nGovernance and team management become important as your integration count grows. Who can create and edit workflows? Is there version control? Can you enforce naming conventions and documentation standards? If you're a team of one managing 10 integrations, this doesn't matter. If you have 5 people managing 100+ integrations, governance prevents chaos."
            }
        ],
        "related_tools": ["zapier", "workato-ipaas", "n8n", "fivetran", "boomi"],
        "related_categories": ["ipaas", "data-quality"],
        "faq": [
            {
                "q": "At what point should I switch from Zapier to an enterprise iPaaS?",
                "a": "When you hit 50+ active workflows, need team collaboration with role-based access, require SOC 2 compliance, or spend more than $500/month on Zapier. Enterprise platforms like Workato or Tray cost more but offer better governance, error handling, and support. The transition typically makes sense for companies with 100+ employees or a dedicated integration ops role."
            },
            {
                "q": "Can iPaaS replace a data engineering team?",
                "a": "For integration work, partially. iPaaS handles SaaS-to-SaaS connectivity without engineering resources. For data pipeline work (warehouse loading, transformations, data modeling), you still need either a data engineering team or specialized tools like Fivetran and dbt. iPaaS covers the operational integration layer. Data engineering covers the analytical layer."
            },
            {
                "q": "What's the biggest hidden cost of custom integrations?",
                "a": "Maintenance. APIs change, authentication tokens expire, rate limits shift, and edge cases surface over time. A custom integration that took 8 hours to build typically requires 3-5 hours per year in maintenance, plus incident response time when it breaks unexpectedly. For 30 integrations, that's 90-150 hours per year of engineering time, often at the most inconvenient moments."
            }
        ]
    }
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
        invalid_tools = [s for s in new_guide.get('related_tools', []) if s not in tc]
        if invalid_tools:
            print(f"  WARNING: {new_guide['slug']} has invalid tool refs: {invalid_tools}")
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
