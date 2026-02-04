# DataStackGuide — Claude Code Project Instructions

## Project Overview

DataStackGuide is a static site built with Astro that reviews B2B data tools (CRMs, enrichment providers, sales engagement platforms, ABM tools, iPaaS, etc.). Content is driven by analyzed job posting data (23,000+ postings) and editorial reviews.

## Architecture

- **Framework:** Astro (static site generator)
- **Data files:** `data/*.json` — all content is JSON-driven, no markdown content files
- **Templates:** `src/pages/tools/[slug].astro` renders tool review pages
- **Build:** `npm run build` (Astro) or `npm run full-build` (extract data + build)

## Key Data Files

| File | Purpose |
|------|---------|
| `data/tool_content.json` | Editorial content for each tool (descriptions, pricing, pros/cons, FAQs, and expanded review fields) |
| `data/tools.json` | Tool metadata — job counts, salary ranges, categories, company counts |
| `data/tool_details.json` | Per-tool job market details — company stages, seniority, functions, top companies/titles |
| `data/cooccurrence.json` | Which tools are mentioned together in job postings |

## Tool Review Expansion

### Status

6 of 60 tools are fully expanded with rich review content. The remaining 54 have base fields only (`description`, `description_2`, `pricing`, `pros`, `cons`, `faq`).

### Expanded fields

Tools with full reviews have these additional fields in `data/tool_content.json`:

- **`overview`** — Array of 4 paragraph strings (replaces description/description_2 in rendering)
- **`key_features`** — Array of 6 `{name, description}` objects
- **`use_cases`** — Array of 3 `{title, description}` objects
- **`pricing_detail`** — String with `\n\n`-separated paragraphs (deeper pricing analysis)
- **`data_quality`** — String with `\n\n`-separated paragraphs (ONLY for data providers/enrichment tools — skip for CRMs, SEPs, iPaaS)
- **`verdict`** — String with `\n\n`-separated paragraphs (3-paragraph recommendation)

### Quality bar

Use the ZoomInfo entry as the template. Key standards:
- Overview paragraphs: 4-6 sentences each, specific market data
- Feature descriptions: 3-5 sentences, practical not marketing-speak
- Use cases: 4-8 sentences with specific personas and workflows
- Pricing: Real dollar amounts, hidden costs, negotiation tips
- Verdict: Honest recommendation with trade-offs and job market data
- Voice: Direct, opinionated, em-dashes, no fluff or superlatives

### How to expand a tool

1. Run `python3 scripts/extract_tool_context.py <slug>` to get all context
2. Read the existing entry in `data/tool_content.json`
3. Write a Python script that adds the 6 new fields to the tool's object
4. Execute the script — it reads, modifies, and writes `tool_content.json`
5. Do NOT delete or modify existing fields — only ADD new ones
6. Verify with: `python3 -c "import json; d=json.load(open('data/tool_content.json')); print('overview' in d['<slug>'])"`

### Batch expansion scripts

| Script | Purpose |
|--------|---------|
| `scripts/extract_tool_context.py` | Extract context data for any tool slug(s) |
| `scripts/expand_prompt_template.md` | Writing instructions and quality standards |
| `scripts/batch_expand.sh` | Process next N tools in one Claude Code invocation |
| `scripts/expand_all.sh` | Loop batch_expand.sh until all tools are done |

## Editorial Voice

- Direct and opinionated — state clear recommendations
- Use em dashes (—) for asides, not parentheses
- Reference specific numbers: pricing, database sizes, accuracy percentages
- Acknowledge weaknesses honestly — the site's value is being trustworthy
- Reference job posting data from our analysis when discussing demand
- Write for B2B buyers (RevOps, VP Sales, Marketing Ops) comparing tools
