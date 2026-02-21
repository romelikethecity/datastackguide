#!/usr/bin/env python3
"""
Add 6 new B2B tools to DataStackGuide:
- Tableau, Power BI, Looker (analytics category)
- Clari (list-building category)
- Braze (marketing-automation category)
- Gainsight (customer-success category)

Also creates 2 new categories: analytics, customer-success
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


# ── Tools.json entries ────────────────────────────────────────────────
TOOLS_JSON_ENTRIES = [
    {
        "name": "Tableau",
        "slug": "tableau",
        "description": "",
        "categories": ["analytics"],
        "primary_category": "analytics",
        "job_count": 412,
        "unique_companies": 208,
        "salary_min": 108000,
        "salary_max": 158000,
        "is_service": False,
        "db_category": "Analytics_BI"
    },
    {
        "name": "Power BI",
        "slug": "power-bi",
        "description": "",
        "categories": ["analytics"],
        "primary_category": "analytics",
        "job_count": 358,
        "unique_companies": 185,
        "salary_min": 95000,
        "salary_max": 145000,
        "is_service": False,
        "db_category": "Analytics_BI"
    },
    {
        "name": "Looker",
        "slug": "looker",
        "description": "",
        "categories": ["analytics"],
        "primary_category": "analytics",
        "job_count": 195,
        "unique_companies": 112,
        "salary_min": 115000,
        "salary_max": 168000,
        "is_service": False,
        "db_category": "Analytics_BI"
    },
    {
        "name": "Clari",
        "slug": "clari",
        "description": "",
        "categories": ["list-building"],
        "primary_category": "list-building",
        "job_count": 48,
        "unique_companies": 36,
        "salary_min": 105000,
        "salary_max": 162000,
        "is_service": False,
        "db_category": "Revenue_Intelligence"
    },
    {
        "name": "Braze",
        "slug": "braze",
        "description": "",
        "categories": ["marketing-automation"],
        "primary_category": "marketing-automation",
        "job_count": 52,
        "unique_companies": 41,
        "salary_min": 98000,
        "salary_max": 155000,
        "is_service": False,
        "db_category": "Marketing_Automation"
    },
    {
        "name": "Gainsight",
        "slug": "gainsight",
        "description": "",
        "categories": ["customer-success"],
        "primary_category": "customer-success",
        "job_count": 44,
        "unique_companies": 32,
        "salary_min": 88000,
        "salary_max": 148000,
        "is_service": False,
        "db_category": "Customer_Success"
    },
]


# ── Tool content entries ──────────────────────────────────────────────

TOOL_CONTENT = {
    "tableau": {
        "display_name": "Tableau",
        "tagline": "Visual analytics platform for business intelligence and data exploration",
        "description": "Tableau lets business users explore data through drag-and-drop visualizations. Connect to virtually any data source, build interactive dashboards, and share insights across the organization without writing SQL.",
        "description_2": "Founded in 2003 as a Stanford research spinoff, Tableau became the dominant visual analytics platform before Salesforce acquired it for $15.7 billion in 2019. It appears in 412 job postings in our dataset, with the heaviest demand in enterprise companies running complex data stacks.",
        "website": "https://www.tableau.com",
        "founded": 2003,
        "hq": "Seattle, WA",
        "pricing": {
            "model": "Per user/month",
            "tiers": [
                {"name": "Viewer", "price": "$15/user/mo", "notes": "View and interact with dashboards. No authoring."},
                {"name": "Explorer", "price": "$42/user/mo", "notes": "Edit existing workbooks, create from published data sources."},
                {"name": "Creator", "price": "$75/user/mo", "notes": "Full authoring, Tableau Prep, all data connections."}
            ],
            "notes": "Annual billing required. Tableau Cloud pricing shown. Server licenses are separate and typically more expensive. Minimum 1 Creator license per deployment. Data Management add-on ($5.50/user/mo) and Advanced Management ($4.25/user/mo) are common extras."
        },
        "pros": [
            "Best-in-class drag-and-drop visualization capabilities",
            "Connects to 100+ data sources natively",
            "Massive community with free learning resources and public dashboards",
            "Level-of-detail expressions handle complex calculations without code",
            "Salesforce integration is increasingly deep and bidirectional"
        ],
        "cons": [
            "Per-seat pricing adds up fast when scaling beyond analysts",
            "Steep learning curve for advanced features like LOD expressions and table calculations",
            "Desktop client is resource-heavy and Windows/Mac only",
            "Data prep capabilities (Tableau Prep) lag behind dedicated ETL tools",
            "Post-acquisition roadmap is increasingly tied to Salesforce ecosystem"
        ],
        "best_for": "Mid-market and enterprise teams with dedicated analysts who need flexible, visual data exploration across large datasets",
        "not_for": "Small teams without a data warehouse, or organizations that need lightweight embedded analytics at a low price point",
        "alternatives": ["power-bi", "looker", "salesforce"],
        "faq": [
            {"q": "Is Tableau free?", "a": "Tableau Public is free but your dashboards are public. Tableau Desktop has a 14-day trial. Paid plans start at $15/user/month for viewers on Tableau Cloud. Most teams need at least one Creator license at $75/user/month for authoring."},
            {"q": "What is the difference between Tableau Cloud and Tableau Server?", "a": "Tableau Cloud is fully managed SaaS. Tableau Server is self-hosted on your infrastructure. Cloud is simpler to operate but Server gives more control over data governance, security policies, and deployment. Server requires its own licensing model with per-core pricing."},
            {"q": "Can Tableau connect to Salesforce?", "a": "Yes, natively. Since Salesforce owns Tableau, the integration has gotten deeper. You can connect directly to Salesforce data, embed Tableau dashboards in Salesforce Lightning pages, and use CRM Analytics (formerly Einstein Analytics) alongside Tableau."},
            {"q": "How does Tableau compare to Power BI?", "a": "Tableau excels at visual exploration and handles complex analytical workflows better. Power BI costs a fraction of the price ($10/user/mo vs $75/user/mo for authoring) and integrates more tightly with Microsoft 365. Most teams choose based on their existing ecosystem: Microsoft shops go Power BI, Salesforce shops go Tableau."},
            {"q": "Is Tableau hard to learn?", "a": "Basic charts and dashboards take a few hours to learn. Intermediate features like calculated fields and parameters take a few weeks. Advanced concepts like LOD expressions, table calculations, and performance optimization take months. Tableau's free training resources and community forums make self-learning practical."}
        ],
        "overview": [
            "Tableau defined the modern BI category when it launched in 2003. The Stanford research project turned commercial product made visual data exploration accessible to business users who could not write SQL. Salesforce acquired the company for $15.7 billion in 2019, giving Tableau access to the largest CRM install base in the world. It appears in 412 job postings in our dataset, making it one of the most in-demand analytics skills in B2B.",
            "The platform works through a drag-and-drop interface that connects to databases, spreadsheets, cloud services, and APIs. Users build charts by dragging dimensions and measures onto visual shelves. Interactive filters, parameters, and actions link dashboards together into analytical applications. The visual query engine translates interface actions into optimized database queries without exposing users to SQL.",
            "Tableau deploys as Cloud (fully managed SaaS), Server (self-hosted), or Desktop (local authoring). Most new customers choose Cloud. The ecosystem includes Tableau Prep for data preparation, Tableau CRM for Salesforce-embedded analytics, and a public gallery with millions of community-created visualizations. An active developer community builds extensions, connectors, and custom integrations.",
            "Pricing is the persistent pain point. Viewer licenses ($15/user/month) seem reasonable until you calculate the cost of getting 200 people access to dashboards. Creator licenses at $75/user/month for the people who build content add up quickly. Competitors like Power BI undercut Tableau on price by 5-7x, which has shifted the competitive dynamic toward value justification rather than feature comparison."
        ],
        "key_features": [
            {"name": "Visual Analytics Engine", "description": "The core of Tableau is VizQL, a visual query language that translates drag-and-drop actions into database queries. Users build charts, maps, scatter plots, and complex multi-layered visualizations without writing code. The engine handles aggregation, filtering, and calculation at query time, pulling from live data connections or in-memory extracts."},
            {"name": "Level-of-Detail Expressions", "description": "LOD expressions let users compute aggregations at different granularities within the same view. A single chart can show customer-level revenue alongside region-level averages without creating separate data sources. These expressions solve calculation problems that would require subqueries or window functions in SQL."},
            {"name": "Dashboard Interactivity", "description": "Dashboards combine multiple views into interactive applications. Filter actions, highlight actions, and URL actions let users click on one chart to filter all others. Parameters create user-controlled inputs that change calculations dynamically. Stories sequence dashboards into guided analytical narratives."},
            {"name": "Data Source Connectivity", "description": "Tableau connects to over 100 data sources natively: databases (Postgres, MySQL, Snowflake, BigQuery, Redshift), files (CSV, Excel, JSON), cloud apps (Salesforce, Google Analytics, ServiceNow), and APIs. Live connections query the source in real time. Extracts pull snapshots into Tableau's in-memory engine for faster performance."},
            {"name": "Tableau Prep", "description": "A visual data preparation tool bundled with Creator licenses. Users clean, reshape, and combine data sources through a flow-based interface. Common operations include pivoting, aggregating, splitting fields, and joining tables. Output flows to Tableau Server or Cloud as published data sources that other users can build from."},
            {"name": "Embedded Analytics", "description": "Tableau embeds into web applications, portals, and third-party software through JavaScript API integration. Connected Apps handle authentication and single sign-on. Row-level security ensures each user sees only their authorized data. Pricing for embedded use cases follows a separate licensing model with usage-based options."}
        ],
        "use_cases": [
            {"title": "Executive and board reporting", "description": "Finance and strategy teams build KPI dashboards that pull from multiple systems: CRM pipeline data, financial actuals from the ERP, and marketing metrics from various platforms. Automated data refreshes keep dashboards current without manual report generation. Tableau Server schedules email subscriptions so executives get PDF snapshots without logging in. The visual format makes quarterly board presentations significantly faster to prepare."},
            {"title": "Sales performance analysis", "description": "Revenue operations teams use Tableau to analyze pipeline velocity, win rates by segment, and rep performance across territories. Connecting directly to Salesforce (or HubSpot, Dynamics) provides real-time visibility into deal progression. Managers identify bottlenecks by comparing average deal cycle times across stages, products, and rep cohorts. The analysis surfaces patterns that CRM built-in reporting misses."},
            {"title": "Self-service analytics for business teams", "description": "Data teams publish curated data sources to Tableau Server or Cloud, and business users build their own analyses without filing tickets. Marketing explores campaign performance, HR analyzes hiring funnels, and customer success tracks health scores. Governance features like certified data sources and usage analytics help IT maintain data quality without blocking self-service. This model reduces the backlog on analytics teams by 40-60% in typical deployments."}
        ],
        "pricing_detail": "Tableau Cloud pricing starts at $15/user/month for Viewers (dashboard consumers), $42 for Explorers (can edit existing content), and $75 for Creators (full authoring). Annual billing is required. Most mid-market deployments have 5-10 Creators, 20-30 Explorers, and 50-200 Viewers, landing in the $30,000-$80,000/year range.\n\nAdd-ons increase the cost: Data Management ($5.50/user/month) for data quality and cataloging, Advanced Management ($4.25/user/month) for enhanced security and deployment controls. These are per-user across all license types.\n\nTableau Server (self-hosted) uses core-based licensing starting around $35/core/year, plus the infrastructure costs of running your own servers. Most companies find Cloud cheaper when factoring in ops overhead.\n\nEnterprise agreements with Salesforce bundle Tableau alongside CRM and other products, often at significant discounts. Negotiate hard if you are already a Salesforce customer.",
        "verdict": "Tableau remains the most capable visual analytics platform on the market. The visualization engine handles complexity that competitors struggle with, and the community ecosystem is unmatched. If your analysts need to explore data flexibly and produce polished interactive dashboards, Tableau delivers.\n\nThe price is the main objection. Power BI does 80% of what Tableau does at 20% of the cost. Organizations standardized on Microsoft 365 will find Power BI's integration advantages hard to ignore. Looker competes on the governance and semantic layer front.\n\nTableau makes sense for teams that need visual depth, connect to diverse data sources, and can justify the per-seat investment. It appears alongside Salesforce, Power BI, and Looker in job postings, reflecting its position as a core enterprise analytics skill.",
        "data_quality": "",
        "categories": ["analytics"],
        "date_published": TODAY,
        "date_modified": TODAY,
        "meta_description": "Tableau review: pricing, features, and job demand data. Visual analytics platform with drag-and-drop dashboards, 100+ data connectors, and enterprise deployment options."
    },

    "power-bi": {
        "display_name": "Power BI",
        "tagline": "Microsoft's business intelligence platform for reporting and data visualization",
        "description": "Power BI turns raw data into interactive reports and dashboards within the Microsoft ecosystem. Pro licenses start at $10/user/month, making it the most affordable enterprise BI tool on the market.",
        "description_2": "Launched in 2015, Power BI grew from Microsoft's Excel add-ins (Power Pivot, Power Query) into a standalone platform. It appears in 358 job postings in our dataset. The tight integration with Azure, Microsoft 365, and Teams makes it the default choice for Microsoft-first organizations.",
        "website": "https://powerbi.microsoft.com",
        "founded": 2015,
        "hq": "Redmond, WA",
        "pricing": {
            "model": "Per user/month or capacity",
            "tiers": [
                {"name": "Power BI Pro", "price": "$10/user/mo", "notes": "Full authoring and sharing. Included in Microsoft 365 E5."},
                {"name": "Power BI Premium Per User", "price": "$20/user/mo", "notes": "Pro features plus larger datasets, paginated reports, AI capabilities."},
                {"name": "Power BI Premium Per Capacity", "price": "$4,995/mo", "notes": "Dedicated cloud compute. Unlimited viewers. Starts at P1 SKU."},
                {"name": "Power BI Embedded", "price": "Usage-based", "notes": "Embed analytics in your own applications. Azure consumption pricing."}
            ],
            "notes": "Pro is included with Microsoft 365 E5 subscriptions. Power BI Desktop (authoring tool) is free to download and use locally. Premium Per Capacity removes the per-user viewer cost, which makes it economical above ~250 users."
        },
        "pros": [
            "Pro at $10/user/month is 5-7x cheaper than Tableau Creator",
            "Deep integration with Excel, Azure, Teams, and SharePoint",
            "Power BI Desktop is free for local development",
            "DAX formula language is powerful once learned",
            "Largest and fastest-growing BI user base worldwide"
        ],
        "cons": [
            "DAX has a steep learning curve with limited debugging tools",
            "1 GB dataset size limit on Pro (10 GB on Premium Per User)",
            "Visual customization options are less flexible than Tableau",
            "Governance features require Premium licensing",
            "Performance degrades with complex data models on shared capacity"
        ],
        "best_for": "Microsoft-first organizations that need affordable BI across departments, especially teams already using Azure and Microsoft 365",
        "not_for": "Organizations with complex visual analytics needs, non-Microsoft data ecosystems, or teams that need code-first BI governance (Looker fits better)",
        "alternatives": ["tableau", "looker", "salesforce"],
        "faq": [
            {"q": "Is Power BI free?", "a": "Power BI Desktop is free to download and use locally for personal analysis. Sharing reports with others requires Power BI Pro ($10/user/month) or Premium. If your organization has Microsoft 365 E5, Pro is included at no extra cost."},
            {"q": "What is DAX?", "a": "DAX (Data Analysis Expressions) is Power BI's formula language for creating calculated columns, measures, and tables. It's similar to Excel formulas but designed for relational data models. Learning DAX is the main barrier to becoming proficient in Power BI."},
            {"q": "Power BI vs Excel: when to use which?", "a": "Use Excel for ad-hoc analysis, financial modeling, and situations where the analyst is also the consumer. Use Power BI when reports need to be shared across teams, refreshed automatically, or connected to live data sources. Many teams use both, with Power BI pulling from Excel data models."},
            {"q": "Can Power BI handle real-time data?", "a": "Yes, through DirectQuery (queries the source live), streaming datasets (push data via API), and Azure Stream Analytics integration. Real-time dashboards update automatically. However, DirectQuery performance depends on the source database, and complex DAX measures can be slow without Import mode."},
            {"q": "How does Power BI pricing compare to Tableau?", "a": "Power BI Pro costs $10/user/month vs Tableau Creator at $75/user/month. For 50 users, that is $6,000/year vs $45,000/year. Power BI Premium Per Capacity ($4,995/month) eliminates viewer costs, making it cheaper than Tableau at scale. Tableau has deeper visualization capabilities that justify the premium for some teams."}
        ],
        "overview": [
            "Power BI is the price disruptor that changed the BI market. At $10/user/month for Pro, it undercuts every enterprise competitor by a wide margin. Microsoft launched it in 2015 by packaging existing Excel technologies (Power Pivot, Power Query, Power View) into a standalone cloud service. It appears in 358 job postings in our dataset, second only to Tableau among BI tools.",
            "The platform consists of Power BI Desktop (free Windows application for authoring), Power BI Service (cloud platform for sharing and collaboration), and Power BI Mobile (iOS and Android apps). Reports built in Desktop are published to the Service, where they refresh on schedule and render in web browsers. The entire workflow feels native to anyone comfortable with Microsoft products.",
            "Data modeling in Power BI uses an in-memory columnar engine (VertipaqANALYZE) that compresses data for fast queries. DAX is the formula language for calculations. Power Query (M language) handles data ingestion and transformation. The combination is powerful but has a real learning curve. Most teams take 2-3 months before their analysts are comfortable building production-quality reports.",
            "The main limitation is Tableau-level visual sophistication. Power BI's built-in visuals cover standard charts well, and the AppSource marketplace adds custom visuals, but complex analytical layouts that Tableau handles natively require workarounds in Power BI. For organizations where the Microsoft ecosystem is already the default, this trade-off is worth the 5-7x cost savings."
        ],
        "key_features": [
            {"name": "DAX and Data Modeling", "description": "DAX (Data Analysis Expressions) is Power BI's formula language for creating measures, calculated columns, and tables. It operates on a tabular data model with relationships between tables. Time intelligence functions, iterator functions, and filter context manipulation give analysts SQL-level power through a formula interface. The learning curve is real, but DAX skills transfer across the Microsoft analytics stack."},
            {"name": "Power Query (ETL)", "description": "Power Query handles data ingestion, cleaning, and transformation through a visual interface with an M language backend. It connects to 150+ data sources: databases, APIs, files, and cloud services. Common transformations like pivot, unpivot, merge, and append work through point-and-click. Queries run on refresh, keeping reports current without manual intervention."},
            {"name": "DirectQuery and Live Connection", "description": "DirectQuery sends queries to the source database in real time instead of importing data into Power BI's engine. This is critical for large datasets that exceed import size limits (1 GB on Pro, 10 GB on Premium Per User). Live Connection to SQL Server Analysis Services and Azure Analysis Services provides the same real-time behavior with existing enterprise data models."},
            {"name": "Microsoft 365 Integration", "description": "Power BI embeds natively in Teams channels, SharePoint pages, and PowerPoint presentations. Excel users can connect to Power BI datasets and analyze them with pivot tables. Copilot in Power BI generates DAX measures and report pages from natural language prompts. This integration makes Power BI the path of least resistance for Microsoft-first organizations."},
            {"name": "Paginated Reports", "description": "Paginated reports (formerly SSRS) produce pixel-perfect, print-ready documents. Invoices, regulatory filings, and operational reports that need exact formatting use this feature. Available on Premium Per User and Premium Per Capacity licenses. The Report Builder authoring tool is separate from Power BI Desktop."},
            {"name": "Row-Level Security", "description": "RLS restricts data access based on user identity. A single report serves different audiences with each user seeing only their authorized data. Roles are defined in Power BI Desktop using DAX filters and assigned to users in the Power BI Service. Dynamic RLS uses the logged-in user's email or Active Directory group membership to determine access rules automatically."}
        ],
        "use_cases": [
            {"title": "Company-wide operational reporting", "description": "Finance, HR, sales, and operations teams all build and consume Power BI reports from a single tenant. The low per-user cost makes it feasible to give every manager and director a Pro license. Centralized datasets maintained by the data team feed standardized reports across departments. Teams pin dashboards to their Microsoft Teams channels for daily standups and review meetings."},
            {"title": "Excel power user migration", "description": "Organizations move critical Excel reports into Power BI to solve version control, data freshness, and distribution problems. Power Query replaces manual copy-paste data gathering. DAX replaces complex nested formulas. The published report refreshes automatically and serves a single source of truth instead of 15 spreadsheets emailed weekly. Most finance teams see this as the first high-value Power BI use case."},
            {"title": "Embedded analytics in applications", "description": "Software companies embed Power BI reports in their products using Power BI Embedded. Azure consumption-based pricing means cost scales with usage rather than named users. The JavaScript SDK controls the embedded experience: filtering, navigation, and event handling. This gives product teams analytics capabilities without building a visualization engine from scratch."}
        ],
        "pricing_detail": "Power BI Pro at $10/user/month is the entry point. It is included free with Microsoft 365 E5 subscriptions, so many enterprise teams already have access without a separate purchase. Pro includes full report authoring, sharing, and collaboration.\n\nPremium Per User at $20/user/month adds larger dataset sizes (up to 100 GB), paginated reports, AI features, and deployment pipelines. This tier fills the gap between Pro and full Premium.\n\nPremium Per Capacity starts at $4,995/month (P1 SKU) and provides dedicated compute resources. The key benefit: unlimited free viewers. If you have 500+ report consumers, Premium Per Capacity is cheaper than giving everyone a Pro license.\n\nPower BI Embedded uses Azure consumption pricing for embedding analytics in your own applications. Costs vary based on render volume and compute tier. Most SaaS companies start at $500-$1,500/month for embedded workloads.",
        "verdict": "Power BI is the most cost-effective enterprise BI tool available. At $10/user/month for Pro, it removes the budget objection that keeps analytics locked in spreadsheets. The Microsoft 365 integration makes adoption frictionless for organizations already in that ecosystem.\n\nThe trade-offs are real. DAX is harder to learn than it should be, and the visual flexibility gap versus Tableau matters for teams doing complex exploratory analysis. Dataset size limits on Pro can force upgrades to Premium earlier than expected.\n\nPower BI makes the most sense for Microsoft-first organizations that want BI across the whole company, not just the data team. It appears in 358 job postings in our dataset, reflecting its dominance in the enterprise reporting space.",
        "data_quality": "",
        "categories": ["analytics"],
        "date_published": TODAY,
        "date_modified": TODAY,
        "meta_description": "Power BI review: pricing from $10/user/month, features, and job demand data. Microsoft's BI platform with DAX, Power Query, and deep M365 integration."
    },

    "looker": {
        "display_name": "Looker",
        "tagline": "Google Cloud's code-first BI platform with a semantic modeling layer",
        "description": "Looker uses LookML, a modeling language, to define business logic in version-controlled code. The semantic layer ensures every team queries the same metric definitions, eliminating the 'whose numbers are right' problem.",
        "description_2": "Founded in 2012 and acquired by Google for $2.6 billion in 2020, Looker takes a developer-centric approach to BI. It appears in 195 job postings in our dataset. The platform is strongest in data-mature organizations where analytics engineering and governed metrics are priorities.",
        "website": "https://cloud.google.com/looker",
        "founded": 2012,
        "hq": "Santa Cruz, CA",
        "pricing": {
            "model": "Custom pricing",
            "tiers": [
                {"name": "Looker Core", "price": "Custom", "notes": "Full BI platform with LookML, Explores, and dashboards."},
                {"name": "Looker Modeler", "price": "Custom", "notes": "Semantic layer only, for use with Looker Studio or other BI tools."},
                {"name": "Looker Studio Pro", "price": "$9/user/mo", "notes": "Enhanced Looker Studio (formerly Data Studio) with governance features."}
            ],
            "notes": "Looker Core pricing is not published. Typical contracts start at $5,000/month for small deployments and scale to $25,000-$50,000/month for enterprise. Annual contracts required. Google Cloud consumption credits can sometimes apply."
        },
        "pros": [
            "LookML provides version-controlled, reusable metric definitions",
            "Git-based workflow fits engineering teams and modern data practices",
            "Strong embedded analytics with row-level security and theming",
            "Semantic layer ensures metric consistency across all consumers",
            "Native BigQuery integration with push-down query optimization"
        ],
        "cons": [
            "No published pricing, typical contracts start at $5,000+/month",
            "LookML requires developer skills, not accessible to business users",
            "Self-service exploration is less intuitive than Tableau or Power BI",
            "Post-Google acquisition roadmap has been confusing with Looker Studio overlap",
            "Smaller third-party connector ecosystem than Tableau"
        ],
        "best_for": "Data-mature organizations with analytics engineers who want governed, code-defined metrics and strong embedded analytics capabilities",
        "not_for": "Business-user-driven teams that need drag-and-drop exploration, or small companies that cannot justify $5,000+/month for BI",
        "alternatives": ["tableau", "power-bi", "salesforce"],
        "faq": [
            {"q": "What is LookML?", "a": "LookML is Looker's proprietary modeling language for defining data relationships, metrics, and business logic in code. Models are stored in Git repositories and reviewed through pull requests. This approach ensures every dashboard and Explore uses the same metric definitions, solving the consistency problems common in drag-and-drop BI tools."},
            {"q": "Looker vs Looker Studio: what is the difference?", "a": "Looker is a full enterprise BI platform with LookML modeling, Explores, and embedded analytics. Looker Studio (formerly Google Data Studio) is a free dashboarding tool for quick visualizations. They are separate products despite sharing the Looker name. Looker Studio Pro ($9/user/month) adds governance features but is still much simpler than full Looker."},
            {"q": "How much does Looker cost?", "a": "Google does not publish Looker pricing. Based on market data, small deployments start around $5,000/month and enterprise contracts run $25,000-$50,000/month. Pricing factors include user count, query volume, and support tier. The lack of transparent pricing is a common complaint."},
            {"q": "Can Looker work with non-Google Cloud databases?", "a": "Yes. Looker connects to Snowflake, Redshift, Postgres, MySQL, SQL Server, Databricks, and many other databases. However, performance and feature integration are strongest with BigQuery. Push-down query optimization and some newer features are BigQuery-first."},
            {"q": "Is Looker hard to set up?", "a": "Setting up Looker takes more time than Tableau or Power BI because the LookML model must be built before anyone can explore data. A typical implementation takes 4-8 weeks for the initial model. After that, adding new Explores and dashboards is fast. Organizations without analytics engineering resources often struggle with the initial setup."}
        ],
        "overview": [
            "Looker approaches BI differently than Tableau or Power BI. Instead of drag-and-drop visualizations, Looker starts with LookML: a modeling language that defines how data is structured, related, and calculated. These definitions live in Git repositories and go through code review. The result is a governed semantic layer where every dashboard, Explore, and API consumer uses the same metric definitions.",
            "Google acquired Looker for $2.6 billion in 2020, integrating it into Google Cloud Platform. The combination with BigQuery creates a strong analytics stack for GCP customers. Looker appears in 195 job postings in our dataset, with demand concentrated in data engineering and analytics engineering roles at tech companies and data-mature enterprises.",
            "The Explore interface lets business users ask questions of the modeled data through a point-and-click interface. Dimensions, measures, and filters are pre-defined in LookML, so users choose from validated options rather than writing ad-hoc calculations. This prevents the 'whose numbers are right' arguments that plague self-service BI tools. The trade-off is less flexibility for exploratory analysis compared to Tableau.",
            "Embedded analytics is a major Looker strength. The platform powers customer-facing dashboards, in-product analytics, and data-as-a-service offerings for SaaS companies. Row-level security, white-labeling, and the Looker API give development teams the building blocks to ship analytics features without building an analytics engine. This use case justifies Looker's premium pricing for many organizations."
        ],
        "key_features": [
            {"name": "LookML Modeling Language", "description": "LookML defines data models in code: table relationships, field definitions, aggregation logic, and derived tables. Models are version-controlled in Git and deployed through a CI/CD-like workflow. Changes go through pull requests, and the IDE validates SQL generation before deployment. This approach catches metric definition errors before they reach production dashboards."},
            {"name": "Explores", "description": "Explores are the primary self-service interface in Looker. Business users select dimensions, measures, and filters from a pre-defined list to build queries. The LookML model constrains the available fields and joins, ensuring queries are valid and consistent. Results display as tables, charts, or can be downloaded. Explores replace ad-hoc SQL for most analytical questions."},
            {"name": "Semantic Layer", "description": "Looker's semantic layer (now part of Google's universal semantic layer strategy) defines metrics once and makes them available across BI tools, notebooks, and applications. Metric definitions include the calculation logic, grain, and time dimensions. Tools like Looker Studio, Google Sheets, and third-party BI products can query the semantic layer directly."},
            {"name": "Embedded Analytics", "description": "Looker embeds dashboards and Explores in web applications through iframes and the JavaScript SDK. Signed URLs handle authentication without requiring Looker accounts for end users. Row-level security ensures multi-tenant data isolation. Theming APIs match the embedded content to the host application's design. Many SaaS companies use Looker to ship analytics features to their customers."},
            {"name": "Git Integration and Version Control", "description": "LookML projects are Git repositories. Developers work in branches, submit pull requests, and merge changes through standard Git workflows. The Looker IDE provides in-browser editing with SQL validation and content dependency checking. Deployment follows the branch: changes on a development branch only affect that developer's view until merged to production."},
            {"name": "Derived Tables and PDTs", "description": "Derived tables define SQL transformations that Looker materializes on schedule. Persistent Derived Tables (PDTs) are cached in the database and rebuilt at configured intervals. This approach handles data transformation within the BI layer, reducing the need for separate ETL pipelines for analytics-specific tables. PDTs work well for aggregation tables that speed up dashboard performance."}
        ],
        "use_cases": [
            {"title": "Governed enterprise analytics", "description": "Data teams define metrics in LookML and publish Explores for business users. Revenue is calculated one way, churn is defined consistently, and conversion rates use the same denominator everywhere. Finance, sales, and marketing all query the same semantic layer. This eliminates the monthly debate about why different dashboards show different numbers for the same metric."},
            {"title": "Customer-facing embedded analytics", "description": "SaaS companies embed Looker dashboards in their products to give customers data visibility. A project management tool shows team velocity charts. A marketing platform displays campaign performance. Row-level security ensures each customer sees only their data. The Looker API powers custom analytics experiences beyond standard dashboards. This embedded use case is Looker's strongest competitive differentiator."},
            {"title": "Data product development", "description": "Analytics engineering teams use Looker alongside dbt to build data products. dbt handles transformation in the warehouse, Looker handles the semantic layer and consumption. The LookML model exposes curated datasets through Explores, APIs, and actions. Teams treat the semantic layer as a product with versioning, documentation, and SLAs for data freshness and query performance."}
        ],
        "pricing_detail": "Looker does not publish pricing. Based on market data and customer reports, expect the following ranges:\n\nSmall deployments (10-25 users) typically start at $5,000-$8,000/month. Mid-market deployments (50-200 users) run $12,000-$25,000/month. Enterprise agreements with hundreds of users and embedded analytics can exceed $50,000/month.\n\nLooker Studio Pro is the affordable entry point at $9/user/month, but it is a different product. It adds governance features to the free Looker Studio (formerly Google Data Studio) but does not include LookML modeling or Explores.\n\nGoogle Cloud customers can sometimes apply committed spend credits toward Looker licenses. Negotiate this during contract discussions. The lack of published pricing makes vendor comparison difficult by design.",
        "verdict": "Looker is the right choice for organizations that treat analytics as an engineering discipline. The LookML modeling layer solves the metric consistency problem that plagues every BI tool with open-ended self-service. If your team has analytics engineers, uses dbt, and cares about governed metric definitions, Looker fits naturally into the workflow.\n\nThe barriers are cost and complexity. Starting at $5,000/month with unpublished pricing, Looker is the most expensive mainstream BI tool. The LookML learning curve means business users cannot self-serve without the analytics team first building the model. Organizations that want quick, flexible visual exploration are better served by Tableau or Power BI.\n\nLooker appears in 195 job postings in our dataset, often alongside BigQuery, Snowflake, and dbt. It is a specialized tool for data-mature organizations, not a general-purpose BI platform.",
        "data_quality": "",
        "categories": ["analytics"],
        "date_published": TODAY,
        "date_modified": TODAY,
        "meta_description": "Looker review: pricing, LookML features, and job demand data. Google Cloud's code-first BI platform with semantic modeling, embedded analytics, and Git workflows."
    },

    "clari": {
        "display_name": "Clari",
        "tagline": "Revenue operations platform for pipeline management and forecasting",
        "description": "Clari captures signals from email, calendar, and CRM to give revenue leaders an accurate view of pipeline health. AI-powered forecasting replaces spreadsheet-based commit calls with data-driven predictions.",
        "description_2": "Founded in 2012, Clari addresses the gap between CRM data (what reps enter) and reality (what's happening in deals). It appears in 48 job postings in our dataset, concentrated in VP Sales, Revenue Operations, and CRO roles at mid-market and enterprise SaaS companies.",
        "website": "https://www.clari.com",
        "founded": 2012,
        "hq": "Sunnyvale, CA",
        "pricing": {
            "model": "Custom pricing",
            "tiers": [
                {"name": "Clari Align", "price": "Custom", "notes": "Mutual action plans and buyer collaboration."},
                {"name": "Clari Forecast", "price": "Custom", "notes": "AI-powered revenue forecasting and pipeline analytics."},
                {"name": "Clari Copilot", "price": "Custom", "notes": "Conversation intelligence (formerly Wingman). Call recording and analysis."},
                {"name": "Clari Platform", "price": "Custom", "notes": "Full suite: forecast, inspect, align, and analytics."}
            ],
            "notes": "Pricing is not published. Based on market data, expect $50-$100/user/month for the core platform. Enterprise contracts with full suite access run higher. Annual contracts required. Implementation typically takes 4-8 weeks."
        },
        "pros": [
            "Activity capture removes dependency on reps logging CRM data",
            "Forecast accuracy improves measurably vs. spreadsheet-based methods",
            "Pipeline inspection surfaces risk signals that CRM views miss",
            "Mutual action plans (Align) improve buyer-seller collaboration",
            "Salesforce integration is deep and bidirectional"
        ],
        "cons": [
            "Enterprise pricing with no published rates makes budgeting difficult",
            "Value proposition is strongest for 50+ seat sales teams",
            "Requires clean CRM data to produce accurate baseline forecasts",
            "Conversation intelligence (Copilot) competes with dedicated tools like Gong",
            "Initial setup and calibration period takes 1-2 quarters before AI predictions are reliable"
        ],
        "best_for": "VP Sales, CROs, and RevOps leaders at SaaS companies with 50+ reps who need accurate forecasting and pipeline visibility beyond what Salesforce provides",
        "not_for": "Small sales teams under 20 reps, or organizations with simple sales cycles where CRM reporting is sufficient",
        "alternatives": ["gong-engage", "salesforce", "hubspot"],
        "faq": [
            {"q": "How does Clari improve forecast accuracy?", "a": "Clari analyzes activity signals (emails, meetings, CRM updates) alongside historical deal patterns to predict which deals will close. The AI model learns from your team's actual win/loss history rather than relying on rep-entered probabilities. Most teams report 15-25% improvement in forecast accuracy within 2-3 quarters."},
            {"q": "Does Clari replace Salesforce?", "a": "No. Clari sits on top of Salesforce (or HubSpot) and enriches CRM data with activity intelligence. It reads and writes to your CRM. Think of it as a revenue operations layer that makes CRM data more accurate and actionable. You still need your CRM as the system of record."},
            {"q": "How does Clari compare to Gong?", "a": "Gong focuses primarily on conversation intelligence: recording, transcribing, and analyzing sales calls. Clari focuses on pipeline management and forecasting. Clari added conversation intelligence (Copilot, formerly Wingman), and Gong has added forecasting features. The overlap is growing, but Clari is stronger on pipeline analytics and Gong is stronger on call coaching."},
            {"q": "How long does Clari implementation take?", "a": "Initial setup takes 4-8 weeks including CRM integration, user training, and historical data ingestion. The AI forecasting model needs 1-2 quarters of data before predictions become reliable. Most teams see clear ROI by the second quarter of use."},
            {"q": "What data does Clari capture?", "a": "Clari captures email metadata (sender, recipient, timestamps), calendar events, CRM field changes, and call data (if using Copilot). It does not read email body content by default. Activity data populates pipeline dashboards and feeds the forecasting AI without requiring reps to manually log activities in the CRM."}
        ],
        "overview": [
            "Clari exists because CRM data is unreliable. Reps forget to update deals, stage probabilities are guesses, and forecast calls devolve into opinion debates. Clari captures activity signals from email, calendar, and CRM to build an independent view of pipeline health. The AI analyzes patterns across thousands of deals to predict outcomes with more accuracy than human judgment alone.",
            "The platform started as a forecasting tool and expanded into a full revenue operations suite. Pipeline inspection shows deal-level risk signals. Mutual action plans (Align) give buyers and sellers a shared workspace. Conversation intelligence (Copilot, acquired from Wingman) records and analyzes sales calls. The expansion puts Clari in competition with Gong, but the core strength remains pipeline analytics.",
            "Clari appears in 48 job postings in our dataset, with demand concentrated in revenue operations and sales leadership roles. Companies listing Clari tend to be mid-market and enterprise SaaS businesses with 50+ person sales teams. The tool pairs most frequently with Salesforce, reflecting its position as a CRM enhancement layer.",
            "Implementation requires clean CRM data and a 1-2 quarter calibration period for the AI model. Organizations with messy Salesforce instances should fix data hygiene before deploying Clari. The forecasting accuracy improvement is measurable once the model has enough historical data, with most teams reporting 15-25% improvement over spreadsheet methods."
        ],
        "key_features": [
            {"name": "Revenue Forecasting", "description": "Clari's AI model predicts quarterly revenue by analyzing deal activity patterns, historical outcomes, and pipeline composition. The forecast updates continuously as new signals arrive. Forecasting dashboards show commit, best case, and pipeline categories with AI-adjusted amounts. Sales leaders compare their judgment-based forecast against the AI prediction to identify blind spots."},
            {"name": "Pipeline Inspection", "description": "Pipeline inspection surfaces deal-level risk signals that CRM views miss. Deals with declining engagement, slipping close dates, or missing stakeholders get flagged automatically. Managers drill into individual opportunities to see activity timelines, stakeholder maps, and next step compliance. The inspection view replaces the weekly pipeline review spreadsheet."},
            {"name": "Activity Capture", "description": "Clari captures email metadata and calendar events automatically, removing the dependency on reps logging activities in the CRM. The platform maps activities to contacts and opportunities, building an engagement timeline for every deal. This data feeds both pipeline inspection and forecasting without adding data entry burden to the sales team."},
            {"name": "Mutual Action Plans (Align)", "description": "Align creates shared workspaces between buyers and sellers with tasks, milestones, and document sharing. Both sides see what needs to happen to close the deal. Completion tracking gives managers visibility into deal progress beyond what CRM stages convey. The mutual action plan replaces email chains and shared Google Docs for deal coordination."},
            {"name": "Conversation Intelligence (Copilot)", "description": "Copilot records, transcribes, and analyzes sales calls and meetings. AI identifies key moments: objections, competitor mentions, pricing discussions, and next steps. Call summaries sync to the CRM automatically. Managers use Copilot for coaching sessions, reviewing how reps handle specific objections or discovery questions."},
            {"name": "Revenue Analytics", "description": "Pre-built and custom analytics dashboards track pipeline creation, conversion rates, deal velocity, and team performance. Trend analysis shows whether pipeline generation is keeping pace with targets. Segment-level views break down performance by region, product line, or rep cohort. The analytics layer provides the data foundation for revenue operations decision-making."}
        ],
        "use_cases": [
            {"title": "Quarterly forecasting", "description": "Revenue leaders use Clari to replace spreadsheet-based forecast calls. The AI prediction serves as a starting point, and managers adjust based on deal-level inspection. Forecast categories (commit, best case, pipeline) update in real time as deals progress. Finance and executive teams get a more reliable revenue outlook earlier in the quarter, reducing end-of-quarter surprises."},
            {"title": "Pipeline management and deal coaching", "description": "Front-line managers use pipeline inspection to identify at-risk deals during weekly one-on-ones. Activity gaps, stakeholder coverage issues, and timeline slippage surface automatically. Managers coach reps on specific deals rather than reviewing a CRM list. The conversation shifts from 'update your stages' to 'this deal shows declining engagement, what's your plan.'"},
            {"title": "Revenue operations reporting", "description": "RevOps teams use Clari analytics to track pipeline creation trends, win rate changes, and cycle time by segment. The data informs territory planning, quota setting, and capacity modeling. Because Clari captures activity data that reps do not log in the CRM, the analytics are more complete than native CRM reports. Board-level reporting on revenue predictability becomes data-driven rather than anecdotal."}
        ],
        "pricing_detail": "Clari does not publish pricing. Based on market reports and customer feedback, the core forecasting platform typically runs $50-$100/user/month for the sales team. Enterprise agreements with full suite access (Forecast, Inspect, Align, Copilot) run higher.\n\nImplementation costs vary. Clari provides onboarding and training, but complex CRM integrations or custom analytics requirements may involve additional professional services. Expect $10,000-$30,000 for implementation beyond the standard deployment.\n\nThe ROI case for Clari centers on forecast accuracy improvement and the sales time saved by automated activity capture. Teams with 50+ reps see the clearest return. Smaller teams can often get sufficient forecasting from CRM native reports and spreadsheets.",
        "verdict": "Clari solves a real problem: the gap between what reps enter in the CRM and what is happening in deals. The activity capture and AI forecasting combination produces measurably better pipeline visibility. Sales leaders who have used Clari consistently report they cannot go back to spreadsheet forecasting.\n\nThe cost and complexity are barriers for smaller teams. At $50-$100/user/month with unpublished pricing, Clari is a significant investment. The 1-2 quarter calibration period means ROI is not immediate. Teams under 50 reps may find the investment hard to justify.\n\nClari appears in 48 job postings in our dataset, often alongside Salesforce and Gong. It is a specialized tool for revenue-focused organizations that prioritize forecast accuracy and pipeline discipline. If you are running a 100+ person sales org and still forecasting in spreadsheets, Clari deserves serious evaluation.",
        "data_quality": "",
        "categories": ["list-building"],
        "date_published": TODAY,
        "date_modified": TODAY,
        "meta_description": "Clari review: pricing, forecasting features, and job demand data. Revenue operations platform with AI-powered pipeline inspection and activity capture."
    },

    "braze": {
        "display_name": "Braze",
        "tagline": "Customer engagement platform for cross-channel messaging and lifecycle marketing",
        "description": "Braze orchestrates messaging across email, push notifications, SMS, in-app messages, and web. The event-driven architecture processes user behavior in real time, triggering personalized campaigns within seconds of an action.",
        "description_2": "Founded in 2011 (originally as Appboy), Braze went public in 2021 and has become the standard for lifecycle marketing at high-growth consumer and B2B companies. It appears in 52 job postings in our dataset, primarily in marketing operations and lifecycle marketing roles.",
        "website": "https://www.braze.com",
        "founded": 2011,
        "hq": "New York, NY",
        "pricing": {
            "model": "Custom pricing",
            "tiers": [
                {"name": "Growth", "price": "Custom", "notes": "Core messaging channels, Canvas, basic segmentation. Typically starts at $50K/year."},
                {"name": "Pro", "price": "Custom", "notes": "Advanced analytics, predictive suite, Content Cards."},
                {"name": "Enterprise", "price": "Custom", "notes": "Full platform with custom integrations, dedicated support, SLAs."}
            ],
            "notes": "Pricing is based on monthly active users (MAUs), not seats. A company with 1M MAUs pays significantly more than one with 100K. Typical mid-market contracts start at $50,000-$80,000/year. Enterprise agreements run $150,000-$500,000+/year depending on MAU volume and channels used."
        },
        "pros": [
            "Real-time event processing enables sub-second campaign triggers",
            "Canvas visual journey builder is intuitive for complex multi-step flows",
            "Native support for push, email, SMS, in-app, Content Cards, and webhooks",
            "Currents data streaming exports engagement data to warehouses in real time",
            "Strong API-first architecture supports developer-led implementations"
        ],
        "cons": [
            "Expensive: $50K+/year minimum puts it out of reach for small teams",
            "Pricing based on MAUs can spike unpredictably with user growth",
            "Email template builder is less polished than dedicated ESP tools",
            "Reporting is adequate but not best-in-class for deep analytics",
            "Implementation requires engineering resources for proper event tracking setup"
        ],
        "best_for": "Growth and lifecycle marketing teams at companies with 100K+ monthly active users who need real-time, cross-channel messaging orchestration",
        "not_for": "Small businesses with simple email needs, or B2B companies with low user volumes where Marketo or HubSpot Marketing covers the use case",
        "alternatives": ["marketo", "salesforce-marketing-cloud", "hubspot"],
        "faq": [
            {"q": "How does Braze pricing work?", "a": "Braze charges based on monthly active users (MAUs), not seats or email volume. A user who opens your app or visits your website in a given month counts as an active user. This model means costs scale with your audience size. Companies with 100K MAUs might pay $50K-$80K/year, while those with millions of MAUs pay significantly more."},
            {"q": "Is Braze good for B2B companies?", "a": "Braze is primarily designed for consumer-facing and product-led companies. B2B companies with high user volumes (SaaS platforms, marketplaces) can use Braze effectively. Traditional B2B companies with low user counts and account-based sales cycles are better served by Marketo or HubSpot Marketing."},
            {"q": "What is Braze Canvas?", "a": "Canvas is Braze's visual journey builder for multi-step, cross-channel campaigns. Marketers create flows with branches, delays, A/B tests, and channel-specific messages. A welcome journey might send an email on day 1, a push notification on day 3, and an in-app message on day 7, with branches based on user engagement. Canvas handles the orchestration logic visually."},
            {"q": "How does Braze compare to Marketo?", "a": "Braze excels at real-time, event-driven messaging for consumer-facing products (push, in-app, SMS). Marketo excels at B2B demand generation workflows (lead scoring, nurture sequences, sales handoff). Braze processes events in real time. Marketo operates on batch-based campaign schedules. Some companies use both: Braze for product-led engagement and Marketo for demand generation."},
            {"q": "Does Braze support email marketing?", "a": "Yes. Braze handles email alongside push, SMS, in-app, Content Cards, and webhooks. The email builder supports drag-and-drop design, HTML templates, and dynamic content. For companies that only need email, a dedicated ESP like Mailchimp or Klaviyo is more cost-effective. Braze's value is cross-channel orchestration, not email alone."}
        ],
        "overview": [
            "Braze is the customer engagement platform that high-growth companies adopt when they outgrow basic ESPs. The event-driven architecture processes user behavior in real time, triggering personalized messages across email, push, SMS, in-app, and web within seconds. Founded in 2011 as Appboy and rebranded in 2017, Braze went public in 2021 and serves brands like Burger King, HBO Max, and Grubhub.",
            "The platform differentiates on real-time processing speed and cross-channel orchestration. While competitors like Marketo operate on batch campaign schedules (run every 15-60 minutes), Braze processes events as they happen. A user adding an item to their cart triggers a personalized push notification in under a second. This speed matters for use cases where timing drives conversion.",
            "Braze appears in 52 job postings in our dataset, concentrated in lifecycle marketing, growth marketing, and marketing operations roles. Companies listing Braze tend to be consumer-facing tech companies, marketplaces, and subscription businesses with large user bases. The MAU-based pricing model means Braze is most cost-effective for companies with high engagement rates.",
            "Implementation requires engineering support to set up event tracking through the Braze SDK. The marketing team defines the engagement strategy, but developers instrument the events that trigger campaigns. This API-first approach gives Braze flexibility that template-based tools lack, but it means marketing cannot operate independently of engineering during setup."
        ],
        "key_features": [
            {"name": "Canvas Journey Builder", "description": "Canvas is Braze's visual workflow editor for multi-step campaigns. Marketers build branching journeys with delays, A/B test splits, audience filters, and channel-specific messages. Action paths branch based on user behavior (opened email, clicked button, made purchase). Canvas supports nested journeys and can trigger other Canvases, enabling complex lifecycle programs."},
            {"name": "Real-Time Event Processing", "description": "Braze's streaming architecture ingests user events and triggers campaigns in real time. SDK events (app open, button click, purchase), API events (backend signals), and connected source events all process immediately. A user abandoning checkout can receive a push notification within seconds. This latency advantage is the core differentiator versus batch-based marketing automation platforms."},
            {"name": "Cross-Channel Messaging", "description": "Braze sends email, push notifications (iOS, Android, web), SMS, MMS, in-app messages, Content Cards, and webhooks from a single platform. Intelligent channel selection picks the best channel based on user preferences and engagement history. Frequency capping prevents message fatigue across all channels. Quiet hours respect time zones automatically."},
            {"name": "Currents Data Streaming", "description": "Currents exports engagement data (sends, opens, clicks, conversions) to data warehouses and analytics tools in real time. Supported destinations include Snowflake, BigQuery, Redshift, Mixpanel, and Amplitude. This streaming export enables marketing analytics teams to join campaign data with product and revenue data for attribution modeling."},
            {"name": "Predictive Suite", "description": "Braze's predictive features estimate likelihood to churn, likelihood to purchase, and likelihood to open/click for each user. Models train on your historical data and update automatically. Marketers use predictions as segmentation criteria: target users likely to churn with retention offers, or suppress users unlikely to convert from paid channels."},
            {"name": "Content Cards", "description": "Content Cards deliver persistent, personalized content within your app or website. Unlike push notifications or in-app messages that interrupt, Content Cards sit in a feed that users browse at their own pace. Common use cases include personalized offers, feature announcements, and onboarding checklists. Cards update dynamically and respect targeting and segmentation rules."}
        ],
        "use_cases": [
            {"title": "User onboarding and activation", "description": "Product and growth teams use Braze to guide new users through activation milestones. A multi-channel journey sends welcome emails, in-app tutorials, push reminders, and Content Cards based on which steps the user has completed. Users who stall at a specific step receive targeted nudges. The onboarding flow adapts in real time as users progress, rather than following a static email drip schedule."},
            {"title": "Re-engagement and retention", "description": "Lifecycle marketing teams build Braze campaigns to bring back lapsed users. Predictive churn scores identify at-risk users before they disengage. Canvas journeys combine incentive offers, feature highlights, and social proof across channels. Win-back campaigns escalate from push to email to SMS based on user responsiveness. The real-time processing means re-engagement triggers as soon as behavior patterns indicate risk."},
            {"title": "Transactional and triggered messaging", "description": "Engineering teams use Braze's API to send order confirmations, shipping updates, password resets, and payment reminders alongside marketing messages. Transactional sends use dedicated infrastructure for deliverability. Having transactional and marketing messages in one platform gives marketers visibility into the full customer communication timeline and prevents message collision between systems."}
        ],
        "pricing_detail": "Braze pricing is based on monthly active users (MAUs) and is not publicly listed. Based on market data, typical pricing ranges:\n\nGrowth tier for companies with 100K-500K MAUs: $50,000-$80,000/year. Pro tier for 500K-2M MAUs with advanced features: $100,000-$200,000/year. Enterprise tier for 2M+ MAUs with dedicated support: $200,000-$500,000+/year.\n\nChannel add-ons (SMS credits, additional push volume) increase costs beyond the base platform fee. Implementation services are often quoted separately at $15,000-$50,000 depending on complexity.\n\nThe MAU model means costs scale with audience growth. Companies with rapid user acquisition should model future costs carefully. Some negotiate MAU tier caps or graduated pricing to control costs as they scale.",
        "verdict": "Braze is the right choice for companies where real-time, cross-channel engagement drives business outcomes. The event-driven architecture, Canvas journey builder, and sub-second trigger processing create engagement experiences that batch-based tools cannot match. If your product has mobile users, high engagement frequency, and lifecycle marketing complexity, Braze handles it well.\n\nThe cost and implementation requirements limit the audience. At $50K+/year minimum and engineering-dependent setup, Braze is overkill for companies with simple email needs. B2B companies with small user bases and account-based sales motions are better served by Marketo or HubSpot Marketing.\n\nBraze appears in 52 job postings in our dataset, reflecting growing demand for lifecycle marketing skills. The platform pairs frequently with analytics tools, data warehouses, and mobile development frameworks in job requirements.",
        "data_quality": "",
        "categories": ["marketing-automation"],
        "date_published": TODAY,
        "date_modified": TODAY,
        "meta_description": "Braze review: MAU-based pricing, cross-channel features, and job demand data. Customer engagement platform for real-time push, email, SMS, and in-app messaging."
    },

    "gainsight": {
        "display_name": "Gainsight",
        "tagline": "Customer success platform for retention, expansion, and health scoring",
        "description": "Gainsight gives customer success teams a system of record for post-sale relationships. Health scores, lifecycle automation, and renewal management replace spreadsheet tracking with structured workflows.",
        "description_2": "Founded in 2009, Gainsight pioneered the customer success software category. It appears in 44 job postings in our dataset. The platform is strongest in B2B SaaS companies with CSM teams managing portfolio-based customer relationships.",
        "website": "https://www.gainsight.com",
        "founded": 2009,
        "hq": "San Francisco, CA",
        "pricing": {
            "model": "Custom pricing",
            "tiers": [
                {"name": "Essentials", "price": "Custom", "notes": "Health scores, timeline, Calls to Action. For smaller CS teams."},
                {"name": "Enterprise", "price": "Custom", "notes": "Journey Orchestrator, advanced analytics, Salesforce bi-directional sync."},
                {"name": "Enterprise+", "price": "Custom", "notes": "Full platform with PX, custom integrations, and dedicated CSM."}
            ],
            "notes": "Pricing is not published. Based on market data, Essentials starts around $2,500/month for small teams. Enterprise contracts typically run $5,000-$15,000/month depending on CSM count and feature tier. Annual contracts required. Gainsight PX (product analytics) is an additional product with separate pricing."
        },
        "pros": [
            "Health score framework is the most mature in the customer success category",
            "Journey Orchestrator automates lifecycle touchpoints at scale",
            "Salesforce integration is deep with bidirectional data sync",
            "Calls to Action system creates prioritized task lists for CSMs",
            "PX product adds product usage analytics alongside customer success"
        ],
        "cons": [
            "Expensive for small CS teams: $2,500+/month minimum",
            "Implementation is complex and typically takes 2-4 months",
            "Admin overhead is significant, often requires a dedicated Gainsight admin",
            "UI can feel dated compared to newer competitors like Vitally or Totango",
            "Heavy Salesforce dependency in many workflows"
        ],
        "best_for": "B2B SaaS companies with 10+ CSMs managing named accounts that need structured health scoring, lifecycle automation, and renewal tracking",
        "not_for": "Small customer success teams under 5 people, or high-volume/low-touch businesses where product-led customer success is more appropriate",
        "alternatives": ["salesforce", "hubspot"],
        "faq": [
            {"q": "What is a customer health score in Gainsight?", "a": "A health score combines multiple signals (product usage, support tickets, NPS responses, CSM sentiment, contract value) into a single color-coded indicator (green, yellow, red) for each account. Gainsight lets you define the scoring methodology with weighted factors. Health scores drive Calls to Action: red accounts trigger intervention workflows automatically."},
            {"q": "How does Gainsight integrate with Salesforce?", "a": "Gainsight syncs bidirectionally with Salesforce. Account data, opportunity stages, and contact information flow from Salesforce to Gainsight. Health scores, CSM activities, and renewal forecasts flow back. The integration uses the Salesforce API and can be configured for real-time or scheduled sync. Most Gainsight customers run Salesforce as their CRM."},
            {"q": "How long does Gainsight implementation take?", "a": "A typical Gainsight implementation takes 2-4 months. Phase 1 (4-6 weeks) covers data integration, health score setup, and basic Calls to Action. Phase 2 (4-8 weeks) adds Journey Orchestrator automations, advanced analytics, and team workflows. Most companies hire a Gainsight admin (internal or contracted) to manage ongoing configuration."},
            {"q": "Gainsight vs ChurnZero: how do they compare?", "a": "Gainsight is the market leader with the deepest feature set, designed for enterprise CS teams. ChurnZero is a strong mid-market alternative with faster implementation, lower cost, and a more modern UI. Companies with 5-15 CSMs often find ChurnZero sufficient. Companies with 20+ CSMs and complex segmentation needs typically choose Gainsight."},
            {"q": "What is Gainsight PX?", "a": "Gainsight PX is a product analytics and in-app engagement tool. It tracks product usage, feature adoption, and user journeys. PX is a separate product from Gainsight CS (customer success). Using both together lets CS teams combine account health data with actual product usage patterns. PX competes with Pendo and WalkMe in the digital adoption space."}
        ],
        "overview": [
            "Gainsight created the customer success software category in 2009 and remains the market leader. The platform gives CS teams a system of record for managing post-sale relationships at scale. Health scores aggregate product usage, support sentiment, and engagement signals into actionable account-level views. Calls to Action prioritize CSM workflows based on risk signals and lifecycle stage.",
            "The platform consists of Gainsight CS (customer success management), Gainsight PX (product analytics and in-app engagement), and Gainsight inSided (community). Most customers start with CS and add PX later. The combination of customer health data and product usage analytics gives CS leaders the complete picture that CRM alone cannot provide.",
            "Gainsight appears in 44 job postings in our dataset, primarily in customer success management and CS operations roles at B2B SaaS companies. The tool pairs with Salesforce in most deployments. Companies listing Gainsight typically have dedicated CS teams of 10-50 people managing named enterprise accounts.",
            "Implementation is the main barrier. A typical Gainsight deployment takes 2-4 months and requires dedicated admin resources ongoing. The platform is powerful but complex, and underinvestment in configuration leads to poor adoption. Companies that succeed with Gainsight treat it as a strategic CS platform investment, not a lightweight tool purchase."
        ],
        "key_features": [
            {"name": "Health Scores", "description": "Gainsight's health scoring framework combines multiple data sources into a single account health indicator. Administrators define scoring categories (usage, support, engagement, sentiment) with weighted factors and thresholds. Scores update automatically as new data arrives. The framework supports multiple scorecard types for different customer segments. CSMs see health trends over time, not just current state."},
            {"name": "Calls to Action (CTAs)", "description": "CTAs are prioritized tasks generated by rules, health score changes, or manual creation. A customer's health dropping to red triggers an at-risk CTA assigned to the CSM. A renewal approaching in 90 days creates a renewal CTA. CTAs include playbooks with recommended next steps. Managers track CTA resolution rates and response times across the team."},
            {"name": "Journey Orchestrator", "description": "Journey Orchestrator automates lifecycle communications at scale. Onboarding sequences, QBR scheduling, renewal reminders, and NPS surveys run automatically based on customer segment and lifecycle stage. The automation handles the high-volume touchpoints so CSMs can focus on strategic accounts. Programs trigger from Gainsight data, CRM events, or external signals."},
            {"name": "Timeline", "description": "Timeline captures the complete history of CSM-customer interactions in a single view. Activities sync from email, calendar, CRM, and manual entries. Each timeline entry can be tagged with activity type, sentiment, and attendees. Managers review timelines during account handoffs and escalations. The timeline serves as the CS team's institutional memory for every account relationship."},
            {"name": "Renewal and Expansion Management", "description": "Renewal Center tracks upcoming renewals with forecast amounts, risk indicators, and owner assignments. Early warning signals (declining usage, open support escalations, negative NPS) flag renewals at risk months before the expiration date. Expansion opportunities surface when product usage patterns indicate readiness for upsell. Revenue forecasting for the CS function mirrors what CRM provides for new business."},
            {"name": "Gainsight PX (Product Analytics)", "description": "PX tracks product usage at the feature level across users and accounts. Adoption dashboards show which features customers use, how often, and how deeply. In-app engagement tools (guides, tooltips, surveys) drive feature discovery. PX data feeds into health scores, giving CS teams usage-based signals alongside relationship-based ones. The combination closes the gap between what CSMs hear and what customers do."}
        ],
        "use_cases": [
            {"title": "At-risk account management", "description": "CS operations teams configure health score rules that flag accounts showing churn signals: declining login frequency, increasing support ticket volume, negative survey responses, or stakeholder departures. When health drops to yellow or red, Gainsight creates CTAs with intervention playbooks. CSMs follow structured workflows to diagnose the issue, schedule executive check-ins, and document recovery plans. The systematic approach catches at-risk accounts months before renewal."},
            {"title": "Scaled onboarding automation", "description": "Companies with high customer volume use Journey Orchestrator to automate onboarding touchpoints. Welcome emails, training invitations, milestone check-ins, and adoption nudges send automatically based on time-since-purchase and product usage milestones. CSMs only intervene when customers fall behind the expected onboarding trajectory. This model lets a single CSM support 50-100 accounts during onboarding versus 15-20 with manual processes."},
            {"title": "QBR and executive reporting", "description": "CS leaders use Gainsight dashboards for quarterly business reviews with customers and internal executive reporting. Customer-facing QBR slides auto-populate with usage data, health trends, and support history. Internal reports show portfolio health, NRR trends, and CSM capacity utilization. The data-driven approach replaces anecdotal CS reporting with metrics that finance and executive teams can act on."}
        ],
        "pricing_detail": "Gainsight does not publish pricing. Based on market data and customer reports:\n\nEssentials tier for small CS teams (5-10 CSMs) starts around $2,500-$4,000/month. Enterprise tier with Journey Orchestrator and advanced analytics runs $5,000-$15,000/month depending on team size and data volume. Enterprise+ with PX, custom integrations, and premium support can exceed $20,000/month.\n\nImplementation services are typically quoted at $15,000-$50,000 depending on complexity. Many companies hire Gainsight-certified consultants for the initial build. Ongoing admin costs (internal headcount or contractor) should be factored into total cost of ownership.\n\nGainsight PX is priced separately based on monthly tracked users (MTUs). Bundling CS and PX together typically earns a 15-25% discount versus purchasing separately.",
        "verdict": "Gainsight is the enterprise standard for customer success management. The health scoring framework, Calls to Action system, and Journey Orchestrator create a structured approach to post-sale customer management that spreadsheets and CRM tasks cannot replicate. If you have 10+ CSMs and take customer retention seriously, Gainsight delivers.\n\nThe investment is substantial. Between licensing ($30,000-$180,000/year), implementation, and ongoing admin, Gainsight is a platform-level commitment. Smaller teams should evaluate ChurnZero or Vitally, which offer simpler implementations at lower price points. Gainsight's depth becomes a liability if you do not have the resources to configure and maintain it.\n\nGainsight appears in 44 job postings in our dataset, reflecting steady demand for structured customer success operations. It pairs most frequently with Salesforce, confirming its position as the CS system of record in Salesforce-centric organizations.",
        "data_quality": "",
        "categories": ["customer-success"],
        "date_published": TODAY,
        "date_modified": TODAY,
        "meta_description": "Gainsight review: pricing, health scoring features, and job demand data. Enterprise customer success platform for retention, expansion, and lifecycle automation."
    },
}


# ── Pricing page entries ──────────────────────────────────────────────

PRICING_PAGES = [
    {
        "slug": "tableau-pricing",
        "tool_slug": "tableau",
        "title": "Tableau Pricing (2026): What It Actually Costs",
        "meta_description": "Tableau pricing breakdown: Viewer, Explorer, and Creator tiers. Real costs for Cloud, Server, and enterprise deployments. Updated for 2026.",
        "hook": "Tableau lists $15-$75/user/month on their pricing page. The real cost depends on your mix of Creators, Explorers, and Viewers, plus add-ons that most teams eventually need.",
        "tiers": [
            {"name": "Viewer", "price": "$15/user/mo", "billing": "Annual", "highlights": ["View and interact with published dashboards", "Filter, drill, and export data", "Subscribe to dashboard email alerts", "Mobile app access"]},
            {"name": "Explorer", "price": "$42/user/mo", "billing": "Annual", "highlights": ["Edit existing workbooks", "Create from published data sources", "Web authoring capabilities", "All Viewer features"]},
            {"name": "Creator", "price": "$75/user/mo", "billing": "Annual", "popular": True, "highlights": ["Full Tableau Desktop authoring", "Tableau Prep for data preparation", "Connect to any data source", "Publish to Server/Cloud", "All Explorer features"]},
            {"name": "Data Management Add-on", "price": "$5.50/user/mo", "billing": "Annual", "highlights": ["Catalog (data discovery)", "Data quality warnings", "Lineage tracking", "Virtual connections"]},
        ],
        "faq": [
            {"q": "Is Tableau included with Salesforce?", "a": "Not automatically. Tableau is a separate purchase from Salesforce CRM. However, enterprise agreements often bundle both products at a discount. CRM Analytics (formerly Einstein Analytics) is the Salesforce-native analytics tool and is included in some CRM tiers."},
            {"q": "How much does a typical Tableau deployment cost?", "a": "A mid-market deployment with 5 Creators, 20 Explorers, and 100 Viewers on Tableau Cloud costs approximately $3,615/month or $43,380/year before add-ons. Enterprise deployments with Data Management and Advanced Management add-ons run 30-50% higher."},
            {"q": "Can I use Tableau for free?", "a": "Tableau Public is free but all your dashboards are publicly visible. Tableau Desktop offers a 14-day free trial. There is no free tier for private, commercial use."}
        ]
    },
    {
        "slug": "power-bi-pricing",
        "tool_slug": "power-bi",
        "title": "Power BI Pricing (2026): What It Actually Costs",
        "meta_description": "Power BI pricing breakdown: Pro at $10/user/mo, Premium Per User, and Premium Capacity options. Real costs for Microsoft BI. Updated for 2026.",
        "hook": "Power BI Pro at $10/user/month is the most affordable enterprise BI license on the market. But Premium features, capacity pricing, and Azure consumption costs can push the real number higher.",
        "tiers": [
            {"name": "Power BI Pro", "price": "$10/user/mo", "billing": "Monthly or Annual", "popular": True, "highlights": ["Full report authoring and sharing", "1 GB max dataset size", "8 daily data refreshes", "Included in Microsoft 365 E5"]},
            {"name": "Premium Per User (PPU)", "price": "$20/user/mo", "billing": "Monthly or Annual", "highlights": ["100 GB max dataset size", "48 daily data refreshes", "Paginated reports", "AI features and dataflows", "Deployment pipelines"]},
            {"name": "Premium Per Capacity (P1)", "price": "$4,995/mo", "billing": "Annual", "highlights": ["Dedicated cloud compute resources", "Unlimited free viewers", "Larger dataset sizes", "XMLA endpoint access", "Autoscale option"]},
            {"name": "Power BI Embedded", "price": "Usage-based", "billing": "Azure consumption", "highlights": ["Embed in custom applications", "Azure capacity pricing", "No named user licenses needed", "White-label capabilities"]},
        ],
        "faq": [
            {"q": "Is Power BI free with Microsoft 365?", "a": "Power BI Pro is included with Microsoft 365 E5 subscriptions at no additional cost. Other M365 plans do not include Power BI. Power BI Desktop (the authoring application) is a free download for anyone."},
            {"q": "When should I upgrade to Premium?", "a": "Consider Premium Per User ($20/user/month) when you need datasets larger than 1 GB, paginated reports, or AI features. Consider Premium Per Capacity ($4,995/month) when you have 250+ report viewers, since it eliminates per-user viewer costs."},
            {"q": "How does Power BI pricing compare to Tableau?", "a": "Power BI Pro ($10/user/month) is 7.5x cheaper than Tableau Creator ($75/user/month). Even Premium Per User ($20/month) is less than half of Tableau Explorer ($42/month). The cost advantage narrows at enterprise scale with Premium Capacity, but Power BI remains significantly cheaper in most deployments."}
        ]
    },
    {
        "slug": "looker-pricing",
        "tool_slug": "looker",
        "title": "Looker Pricing (2026): What It Actually Costs",
        "meta_description": "Looker pricing breakdown: custom enterprise pricing, typical contract ranges, and Looker Studio Pro alternative. Updated for 2026.",
        "hook": "Looker does not publish pricing. Based on market data, expect $5,000-$50,000+/month depending on user count and deployment complexity. Google Cloud credits can sometimes apply.",
        "tiers": [
            {"name": "Looker Core", "price": "Custom", "billing": "Annual", "popular": True, "highlights": ["Full LookML modeling", "Explores and dashboards", "Embedded analytics", "API access", "Git integration"]},
            {"name": "Looker Modeler", "price": "Custom", "billing": "Annual", "highlights": ["Semantic layer only", "Use with Looker Studio or other BI tools", "Metric definitions without full Looker"]},
            {"name": "Looker Studio Pro", "price": "$9/user/mo", "billing": "Monthly", "highlights": ["Enhanced Looker Studio (formerly Data Studio)", "Team content management", "Admin controls and governance", "Not full Looker platform"]},
        ],
        "faq": [
            {"q": "Why does Looker not publish pricing?", "a": "Like most enterprise software, Looker uses custom pricing based on deployment size, user count, and support requirements. This allows Google Cloud to bundle Looker with other GCP services and negotiate enterprise agreements. It also makes direct price comparison with Tableau and Power BI more difficult."},
            {"q": "What is a typical Looker contract?", "a": "Small deployments (10-25 users) typically start at $5,000-$8,000/month. Mid-market (50-200 users) runs $12,000-$25,000/month. Enterprise with embedded analytics can exceed $50,000/month. Annual contracts are standard. Google Cloud committed spend may apply."},
            {"q": "Is Looker Studio the same as Looker?", "a": "No. Looker Studio (formerly Google Data Studio) is a free dashboarding tool. Looker is a full enterprise BI platform with LookML modeling. Looker Studio Pro ($9/user/month) adds governance features to the free tool but is still a different product from Looker Core."}
        ]
    },
    {
        "slug": "clari-pricing",
        "tool_slug": "clari",
        "title": "Clari Pricing (2026): What It Actually Costs",
        "meta_description": "Clari pricing breakdown: custom enterprise pricing for forecasting, pipeline inspection, and conversation intelligence. Updated for 2026.",
        "hook": "Clari does not publish pricing. Based on market data, the core platform runs $50-$100/user/month for sales teams. The ROI case centers on forecast accuracy improvement and activity capture.",
        "tiers": [
            {"name": "Clari Forecast", "price": "Custom", "billing": "Annual", "popular": True, "highlights": ["AI-powered revenue forecasting", "Pipeline analytics", "Historical trending", "Salesforce integration"]},
            {"name": "Clari Inspect", "price": "Custom", "billing": "Annual", "highlights": ["Deal-level risk signals", "Activity timelines", "Stakeholder mapping", "Next step tracking"]},
            {"name": "Clari Align", "price": "Custom", "billing": "Annual", "highlights": ["Mutual action plans", "Buyer collaboration workspace", "Milestone tracking", "Document sharing"]},
            {"name": "Clari Copilot", "price": "Custom", "billing": "Annual", "highlights": ["Call recording and transcription", "AI conversation analysis", "CRM activity sync", "Coaching insights"]},
        ],
        "faq": [
            {"q": "How much does Clari cost per user?", "a": "Based on market reports, Clari's core forecasting platform runs $50-$100/user/month. The full suite (Forecast, Inspect, Align, Copilot) costs more. Enterprise agreements are negotiated individually. Implementation costs typically add $10,000-$30,000."},
            {"q": "Does Clari charge for all CRM users?", "a": "Clari typically licenses to sales team members who need forecasting and pipeline visibility: reps, managers, and revenue operations. Executive viewers may have lighter-weight access. The exact licensing model depends on your contract."},
            {"q": "What is the ROI of Clari?", "a": "Clari's ROI case is forecast accuracy improvement (15-25% better than spreadsheets) and time savings from automated activity capture. A VP Sales spending 10 hours/week on manual forecasting can reclaim most of that time. The math works best for teams with 50+ reps."}
        ]
    },
    {
        "slug": "braze-pricing",
        "tool_slug": "braze",
        "title": "Braze Pricing (2026): What It Actually Costs",
        "meta_description": "Braze pricing breakdown: MAU-based pricing model, typical contract ranges by company size. Updated for 2026.",
        "hook": "Braze charges by monthly active users (MAUs), not seats or email volume. This model scales with your audience. Companies with 100K MAUs might pay $50K-$80K/year, while those with millions pay significantly more.",
        "tiers": [
            {"name": "Growth", "price": "~$50K/year", "billing": "Annual", "highlights": ["Core messaging channels (email, push, SMS)", "Canvas journey builder", "Basic segmentation", "Standard support"]},
            {"name": "Pro", "price": "Custom", "billing": "Annual", "popular": True, "highlights": ["Advanced analytics and reporting", "Predictive suite (churn, purchase likelihood)", "Content Cards", "Currents data streaming"]},
            {"name": "Enterprise", "price": "Custom", "billing": "Annual", "highlights": ["Custom integrations", "Dedicated customer success manager", "SLA guarantees", "Advanced security and compliance"]},
        ],
        "faq": [
            {"q": "How does Braze MAU pricing work?", "a": "A monthly active user (MAU) is anyone who opens your app or visits your website in a given month. You pay based on your peak MAU count. If you have 500K users but only 200K are active monthly, you pay for 200K. MAU tiers are negotiated at contract signing."},
            {"q": "Is Braze more expensive than Marketo?", "a": "It depends on your use case. Braze is priced on MAUs while Marketo is priced on database size (contacts). For companies with large, active user bases, Braze can be more expensive. For B2B companies with smaller contact databases, Marketo is typically comparable or higher per contact."},
            {"q": "What channels does Braze pricing include?", "a": "Email and push notifications are included in the base platform price. SMS and MMS have per-message costs on top of the platform fee. WhatsApp and other messaging channels have separate pricing. The total cost depends on your channel mix and message volume."}
        ]
    },
    {
        "slug": "gainsight-pricing",
        "tool_slug": "gainsight",
        "title": "Gainsight Pricing (2026): What It Actually Costs",
        "meta_description": "Gainsight pricing breakdown: custom pricing for CS teams, typical contract ranges, and PX add-on costs. Updated for 2026.",
        "hook": "Gainsight does not publish pricing. Based on market data, the platform starts around $2,500/month for small CS teams and scales to $15,000+/month for enterprise deployments. Implementation and admin costs add significantly to the total.",
        "tiers": [
            {"name": "Essentials", "price": "~$2,500/mo", "billing": "Annual", "highlights": ["Health scores", "Timeline", "Calls to Action", "Basic reporting", "Salesforce sync"]},
            {"name": "Enterprise", "price": "Custom", "billing": "Annual", "popular": True, "highlights": ["Journey Orchestrator", "Advanced analytics", "Bi-directional Salesforce sync", "Renewal Center", "Surveys"]},
            {"name": "Enterprise+", "price": "Custom", "billing": "Annual", "highlights": ["Gainsight PX included", "Custom integrations", "Dedicated CSM", "Premium support SLA"]},
        ],
        "faq": [
            {"q": "How much does Gainsight cost for a small CS team?", "a": "Gainsight Essentials starts around $2,500/month based on market data. A team of 5-10 CSMs typically pays $2,500-$4,000/month. This does not include implementation services, which run $15,000-$30,000 for a standard deployment."},
            {"q": "Is Gainsight PX included?", "a": "Gainsight PX (product analytics) is a separate product with its own pricing based on monthly tracked users (MTUs). It can be bundled with Gainsight CS at a 15-25% discount. Many companies start with CS only and add PX after proving initial value."},
            {"q": "What are the hidden costs of Gainsight?", "a": "Beyond licensing, plan for: implementation services ($15K-$50K), a dedicated Gainsight admin (internal hire or contractor), and ongoing configuration as your CS processes evolve. Total first-year cost is typically 2-3x the annual license fee."}
        ]
    },
]


# ── New category entries ──────────────────────────────────────────────

NEW_CATEGORIES = [
    {
        "name": "Analytics & BI",
        "slug": "analytics",
        "description": "Visualize data, build dashboards, and deliver business intelligence across the organization.",
        "meta_description": "Compare analytics and BI tools: pricing, features, and job demand data. See which business intelligence platforms teams rely on in 2026.",
        "color": "#8B5CF6",
        "icon": "📊",
        "tool_count": 3,
        "tools": [
            {"name": "Tableau", "slug": "tableau", "job_count": 412, "description": "Visual analytics platform for business intelligence and data exploration.", "is_service": False},
            {"name": "Power BI", "slug": "power-bi", "job_count": 358, "description": "Microsoft's business intelligence platform for reporting and data visualization.", "is_service": False},
            {"name": "Looker", "slug": "looker", "job_count": 195, "description": "Google Cloud's code-first BI platform with a semantic modeling layer.", "is_service": False},
        ],
        "faq": [
            {"q": "What is business intelligence (BI)?", "a": "Business intelligence is the process of turning raw data into actionable insights through visualization, reporting, and analysis. BI tools connect to databases and data warehouses, let users build interactive dashboards, and distribute insights across the organization. Modern BI platforms range from drag-and-drop tools (Tableau, Power BI) to code-first platforms (Looker)."},
            {"q": "Which BI tool is cheapest?", "a": "Power BI Pro at $10/user/month is the most affordable enterprise BI tool. Power BI Desktop is free for local use. Looker Studio (formerly Data Studio) is free for basic dashboards. Tableau's cheapest option is $15/user/month for Viewer access, with Creator licenses at $75/user/month."},
            {"q": "Do I need a data warehouse for BI tools?", "a": "Not necessarily. BI tools can connect directly to databases, spreadsheets, and cloud applications. However, a data warehouse (Snowflake, BigQuery, Redshift) provides better performance, data consolidation, and governance for serious analytics deployments. Most companies adopt a warehouse as their BI usage matures."},
            {"q": "Tableau vs Power BI: which should I choose?", "a": "Choose Power BI if your organization runs Microsoft 365 and wants affordable company-wide BI. Choose Tableau if you need deeper visual analytics and more flexible data exploration. Power BI costs 5-7x less per user. Tableau handles complex analytical workflows better. Most teams choose based on their existing technology ecosystem."},
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },
    {
        "name": "Customer Success",
        "slug": "customer-success",
        "description": "Manage post-sale customer relationships, track health scores, and drive retention and expansion.",
        "meta_description": "Compare customer success platforms: pricing, features, and job demand data. See which CS tools teams rely on for retention in 2026.",
        "color": "#10B981",
        "icon": "🤝",
        "tool_count": 1,
        "tools": [
            {"name": "Gainsight", "slug": "gainsight", "job_count": 44, "description": "Customer success platform for retention, expansion, and health scoring.", "is_service": False},
        ],
        "faq": [
            {"q": "What is customer success software?", "a": "Customer success software helps post-sale teams manage customer relationships systematically. Core features include health scores (risk indicators), lifecycle automation (onboarding, renewal reminders), and activity tracking. These tools replace spreadsheet-based customer tracking with structured workflows and data-driven prioritization."},
            {"q": "When does a company need customer success software?", "a": "Most B2B SaaS companies adopt CS software when they reach 5-10 CSMs managing named accounts. Below that threshold, CRM tasks and spreadsheets usually suffice. The tipping point is when manual tracking starts missing renewal risks or expansion opportunities due to scale."},
            {"q": "How does customer success software differ from CRM?", "a": "CRMs manage the sales pipeline (pre-sale). Customer success platforms manage the post-sale relationship: onboarding, adoption, health monitoring, renewal, and expansion. Some CRMs (Salesforce, HubSpot) have CS features, but dedicated CS platforms like Gainsight offer deeper health scoring, lifecycle automation, and CS-specific analytics."},
            {"q": "What is a customer health score?", "a": "A health score is a composite metric that indicates the likelihood of a customer renewing or expanding. It combines signals like product usage frequency, support ticket volume, NPS survey responses, executive engagement, and contract value. Green, yellow, and red scores help CSMs prioritize their attention across a large portfolio."},
        ],
        "date_published": TODAY,
        "date_modified": TODAY,
    },
]


# ── Category updates (add tools to existing categories) ───────────────

CATEGORY_TOOL_ADDITIONS = {
    "list-building": [
        {"name": "Clari", "slug": "clari", "job_count": 48, "description": "Revenue operations platform for pipeline management and forecasting.", "is_service": False},
    ],
    "marketing-automation": [
        {"name": "Braze", "slug": "braze", "job_count": 52, "description": "Customer engagement platform for cross-channel messaging and lifecycle marketing.", "is_service": False},
    ],
}


def main():
    dry_run = '--dry-run' in sys.argv

    # Load existing data
    tools = load("tools.json")
    tc = load("tool_content.json")
    pricing = load("pricing_pages.json")
    cats = load("categories.json")

    existing_slugs = {t['slug'] for t in tools['tools']}

    # Add tools to tools.json
    added_tools = 0
    for entry in TOOLS_JSON_ENTRIES:
        if entry['slug'] in existing_slugs:
            print(f"  SKIP {entry['slug']} (already exists)")
            continue
        tools['tools'].append(entry)
        tools['tool_count'] = len(tools['tools'])
        print(f"  + tools.json: {entry['slug']} (job_count={entry['job_count']})")
        added_tools += 1

    # Add tool content
    added_content = 0
    for slug, content in TOOL_CONTENT.items():
        if slug in tc:
            print(f"  SKIP tool_content: {slug} (already exists)")
            continue
        tc[slug] = content
        print(f"  + tool_content: {slug} ({len(content.get('overview', []))} overview paras, {len(content.get('key_features', []))} features)")
        added_content += 1

    # Add pricing pages
    added_pricing = 0
    existing_pricing_slugs = {p['slug'] for p in pricing['pages']}
    for page in PRICING_PAGES:
        if page['slug'] in existing_pricing_slugs:
            print(f"  SKIP pricing: {page['slug']} (already exists)")
            continue
        pricing['pages'].append(page)
        print(f"  + pricing: {page['slug']} ({len(page['tiers'])} tiers)")
        added_pricing += 1

    # Add new categories
    added_cats = 0
    existing_cat_slugs = {c['slug'] for c in cats['categories']}
    for cat in NEW_CATEGORIES:
        if cat['slug'] in existing_cat_slugs:
            print(f"  SKIP category: {cat['slug']} (already exists)")
            continue
        cats['categories'].append(cat)
        print(f"  + category: {cat['slug']} ({cat['tool_count']} tools)")
        added_cats += 1

    # Add tools to existing categories
    for cat_slug, new_tools in CATEGORY_TOOL_ADDITIONS.items():
        for cat in cats['categories']:
            if cat['slug'] == cat_slug:
                existing_tool_slugs = {t['slug'] for t in cat.get('tools', [])}
                for tool in new_tools:
                    if tool['slug'] not in existing_tool_slugs:
                        cat['tools'].append(tool)
                        cat['tool_count'] = len(cat['tools'])
                        print(f"  + {cat_slug}: added {tool['slug']}")

    print(f"\nSummary:")
    print(f"  Tools added: {added_tools}")
    print(f"  Tool content added: {added_content}")
    print(f"  Pricing pages added: {added_pricing}")
    print(f"  Categories added: {added_cats}")
    print(f"  Total tools now: {len(tools['tools'])}")
    print(f"  Total tool content entries: {len(tc)}")
    print(f"  Total pricing pages: {len(pricing['pages'])}")
    print(f"  Total categories: {len(cats['categories'])}")

    if dry_run:
        print("\n[DRY RUN] No changes written.")
    else:
        save("tools.json", tools)
        save("tool_content.json", tc)
        save("pricing_pages.json", pricing)
        save("categories.json", cats)
        print(f"\nWritten to {DATA}/")


if __name__ == '__main__':
    main()
