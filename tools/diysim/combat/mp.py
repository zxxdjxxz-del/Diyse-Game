"""MP-cost legality and modifier resolution."""
from __future__ import annotations
from typing import Sequence

from ..core import round_half_up


def resolve_mp_cost(base_cost: int, *, flat_delta: int = 0, remaining_cost_factors: Sequence[float] = ()) -> int:
    if base_cost < 0 or any(factor < 0 for factor in remaining_cost_factors):
        raise ValueError("MP costs and remaining-cost factors cannot be negative")
    if base_cost == 0:
        return 0
    value = max(1, base_cost + flat_delta)
    for factor in remaining_cost_factors:
        value *= factor
    return max(1, round_half_up(value))
