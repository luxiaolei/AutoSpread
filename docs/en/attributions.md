# Method attributions

AutoSpread is MIT licensed and intentionally avoids vendoring third-party skill libraries. It may adapt general workflow ideas, routing patterns, and quality gates discovered during source review.

## Claude SEO

`AgriciDaniel/claude-seo` (MIT) materially informed AutoSpread v0.3's conditional SEO specialist layer. In particular, AutoSpread adopted the general ideas of:

- routing specialist checks only when site/business signals require them;
- treating SEO drift as a baseline/diff problem after deployments;
- separating search-experience/page-type intent analysis from technical SEO;
- treating local, international/hreflang, ecommerce, schema/sitemap/images, and agent operability as distinct conditional concerns;
- keeping GEO/AI citability separate from agent-operability;
- enriching audits with external providers only when configured and budgeted.

AutoSpread does not copy Claude SEO's scripts, scores, proprietary datasets, or third-party statistical claims. Where the projects differ, AutoSpread prefers host-independent methods, explicit business-outcome experiments, conservative evidence language, and its own autonomy/capability model.

Source: https://github.com/AgriciDaniel/claude-seo
