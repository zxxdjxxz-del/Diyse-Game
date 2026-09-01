"""Build the universal Basic Attack from current repository authority."""
from __future__ import annotations
from pathlib import Path
import re

from ..sources.combat import DAMAGE_PATH, load_combat_rules
from ..sources.repo import SourceGapError, read_repo_text
from .models import CombatAction


def basic_attack_action(*, root: Path | None = None) -> CombatAction:
    """Return a fresh Basic Attack action using the current combat owner files.

    Power, damage kind, element, and Base Hit come from repository authority.
    The returned object is runtime data, not a simulator-owned canon snapshot.
    """
    rules = load_combat_rules(root=root)
    damage_text = read_repo_text(DAMAGE_PATH, root=root)
    section = re.search(r"## Basic Attack\s*([\s\S]*?)(?=\n## |\Z)", damage_text)
    if not section:
        raise SourceGapError("Missing Basic Attack section in direct-damage authority")
    body = section.group(1)
    kind = re.search(r"- \*\*(Physical|Magical|Hybrid)\*\*", body, re.I)
    element = re.search(r"- \*\*(Neutral|Colorless|Fire|Ice|Lightning|Earth|Ruin)\*\*", body, re.I)
    if not (kind and element):
        raise SourceGapError("Incomplete Basic Attack damage-kind/element authority")

    return CombatAction(
        name="Attack",
        action_kind="damage",
        mp_cost=0,
        target_side="enemy",
        target_scope="one",
        damage_kind=kind.group(1).lower(),
        element=element.group(1).lower(),
        power=rules.basic_attack_power,
        base_hit=rules.default_player_base_hit,
        weight=None,
    )


__all__ = ["basic_attack_action"]
