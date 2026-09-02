"""Source-backed chapter/loadout resolution for DiySim progression audits."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from ..sources.campaign_progression import load_character_campaign_sources
from ..sources.equipment import load_equipment
from ..sources.equipment_availability import (
    ORDINARY_WEAPONS_PATH,
    STARTING_LOADOUTS_PATH,
    load_guaranteed_loadouts,
    load_ordinary_weapon_availability,
)

ProgressionAssumption = Literal["mandatory", "expected", "best_available"]


@dataclass(frozen=True)
class ProgressionSourceGap:
    code: str
    detail: str
    source_path: str | None = None


@dataclass(frozen=True)
class ResolvedLoadout:
    character: str
    chapter: int
    assumption: ProgressionAssumption
    weapon: str | None
    armor: str | None
    secondary: str | None
    secondary_consumed_by_weapon: bool
    source_gaps: tuple[ProgressionSourceGap, ...] = ()
    source_paths: tuple[str, ...] = ()

    @property
    def equipment_names(self) -> tuple[str, ...]:
        return tuple(name for name in (self.weapon, self.armor, self.secondary) if name)

    @property
    def slots_complete(self) -> bool:
        return (
            self.weapon is not None
            and self.armor is not None
            and (self.secondary is not None or self.secondary_consumed_by_weapon)
        )

    @property
    def authority_complete(self) -> bool:
        return self.slots_complete and not self.source_gaps


def _weapon_consumes_secondary(name: str | None, *, root: Path | None) -> bool:
    if not name:
        return False
    equipment_type = load_equipment(name, root=root).equipment_type.lower()
    return equipment_type in {"great bow", "two-handed sword", "two-handed conduit"}


def _dedupe_paths(paths: list[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(paths))


def resolve_loadout(
    character: str,
    chapter: int,
    assumption: ProgressionAssumption = "mandatory",
    *,
    root: Path | None = None,
) -> ResolvedLoadout:
    """Resolve only equipment justified by current repo authority.

    `mandatory` treats guaranteed ownership separately from mere availability.
    `expected` refuses to invent a purchase/upgrade policy.
    `best_available` may advance to the latest explicitly chapter-dated native
    ordinary weapon, but never invents armor/secondary timing.
    """
    if chapter < 0:
        raise ValueError("chapter must be >= 0")
    if assumption not in ("mandatory", "expected", "best_available"):
        raise ValueError(f"Unsupported progression assumption: {assumption}")

    characters = {row.character: row for row in load_character_campaign_sources(root=root)}
    campaign = characters.get(character)
    if campaign is None:
        raise KeyError(f"Unknown permanent character in campaign authority: {character}")

    if chapter < campaign.recruitment_chapter:
        return ResolvedLoadout(
            character=character,
            chapter=chapter,
            assumption=assumption,
            weapon=None,
            armor=None,
            secondary=None,
            secondary_consumed_by_weapon=False,
            source_gaps=(
                ProgressionSourceGap(
                    "not_recruited",
                    f"{character} is not recruited by Chapter {chapter}.",
                    campaign.recruitment_source_path,
                ),
            ),
            source_paths=(campaign.recruitment_source_path,),
        )

    guaranteed_rows = [
        row
        for row in load_guaranteed_loadouts(root=root)
        if row.character == character and row.chapter <= chapter
    ]
    guaranteed = max(guaranteed_rows, key=lambda row: row.chapter) if guaranteed_rows else None

    weapon = guaranteed.weapon if guaranteed else None
    armor = guaranteed.armor if guaranteed else None
    secondary = guaranteed.secondary if guaranteed else None
    gaps: list[ProgressionSourceGap] = []
    paths: list[str] = []

    if guaranteed:
        paths.append(guaranteed.source_path)
    else:
        gaps.append(
            ProgressionSourceGap(
                "guaranteed_join_loadout_missing",
                f"No guaranteed/join loadout is currently published for {character}.",
                STARTING_LOADOUTS_PATH,
            )
        )

    if assumption == "mandatory":
        if guaranteed and chapter > guaranteed.chapter:
            gaps.append(
                ProgressionSourceGap(
                    "later_mandatory_loadout_map_missing",
                    "Current authority preserves the guaranteed earlier loadout, but does not "
                    "publish a complete later mandatory equipment-ownership map.",
                    STARTING_LOADOUTS_PATH,
                )
            )

    elif assumption == "expected":
        if guaranteed and chapter > guaranteed.chapter:
            gaps.append(
                ProgressionSourceGap(
                    "expected_loadout_policy_missing",
                    "The repo does not currently specify which available purchases/upgrades "
                    "define the normal expected loadout at this checkpoint.",
                    None,
                )
            )

    else:
        candidates = [
            row
            for row in load_ordinary_weapon_availability(root=root)
            if row.character == character and row.first_chapter <= chapter
        ]
        if candidates:
            latest = max(candidates, key=lambda row: row.first_chapter)
            weapon = latest.name
            paths.append(latest.source_path)
        else:
            gaps.append(
                ProgressionSourceGap(
                    "weapon_availability_timing_missing",
                    f"No chapter-dated native ordinary weapon is published for {character} "
                    f"by Chapter {chapter}.",
                    ORDINARY_WEAPONS_PATH,
                )
            )

        gaps.append(
            ProgressionSourceGap(
                "armor_availability_timing_missing",
                "Ordinary armor authority currently has no First availability column, so "
                "best-available armor cannot be selected without guessing.",
                "docs/08_ITEMS_AND_EQUIPMENT/ARMOR/ORDINARY_ARMOR.md",
            )
        )

        consumes_secondary = _weapon_consumes_secondary(weapon, root=root)
        if not consumes_secondary:
            gaps.append(
                ProgressionSourceGap(
                    "secondary_availability_timing_missing",
                    "Ordinary Shield/Focus authority currently has no First availability "
                    "timing, so best-available Secondary cannot be selected without guessing.",
                    "docs/08_ITEMS_AND_EQUIPMENT",
                )
            )

    consumes_secondary = _weapon_consumes_secondary(weapon, root=root)
    if consumes_secondary:
        secondary = None

    return ResolvedLoadout(
        character=character,
        chapter=chapter,
        assumption=assumption,
        weapon=weapon,
        armor=armor,
        secondary=secondary,
        secondary_consumed_by_weapon=consumes_secondary,
        source_gaps=tuple(gaps),
        source_paths=_dedupe_paths(paths),
    )


def resolve_campaign_loadouts(
    chapter: int,
    assumption: ProgressionAssumption = "mandatory",
    *,
    root: Path | None = None,
) -> tuple[ResolvedLoadout, ...]:
    characters = load_character_campaign_sources(root=root)
    return tuple(
        resolve_loadout(row.character, chapter, assumption, root=root)
        for row in characters
        if row.recruitment_chapter <= chapter
    )


__all__ = [
    "ProgressionAssumption",
    "ProgressionSourceGap",
    "ResolvedLoadout",
    "resolve_campaign_loadouts",
    "resolve_loadout",
]
