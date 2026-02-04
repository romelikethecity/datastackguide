#!/usr/bin/env bash
#
# batch_expand.sh — Expand tool reviews in batches using Claude Code CLI
#
# Usage:
#   ./scripts/batch_expand.sh              # Process next 5 unexpanded tools
#   ./scripts/batch_expand.sh 3            # Process next 3
#   ./scripts/batch_expand.sh 5 --dry-run  # Show what would be processed
#
# Auto-compaction strategy:
#   Each batch runs as a SEPARATE claude invocation, so context never
#   accumulates across batches.
#

set -euo pipefail

BATCH_SIZE="${1:-5}"
DRY_RUN="${2:-}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
TEMPLATE="$SCRIPT_DIR/expand_prompt_template.md"
CONTEXT_SCRIPT="$SCRIPT_DIR/extract_tool_context.py"

cd "$PROJECT_DIR"

# Get remaining unexpanded slugs
REMAINING=$(python3 "$CONTEXT_SCRIPT" --all-remaining 2>/dev/null | grep "^  " | sed 's/^  //')
TOTAL=$(echo "$REMAINING" | wc -l | tr -d ' ')

if [ -z "$REMAINING" ] || [ "$TOTAL" -eq 0 ]; then
    echo "All tools have been expanded!"
    exit 0
fi

echo "=== DataStackGuide Tool Review Expansion ==="
echo "Remaining: $TOTAL tools"
echo "Batch size: $BATCH_SIZE"
echo ""

# Take the next batch
BATCH=$(echo "$REMAINING" | head -n "$BATCH_SIZE")
BATCH_LIST=$(echo "$BATCH" | tr '\n' ' ')

echo "This batch: $BATCH_LIST"
echo ""

if [ "$DRY_RUN" = "--dry-run" ]; then
    echo "[DRY RUN] Would process these tools:"
    echo "$BATCH" | while read -r slug; do
        echo "  - $slug"
    done
    echo ""
    echo "Context that would be sent:"
    python3 "$CONTEXT_SCRIPT" $BATCH_LIST
    exit 0
fi

# Build prompt file using Python (avoids all shell escaping issues)
PROMPT_FILE=$(mktemp /tmp/expand_prompt.XXXXXX)

python3 - "$TEMPLATE" "$CONTEXT_SCRIPT" "$PROMPT_FILE" $BATCH_LIST <<'PYEOF'
import subprocess, sys

template_path = sys.argv[1]
context_script = sys.argv[2]
output_path = sys.argv[3]
slugs = sys.argv[4:]

# Read template
with open(template_path) as f:
    template = f.read()

# Extract context by calling the context script
result = subprocess.run(
    ["python3", context_script] + slugs,
    capture_output=True, text=True, check=True
)

# Inject briefs into template
prompt = template.replace("{{TOOL_BRIEFS}}", result.stdout)

# Write final prompt
with open(output_path, "w") as f:
    f.write(prompt)

print(f"Prompt: {len(prompt)} chars for {len(slugs)} tools")
PYEOF

echo "Prompt written to $PROMPT_FILE"
echo "Launching Claude Code..."
echo ""

# Run claude with the prompt file piped via stdin
# --dangerously-skip-permissions: auto-approve all tool calls (required for headless mode)
cat "$PROMPT_FILE" | claude -p \
    --dangerously-skip-permissions \
    --max-turns 25

EXIT_CODE=$?

rm -f "$PROMPT_FILE"

if [ $EXIT_CODE -eq 0 ]; then
    echo ""
    echo "=== Batch complete ==="

    # Verify results
    python3 -c "
import json
with open('data/tool_content.json') as f:
    data = json.load(f)
for slug in '$BATCH_LIST'.split():
    has = 'overview' in data.get(slug, {})
    status = 'EXPANDED' if has else 'MISSING'
    print(f'  {status}: {slug}')
"

    NEW_REMAINING=$(python3 "$CONTEXT_SCRIPT" --all-remaining 2>/dev/null | grep "^  " | wc -l | tr -d ' ')
    echo ""
    echo "Remaining after this batch: $NEW_REMAINING tools"
    echo ""
    echo "Run again to process the next batch:"
    echo "  ./scripts/batch_expand.sh $BATCH_SIZE"
else
    echo ""
    echo "=== Batch FAILED (exit code $EXIT_CODE) ==="
    echo "Check output above for errors. Re-run to retry this same batch."
fi
