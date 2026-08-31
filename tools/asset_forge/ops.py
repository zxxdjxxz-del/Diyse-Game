#!/usr/bin/env python3
"""Operational utilities for Diyse Asset Forge v0.3."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import forge
import atlas_engine
import lighting_engine
import qa_engine
import budget_engine


def cmd_budget(args: argparse.Namespace) -> None:
    queue = forge.read_jsonl(Path(args.queue))
    result = budget_engine.estimate_generation_calls(
        queue,
        atlas_tile=args.atlas_tile,
        atlas_overlap=args.atlas_overlap,
    )
    print(json.dumps(result, indent=2))


def cmd_lighting(args: argparse.Namespace) -> None:
    states = {}
    for item in args.state:
        if "=" not in item:
            raise ValueError("--state must use NAME=/path/to/file syntax")
        name, path = item.split("=", 1)
        states[name] = Path(path)
    result = lighting_engine.propagate_lighting_family(
        Path(args.source_base),
        Path(args.styled_base),
        states,
        Path(args.output_dir),
        strength=args.strength,
    )
    print(json.dumps(result, indent=2))


def cmd_qa_atlas(args: argparse.Namespace) -> None:
    plan = json.loads(Path(args.plan).read_text(encoding="utf-8"))
    result = qa_engine.atlas_seam_regression(
        Path(args.source),
        Path(args.output),
        plan["patches"],
        threshold=args.threshold,
    )
    print(json.dumps(result, indent=2))


def cmd_qa_alpha(args: argparse.Namespace) -> None:
    print(json.dumps(qa_engine.alpha_fringe_metrics(Path(args.image)), indent=2))


def cmd_qa_animation(args: argparse.Namespace) -> None:
    result = qa_engine.animation_flicker_regression(
        [Path(path) for path in args.source],
        [Path(path) for path in args.output],
        threshold_ratio=args.threshold_ratio,
    )
    print(json.dumps(result, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="diyse-asset-forge-ops")
    sub = parser.add_subparsers(dest="command", required=True)

    command = sub.add_parser("budget", help="Estimate image-generation calls before processing")
    command.add_argument("queue")
    command.add_argument("--atlas-tile", type=int, default=768)
    command.add_argument("--atlas-overlap", type=int, default=96)
    command.set_defaults(func=cmd_budget)

    command = sub.add_parser("lighting", help="Propagate styled base treatment to lighting states")
    command.add_argument("source_base")
    command.add_argument("styled_base")
    command.add_argument("--state", action="append", default=[], help="NAME=/path/to/source_state")
    command.add_argument("--output-dir", default=".asset_forge/lighting_output")
    command.add_argument("--strength", type=float, default=1.0)
    command.set_defaults(func=cmd_lighting)

    command = sub.add_parser("qa-atlas", help="Measure new seams introduced at atlas patch boundaries")
    command.add_argument("source")
    command.add_argument("output")
    command.add_argument("plan")
    command.add_argument("--threshold", type=float, default=0.06)
    command.set_defaults(func=cmd_qa_atlas)

    command = sub.add_parser("qa-alpha", help="Report semi-transparent edge/fringe diagnostics")
    command.add_argument("image")
    command.set_defaults(func=cmd_qa_alpha)

    command = sub.add_parser("qa-animation", help="Measure temporal flicker regression")
    command.add_argument("--source", nargs="+", required=True)
    command.add_argument("--output", nargs="+", required=True)
    command.add_argument("--threshold-ratio", type=float, default=1.65)
    command.set_defaults(func=cmd_qa_animation)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
