#!/usr/bin/env python3
"""
generate_weekly_email.py — Weekly email generator for Data Stack Weekly.

Reads data from data/*.json, computes week-over-week changes,
generates an HTML email, and sends via Resend API.

Usage:
    python3 scripts/generate_weekly_email.py              # Preview only (prints HTML)
    python3 scripts/generate_weekly_email.py --send        # Send via Resend
    python3 scripts/generate_weekly_email.py --save-snapshot  # Save current data as previous snapshot
"""

import json
import os
import sys
import argparse
from datetime import datetime
from pathlib import Path

# Resolve project root (parent of scripts/)
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
SNAPSHOT_PATH = DATA_DIR / "previous_market_snapshot.json"

# Shared inline styles
S_MONO = "font-family:'Space Mono',monospace;"
S_SECTION_TITLE = "margin:0 0 16px;font-size:15px;font-weight:700;color:#e2e8f0;"
S_SECTION_PAD = "padding:24px 24px 20px;"
S_CARD = "background:rgba(255,255,255,0.03);border:1px solid #1e293b;border-radius:10px;padding:16px;"
S_DIVIDER = "border-bottom:1px solid #1e293b;"
S_TEAL_CARD = "background:rgba(20,184,166,0.06);border:1px solid rgba(20,184,166,0.15);border-radius:10px;padding:16px;"
S_PILL = "display:inline-block;padding:4px 10px;background:rgba(20,184,166,0.1);border:1px solid rgba(20,184,166,0.2);border-radius:4px;font-weight:600;color:#5eead4;font-size:13px;"


def load_json(filename):
    with open(DATA_DIR / filename) as f:
        return json.load(f)


def load_previous_snapshot():
    if SNAPSHOT_PATH.exists():
        with open(SNAPSHOT_PATH) as f:
            return json.load(f)
    return None


def save_snapshot(current_data):
    with open(SNAPSHOT_PATH, "w") as f:
        json.dump(current_data, f, indent=2)
    print(f"Snapshot saved to {SNAPSHOT_PATH}")


def tool_display_name(slug):
    return " ".join(w.capitalize() for w in slug.split("-"))


