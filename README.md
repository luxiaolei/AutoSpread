# AutoSpread

AutoSpread is a lightweight, bilingual growth operating system for AI agents. Give a capable agent a product repository, product URL, business goal, and autonomy boundary; the Lead diagnoses the largest current growth constraint, loads only the relevant playbooks, uses the connected tools, verifies real-world outcomes, and learns from the result.

It is intentionally not another multi-agent runtime. Roles are methods, not mandatory bots. One Codex/ChatGPT/Hermes/Claude-style session can perform several roles, or delegate independent work when the host supports it.

## v0.2 operating model

```text
product + goal + autonomy policy
            |
        Growth Lead
            |
    diagnose constraint
            |
  choose the smallest playbook
            |
product / funnel / monetization / SEO-GEO / content / channels / lifecycle / paid
            |
 API/MCP -> CLI -> SDK/code -> ego-browser -> human
            |
       execute + verify
            |
 activation / revenue / retention / learning
            `----> next cycle
```

## Included

- a Growth Lead router and constraint-diagnosis method;
- an explicit autonomy-policy method and editable policy template;
- project audit, customer research, CRO, monetization, lifecycle, paid acquisition and analytics playbooks;
- SEO split into foundation, GEO/answer-engine optimization, and AI-visibility measurement;
- content strategy, content/video production, channel selection and channel operations;
- a growth-experiment contract that ties work to evidence and business outcomes;
- 19 bilingual Agent Skills;
- five product workspace templates: product context, autonomy policy, capability inventory, experiment ledger, and work log;
- a machine-readable catalog of 64 reviewed capability pointers (skills, plugins, MCPs, CLIs, platforms and runtimes);
- a standard-library-only helper for validation, catalog filtering, context initialization and project-skill installation.

## Use it

In a capable session, read `skills/autospread/SKILL.md`, then provide the product repository/path, public URL, goal, and the amount of autonomy you want to grant.

```text
Read /path/to/AutoSpread/skills/autospread/SKILL.md.
Take over growth for /path/to/my-product and https://example.com.
Use the product's autonomy-policy.yaml. Start with a read-first audit and constraint diagnosis,
then propose or execute the smallest useful growth experiment within that policy.
```

Initialize the product records:

```bash
python3 scripts/autospread.py init-context /path/to/my-product/.autospread
```

Explore resources by role or keyword:

```bash
python3 scripts/autospread.py catalog --role geo-optimization
python3 scripts/autospread.py catalog --query stripe
```

Run offline checks:

```bash
python3 scripts/autospread.py validate
python3 -m pytest -q
```

See `README.zh-CN.md`, `docs/en/operating-model.md`, and `docs/zh-CN/operating-model.md` for the full model.
