"""Direct Physical, Magical, and Hybrid damage formulas."""
from __future__ import annotations
import math

from ..common import round_half_up
from .criticals import CRIT_MULTIPLIER
from .models import DamageKind

PENETRATION_CAP = 0.75


def _capped_penetration(value: float) -> float:
    return max(0.0, min(PENETRATION_CAP, value))


def physical_damage(attack: float, defense: float, power: float, *, defense_penetration: float = 0.0) -> float:
    effective_defense = max(0.0, defense) * (1.0 - _capped_penetration(defense_penetration))
    denominator = attack + effective_defense
    if attack <= 0 or denominator <= 0:
        return 0.0
    return (attack * attack / denominator) * (power / 100.0)


def magical_damage(magic: float, spirit: float, power: float, *, spirit_penetration: float = 0.0) -> float:
    effective_spirit = max(0.0, spirit) * (1.0 - _capped_penetration(spirit_penetration))
    denominator = magic + effective_spirit
    if magic <= 0 or denominator <= 0:
        return 0.0
    return (magic * magic / denominator) * (power / 100.0)


def direct_damage(kind: DamageKind, *, attack: float, magic: float, defense: float, spirit: float, power: float, defense_penetration: float = 0.0, spirit_penetration: float = 0.0, physical_weight: float = 0.5, magical_weight: float = 0.5, crit: bool = False, direct_damage_reduction: float = 0.0) -> int:
    if power < 0:
        raise ValueError("power cannot be negative")
    if kind == "physical":
        pre = physical_damage(attack, defense, power, defense_penetration=defense_penetration)
    elif kind == "magical":
        pre = magical_damage(magic, spirit, power, spirit_penetration=spirit_penetration)
    elif kind == "hybrid":
        if physical_weight < 0 or magical_weight < 0:
            raise ValueError("hybrid weights cannot be negative")
        if not math.isclose(physical_weight + magical_weight, 1.0, abs_tol=1e-9):
            raise ValueError("hybrid weights must sum to 1.0")
        pre = physical_weight * physical_damage(attack, defense, power, defense_penetration=defense_penetration) + magical_weight * magical_damage(magic, spirit, power, spirit_penetration=spirit_penetration)
    else:
        raise ValueError(f"unknown damage kind: {kind}")
    if crit:
        pre *= CRIT_MULTIPLIER
    reduction = max(0.0, min(1.0, direct_damage_reduction))
    return max(0, round_half_up(pre * (1.0 - reduction)))
