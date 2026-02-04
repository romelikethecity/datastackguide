#!/usr/bin/env python3
"""
SEO Audit Script for DataStackGuide
====================================
Audits all HTML pages in the dist/ directory for SEO best practices.

Checks performed:
  1.  Title tag (present, unique, length 50-60 chars ideal)
  2.  Meta description (present, length 120-160 chars ideal)
  3.  Canonical URL (present, datastackguide.com domain, trailing slash)
  4.  Open Graph tags (6 required tags)
  5.  Twitter Card tags (4 required tags)
  6.  H1 tag (exactly one, length 40-70 chars ideal)
  7.  JSON-LD Schema (present, valid JSON, appropriate @type)
  8.  BreadcrumbList schema (present on inner pages)
  9.  FAQPage schema (present on compare, alternatives, best-of, pricing pages)
  10. Internal links (count, flag pages with < 3)
  11. Images (alt attributes, width/height attributes)
  12. CSS version parameter (?v= cache busting on stylesheets)
  13. Robots meta tag (check for accidental noindex/nofollow)
  14. Viewport meta tag (present and correct)
  15. GA4/Analytics (present)
  16. Content length (word count of main content area)

Usage:
  python3 scripts/seo_audit.py
"""

import os
import sys
import json
import re
from html.parser import HTMLParser
from collections import defaultdict, Counter
from pathlib import Path
from datetime import datetime


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = PROJECT_ROOT / "dist"
REPORT_PATH = PROJECT_ROOT / "seo-audit-report.txt"
EXPECTED_DOMAIN = "datastackguide.com"

# Page type patterns (directory segments that indicate page type)
COMPARE_PATTERN = "/compare/"
ALTERNATIVES_PATTERN = "/alternatives/"
BEST_PATTERN = "/best/"
PRICING_PATTERN = "/pricing/"
FAQ_EXPECTED_SECTIONS = [COMPARE_PATTERN, ALTERNATIVES_PATTERN, BEST_PATTERN, PRICING_PATTERN]

# Ideal ranges
TITLE_MIN, TITLE_MAX = 30, 60
TITLE_WARN_MAX = 70
META_DESC_MIN, META_DESC_MAX = 120, 160
META_DESC_WARN_MIN = 70
H1_MIN, H1_MAX = 20, 70
H1_WARN_MAX = 90
MIN_INTERNAL_LINKS = 3
MIN_WORD_COUNT = 100

# Severity levels
CRITICAL = "CRITICAL"
WARNING = "WARNING"
INFO = "INFO"

# Required OG tags
REQUIRED_OG_TAGS = {"og:type", "og:url", "og:title", "og:description", "og:site_name", "og:image"}
REQUIRED_TWITTER_TAGS = {"twitter:card", "twitter:title", "twitter:description", "twitter:image"}


