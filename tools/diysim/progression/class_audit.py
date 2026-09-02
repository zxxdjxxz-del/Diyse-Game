"""Named-checkpoint audits with explicit validated Class EXP state inputs."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from ..sources.campaign_progression import load_campaign_checkpoint, load_character_campaign_sources
from .audit import (
    CharacterLoadoutAudit,
    _build_character_audit,
    _validated_character_keys,
    _validated_class_choices,
    _validated_equipment_choices,
    audit_character_named_checkpoint,
)
from .class_exp import ClassCexpState
from .class_loadouts import resolve_class_aware_loadout_at_checkpoint
from .loadouts import ProgressionAssumption, ProgressionSourceGap


def audit_character_class_aware_named_checkpoint(
    character: str,
    checkpoint_key: str,
    assumption: ProgressionAssumption = "mandatory",
    *,
    selected_class: str | None = None,
    equipment_choices: Mapping[str, str] | None = None,
    class_state: ClassCexpState | None = None,
    root: Path | None = None,
) -> CharacterLoadoutAudit:
    """Audit one named checkpoint, optionally proving an explicit CEXP state.

    When no class state is supplied, this delegates to the existing named-checkpoint
    audit exactly. Supplying a class state activates mandatory-route CEXP validation
    and source-backed donor Ordinary equipment access at Subclass CL1/3/5.
    """
    if class_state is None:
        return audit_character_named_checkpoint(
            character,
            checkpoint_key,
            assumption,
            selected_class=selected_class,
            equipment_choices=equipment_choices,
            root=root,
        )

    campaign_sources = {
        row.character: row for row in load_character_campaign_sources(root=root)
    }
    campaign = campaign_sources.get(character)
    if campaign is None:
        raise KeyError(f"Unknown permanent character in campaign authority: {character}")

    checkpoint = load_campaign_checkpoint(checkpoint_key, root=root)
    loadout = resolve_class_aware_loadout_at_checkpoint(
        character,
        checkpoint.key,
        assumption,
        equipment_choices=equipment_choices,
        class_state=class_state,
        root=root,
    )
    level_gaps: list[ProgressionSourceGap] = []
    if assumption != "mandatory":
        # Normally unreachable when class_state is supplied because the class-aware
        # resolver rejects non-mandatory CEXP states. Kept for defensive parity.
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


def _validated_class_states(
    class_states: Mapping[str, ClassCexpState] | None,
    campaign_sources,
) -> dict[str, ClassCexpState]:
    values = _validated_character_keys(
        class_states,
        campaign_sources,
        kind="class-state",
    )
    result: dict[str, ClassCexpState] = {}
    for character, value in values.items():
        if not isinstance(value, ClassCexpState):
            raise TypeError(
                f"Class-state choice for {character} must be ClassCexpState, "
                f"got {type(value).__name__}."
            )
        result[character] = value
    return result


def audit_campaign_class_aware_named_checkpoint(
    checkpoint_key: str,
    assumption: ProgressionAssumption = "mandatory",
    *,
    class_choices: Mapping[str, str] | None = None,
    equipment_choices: Mapping[str, Mapping[str, str]] | None = None,
    class_states: Mapping[str, ClassCexpState] | None = None,
    root: Path | None = None,
) -> tuple[CharacterLoadoutAudit, ...]:
    """Audit all recruited characters at a named checkpoint with optional CEXP states."""
    checkpoint = load_campaign_checkpoint(checkpoint_key, root=root)
    campaign_sources = load_character_campaign_sources(root=root)
    classes = _validated_class_choices(class_choices, campaign_sources)
    equipment = _validated_equipment_choices(equipment_choices, campaign_sources)
    states = _validated_class_states(class_states, campaign_sources)
    return tuple(
        audit_character_class_aware_named_checkpoint(
            row.character,
            checkpoint.key,
            assumption,
            selected_class=classes.get(row.character),
            equipment_choices=equipment.get(row.character),
            class_state=states.get(row.character),
            root=root,
        )
        for row in campaign_sources
        if row.recruitment_chapter <= checkpoint.chapter
    )


__all__ = [
    "audit_campaign_class_aware_named_checkpoint",
    "audit_character_class_aware_named_checkpoint",
]
