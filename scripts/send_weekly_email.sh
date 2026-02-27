#!/bin/bash
# send_weekly_email.sh — Monday cron script for Data Stack Weekly
#
# Generates LinkedIn carousel, sends weekly email, and saves snapshot.
#
# Cron example (every Monday at 7 AM):
#   0 7 * * 1 cd /path/to/datastackguide && /bin/bash scripts/send_weekly_email.sh >> logs/weekly_email.log 2>&1
#
# Prerequisites:
#   pip install Pillow resend
#   .env file with RESEND_API_KEY and RESEND_AUDIENCE_ID

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

echo "=========================================="
echo "Data Stack Weekly — $(date)"
echo "=========================================="

# Pull latest code
echo "[0/3] Pulling latest..."
git pull --rebase --autostash 2>&1 || echo "Warning: git pull failed, running with current code"

# Load .env if present
if [ -f .env ]; then
    set -a
    source .env
    set +a
fi

# Create logs directory
mkdir -p logs

# 1. Generate LinkedIn carousel
echo ""
echo "[1/3] Generating LinkedIn carousel..."
python3 scripts/generate_linkedin_carousel.py --output-dir carousel_output
echo "Carousel done."

# 2. Send email
echo ""
echo "[2/3] Sending weekly email..."
python3 scripts/generate_weekly_email.py --send
echo "Email sent."

# 3. Save snapshot for next week's comparison
echo ""
echo "[3/3] Saving market snapshot..."
python3 scripts/generate_weekly_email.py --save-snapshot
echo "Snapshot saved."

echo ""
echo "=========================================="
echo "All done! $(date)"
echo "=========================================="
