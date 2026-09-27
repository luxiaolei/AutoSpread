---
name: growth-experiment
description: Turn a growth hypothesis into a bounded, measurable experiment with primary metric, guardrails, observation window, and decision rule.
---

# Growth Experiment

Use before material changes or whenever multiple plausible growth levers compete for attention.

## Experiment contract

Record before launch:

- hypothesis and evidence;
- target segment and funnel stage;
- intervention and control/baseline when available;
- primary outcome metric and exact definition;
- diagnostic metrics and guardrails;
- attribution identifiers or event requirements;
- minimum observation window or sample logic;
- cost/budget limit;
- stop, rollback, continue, or scale rule;
- owner and autonomy-policy decision.

## Execution

Change as few major variables as practical. Verify instrumentation and the external action before starting the observation clock. When traffic is too low for a formal A/B test, use qualitative evidence, before/after cohorts, interviews, replay, or sequential tests without pretending they provide randomized causal certainty.

## Closeout

Return observed result, data-quality limitations, causal confidence, cost, downstream quality, decision, and what changed in the product/growth model. `insufficient evidence` is a valid result.