# ---------------------------------------------------------------------------
# Lightweight HTML parser (stdlib only, no BeautifulSoup dependency)
# ---------------------------------------------------------------------------
class SEOHTMLParser(HTMLParser):
    """Parse an HTML document and extract SEO-relevant data."""

    def __init__(self):
        super().__init__()
        # Metadata
        self.title = None
        self.meta_description = None
        self.canonical_url = None
        self.viewport = None
        self.robots_meta = None

        # OG / Twitter
        self.og_tags = {}
        self.twitter_tags = {}

        # Headings
        self.h1_texts = []
        self._in_h1 = False
        self._h1_buf = []

        # Title capture
        self._in_title = False
        self._title_buf = []

        # JSON-LD
        self.json_ld_blocks = []
        self._in_json_ld = False
        self._json_ld_buf = []

        # Links
        self.internal_links = []
        self.external_links = []
        self.stylesheet_links = []

        # Images
        self.images = []  # list of dicts: {src, alt, has_width, has_height}

        # Analytics
        self.has_ga4 = False

        # Content word count (text inside <main>)
        self._in_main = False
        self._main_depth = 0
        self._main_text_buf = []

        # Tag depth tracker for nested elements
        self._tag_stack = []

    # -- handlers ----------------------------------------------------------

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        tag_lower = tag.lower()
        self._tag_stack.append(tag_lower)

        if tag_lower == "title":
            self._in_title = True
            self._title_buf = []

        elif tag_lower == "meta":
            name = attrs_dict.get("name", "").lower()
            prop = attrs_dict.get("property", "").lower()
            content = attrs_dict.get("content", "")

            if name == "description":
                self.meta_description = content
            elif name == "viewport":
                self.viewport = content
            elif name == "robots":
                self.robots_meta = content

            # OG tags
            if prop.startswith("og:"):
                self.og_tags[prop] = content
            # Twitter tags
            if name.startswith("twitter:"):
                self.twitter_tags[name] = content

        elif tag_lower == "link":
            rel = attrs_dict.get("rel", "").lower()
            href = attrs_dict.get("href", "")
            if rel == "canonical":
                self.canonical_url = href
            if rel == "stylesheet" or (rel == "stylesheet" and href):
                if href and not href.startswith("http"):
                    self.stylesheet_links.append(href)
                elif href:
                    self.stylesheet_links.append(href)

        elif tag_lower == "h1":
            self._in_h1 = True
            self._h1_buf = []

        elif tag_lower == "script":
            stype = attrs_dict.get("type", "").lower()
            src = attrs_dict.get("src", "")
            if stype == "application/ld+json":
                self._in_json_ld = True
                self._json_ld_buf = []
            if "googletagmanager.com" in src or "gtag" in src:
                self.has_ga4 = True

        elif tag_lower == "a":
            href = attrs_dict.get("href", "")
            if href:
                if href.startswith("/") or href.startswith(f"https://{EXPECTED_DOMAIN}"):
                    self.internal_links.append(href)
                elif href.startswith("http"):
                    self.external_links.append(href)

        elif tag_lower == "img":
            self.images.append({
                "src": attrs_dict.get("src", ""),
                "alt": attrs_dict.get("alt"),
                "has_width": "width" in attrs_dict,
                "has_height": "height" in attrs_dict,
            })

        elif tag_lower == "main":
            self._in_main = True
            self._main_depth = len(self._tag_stack)

    def handle_endtag(self, tag):
        tag_lower = tag.lower()

        if tag_lower == "title":
            self._in_title = False
            self.title = "".join(self._title_buf).strip()

        elif tag_lower == "h1" and self._in_h1:
            self._in_h1 = False
            self.h1_texts.append("".join(self._h1_buf).strip())

        elif tag_lower == "script" and self._in_json_ld:
            self._in_json_ld = False
            raw = "".join(self._json_ld_buf).strip()
            if raw:
                self.json_ld_blocks.append(raw)

        elif tag_lower == "main" and self._in_main:
            self._in_main = False

        # Pop tag stack
        if self._tag_stack and self._tag_stack[-1] == tag_lower:
            self._tag_stack.pop()

    def handle_data(self, data):
        if self._in_title:
            self._title_buf.append(data)
        if self._in_h1:
            self._h1_buf.append(data)
        if self._in_json_ld:
            self._json_ld_buf.append(data)
        if self._in_main:
            self._main_text_buf.append(data)

    def handle_comment(self, data):
        pass

    # -- derived properties ------------------------------------------------

    @property
    def main_word_count(self):
        text = " ".join(self._main_text_buf)
        # Strip extra whitespace and count words
        words = re.findall(r"\b\w+\b", text)
        return len(words)

    @property
    def parsed_json_ld(self):
        """Return list of (raw_str, parsed_obj_or_None) tuples."""
        results = []
        for raw in self.json_ld_blocks:
            try:
                obj = json.loads(raw)
                results.append((raw, obj))
            except json.JSONDecodeError:
                results.append((raw, None))
        return results


# ---------------------------------------------------------------------------
# Issue collector
# ---------------------------------------------------------------------------
class PageAudit:
    """Collects issues for a single page."""

    def __init__(self, filepath: str, url_path: str):
        self.filepath = filepath
        self.url_path = url_path
        self.issues = []  # list of (severity, category, message)
        # Diagnostic stats (not counted as issues)
        self.stats = {}  # key -> value for reporting

    def add(self, severity: str, category: str, message: str):
        self.issues.append((severity, category, message))

    @property
    def critical_count(self):
        return sum(1 for s, _, _ in self.issues if s == CRITICAL)

    @property
    def warning_count(self):
        return sum(1 for s, _, _ in self.issues if s == WARNING)

    @property
    def info_count(self):
        return sum(1 for s, _, _ in self.issues if s == INFO)

    @property
    def has_issues(self):
        return len(self.issues) > 0

    @property
    def is_passing(self):
        return self.critical_count == 0 and self.warning_count == 0


