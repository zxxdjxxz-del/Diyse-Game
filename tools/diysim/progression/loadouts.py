"""Source-backed chapter/loadout resolution for DiySim progression audits."""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Literal

from ..sources.campaign_progression import load_campaign_checkpoint, load_character_campaign_sources
from ..sources.equipment import EQUIPMENT_REGISTER_PATH, load_equipment
from ..sources.equipment_availability import (
    ORDINARY_WEAPONS_PATH,
    STARTING_LOADOUTS_PATH,
    load_guaranteed_loadouts,
    load_ordinary_weapon_availability,
)
from ..sources.repo import SourceGapError, read_repo_text

ProgressionAssumption = Literal["mandatory", "expected", "best_available"]
EquipmentSlot = Literal["weapon", "armor", "secondary"]
EQUIPMENT_SLOT_RULES_PATH = "docs/08_ITEMS_AND_EQUIPMENT/EQUIPMENT_SLOT_RULES.md"
EQUIPMENT_SYSTEM_MASTER_PATH = "docs/08_ITEMS_AND_EQUIPMENT/EQUIPMENT_SYSTEM_MASTER.md"


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
    explicit_slots: tuple[EquipmentSlot, ...] = ()
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


def _ordinary_weapon_rows(character: str, *, root: Path | None):
    return tuple(
        row
        for row in load_ordinary_weapon_availability(root=root)
        if row.character == character
    )


def _item_slot(name: str, *, root: Path | None) -> EquipmentSlot:
    item = load_equipment(name, root=root)
    if item.layer.casefold() != "ordinary":
        raise ValueError(
            f"Explicit progression equipment currently supports Ordinary gear only: {name}."
        )
    weapon_names = {
        row.name.casefold() for row in load_ordinary_weapon_availability(root=root)
    }
    if item.name.casefold() in weapon_names:
        return "weapon"
    if item.equipment_type.casefold() in {"shield", "focus"}:
        return "secondary"
    if "armor" in item.equipment_type.casefold():
        return "armor"
    raise ValueError(f"Could not resolve an equipment slot for ordinary item {name!r}.")


def _native_secondary_access(
    character: str,
    *,
    root: Path | None,
) -> tuple[set[str], list[str]]:
    """Return Secondary families explicitly proven legal for the native character.

    This deliberately does not infer donor access. Starting loadouts prove any
    Secondary family already equipped at recruitment; current equipment-system
    owner text additionally names Ilyra/Vaelira native Secondary options.
    """
    families: set[str] = set()
    paths: list[str] = []

    for row in load_guaranteed_loadouts(root=root):
        if row.character != character or not row.secondary:
            continue
        item = load_equipment(row.secondary, root=root)
        if item.equipment_type.casefold() in {"shield", "focus"}:
            families.add(item.equipment_type.casefold())
            paths.append(row.source_path)

    text = read_repo_text(EQUIPMENT_SYSTEM_MASTER_PATH, root=root)
    block_match = re.search(
        rf"(?ms)^\s*{re.escape(character)}:\s*$\n(?P<body>(?:-.*\n?)+)",
        text,
    )
    if block_match:
        body = block_match.group("body")
        for family in ("Shield", "Focus"):
            if re.search(rf"\b{family}\b", body, re.I):
                families.add(family.casefold())
        if families:
            paths.append(EQUIPMENT_SYSTEM_MASTER_PATH)

    return families, paths


def _validate_explicit_item(
    character: str,
    slot: EquipmentSlot,
    name: str,
    *,
    availability_through_chapter: int,
    root: Path | None,
) -> tuple[str, list[str]]:
    try:
        item = load_equipment(name, root=root)
    except SourceGapError as exc:
        raise ValueError(str(exc)) from exc

    actual_slot = _item_slot(item.name, root=root)
    if actual_slot != slot:
        raise ValueError(
            f"{item.name} occupies {actual_slot}, not requested slot {slot}."
        )

    paths = [EQUIPMENT_REGISTER_PATH]
    if slot in {"weapon", "armor"}:
        if item.owner.casefold() != character.casefold():
            raise ValueError(
                f"{item.name} is not native ordinary {slot} equipment for {character}; "
                "donor equipment access requires Class-Level progression and is not yet "
                "accepted by this override."
            )
        if slot == "weapon":
            timing = next(
                (
                    row
                    for row in _ordinary_weapon_rows(character, root=root)
                    if row.name.casefold() == item.name.casefold()
                ),
                None,
            )
            if timing is None:
                raise ValueError(
                    f"No chapter availability authority was found for ordinary weapon {item.name}."
                )
            if timing.first_chapter > availability_through_chapter:
                raise ValueError(
                    f"{item.name} is first available in Chapter {timing.first_chapter}, "
                    f"after this checkpoint's Chapter-{availability_through_chapter} "
                    "equipment cutoff."
                )
            paths.append(timing.source_path)
    else:
        legal_families, access_paths = _native_secondary_access(character, root=root)
        family = item.equipment_type.casefold()
        if family not in legal_families:
            raise ValueError(
                f"Current authority does not prove native {item.equipment_type} Secondary "
                f"access for {character}; donor/other access cannot be assumed."
            )
        paths.extend(access_paths)
        paths.append(EQUIPMENT_SLOT_RULES_PATH)

    return item.name, paths