def build_email_data():
    market = load_json("market_signals.json")
    trends = load_json("trends.json")
    cooccurrence = load_json("cooccurrence.json")
    tool_details = load_json("tool_details.json")
    tool_content = load_json("tool_content.json")
    categories = load_json("categories.json")

    # Latest two months from trends
    months = sorted(trends["trends"].keys(), reverse=True)
    latest_month = months[0]
    prev_month = months[1] if len(months) > 1 else None

    latest_data = trends["trends"][latest_month]
    prev_data = trends["trends"][prev_month] if prev_month else []
    prev_lookup = {t["slug"]: t["mentions"] for t in prev_data}

    # Check if previous month has comparable coverage (>50% of current tool count)
    # If not, trends are artifacts of data coverage differences, not real growth
    trends_reliable = len(prev_data) >= len(latest_data) * 0.5

    # Top 10 tools with trend
    top_tools = []
    for t in latest_data[:10]:
        prev_val = prev_lookup.get(t["slug"], 0)
        if trends_reliable and prev_val > 0:
            change = round(((t["mentions"] - prev_val) / prev_val) * 100)
        else:
            change = 0
        top_tools.append({
            "name": t["tool"],
            "slug": t["slug"],
            "mentions": t["mentions"],
            "prev": prev_val if trends_reliable else 0,
            "change": change,
        })

    # Fastest growers (only when trends are reliable)
    growers = []
    if trends_reliable:
        for t in latest_data:
            if t["mentions"] > 10 and t["slug"] in prev_lookup and prev_lookup[t["slug"]] > 0:
                prev_val = prev_lookup[t["slug"]]
                change = round(((t["mentions"] - prev_val) / prev_val) * 100)
                if change > 20:
                    growers.append({
                        "name": t["tool"],
                        "slug": t["slug"],
                        "mentions": t["mentions"],
                        "prev": prev_val,
                        "change": change,
                    })
        growers.sort(key=lambda x: x["change"], reverse=True)

    # Top 5 cooccurrence pairs (deduplicated)
    all_pairs = []
    seen = set()
    for key, pairs in cooccurrence.get("cooccurrence", {}).items():
        for p in pairs[:3]:
            pair_key = tuple(sorted([key, p["slug"]]))
            if pair_key not in seen:
                seen.add(pair_key)
                all_pairs.append({
                    "tool_a": tool_display_name(key),
                    "tool_b": p["tool"],
                    "count": p["count"],
                })
    all_pairs.sort(key=lambda x: x["count"], reverse=True)

    # Seniority breakdown for top tool
    top_slug = top_tools[0]["slug"] if top_tools else "salesforce"
    details = tool_details["details"].get(top_slug, {})
    seniority = details.get("seniority", {})
    seniority_tiers = {
        "Entry": seniority.get("entry", 0),
        "Mid-Level": seniority.get("mid", 0),
        "Senior": seniority.get("senior", 0) + seniority.get("lead", 0),
        "Manager": seniority.get("manager", 0) + seniority.get("senior_manager", 0),
        "Director": seniority.get("director", 0),
        "VP+": seniority.get("vp", 0) + seniority.get("svp", 0) + seniority.get("evp", 0) + seniority.get("c_level", 0),
    }
    seniority_total = sum(seniority_tiers.values()) or 1

    # Remote vs onsite for top 5 tools
    remote_data = []
    for t in top_tools[:5]:
        d = tool_details["details"].get(t["slug"], {})
        rs = d.get("remote_split", {})
        remote = rs.get("remote", 0)
        onsite = rs.get("onsite", 0)
        total = remote + onsite
        if total > 0:
            remote_data.append({
                "name": t["name"],
                "remote_pct": round((remote / total) * 100),
                "remote": remote,
                "onsite": onsite,
            })

    # Top hiring companies across all tools
    all_companies = {}
    for slug, d in tool_details["details"].items():
        for comp in d.get("top_companies", []):
            name = comp["name"].title()
            all_companies[name] = all_companies.get(name, 0) + comp["jobs"]
    top_companies = sorted(all_companies.items(), key=lambda x: x[1], reverse=True)[:8]

    # Pricing spotlight — pick a popular tool with pricing tiers
    pricing_spotlight = None
    for t in top_tools[:10]:
        tc = tool_content.get(t["slug"], {})
        tiers = tc.get("pricing", {}).get("tiers", [])
        if len(tiers) >= 2:
            pricing_spotlight = {
                "name": tc.get("display_name", t["name"]),
                "slug": t["slug"],
                "tiers": tiers[:4],
                "notes": tc.get("pricing", {}).get("notes", ""),
            }
            break

    # Category breakdown
    cat_data = []
    for c in categories.get("categories", []):
        cat_data.append({
            "name": c["name"],
            "count": c.get("tool_count", 0),
            "color": c.get("color", "#14B8A6"),
        })
    cat_data.sort(key=lambda x: x["count"], reverse=True)

    # Format month
    year, month = latest_month.split("-")
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    formatted_month = f"{month_names[int(month) - 1]} {year}"

    return {
        "total_jobs": market["total_jobs_analyzed"],
        "total_tools": market["total_tools_tracked"],
        "total_companies": market["total_companies"],
        "top_tools": top_tools,
        "growers": growers[:3],
        "top_pairs": all_pairs[:5],
        "seniority": seniority_tiers,
        "seniority_total": seniority_total,
        "seniority_tool": top_tools[0]["name"] if top_tools else "Salesforce",
        "remote_data": remote_data,
        "top_companies": top_companies,
        "pricing_spotlight": pricing_spotlight,
        "categories": cat_data[:8],
        "formatted_month": formatted_month,
        "generated_at": datetime.now().isoformat(),
    }


def _trend_arrow(change):
    if change > 0:
        return f'<span style="color:#34d399;{S_MONO}font-size:13px;font-weight:700;">▲ {change}%</span>'
    elif change < 0:
        return f'<span style="color:#f87171;{S_MONO}font-size:13px;font-weight:700;">▼ {abs(change)}%</span>'
    return f'<span style="color:#64748b;{S_MONO}font-size:13px;">—</span>'


