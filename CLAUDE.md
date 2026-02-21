# DataStackGuide: Claude Code Project Instructions

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

All 60 tools are expanded with review content (overview, key_features, use_cases, pricing_detail, verdict). 18 tools have shorter-than-ideal feature descriptions (avg <300 chars vs 485-char target). See Priority 6 in the content scaling plan.

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
- Voice: Direct, opinionated, no fluff or superlatives. NO em-dashes (AI writing tell per style guide).

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

See `docs/writing-style-guide.md` for the full style guide. Key rules:

- Direct and opinionated. State clear recommendations.
- **NO em-dashes.** Use periods, commas, or restructure. Em-dashes are the #1 AI writing tell.
- **NO banned words:** genuinely, truly, really, actually, robust, leverage, synergy, holistic, cutting-edge, game-changer, paradigm shift, "continues to", "in today's market"
- **NO false reframes:** "This isn't X, it's Y" constructions
- **NO unearned declarations:** "The pattern here is clear:", "Here's the thing:", "What this means:"
- Reference specific numbers: pricing, database sizes, accuracy percentages
- Acknowledge weaknesses honestly. The site's value is being trustworthy.
- Reference job posting data from our analysis when discussing demand
- Write for B2B buyers (RevOps, VP Sales, Marketing Ops) comparing tools
- Use contractions. Vary sentence length. Let data speak for itself.

## Content Quality Scripts

| Script | Purpose |
|--------|---------|
| `scripts/fix_em_dashes.py` | Remove em-dashes from tool_content.json |
| `scripts/fix_banned_words.py` | Remove banned words/phrases |
| `scripts/fix_broken_refs.py` | Remove broken tool slug references |
| `scripts/generate_faqs.py` | Add data-driven FAQs to tools with <5 |
| `scripts/generate_alternatives.py` | Create alternatives pages for tools without one |
