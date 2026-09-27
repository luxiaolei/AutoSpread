---
name: project-audit
description: Establish product, audience, funnel, monetization, measurement, access, and deployment facts before choosing growth work.
---

# Project Audit

Use on initial handoff or when the product changed enough that old growth assumptions may be stale. Audit is read-first: do not mutate production during diagnosis.

## Inspect

1. Repository, README/docs, architecture, deployment config, public product pages, pricing, signup/onboarding, core workflow, and billing path when accessible.
2. Existing product context, autonomy policy, experiments, work log, analytics, search data, customer feedback, issues/support, and known campaigns.
3. Current acquisition -> signup -> activation -> payment -> retention path, including unmeasured steps and inconsistent definitions.
4. Product claims versus what the implementation and public evidence actually support.
5. Operational capability: code/deploy, analytics, search, payments, publishing, browser, content, and the permission scope of each.

## Classify findings

For each finding record: observed fact, evidence/source, user/business impact, confidence, likely owner/skill, effort, reversibility, and whether it blocks trustworthy measurement.

Prioritize measurement blockers and severe product/funnel failures before increasing acquisition. Do not mistake missing data for poor performance.

## Deliver

Return a compact product model, funnel map, measurement map, access map, verified claims, unknowns, top constraints/hypotheses, and the smallest safe next investigation or experiment. Hand the constraint decision to `growth-strategy`.
