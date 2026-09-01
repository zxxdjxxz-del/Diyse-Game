"""Speed-derived turn ordering for the advanced combat runtime."""
from __future__ import annotations
from typing import Sequence

from .derived_stats import effective_speed
from .models import CombatUnit


def turn_order(units: Sequence[CombatUnit]) -> list[CombatUnit]:
    """Return currently living units in current Speed order.

    Exact party-vs-enemy Speed ties resolve party-first. Stable scenario order
    breaks remaining ties within a side.
    """
    return sorted(
        (unit for unit in units if unit.alive),
        key=lambda unit: (
            -effective_speed(unit),
            0 if unit.side == "party" else 1,
            unit.stable_index,
        ),
    )
