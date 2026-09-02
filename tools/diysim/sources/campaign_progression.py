"""Parse campaign checkpoint, recruitment, and native-class authority."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re
from typing import Literal

from .markdown import find_markdown_table
from .repo import SourceGapError, find_repo_root, read_repo_text

CAMPAIGN_LEVEL_SPINE_PATH = "docs/10_PROGRESSION_AND_EXP/CAMPAIGN_LEVEL_SPINE.md"
RECRUITMENT_PATH = "docs/10_PROGRESSION_AND_EXP/CLASS_RECRUITMENT_AND_STARTING_CEXP.md"
BASE_CLASSES_DIR = "docs/06_CLASSES_AND_ABILITIES/BASE_CLASSES"
SUBCLASSES_DIR = "docs/06_CLASSES_AND_ABILITIES/SUBCLASSES"
CLASS_SYSTEM_MASTER_PATH = "docs/06_CLASSES_AND_ABILITIES/CLASS_SYSTEM_MASTER.md"
SUBCLASS_UNLOCK_CHAPTER = 7
CheckpointKind = Literal["chapter_start", "chapter_internal", "chapter_end"]


@dataclass(frozen=True)
class CharacterCampaignSource:
    character: str
    recruitment_chapter: int
    base_class: str
    subclass: str
    recruitment_source_path: str = RECRUITMENT_PATH
    class_source_path: str = ""
    subclass_source_path: str = ""
    subclass_unlock_source_path: str = CLASS_SYSTEM_MASTER_PATH

    @property
    def selectable_classes(self) -> tuple[str, str]:
        return self.base_class, self.subclass


@dataclass(frozen=True)
class CampaignLevelTarget:
    chapter: int
    level: int
    label: str
    source_path: str = CAMPAIGN_LEVEL_SPINE_PATH


@dataclass(frozen=True)
class CampaignCheckpointSource:
    key: str
    chapter: int
    level: int
    label: str
    kind: CheckpointKind
    source_path: str = CAMPAIGN_LEVEL_SPINE_PATH

    @property
    def chapter_granular_equipment_cutoff(self) -> int:
        """Latest chapter whose availability is definitely reached at this checkpoint.

        End-of-chapter checkpoints can use equipment explicitly marked available in
        that chapter. Start/internal checkpoints cannot assume when an item with only
        chapter-granular timing appears, so the safe cutoff is the prior chapter.
        """
        return self.chapter if self.kind == "chapter_end" else max(0, self.chapter - 1)


def _load_owned_classes(
    root: Path,
    directory_path: str,
    *,
    class_kind: str,
) -> dict[str, tuple[str, str]]:
    directory = root / directory_path
    if not directory.is_dir():
        raise SourceGapError(f"Missing {class_kind} source directory: {directory_path}")

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
            raise SourceGapError(f"Multiple native {class_kind}s found for {owner}")
        owners[owner] = (class_name, relative)

    if not owners:
        raise SourceGapError(f"No native {class_kind} owners found under {directory_path}")
    return owners


def _validate_subclass_unlock(root: Path) -> None:
    text = read_repo_text(CLASS_SYSTEM_MASTER_PATH, root=root)
    match = re.search(
        r"Subclasses do not become usable before the \*\*Sixfold Volition at the end of Chapter (\d+)\*\*",
        text,
        re.I,
    )
    if not match:
        raise SourceGapError(
            f"Could not resolve Subclass unlock timing from {CLASS_SYSTEM_MASTER_PATH}"
        )
    if int(match.group(1)) != SUBCLASS_UNLOCK_CHAPTER:
        raise SourceGapError(
            "DiySim Subclass unlock constant disagrees with current class-system authority: "
            f"expected Chapter {SUBCLASS_UNLOCK_CHAPTER}, found Chapter {match.group(1)}"
        )


def _load_characters(root_string: str) -> tuple[CharacterCampaignSource, ...]:
    root = Path(root_string)
    text = read_repo_text(RECRUITMENT_PATH, root=root)
    table = find_markdown_table(text, ("Character", "Recruitment"))
    base_owners = _load_owned_classes(root, BASE_CLASSES_DIR, class_kind="Base Class")
    subclass_owners = _load_owned_classes(root, SUBCLASSES_DIR, class_kind="Subclass")
    _validate_subclass_unlock(root)
    rows: list[CharacterCampaignSource] = []

    for row in table:
        character = row["Character"]
        recruitment_match = re.search(r"\bCh(?:apter)?\s*(\d+)\b", row["Recruitment"], re.I)
        if not recruitment_match:
            raise SourceGapError(
                f"Unsupported recruitment chapter for {character}: {row['Recruitment']!r}"
            )
        base_info = base_owners.get(character)
        if base_info is None:
            raise SourceGapError(f"No native Base Class owner sheet found for {character}")
        subclass_info = subclass_owners.get(character)
        if subclass_info is None:
            raise SourceGapError(f"No native Subclass owner sheet found for {character}")
        base_name, base_path = base_info
        subclass_name, subclass_path = subclass_info
        rows.append(
            CharacterCampaignSource(
                character=character,
                recruitment_chapter=int(recruitment_match.group(1)),
                base_class=base_name,
                subclass=subclass_name,
                class_source_path=base_path,
                subclass_source_path=subclass_path,
            )
        )

    if not rows:
        raise SourceGapError(f"No recruitment rows found in {RECRUITMENT_PATH}")

    recruited = {row.character for row in rows}
    extra_base = sorted(set(base_owners) - recruited)
    extra_subclasses = sorted(set(subclass_owners) - recruited)
    if extra_base:
        raise SourceGapError(
            "Base-Class owner sheets exist for characters absent from recruitment authority: "
            + ", ".join(extra_base)
        )
    if extra_subclasses:
        raise SourceGapError(
            "Subclass owner sheets exist for characters absent from recruitment authority: "
            + ", ".join(extra_subclasses)
        )
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


def _load_checkpoints(root_string: str) -> tuple[CampaignCheckpointSource, ...]:
    root = Path(root_string)
    text = read_repo_text(CAMPAIGN_LEVEL_SPINE_PATH, root=root)
    checkpoints: list[CampaignCheckpointSource] = []

    for target in _load_level_targets(root_string):
        checkpoints.append(
            CampaignCheckpointSource(
                key=f"end_ch{target.chapter}",
                chapter=target.chapter,
                level=target.level,
                label=target.label,
                kind="chapter_end",
            )
        )

    anchor_specs = (
        ("ch13_start", "start Ch13", "chapter_start"),
        ("ch13_last_shelter", "Last Shelter", "chapter_internal"),
        ("ch13_ending", "ending", "chapter_end"),
    )
    for key, label, kind in anchor_specs:
        match = re.search(
            rf"^-\s*{re.escape(label)}\s*:\s*\*\*~?Lv(\d+)\b",
            text,
            re.I | re.M,
        )
        if match:
            checkpoints.append(
                CampaignCheckpointSource(
                    key=key,
                    chapter=13,
                    level=int(match.group(1)),
                    label=label if key != "ch13_ending" else "End Ch13 — The Last Command",
                    kind=kind,
                )
            )

    keys = [row.key for row in checkpoints]
    if len(keys) != len(set(keys)):
        raise SourceGapError(f"Duplicate campaign checkpoint keys in {CAMPAIGN_LEVEL_SPINE_PATH}")
    if not checkpoints:
        raise SourceGapError(f"No campaign checkpoints found in {CAMPAIGN_LEVEL_SPINE_PATH}")
    return tuple(checkpoints)


@lru_cache(maxsize=4)
def _cached_characters(root_string: str) -> tuple[CharacterCampaignSource, ...]:
    return _load_characters(root_string)


@lru_cache(maxsize=4)
def _cached_level_targets(root_string: str) -> tuple[CampaignLevelTarget, ...]:
    return _load_level_targets(root_string)


@lru_cache(maxsize=4)
def _cached_checkpoints(root_string: str) -> tuple[CampaignCheckpointSource, ...]:
    return _load_checkpoints(root_string)


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


def load_campaign_checkpoints(
    *, root: Path | None = None
) -> tuple[CampaignCheckpointSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _cached_checkpoints(str(repo))


def load_campaign_checkpoint(
    key: str,
    *,
    root: Path | None = None,
) -> CampaignCheckpointSource:
    normalized = key.strip().lower().replace("-", "_").replace(" ", "_")
    aliases = {
        "start_ch13": "ch13_start",
        "last_shelter": "ch13_last_shelter",
        "ending": "ch13_ending",
    }
    normalized = aliases.get(normalized, normalized)
    for checkpoint in load_campaign_checkpoints(root=root):
        if checkpoint.key == normalized:
            return checkpoint
    available = ", ".join(row.key for row in load_campaign_checkpoints(root=root))
    raise KeyError(f"Unknown campaign checkpoint {key!r}. Available: {available}")


__all__ = [
    "BASE_CLASSES_DIR",
    "CAMPAIGN_LEVEL_SPINE_PATH",
    "CLASS_SYSTEM_MASTER_PATH",
    "RECRUITMENT_PATH",
    "SUBCLASSES_DIR",
    "SUBCLASS_UNLOCK_CHAPTER",
    "CampaignCheckpointSource",
    "CampaignLevelTarget",
    "CharacterCampaignSource",
    "CheckpointKind",
    "load_campaign_checkpoint",
    "load_campaign_checkpoints",
    "load_campaign_level_targets",
    "load_character_campaign_sources",
]
