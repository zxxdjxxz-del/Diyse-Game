"""Repo-backed Hollow Watch party snapshots from the v93 true-battle report."""
from __future__ import annotations

from dataclasses import replace
from pathlib import Path

from tools.diysim.combat.models import Combatant
from tools.diysim.progression import Stats
from tools.diysim.sources.markdown import extract_markdown_table, parse_int
from tools.diysim.sources.repo import SourceGapError, read_repo_text

from .repo_loader import HollowWatchRepoData, TRUE_BATTLE_PATH

_SUPPORTED_LEVELS = frozenset({2, 3})


def _stats_from_row(row: dict[str, str]) -> Stats:
    return Stats(
        parse_int(row["HP"]),
        parse_int(row["MP"]),
        parse_int(row["ATK"]),
        parse_int(row["MAG"]),
        parse_int(row["DEF"]),
        parse_int(row["Spirit"]),
        parse_int(row["SPD"]),
    )


def load_hollow_watch_party_snapshot(
    level: int,
    *,
    root: Path | None = None,
) -> tuple[Combatant, Combatant, Combatant]:
    """Load the exact Cyanis/Ilyra/Maevra snapshot printed by v93."""
    if level not in _SUPPORTED_LEVELS:
        raise ValueError(f"Hollow Watch v93 only owns exact Lv2/Lv3 snapshots, not Lv{level}")

    text = read_repo_text(TRUE_BATTLE_PATH, root=root)
    rows = extract_markdown_table(text, f"Exact Lv{level} bodies")
    by_name: dict[str, Combatant] = {}
    for row in rows:
        name = row["Character"]
        by_name[name] = Combatant(
            name=name,
            side="party",
            stats=_stats_from_row(row),
            evasion=parse_int(row["EVA"]),
            status_resistance=parse_int(row["SR"]),
        )

    missing = [name for name in ("Cyanis", "Ilyra", "Maevra") if name not in by_name]
    if missing:
        raise SourceGapError(
            f"{TRUE_BATTLE_PATH} lacks Lv{level} party bodies for: {', '.join(missing)}"
        )
    return by_name["Cyanis"], by_name["Ilyra"], by_name["Maevra"]


def with_hollow_watch_party_snapshot(
    data: HollowWatchRepoData,
    level: int,
    *,
    root: Path | None = None,
) -> HollowWatchRepoData:
    cyanis, ilyra, maevra = load_hollow_watch_party_snapshot(level, root=root)
    return replace(data, cyanis=cyanis, ilyra=ilyra, maevra=maevra)


__all__ = ["load_hollow_watch_party_snapshot", "with_hollow_watch_party_snapshot"]