def _normalize_equipment_choices(
    equipment_choices: Mapping[str, str] | None,
) -> dict[EquipmentSlot, str]:
    choices: dict[EquipmentSlot, str] = {}
    for raw_slot, name in (equipment_choices or {}).items():
        slot = raw_slot.strip().casefold()
        if slot not in {"weapon", "armor", "secondary"}:
            raise ValueError(
                f"Unknown equipment slot {raw_slot!r}; use weapon, armor, or secondary."
            )
        if not name or not name.strip():
            raise ValueError(f"Explicit {slot} equipment name cannot be empty.")
        choices[slot] = name.strip()  # type: ignore[assignment]
    return choices


def _apply_explicit_choices(
    resolved: ResolvedLoadout,
    equipment_choices: Mapping[str, str] | None,
    *,
    availability_through_chapter: int,
    root: Path | None,
) -> ResolvedLoadout:
    choices = _normalize_equipment_choices(equipment_choices)
    if not choices:
        return resolved

    weapon = resolved.weapon
    armor = resolved.armor
    secondary = resolved.secondary
    explicit_slots: list[EquipmentSlot] = []
    paths = list(resolved.source_paths)

    for slot in ("weapon", "armor", "secondary"):
        if slot not in choices:
            continue
        name, item_paths = _validate_explicit_item(
            resolved.character,
            slot,  # type: ignore[arg-type]
            choices[slot],
            availability_through_chapter=availability_through_chapter,
            root=root,
        )
        explicit_slots.append(slot)  # type: ignore[arg-type]
        paths.extend(item_paths)
        if slot == "weapon":
            weapon = name
        elif slot == "armor":
            armor = name
        else:
            secondary = name

    consumes_secondary = _weapon_consumes_secondary(weapon, root=root)
    if consumes_secondary:
        if "secondary" in choices:
            raise ValueError(
                f"{weapon} consumes Weapon + Secondary and cannot be combined with "
                f"explicit Secondary {choices['secondary']}."
            )
        secondary = None

    gaps = list(resolved.source_gaps)
    if "weapon" in choices:
        gaps = [
            gap
            for gap in gaps
            if gap.code
            not in {"weapon_availability_timing_missing", "weapon_checkpoint_granularity_missing"}
        ]
    if "armor" in choices:
        gaps = [gap for gap in gaps if gap.code != "armor_availability_timing_missing"]
    if "secondary" in choices or consumes_secondary:
        gaps = [gap for gap in gaps if gap.code != "secondary_availability_timing_missing"]

    required_explicit = {"weapon", "armor"}
    if not consumes_secondary:
        required_explicit.add("secondary")
    if required_explicit.issubset(choices):
        gaps = [
            gap
            for gap in gaps
            if gap.code
            not in {
                "guaranteed_join_loadout_missing",
                "later_mandatory_loadout_map_missing",
                "expected_loadout_policy_missing",
            }
        ]

    return ResolvedLoadout(
        character=resolved.character,
        chapter=resolved.chapter,
        assumption=resolved.assumption,
        weapon=weapon,
        armor=armor,
        secondary=secondary,
        secondary_consumed_by_weapon=consumes_secondary,
        explicit_slots=tuple(explicit_slots),
        source_gaps=tuple(gaps),
        source_paths=_dedupe_paths(paths),
    )


