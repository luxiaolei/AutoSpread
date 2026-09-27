# Quick start

1. Copy `templates/product-context.md` and `templates/work-log.md` into the
   product workspace, or run `python3 scripts/autospread.py init-context PATH`.
2. Read `skills/autospread/SKILL.md` in a Codex session.
3. Ask for an audit with a scope and safety constraints.
4. Load only the role skill required by the next step.
5. Record evidence and external action status in the work log.

Install the Lead skill into another local workspace with:

```bash
python3 scripts/autospread.py install /path/to/project
```

The installer refuses to overwrite an existing skill unless `--force` is used.
