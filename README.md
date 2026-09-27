# AutoSpread

AutoSpread is a lightweight Codex plugin for organizing product growth work.
It gives one session a Growth Lead method, reusable role skills, tool-selection
rules, and evidence-based delivery checks. It does not require a message bus,
database, always-on team, or a particular marketing platform.

## What is included

- one Lead skill that chooses the smallest useful workflow;
- ten focused skills for audits, research, SEO/GEO, conversion, content,
  channels, analytics, lifecycle work, and paid acquisition;
- role and delegation guidance in `skills/autospread/references/`;
- bilingual quick-start guides and product-record templates;
- a source-backed, machine-readable resource catalog;
- a standard-library-only helper for validation, catalog filtering, context
  initialization, and project skill installation.

## Use it

Read `skills/autospread/SKILL.md` in a Codex session and give it the product
path. The Lead first reads the product record, checks the available tools, and
chooses only the relevant role skills. Small tasks stay in the current session;
independent work can be delegated when the host supports it.

```text
Read /path/to/AutoSpread/skills/autospread/SKILL.md.
Act as my Growth Lead for /path/to/my-product and work in Chinese.
Start with a product audit. Do not publish, spend money, change production,
or create scheduled jobs without explicit approval.
```

Run the offline checks with:

```bash
python3 scripts/autospread.py validate
python3 tests/test_structure.py
```

The Chinese documentation is in `README.zh-CN.md` and `docs/zh-CN/`.
