from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .core import ActionProfile, BattleScenario, CombatantTemplate, Stats


def _action(data: dict[str, Any]) -> ActionProfile:
    return ActionProfile(
        name=data["name"],
        kind=data.get("kind", "physical"),
        power=float(data.get("power", 100)),
        base_hit=int(data.get("base_hit", 100)),
        crit_chance=float(data.get("crit_chance", 5)),
        defense_penetration=float(data.get("defense_penetration", 0)),
        spirit_penetration=float(data.get("spirit_penetration", 0)),
        physical_weight=float(data.get("physical_weight", 0.5)),
        magical_weight=float(data.get("magical_weight", 0.5)),
        weight=float(data.get("weight", 1)),
    )


def _combatant(data: dict[str, Any], side: str) -> CombatantTemplate:
    stats = Stats(**{key: int(data["stats"][key]) for key in ("hp", "mp", "attack", "magic", "defense", "spirit", "speed")})
    actions = tuple(_action(action) for action in data.get("actions", [{"name": "Attack"}]))
    return CombatantTemplate(
        name=data["name"],
        side=side,
        stats=stats,
        actions=actions,
        evasion=int(data.get("evasion", 0)),
        direct_damage_reduction=float(data.get("direct_damage_reduction", 0)),
        target_policy=data.get("target_policy", "random"),
    )


def load_scenario(path: str | Path) -> BattleScenario:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return BattleScenario(
        party=tuple(_combatant(unit, "party") for unit in data["party"]),
        enemies=tuple(_combatant(unit, "enemy") for unit in data["enemies"]),
        max_rounds=int(data.get("max_rounds", 100)),
    )
