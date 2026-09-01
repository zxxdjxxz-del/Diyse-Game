"""Player-EXP route projection and target-checkpoint planning."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from ..common import round_half_up
from .player_exp import cumulative_exp, exp_to_next_level, level_from_exp
from .stats import LEVEL_CAP


@dataclass(frozen=True)
class ProgressionSegment:
    """One route segment used for expected Player-EXP planning.

    `completion_rate` is a planning fraction, not a battle mechanic. It lets a
    route model things like "the player fights ~70% of available encounters"
    without changing the authored reward on any individual encounter.
    """

    name: str
    count: int = 1
    exp_each: int = 0
    flat_exp: int = 0
    completion_rate: float = 1.0

    def __post_init__(self) -> None:
        if self.count < 0:
            raise ValueError("count cannot be negative")
        if self.exp_each < 0 or self.flat_exp < 0:
            raise ValueError("EXP awards cannot be negative")
        if not 0.0 <= self.completion_rate <= 1.0:
            raise ValueError("completion_rate must be between 0 and 1")

    @property
    def expected_exp(self) -> int:
        repeated = self.count * self.exp_each * self.completion_rate
        return self.flat_exp + round_half_up(repeated)


@dataclass(frozen=True)
class ProgressionCheckpoint:
    segment: str
    gained_exp: int
    cumulative_exp: int
    level: int
    exp_to_next: int

    def as_dict(self) -> dict[str, int | str]:
        return {
            "segment": self.segment,
            "gained_exp": self.gained_exp,
            "cumulative_exp": self.cumulative_exp,
            "level": self.level,
            "exp_to_next": self.exp_to_next,
        }


@dataclass(frozen=True)
class ProgressionProjection:
    start_exp: int
    start_level: int
    total_gained_exp: int
    final_exp: int
    final_level: int
    levels_gained: int
    exp_to_next: int
    checkpoints: tuple[ProgressionCheckpoint, ...]

    def as_dict(self) -> dict[str, object]:
        return {
            "start_exp": self.start_exp,
            "start_level": self.start_level,
            "total_gained_exp": self.total_gained_exp,
            "final_exp": self.final_exp,
            "final_level": self.final_level,
            "levels_gained": self.levels_gained,
            "exp_to_next": self.exp_to_next,
            "checkpoints": [checkpoint.as_dict() for checkpoint in self.checkpoints],
        }


def exp_at_level_progress(level: int, progress: float = 0.0) -> int:
    if not 1 <= level <= LEVEL_CAP:
        raise ValueError(f"level must be between 1 and {LEVEL_CAP}")
    if not 0.0 <= progress < 1.0:
        raise ValueError("progress must be >= 0 and < 1")
    base = cumulative_exp(level)
    if level == LEVEL_CAP:
        if progress != 0.0:
            raise ValueError("Lv70 has no progress toward Lv71")
        return base
    span = cumulative_exp(level + 1) - base
    return base + round_half_up(span * progress)


def project_progression(start_exp: int, segments: Sequence[ProgressionSegment]) -> ProgressionProjection:
    if start_exp < 0:
        raise ValueError("start_exp cannot be negative")
    capped_start = min(start_exp, cumulative_exp(LEVEL_CAP))
    start_level = level_from_exp(capped_start)
    current_exp = capped_start
    checkpoints: list[ProgressionCheckpoint] = []

    for segment in segments:
        gained = segment.expected_exp
        current_exp = min(cumulative_exp(LEVEL_CAP), current_exp + gained)
        checkpoints.append(
            ProgressionCheckpoint(
                segment=segment.name,
                gained_exp=gained,
                cumulative_exp=current_exp,
                level=level_from_exp(current_exp),
                exp_to_next=exp_to_next_level(current_exp),
            )
        )

    final_level = level_from_exp(current_exp)
    return ProgressionProjection(
        start_exp=capped_start,
        start_level=start_level,
        total_gained_exp=current_exp - capped_start,
        final_exp=current_exp,
        final_level=final_level,
        levels_gained=final_level - start_level,
        exp_to_next=exp_to_next_level(current_exp),
        checkpoints=tuple(checkpoints),
    )


def required_average_exp_per_encounter(
    *,
    start_exp: int,
    target_level: int,
    encounter_count: int,
    fixed_exp: int = 0,
    target_level_progress: float = 0.0,
) -> float:
    if start_exp < 0 or fixed_exp < 0:
        raise ValueError("EXP values cannot be negative")
    if encounter_count <= 0:
        raise ValueError("encounter_count must be positive")
    target_exp = exp_at_level_progress(target_level, target_level_progress)
    remaining = target_exp - start_exp - fixed_exp
    return max(0.0, remaining / encounter_count)
