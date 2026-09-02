"""Explicit, source-bounded Legacy project completion proof.

Legacy availability is not ownership. This module validates an explicit completed
item against the native owner's class state and authored project requirements.
Because the repo does not yet publish Kessara's exact Legacy-service opening chapter,
validation is deliberately conservative: completed projects are supported only from
end Chapter 12 through Last Shelter, where the current sources prove all dated
prerequisite lanes can already be available.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from ..sources.campaign_progression import CLASS_SYSTEM_MASTER_PATH, load_campaign_checkpoint
from ..sources.equipment import EQUIPMENT_REGISTER_PATH, load_equipment
from ..sources.legacies import (
    CHARACTER_QUEST_LEGACY_COMPONENTS_PATH,
    CHARACTER_QUEST_LEGACY_HANDOFF_PATH,
    CHARACTER_QUEST_MASTER_REGISTER_PATH,
    FORGE_COMPONENT_SOURCE_MATRIX_PATH,
    LEGACY_MASTER_REGISTER_PATH,
    LEGACY_PRECURSORS_PATH,
    LEGACY_PROJECT_RULES_PATH,
    load_legacy_character_project,
    load_legacy_endgame_project_window,
    load_legacy_item,
    load_legacy_project_rules,
)
from .class_exp import ClassCexpState, class_level_from_cexp
from .class_state import validate_class_state_at_checkpoint

_SUPPORTED_CHECKPOINTS = frozenset({"end_ch12", "ch13_start", "ch13_last_shelter"})


@dataclass(frozen=True)
class LegacyProjectEvidence:
    """Explicit scenario facts that availability documents cannot prove as ownership."""

    character_quest_complete: bool = False
    precursor_owned: bool = False
    gate_a_owned: bool = False
    gate_b_owned: bool = False
    kessara_project_available: bool = False
    completed_items: frozenset[str] = field(default_factory=frozenset)

    def __post_init__(self) -> None:
        object.__setattr__(self, "completed_items", frozenset(self.completed_items))

    def proves_completed_item(self, legacy: str) -> bool:
        target = legacy.casefold()
        return any(name.casefold() == target for name in self.completed_items)


@dataclass(frozen=True)
class LegacyProjectProof:
    class_state: ClassCexpState
    evidence: LegacyProjectEvidence


@dataclass(frozen=True)
class LegacyItemCheckpointValidation:
    character: str
    legacy: str
    checkpoint_key: str
    is_weapon: bool
    gate_b_required: bool
    source_paths: tuple[str, ...]


def validate_native_legacy_item_at_checkpoint(
    character: str,
    legacy: str,
    checkpoint_key: str,
    proof: LegacyProjectProof,
    *,
    root: Path | None = None,
) -> LegacyItemCheckpointValidation:
    """Validate an explicitly completed native Legacy item at a supported checkpoint."""
    checkpoint = load_campaign_checkpoint(checkpoint_key, root=root)
    item = load_legacy_item(legacy, root=root)
    if item.character.casefold() != character.casefold():
        raise ValueError(
            f"{item.legacy} belongs to {item.character}'s native Legacy package, not {character}'s."
        )

    validate_class_state_at_checkpoint(character, checkpoint.key, proof.class_state, root=root)
    rules = load_legacy_project_rules(root=root)
    base_cl = class_level_from_cexp(proof.class_state.base_cexp, root=root)
    if base_cl < rules.native_base_class_level:
        raise ValueError(
            f"{item.legacy} requires {character}'s native Base Class CL{rules.native_base_class_level}; "
            f"the supplied project-owner state is only Base CL{base_cl}."
        )

    # Current Class-System authority unlocks all four native Core Masteries by Base
    # CL12, so the stricter Base CL13 project requirement also proves that prerequisite.
    project = load_legacy_character_project(character, root=root)
    window = load_legacy_endgame_project_window(root=root)
    if checkpoint.key not in _SUPPORTED_CHECKPOINTS:
        if checkpoint.chapter < window.safe_completion_chapter or checkpoint.key == "end_ch11":
            raise ValueError(
                "Current repo authority does not prove Kessara's exact Legacy-project opening "
                "before late Chapter 12. DiySim conservatively validates completed Legacy "
                "projects only at end_ch12, ch13_start, or ch13_last_shelter."
            )
        raise ValueError(
            "Legacy project validation ends at Last Shelter; the authored final cutoff is "
            "Last Shelter → Reactor Galleries."
        )

    evidence = proof.evidence
    if not evidence.character_quest_complete:
        raise ValueError(
            f"{item.legacy} requires completion of {character}'s Character Quest "
            f"({project.quest}); quest availability alone is not completion."
        )
    # The quest handoff explicitly grants that character's unique Legacy Component at
    # completion, so a separate assumed-ownership flag would duplicate source authority.
    if not evidence.precursor_owned:
        raise ValueError(
            f"{item.legacy} requires {character}'s Legacy precursor to be explicitly owned."
        )
    if not evidence.gate_a_owned:
        raise ValueError(f"{item.legacy} requires the native Legacy Gate A material to be owned.")
    if not evidence.kessara_project_available:
        raise ValueError(
            f"{item.legacy} requires explicit Kessara project availability for this scenario."
        )

    equipment = load_equipment(item.legacy, root=root)
    is_weapon = equipment.equipment_type.casefold() == "weapon"
    gate_b_required = not is_weapon
    if gate_b_required and not evidence.gate_b_owned:
        raise ValueError(
            f"{item.legacy} is not the package weapon and therefore requires native Legacy Gate B."
        )
    if not evidence.proves_completed_item(item.legacy):
        raise ValueError(
            f"{item.legacy} is available/eligible but not explicitly proven forged/completed. "
            "Add the exact item to completed_items only when the project actually exists."
        )

    return LegacyItemCheckpointValidation(
        character=character,
        legacy=item.legacy,
        checkpoint_key=checkpoint.key,
        is_weapon=is_weapon,
        gate_b_required=gate_b_required,
        source_paths=(
            LEGACY_MASTER_REGISTER_PATH,
            LEGACY_PROJECT_RULES_PATH,
            CLASS_SYSTEM_MASTER_PATH,
            CHARACTER_QUEST_MASTER_REGISTER_PATH,
            CHARACTER_QUEST_LEGACY_COMPONENTS_PATH,
            CHARACTER_QUEST_LEGACY_HANDOFF_PATH,
            LEGACY_PRECURSORS_PATH,
            FORGE_COMPONENT_SOURCE_MATRIX_PATH,
            EQUIPMENT_REGISTER_PATH,
        ),
    )


__all__ = [
    "LegacyItemCheckpointValidation",
    "LegacyProjectEvidence",
    "LegacyProjectProof",
    "validate_native_legacy_item_at_checkpoint",
]