# ---------------------------------------------------------------------------
# Audit logic for a single page
# ---------------------------------------------------------------------------
def determine_page_type(url_path: str) -> str:
    """Return a human-readable page type based on URL path."""
    if url_path == "/":
        return "homepage"
    for pattern, name in [
        (COMPARE_PATTERN, "comparison"),
        (ALTERNATIVES_PATTERN, "alternatives"),
        (BEST_PATTERN, "best-of"),
        (PRICING_PATTERN, "pricing"),
        ("/tools/", "tool"),
        ("/categories/", "category"),
        ("/guides/", "guide"),
        ("/glossary/", "glossary"),
        ("/reports/", "report"),
        ("/about/", "about"),
        ("/methodology/", "methodology"),
    ]:
        if pattern in url_path:
            return name
    return "other"


def is_inner_page(url_path: str) -> bool:
    """True for anything other than the homepage."""
    return url_path != "/"


def should_have_faq_schema(url_path: str) -> bool:
    """Return True if the page type typically requires FAQPage schema."""
    return any(p in url_path for p in FAQ_EXPECTED_SECTIONS)


def audit_page(filepath: str, url_path: str) -> PageAudit:
    """Run all SEO checks on a single HTML file."""
    audit = PageAudit(filepath, url_path)
    page_type = determine_page_type(url_path)

    # Read and parse
    with open(filepath, "r", encoding="utf-8") as f:
        html_content = f.read()

    parser = SEOHTMLParser()
    try:
        parser.feed(html_content)
    except Exception as e:
        audit.add(CRITICAL, "Parse Error", f"Failed to parse HTML: {e}")
        return audit

    # --- 1. Title Tag ---
    if parser.title is None or parser.title == "":
        audit.add(CRITICAL, "Title", "Missing or empty <title> tag")
    else:
        title_len = len(parser.title)
        if title_len < TITLE_MIN:
            audit.add(WARNING, "Title", f"Title too short ({title_len} chars): \"{parser.title}\"")
        elif title_len > TITLE_WARN_MAX:
            audit.add(WARNING, "Title", f"Title too long ({title_len} chars, ideal: {TITLE_MIN}-{TITLE_MAX}): \"{parser.title[:80]}...\"")
        elif title_len > TITLE_MAX:
            audit.add(INFO, "Title", f"Title slightly long ({title_len} chars, ideal: {TITLE_MIN}-{TITLE_MAX})")

    # --- 2. Meta Description ---
    if parser.meta_description is None:
        audit.add(CRITICAL, "Meta Description", "Missing <meta name=\"description\"> tag")
    elif parser.meta_description == "":
        audit.add(CRITICAL, "Meta Description", "Empty meta description")
    else:
        desc_len = len(parser.meta_description)
        if desc_len < META_DESC_WARN_MIN:
            audit.add(WARNING, "Meta Description", f"Meta description too short ({desc_len} chars)")
        elif desc_len < META_DESC_MIN:
            audit.add(INFO, "Meta Description", f"Meta description slightly short ({desc_len} chars, ideal: {META_DESC_MIN}-{META_DESC_MAX})")
        elif desc_len > META_DESC_MAX:
            audit.add(INFO, "Meta Description", f"Meta description long ({desc_len} chars, may be truncated in SERPs)")

    # --- 3. Canonical URL ---
    if parser.canonical_url is None:
        audit.add(CRITICAL, "Canonical", "Missing <link rel=\"canonical\"> tag")
    else:
        canon = parser.canonical_url
        if "github.io" in canon:
            audit.add(CRITICAL, "Canonical", f"Canonical uses github.io domain: {canon}")
        if EXPECTED_DOMAIN not in canon:
            audit.add(CRITICAL, "Canonical", f"Canonical does not use {EXPECTED_DOMAIN}: {canon}")
        if not canon.endswith("/"):
            audit.add(WARNING, "Canonical", f"Canonical URL missing trailing slash: {canon}")

    # --- 4. Open Graph Tags ---
    missing_og = REQUIRED_OG_TAGS - set(parser.og_tags.keys())
    if missing_og:
        audit.add(CRITICAL, "Open Graph", f"Missing OG tags: {', '.join(sorted(missing_og))}")
    else:
        for tag, value in parser.og_tags.items():
            if tag in REQUIRED_OG_TAGS and not value:
                audit.add(WARNING, "Open Graph", f"Empty OG tag: {tag}")

    # --- 5. Twitter Card Tags ---
    missing_tw = REQUIRED_TWITTER_TAGS - set(parser.twitter_tags.keys())
    if missing_tw:
        audit.add(CRITICAL, "Twitter Card", f"Missing Twitter tags: {', '.join(sorted(missing_tw))}")
    else:
        for tag, value in parser.twitter_tags.items():
            if tag in REQUIRED_TWITTER_TAGS and not value:
                audit.add(WARNING, "Twitter Card", f"Empty Twitter tag: {tag}")

    # --- 6. H1 Tag ---
    h1_count = len(parser.h1_texts)
    if h1_count == 0:
        audit.add(CRITICAL, "H1", "Missing <h1> tag")
    elif h1_count > 1:
        audit.add(WARNING, "H1", f"Multiple H1 tags ({h1_count} found): {[t[:50] for t in parser.h1_texts]}")
    else:
        h1_text = parser.h1_texts[0]
        h1_len = len(h1_text)
        if h1_len < H1_MIN:
            audit.add(INFO, "H1", f"H1 short ({h1_len} chars): \"{h1_text}\"")
        elif h1_len > H1_WARN_MAX:
            audit.add(WARNING, "H1", f"H1 too long ({h1_len} chars): \"{h1_text[:60]}...\"")
        elif h1_len > H1_MAX:
            audit.add(INFO, "H1", f"H1 slightly long ({h1_len} chars, ideal: {H1_MIN}-{H1_MAX})")

    # --- 7. JSON-LD Schema ---
    json_ld_items = parser.parsed_json_ld
    if not json_ld_items:
        audit.add(CRITICAL, "JSON-LD", "No JSON-LD structured data found")
    else:
        for i, (raw, obj) in enumerate(json_ld_items):
            if obj is None:
                audit.add(CRITICAL, "JSON-LD", f"Invalid JSON in JSON-LD block #{i+1}")

    # Collect @type values
    schema_types = set()
    for _, obj in json_ld_items:
        if obj and isinstance(obj, dict):
            t = obj.get("@type", "")
            if t:
                schema_types.add(t)

    # --- 8. BreadcrumbList schema on inner pages ---
    if is_inner_page(url_path):
        if "BreadcrumbList" not in schema_types:
            audit.add(WARNING, "Breadcrumb Schema", "Inner page missing BreadcrumbList JSON-LD schema")

    # --- 9. FAQPage schema on comparison/alternatives/best/pricing ---
    if should_have_faq_schema(url_path):
        # Only check detail pages (not index listing pages)
        # Index pages are like /compare/index.html, /alternatives/index.html
        path_parts = [p for p in url_path.strip("/").split("/") if p]
        if len(path_parts) >= 2:
            if "FAQPage" not in schema_types:
                audit.add(WARNING, "FAQ Schema", f"Page type '{page_type}' should have FAQPage schema")

    # --- 10. Internal Links ---
    internal_count = len(parser.internal_links)
    audit.stats["internal_links"] = internal_count
    audit.stats["external_links"] = len(parser.external_links)
    if internal_count < MIN_INTERNAL_LINKS:
        audit.add(WARNING, "Internal Links", f"Only {internal_count} internal links (minimum recommended: {MIN_INTERNAL_LINKS})")

    # --- 11. Images ---
    images_missing_alt = [img for img in parser.images if img["alt"] is None]
    images_empty_alt = [img for img in parser.images if img["alt"] is not None and img["alt"].strip() == "" and not _is_decorative(img)]
    images_missing_dimensions = [img for img in parser.images if not img["has_width"] or not img["has_height"]]

    if images_missing_alt:
        audit.add(WARNING, "Images", f"{len(images_missing_alt)} image(s) missing alt attribute: {[i['src'][:60] for i in images_missing_alt[:3]]}")
    if images_empty_alt:
        audit.add(INFO, "Images", f"{len(images_empty_alt)} image(s) with empty alt (non-decorative?): {[i['src'][:60] for i in images_empty_alt[:3]]}")
    if images_missing_dimensions:
        audit.add(INFO, "Images", f"{len(images_missing_dimensions)} image(s) missing width/height attributes (CLS risk)")

    # --- 12. CSS Version Parameter ---
    local_css = [s for s in parser.stylesheet_links if not s.startswith("http")]
    # Astro uses content-hashed filenames (e.g., index.g6pYwFxp.css), which is
    # equivalent to cache busting. Only flag plain filenames without hashes.
    css_without_busting = []
    for css_href in local_css:
        filename = css_href.split("/")[-1].split("?")[0]
        # Check if filename has a hash-like pattern (e.g., .XXXXXXXX. or ?v=)
        has_hash = bool(re.search(r"\.[a-zA-Z0-9]{6,}\.", filename))
        has_version_param = "?v=" in css_href or "&v=" in css_href
        if not has_hash and not has_version_param:
            css_without_busting.append(css_href)
    if css_without_busting:
        audit.add(INFO, "CSS Cache Busting", f"{len(css_without_busting)} stylesheet(s) without cache-busting: {css_without_busting[:3]}")

    # --- 13. Robots Meta Tag ---
    if parser.robots_meta:
        robots_lower = parser.robots_meta.lower()
        if "noindex" in robots_lower:
            audit.add(CRITICAL, "Robots", f"Page has noindex set: {parser.robots_meta}")
        if "nofollow" in robots_lower:
            audit.add(WARNING, "Robots", f"Page has nofollow set: {parser.robots_meta}")

    # --- 14. Viewport Meta Tag ---
    if not parser.viewport:
        audit.add(CRITICAL, "Viewport", "Missing <meta name=\"viewport\"> tag")
    elif "width=device-width" not in parser.viewport:
        audit.add(WARNING, "Viewport", f"Viewport may be misconfigured: {parser.viewport}")

    # --- 15. GA4/Analytics ---
    # Also check the raw HTML for gtag patterns
    if not parser.has_ga4:
        if "googletagmanager.com/gtag" in html_content or "G-" in html_content:
            parser.has_ga4 = True
    if not parser.has_ga4:
        audit.add(CRITICAL, "Analytics", "No GA4/Google Analytics detected")

    # --- 16. Content Length ---
    word_count = parser.main_word_count
    audit.stats["word_count"] = word_count
    audit.stats["images"] = len(parser.images)
    audit.stats["title_len"] = len(parser.title) if parser.title else 0
    audit.stats["desc_len"] = len(parser.meta_description) if parser.meta_description else 0
    if word_count < MIN_WORD_COUNT:
        audit.add(INFO, "Content Length", f"Low word count in <main>: {word_count} words")

    return audit


