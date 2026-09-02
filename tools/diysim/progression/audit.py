"""Build chapter-by-chapter character stat/loadout audit snapshots."""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

from ..sources.campaign_progression import (
    CAMPAIGN_LEVEL_SPINE_PATH,
    SUBCLASS_UNLOCK_CHAPTER,
    CharacterCampaignSource,
    load_campaign_checkpoint,
    load_campaign_level_targets,
    load_character_campaign_sources,
)
from ..sources.equipment import combine_equipment_bonuses
from ..sources.equipment_availability import STARTING_LOADOUTS_PATH, load_guaranteed_loadouts
from .loadouts import (
    ProgressionAssumption,
    ProgressionSourceGap,
    ResolvedLoadout,
    resolve_loadout,
    resolve_loadout_at_checkpoint,
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
    class_selection_explicit: bool
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
            "Class Selection": "Explicit" if self.class_selection_explicit else "Base floor",
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
            "Source Paths": "; ".join(self.source_paths),
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


def _resolve_selected_class(
    campaign: CharacterCampaignSource,
    chapter: int,
    selected_class: str | None,
) -> tuple[str, bool, list[ProgressionSourceGap], list[str]]:
    if selected_class is None:
        gaps: list[ProgressionSourceGap] = []
        paths = [campaign.class_source_path]
        if chapter >= SUBCLASS_UNLOCK_CHAPTER:
            gaps.append(
                ProgressionSourceGap(
                    "selected_class_route_missing",
                    "Subclasses are available at the end of Chapter 7 after Sixfold Volition, "
                    "but no selected class was supplied for this simulation checkpoint. "
                    "The native Base Class is retained as a source-backed floor snapshot.",
                    campaign.subclass_unlock_source_path,
                )
            )
            paths.append(campaign.subclass_unlock_source_path)
        return campaign.base_class, False, gaps, paths

    normalized = selected_class.strip().casefold()
    legal = {
        campaign.base_class.casefold(): (campaign.base_class, campaign.class_source_path),
        campaign.subclass.casefold(): (campaign.subclass, campaign.subclass_source_path),
    }
    resolved = legal.get(normalized)
    if resolved is None:
        choices = ", ".join(campaign.selectable_classes)
        raise ValueError(
            f"{selected_class!r} is not a selectable class for {campaign.character}. "
            f"Legal choices: {choices}."
        )

    class_name, source_path = resolved
    paths = [source_path]
    if class_name == campaign.subclass:
        if chapter < SUBCLASS_UNLOCK_CHAPTER:
            raise ValueError(
                f"{campaign.subclass} is not usable for {campaign.character} before the "
                f"Sixfold Volition at the end of Chapter {SUBCLASS_UNLOCK_CHAPTER}."
            )
        paths.append(campaign.subclass_unlock_source_path)
    return class_name, True, [], paths


def _validated_class_choices(
    class_choices: Mapping[str, str] | None,
    campaign_sources: tuple[CharacterCampaignSource, ...],
) -> dict[str, str]:
    choices = dict(class_choices or {})
    known = {row.character for row in campaign_sources}
    unknown = sorted(set(choices) - known)
    if unknown:
        raise ValueError(
            "Unknown permanent character in class choices: " + ", ".join(unknown)
        )
    return choices


def _build_character_audit(
    *,
    campaign: CharacterCampaignSource,
    chapter: int,
    checkpoint: str,
    assumption: ProgressionAssumption,
    level: int | None,
    loadout: ResolvedLoadout,
    level_gaps: list[ProgressionSourceGap],
    level_paths: list[str],
    selected_class: str | None,
    root: Path | None,
) -> CharacterLoadoutAudit:
    class_name, class_selection_explicit, class_gaps, class_paths = _resolve_selected_class(
        campaign,
        chapter,
        selected_class,
    )

    stats: Stats | None = None
    evasion: int | None = None
    status_resistance: int | None = None
    if level is not None and loadout.slots_complete:
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
        character=campaign.character,
        level=level,
        class_name=class_name,
        class_selection_explicit=class_selection_explicit,
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


def audit_character_checkpoint(
    character: str,
    chapter: int,
    assumption: ProgressionAssumption = "mandatory",
    *,
    selected_class: str | None = None,
    root: Path | None = None,
) -> CharacterLoadoutAudit:
    """Calculate a source-backed end-of-chapter character snapshot."""
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
    return _build_character_audit(
        campaign=campaign,
        chapter=chapter,
        checkpoint=checkpoint,
        assumption=assumption,
        level=level,
        loadout=loadout,
        level_gaps=level_gaps,
        level_paths=level_paths,
        selected_class=selected_class,
        root=root,
    )


def audit_character_named_checkpoint(
    character: str,
    checkpoint_key: str,
    assumption: ProgressionAssumption = "mandatory",
    *,
    selected_class: str | None = None,
    root: Path | None = None,
) -> CharacterLoadoutAudit:
    """Audit one exact named campaign checkpoint from current repository authority."""
    campaign_sources = {
        row.character: row for row in load_character_campaign_sources(root=root)
    }
    campaign = campaign_sources.get(character)
    if campaign is None:
        raise KeyError(f"Unknown permanent character in campaign authority: {character}")

    checkpoint = load_campaign_checkpoint(checkpoint_key, root=root)
    loadout = resolve_loadout_at_checkpoint(
        character,
        checkpoint.key,
        assumption,
        root=root,
    )
    level_gaps: list[ProgressionSourceGap] = []
    if assumption != "mandatory":
        level_gaps.append(
            ProgressionSourceGap(
                "route_specific_level_target_missing",
                f"{assumption} has no distinct named-checkpoint level target; using the "
                "published campaign-only target as a source-backed floor.",
                checkpoint.source_path,
            )
        )

    return _build_character_audit(
        campaign=campaign,
        chapter=checkpoint.chapter,
        checkpoint=checkpoint.label,
        assumption=assumption,
        level=checkpoint.level,
        loadout=loadout,
        level_gaps=level_gaps,
        level_paths=[checkpoint.source_path],
        selected_class=selected_class,
        root=root,
    )


def audit_campaign_checkpoint(
    chapter: int,
    assumption: ProgressionAssumption = "mandatory",
    *,
    class_choices: Mapping[str, str] | None = None,
    root: Path | None = None,
) -> tuple[CharacterLoadoutAudit, ...]:
    campaign_sources = load_character_campaign_sources(root=root)
    choices = _validated_class_choices(class_choices, campaign_sources)
    return tuple(
        audit_character_checkpoint(
            row.character,
            chapter,
            assumption,
            selected_class=choices.get(row.character),
            root=root,
        )
        for row in campaign_sources
        if row.recruitment_chapter <= chapter
    )


def audit_campaign_named_checkpoint(
    checkpoint_key: str,
    assumption: ProgressionAssumption = "mandatory",
    *,
    class_choices: Mapping[str, str] | None = None,
    root: Path | None = None,
) -> tuple[CharacterLoadoutAudit, ...]:
    checkpoint = load_campaign_checkpoint(checkpoint_key, root=root)
    campaign_sources = load_character_campaign_sources(root=root)
    choices = _validated_class_choices(class_choices, campaign_sources)
    return tuple(
        audit_character_named_checkpoint(
            row.character,
            checkpoint.key,
            assumption,
            selected_class=choices.get(row.character),
            root=root,
        )
        for row in campaign_sources
        if row.recruitment_chapter <= checkpoint.chapter
    )


def audit_campaign(
    assumption: ProgressionAssumption = "mandatory",
    *,
    start_chapter: int = 0,
    end_chapter: int = 13,
    class_choices: Mapping[str, str] | None = None,
    root: Path | None = None,
) -> tuple[CharacterLoadoutAudit, ...]:
    if start_chapter < 0 or end_chapter < start_chapter:
        raise ValueError("Invalid campaign chapter range")
    campaign_sources = load_character_campaign_sources(root=root)
    choices = _validated_class_choices(class_choices, campaign_sources)
    rows: list[CharacterLoadoutAudit] = []
    for chapter in range(start_chapter, end_chapter + 1):
        rows.extend(
            audit_campaign_checkpoint(
                chapter,
                assumption,
                class_choices=choices,
                root=root,
            )
        )
    return tuple(rows)


__all__ = [
    "CharacterLoadoutAudit",
    "audit_campaign",
    "audit_campaign_checkpoint",
    "audit_campaign_named_checkpoint",
    "audit_character_checkpoint",
    "audit_character_named_checkpoint",
]