def resolve_loadout(
    character: str,
    chapter: int,
    assumption: ProgressionAssumption = "mandatory",
    *,
    availability_through_chapter: int | None = None,
    checkpoint_label: str | None = None,
    equipment_choices: Mapping[str, str] | None = None,
    root: Path | None = None,
) -> ResolvedLoadout:
    """Resolve only equipment justified by current repo authority or explicit inputs.

    `mandatory` treats guaranteed ownership separately from mere availability.
    `expected` refuses to invent a purchase/upgrade policy.
    `best_available` may advance to the latest explicitly chapter-dated native
    ordinary weapon, but never invents armor/secondary timing.

    Explicit equipment choices are simulator inputs, not claims of canonical
    acquisition. They currently accept only native Ordinary equipment. Known
    weapon availability timing is still enforced; armor/Secondary timing can be
    supplied as an explicit assumed-owned simulation choice because the repo does
    not publish those chapter dates. Donor/Relic/Legacy access is intentionally
    deferred until Class-Level progression can validate its unlocks.

    For an intra-chapter checkpoint, `availability_through_chapter` can be lower
    than `chapter`. That prevents chapter-granular availability from being pulled
    forward to a point where its exact within-chapter timing is unpublished.
    """
    if chapter < 0:
        raise ValueError("chapter must be >= 0")
    if assumption not in ("mandatory", "expected", "best_available"):
        raise ValueError(f"Unsupported progression assumption: {assumption}")
    if availability_through_chapter is None:
        availability_through_chapter = chapter
    if not 0 <= availability_through_chapter <= chapter:
        raise ValueError("availability_through_chapter must satisfy 0 <= cutoff <= chapter")

    characters = {row.character: row for row in load_character_campaign_sources(root=root)}
    campaign = characters.get(character)
    if campaign is None:
        raise KeyError(f"Unknown permanent character in campaign authority: {character}")

    if chapter < campaign.recruitment_chapter:
        if equipment_choices:
            raise ValueError(
                f"Cannot apply explicit equipment to {character} before recruitment in "
                f"Chapter {campaign.recruitment_chapter}."
            )
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
        all_weapons = list(_ordinary_weapon_rows(character, root=root))
        candidates = [
            row for row in all_weapons
            if row.first_chapter <= availability_through_chapter
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
                    f"by Chapter {availability_through_chapter}.",
                    ORDINARY_WEAPONS_PATH,
                )
            )

        withheld_same_chapter = [
            row for row in all_weapons
            if availability_through_chapter < row.first_chapter <= chapter
        ]
        if withheld_same_chapter:
            names = ", ".join(row.name for row in withheld_same_chapter)
            where = checkpoint_label or f"Chapter {chapter} checkpoint"
            gaps.append(
                ProgressionSourceGap(
                    "weapon_checkpoint_granularity_missing",
                    f"{names} are only dated to Chapter {chapter}; current authority does not "
                    f"state whether they are obtainable by {where}, so they were not pulled forward.",
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

    resolved = ResolvedLoadout(
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
    return _apply_explicit_choices(
        resolved,
        equipment_choices,
        availability_through_chapter=availability_through_chapter,
        root=root,
    )


def resolve_loadout_at_checkpoint(
    character: str,
    checkpoint_key: str,
    assumption: ProgressionAssumption = "mandatory",
    *,
    equipment_choices: Mapping[str, str] | None = None,
    root: Path | None = None,
) -> ResolvedLoadout:
    checkpoint = load_campaign_checkpoint(checkpoint_key, root=root)
    return resolve_loadout(
        character,
        checkpoint.chapter,
        assumption,
        availability_through_chapter=checkpoint.chapter_granular_equipment_cutoff,
        checkpoint_label=checkpoint.label,
        equipment_choices=equipment_choices,
        root=root,
    )


def resolve_campaign_loadouts(
    chapter: int,
    assumption: ProgressionAssumption = "mandatory",
    *,
    equipment_choices: Mapping[str, Mapping[str, str]] | None = None,
    root: Path | None = None,
) -> tuple[ResolvedLoadout, ...]:
    characters = load_character_campaign_sources(root=root)
    choices = equipment_choices or {}
    unknown = sorted(set(choices) - {row.character for row in characters})
    if unknown:
        raise ValueError(
            "Unknown permanent character in equipment choices: " + ", ".join(unknown)
        )
    return tuple(
        resolve_loadout(
            row.character,
            chapter,
            assumption,
            equipment_choices=choices.get(row.character),
            root=root,
        )
        for row in characters
        if row.recruitment_chapter <= chapter
    )


__all__ = [
    "EQUIPMENT_SLOT_RULES_PATH",
    "EQUIPMENT_SYSTEM_MASTER_PATH",
    "EquipmentSlot",
    "ProgressionAssumption",
    "ProgressionSourceGap",
    "ResolvedLoadout",
    "resolve_campaign_loadouts",
    "resolve_loadout",
    "resolve_loadout_at_checkpoint",
]
