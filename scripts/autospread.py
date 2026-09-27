#!/usr/bin/env python3
"""Small standard-library helper for the AutoSpread plugin."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTEXT_TEMPLATES = (
    "product-context.md",
    "autonomy-policy.yaml",
    "experiment-ledger.md",
    "capabilities.yaml",
    "work-log.md",
)
REQUIRED_CATALOG_RESOURCES = {
    "marketingskills",
    "Corey AI SEO",
    "Aaron Marketing Skills",
    "UnifAPI AI Visibility",
    "Google AI features guidance",
    "ego-browser",
    "Cloudflare API MCP",
    "Vercel Plugin",
    "Supabase MCP",
    "Stripe MCP",
}


def load_manifest() -> dict:
    return json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))


def load_catalog() -> dict:
    return json.loads((ROOT / "docs/catalog.json").read_text(encoding="utf-8"))


def validate() -> int:
    errors: list[str] = []
    manifest = load_manifest()
    skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    seen_skills: set[str] = set()
    for skill in skills:
        relative = skill.relative_to(ROOT).as_posix()
        if relative in seen_skills:
            errors.append(f"duplicate skill path: {relative}")
        seen_skills.add(relative)
        for name in ("SKILL.md", "SKILL.zh-CN.md"):
            path = skill / name
            if not path.is_file():
                errors.append(f"missing {relative}/{name}")
                continue
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---\n") or "description:" not in text.split("---", 2)[1]:
                errors.append(f"invalid frontmatter: {relative}/{name}")

    catalog = load_catalog()
    resources = catalog.get("resources", [])
    names = [item.get("name") for item in resources]
    if len(names) != len(set(names)):
        errors.append("catalog resource names must be unique")
    missing_required = sorted(REQUIRED_CATALOG_RESOURCES - set(names))
    if missing_required:
        errors.append("catalog missing required resources: " + ", ".join(missing_required))
    for item in resources:
        for key in ("name", "role", "type", "url", "status"):
            if not item.get(key):
                errors.append(f"catalog resource missing {key}: {item.get('name', '<unnamed>')}")

    required_files = [
        "README.md",
        "README.zh-CN.md",
        "docs/en/quickstart.md",
        "docs/zh-CN/quickstart.md",
        "docs/en/operating-model.md",
        "docs/zh-CN/operating-model.md",
        "docs/catalog.json",
        *[f"templates/{name}" for name in CONTEXT_TEMPLATES],
    ]
    for relative in required_files:
        if not (ROOT / relative).is_file():
            errors.append(f"missing {relative}")

    if errors:
        print("validation: failed")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"validation: ok ({len(skills)} skills, {len(resources)} resources, {len(CONTEXT_TEMPLATES)} context templates)")
    return 0


def catalog(role: str | None, query: str | None) -> int:
    resources = load_catalog()["resources"]
    if role:
        resources = [item for item in resources if item["role"] in {role, "all"}]
    if query:
        needle = query.casefold()
        resources = [
            item for item in resources
            if needle in json.dumps(item, ensure_ascii=False).casefold()
        ]
    print(json.dumps(resources, ensure_ascii=False, indent=2))
    return 0


def init_context(target: Path, force: bool) -> int:
    target = target.expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    files = {name: ROOT / "templates" / name for name in CONTEXT_TEMPLATES}
    existing = [name for name in files if (target / name).exists()]
    if existing and not force:
        print(f"refusing to overwrite: {', '.join(existing)}", file=sys.stderr)
        return 2
    for name, source in files.items():
        shutil.copyfile(source, target / name)
    print(f"initialized {len(files)} context files: {target}")
    return 0


def install(target: Path, force: bool) -> int:
    target = target.expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    destination = target / ".codex" / "skills"
    destination.mkdir(parents=True, exist_ok=True)
    sources = [p for p in sorted((ROOT / "skills").iterdir()) if p.is_dir() or p.is_symlink()]
    for source in sources:
        if source.is_symlink():
            print(f"refusing symlink source: {source}", file=sys.stderr)
            return 2
        dest = destination / source.name
        if dest.exists() or dest.is_symlink():
            if not force:
                print(f"refusing to overwrite: {dest}", file=sys.stderr)
                return 2
            if dest.is_dir() and not dest.is_symlink():
                shutil.rmtree(dest)
            else:
                dest.unlink()
        shutil.copytree(source, dest)
    print(f"installed {len(sources)} skills: {destination}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="autospread")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    catalog_parser = subparsers.add_parser("catalog")
    catalog_parser.add_argument("--role")
    catalog_parser.add_argument("--query")
    for name in ("init-context", "install"):
        command = subparsers.add_parser(name)
        command.add_argument("target", type=Path)
        command.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)
    if args.command == "validate":
        return validate()
    if args.command == "catalog":
        return catalog(args.role, args.query)
    if args.command == "init-context":
        return init_context(args.target, args.force)
    return install(args.target, args.force)


if __name__ == "__main__":
    raise SystemExit(main())
