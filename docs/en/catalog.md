# Resource catalog

The machine-readable catalog is in [`../catalog.json`](../catalog.json). AutoSpread v0.3 contains 67 reviewed capability pointers grouped by role. They include reusable Agent Skills, official MCP/API surfaces, CLIs, content/publishing tools, analytics systems and optional runtimes.

A catalog item is a pointer, not an installed dependency and not proof of account access. Before execution, verify current provider documentation, permissions, pricing, platform policy and the user's autonomy policy.

High-signal resources include the Corey AI SEO skill, Aaron Marketing Skills SEO/GEO lifecycle, UnifAPI AI-visibility methods, Google Search's official AI-feature guidance, ScrapeCreators social research skills, Social Media Skills, official Cloudflare/Supabase/Stripe/Vercel agent integrations, and the Claude SEO specialist/extension ecosystem.

Filter by role or search all metadata:

```bash
python3 scripts/autospread.py catalog --role ai-visibility
python3 scripts/autospread.py catalog --query cloudflare
```
