---
name: conversion-optimization
description: Diagnose and improve landing, signup, onboarding, activation, paywall, and upgrade flows using observed behavior and bounded experiments.
---

# Conversion Optimization

## Diagnose before changing

1. Define the exact funnel step, denominator, target segment, and business outcome.
2. Reproduce the flow on the real product with the appropriate device/account state; capture errors, ambiguity, latency, trust gaps, unnecessary work, and mismatched expectations.
3. Combine product behavior, funnel data, replay/session evidence, support/customer evidence, and technical failures. Missing denominators or broken instrumentation are first-class issues.
4. Check upstream traffic quality and downstream activation/revenue so a local conversion gain does not hide worse users.

## Experiment

Use `growth-experiment`: state the friction hypothesis, one primary change, primary metric, diagnostics, guardrails, observation logic, and rollback. For low traffic, use qualitative or sequential evidence without claiming randomized certainty.

## Implement and verify

Prefer preview/staging first, test happy and failure paths, preserve analytics events, then follow the autonomy policy for production rollout. Verify the live state after deploy and start the observation window only when instrumentation and treatment are confirmed.
