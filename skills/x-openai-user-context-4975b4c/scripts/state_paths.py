#!/usr/bin/env python3
"""Shared Public Equity Investing state path resolution."""

from __future__ import annotations

import os
from pathlib import Path

MARKETPLACE_ID = "openai-monorepo"
PLUGIN_ID = "public-equity-investing"
PLUGIN_LABEL = "Public Equity Investing"
STATE_FILENAMES = (
    "user-context.md",
    # Legacy readiness state is never created or read, but reset should clear it.
    "category-state.json",
    "onboarding-state.json",
)

STATE_DIR_HELP = (
    f"{PLUGIN_LABEL} state directory. Defaults to "
    "an explicit --state-dir or $PUBLIC_EQUITY_STATE_DIR; no host home is assumed."
)


def default_state_dir() -> Path:
    env_dir = os.environ.get("PUBLIC_EQUITY_STATE_DIR")
    if env_dir:
        return Path(env_dir).expanduser()
    raise ValueError("Choose a state directory with --state-dir or PUBLIC_EQUITY_STATE_DIR.")


def configured_state_dir(codex_home: Path) -> Path:
    return codex_home / "state/plugins" / MARKETPLACE_ID / PLUGIN_ID


def resolve_state_dir(codex_home: Path | None, state_dir: Path | None) -> Path:
    if state_dir:
        return state_dir.expanduser()

    # --codex-home remains an explicit legacy compatibility option only.
    if codex_home:
        return configured_state_dir(codex_home.expanduser())
    return default_state_dir()
