"""JSON loaders for synthetic/test battle scenarios.

Real Diyse encounters should use repo-backed encounter adapters, not copied JSON.
Omitted actions/weights remain omitted; runtime source/policy fallbacks decide them.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..combat.advanced_runtime import AdvancedBattleScenario
from ..combat.models import CombatAction, Combatant, StatusRider
from ..combat.simple_runtime import ActionProfile, BattleScenario, CombatantTemplate
from ..progression.stats import Stats


def _optional_float(data: dict[str, Any], key: str) -> float | None:
    return None if key not in data else float(data[key])


def _optional_int(data: dict[str, Any], key: str) -> int | None:
    return None if key not in data else int(data[key])


def _action(data: dict[str, Any]) -> ActionProfile:
    return ActionProfile(
        name=data["name"],
        kind=data.get("kind", "physical"),
        power=_optional_float(data, "power"),
        base_hit=_optional_int(data, "base_hit"),
        crit_chance=_optional_float(data, "crit_chance"),
        defense_penetration=float(data.get("defense_penetration", 0)),
        spirit_penetration=float(data.get("spirit_penetration", 0)),
        physical_weight=_optional_float(data, "physical_weight"),
        magical_weight=_optional_float(data, "magical_weight"),
        weight=_optional_float(data, "weight"),
    )


def _combatant(data: dict[str, Any], side: str) -> CombatantTemplate:
    stats = Stats(**{key: int(data["stats"][key]) for key in ("hp", "mp", "attack", "magic", "defense", "spirit", "speed")})
    actions = tuple(_action(action) for action in data.get("actions", []))
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
        power=_optional_float(data, "power"),
        base_hit=_optional_int(data, "base_hit"),
        crit_chance=_optional_float(data, "crit_chance"),
        defense_penetration=float(data.get("defense_penetration", 0)),
        spirit_penetration=float(data.get("spirit_penetration", 0)),
        physical_weight=_optional_float(data, "physical_weight"),
        magical_weight=_optional_float(data, "magical_weight"),
        heal_max_hp_percent=float(data.get("heal_max_hp_percent", 0)),
        heal_magic_scaling=float(data.get("heal_magic_scaling", 0)),
        healing_potency=float(data.get("healing_potency", 1)),
        clear_harmful_statuses=data.get("clear_harmful_statuses", 0),
        status_riders=tuple(_status_rider(rider) for rider in data.get("status_riders", [])),
        weight=_optional_float(data, "weight"),
    )


def _advanced_combatant(data: dict[str, Any], side: str) -> Combatant:
    stats = Stats(**{key: int(data["stats"][key]) for key in ("hp", "mp", "attack", "magic", "defense", "spirit", "speed")})
    return Combatant(
        name=data["name"],
        side=side,
        stats=stats,
        actions=tuple(_advanced_action(action) for action in data.get("actions", [])),
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
