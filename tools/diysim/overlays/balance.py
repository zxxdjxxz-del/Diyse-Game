"""Non-destructive working balance overlays for current sensitivity passes.

These helpers do not rewrite owner data. They transform in-memory simulator
objects so working hypotheses such as enemy Power ×1.20 and boss +5 effective
core-stat levels can be tested against the same authored encounter package.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
from typing import Iterable

from ..combat.models import CombatAction, Combatant
from ..common import round_half_up
from ..progression.stats import Stats, neutral_natural_stats

_EFFECTIVE_LEVEL_STAT_KEYS = ("attack", "magic", "defense", "spirit", "speed")


@dataclass(frozen=True)
class BalanceOverlay:
    """Working sensitivity settings applied only in simulator memory."""

    direct_damage_power_multiplier: float = 1.0
    effective_stat_level_offset: int = 0

    def __post_init__(self) -> None:
        if self.direct_damage_power_multiplier <= 0:
            raise ValueError("direct_damage_power_multiplier must be positive")
        if not isinstance(self.effective_stat_level_offset, int):
            raise TypeError("effective_stat_level_offset must be an integer")


def scale_direct_damage_power(action: CombatAction, multiplier: float) -> CombatAction:
    """Return an action with only authored direct-damage Power scaled."""
    if multiplier <= 0:
        raise ValueError("multiplier must be positive")
    if action.action_kind != "damage" or action.power is None:
        return action
    return replace(action, power=action.power * multiplier)


def scale_direct_damage_actions(
    actions: Iterable[CombatAction],
    multiplier: float,
) -> tuple[CombatAction, ...]:
    return tuple(scale_direct_damage_power(action, multiplier) for action in actions)


def scale_effective_core_stat_level(
    stats: Stats,
    *,
    displayed_level: int,
    level_offset: int,
    root: Path | None = None,
) -> Stats:
    """Scale ATK/MAG/DEF/Spirit/SPD by neutral natural-curve level ratios.

    HP and MP are intentionally preserved. The helper uses the repository-owned
    natural stat curve at displayed_level and displayed_level + level_offset,
    matching the v106 working sensitivity definition.
    """
    if not isinstance(level_offset, int):
        raise TypeError("level_offset must be an integer")
    if level_offset == 0:
        return stats

    source_curve = neutral_natural_stats(displayed_level, root=root)
    target_curve = neutral_natural_stats(displayed_level + level_offset, root=root)

    replacements: dict[str, int] = {}
    for key in _EFFECTIVE_LEVEL_STAT_KEYS:
        source_value = source_curve[key]
        target_value = target_curve[key]
        replacements[key] = max(0, round_half_up(getattr(stats, key) * target_value / source_value))
    return replace(stats, **replacements)


def apply_enemy_balance_overlay(
    combatant: Combatant,
    *,
    overlay: BalanceOverlay,
    displayed_level: int | None = None,
    root: Path | None = None,
) -> Combatant:
    """Apply a working overlay to one enemy without mutating source objects."""
    if combatant.side != "enemy":
        raise ValueError("enemy balance overlays can only be applied to enemy combatants")
    if overlay.effective_stat_level_offset and displayed_level is None:
        raise ValueError("displayed_level is required for an effective stat-level overlay")

    stats = combatant.stats
    if overlay.effective_stat_level_offset:
        assert displayed_level is not None
        stats = scale_effective_core_stat_level(
            stats,
            displayed_level=displayed_level,
            level_offset=overlay.effective_stat_level_offset,
            root=root,
        )

    actions = scale_direct_damage_actions(
        combatant.actions,
        overlay.direct_damage_power_multiplier,
    )
    return replace(combatant, stats=stats, actions=actions)


__all__ = [
    "BalanceOverlay",
    "apply_enemy_balance_overlay",
    "scale_direct_damage_actions",
    "scale_direct_damage_power",
    "scale_effective_core_stat_level",
]
