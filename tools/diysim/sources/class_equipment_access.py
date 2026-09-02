"""Parse reciprocal donor relationships and Class-Level equipment access milestones."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re

from .campaign_progression import CLASS_SYSTEM_MASTER_PATH, load_character_campaign_sources
from .markdown import extract_markdown_table, parse_int
from .repo import SourceGapError, find_repo_root, read_repo_text


@dataclass(frozen=True)
class DonorEquipmentAccessSource:
    character: str
    donor_character: str
    primary_class_level: int
    armor_class_level: int
    secondary_class_level: int
    relic_class_level: int
    legacy_class_level: int
    source_path: str = CLASS_SYSTEM_MASTER_PATH

    def required_class_level(self, access_kind: str) -> int:
        normalized = access_kind.strip().casefold()
        mapping = {
            "primary": self.primary_class_level,
            "weapon": self.primary_class_level,
            "armor": self.armor_class_level,
            "secondary": self.secondary_class_level,
            "relic": self.relic_class_level,
            "legacy": self.legacy_class_level,
        }
        try:
            return mapping[normalized]
        except KeyError as exc:
            raise ValueError(f"Unknown donor equipment access kind: {access_kind}") from exc


def _milestone_from_table(text: str, phrase: str) -> int:
    rows = extract_markdown_table(text, "Subclass learning rhythm")
    matches: list[int] = []
    for row in rows:
        if phrase.casefold() not in row["Result"].casefold():
            continue
        matches.append(parse_int(row["Class Level"]))
    if len(matches) != 1:
        raise SourceGapError(
            f"Expected exactly one {phrase!r} milestone in {CLASS_SYSTEM_MASTER_PATH}, "
            f"found {len(matches)}"
        )
    return matches[0]


def _mastery_milestone(text: str, mastery: str, equipment: str) -> int:
    match = re.search(
        rf"Subclass\s+CL(\d+)\s*/\s*{re.escape(mastery)}\s+opens\s+class\s+eligibility\s+"
        rf"for\s+the\s+donor\s+Base-Class\s+{re.escape(equipment)}",
        text,
        re.I,
    )
    if not match:
        raise SourceGapError(
            f"Could not resolve donor {equipment} Class Level from {CLASS_SYSTEM_MASTER_PATH}"
        )
    return int(match.group(1))


def _load_access(root_string: str) -> tuple[DonorEquipmentAccessSource, ...]:
    root = Path(root_string)
    text = read_repo_text(CLASS_SYSTEM_MASTER_PATH, root=root)
    primary_cl = _milestone_from_table(text, "donor Primary access")
    armor_cl = _milestone_from_table(text, "donor Armor access")
    secondary_cl = _milestone_from_table(text, "donor Secondary access")
    relic_cl = _mastery_milestone(text, "Equipment Mastery", "Relic")
    legacy_cl = _mastery_milestone(text, "Legacy Mastery", "Legacy")

    pair_block = text.split("Reciprocal donor pairs:", 1)
    if len(pair_block) != 2:
        raise SourceGapError(f"Missing reciprocal donor-pair block in {CLASS_SYSTEM_MASTER_PATH}")
    pair_text = pair_block[1].split("##", 1)[0]
    pairs = re.findall(r"^-\s*(.+?)\s*⇄\s*(.+?)\s*$", pair_text, re.M)
    if not pairs:
        raise SourceGapError(f"No reciprocal donor pairs found in {CLASS_SYSTEM_MASTER_PATH}")

    donor_map: dict[str, str] = {}
    for left, right in pairs:
        left = left.strip()
        right = right.strip()
        if left in donor_map or right in donor_map:
            raise SourceGapError("A character appears in more than one reciprocal donor pair")
        donor_map[left] = right
        donor_map[right] = left

    characters = {row.character for row in load_character_campaign_sources(root=root)}
    if set(donor_map) != characters:
        missing = sorted(characters - set(donor_map))
        extra = sorted(set(donor_map) - characters)
        detail = []
        if missing:
            detail.append("missing: " + ", ".join(missing))
        if extra:
            detail.append("unknown: " + ", ".join(extra))
        raise SourceGapError(
            "Reciprocal donor pairs do not cover the permanent cast (" + "; ".join(detail) + ")"
        )

    return tuple(
        DonorEquipmentAccessSource(
            character=character,
            donor_character=donor_map[character],
            primary_class_level=primary_cl,
            armor_class_level=armor_cl,
            secondary_class_level=secondary_cl,
            relic_class_level=relic_cl,
            legacy_class_level=legacy_cl,
        )
        for character in sorted(characters)
    )


@lru_cache(maxsize=4)
def _cached_access(root_string: str) -> tuple[DonorEquipmentAccessSource, ...]:
    return _load_access(root_string)


def load_donor_equipment_access(
    *, root: Path | None = None
) -> tuple[DonorEquipmentAccessSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _cached_access(str(repo))


def load_character_donor_equipment_access(
    character: str,
    *,
    root: Path | None = None,
) -> DonorEquipmentAccessSource:
    for row in load_donor_equipment_access(root=root):
        if row.character.casefold() == character.casefold():
            return row
    raise KeyError(f"Unknown permanent character in donor-equipment authority: {character}")


__all__ = [
    "DonorEquipmentAccessSource",
    "load_character_donor_equipment_access",
    "load_donor_equipment_access",
]