def _bar_html(pct, label, color="#0d9488"):
    """Inline CSS bar chart row."""
    return f'''<div style="margin-bottom:8px;">
      <div style="display:flex;justify-content:space-between;margin-bottom:3px;">
        <span style="font-size:13px;color:#cbd5e1;">{label}</span>
        <span style="{S_MONO}font-size:13px;color:#94a3b8;">{pct}%</span>
      </div>
      <div style="background:#1e293b;border-radius:4px;height:8px;overflow:hidden;">
        <div style="background:{color};height:8px;width:{min(pct, 100)}%;border-radius:4px;"></div>
      </div>
    </div>'''


def generate_html(data):
    """Generate the HTML email body."""

    # ── Section 1: Tool Demand Table (10 tools) ──
    tool_rows = ""
    for i, tool in enumerate(data["top_tools"], 1):
        prev_str = f'{tool["prev"]:,}' if tool["prev"] > 0 else "—"
        bg = "rgba(20,184,166,0.04)" if i % 2 == 0 else "transparent"
        tool_rows += f'''<tr style="background:{bg};">
          <td style="padding:8px 8px;color:#e2e8f0;font-size:14px;">
            <span style="display:inline-block;width:22px;height:22px;line-height:22px;text-align:center;font-size:11px;font-weight:600;background:rgba(20,184,166,0.15);color:#2dd4bf;border-radius:4px;margin-right:8px;">{i}</span>
            {tool["name"]}
          </td>
          <td style="padding:8px 8px;color:#cbd5e1;text-align:right;{S_MONO}font-size:13px;">{tool["mentions"]:,}</td>
          <td style="padding:8px 8px;color:#94a3b8;text-align:right;{S_MONO}font-size:13px;">{prev_str}</td>
          <td style="padding:8px 8px;text-align:right;">{_trend_arrow(tool["change"])}</td>
        </tr>'''

    # ── Section 2: Trending Tools ──
    growers_html = ""
    if data["growers"]:
        grower_cards = ""
        for g in data["growers"]:
            grower_cards += f'''<div style="{S_TEAL_CARD}margin-bottom:8px;">
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <span style="font-weight:600;color:#f1f5f9;font-size:14px;">{g["name"]}</span>
                {_trend_arrow(g["change"])}
              </div>
              <div style="font-size:12px;color:#94a3b8;margin-top:4px;">{g["prev"]:,} → {g["mentions"]:,} mentions</div>
            </div>'''
        growers_html = f'''<tr><td style="{S_SECTION_PAD}{S_DIVIDER}">
          <h3 style="{S_SECTION_TITLE}">🚀 Biggest Movers</h3>
          {grower_cards}
        </td></tr>'''

    # ── Section 3: Who's Hiring — Seniority Breakdown ──
    seniority_bars = ""
    max_pct = max((v / data["seniority_total"] * 100 for v in data["seniority"].values()), default=1)
    for level, count in data["seniority"].items():
        pct = round((count / data["seniority_total"]) * 100)
        seniority_bars += _bar_html(pct, f"{level} ({count:,})")

    seniority_html = f'''<tr><td style="{S_SECTION_PAD}{S_DIVIDER}">
      <h3 style="{S_SECTION_TITLE}">📊 Who's Hiring — {data["seniority_tool"]} Roles</h3>
      <div style="{S_CARD}">
        {seniority_bars}
      </div>
      <div style="font-size:11px;color:#475569;margin-top:8px;">n = {data["seniority_total"]:,} roles</div>
    </td></tr>'''

    # ── Section 4: Remote vs Onsite ──
    remote_rows = ""
    for r in data["remote_data"]:
        bar_color = "#34d399" if r["remote_pct"] >= 50 else "#f59e0b"
        remote_rows += _bar_html(r["remote_pct"], r["name"], bar_color)

    remote_html = f'''<tr><td style="{S_SECTION_PAD}{S_DIVIDER}">
      <h3 style="{S_SECTION_TITLE}">🏠 Remote Work by Tool</h3>
      <div style="{S_CARD}">
        {remote_rows}
      </div>
      <div style="font-size:11px;color:#475569;margin-top:8px;">% of roles listed as remote</div>
    </td></tr>'''

    # ── Section 5: Top Hiring Companies ──
    company_items = ""
    for name, count in data["top_companies"]:
        company_items += f'''<tr>
          <td style="padding:5px 8px;font-size:13px;color:#cbd5e1;border-bottom:1px solid #1e293b;">{name}</td>
          <td style="padding:5px 8px;text-align:right;{S_MONO}font-size:13px;color:#2dd4bf;border-bottom:1px solid #1e293b;">{count}</td>
        </tr>'''

    companies_html = f'''<tr><td style="{S_SECTION_PAD}{S_DIVIDER}">
      <h3 style="{S_SECTION_TITLE}">🏢 Top Hiring Companies</h3>
      <table role="presentation" width="100%" cellspacing="0" cellpadding="0">
        <tr>
          <td style="font-size:11px;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:0.05em;padding-bottom:6px;border-bottom:1px solid #334155;">Company</td>
          <td style="font-size:11px;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:0.05em;padding-bottom:6px;border-bottom:1px solid #334155;text-align:right;">Open Roles</td>
        </tr>
        {company_items}
      </table>
    </td></tr>'''

    # ── Section 6: Pricing Spotlight ──
    pricing_html = ""
    if data["pricing_spotlight"]:
        ps = data["pricing_spotlight"]
        tier_rows = ""
        for tier in ps["tiers"]:
            tier_rows += f'''<tr>
              <td style="padding:6px 8px;font-size:13px;color:#e2e8f0;font-weight:600;border-bottom:1px solid #1e293b;">{tier["name"]}</td>
              <td style="padding:6px 8px;{S_MONO}font-size:13px;color:#2dd4bf;text-align:right;border-bottom:1px solid #1e293b;">{tier["price"]}</td>
            </tr>'''

        notes_line = ""
        if ps["notes"]:
            # Truncate long notes
            notes = ps["notes"][:200] + ("..." if len(ps["notes"]) > 200 else "")
            notes_line = f'<div style="font-size:12px;color:#94a3b8;margin-top:10px;line-height:1.5;">{notes}</div>'

        pricing_html = f'''<tr><td style="{S_SECTION_PAD}{S_DIVIDER}">
          <h3 style="{S_SECTION_TITLE}">💰 Pricing Spotlight — {ps["name"]}</h3>
          <div style="{S_CARD}">
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0">
              <tr>
                <td style="font-size:11px;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:0.05em;padding-bottom:6px;border-bottom:1px solid #334155;">Tier</td>
                <td style="font-size:11px;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:0.05em;padding-bottom:6px;border-bottom:1px solid #334155;text-align:right;">Price</td>
              </tr>
              {tier_rows}
            </table>
            {notes_line}
          </div>
          <div style="margin-top:10px;text-align:center;">
            <a href="https://datastackguide.com/pricing/{ps["slug"]}-pricing/" style="font-size:13px;color:#2dd4bf;text-decoration:none;">Full pricing breakdown →</a>
          </div>
        </td></tr>'''

    # ── Section 7: Stack Combos ──
    pair_cards = ""
    for i, pair in enumerate(data["top_pairs"]):
        border = "border-bottom:1px solid #1e293b;" if i < len(data["top_pairs"]) - 1 else ""
        pair_cards += f'''<tr>
          <td style="padding:10px 0;{border}">
            <span style="{S_PILL}">{pair["tool_a"]}</span>
            <span style="color:#64748b;margin:0 4px;font-size:12px;">+</span>
            <span style="{S_PILL}">{pair["tool_b"]}</span>
          </td>
          <td style="padding:10px 0;{border}{S_MONO}font-size:13px;color:#94a3b8;text-align:right;white-space:nowrap;">{pair["count"]} posts</td>
        </tr>'''

    stacks_html = f'''<tr><td style="{S_SECTION_PAD}{S_DIVIDER}">
      <h3 style="{S_SECTION_TITLE}">🔗 Most Common Stack Combos</h3>
      <div style="{S_CARD}">
        <table role="presentation" width="100%" cellspacing="0" cellpadding="0">
          {pair_cards}
        </table>
      </div>
      <div style="font-size:11px;color:#475569;margin-top:8px;">Tools found together in the same job posting</div>
    </td></tr>'''

    # ── Section 8: Category Landscape ──
    cat_rows = ""
    for c in data["categories"]:
        cat_rows += f'''<tr>
          <td style="padding:6px 0;font-size:13px;color:#cbd5e1;border-bottom:1px solid rgba(255,255,255,0.03);">{c["name"]}</td>
          <td style="padding:6px 0;{S_MONO}font-size:13px;color:#2dd4bf;text-align:right;border-bottom:1px solid rgba(255,255,255,0.03);">{c["count"]} tools</td>
        </tr>'''

    categories_html = f'''<tr><td style="{S_SECTION_PAD}{S_DIVIDER}">
      <h3 style="{S_SECTION_TITLE}">🗂️ Category Landscape</h3>
      <div style="{S_CARD}">
        <table role="presentation" width="100%" cellspacing="0" cellpadding="0">
          {cat_rows}
        </table>
      </div>
    </td></tr>'''

    # ── Assemble email ──
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Data Stack Weekly — {data["formatted_month"]}</title>
</head>
<body style="margin:0;padding:0;background:#0f172a;font-family:'Plus Jakarta Sans',-apple-system,BlinkMacSystemFont,sans-serif;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#0f172a;">
    <tr><td align="center" style="padding:24px 16px;">
      <table role="presentation" width="600" cellspacing="0" cellpadding="0" style="background:#0f172a;max-width:600px;width:100%;">

        <!-- Header -->
        <tr><td style="padding:24px 24px 16px;border-bottom:2px solid #0d9488;">
          <div style="{S_MONO}font-size:13px;font-weight:700;color:#2dd4bf;letter-spacing:0.15em;">DATA STACK WEEKLY</div>
          <div style="font-size:20px;font-weight:700;color:#f1f5f9;margin-top:8px;">Your weekly B2B data tool briefing</div>
          <div style="font-size:12px;color:#64748b;margin-top:4px;">{data["formatted_month"]} · datastackguide.com</div>
        </td></tr>

        <!-- Signal strip -->
        <tr><td style="padding:0;">
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:rgba(255,255,255,0.02);{S_DIVIDER}">
            <tr>
              <td width="33%" style="padding:16px;text-align:center;">
                <div style="{S_MONO}font-size:20px;font-weight:700;color:#f1f5f9;">{data["total_tools"]}+</div>
                <div style="font-size:11px;color:#64748b;text-transform:uppercase;letter-spacing:0.05em;">Tools Tracked</div>
              </td>
              <td width="33%" style="padding:16px;text-align:center;border-left:1px solid #1e293b;border-right:1px solid #1e293b;">
                <div style="{S_MONO}font-size:20px;font-weight:700;color:#f1f5f9;">{data["total_jobs"]:,}</div>
                <div style="font-size:11px;color:#64748b;text-transform:uppercase;letter-spacing:0.05em;">Jobs Analyzed</div>
              </td>
              <td width="33%" style="padding:16px;text-align:center;">
                <div style="{S_MONO}font-size:20px;font-weight:700;color:#f1f5f9;">{data["total_companies"]:,}</div>
                <div style="font-size:11px;color:#64748b;text-transform:uppercase;letter-spacing:0.05em;">Companies</div>
              </td>
            </tr>
          </table>
        </td></tr>

        <!-- Tool Demand -->
        <tr><td style="{S_SECTION_PAD}{S_DIVIDER}">
          <h3 style="{S_SECTION_TITLE}">🔥 Tool Demand — Top 10</h3>
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0">
            <tr>
              <td style="font-size:11px;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:0.05em;padding:6px 8px;border-bottom:1px solid #334155;">Tool</td>
              <td style="font-size:11px;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:0.05em;padding:6px 8px;border-bottom:1px solid #334155;text-align:right;">Mentions</td>
              <td style="font-size:11px;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:0.05em;padding:6px 8px;border-bottom:1px solid #334155;text-align:right;">Prev</td>
              <td style="font-size:11px;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:0.05em;padding:6px 8px;border-bottom:1px solid #334155;text-align:right;">Trend</td>
            </tr>
            {tool_rows}
          </table>
        </td></tr>

        {growers_html}

        {seniority_html}

        {remote_html}

        {companies_html}

        {pricing_html}

        {stacks_html}

        {categories_html}

        <!-- CTA -->
        <tr><td style="padding:32px 24px;text-align:center;">
          <div style="font-size:18px;font-weight:700;color:#f1f5f9;margin-bottom:8px;">Want the full picture on any tool?</div>
          <div style="font-size:13px;color:#94a3b8;margin-bottom:20px;">Deep-dive reviews with pricing, pros/cons, and hiring data.</div>
          <a href="https://datastackguide.com/tools/" style="display:inline-block;padding:12px 28px;background:linear-gradient(135deg,#14b8a6,#0d9488);color:white;text-decoration:none;border-radius:8px;font-weight:600;font-size:14px;">Browse All {data["total_tools"]}+ Tool Reviews →</a>
        </td></tr>

        <!-- Share CTA -->
        <tr><td style="padding:28px 24px;text-align:center;background:rgba(20,184,166,0.04);border-top:1px solid rgba(20,184,166,0.1);">
          <div style="font-size:16px;font-weight:700;color:#f1f5f9;margin-bottom:8px;">Know someone building a data stack?</div>
          <div style="font-size:14px;color:#94a3b8;line-height:1.6;margin-bottom:16px;">Forward this email — they'll thank you.</div>
          <div style="font-size:13px;color:#64748b;">Not subscribed? <a href="https://datastackguide.com/newsletter/" style="color:#2dd4bf;text-decoration:none;font-weight:600;">Sign up here</a> — free, every Tuesday.</div>
        </td></tr>

        <!-- Footer -->
        <tr><td style="padding:20px 24px;text-align:center;border-top:1px solid #1e293b;">
          <p style="font-size:12px;color:#475569;margin:0 0 4px;">DataStackGuide · <a href="https://datastackguide.com" style="color:#64748b;">datastackguide.com</a></p>
          <p style="font-size:11px;color:#334155;margin:0;">You received this because you subscribed to Data Stack Weekly.<br>
          <a href="{{{{RESEND_UNSUBSCRIBE_URL}}}}" style="color:#475569;">Unsubscribe</a></p>
        </td></tr>

      </table>
    </td></tr>
  </table>
