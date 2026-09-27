# Quick start

1. Initialize the product workspace with `python3 scripts/autospread.py init-context PATH/.autospread`. This creates product context, autonomy policy, capability inventory, experiment ledger, and work log.
2. Fill only the facts you already know. Keep unknowns unknown.
3. Read `skills/autospread/SKILL.md` in the agent session that will act as Growth Lead.
4. Give the Lead the repository/path, public URL, business goal, time horizon, and any explicit autonomy changes.
5. Ask for a read-first project audit and growth-constraint diagnosis. Do not force a channel before diagnosis.
6. Let the Lead load only the playbooks needed for the current constraint.
7. For material actions, record an experiment and check `autonomy-policy.yaml` before execution.
8. Prefer API/MCP, CLI, and deterministic code for repeatable work; use `ego-browser` for UI-only/logged-in workflows.
9. Verify external state after writes and store evidence/IDs in the work log.
10. Reassess the constraint after the observation window.

Install all AutoSpread skills into another local project:

```bash
python3 scripts/autospread.py install /path/to/project
```

The installer refuses to overwrite existing skill directories unless `--force` is used.
