"""Parse the non-canon Zevraya true-battle candidate from 90_WORKING."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from tools.diysim.sources import SourceGapError, extract_markdown_table, find_repo_root, read_repo_text

WORKING_SNAPSHOT_PATH = "docs/90_WORKING/MATRON_ZEVRAYA_TRUE_BATTLE_SNAPSHOT_WORKING.md"


@dataclass(frozen=True)
class ZevrayaWorkingSnapshot:
    prepared_consumables: dict[str, int]


@lru_cache(maxsize=4)
def _cached(root_string: str) -> ZevrayaWorkingSnapshot:
    root = Path(root_string)
    text = read_repo_text(WORKING_SNAPSHOT_PATH, root=root)
    rows = extract_markdown_table(text, "Prepared consumable candidate")
    prepared = {row["Consumable"]: int(row["Count"].replace(",", "")) for row in rows}
    expected = {
        "Restorative Salve",
        "Deepflow Tonic",
        "Trauma Remedy",
        "Stability Remedy",
        "Rousing Salts",
    }
    if set(prepared) != expected:
        raise SourceGapError(
            f"Zevraya working snapshot must define exactly {sorted(expected)}, found {sorted(prepared)}"
        )
    return ZevrayaWorkingSnapshot(prepared_consumables=prepared)


def load_zevraya_working_snapshot(*, root: Path | None = None) -> ZevrayaWorkingSnapshot:
    repo = (root or find_repo_root()).resolve()
    return _cached(str(repo))


__all__ = ["WORKING_SNAPSHOT_PATH", "ZevrayaWorkingSnapshot", "load_zevraya_working_snapshot"]
