#!/usr/bin/env python3
"""
generate_linkedin_carousel.py — Generate branded LinkedIn carousel slides + PDF.

Creates 6 PNG slides (1080x1350) and a combined PDF.

Usage:
    python3 scripts/generate_linkedin_carousel.py
    python3 scripts/generate_linkedin_carousel.py --output-dir ./carousel_output

Requires: Pillow (pip install Pillow)
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: Pillow not installed. Run: pip install Pillow")
    sys.exit(1)

# Resolve project root
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

# Brand colors
TEAL = (13, 148, 136)       # #0D9488
TEAL_LIGHT = (45, 212, 191) # #2DD4BF
DARK_BG = (15, 23, 42)      # #0F172A
CARD_BG = (30, 41, 59)      # #1E293B
WHITE = (241, 245, 249)     # #F1F5F9
MUTED = (148, 163, 184)     # #94A3B8
GREEN = (52, 211, 153)      # #34D399
RED = (248, 113, 113)       # #F87171

# Slide dimensions
W, H = 1080, 1350


def load_json(filename):
    with open(DATA_DIR / filename) as f:
        return json.load(f)


def get_font(size, bold=False):
    """Try to load a system font, fall back to default."""
    font_names = [
        "PlusJakartaSans-Bold.ttf" if bold else "PlusJakartaSans-Regular.ttf",
        "Arial Bold.ttf" if bold else "Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for name in font_names:
        try:
            return ImageFont.truetype(name, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def get_mono_font(size):
    """Try to load a monospace font."""
    mono_names = [
        "SpaceMono-Regular.ttf",
        "Courier New.ttf",
        "/System/Library/Fonts/Courier.dfont",
    ]
    for name in mono_names:
        try:
            return ImageFont.truetype(name, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def draw_rounded_rect(draw, xy, radius, fill):
    """Draw a rounded rectangle."""
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill)


def draw_teal_accent(draw, y, width=200):
    """Draw a teal accent line."""
    x_center = W // 2
    draw.line([(x_center - width // 2, y), (x_center + width // 2, y)],
              fill=TEAL, width=3)


def create_slide_1_cover(market, trends):
    """Cover slide: Data Stack Weekly + key stats."""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)

    # Brand accent bar at top
    draw.rectangle([0, 0, W, 6], fill=TEAL)

    # Title
    font_brand = get_font(28, bold=True)
    font_title = get_font(64, bold=True)
    font_sub = get_font(28)
    font_stat_num = get_mono_font(72)
    font_stat_label = get_font(22)

    # Brand name
    draw.text((W // 2, 200), "DATA STACK WEEKLY", font=font_brand, fill=TEAL_LIGHT, anchor="mm")

    draw_teal_accent(draw, 240)

    # Main title
    draw.text((W // 2, 360), "This Week in", font=font_title, fill=WHITE, anchor="mm")
    draw.text((W // 2, 440), "B2B Data Tools", font=font_title, fill=WHITE, anchor="mm")

    # Stats
    stats = [
        (f"{market['total_tools_tracked']}+", "Tools Tracked"),
        (f"{market['total_jobs_analyzed']:,}", "Jobs Analyzed"),
        (f"{market['total_companies']:,}", "Companies"),
    ]

    y_start = 620
    for i, (val, label) in enumerate(stats):
        y = y_start + i * 160
        draw_rounded_rect(draw, (140, y, W - 140, y + 120), 16, CARD_BG)
        draw.text((W // 2, y + 40), val, font=font_stat_num, fill=TEAL_LIGHT, anchor="mm")
        draw.text((W // 2, y + 90), label, font=font_stat_label, fill=MUTED, anchor="mm")

    # Bottom branding
    draw.text((W // 2, H - 80), "datastackguide.com", font=font_sub, fill=MUTED, anchor="mm")

    return img


def create_slide_2_demand(trends):
    """Top 5 tools by demand (horizontal bar chart)."""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 6], fill=TEAL)

    font_title = get_font(40, bold=True)
    font_sub = get_font(22)
    font_tool = get_font(28, bold=True)
    font_num = get_mono_font(28)
    font_label = get_font(20)

    draw.text((W // 2, 100), "🔥 Top 5 by Demand", font=font_title, fill=WHITE, anchor="mm")
    draw.text((W // 2, 155), "Job postings mentioning each tool", font=font_sub, fill=MUTED, anchor="mm")
    draw_teal_accent(draw, 195)

    months = sorted(trends["trends"].keys(), reverse=True)
    latest = trends["trends"][months[0]][:5]
    max_val = latest[0]["mentions"] if latest else 1

    bar_left = 100
    bar_right = W - 100
    bar_width = bar_right - bar_left
    y_start = 280

    for i, tool in enumerate(latest):
        y = y_start + i * 180
        ratio = tool["mentions"] / max_val
        fill_w = int(bar_width * ratio)

        # Tool name
        draw.text((bar_left, y), tool["tool"], font=font_tool, fill=WHITE, anchor="lm")

        # Bar background
        draw_rounded_rect(draw, (bar_left, y + 30, bar_right, y + 90), 12, CARD_BG)

        # Bar fill
        if fill_w > 24:
            draw_rounded_rect(draw, (bar_left, y + 30, bar_left + fill_w, y + 90), 12, TEAL)

        # Value
        draw.text((bar_left + fill_w + 15 if fill_w < bar_width - 100 else bar_left + fill_w - 15, y + 60),
                  f"{tool['mentions']:,}",
                  font=font_num,
                  fill=WHITE if fill_w >= bar_width - 100 else TEAL_LIGHT,
                  anchor="lm" if fill_w < bar_width - 100 else "rm")

    # Footer
    draw.text((W // 2, H - 80), "datastackguide.com/newsletter", font=font_label, fill=MUTED, anchor="mm")

    return img


def create_slide_3_trending(trends):
    """Fastest growing tool this week."""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 6], fill=TEAL)

    font_title = get_font(40, bold=True)
    font_sub = get_font(22)
    font_tool = get_font(56, bold=True)
    font_change = get_mono_font(80)
    font_detail = get_font(26)
    font_label = get_font(20)

    draw.text((W // 2, 100), "🚀 Fastest Growing", font=font_title, fill=WHITE, anchor="mm")
    draw.text((W // 2, 155), "Biggest month-over-month jump", font=font_sub, fill=MUTED, anchor="mm")
    draw_teal_accent(draw, 195)

    months = sorted(trends["trends"].keys(), reverse=True)
    latest = trends["trends"][months[0]]
    prev = trends["trends"][months[1]] if len(months) > 1 else []
    prev_lookup = {t["slug"]: t["mentions"] for t in prev}

    grower = None
    best_change = 0
    for t in latest:
        if t["mentions"] > 10 and t["slug"] in prev_lookup and prev_lookup[t["slug"]] > 0:
            change = round(((t["mentions"] - prev_lookup[t["slug"]]) / prev_lookup[t["slug"]]) * 100)
            if change > best_change:
                best_change = change
                grower = {**t, "change": change, "prev": prev_lookup[t["slug"]]}

    if grower:
        # Big card
        draw_rounded_rect(draw, (80, 300, W - 80, 900), 24, CARD_BG)

        draw.text((W // 2, 420), grower["tool"], font=font_tool, fill=WHITE, anchor="mm")

        draw.text((W // 2, 580), f"▲ {grower['change']}%", font=font_change, fill=GREEN, anchor="mm")

        draw.text((W // 2, 700),
                  f"{grower['prev']:,} → {grower['mentions']:,} mentions",
                  font=font_detail, fill=MUTED, anchor="mm")

        draw.text((W // 2, 770),
                  f"Month over month growth",
                  font=font_detail, fill=MUTED, anchor="mm")
    else:
        draw.text((W // 2, 600), "No significant growth this period", font=font_detail, fill=MUTED, anchor="mm")

    draw.text((W // 2, H - 80), "datastackguide.com/newsletter", font=font_label, fill=MUTED, anchor="mm")
    return img


def create_slide_4_seniority(tool_details):
    """Seniority breakdown for top tool."""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 6], fill=TEAL)

    font_title = get_font(40, bold=True)
    font_sub = get_font(22)
    font_level = get_font(26, bold=True)
    font_num = get_mono_font(26)
    font_label = get_font(20)

    draw.text((W // 2, 100), "📊 Who's Hiring?", font=font_title, fill=WHITE, anchor="mm")
    draw.text((W // 2, 155), "Seniority distribution — top tool roles", font=font_sub, fill=MUTED, anchor="mm")
    draw_teal_accent(draw, 195)

    # Use Salesforce (most data)
    details = tool_details["details"].get("salesforce", {})
    seniority = details.get("seniority", {})

    # Aggregate into readable tiers
    tiers = {
        "Entry": seniority.get("entry", 0),
        "Mid-Level": seniority.get("mid", 0),
        "Senior": seniority.get("senior", 0) + seniority.get("lead", 0),
        "Manager": seniority.get("manager", 0) + seniority.get("senior_manager", 0),
        "Director": seniority.get("director", 0),
        "VP+": seniority.get("vp", 0) + seniority.get("svp", 0) + seniority.get("evp", 0) + seniority.get("c_level", 0),
    }

    total = sum(tiers.values()) or 1
    max_val = max(tiers.values()) or 1

    bar_left = 220
    bar_right = W - 100
    bar_w = bar_right - bar_left
    y_start = 300

    for i, (level, count) in enumerate(tiers.items()):
        y = y_start + i * 140
        pct = round((count / total) * 100)
        ratio = count / max_val
        fill_w = int(bar_w * ratio)

        draw.text((bar_left - 20, y + 15), level, font=font_level, fill=WHITE, anchor="rm")

        draw_rounded_rect(draw, (bar_left, y, bar_right, y + 50), 10, CARD_BG)
        if fill_w > 20:
            draw_rounded_rect(draw, (bar_left, y, bar_left + fill_w, y + 50), 10, TEAL)

        draw.text((bar_left + fill_w + 12, y + 25),
                  f"{pct}%", font=font_num, fill=TEAL_LIGHT, anchor="lm")

    draw.text((W // 2, H - 120), "Salesforce ecosystem roles (n=976)", font=font_label, fill=MUTED, anchor="mm")
    draw.text((W // 2, H - 80), "datastackguide.com/newsletter", font=font_label, fill=MUTED, anchor="mm")
    return img


def create_slide_5_stack(cooccurrence):
    """Most common tool pairings."""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 6], fill=TEAL)

    font_title = get_font(40, bold=True)
    font_sub = get_font(22)
    font_pair = get_font(26, bold=True)
    font_num = get_mono_font(24)
    font_label = get_font(20)

    draw.text((W // 2, 100), "🔗 Common Stack Combos", font=font_title, fill=WHITE, anchor="mm")
    draw.text((W // 2, 155), "Tools found together in job postings", font=font_sub, fill=MUTED, anchor="mm")
    draw_teal_accent(draw, 195)

    # Collect top pairs
    all_pairs = []
    seen = set()
    for key, pairs in cooccurrence.get("cooccurrence", {}).items():
        for p in pairs[:3]:
            pair_key = tuple(sorted([key, p["slug"]]))
            if pair_key not in seen:
                seen.add(pair_key)
                display_a = " ".join(w.capitalize() for w in key.split("-"))
                all_pairs.append({
                    "a": display_a,
                    "b": p["tool"],
                    "count": p["count"],
                })

    all_pairs.sort(key=lambda x: x["count"], reverse=True)
    top_pairs = all_pairs[:5]

    y_start = 300
    for i, pair in enumerate(top_pairs):
        y = y_start + i * 170
        draw_rounded_rect(draw, (80, y, W - 80, y + 130), 16, CARD_BG)

        # Pair names
        draw.text((120, y + 35), pair["a"], font=font_pair, fill=TEAL_LIGHT, anchor="lm")
        draw.text((120 + len(pair["a"]) * 16, y + 35), "  +  ", font=font_pair, fill=MUTED, anchor="lm")
        draw.text((120, y + 80), pair["b"], font=font_pair, fill=TEAL_LIGHT, anchor="lm")

        # Count
        draw.text((W - 120, y + 55),
                  f"{pair['count']}", font=font_num, fill=WHITE, anchor="rm")
        draw.text((W - 120, y + 90),
                  "postings", font=font_label, fill=MUTED, anchor="rm")

    draw.text((W // 2, H - 80), "datastackguide.com/newsletter", font=font_label, fill=MUTED, anchor="mm")
    return img


def create_slide_6_cta(market):
    """CTA slide."""
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 6], fill=TEAL)

    font_brand = get_font(28, bold=True)
    font_title = get_font(52, bold=True)
    font_sub = get_font(26)
    font_url = get_font(36, bold=True)
    font_detail = get_font(22)

    draw.text((W // 2, 250), "DATA STACK WEEKLY", font=font_brand, fill=TEAL_LIGHT, anchor="mm")
    draw_teal_accent(draw, 290)

    draw.text((W // 2, 420), "Get this data", font=font_title, fill=WHITE, anchor="mm")
    draw.text((W // 2, 490), "every Tuesday", font=font_title, fill=WHITE, anchor="mm")

    draw.text((W // 2, 600), "Free. No spam. Unsubscribe anytime.", font=font_sub, fill=MUTED, anchor="mm")

    # CTA button
    btn_w, btn_h = 560, 80
    btn_x = (W - btn_w) // 2
    btn_y = 720
    draw_rounded_rect(draw, (btn_x, btn_y, btn_x + btn_w, btn_y + btn_h), 16, TEAL)
    draw.text((W // 2, btn_y + btn_h // 2), "datastackguide.com/newsletter", font=font_url, fill=WHITE, anchor="mm")

    # Stats recap
    stats_text = f"{market['total_tools_tracked']}+ tools · {market['total_jobs_analyzed']:,} jobs · {market['total_companies']:,} companies"
    draw.text((W // 2, 900), stats_text, font=font_detail, fill=MUTED, anchor="mm")

    return img


def generate_post_text(output_dir, market, trends, cooccurrence):
    """Generate a LinkedIn post text file with rotating hooks and key stats."""

    total_tools = market.get("total_tools_tracked", 0)
    total_jobs = market.get("total_jobs_analyzed", 0)
    total_companies = market.get("total_companies", 0)
    top_tools = market.get("top_tools", [])

    # Top tool by demand
    top_tool_name = top_tools[0]["name"] if top_tools else "Salesforce"
    top_tool_jobs = top_tools[0]["job_count"] if top_tools else 0

    # Fastest growing tool (same logic as slide 3)
    months = sorted(trends.get("trends", {}).keys(), reverse=True)
    latest_list = trends["trends"].get(months[0], []) if months else []
    prev_list = trends["trends"].get(months[1], []) if len(months) > 1 else []
    prev_lookup = {t["slug"]: t["mentions"] for t in prev_list}

    grower_name = None
    grower_change = 0
    for t in latest_list:
        if t["mentions"] > 10 and t["slug"] in prev_lookup and prev_lookup[t["slug"]] > 0:
            change = round(((t["mentions"] - prev_lookup[t["slug"]]) / prev_lookup[t["slug"]]) * 100)
            if change > grower_change:
                grower_change = change
                grower_name = t["tool"]

    # Top co-occurrence pair
    top_pair = None
    best_count = 0
    seen = set()
    for key, pairs in cooccurrence.get("cooccurrence", {}).items():
        for p in pairs[:3]:
            pair_key = tuple(sorted([key, p["slug"]]))
            if pair_key not in seen:
                seen.add(pair_key)
                if p["count"] > best_count:
                    best_count = p["count"]
                    display_a = " ".join(w.capitalize() for w in key.split("-"))
                    top_pair = (display_a, p["tool"], p["count"])

    # Count how many tools in latest month had 50+ mentions
    hot_tools_count = sum(1 for t in latest_list if t["mentions"] >= 50)

    # --- Build candidate hooks ---
    candidates = []

    # Hook 1: total jobs analyzed
    candidates.append(
        f"We analyzed {total_jobs:,} job postings to find out which B2B data tools actually matter."
    )

    # Hook 2: top tool dominance
    if top_tool_jobs > 0:
        candidates.append(
            f"{top_tool_name} appeared in {top_tool_jobs:,} job postings last month. Nothing else comes close."
        )

    # Hook 3: fastest grower
    if grower_name and grower_change > 0:
        candidates.append(
            f"{grower_name} job mentions jumped {grower_change}% month over month. Here's what's driving it."
        )

    # Hook 4: tool count
    candidates.append(
        f"{total_tools}+ B2B data tools. {total_jobs:,} job postings. Here's what the hiring data says."
    )

    # Ensure at least 3 candidates (fallback)
    if len(candidates) < 3:
        candidates.append(
            f"The B2B data stack is shifting fast. We tracked {total_tools}+ tools to prove it."
        )

    # Pick hook using week number
    week_num = datetime.now().isocalendar()[1]
    hook = candidates[week_num % len(candidates)]

    # --- Build bullet points ---
    bullets = []

    # Bullet: top 3 tools by demand
    if len(latest_list) >= 3:
        top3 = [t["tool"] for t in latest_list[:3]]
        bullets.append(f"Top 3 by demand: {top3[0]}, {top3[1]}, {top3[2]}")

    # Bullet: total companies hiring
    bullets.append(f"{total_companies:,} companies hiring across {total_tools}+ tools")

    # Bullet: fastest grower
    if grower_name and grower_change > 0:
        bullets.append(f"Fastest grower: {grower_name} ({grower_change}% MoM)")

    # Bullet: top pairing
    if top_pair:
        bullets.append(f"Most common pairing: {top_pair[0]} + {top_pair[1]} ({top_pair[2]} postings)")

    # Bullet: hot tools count
    if hot_tools_count > 0:
        bullets.append(f"{hot_tools_count} tools with 50+ job mentions this month")

    # Trim to 3-4 bullets
    bullets = bullets[:4]

    # --- Assemble post ---
    lines = [hook, ""]
    for b in bullets:
        lines.append(f"  {b}")
    lines.append("")
    lines.append("Swipe for the full breakdown \u2193")
    lines.append("")
    lines.append("#DataStack #DataEngineering #Analytics #DataOps #ModernDataStack")

    post_text = "\n".join(lines)

    # Save
    post_path = Path(output_dir) / "post.txt"
    with open(post_path, "w") as f:
        f.write(post_text)
    print(f"Saved post text: {post_path}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate LinkedIn carousel slides")
    parser.add_argument("--output-dir", type=str, default=str(ROOT / "carousel_output"),
                        help="Output directory for slides")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load data
    market = load_json("market_signals.json")
    trends = load_json("trends.json")
    cooccurrence = load_json("cooccurrence.json")
    tool_details = load_json("tool_details.json")

    # Generate slides
    slides = [
        ("01-cover", create_slide_1_cover(market, trends)),
        ("02-demand", create_slide_2_demand(trends)),
        ("03-trending", create_slide_3_trending(trends)),
        ("04-seniority", create_slide_4_seniority(tool_details)),
        ("05-stack-combos", create_slide_5_stack(cooccurrence)),
        ("06-cta", create_slide_6_cta(market)),
    ]

    png_paths = []
    for name, img in slides:
        path = output_dir / f"{name}.png"
        img.save(path, "PNG", quality=95)
        png_paths.append(path)
        print(f"Saved: {path}")

    # Combine into PDF
    pdf_path = output_dir / "data-stack-weekly-carousel.pdf"
    images = [Image.open(p).convert("RGB") for p in png_paths]
    images[0].save(pdf_path, "PDF", resolution=150, save_all=True, append_images=images[1:])
    print(f"Saved PDF: {pdf_path}")

    # Generate LinkedIn post text
    generate_post_text(output_dir, market, trends, cooccurrence)

    print(f"\nDone! {len(slides)} slides + 1 PDF + post.txt in {output_dir}/")


if __name__ == "__main__":
    main()
