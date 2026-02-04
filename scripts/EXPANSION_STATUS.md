# Tool Expansion Status

## What exists
- `data/tool_content.json` — 6/60 tools expanded (salesforce, hubspot, zoominfo, dynamics-365, linkedin-sales-navigator, salesloft)
- 54 tools remaining
- ZoomInfo is the quality template (overview, key_features, use_cases, pricing_detail, data_quality, verdict)
- `[slug].astro` template already renders all expanded fields

## Scripts created (need debugging)
- `scripts/extract_tool_context.py` — WORKS. Extracts job market data, pricing, co-occurrence for any slug
- `scripts/expand_prompt_template.md` — Writing instructions and quality standards
- `scripts/batch_expand.sh` — Calls `claude -p` per batch. Had issues: mktemp syntax, stdin piping, permission flags
- `scripts/expand_all.sh` — Loops batch_expand.sh
- `CLAUDE.md` — Project context for Claude Code

## What went wrong
1. `mktemp` macOS syntax didn't support `.md` extension — fixed
2. Prompt too large for CLI arg — switched to stdin pipe — fixed
3. `--allowedTools` comma syntax wrong + hung on permissions — switched to `--dangerously-skip-permissions` — NOT YET TESTED

## Current batch_expand.sh claude invocation
```bash
cat "$PROMPT_FILE" | claude -p \
    --dangerously-skip-permissions \
    --max-turns 25
```

## What needs to happen
1. Test that the `claude -p --dangerously-skip-permissions` invocation actually works end-to-end for 1 tool
2. If it works, run `./scripts/expand_all.sh 3` and let it go
3. If not, consider alternative: single Python script that Claude runs within one session to expand tools in groups
