#!/usr/bin/env python3
"""Small standard-library helper for the AutoSpread plugin."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_manifest() -> dict:
    return json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))


def validate() -> int:
    errors: list[str] = []
    manifest = load_manifest()
    for relative in manifest.get("skills", []):
        skill = ROOT / relative
        if not (skill / "SKILL.md").is_file():
            errors.append(f"missing {relative}/SKILL.md")
        if not (skill / "SKILL.zh-CN.md").is_file():
            errors.append(f"missing {relative}/SKILL.zh-CN.md")
    catalog = json.loads((ROOT / "docs/catalog.json").read_text(encoding="utf-8"))
    if len(catalog.get("resources", [])) != 49:
        errors.append("catalog must contain 49 resources")
    for relative in (
        "README.md",
        "README.zh-CN.md",
        "docs/en/quickstart.md",
        "docs/zh-CN/quickstart.md",
        "templates/product-context.md",
        "templates/work-log.md",
    ):
        if not (ROOT / relative).is_file():
            errors.append(f"missing {relative}")
    if errors:
        print("validation: failed")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"validation: ok ({len(manifest['skills'])} skills, {len(catalog['resources'])} resources)")
    return 0


def catalog(role: str | None) -> int:
    data = json.loads((ROOT / "docs/catalog.json").read_text(encoding="utf-8"))
    resources = data["resources"]
    if role:
        resources = [item for item in resources if item["role"] in {role, "all"}]
    print(json.dumps(resources, ensure_ascii=False, indent=2))
    return 0


def init_context(target: Path, force: bool) -> int:
    target = target.expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    files = {"product-context.md": ROOT / "templates/product-context.md", "work-log.md": ROOT / "templates/work-log.md"}
    existing = [name for name in files if (target / name).exists()]
    if existing and not force:
        print(f"refusing to overwrite: {', '.join(existing)}", file=sys.stderr)
        return 2
    for name, source in files.items():
        shutil.copyfile(source, target / name)
    print(f"initialized: {target}")
    return 0


def install(target: Path, force: bool) -> int:
    target = target.expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    destination = target / ".codex" / "skills"
    destination.mkdir(parents=True, exist_ok=True)
    for source in sorted((ROOT / "skills").iterdir()):
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
    print(f"installed {len(list((ROOT / 'skills').iterdir()))} skills: {destination}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="autospread")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    catalog_parser = subparsers.add_parser("catalog")
    catalog_parser.add_argument("--role")
    for name in ("init-context", "install"):
        command = subparsers.add_parser(name)
        command.add_argument("target", type=Path)
        command.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)
    if args.command == "validate":
        return validate()
    if args.command == "catalog":
        return catalog(args.role)
    if args.command == "init-context":
        return init_context(args.target, args.force)
    return install(args.target, args.force)


if __name__ == "__main__":
    raise SystemExit(main())
