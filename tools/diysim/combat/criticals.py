"""Critical-hit rule access backed by repository authority."""
from __future__ import annotations
from pathlib import Path

from ..sources.combat import load_combat_rules


def base_crit_chance(*, root: Path | None = None) -> float:
    return load_combat_rules(root=root).base_crit_chance


def crit_chance_cap(*, root: Path | None = None) -> float:
    return load_combat_rules(root=root).crit_chance_cap


def crit_multiplier(*, root: Path | None = None) -> float:
    return load_combat_rules(root=root).crit_multiplier


__all__ = ["base_crit_chance", "crit_chance_cap", "crit_multiplier"]
