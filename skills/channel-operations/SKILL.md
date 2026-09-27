---
name: channel-operations
description: Prepare, publish, schedule, and verify approved content through authorized APIs, CLIs, or UI automation while preserving external evidence.
---

# Channel Operations

Use after `channel-selection` and content approval.

## Before action

Confirm channel/account, target audience, asset version, destination URL, campaign/UTM identifiers, approval/autonomy status, platform requirements, and whether the tool can verify the result.

## Tool routing

Prefer official API/MCP -> provider CLI -> SDK/code -> approved `ego-browser` UI -> human handoff. Use the browser for authenticated UI work that lacks a reliable structured interface, not to bypass platform rules.

## Execute safely

- use an idempotency or operation key when available;
- serialize actions when the platform/account cannot safely accept concurrent writes;
- after ambiguous timeout, query external state before retrying;
- save external post/video/submission/schedule identifiers and canonical URLs;
- distinguish draft, scheduled, submitted, published, rejected, and unknown states;
- for community surfaces, participate according to community/platform norms rather than posting disguised automation spam.

## Verify

A task is complete only after the external system shows the intended state. Record timestamp, account, external ID/URL, asset ID, campaign/landing destination, and verification method.
