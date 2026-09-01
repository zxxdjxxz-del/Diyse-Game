from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .battle import AdvancedBattleScenario
from .core import ActionProfile, BattleScenario, CombatantTemplate, Stats, cumulative_exp
from .progression import ProgressionSegment
from .rules import CombatAction, Combatant, StatusRider


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


def _status_rider(data: dict[str, Any]) -> StatusRider:
    return StatusRider(
        status=data["status"],
        base_chance=float(data["base_chance"]),
        specialist_bonus=int(data.get("specialist_bonus", 0)),
        reliability_bonus=int(data.get("reliability_bonus", 0)),
    )


def _advanced_action(data: dict[str, Any]) -> CombatAction:
    return CombatAction(
        name=data["name"],
        action_kind=data.get("action_kind", "damage"),
        mp_cost=int(data.get("mp_cost", 0)),
        target_side=data.get("target_side", "enemy"),
        target_scope=data.get("target_scope", "one"),
        damage_kind=data.get("damage_kind", "physical"),
        element=data.get("element", "neutral"),
        power=float(data.get("power", 100)),
        base_hit=int(data.get("base_hit", 100)),
        crit_chance=float(data.get("crit_chance", 5)),
        defense_penetration=float(data.get("defense_penetration", 0)),
        spirit_penetration=float(data.get("spirit_penetration", 0)),
        physical_weight=float(data.get("physical_weight", 0.5)),
        magical_weight=float(data.get("magical_weight", 0.5)),
        heal_max_hp_percent=float(data.get("heal_max_hp_percent", 0)),
        heal_magic_scaling=float(data.get("heal_magic_scaling", 0)),
        healing_potency=float(data.get("healing_potency", 1)),
        clear_harmful_statuses=data.get("clear_harmful_statuses", 0),
        status_riders=tuple(_status_rider(rider) for rider in data.get("status_riders", [])),
        weight=float(data.get("weight", 1)),
    )


def _advanced_combatant(data: dict[str, Any], side: str) -> Combatant:
    stats = Stats(**{key: int(data["stats"][key]) for key in ("hp", "mp", "attack", "magic", "defense", "spirit", "speed")})
    return Combatant(
        name=data["name"],
        side=side,
        stats=stats,
        actions=tuple(_advanced_action(action) for action in data.get("actions", [{"name": "Attack"}])),
        evasion=int(data.get("evasion", 0)),
        direct_damage_reduction=float(data.get("direct_damage_reduction", 0)),
        rank=data.get("rank", "ordinary"),
        status_resistance=int(data.get("status_resistance", 0)),
        status_immunities=frozenset(data.get("status_immunities", [])),
        elemental_affinities=dict(data.get("elemental_affinities", {})),
    )


def load_advanced_scenario(path: str | Path) -> AdvancedBattleScenario:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return AdvancedBattleScenario(
        party=tuple(_advanced_combatant(unit, "party") for unit in data["party"]),
        enemies=tuple(_advanced_combatant(unit, "enemy") for unit in data["enemies"]),
        max_rounds=int(data.get("max_rounds", 100)),
    )


def load_progression_route(path: str | Path) -> tuple[int, tuple[ProgressionSegment, ...]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if "start_exp" in data:
        start_exp = int(data["start_exp"])
    else:
        start_level = int(data.get("start_level", 1))
        start_exp = cumulative_exp(start_level)
    segments = tuple(
        ProgressionSegment(
            name=segment["name"],
            count=int(segment.get("count", 1)),
            exp_each=int(segment.get("exp_each", 0)),
            flat_exp=int(segment.get("flat_exp", 0)),
            completion_rate=float(segment.get("completion_rate", 1.0)),
        )
        for segment in data.get("segments", [])
    )
    return start_exp, segments
