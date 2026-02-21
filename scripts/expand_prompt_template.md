# Tool Review Expansion — Prompt Template

This file is used by `batch_expand.sh` to construct prompts for Claude Code.
The batch runner injects the tool context briefs between the `{{TOOL_BRIEFS}}` markers.

---

## Prompt

You are expanding tool reviews for the DataStackGuide website. Your job is to add 6 new fields to each tool entry in `data/tool_content.json`. Only edit that file — do not touch any templates or other files.

### Fields to add

For each tool slug listed below, add these fields to its object in `data/tool_content.json`:

1. **`overview`** — Array of 4 strings (paragraphs). This replaces the 2 short `description`/`description_2` paragraphs with a substantive 4-paragraph deep dive:
   - Para 1: What the tool is, market position, core value proposition with specifics (user counts, database sizes, market share where known)
   - Para 2: Key competitive differentiator — what separates this tool from alternatives
   - Para 3: Platform evolution, acquisitions, product expansion, or ecosystem context
   - Para 4: Practical buyer considerations — who should care, what to watch out for, honest limitations

2. **`key_features`** — Array of 6 objects, each `{"name": "...", "description": "..."}`. Each description should be 3-5 sentences covering:
   - What it does concretely
   - How teams actually use it (not marketing speak)
   - Limitations or caveats where relevant
   - Competitive context if helpful (e.g., "less mature than Gong for this use case")

3. **`use_cases`** — Array of 3 objects, each `{"title": "...", "description": "..."}`. Each description should be 4-8 sentences covering:
   - The specific persona/team using it
   - The concrete workflow (what they do step by step)
   - Typical spend or scale context
   - Why this tool specifically (not a generic alternative)

4. **`pricing_detail`** — Single string with `\n\n` separating 3-4 paragraphs. Cover:
   - Real pricing with specific numbers (not "contact for pricing" — estimate from user reports if needed)
   - Hidden costs, credit systems, add-ons, mandatory fees
   - Practical cost comparisons with named alternatives
   - Negotiation tips or procurement advice where relevant

5. **`data_quality`** — Single string with `\n\n` separating 3-4 paragraphs. **Only include for data providers, enrichment tools, and intent data tools.** Skip for CRMs, SEPs, iPaaS, and other non-data tools. Cover:
   - Accuracy ranges by segment (US vs international, enterprise vs SMB)
   - Known strengths and weaknesses in coverage
   - Data sourcing methodology and freshness
   - Practical verification advice

6. **`verdict`** — Single string with `\n\n` separating 3 paragraphs:
   - Para 1: Clear recommendation — who should buy this tool
   - Para 2: The trade-off — what you give up, and who should use an alternative instead
   - Para 3: Job market context — reference the tool's job posting count, salary range, and demand signals from the brief data provided

### Quality standards

- **Match ZoomInfo's depth.** Each overview paragraph should be 4-6 sentences. Each feature description should be 3-5 sentences. Each use case should be 4-8 sentences.
- **Be specific, not generic.** Use real numbers: database sizes, user counts, pricing, accuracy percentages, typical spend. "Enterprise-grade" and "powerful platform" are banned — say what makes it enterprise-grade.
- **Be honest.** Every tool has weaknesses. State them directly. The site's credibility depends on not sounding like vendor marketing.
- **Use the provided data.** Reference job posting counts, salary ranges, co-occurring tools, company stages, and department distribution from the brief. These are real data points from 23,000+ analyzed job postings.
- **Write for a B2B buyer evaluating tools.** The reader is a RevOps leader, VP of Sales, or marketing ops manager comparing options. They want facts and honest trade-offs, not hype.
- **NO em-dashes.** Em-dashes are the #1 AI writing tell. Use periods, commas, or restructure sentences instead. Also avoid: genuinely, truly, really, actually, robust, leverage, synergy, holistic, cutting-edge, "continues to". See `docs/writing-style-guide.md` for the full list.

### Implementation

Use a Python script to:
1. Read `data/tool_content.json`
2. Add the new fields to each specified tool's object
3. Write the file back with `json.dump(data, f, indent=2, ensure_ascii=False)`

Do NOT delete or modify any existing fields. Only ADD the new fields.

### Tool briefs

{{TOOL_BRIEFS}}
