"""Build chapter-by-chapter character stat/loadout audit snapshots."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ..sources.campaign_progression import (
    CAMPAIGN_LEVEL_SPINE_PATH,
    load_campaign_level_targets,
    load_character_campaign_sources,
)
from ..sources.equipment import combine_equipment_bonuses
from ..sources.equipment_availability import STARTING_LOADOUTS_PATH, load_guaranteed_loadouts
from .loadouts import (
    ProgressionAssumption,
    ProgressionSourceGap,
    resolve_loadout,
)
from .stats import Stats, natural_stats


@dataclass(frozen=True)
class CharacterLoadoutAudit:
    chapter: int
    checkpoint: str
    assumption: ProgressionAssumption
    character: str
    level: int | None
    class_name: str | None
    weapon: str | None
    armor: str | None
    secondary: str | None
    secondary_consumed_by_weapon: bool
    stats: Stats | None
    evasion: int | None
    status_resistance: int | None
    source_gaps: tuple[ProgressionSourceGap, ...]
    source_paths: tuple[str, ...]

    @property
    def authority_complete(self) -> bool:
        return self.stats is not None and not self.source_gaps

    def as_dict(self) -> dict[str, object]:
        stats = self.stats
        return {
            "Chapter": self.chapter,
            "Checkpoint": self.checkpoint,
            "Route": self.assumption,
            "Character": self.character,
            "Level": self.level,
            "Class": self.class_name,
            "Weapon": self.weapon,
            "Armor": self.armor,
            "Secondary": (
                "Consumed by Weapon" if self.secondary_consumed_by_weapon else self.secondary
            ),
            "HP": stats.hp if stats else None,
            "MP": stats.mp if stats else None,
            "ATK": stats.attack if stats else None,
            "MAG": stats.magic if stats else None,
            "DEF": stats.defense if stats else None,
            "SPR": stats.spirit if stats else None,
            "SPD": stats.speed if stats else None,
            "EVA": self.evasion,
            "Status Resistance": self.status_resistance,
            "Authority Complete": self.authority_complete,
            "Source Gaps": "; ".join(gap.code for gap in self.source_gaps),
        }


def _checkpoint_level(
    character: str,
    chapter: int,
    assumption: ProgressionAssumption,
    *,
    root: Path | None,
) -> tuple[int | None, str, list[ProgressionSourceGap], list[str]]:
    gaps: list[ProgressionSourceGap] = []
    paths: list[str] = []

    if chapter == 0:
        row = next(
            (
                item
                for item in load_guaranteed_loadouts(root=root)
                if item.character == character and item.chapter == 0
            ),
            None,
        )
        level = row.level if row else None
        if level is None:
            gaps.append(
                ProgressionSourceGap(
                    "chapter0_level_missing",
                    f"No source-backed Chapter-0 Player Level was found for {character}.",
                    STARTING_LOADOUTS_PATH,
                )
            )
        else:
            paths.append(STARTING_LOADOUTS_PATH)
        return level, "Chapter 0", gaps, paths

    target = next(
        (row for row in load_campaign_level_targets(root=root) if row.chapter == chapter),
        None,
    )
    if target is None:
        gaps.append(
            ProgressionSourceGap(
                "campaign_level_checkpoint_missing",
                f"No campaign-only end-Chapter-{chapter} level target is published.",
                CAMPAIGN_LEVEL_SPINE_PATH,
            )
        )
        return None, f"End Ch{chapter}", gaps, paths

    paths.append(target.source_path)
    if assumption != "mandatory":
        gaps.append(
            ProgressionSourceGap(
                "route_specific_level_target_missing",
                f"{assumption} has no distinct chapter-level target; using the published "
                "campaign-only target as a source-backed floor.",
                target.source_path,
            )
        )
    return target.level, target.label, gaps, paths


def audit_character_checkpoint(
    character: str,
    chapter: int,
    assumption: ProgressionAssumption = "mandatory",
    *,
    root: Path | None = None,
) -> CharacterLoadoutAudit:
    """Calculate a source-backed character snapshot and expose every unresolved assumption."""
    campaign_sources = {
        row.character: row for row in load_character_campaign_sources(root=root)
    }
    campaign = campaign_sources.get(character)
    if campaign is None:
        raise KeyError(f"Unknown permanent character in campaign authority: {character}")

    loadout = resolve_loadout(character, chapter, assumption, root=root)
    level, checkpoint, level_gaps, level_paths = _checkpoint_level(
        character,
        chapter,
        assumption,
        root=root,
    )

    class_name: str | None = campaign.base_class
    class_gaps: list[ProgressionSourceGap] = []
    class_paths = [campaign.class_source_path]
    if chapter >= 8:
        class_gaps.append(
            ProgressionSourceGap(
                "selected_class_route_missing",
                "Subclasses are available after Sixfold Volition, but the repo does not "
                "define one required selected class for this route/checkpoint. The native "
                "Base Class is retained as a source-backed floor snapshot.",
                campaign.class_source_path,
            )
        )

    stats: Stats | None = None
    evasion: int | None = None
    status_resistance: int | None = None
    if level is not None and class_name is not None and loadout.slots_complete:
        equipment_bonuses, evasion_bonus, status_resistance_bonus = combine_equipment_bonuses(
            loadout.equipment_names,
            root=root,
        )
        stats = natural_stats(
            level,
            class_name,
            equipment_bonuses,
            root=root,
        )
        # Evasion and Status Resistance are not natural level-growth stats.
        # Static loadout snapshots therefore start from the combat model's neutral
        # baseline and add only source-backed permanent equipment bonuses.
        evasion = evasion_bonus
        status_resistance = status_resistance_bonus

    gaps = tuple((*loadout.source_gaps, *level_gaps, *class_gaps))
    source_paths = tuple(
        dict.fromkeys(
            (
                *loadout.source_paths,
                *level_paths,
                campaign.recruitment_source_path,
                *class_paths,
            )
        )
    )

    return CharacterLoadoutAudit(
        chapter=chapter,
        checkpoint=checkpoint,
        assumption=assumption,
        character=character,
        level=level,
        class_name=class_name,
        weapon=loadout.weapon,
        armor=loadout.armor,
        secondary=loadout.secondary,
        secondary_consumed_by_weapon=loadout.secondary_consumed_by_weapon,
        stats=stats,
        evasion=evasion,
        status_resistance=status_resistance,
        source_gaps=gaps,
        source_paths=source_paths,
    )


def audit_campaign_checkpoint(
    chapter: int,
    assumption: ProgressionAssumption = "mandatory",
    *,
    root: Path | None = None,
) -> tuple[CharacterLoadoutAudit, ...]:
    return tuple(
        audit_character_checkpoint(row.character, chapter, assumption, root=root)
        for row in load_character_campaign_sources(root=root)
        if row.recruitment_chapter <= chapter
    )


def audit_campaign(
    assumption: ProgressionAssumption = "mandatory",
    *,
    start_chapter: int = 0,
    end_chapter: int = 13,
    root: Path | None = None,
) -> tuple[CharacterLoadoutAudit, ...]:
    if start_chapter < 0 or end_chapter < start_chapter:
        raise ValueError("Invalid campaign chapter range")
    rows: list[CharacterLoadoutAudit] = []
    for chapter in range(start_chapter, end_chapter + 1):
        rows.extend(audit_campaign_checkpoint(chapter, assumption, root=root))
    return tuple(rows)


__all__ = [
    "CharacterLoadoutAudit",
    "audit_campaign",
    "audit_campaign_checkpoint",
    "audit_character_checkpoint",
]
