#!/usr/bin/env python3
"""Record a dismissed Data Analytics plugin-install suggestion."""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Remember that Data Analytics should not suggest a plugin install again."
    )
    parser.add_argument("--plugin-id", required=True)
    parser.add_argument("--tool-type", default="plugin")
    parser.add_argument("--reason", default="user_dismissed_request_plugin_install")
    parser.add_argument("--agent-home", "--codex-home", dest="agent_home", type=Path, default=None, help="Optional host data root; --codex-home is a legacy explicit alias.")
    parser.add_argument("--state-dir", type=Path, default=None)
    return parser.parse_args()


def default_agent_home() -> Path:
    env_home = os.environ.get("AGENT_HOME")
    if env_home:
        return Path(env_home).expanduser()
    return Path.cwd() / ".agent-skills"


def state_dir_from_args(args: argparse.Namespace) -> Path:
    if args.state_dir:
        return args.state_dir.expanduser()
    agent_home = args.agent_home.expanduser() if args.agent_home else default_agent_home()
    return agent_home / "state/plugins/data-analytics"


def read_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"suppressed_plugin_installs": []}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid plugin-install-suppressions.json: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit("invalid plugin-install-suppressions.json: root must be an object")
    return data


def main() -> int:
    args = parse_args()
    state_dir = state_dir_from_args(args)
    state_dir.mkdir(parents=True, exist_ok=True)
    state_path = state_dir / "plugin-install-suppressions.json"
    state = read_state(state_path)
    entries = state.get("suppressed_plugin_installs")
    if not isinstance(entries, list):
        entries = []
    plugin_id = args.plugin_id.strip()
    if not plugin_id:
        raise SystemExit("--plugin-id must not be empty")
    now = datetime.now(tz=timezone.utc).isoformat()
    replacement = {
        "plugin_id": plugin_id,
        "tool_type": args.tool_type,
        "reason": args.reason,
        "source": "request_plugin_install",
        "suppressed_at": now,
    }
    updated_entries: list[Any] = []
    replaced = False
    for entry in entries:
        entry_id = None
        if isinstance(entry, str):
            entry_id = entry
        elif isinstance(entry, dict):
            entry_id = entry.get("plugin_id") or entry.get("tool_id") or entry.get("id")
        if entry_id == plugin_id:
            if not replaced:
                updated_entries.append(replacement)
                replaced = True
            continue
        updated_entries.append(entry)
    if not replaced:
        updated_entries.append(replacement)
    state["suppressed_plugin_installs"] = updated_entries
    state_path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"path": str(state_path), "plugin_id": plugin_id, "suppressed": True}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
