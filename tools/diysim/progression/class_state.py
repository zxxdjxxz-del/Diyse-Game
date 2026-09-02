"""Validate explicit Base/Subclass CEXP states against campaign checkpoint authority."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ..sources.campaign_progression import load_campaign_checkpoint
from ..sources.class_exp import load_character_starting_cexp
from .class_exp import (
    CLASS_CEXP_CAP,
    ClassCexpState,
    class_state_at_volition,
    mandatory_base_cexp_at_end_chapter,
    post_volition_cexp_available_at_checkpoint,
)


@dataclass(frozen=True)
class ClassCexpCheckpointValidation:
    character: str
    checkpoint_key: str
    checkpoint_label: str
    state: ClassCexpState
    volition_state: ClassCexpState | None
    post_volition_cexp_available: int
    post_volition_cexp_applied: int
    post_volition_cexp_lost: int

    @property
    def exact_no_loss(self) -> bool:
        return self.post_volition_cexp_lost == 0

    def as_dict(self) -> dict[str, object]:
        return {
            "character": self.character,
            "checkpoint_key": self.checkpoint_key,
            "checkpoint_label": self.checkpoint_label,
            "state": self.state.as_dict(),
            "volition_state": self.volition_state.as_dict() if self.volition_state else None,
            "post_volition_cexp_available": self.post_volition_cexp_available,
            "post_volition_cexp_applied": self.post_volition_cexp_applied,
            "post_volition_cexp_lost": self.post_volition_cexp_lost,
            "exact_no_loss": self.exact_no_loss,
        }


def validate_class_state_at_checkpoint(
    character: str,
    checkpoint_key: str,
    state: ClassCexpState,
    *,
    root: Path | None = None,
) -> ClassCexpCheckpointValidation:
    """Prove that an explicit class state is possible on the mandatory CEXP stream.

    Before Sixfold Volition, only the Base Class can receive CEXP, so the state is
    exact. From Volition onward, the repository does not define one mandatory
    Base/Subclass selection policy. A supplied state is therefore accepted when
    its gains can consume no more than the published post-Volition stream.

    Any difference between published CEXP and applied gains must be explainable by
    the current rule that CEXP fed to a selected CL13 class is lost rather than
    spilling to the other class. Consequently, a positive loss is only possible
    when at least one class is capped in the supplied final state.
    """
    checkpoint = load_campaign_checkpoint(checkpoint_key, root=root)
    starts = {row.character: row for row in load_character_starting_cexp(root=root)}
    source = starts.get(character)
    if source is None:
        raise KeyError(f"Unknown permanent character in CEXP authority: {character}")
    if checkpoint.chapter < source.recruitment_chapter:
        raise ValueError(
            f"{character} is not recruited by {checkpoint.label}; recruitment is Chapter "
            f"{source.recruitment_chapter}."
        )

    if checkpoint.chapter <= 7:
        expected = ClassCexpState(
            base_cexp=mandatory_base_cexp_at_end_chapter(
                character,
                checkpoint.chapter,
                root=root,
            ),
            subclass_cexp=0,
        )
        if state != expected:
            raise ValueError(
                f"Impossible Class CEXP state for {character} at {checkpoint.label}: "
                f"mandatory authority requires Base {expected.base_cexp} / Subclass 0, "
                f"got Base {state.base_cexp} / Subclass {state.subclass_cexp}."
            )
        return ClassCexpCheckpointValidation(
            character=character,
            checkpoint_key=checkpoint.key,
            checkpoint_label=checkpoint.label,
            state=state,
            volition_state=expected if checkpoint.chapter == 7 else None,
            post_volition_cexp_available=0,
            post_volition_cexp_applied=0,
            post_volition_cexp_lost=0,
        )

    volition = class_state_at_volition(character, root=root)
    if state.base_cexp < volition.base_cexp:
        raise ValueError(
            f"Impossible Base CEXP regression for {character} at {checkpoint.label}: "
            f"Volition starts at {volition.base_cexp}, got {state.base_cexp}."
        )

    available = post_volition_cexp_available_at_checkpoint(checkpoint.key, root=root)
    base_gain = state.base_cexp - volition.base_cexp
    subclass_gain = state.subclass_cexp
    applied = base_gain + subclass_gain
    if applied > available:
        raise ValueError(
            f"Impossible Class CEXP state for {character} at {checkpoint.label}: "
            f"state requires {applied} post-Volition CEXP but only {available} mandatory "
            "CEXP is published by this checkpoint."
        )

    lost = available - applied
    if lost and state.base_cexp < CLASS_CEXP_CAP and state.subclass_cexp < CLASS_CEXP_CAP:
        raise ValueError(
            f"Impossible unaccounted CEXP for {character} at {checkpoint.label}: "
            f"{lost} mandatory CEXP would have to be lost, but neither Base nor Subclass "
            "is at CL13. CEXP can only be lost when fed to a capped selected class."
        )

    return ClassCexpCheckpointValidation(
        character=character,
        checkpoint_key=checkpoint.key,
        checkpoint_label=checkpoint.label,
        state=state,
        volition_state=volition,
        post_volition_cexp_available=available,
        post_volition_cexp_applied=applied,
        post_volition_cexp_lost=lost,
    )


__all__ = [
    "ClassCexpCheckpointValidation",
    "validate_class_state_at_checkpoint",
]
