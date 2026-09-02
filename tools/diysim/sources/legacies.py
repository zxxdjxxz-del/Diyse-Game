"""Repository-backed Legacy package and donor-access authority.

This module inventories authored Legacy equipment and reciprocal donor relationships.
It deliberately does not infer project completion, inventory ownership, or chapter
availability from the package definitions alone.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from .class_equipment_access import load_donor_equipment_access
from .equipment import load_equipment
from .markdown import find_markdown_table
from .repo import SourceGapError, find_repo_root, read_repo_text

LEGACY_MASTER_REGISTER_PATH = (
    "docs/08_ITEMS_AND_EQUIPMENT/LEGACIES/LEGACY_MASTER_REGISTER.md"
)
DONOR_LEGACY_ACCESS_PATH = (
    "docs/08_ITEMS_AND_EQUIPMENT/LEGACIES/DONOR_LEGACY_ACCESS.md"
)
LEGACY_PROJECT_RULES_PATH = (
    "docs/08_ITEMS_AND_EQUIPMENT/LEGACIES/LEGACY_PROJECT_RULES.md"
)

_EXPECTED_CHARACTER_COUNTS = {
    "Cyanis": 3,
    "Ilyra": 4,
    "Torren": 2,
    "Nimera": 3,
    "Vaelira": 3,
    "Seyrik": 2,
}


@dataclass(frozen=True)
class LegacyItemSource:
    character: str
    legacy: str
    slot: str
    raw_stats: str
    capstone_perk: str
    legacy_trait: str
    source_path: str = LEGACY_MASTER_REGISTER_PATH

    @property
    def consumes_secondary(self) -> bool:
        return "weapon + secondary" in self.slot.casefold()


@dataclass(frozen=True)
class DonorLegacyAccessSource:
    receiver: str
    donor: str
    donor_package: str
    source_path: str = DONOR_LEGACY_ACCESS_PATH


@dataclass(frozen=True)
class LegacyProjectRuleSource:
    native_base_class_level: int
    requires_all_four_core_masteries: bool
    requires_character_quest: bool
    requires_quest_component: bool
    requires_precursor: bool
    requires_gate_a: bool
    requires_gate_b: bool
    requires_kessara: bool
    donor_requires_existing_item: bool
    unique_not_copied: bool
    source_path: str = LEGACY_PROJECT_RULES_PATH


@lru_cache(maxsize=4)
def _load_items(root_string: str) -> tuple[LegacyItemSource, ...]:
    root = Path(root_string)
    text = read_repo_text(LEGACY_MASTER_REGISTER_PATH, root=root)
    rows = find_markdown_table(
        text,
        (
            "Character",
            "Legacy",
            "Slot",
            "Current raw stats",
            "Capstone perk",
            "Legacy Trait",
        ),
    )
    entries = tuple(
        LegacyItemSource(
            character=row["Character"].strip(),
            legacy=row["Legacy"].strip(),
            slot=row["Slot"].strip(),
            raw_stats=row["Current raw stats"].strip(),
            capstone_perk=row["Capstone perk"].strip(),
            legacy_trait=row["Legacy Trait"].strip(),
        )
        for row in rows
    )
    if len(entries) != 17:
        raise SourceGapError(
            f"Expected 17 Legacy rows in {LEGACY_MASTER_REGISTER_PATH}, found {len(entries)}"
        )
    if len({row.legacy.casefold() for row in entries}) != len(entries):
        raise SourceGapError(f"Duplicate Legacy identity in {LEGACY_MASTER_REGISTER_PATH}")

    counts = Counter(row.character for row in entries)
    if dict(counts) != _EXPECTED_CHARACTER_COUNTS:
        raise SourceGapError(
            "Legacy package counts do not match the authored six-character 17-piece split: "
            f"{dict(counts)}"
        )

    for row in entries:
        equipment = load_equipment(row.legacy, root=root)
        if equipment.layer.casefold() != "legacy":
            raise SourceGapError(
                f"Legacy master row {row.legacy!r} resolves to equipment layer {equipment.layer!r}"
            )
        if equipment.owner.casefold() != row.character.casefold():
            raise SourceGapError(
                f"Legacy owner mismatch for {row.legacy}: package says {row.character}, "
                f"equipment register says {equipment.owner}"
            )
    return entries


@lru_cache(maxsize=4)
def _load_donors(root_string: str) -> tuple[DonorLegacyAccessSource, ...]:
    root = Path(root_string)
    text = read_repo_text(DONOR_LEGACY_ACCESS_PATH, root=root)
    rows = find_markdown_table(text, ("Receiver", "Donor", "Donor package"))
    entries = tuple(
        DonorLegacyAccessSource(
            receiver=row["Receiver"].strip(),
            donor=row["Donor"].strip(),
            donor_package=row["Donor package"].strip(),
        )
        for row in rows
    )
    if len(entries) != 6:
        raise SourceGapError(
            f"Expected 6 donor Legacy rows in {DONOR_LEGACY_ACCESS_PATH}, found {len(entries)}"
        )
    if len({row.receiver.casefold() for row in entries}) != len(entries):
        raise SourceGapError(f"Duplicate Legacy donor receiver in {DONOR_LEGACY_ACCESS_PATH}")

    class_donors = {
        row.character.casefold(): row.donor_character.casefold()
        for row in load_donor_equipment_access(root=root)
    }
    legacy_donors = {row.receiver.casefold(): row.donor.casefold() for row in entries}
    if legacy_donors != class_donors:
        raise SourceGapError(
            "Legacy donor relationships do not match Class-System reciprocal donor authority"
        )
    return entries


@lru_cache(maxsize=4)
def _load_project_rules(root_string: str) -> LegacyProjectRuleSource:
    root = Path(root_string)
    text = read_repo_text(LEGACY_PROJECT_RULES_PATH, root=root)
    folded = text.casefold()

    required_phrases = {
        "all four core masteries": "all four native Core Masteries",
        "character quest": "Character Quest",
        "legacy component": "Legacy Component",
        "precursor": "Legacy precursor",
        "legacy gate a": "Legacy Gate A",
        "legacy gate b": "Legacy Gate B",
        "kessara": "Kessara",
    }
    missing = [label for phrase, label in required_phrases.items() if phrase not in folded]
    if missing:
        raise SourceGapError(
            f"Legacy project rules are missing required authority: {', '.join(missing)}"
        )
    if "cl13" not in folded:
        raise SourceGapError("Legacy project rules do not state native Base Class CL13 completion")
    if "actual donor legacy item must already exist" not in folded:
        raise SourceGapError("Legacy donor rules do not require the actual donor item to exist")
    if "legacies cannot be copied" not in folded:
        raise SourceGapError("Legacy project rules do not preserve the no-copy uniqueness rule")

    return LegacyProjectRuleSource(
        native_base_class_level=13,
        requires_all_four_core_masteries=True,
        requires_character_quest=True,
        requires_quest_component=True,
        requires_precursor=True,
        requires_gate_a=True,
        requires_gate_b=True,
        requires_kessara=True,
        donor_requires_existing_item=True,
        unique_not_copied=True,
    )


def load_legacy_items(*, root: Path | None = None) -> tuple[LegacyItemSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _load_items(str(repo))


def load_legacy_item(legacy: str, *, root: Path | None = None) -> LegacyItemSource:
    matches = tuple(
        row for row in load_legacy_items(root=root) if row.legacy.casefold() == legacy.casefold()
    )
    if not matches:
        raise SourceGapError(f"No Legacy package row found for: {legacy}")
    if len(matches) != 1:
        raise SourceGapError(f"Ambiguous Legacy package row for: {legacy}")
    return matches[0]


def load_character_legacy_package(
    character: str,
    *,
    root: Path | None = None,
) -> tuple[LegacyItemSource, ...]:
    rows = tuple(
        row for row in load_legacy_items(root=root) if row.character.casefold() == character.casefold()
    )
    if not rows:
        raise KeyError(f"Unknown permanent character in Legacy package authority: {character}")
    return rows


def load_donor_legacy_access(
    *,
    root: Path | None = None,
) -> tuple[DonorLegacyAccessSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _load_donors(str(repo))


def load_character_donor_legacy_access(
    receiver: str,
    *,
    root: Path | None = None,
) -> DonorLegacyAccessSource:
    for row in load_donor_legacy_access(root=root):
        if row.receiver.casefold() == receiver.casefold():
            return row
    raise KeyError(f"Unknown permanent character in donor Legacy authority: {receiver}")


def load_legacy_project_rules(*, root: Path | None = None) -> LegacyProjectRuleSource:
    repo = (root or find_repo_root()).resolve()
    return _load_project_rules(str(repo))


__all__ = [
    "DONOR_LEGACY_ACCESS_PATH",
    "LEGACY_MASTER_REGISTER_PATH",
    "LEGACY_PROJECT_RULES_PATH",
    "DonorLegacyAccessSource",
    "LegacyItemSource",
    "LegacyProjectRuleSource",
    "load_character_donor_legacy_access",
    "load_character_legacy_package",
    "load_donor_legacy_access",
    "load_legacy_item",
    "load_legacy_items",
    "load_legacy_project_rules",
]
