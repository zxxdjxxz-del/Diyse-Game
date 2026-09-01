"""Direct healing formulas."""
from __future__ import annotations

from ..common import round_half_up


def healing_amount(
    target_max_hp: int,
    caster_magic: int,
    *,
    max_hp_percent: float = 0.0,
    magic_scaling: float = 0.0,
    potency_multiplier: float = 1.0,
) -> int:
    if target_max_hp < 1 or caster_magic < 0:
        raise ValueError("invalid healing stats")
    if min(max_hp_percent, magic_scaling, potency_multiplier) < 0:
        raise ValueError("healing parameters cannot be negative")
    return max(
        0,
        round_half_up(
            (target_max_hp * max_hp_percent + caster_magic * magic_scaling)
            * potency_multiplier
        ),
    )
