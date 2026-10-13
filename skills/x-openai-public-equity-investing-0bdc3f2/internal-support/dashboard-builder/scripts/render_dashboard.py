#!/usr/bin/env python3
"""Render a standalone Public Equity Investing dashboard HTML file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path



def _resolve_plugin_root() -> Path:
    """Find shared resources beside the exported skills without fixed depth."""
    for export_root in Path(__file__).resolve().parents:
        if (export_root / "resources").is_dir() and (export_root / "skills").is_dir():
            plugin_root = (
                export_root / "resources" / "plugins-6ebaff11" / "plugins"
                / "public-equity-investing"
            )
            if not (plugin_root / "shared").is_dir():
                raise FileNotFoundError(
                    f"Public Equity Investing shared resources are missing: {plugin_root / 'shared'}"
                )
            return plugin_root
    raise FileNotFoundError(
        "Cannot locate the export root containing resources/ and skills/ "
        f"above {Path(__file__).resolve()}"
    )


PLUGIN_ROOT = _resolve_plugin_root()
sys.path.insert(0, str(PLUGIN_ROOT))

from shared.dashboard.qa import load_payload, validate_payload  # noqa: E402
from shared.dashboard.renderer import render_dashboard  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("payload", help="Path to dashboard payload JSON.")
    parser.add_argument("output", help="Path to write standalone HTML.")
    parser.add_argument(
        "--profile",
        choices=["draft", "production"],
        default="production",
        help="Validation profile. Rendering defaults to production because HTML is the user-facing artifact.",
    )
    parser.add_argument("--qa-json", help="Optional path to write validation report JSON.")
    args = parser.parse_args()

    payload = load_payload(args.payload)
    report = validate_payload(payload, profile=args.profile)
    if args.qa_json:
        qa_path = Path(args.qa_json)
        qa_path.parent.mkdir(parents=True, exist_ok=True)
        qa_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if report["hard_failures"]:
        for failure in report["hard_failures"]:
            print(f"failure: {failure}", file=sys.stderr)
        return 1

    html = render_dashboard(payload, validate=False)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    for warning in report["warnings"]:
        print(f"warning: {warning}", file=sys.stderr)
    print(str(output_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
