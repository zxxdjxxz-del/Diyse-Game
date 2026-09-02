"""Exact Class EXP math and explicit Base/Subclass CEXP allocation."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from ..sources.campaign_progression import load_campaign_checkpoint
from ..sources.class_exp import (
    CLASS_CEXP_CAP,
    CLASS_LEVEL_CAP,
    load_campaign_cexp_budgets,
    load_character_starting_cexp,
    load_chapter13_cexp_split,
    load_class_level_thresholds,
)

ClassTrack = Literal["base", "subclass"]


@dataclass(frozen=True)
class ClassCexpState:
    base_cexp: int = 0
    subclass_cexp: int = 0

    def __post_init__(self) -> None:
        for label, value in (
            ("base_cexp", self.base_cexp),
            ("subclass_cexp", self.subclass_cexp),
        ):
            if not 0 <= value <= CLASS_CEXP_CAP:
                raise ValueError(f"{label} must be between 0 and {CLASS_CEXP_CAP}")

    @property
    def base_class_level(self) -> int:
        return class_level_from_cexp(self.base_cexp)

    @property
    def subclass_class_level(self) -> int:
        return class_level_from_cexp(self.subclass_cexp)

    @property
    def complete(self) -> bool:
        return self.base_cexp == CLASS_CEXP_CAP and self.subclass_cexp == CLASS_CEXP_CAP

    def as_dict(self) -> dict[str, int | bool]:
        return {
            "base_cexp": self.base_cexp,
            "base_class_level": self.base_class_level,
            "subclass_cexp": self.subclass_cexp,
            "subclass_class_level": self.subclass_class_level,
            "complete": self.complete,
        }


@dataclass(frozen=True)
class CexpAwardResult:
    track: ClassTrack
    requested_cexp: int
    applied_cexp: int
    lost_cexp: int
    before: ClassCexpState
    after: ClassCexpState


@dataclass(frozen=True)
class CexpAllocationSegment:
    label: str
    cexp: int
    selected_track: ClassTrack

    def __post_init__(self) -> None:
        if self.cexp < 0:
            raise ValueError("CEXP allocation segment cannot be negative")


@dataclass(frozen=True)
class CexpAllocationCheckpoint:
    label: str
    selected_track: ClassTrack
    requested_cexp: int
    applied_cexp: int
    lost_cexp: int
    state: ClassCexpState


@dataclass(frozen=True)
class CexpAllocationProjection:
    start: ClassCexpState
    checkpoints: tuple[CexpAllocationCheckpoint, ...]

    @property
    def final(self) -> ClassCexpState:
        return self.checkpoints[-1].state if self.checkpoints else self.start

    @property
    def total_requested_cexp(self) -> int:
        return sum(row.requested_cexp for row in self.checkpoints)

    @property
    def total_applied_cexp(self) -> int:
        return sum(row.applied_cexp for row in self.checkpoints)

    @property
    def total_lost_cexp(self) -> int:
        return sum(row.lost_cexp for row in self.checkpoints)

    def as_dict(self) -> dict[str, object]:
        return {
            "start": self.start.as_dict(),
            "checkpoints": [
                {
                    "label": row.label,
                    "selected_track": row.selected_track,
                    "requested_cexp": row.requested_cexp,
                    "applied_cexp": row.applied_cexp,
                    "lost_cexp": row.lost_cexp,
                    **row.state.as_dict(),
                }
                for row in self.checkpoints
            ],
            "final": self.final.as_dict(),
            "total_requested_cexp": self.total_requested_cexp,
            "total_applied_cexp": self.total_applied_cexp,
            "total_lost_cexp": self.total_lost_cexp,
        }


def _thresholds(*, root: Path | None = None):
    return load_class_level_thresholds(root=root)


def class_level_from_cexp(cexp: int, *, root: Path | None = None) -> int:
    """Return current CL from cumulative CEXP using live repository thresholds."""
    if not 0 <= cexp <= CLASS_CEXP_CAP:
        raise ValueError(f"CEXP must be between 0 and {CLASS_CEXP_CAP}")
    level = 1
    for row in _thresholds(root=root):
        if cexp < row.cumulative_cexp:
            break
        level = row.class_level
    return level


def cexp_to_next_class_level(cexp: int, *, root: Path | None = None) -> int:
    """Return CEXP still needed for the next CL; zero when already at CL13."""
    level = class_level_from_cexp(cexp, root=root)
    if level >= CLASS_LEVEL_CAP:
        return 0
    thresholds = {row.class_level: row.cumulative_cexp for row in _thresholds(root=root)}
    return thresholds[level + 1] - cexp


def mandatory_base_cexp_at_end_chapter(
    character: str,
    chapter: int,
    *,
    root: Path | None = None,
) -> int:
    """Return recruitment-aware mandatory Base CEXP through end Ch0–Ch7.

    The result uses the published starting package, the canonical recruitment-
    chapter handoff remainder, and only later full chapter budgets. It stops at
    Volition because post-Volition awards can be directed to Base or Subclass and
    the repository does not define one mandatory selection policy.
    """
    if not 0 <= chapter <= 7:
        raise ValueError("mandatory pre-Volition Base CEXP helper supports Chapters 0–7 only")
    starts = {row.character: row for row in load_character_starting_cexp(root=root)}
    source = starts.get(character)
    if source is None:
        raise KeyError(f"Unknown permanent character in CEXP authority: {character}")
    if chapter < source.recruitment_chapter:
        raise ValueError(
            f"{character} is not recruited by end Chapter {chapter}; recruitment is Chapter "
            f"{source.recruitment_chapter}."
        )

    total = source.starting_base_cexp
    budgets = {row.chapter: row.cexp for row in load_campaign_cexp_budgets(root=root)}
    if source.recruitment_chapter == 0:
        total += sum(budgets[ch] for ch in range(1, chapter + 1))
    else:
        total += source.recruitment_chapter_cexp_after_join
        total += sum(
            budgets[ch]
            for ch in range(source.recruitment_chapter + 1, chapter + 1)
        )
    if total > CLASS_CEXP_CAP:
        raise ValueError(
            f"Pre-Volition mandatory CEXP arithmetic overcaps {character}: {total}"
        )
    return total


def class_state_at_volition(
    character: str,
    *,
    root: Path | None = None,
) -> ClassCexpState:
    """Return exact recruitment-aware Base/Subclass CEXP at end Ch7 Volition."""
    return ClassCexpState(
        base_cexp=mandatory_base_cexp_at_end_chapter(character, 7, root=root),
        subclass_cexp=0,
    )


def post_volition_cexp_available_at_checkpoint(
    checkpoint_key: str,
    *,
    root: Path | None = None,
) -> int:
    """Return mandatory CEXP available after Volition by an exact campaign checkpoint.

    This reports the award stream only. It deliberately does not decide whether
    those awards went to Base or Subclass.
    """
    checkpoint = load_campaign_checkpoint(checkpoint_key, root=root)
    if checkpoint.chapter < 7:
        raise ValueError("checkpoint occurs before Sixfold Volition")
    if checkpoint.chapter == 7:
        return 0

    budgets = {row.chapter: row.cexp for row in load_campaign_cexp_budgets(root=root)}
    total = sum(budgets[ch] for ch in range(8, min(checkpoint.chapter, 12) + 1))
    if checkpoint.chapter < 13:
        return total

    if checkpoint.key in {"ch13_start"}:
        return total
    split = load_chapter13_cexp_split(root=root)
    if checkpoint.key == "ch13_last_shelter":
        return total + split.pre_last_shelter
    # End-Ch13 aliases and the named ending both have the entire chapter stream.
    if checkpoint.kind == "chapter_end":
        return total + budgets[13]
    raise ValueError(
        f"No exact Chapter-13 CEXP timing is published for checkpoint {checkpoint.key!r}"
    )


def apply_class_cexp(
    state: ClassCexpState,
    cexp: int,
    selected_track: ClassTrack,
) -> CexpAwardResult:
    """Apply one CEXP package to exactly one selected class track.

    CEXP never splits and never spills to the other class. Any amount above the
    selected track's CL13 cap is lost, matching current repository authority.
    """
    if cexp < 0:
        raise ValueError("CEXP award cannot be negative")
    if selected_track not in ("base", "subclass"):
        raise ValueError(f"Unsupported selected class track: {selected_track}")

    current = state.base_cexp if selected_track == "base" else state.subclass_cexp
    capacity = CLASS_CEXP_CAP - current
    applied = min(cexp, capacity)
    lost = cexp - applied
    if selected_track == "base":
        after = ClassCexpState(
            base_cexp=current + applied,
            subclass_cexp=state.subclass_cexp,
        )
    else:
        after = ClassCexpState(
            base_cexp=state.base_cexp,
            subclass_cexp=current + applied,
        )
    return CexpAwardResult(
        track=selected_track,
        requested_cexp=cexp,
        applied_cexp=applied,
        lost_cexp=lost,
        before=state,
        after=after,
    )


def project_class_cexp(
    start: ClassCexpState,
    segments: tuple[CexpAllocationSegment, ...] | list[CexpAllocationSegment],
) -> CexpAllocationProjection:
    """Project explicit selected-class allocation without inventing a switch policy."""
    state = start
    checkpoints: list[CexpAllocationCheckpoint] = []
    for segment in segments:
        result = apply_class_cexp(state, segment.cexp, segment.selected_track)
        state = result.after
        checkpoints.append(
            CexpAllocationCheckpoint(
                label=segment.label,
                selected_track=segment.selected_track,
                requested_cexp=result.requested_cexp,
                applied_cexp=result.applied_cexp,
                lost_cexp=result.lost_cexp,
                state=state,
            )
        )
    return CexpAllocationProjection(start=start, checkpoints=tuple(checkpoints))


__all__ = [
    "CLASS_CEXP_CAP",
    "CLASS_LEVEL_CAP",
    "CexpAllocationCheckpoint",
    "CexpAllocationProjection",
    "CexpAllocationSegment",
    "CexpAwardResult",
    "ClassCexpState",
    "ClassTrack",
    "apply_class_cexp",
    "cexp_to_next_class_level",
    "class_level_from_cexp",
    "class_state_at_volition",
    "mandatory_base_cexp_at_end_chapter",
    "post_volition_cexp_available_at_checkpoint",
    "project_class_cexp",
]
