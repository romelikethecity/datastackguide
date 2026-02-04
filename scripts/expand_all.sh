#!/usr/bin/env bash
#
# expand_all.sh — Run batch_expand.sh in a loop until all tools are done
#
# Usage:
#   ./scripts/expand_all.sh         # Default: batches of 5
#   ./scripts/expand_all.sh 3       # Batches of 3 (smaller = safer)
#   ./scripts/expand_all.sh 8       # Batches of 8 (faster, uses more context)
#
# Each batch is a fresh Claude Code invocation, so there is NO context
# accumulation between batches. This is the auto-compaction strategy:
# rather than compacting within one long session, each batch starts clean.
#
# The script pauses 5 seconds between batches so you can Ctrl+C to stop.
# Progress is printed after each batch.
#

set -euo pipefail

BATCH_SIZE="${1:-5}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CONTEXT_SCRIPT="$SCRIPT_DIR/extract_tool_context.py"
LOG_FILE="$PROJECT_DIR/scripts/expand_log.txt"

cd "$PROJECT_DIR"

echo "=== DataStackGuide — Full Expansion Run ===" | tee -a "$LOG_FILE"
echo "Batch size: $BATCH_SIZE" | tee -a "$LOG_FILE"
echo "Log: $LOG_FILE" | tee -a "$LOG_FILE"
echo "Started: $(date)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

BATCH_NUM=0

while true; do
    # Check how many remain
    REMAINING=$(python3 "$CONTEXT_SCRIPT" --all-remaining 2>/dev/null | grep "^  " | wc -l | tr -d ' ')

    if [ "$REMAINING" -eq 0 ]; then
        echo "All tools expanded! Done." | tee -a "$LOG_FILE"
        break
    fi

    BATCH_NUM=$((BATCH_NUM + 1))
    echo "--- Batch $BATCH_NUM ($REMAINING tools remaining) ---" | tee -a "$LOG_FILE"
    echo "$(date): Starting batch $BATCH_NUM" >> "$LOG_FILE"

    # Run the batch
    if ./scripts/batch_expand.sh "$BATCH_SIZE" 2>&1 | tee -a "$LOG_FILE"; then
        echo "$(date): Batch $BATCH_NUM succeeded" >> "$LOG_FILE"
    else
        echo "$(date): Batch $BATCH_NUM FAILED" >> "$LOG_FILE"
        echo ""
        echo "Batch $BATCH_NUM failed. Check log: $LOG_FILE"
        echo "Fix the issue and re-run: ./scripts/expand_all.sh $BATCH_SIZE"
        exit 1
    fi

    echo "" | tee -a "$LOG_FILE"

    # Check remaining after batch
    NEW_REMAINING=$(python3 "$CONTEXT_SCRIPT" --all-remaining 2>/dev/null | grep "^  " | wc -l | tr -d ' ')

    if [ "$NEW_REMAINING" -eq "$REMAINING" ]; then
        echo "WARNING: No tools were expanded in this batch. Stopping to avoid infinite loop." | tee -a "$LOG_FILE"
        exit 1
    fi

    if [ "$NEW_REMAINING" -eq 0 ]; then
        echo "All tools expanded! Done." | tee -a "$LOG_FILE"
        break
    fi

    echo "Pausing 5s before next batch (Ctrl+C to stop)..." | tee -a "$LOG_FILE"
    sleep 5
done

echo ""
echo "=== Expansion Complete ===" | tee -a "$LOG_FILE"
echo "Finished: $(date)" | tee -a "$LOG_FILE"

# Final verification
python3 -c "
import json
with open('data/tool_content.json') as f:
    data = json.load(f)
expanded = sum(1 for t in data.values() if 'overview' in t)
total = len(data)
print(f'Final status: {expanded}/{total} tools expanded')
missing = [s for s, t in data.items() if 'overview' not in t]
if missing:
    print(f'Still missing: {', '.join(missing)}')
" | tee -a "$LOG_FILE"