</body>
</html>"""

    return html


def send_email(html, subject):
    """Send email via Resend API."""
    try:
        import resend
    except ImportError:
        print("Error: 'resend' package not installed. Run: pip install resend")
        sys.exit(1)

    api_key = os.environ.get("RESEND_API_KEY")
    audience_id = os.environ.get("RESEND_AUDIENCE_ID")

    if not api_key:
        print("Error: RESEND_API_KEY not set in environment")
        sys.exit(1)
    if not audience_id:
        print("Error: RESEND_AUDIENCE_ID not set in environment")
        sys.exit(1)

    resend.api_key = api_key

    # Send to audience via broadcast
    try:
        broadcast = resend.Broadcasts.create({
            "audience_id": audience_id,
            "from": "Data Stack Weekly <newsletter@datastackguide.com>",
            "subject": subject,
            "html": html,
        })
        print(f"Broadcast created: {broadcast}")

        # Extract broadcast ID — SDK may return dict or object
        broadcast_id = broadcast.get("id") if isinstance(broadcast, dict) else getattr(broadcast, "id", str(broadcast))
        print(f"Broadcast ID: {broadcast_id}")

        # Send the broadcast
        send_result = resend.Broadcasts.send({"broadcast_id": broadcast_id})
        print(f"Broadcast sent: {send_result}")
    except Exception as e:
        print(f"Error sending email: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate and send Data Stack Weekly email")
    parser.add_argument("--send", action="store_true", help="Send email via Resend")
    parser.add_argument("--save-snapshot", action="store_true", help="Save current data as previous snapshot")
    parser.add_argument("--output", type=str, help="Save HTML to file instead of printing")
    args = parser.parse_args()

    # Load .env if present
    env_path = DATA_DIR.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ.setdefault(key.strip(), val.strip())

    data = build_email_data()

    if args.save_snapshot:
        save_snapshot({
            "top_tools": data["top_tools"],
            "total_jobs": data["total_jobs"],
            "saved_at": data["generated_at"],
        })
        return

    subject = f"Data Stack Weekly — {data['formatted_month']}"
    html = generate_html(data)

    if args.output:
        Path(args.output).write_text(html)
        print(f"HTML saved to {args.output}")
    elif args.send:
        send_email(html, subject)
    else:
        print(html)
        print(f"\n--- Preview mode. Use --send to send, or --output file.html to save. ---")


if __name__ == "__main__":
    main()
