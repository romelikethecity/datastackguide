/**
 * Build a BreadcrumbList schema from breadcrumb items.
 */
export function buildBreadcrumbSchema(items: { label: string; href?: string }[]) {
  return {
    "@type": "BreadcrumbList",
    "itemListElement": items.map((item, i) => ({
      "@type": "ListItem",
      "position": i + 1,
      "name": item.label,
      ...(item.href ? { "item": `https://datastackguide.com${item.href}` } : {})
    }))
  };
}
