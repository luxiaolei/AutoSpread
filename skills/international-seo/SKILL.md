---
name: international-seo
description: Design and validate multilingual and multi-region search architecture, hreflang, localization, canonicals, and regional experience.
---

# International SEO

Use for products serving multiple languages or regions with distinct URLs/content.

## Architecture

1. Inventory locale/region variants and decide whether the business truly needs language-only, country-specific, or both targeting.
2. Map equivalent pages across locales; do not create hreflang relationships between pages that are not meaningful equivalents.
3. Verify each locale has a stable canonical URL and that alternate relationships are reciprocal and internally consistent.
4. Use valid BCP 47-style language/script/region combinations supported by search engines; validate exact codes rather than guessing.
5. Use `x-default` when a genuine fallback or selector experience exists; it is not mandatory for every site.
6. Choose HTML, HTTP header, or XML sitemap hreflang implementation based on maintainability and page type; avoid conflicting duplicate implementations.

## Localization quality

International SEO is not translation-only. Validate local terminology, units, currency, pricing availability, legal/compliance notices, examples, proof, support, shipping/service availability, CTA destination, and local search intent. Avoid automatic IP redirects that make alternate versions hard to crawl or override user choice without a clear escape.

## Verify

Check self/return relationships, canonical alignment, HTTP status, indexability, locale content, and regional search behavior with observed data where available. Record market/date/device when SERP differences matter.

Route local physical-business issues to `local-seo`; route sitewide structural problems to `seo-site-integrity`.
