---
name: autonomy-policy
description: Define and enforce what AutoSpread may change autonomously, what requires approval, and what is forbidden.
---

# Autonomy Policy

Use this before any action that can change production, pricing, spend, customer communication, data, credentials, billing, or scheduled work.

## Method

1. Read `autonomy-policy.yaml` from the product workspace when present.
2. Classify the intended action by domain: product, website, deployment, pricing, paid spend, social publishing, email, billing, customer data, credentials, or scheduling.
3. Determine whether the action is `autonomous`, `approval_required`, or `forbidden`.
4. Enforce numeric limits such as price-change percentage, daily/monthly spend, recipient count, rollout percentage, or experiment duration.
5. Require a rollback path for production, pricing, routing, or data-changing work when reversal is feasible.
6. If the requested action exceeds the policy, stop only that action and return the exact approval or policy change needed.
7. Never expand authority by inference. Silence is not approval.

Record the policy decision in the work log for any material external action.
