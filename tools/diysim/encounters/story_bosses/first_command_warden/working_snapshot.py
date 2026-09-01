"""Parse the non-canon Warden true-battle calibration snapshot from 90_WORKING."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re

from tools.diysim.sources import SourceGapError, extract_markdown_table, find_repo_root, read_repo_text

WORKING_SNAPSHOT_PATH = "docs/90_WORKING/FIRST_COMMAND_WARDEN_TRUE_BATTLE_SNAPSHOT_WORKING.md"


@dataclass(frozen=True)
class WardenWorkingSnapshot:
    class_levels: dict[str, int]
    selected_classes: dict[str, str]
    prepared_consumables: dict[str, int]


@lru_cache(maxsize=4)
def _cached(root_string: str) -> WardenWorkingSnapshot:
    root = Path(root_string)
    text = read_repo_text(WORKING_SNAPSHOT_PATH, root=root)

    class_rows = extract_markdown_table(text, "Working pre-Warden Base Class Levels")
    class_levels: dict[str, int] = {}
    selected_classes: dict[str, str] = {}
    for row in class_rows:
        match = re.fullmatch(r"CL(\d+)", row["Working CL at S020"].strip(), re.I)
        if not match:
            raise SourceGapError(f"Invalid Warden working CL: {row['Working CL at S020']}")
        character = row["Character"]
        class_levels[character] = int(match.group(1))
        selected_classes[character] = row["Selected Base Class"]

    item_rows = extract_markdown_table(text, "Working prepared consumable candidate")
    prepared_consumables = {row["Consumable"]: int(row["Count"].replace(",", "")) for row in item_rows}

    expected = {"Cyanis", "Ilyra", "Torren", "Nimera"}
    if set(class_levels) != expected:
        raise SourceGapError("Warden working snapshot must define the v105 active four exactly")
    if not prepared_consumables:
        raise SourceGapError("Warden working snapshot has no prepared consumables")

    return WardenWorkingSnapshot(
        class_levels=class_levels,
        selected_classes=selected_classes,
        prepared_consumables=prepared_consumables,
    )


def load_warden_working_snapshot(*, root: Path | None = None) -> WardenWorkingSnapshot:
    repo = (root or find_repo_root()).resolve()
    return _cached(str(repo))


__all__ = ["WORKING_SNAPSHOT_PATH", "WardenWorkingSnapshot", "load_warden_working_snapshot"]
