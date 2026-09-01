"""Universal harmful-status rules and rank conversions."""
from __future__ import annotations

from .models import ActiveStatus, CombatUnit, StatusName

BURN_RATE = {"ordinary": 0.06, "regional_hunt": 0.045, "major_boss": 0.03}
BLEED_INITIAL_RATE = {"ordinary": 0.03, "regional_hunt": 0.0225, "major_boss": 0.015}
BLEED_ESCALATED_RATE = {"ordinary": 0.04, "regional_hunt": 0.03, "major_boss": 0.02}
STUN_LOSS_CHANCE = {"ordinary": 0.40, "regional_hunt": 0.25, "major_boss": 0.20}
STAGGERED_ROUNDS = {"ordinary": 5, "regional_hunt": 4, "major_boss": 3}
FREEZE_MAX_AFFECTED_ROUNDS = {"ordinary": 4, "regional_hunt": 2, "major_boss": 1}


def status_application_chance(
    base_chance: float,
    *,
    affinity_modifier: int = 0,
    specialist_bonus: int = 0,
    reliability_bonus: int = 0,
    status_resistance: int = 0,
    immune: bool = False,
) -> float:
    if immune:
        return 0.0
    chance = (
        base_chance
        + affinity_modifier
        + specialist_bonus
        + reliability_bonus
        - status_resistance
    )
    return max(5.0, min(95.0, chance))


def apply_status(target: CombatUnit, status: StatusName) -> bool:
    if status in target.template.status_immunities:
        return False
    if status in target.statuses:
        if status == "burn":
            target.statuses[status].remaining_rounds = 4
        elif status == "staggered":
            target.statuses[status].remaining_rounds = STAGGERED_ROUNDS[target.template.rank]
        elif status == "bleed":
            pass
        else:
            return False
        return True

    if status == "burn":
        duration = 4
    elif status == "staggered":
        duration = STAGGERED_ROUNDS[target.template.rank]
    else:
        duration = None

    target.statuses[status] = ActiveStatus(status, remaining_rounds=duration)
    return True
