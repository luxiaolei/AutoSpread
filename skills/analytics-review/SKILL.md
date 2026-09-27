---
name: analytics-review
description: Validate data, explain metric movement, evaluate experiments, and connect acquisition activity to activation, revenue, and retention without overstating causality.
---

# Analytics and Review

## Establish the metric contract

Before calculating, define metric name, business meaning, event/formula, population, denominator, attribution logic, period/timezone, source of truth, and expected latency.

## Validate

Check event/schema changes, duplicates, missing periods, bot/internal traffic, refunds/cancellations where relevant, identity joins, campaign parameters, and differences between analytics and billing/search sources. Resolve material conflicts before using the data for a decision.

## Analyze

- distinguish volume from rate and mix changes;
- segment by acquisition source, landing page, cohort, device/region only when useful and sufficiently supported;
- trace downstream quality from impression/click -> qualified visit -> signup -> activation -> payment -> retention when IDs allow;
- separate correlation, before/after association, and controlled causal evidence;
- include cost and opportunity cost when choosing between growth levers.

## Close the loop

Compare to the predeclared experiment metric and guardrails. Return calculations, source links/queries, limitations, causal confidence, and a continue/stop/rollback/scale/learn decision. `insufficient evidence` is valid.
