#!/usr/bin/env python3
"""Small offline contract check for the AutoSpread plugin package."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]


def test_plugin_contract() -> None:
    manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
    assert manifest["name"] == "autospread"
    assert (ROOT / "skills/autospread/SKILL.md").is_file()
    assert (ROOT / "README.md").is_file()
    assert (ROOT / "README.zh-CN.md").is_file()
    assert (ROOT / "docs/catalog.json").is_file()


def test_cli_initializes_product_records() -> None:
    with TemporaryDirectory() as temp:
        result = subprocess.run(
            ["python3", str(ROOT / "scripts/autospread.py"), "init-context", temp],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert (Path(temp) / "product-context.md").is_file()
        assert (Path(temp) / "work-log.md").is_file()


if __name__ == "__main__":
    test_plugin_contract()
    print("structure contract: ok")
