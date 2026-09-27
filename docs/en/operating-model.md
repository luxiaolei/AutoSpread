# AutoSpread operating model

## What the Lead receives

A normal handoff is: product repository/path, public product URL, a business goal and horizon, connected capabilities (for example GitHub, Cloudflare, Vercel, Supabase, Stripe, analytics, publishing or content tools), an autonomy policy, and a capability inventory that records available interfaces/scopes without storing secrets.

## What happens first

The Lead does not start by posting. It builds or refreshes the product context and maps acquisition -> signup -> activation -> payment -> retention. It checks measurement and product readiness, then uses `growth-strategy` to identify the strongest current constraint.

If acquisition is the constraint, the Lead may route to SEO/GEO, content, channel selection, partnerships, launch or paid acquisition. If conversion is the constraint, it routes to CRO/onboarding. If monetization is the constraint, pricing/packaging is valid. If product capability is the real blocker, growth engineering/product work may come before promotion.

## Search and GEO

AutoSpread separates three jobs:

1. `seo-foundation`: crawl/index, architecture, intent, internal linking, structured data, Search Console and technical search health.
2. `geo-optimization`: useful, factual, extractable and citable content for answer engines without pretending there is a universal GEO ranking hack.
3. `ai-visibility`: a fixed, versioned question/prompt panel that separately tracks mentions, owned-domain citations, third-party citations and competitors over time.

For Google AI Overviews and AI Mode, use Google's own guidance as the guardrail: foundational SEO remains relevant and there is no required special AI markup/file. Optional agent-readable artifacts are experiments, not guarantees.

## Content and distribution

Customer problems and product evidence create content themes. A strong insight can become a website page, docs/tutorial, comparison, founder post, X/LinkedIn variant, community contribution, long demo, short video, newsletter or another channel-native asset. The Lead chooses channels by audience and economics rather than publishing everywhere.

## Autonomy

The policy controls what can happen without another user message. It can allow autonomous website copy, SEO/GEO work, previews, channel strategy or bounded pricing tests while requiring approval for production deploys, live billing changes, paid budget, customer-data actions or other consequential work. Users can intentionally broaden those boundaries.

## Tool routing

Default: official/scoped API or MCP -> provider CLI -> SDK/code -> `ego-browser` -> human. Browser automation is the fallback UI actuator for authenticated dashboards, forms, submissions and UI-only work. Browser login state does not itself grant authority.

## Learning loop

Every meaningful change should have a hypothesis, primary outcome, guardrails, observation logic and stop/rollback/scale rule. Publication or deployment is not the end of the task. The loop closes on activation, revenue, retention or the explicitly chosen business outcome, then the Lead diagnoses the next constraint.
