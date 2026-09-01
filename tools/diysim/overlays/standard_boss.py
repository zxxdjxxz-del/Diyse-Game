"""Shared working boss-test profile for DiySim.

This is simulator policy, not Diyse owner canon. It keeps authored durability and
Speed intact while applying the currently selected boss-pressure hypothesis:
+5 effective offensive levels to ATK/MAG and x1.20 direct-damage Power.
"""
from __future__ import annotations

from .balance import BalanceOverlay

STANDARD_BOSS_POWER_MULTIPLIER = 1.20
STANDARD_BOSS_OFFENSIVE_LEVEL_OFFSET = 5


def standard_boss_test_overlay() -> BalanceOverlay:
    """Return the current cross-boss DiySim pressure profile."""
    return BalanceOverlay(
        direct_damage_power_multiplier=STANDARD_BOSS_POWER_MULTIPLIER,
        offensive_stat_level_offset=STANDARD_BOSS_OFFENSIVE_LEVEL_OFFSET,
    )


__all__ = [
    "STANDARD_BOSS_POWER_MULTIPLIER",
    "STANDARD_BOSS_OFFENSIVE_LEVEL_OFFSET",
    "standard_boss_test_overlay",
]
