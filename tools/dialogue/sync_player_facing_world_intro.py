#!/usr/bin/env python3
"""Synchronize the approved Nimera world intro into game runtime data.

The markdown file in docs/04_WORLD_AND_LORE is the sole wording authority.
The reader consumes it directly; the game consumes the generated JSON.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs/04_WORLD_AND_LORE/PLAYER_FACING_WORLD_INTRO.md"
OUTPUT = ROOT / "game/content/presentation/player_facing_world_intro.json"
MARKER = "## The World of Diyse"
EXPECTED_FINAL_LINE = "If I catch you using it as one, we're going to have a conversation."


def plain_text(line: str) -> str:
    return line.replace("**", "").replace("*", "").replace(chr(96), "").strip()


def extract_intro() -> dict:
    raw = SOURCE.read_text(encoding="utf-8")
    if MARKER not in raw:
        raise RuntimeError("Player-facing world intro marker is missing")

    body = raw.split(MARKER, 1)[1]
    paragraphs: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            break
        paragraphs.append(plain_text(stripped))

    if not paragraphs:
        raise RuntimeError("Player-facing world intro has no body")
    if paragraphs[-1] != EXPECTED_FINAL_LINE:
        raise RuntimeError("Player-facing world intro no longer ends on Nimera's approved sign-off")

    return {
        "schema": "diyse_player_facing_world_intro_v1",
        "source_path": "docs/04_WORLD_AND_LORE/PLAYER_FACING_WORLD_INTRO.md",
        "title": "The World of Diyse",
        "speaker_id": "nimera",
        "speaker_name": "Nimera Pellan",
        "present_year": "720 YF",
        "awakening_period": "around 200 YF",
        "paragraphs": paragraphs,
    }


def serialized_payload() -> str:
    return json.dumps(extract_intro(), ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    payload = serialized_payload()
    if args.check:
        if not OUTPUT.exists():
            raise RuntimeError(f"Runtime intro data is missing: {OUTPUT.relative_to(ROOT)}")
        if OUTPUT.read_text(encoding="utf-8") != payload:
            raise RuntimeError(
                "Runtime player-facing intro is stale. Run "
                "python tools/dialogue/sync_player_facing_world_intro.py and commit the result."
            )
        print("Player-facing world intro runtime data matches authority.")
        return 0

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(payload, encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} from {SOURCE.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
