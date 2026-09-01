"""Universal harmful-status rules backed by repository authority."""
from __future__ import annotations

from ..sources.combat import load_combat_rules
from .models import ActiveStatus, CombatUnit, StatusName


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
    chance = base_chance + affinity_modifier + specialist_bonus + reliability_bonus - status_resistance
    rules = load_combat_rules()
    return max(rules.status_chance_min, min(rules.status_chance_max, chance))


def apply_status(target: CombatUnit, status: StatusName) -> bool:
    if status in target.template.status_immunities:
        return False
    rules = load_combat_rules()
    if status in target.statuses:
        if status == "burn":
            target.statuses[status].remaining_rounds = rules.burn_rounds
        elif status == "staggered":
            target.statuses[status].remaining_rounds = rules.staggered_rounds[target.template.rank]
        elif status == "bleed":
            pass
        else:
            return False
        return True

    if status == "burn":
        duration = rules.burn_rounds
    elif status == "staggered":
        duration = rules.staggered_rounds[target.template.rank]
    else:
        duration = None

    target.statuses[status] = ActiveStatus(status, remaining_rounds=duration)
    return True


__all__ = ["apply_status", "status_application_chance"]