def _is_decorative(img: dict) -> bool:
    """Heuristic: images that are likely decorative (icons, spacers)."""
    src = img.get("src", "").lower()
    return any(x in src for x in ["icon", "spacer", "pixel", "logo", "arrow", "separator"])


# ---------------------------------------------------------------------------
# Uniqueness checks across all pages
# ---------------------------------------------------------------------------
def check_uniqueness(audits: list[PageAudit], all_titles: dict, all_descriptions: dict):
    """Check that titles and meta descriptions are unique across all pages."""
    # Titles
    for title_text, pages in all_titles.items():
        if len(pages) > 1 and title_text:
            for audit in audits:
                if audit.url_path in pages:
                    other_pages = [p for p in pages if p != audit.url_path]
                    audit.add(WARNING, "Title", f"Duplicate title shared with: {other_pages[:3]}")

    # Descriptions
    for desc_text, pages in all_descriptions.items():
        if len(pages) > 1 and desc_text:
            for audit in audits:
                if audit.url_path in pages:
                    other_pages = [p for p in pages if p != audit.url_path]
                    audit.add(WARNING, "Meta Description", f"Duplicate description shared with: {other_pages[:3]}")


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------
def generate_report(audits: list[PageAudit]) -> str:
    """Generate the full text report."""
    lines = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines.append("=" * 80)
    lines.append("  DataStackGuide SEO Audit Report")
    lines.append(f"  Generated: {now}")
    lines.append("=" * 80)
    lines.append("")

    # ---- Summary stats ----
    total = len(audits)
    passing = sum(1 for a in audits if a.is_passing)
    with_issues = total - passing
    total_critical = sum(a.critical_count for a in audits)
    total_warnings = sum(a.warning_count for a in audits)
    total_info = sum(a.info_count for a in audits)

    lines.append("SUMMARY")
    lines.append("-" * 40)
    lines.append(f"  Total pages audited:    {total}")
    lines.append(f"  Pages passing:          {passing}  ({passing/total*100:.1f}%)")
    lines.append(f"  Pages with issues:      {with_issues}  ({with_issues/total*100:.1f}%)")
    lines.append("")
    lines.append(f"  Total CRITICAL issues:  {total_critical}")
    lines.append(f"  Total WARNING issues:   {total_warnings}")
    lines.append(f"  Total INFO notes:       {total_info}")
    lines.append("")

    # ---- Issue distribution by category ----
    category_counts = defaultdict(lambda: {CRITICAL: 0, WARNING: 0, INFO: 0})
    for audit in audits:
        for severity, category, _ in audit.issues:
            category_counts[category][severity] += 1

    lines.append("ISSUES BY CATEGORY")
    lines.append("-" * 40)
    lines.append(f"  {'Category':<25} {'CRIT':>6} {'WARN':>6} {'INFO':>6} {'Total':>6}")
    lines.append(f"  {'-'*25} {'-'*6} {'-'*6} {'-'*6} {'-'*6}")

    sorted_cats = sorted(category_counts.items(),
                         key=lambda x: (x[1][CRITICAL], x[1][WARNING], x[1][INFO]),
                         reverse=True)
    for cat, counts in sorted_cats:
        cat_total = counts[CRITICAL] + counts[WARNING] + counts[INFO]
        lines.append(f"  {cat:<25} {counts[CRITICAL]:>6} {counts[WARNING]:>6} {counts[INFO]:>6} {cat_total:>6}")
    lines.append("")

    # ---- Most common issues (top 15) ----
    issue_counter = Counter()
    for audit in audits:
        for severity, category, message in audit.issues:
            # Normalize messages that contain page-specific data
            key = (severity, category, message)
            issue_counter[key] += 1

    # Group similar issues
    grouped_issues = Counter()
    for (severity, category, message), count in issue_counter.items():
        # Create a simplified key for grouping
        if "Duplicate" in message:
            grouped_issues[(severity, category, "Duplicate content detected")] += count
        else:
            grouped_issues[(severity, category, message)] += count

    lines.append("MOST COMMON ISSUES (Top 20)")
    lines.append("-" * 40)
    for (severity, category, message), count in grouped_issues.most_common(20):
        lines.append(f"  [{severity}] {category}: {message}")
        lines.append(f"    Affected pages: {count}")
    lines.append("")

    # ---- Pages with CRITICAL issues ----
    critical_pages = [a for a in audits if a.critical_count > 0]
    if critical_pages:
        lines.append(f"PAGES WITH CRITICAL ISSUES ({len(critical_pages)} pages)")
        lines.append("-" * 40)
        for audit in sorted(critical_pages, key=lambda a: a.critical_count, reverse=True):
            lines.append(f"  {audit.url_path}")
            for severity, category, message in audit.issues:
                if severity == CRITICAL:
                    lines.append(f"    [{CRITICAL}] {category}: {message}")
        lines.append("")

    # ---- Per-page breakdown (only pages with issues) ----
    lines.append("PER-PAGE BREAKDOWN (pages with warnings or critical issues)")
    lines.append("=" * 80)

    pages_with_problems = [a for a in audits if not a.is_passing]
    for audit in sorted(pages_with_problems, key=lambda a: (a.critical_count, a.warning_count), reverse=True):
        page_type = determine_page_type(audit.url_path)
        lines.append("")
        lines.append(f"  Page: {audit.url_path}")
        lines.append(f"  Type: {page_type}")
        lines.append(f"  Issues: {audit.critical_count} critical, {audit.warning_count} warnings, {audit.info_count} info")

        for severity, category, message in audit.issues:
            if severity in (CRITICAL, WARNING):
                marker = "!!!" if severity == CRITICAL else " ! "
                lines.append(f"    {marker} [{severity}] {category}: {message}")
        lines.append("")

    # ---- INFO-only section (condensed) ----
    info_only_pages = [a for a in audits if a.is_passing and a.info_count > 0]
    if info_only_pages:
        lines.append("")
        lines.append(f"PAGES WITH INFO NOTES ONLY ({len(info_only_pages)} pages)")
        lines.append("-" * 40)
        for audit in info_only_pages[:30]:
            info_msgs = [f"{cat}: {msg}" for _, cat, msg in audit.issues if _ == INFO]
            lines.append(f"  {audit.url_path}")
            for msg in info_msgs:
                lines.append(f"      {msg}")
        if len(info_only_pages) > 30:
            lines.append(f"  ... and {len(info_only_pages) - 30} more pages")

    # ---- Clean pages ----
    clean_pages = [a for a in audits if not a.has_issues]
    lines.append("")
    lines.append(f"CLEAN PAGES ({len(clean_pages)} pages with no issues)")
    lines.append("-" * 40)
    if clean_pages:
        for audit in clean_pages:
            lines.append(f"  {audit.url_path}")
    else:
        lines.append("  (All pages have at least one info-level note)")

    # ---- Page stats table (diagnostic) ----
    lines.append("")
    lines.append("PAGE STATISTICS (all pages)")
    lines.append("=" * 80)
    lines.append(f"  {'Page':<55} {'Words':>6} {'Links':>6} {'Imgs':>5} {'Title':>5} {'Desc':>5}")
    lines.append(f"  {'-'*55} {'-'*6} {'-'*6} {'-'*5} {'-'*5} {'-'*5}")
    for audit in audits:
        wc = audit.stats.get("word_count", 0)
        il = audit.stats.get("internal_links", 0)
        imgs = audit.stats.get("images", 0)
        tl = audit.stats.get("title_len", 0)
        dl = audit.stats.get("desc_len", 0)
        path_display = audit.url_path[:55]
        lines.append(f"  {path_display:<55} {wc:>6} {il:>6} {imgs:>5} {tl:>5} {dl:>5}")

    # ---- Aggregate content stats ----
    word_counts = [a.stats.get("word_count", 0) for a in audits]
    link_counts = [a.stats.get("internal_links", 0) for a in audits]
    lines.append("")
    lines.append("AGGREGATE STATS")
    lines.append("-" * 40)
    lines.append(f"  Average word count:        {sum(word_counts)/len(word_counts):.0f}")
    lines.append(f"  Median word count:         {sorted(word_counts)[len(word_counts)//2]}")
    lines.append(f"  Min word count:            {min(word_counts)}")
    lines.append(f"  Max word count:            {max(word_counts)}")
    lines.append(f"  Average internal links:    {sum(link_counts)/len(link_counts):.0f}")
    lines.append(f"  Pages with < {MIN_INTERNAL_LINKS} links:     {sum(1 for c in link_counts if c < MIN_INTERNAL_LINKS)}")
    lines.append(f"  Pages with < {MIN_WORD_COUNT} words:    {sum(1 for c in word_counts if c < MIN_WORD_COUNT)}")

    # ---- Page type distribution ----
    type_counter = Counter()
    for audit in audits:
        type_counter[determine_page_type(audit.url_path)] += 1
    lines.append("")
    lines.append("PAGE TYPE DISTRIBUTION")
    lines.append("-" * 40)
    for ptype, count in type_counter.most_common():
        lines.append(f"  {ptype:<25} {count:>5} pages")

    lines.append("")
    lines.append("=" * 80)
    lines.append("  End of SEO Audit Report")
    lines.append("=" * 80)

    return "\n".join(lines)


