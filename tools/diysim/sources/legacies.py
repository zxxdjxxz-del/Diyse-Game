"""Repository-backed Legacy package, donor-access, and project authority.

This module inventories authored Legacy equipment and reciprocal donor relationships.
It also parses the character-keyed prerequisite sources needed to validate an explicit
endgame Legacy project. It deliberately does not infer inventory ownership or project
completion merely because a source has become available.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re

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
CHARACTER_QUEST_LEGACY_COMPONENTS_PATH = (
    "docs/08_ITEMS_AND_EQUIPMENT/LEGACIES/CHARACTER_QUEST_LEGACY_COMPONENTS.md"
)
LEGACY_PRECURSORS_PATH = (
    "docs/08_ITEMS_AND_EQUIPMENT/LEGACIES/LEGACY_PRECURSORS.md"
)
CHARACTER_QUEST_MASTER_REGISTER_PATH = (
    "docs/11_QUESTS/CHARACTER_QUESTS/CHARACTER_QUEST_MASTER_REGISTER.md"
)
CHARACTER_QUEST_LEGACY_HANDOFF_PATH = (
    "docs/11_QUESTS/CHARACTER_QUESTS/CHARACTER_QUEST_LEGACY_HANDOFF.md"
)
FORGE_COMPONENT_SOURCE_MATRIX_PATH = (
    "docs/08_ITEMS_AND_EQUIPMENT/MATERIALS/FORGE_COMPONENT_SOURCE_MATRIX.md"
)

_EXPECTED_CHARACTER_COUNTS = {
    "Cyanis": 3,
    "Ilyra": 4,
    "Torren": 2,
    "Nimera": 3,
    "Vaelira": 3,
    "Seyrik": 2,
}
_EXPECTED_CHARACTERS = frozenset(_EXPECTED_CHARACTER_COUNTS)


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


@dataclass(frozen=True)
class LegacyCharacterProjectSource:
    """Character-keyed dated prerequisites without exporting stale Face terminology."""

    character: str
    quest: str
    quest_unlock_after_chapter: int
    quest_component: str
    precursor_source: str
    precursor_earliest_chapter: int
    precursor_after_chapter: bool
    source_paths: tuple[str, ...] = (
        CHARACTER_QUEST_MASTER_REGISTER_PATH,
        CHARACTER_QUEST_LEGACY_HANDOFF_PATH,
        CHARACTER_QUEST_LEGACY_COMPONENTS_PATH,
        LEGACY_PRECURSORS_PATH,
    )


@dataclass(frozen=True)
class LegacyEndgameProjectWindowSource:
    """Conservative project window supported without a stale Face-name material join."""

    safe_completion_chapter: int
    legacy_gate_rows: int
    latest_legacy_gate_chapter: int
    last_supported_checkpoint: str
    source_paths: tuple[str, ...] = (
        CHARACTER_QUEST_LEGACY_HANDOFF_PATH,
        FORGE_COMPONENT_SOURCE_MATRIX_PATH,
    )


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
        "all four native core masteries": "all four native Core Masteries",
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


def _parse_quest_unlock_after_chapter(value: str) -> int:
    if "sixfold volition" in value.casefold():
        return 7
    match = re.search(r"after\s+Chapter\s*(\d+)", value, re.I)
    if not match:
        raise SourceGapError(f"Unsupported Character Quest unlock timing: {value!r}")
    return int(match.group(1))


def _parse_precursor_timing(value: str) -> tuple[int, bool]:
    after = re.search(r"after\s+Ch(?:apter)?\s*(\d+)", value, re.I)
    if after:
        return int(after.group(1)), True
    chapter = re.search(r"\bCh(?:apter)?\s*(\d+)\b", value, re.I)
    if chapter:
        return int(chapter.group(1)), False
    raise SourceGapError(f"Unsupported Legacy precursor timing: {value!r}")


@lru_cache(maxsize=4)
def _load_character_projects(root_string: str) -> tuple[LegacyCharacterProjectSource, ...]:
    root = Path(root_string)
    quest_text = read_repo_text(CHARACTER_QUEST_MASTER_REGISTER_PATH, root=root)
    component_text = read_repo_text(CHARACTER_QUEST_LEGACY_COMPONENTS_PATH, root=root)
    handoff_text = read_repo_text(CHARACTER_QUEST_LEGACY_HANDOFF_PATH, root=root)
    precursor_text = read_repo_text(LEGACY_PRECURSORS_PATH, root=root)

    quest_rows = find_markdown_table(
        quest_text,
        ("Character", "Quest", "Unlock", "Site", "Boss/climax", "EXP"),
    )
    component_rows = find_markdown_table(
        component_text,
        ("Character", "Character Quest source", "Item role"),
    )
    precursor_rows = find_markdown_table(
        precursor_text,
        ("Character", "Face", "Precursor source", "Earliest current availability"),
    )

    quest_by_character = {row["Character"].strip(): row for row in quest_rows}
    component_by_character = {row["Character"].strip(): row for row in component_rows}
    precursor_by_character = {row["Character"].strip(): row for row in precursor_rows}
    for label, mapping in (
        ("Character Quest", quest_by_character),
        ("Legacy Component", component_by_character),
        ("Legacy precursor", precursor_by_character),
    ):
        if frozenset(mapping) != _EXPECTED_CHARACTERS:
            raise SourceGapError(
                f"{label} authority does not cover the exact six permanent characters: "
                f"{sorted(mapping)}"
            )

    entries: list[LegacyCharacterProjectSource] = []
    for character in _EXPECTED_CHARACTER_COUNTS:
        quest_row = quest_by_character[character]
        component_row = component_by_character[character]
        precursor_row = precursor_by_character[character]
        quest = quest_row["Quest"].strip().strip("*")
        component_quest = component_row["Character Quest source"].strip().strip("*")
        if quest.casefold() != component_quest.casefold():
            raise SourceGapError(
                f"Character Quest/Legacy Component mismatch for {character}: "
                f"{quest!r} vs {component_quest!r}"
            )
        component_name = f"{character} Legacy Component"
        if component_name.casefold() not in handoff_text.casefold():
            raise SourceGapError(
                f"Character Quest handoff does not explicitly grant {component_name}"
            )
        precursor_chapter, precursor_after = _parse_precursor_timing(
            precursor_row["Earliest current availability"].strip()
        )
        entries.append(
            LegacyCharacterProjectSource(
                character=character,
                quest=quest,
                quest_unlock_after_chapter=_parse_quest_unlock_after_chapter(
                    quest_row["Unlock"].strip()
                ),
                quest_component=component_name,
                precursor_source=precursor_row["Precursor source"].strip(),
                precursor_earliest_chapter=precursor_chapter,
                precursor_after_chapter=precursor_after,
            )
        )
    return tuple(entries)


@lru_cache(maxsize=4)
def _load_endgame_window(root_string: str) -> LegacyEndgameProjectWindowSource:
    root = Path(root_string)
    handoff_text = read_repo_text(CHARACTER_QUEST_LEGACY_HANDOFF_PATH, root=root)
    matrix_text = read_repo_text(FORGE_COMPONENT_SOURCE_MATRIX_PATH, root=root)
    folded = handoff_text.casefold()
    for phrase in (
        "late chapter 12",
        "returnable early chapter 13",
        "through last shelter",
        "last shelter → reactor galleries",
    ):
        if phrase not in folded:
            raise SourceGapError(
                f"Character Quest Legacy handoff is missing endgame project-window authority: {phrase}"
            )

    rows = find_markdown_table(
        matrix_text,
        ("Face", "Material family", "Role", "Chapter", "Source type", "Source"),
    )
    # Face strings in this source include retired terminology. They are intentionally
    # ignored here. DiySim only proves the conservative point at which all twelve
    # Legacy-gate rows, regardless of source-key label, are already available.
    gate_rows = [row for row in rows if "legacy gate" in row["Role"].casefold()]
    if len(gate_rows) != 12:
        raise SourceGapError(
            f"Expected 12 Legacy Gate rows in {FORGE_COMPONENT_SOURCE_MATRIX_PATH}, "
            f"found {len(gate_rows)}"
        )
    chapters: list[int] = []
    for row in gate_rows:
        match = re.search(r"\bCh(?:apter)?\s*(\d+)\b", row["Chapter"], re.I)
        if not match:
            raise SourceGapError(f"Unsupported Legacy Gate chapter: {row['Chapter']!r}")
        chapters.append(int(match.group(1)))
    latest = max(chapters)
    if latest != 12:
        raise SourceGapError(
            "Conservative Legacy project window expects all Gate A/B sources to be "
            f"available by Chapter 12; latest parsed gate is Chapter {latest}."
        )

    projects = _load_character_projects(root_string)
    if max(row.quest_unlock_after_chapter for row in projects) > 10:
        raise SourceGapError("A Character Quest unlock now extends beyond the Chapter-10 boundary")
    if max(row.precursor_earliest_chapter for row in projects) > 12:
        raise SourceGapError("A Legacy precursor now extends beyond the Chapter-12 boundary")

    return LegacyEndgameProjectWindowSource(
        safe_completion_chapter=12,
        legacy_gate_rows=len(gate_rows),
        latest_legacy_gate_chapter=latest,
        last_supported_checkpoint="ch13_last_shelter",
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


def load_legacy_character_projects(
    *, root: Path | None = None
) -> tuple[LegacyCharacterProjectSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _load_character_projects(str(repo))


def load_legacy_character_project(
    character: str,
    *,
    root: Path | None = None,
) -> LegacyCharacterProjectSource:
    for row in load_legacy_character_projects(root=root):
        if row.character.casefold() == character.casefold():
            return row
    raise KeyError(f"Unknown permanent character in Legacy project authority: {character}")


def load_legacy_endgame_project_window(
    *, root: Path | None = None
) -> LegacyEndgameProjectWindowSource:
    repo = (root or find_repo_root()).resolve()
    return _load_endgame_window(str(repo))


__all__ = [
    "CHARACTER_QUEST_LEGACY_COMPONENTS_PATH",
    "CHARACTER_QUEST_LEGACY_HANDOFF_PATH",
    "CHARACTER_QUEST_MASTER_REGISTER_PATH",
    "DONOR_LEGACY_ACCESS_PATH",
    "FORGE_COMPONENT_SOURCE_MATRIX_PATH",
    "LEGACY_MASTER_REGISTER_PATH",
    "LEGACY_PRECURSORS_PATH",
    "LEGACY_PROJECT_RULES_PATH",
    "DonorLegacyAccessSource",
    "LegacyCharacterProjectSource",
    "LegacyEndgameProjectWindowSource",
    "LegacyItemSource",
    "LegacyProjectRuleSource",
    "load_character_donor_legacy_access",
    "load_character_legacy_package",
    "load_donor_legacy_access",
    "load_legacy_character_project",
    "load_legacy_character_projects",
    "load_legacy_endgame_project_window",
    "load_legacy_item",
    "load_legacy_items",
    "load_legacy_project_rules",
]
