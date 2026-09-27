#!/usr/bin/env python3
"""Offline contract checks for the AutoSpread plugin package."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CONTEXT = {
    "product-context.md",
    "autonomy-policy.yaml",
    "experiment-ledger.md",
    "capabilities.yaml",
    "work-log.md",
}
EXPECTED_SKILLS = {
    "autospread",
    "project-audit",
    "growth-strategy",
    "autonomy-policy",
    "customer-research",
    "seo-geo",
    "seo-foundation",
    "geo-optimization",
    "ai-visibility",
    "conversion-optimization",
    "monetization-pricing",
    "content-strategy",
    "content-video",
    "channel-selection",
    "channel-operations",
    "growth-experiment",
    "analytics-review",
    "lifecycle-operations",
    "paid-acquisition",
}


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", str(ROOT / "scripts/autospread.py"), *args],
        capture_output=True,
        text=True,
    )


def test_plugin_contract() -> None:
    manifest = json.loads((ROOT / "plugin.json").read_text())
    assert manifest["name"] == "autospread"
    assert manifest["version"] == "0.2.0"
    assert manifest["$schema"].endswith("plugin.schema.json")
    compat = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
    assert compat["skills"] == "./skills/"
    skill_names = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    assert skill_names == EXPECTED_SKILLS
    for name in EXPECTED_SKILLS:
        assert (ROOT / "skills" / name / "SKILL.md").is_file()
        assert (ROOT / "skills" / name / "SKILL.zh-CN.md").is_file()
    assert (ROOT / ".agents/plugins/marketplace.json").is_file()
    assert (ROOT / "README.md").is_file()
    assert (ROOT / "README.zh-CN.md").is_file()
    assert (ROOT / "docs/en/operating-model.md").is_file()
    assert (ROOT / "docs/zh-CN/operating-model.md").is_file()
    assert (ROOT / "evals/scenarios.json").is_file()


def test_validate_command() -> None:
    result = run_cli("validate")
    assert result.returncode == 0, result.stderr + result.stdout
    assert "19 skills" in result.stdout
    assert "64 resources" in result.stdout


def test_cli_initializes_product_records() -> None:
    with TemporaryDirectory() as temp:
        result = run_cli("init-context", temp)
        assert result.returncode == 0
        assert {p.name for p in Path(temp).iterdir()} == EXPECTED_CONTEXT


def test_cli_refuses_context_overwrite() -> None:
    with TemporaryDirectory() as temp:
        assert run_cli("init-context", temp).returncode == 0
        second = run_cli("init-context", temp)
        assert second.returncode == 2
        assert "refusing to overwrite" in second.stderr


def test_catalog_has_specialized_geo_and_platform_resources() -> None:
    catalog = json.loads((ROOT / "docs/catalog.json").read_text())
    assert catalog["schema_version"] == 2
    assert len(catalog["resources"]) == 64
    names = {item["name"] for item in catalog["resources"]}
    for required in (
        "Corey AI SEO",
        "Aaron Marketing Skills",
        "UnifAPI AI Visibility",
        "Google AI features guidance",
        "Cloudflare API MCP",
        "Vercel Plugin",
        "Supabase MCP",
        "Stripe MCP",
        "ScrapeCreators Social Research Skills",
        "Social Media Skills",
    ):
        assert required in names


def test_catalog_query_and_role_filter() -> None:
    query = run_cli("catalog", "--query", "stripe")
    assert query.returncode == 0
    payload = json.loads(query.stdout)
    assert {item["name"] for item in payload} >= {"Stripe", "Stripe MCP", "Stripe Agent Skills"}

    role = run_cli("catalog", "--role", "ai-visibility")
    assert role.returncode == 0
    payload = json.loads(role.stdout)
    assert any(item["name"] == "UnifAPI AI Visibility" for item in payload)


def test_project_skill_install_and_overwrite_guard() -> None:
    with TemporaryDirectory() as temp:
        first = run_cli("install", temp)
        assert first.returncode == 0
        installed = Path(temp) / ".codex" / "skills"
        assert {p.name for p in installed.iterdir() if p.is_dir()} == EXPECTED_SKILLS
        second = run_cli("install", temp)
        assert second.returncode == 2
        assert "refusing to overwrite" in second.stderr


def test_marketplace_points_to_local_checkout() -> None:
    market = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
    assert market["name"] == "autospread"
    plugin = market["plugins"][0]
    assert plugin["name"] == "autospread"
    assert plugin["source"] == {"source": "local", "path": "./"}
    assert plugin["policy"]["installation"] == "AVAILABLE"


def test_behavior_scenarios_are_valid() -> None:
    payload = json.loads((ROOT / "evals/scenarios.json").read_text())
    scenarios = payload["scenarios"]
    assert len(scenarios) >= 8
    assert len({item["id"] for item in scenarios}) == len(scenarios)
    for item in scenarios:
        assert item["prompt"]
        assert item["must"]
        assert item["must_not"]


def test_autonomy_policy_is_conservative_by_default() -> None:
    text = (ROOT / "templates/autonomy-policy.yaml").read_text()
    assert "default: approval_required" in text
    assert "payout_or_transfer: forbidden" in text
    assert "broaden_permissions: forbidden" in text


if __name__ == "__main__":
    test_plugin_contract()
    test_validate_command()
    print("structure contract: ok")
