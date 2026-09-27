# Tool selection and execution routing

Read `capabilities.yaml` when present, then choose the least fragile authorized capability that can both perform and verify the action.

## Default order

1. Official API or MCP with scoped permissions.
2. Official/provider CLI.
3. SDK or deterministic code using an official API.
4. Approved `ego-browser` session for authenticated UI work or flows without a reliable structured interface.
5. Human handoff when the action cannot be safely or legally automated.

This is a preference order, not an absolute rule. A mature CLI may be safer than a beta MCP; a browser may be required for an OAuth consent or a UI-only workflow.

## Browser rule

`ego-browser` is the universal UI actuator when available. Use it for visual audits, logged-in dashboards, submissions, form workflows, end-to-end signup/payment checks, and services without a suitable API/CLI. Reuse a task space for one goal, inspect state before retrying, and capture the final observable result. A shared login state is convenience, not a permission boundary.

## Examples

| Need | Preferred route | Browser role |
| --- | --- | --- |
| GitHub branch/PR | git / GitHub API or MCP | inspect UI-only settings if needed |
| Cloudflare DNS/Workers | scoped Cloudflare API/MCP or Wrangler | OAuth or UI-only configuration fallback |
| Vercel deploy/logs | Vercel CLI/API/MCP according to supported capability | UI-only settings or visual deployment check |
| Supabase data/schema | project-scoped, preferably read-only MCP/CLI for analysis; migrations for changes | dashboard-only configuration fallback |
| Stripe revenue/pricing | restricted Stripe MCP/API/CLI | dashboard check when needed; never treat browser login as unlimited billing authority |
| Product analytics | PostHog/GA/warehouse API | dashboard exploration if structured access is missing |
| Search performance | Search Console API/export | URL inspection or search-surface spot checks |
| Social publishing | authorized official API/CLI or approved publisher | UI fallback only where platform rules permit |
| Directory submission | provider API if available | often an appropriate browser workflow |
| Video | deterministic renderer/CLI for repeatable assets | upload/configuration fallback |

## External-action verification

Before retrying any ambiguous write, query external state. Record external ID/URL, account, timestamp, operation key, and verification method when available. Never infer access from an installed skill, plugin, browser session, or tool catalog.
