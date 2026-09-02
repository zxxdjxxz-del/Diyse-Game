"""Parse campaign checkpoint, recruitment, and native-class authority."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re

from .markdown import find_markdown_table
from .repo import SourceGapError, find_repo_root, read_repo_text

CAMPAIGN_LEVEL_SPINE_PATH = "docs/10_PROGRESSION_AND_EXP/CAMPAIGN_LEVEL_SPINE.md"
RECRUITMENT_PATH = "docs/10_PROGRESSION_AND_EXP/CLASS_RECRUITMENT_AND_STARTING_CEXP.md"
BASE_CLASSES_DIR = "docs/06_CLASSES_AND_ABILITIES/BASE_CLASSES"


@dataclass(frozen=True)
class CharacterCampaignSource:
    character: str
    recruitment_chapter: int
    base_class: str
    recruitment_source_path: str = RECRUITMENT_PATH
    class_source_path: str = ""


@dataclass(frozen=True)
class CampaignLevelTarget:
    chapter: int
    level: int
    label: str
    source_path: str = CAMPAIGN_LEVEL_SPINE_PATH


def _load_class_owners(root: Path) -> dict[str, tuple[str, str]]:
    directory = root / BASE_CLASSES_DIR
    if not directory.is_dir():
        raise SourceGapError(f"Missing Base-Class source directory: {BASE_CLASSES_DIR}")

    owners: dict[str, tuple[str, str]] = {}
    for path in sorted(directory.glob("*.md")):
        relative = str(path.relative_to(root))
        text = read_repo_text(relative, root=root)
        class_match = re.search(r"^#\s+Diyse\s+—\s+(.+?)\s*$", text, re.M)
        owner_match = re.search(r"^\*\*Owner:\*\*\s*(.+?)\s*$", text, re.M)
        if not (class_match and owner_match):
            continue
        class_name = class_match.group(1).strip()
        owner = owner_match.group(1).strip()
        if owner in owners:
            raise SourceGapError(f"Multiple native Base Classes found for {owner}")
        owners[owner] = (class_name, relative)

    if not owners:
        raise SourceGapError(f"No native Base-Class owners found under {BASE_CLASSES_DIR}")
    return owners


def _load_characters(root_string: str) -> tuple[CharacterCampaignSource, ...]:
    root = Path(root_string)
    text = read_repo_text(RECRUITMENT_PATH, root=root)
    table = find_markdown_table(text, ("Character", "Recruitment"))
    class_owners = _load_class_owners(root)
    rows: list[CharacterCampaignSource] = []

    for row in table:
        character = row["Character"]
        recruitment_match = re.search(r"\bCh(?:apter)?\s*(\d+)\b", row["Recruitment"], re.I)
        if not recruitment_match:
            raise SourceGapError(
                f"Unsupported recruitment chapter for {character}: {row['Recruitment']!r}"
            )
        class_info = class_owners.get(character)
        if class_info is None:
            raise SourceGapError(f"No native Base Class owner sheet found for {character}")
        class_name, class_path = class_info
        rows.append(
            CharacterCampaignSource(
                character=character,
                recruitment_chapter=int(recruitment_match.group(1)),
                base_class=class_name,
                class_source_path=class_path,
            )
        )

    if not rows:
        raise SourceGapError(f"No recruitment rows found in {RECRUITMENT_PATH}")
    return tuple(rows)


def _load_level_targets(root_string: str) -> tuple[CampaignLevelTarget, ...]:
    root = Path(root_string)
    text = read_repo_text(CAMPAIGN_LEVEL_SPINE_PATH, root=root)
    table = find_markdown_table(text, ("Progress point", "Campaign-only target"))
    rows: list[CampaignLevelTarget] = []

    for row in table:
        chapter_match = re.search(r"\bEnd Ch(?:apter)?\s*(\d+)\b", row["Progress point"], re.I)
        level_match = re.search(r"\bLv\s*(\d+)\b", row["Campaign-only target"], re.I)
        if not (chapter_match and level_match):
            continue
        rows.append(
            CampaignLevelTarget(
                chapter=int(chapter_match.group(1)),
                level=int(level_match.group(1)),
                label=row["Progress point"],
            )
        )

    if not rows:
        raise SourceGapError(f"No end-chapter level targets found in {CAMPAIGN_LEVEL_SPINE_PATH}")
    return tuple(rows)


@lru_cache(maxsize=4)
def _cached_characters(root_string: str) -> tuple[CharacterCampaignSource, ...]:
    return _load_characters(root_string)


@lru_cache(maxsize=4)
def _cached_level_targets(root_string: str) -> tuple[CampaignLevelTarget, ...]:
    return _load_level_targets(root_string)


def load_character_campaign_sources(
    *, root: Path | None = None
) -> tuple[CharacterCampaignSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _cached_characters(str(repo))


def load_campaign_level_targets(
    *, root: Path | None = None
) -> tuple[CampaignLevelTarget, ...]:
    repo = (root or find_repo_root()).resolve()
    return _cached_level_targets(str(repo))


__all__ = [
    "BASE_CLASSES_DIR",
    "CAMPAIGN_LEVEL_SPINE_PATH",
    "RECRUITMENT_PATH",
    "CampaignLevelTarget",
    "CharacterCampaignSource",
    "load_campaign_level_targets",
    "load_character_campaign_sources",
]