def print_summary(audits: list[PageAudit]):
    """Print a concise summary to stdout."""
    total = len(audits)
    passing = sum(1 for a in audits if a.is_passing)
    total_critical = sum(a.critical_count for a in audits)
    total_warnings = sum(a.warning_count for a in audits)
    total_info = sum(a.info_count for a in audits)

    print()
    print("=" * 60)
    print("  DataStackGuide SEO Audit Summary")
    print("=" * 60)
    print()
    print(f"  Pages audited:     {total}")
    print(f"  Passing (0 crit/warn): {passing}/{total} ({passing/total*100:.1f}%)")
    print(f"  CRITICAL issues:   {total_critical}")
    print(f"  WARNING issues:    {total_warnings}")
    print(f"  INFO notes:        {total_info}")
    print()

    # Category summary
    category_counts = defaultdict(lambda: {CRITICAL: 0, WARNING: 0, INFO: 0})
    for audit in audits:
        for severity, category, _ in audit.issues:
            category_counts[category][severity] += 1

    if any(c[CRITICAL] > 0 or c[WARNING] > 0 for c in category_counts.values()):
        print("  Issues by category (critical + warnings):")
        print(f"  {'Category':<25} {'CRIT':>5} {'WARN':>5}")
        print(f"  {'-'*25} {'-'*5} {'-'*5}")
        for cat, counts in sorted(category_counts.items(),
                                   key=lambda x: (x[1][CRITICAL], x[1][WARNING]),
                                   reverse=True):
            if counts[CRITICAL] > 0 or counts[WARNING] > 0:
                print(f"  {cat:<25} {counts[CRITICAL]:>5} {counts[WARNING]:>5}")
        print()

    # Top 5 critical issues
    if total_critical > 0:
        print("  Top critical issues:")
        crit_counter = Counter()
        for audit in audits:
            for severity, category, message in audit.issues:
                if severity == CRITICAL:
                    crit_counter[(category, message)] += 1
        for (cat, msg), count in crit_counter.most_common(5):
            print(f"    [{count} pages] {cat}: {msg[:70]}")
        print()

    print(f"  Full report written to: {REPORT_PATH}")
    print("=" * 60)
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def find_all_pages(dist_dir: Path) -> list[tuple[str, str]]:
    """Find all index.html files and return (filepath, url_path) tuples."""
    pages = []
    for root, dirs, files in os.walk(dist_dir):
        # Skip _astro and assets directories
        dirs[:] = [d for d in dirs if d not in ("_astro", "assets")]
        for fname in files:
            if fname == "index.html":
                filepath = os.path.join(root, fname)
                # Derive URL path from filesystem path
                rel = os.path.relpath(filepath, dist_dir)
                # e.g., "compare/clay-vs-zoominfo/index.html" -> "/compare/clay-vs-zoominfo/"
                url_path = "/" + os.path.dirname(rel).replace(os.sep, "/")
                if url_path == "/.":
                    url_path = "/"
                else:
                    url_path = url_path.rstrip("/") + "/"
                pages.append((filepath, url_path))
    return sorted(pages, key=lambda x: x[1])


