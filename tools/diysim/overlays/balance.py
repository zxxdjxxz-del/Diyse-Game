"""Non-destructive working balance overlays for current sensitivity passes.

These helpers do not rewrite owner data. They transform in-memory simulator
objects so working hypotheses such as enemy Power ×1.20 and boss effective
stat-level changes can be tested against the same authored encounter package.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
from typing import Iterable

from ..combat.models import CombatAction, Combatant
from ..common import round_half_up
from ..progression.stats import Stats, neutral_natural_stats

_EFFECTIVE_LEVEL_STAT_KEYS = ("attack", "magic", "defense", "spirit", "speed")
_OFFENSIVE_LEVEL_STAT_KEYS = ("attack", "magic")
_DEFENSIVE_LEVEL_STAT_KEYS = ("defense", "spirit")
_SPEED_LEVEL_STAT_KEYS = ("speed",)


@dataclass(frozen=True)
class BalanceOverlay:
    """Working sensitivity settings applied only in simulator memory.

    ``effective_stat_level_offset`` is the legacy all-core control and scales
    ATK/MAG/DEF/Spirit/SPD together. The split controls allow offense,
    durability, and Speed to be studied independently. To keep the meaning of
    each run unambiguous, the legacy all-core offset cannot be combined with
    any split offset in the same overlay.
    """

    direct_damage_power_multiplier: float = 1.0
    effective_stat_level_offset: int = 0
    offensive_stat_level_offset: int = 0
    defensive_stat_level_offset: int = 0
    speed_stat_level_offset: int = 0

    def __post_init__(self) -> None:
        if self.direct_damage_power_multiplier <= 0:
            raise ValueError("direct_damage_power_multiplier must be positive")
        for field_name in (
            "effective_stat_level_offset",
            "offensive_stat_level_offset",
            "defensive_stat_level_offset",
            "speed_stat_level_offset",
        ):
            if not isinstance(getattr(self, field_name), int):
                raise TypeError(f"{field_name} must be an integer")
        if self.effective_stat_level_offset and (
            self.offensive_stat_level_offset
            or self.defensive_stat_level_offset
            or self.speed_stat_level_offset
        ):
            raise ValueError(
                "effective_stat_level_offset cannot be combined with split stat-level offsets"
            )


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


def scale_selected_core_stat_level(
    stats: Stats,
    *,
    displayed_level: int,
    level_offset: int,
    stat_keys: Iterable[str],
    root: Path | None = None,
) -> Stats:
    """Scale selected core stats by neutral natural-curve level ratios.

    HP and MP are always preserved. Each selected stat uses the repository-owned
    neutral natural curve ratio between ``displayed_level`` and
    ``displayed_level + level_offset``.
    """
    if not isinstance(level_offset, int):
        raise TypeError("level_offset must be an integer")
    keys = tuple(stat_keys)
    unknown = tuple(key for key in keys if key not in _EFFECTIVE_LEVEL_STAT_KEYS)
    if unknown:
        raise ValueError(f"unsupported core stat keys: {unknown}")
    if level_offset == 0 or not keys:
        return stats

    source_curve = neutral_natural_stats(displayed_level, root=root)
    target_curve = neutral_natural_stats(displayed_level + level_offset, root=root)

    replacements: dict[str, int] = {}
    for key in keys:
        source_value = source_curve[key]
        target_value = target_curve[key]
        replacements[key] = max(
            0,
            round_half_up(getattr(stats, key) * target_value / source_value),
        )
    return replace(stats, **replacements)


def scale_effective_core_stat_level(
    stats: Stats,
    *,
    displayed_level: int,
    level_offset: int,
    root: Path | None = None,
) -> Stats:
    """Scale ATK/MAG/DEF/Spirit/SPD by neutral natural-curve level ratios.

    HP and MP are intentionally preserved. This retains the original v106
    all-core sensitivity definition for historical comparisons.
    """
    return scale_selected_core_stat_level(
        stats,
        displayed_level=displayed_level,
        level_offset=level_offset,
        stat_keys=_EFFECTIVE_LEVEL_STAT_KEYS,
        root=root,
    )


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

    has_stat_overlay = bool(
        overlay.effective_stat_level_offset
        or overlay.offensive_stat_level_offset
        or overlay.defensive_stat_level_offset
        or overlay.speed_stat_level_offset
    )
    if has_stat_overlay and displayed_level is None:
        raise ValueError("displayed_level is required for a stat-level overlay")

    stats = combatant.stats
    if overlay.effective_stat_level_offset:
        assert displayed_level is not None
        stats = scale_effective_core_stat_level(
            stats,
            displayed_level=displayed_level,
            level_offset=overlay.effective_stat_level_offset,
            root=root,
        )
    else:
        assert displayed_level is not None or not has_stat_overlay
        if overlay.offensive_stat_level_offset:
            assert displayed_level is not None
            stats = scale_selected_core_stat_level(
                stats,
                displayed_level=displayed_level,
                level_offset=overlay.offensive_stat_level_offset,
                stat_keys=_OFFENSIVE_LEVEL_STAT_KEYS,
                root=root,
            )
        if overlay.defensive_stat_level_offset:
            assert displayed_level is not None
            stats = scale_selected_core_stat_level(
                stats,
                displayed_level=displayed_level,
                level_offset=overlay.defensive_stat_level_offset,
                stat_keys=_DEFENSIVE_LEVEL_STAT_KEYS,
                root=root,
            )
        if overlay.speed_stat_level_offset:
            assert displayed_level is not None
            stats = scale_selected_core_stat_level(
                stats,
                displayed_level=displayed_level,
                level_offset=overlay.speed_stat_level_offset,
                stat_keys=_SPEED_LEVEL_STAT_KEYS,
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
    "scale_selected_core_stat_level",
]
