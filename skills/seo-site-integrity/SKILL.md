---
name: seo-site-integrity
description: Audit and protect SEO-critical site integrity across schema, sitemaps, images, and post-deploy drift.
---

# SEO Site Integrity

Use when the site needs structural SEO QA, after meaningful deploys, or when rankings/traffic changed after a site modification. This skill combines four tightly related integrity checks without turning each check into a mandatory standalone agent.

## Route by mode

- **schema**: detect structured data, validate syntax and entity relationships, confirm markup matches visible truthful content, and check whether the chosen type is currently useful for the search surface.
- **sitemap**: discover declared and common sitemap locations, validate URLs and canonical/indexability consistency, and compare important crawlable pages against sitemap coverage.
- **images**: check descriptive alt text where appropriate, decorative-image handling, intrinsic dimensions/CLS risk, responsive delivery, LCP treatment, formats/compression, filenames, and image discoverability.
- **drift**: capture or compare a known-good baseline for SEO-critical fields before/after deploys.

## Drift baseline

For important templates/pages, record at least: HTTP status, title, meta description, canonical, robots directives, H1/H2 structure, key JSON-LD types/content hash, important Open Graph fields, rendered main-content hash, and relevant performance signals. Normalize URLs before comparison.

Classify changes as:

- **critical**: indexability/status/canonical/robots changes that can remove or redirect important pages;
- **warning**: schema, heading, metadata, content or performance regressions that need investigation;
- **info**: intentional or low-risk changes to review.

Never infer causality from temporal overlap alone. A drift is a lead to investigate, not proof that it caused a traffic change.

## Quality rules

- Prefer JSON-LD when appropriate, but never generate facts that are not visible or verifiable.
- Do not add structured data solely because a schema type exists; check current search support and business value.
- A sitemap should contain preferred canonical, indexable destinations rather than redirects, noindex URLs, or duplicate variants.
- `lastmod` should represent meaningful page changes rather than being regenerated mechanically.
- Do not lazy-load the primary above-the-fold/LCP image; do use dimensions/aspect ratio to reduce layout shift.
- Avoid arbitrary image byte-size rules as universal truths; optimize against actual dimensions, quality, delivery and performance.

## Verify

After fixes, re-fetch rendered pages and external files, revalidate schema/sitemap, compare the drift baseline, and record the exact changed fields. Feed conversion-facing layout/intent issues to `search-experience` or `conversion-optimization`.