def main():
    if not DIST_DIR.exists():
        print(f"ERROR: dist directory not found at {DIST_DIR}")
        sys.exit(1)

    print(f"Scanning {DIST_DIR} for HTML pages...")
    pages = find_all_pages(DIST_DIR)
    print(f"Found {len(pages)} pages to audit.")
    print()

    # Phase 1: Audit each page
    audits = []
    all_titles = defaultdict(list)
    all_descriptions = defaultdict(list)

    for i, (filepath, url_path) in enumerate(pages):
        if (i + 1) % 50 == 0 or i == 0:
            print(f"  Auditing page {i+1}/{len(pages)}: {url_path}")

        audit = audit_page(filepath, url_path)
        audits.append(audit)

        # Collect titles and descriptions for uniqueness check
        parser = SEOHTMLParser()
        with open(filepath, "r", encoding="utf-8") as f:
            parser.feed(f.read())
        if parser.title:
            all_titles[parser.title].append(url_path)
        if parser.meta_description:
            all_descriptions[parser.meta_description].append(url_path)

    print(f"  Auditing page {len(pages)}/{len(pages)}: done.")
    print()

    # Phase 2: Cross-page uniqueness checks
    print("Running cross-page uniqueness checks...")
    check_uniqueness(audits, all_titles, all_descriptions)

    # Phase 3: Generate report
    print("Generating report...")
    report = generate_report(audits)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    # Phase 4: Print summary
    print_summary(audits)


if __name__ == "__main__":
    main()
