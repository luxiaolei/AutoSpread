---
name: agent-readiness
description: Make a website usable by user-triggered AI agents and machine clients without confusing agent operability with GEO ranking.
---

# Agent Readiness

This is distinct from GEO. GEO asks whether answer engines can understand/cite content; agent readiness asks whether an AI agent acting for a user can reliably read, navigate, fill, submit, and confirm workflows.

## Foundation

1. Prefer accessible semantic HTML, meaningful labels/roles, keyboard-operable controls, stable confirmation states, and content available without fragile hover-only interactions.
2. Ensure important public content is available in rendered/server-delivered form appropriate to the site, and that critical actions expose deterministic success/failure states.
3. Separate access policy by purpose: search/indexing, model training, and user-triggered agents are not the same category. Do not infer one policy from another bot's robots status.
4. Test WAF/CAPTCHA/login behavior only when authorized, and report what was tested rather than claiming universal agent access.
5. Protect private or consequential actions with authentication and explicit confirmation rather than robots.txt.

## Optional enhancements

Machine-readable Markdown variants, discovery documents, API catalogs, agent cards, or WebMCP-style tools may improve some agent workflows, but their support is platform- and browser-dependent. Treat them as optional interoperability experiments, not SEO prerequisites or guaranteed traffic/citation levers.

For agent-callable transactional tools, expose the smallest real operation, accurate descriptions, clear consequential-action metadata, validation, confirmation, logging, and idempotency where appropriate. Never write tool descriptions that instruct an agent to bypass user confirmation.

## Verify

Run the real workflow with an approved browser/agent when available: discover -> navigate -> fill/select -> submit -> observe confirmation. Capture failures in accessibility, dynamic rendering, auth/WAF, ambiguous state, or unsafe tool design. Route ranking/citation questions back to `geo-optimization` and `ai-visibility`.
