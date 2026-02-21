# Tool Expansion Status

## Current state (Feb 2026)

- All 60 tools expanded with full review content (overview, key_features, use_cases, pricing_detail, verdict)
- 718 em-dashes removed across all tools (AI writing tell)
- 72 banned word instances fixed (genuinely, actually, robust, leverage, etc.)
- 22 broken tool slug references cleaned up (18 best-of picks, 3 comparisons, 1 integration)
- 4 thin roundup pages removed (<3 picks after broken ref cleanup)
- 3 orphan tools removed from tools.json (bombora-intent, groove-clari, ringlead-revops)
- 119 new FAQ entries added (all tools now have 4-6 FAQs)
- 19 new alternatives pages generated (58 total, up from 39)
- Build: 401 pages, clean

## Remaining work

### Feature description depth (Priority 6)
18 batch-expanded tools have avg <300 chars per feature description vs. 485-char manual standard:
- salesforce-marketing-cloud (164), amplemarket (167), rb2b (169), rollworks (169)
- capterra (172), nutshell (172), definitive-healthcare (175), marketo (176)
- terminus (177), g2 (177), common-room (177), tray (178)
- celigo (180), leadfeeder (181), oracle-cx (182), mutiny (183)
- airbyte (183), sap-sales-cloud (185)

These need manual expansion with real research to avoid AI tells.

## Scripts

All quality scripts are in `scripts/`:
- `fix_em_dashes.py` - idempotent, run after any content changes
- `fix_banned_words.py` - idempotent, run after any content changes
- `fix_broken_refs.py` - removes dead references
- `generate_faqs.py` - fills tools to 5 FAQs using real data
- `generate_alternatives.py` - creates alternatives pages from tool_content data
