---
name: seo-foundation
description: Audit and improve crawlability, indexability, information architecture, page intent, structured data, performance, and search measurement.
---

# SEO Foundation

## Survey

1. Identify priority audiences, commercial or informational intents, current landing pages, and known queries.
2. Inspect robots, sitemaps, canonicals, redirects, status codes, rendered textual content, metadata, internal links, duplicate/faceted URLs, and indexability.
3. Read Search Console or equivalent first-party data when available. Distinguish demand, impressions, rank, CTR, landing behavior, and conversion.
4. Check page experience and performance only where it can affect usability or discovery; do not optimize synthetic scores without a user or crawl reason.

## Conditional specialist routing

After the base audit, route only when evidence requires it:

- schema/sitemap/image issues or release regression -> `seo-site-integrity`;
- technically sound page but wrong search intent/page type -> `search-experience`;
- physical/service-area/multi-location business -> `local-seo`;
- multilingual or multi-region URL sets -> `international-seo`;
- store/catalog/product commerce -> `ecommerce-seo`;
- site must be operated by user-triggered AI agents -> `agent-readiness`.

Do not run every specialist on every site.

## Implement and tune

- map one primary intent per important page while allowing useful subtopics;
- fix discoverability through navigation and internal links;
- keep important claims and answers in indexable text;
- use structured data only when it matches visible content and supported semantics;
- create new pages only when they add distinct user value, not merely keyword variants;
- preserve canonical and redirect behavior during growth changes.

## Verify

Re-crawl affected URLs, inspect live rendered pages, verify schema where relevant, and define the Search Console observation window. Never promise indexing or ranking.
