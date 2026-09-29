#!/usr/bin/env python3
"""Current Diyse Asset Forge entrypoint with texture-style contract injection.

`forge.py` remains the implementation core and backward-compatible API surface.
This wrapper makes the current texture-facing Art Director contract authoritative for
all newly planned prompts without duplicating those rules in Python source.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import forge

CONTRACT_PATH = Path(__file__).with_name("texture_style_contract_v1.json")


def load_texture_style_contract(path: Path = CONTRACT_PATH) -> dict:
    contract = json.loads(path.read_text(encoding="utf-8"))
    required = {"id", "status", "shared_style_block", "categories", "technical_preservation", "review"}
    missing = sorted(required - set(contract))
    if missing:
        raise ValueError(f"Texture style contract missing required keys: {', '.join(missing)}")
    if contract.get("status") != "active":
        raise ValueError("Texture style contract must be active before Asset Forge may plan new work")
    categories = contract.get("categories") or {}
    required_categories = {
        "stone", "foliage", "grass", "water", "fire", "wood",
        "cave", "ritual", "interior", "prop", "generic",
    }
    missing_categories = sorted(required_categories - set(categories))
    if missing_categories:
        raise ValueError(
            "Texture style contract missing category prompts: " + ", ".join(missing_categories)
        )
    return contract


def apply_texture_style_contract(contract: Optional[dict] = None) -> dict:
    contract = contract or load_texture_style_contract()
    forge.STYLE_BLOCK = str(contract["shared_style_block"])
    forge.PROMPT_BY_CATEGORY = dict(contract["categories"])
    return contract


STYLE_CONTRACT = apply_texture_style_contract()

# Re-export the most frequently used planning functions so callers can migrate from
# `forge` to `forge_current` without changing their API usage.
classify = forge.classify
inventory = forge.inventory
plan = forge.plan
make_prompt = forge.make_prompt
qa = forge.qa
summary = forge.summary
write_jsonl = forge.write_jsonl
read_jsonl = forge.read_jsonl


def main(argv: Optional[list[str]] = None) -> int:
    # Re-apply at command entry in case another import mutated forge globals.
    apply_texture_style_contract(STYLE_CONTRACT)
    return forge.main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
