"""Shared execution primitives for repo-parsed generic enemies."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import random

from tools.diysim.combat.models import CombatAction, Combatant
from tools.diysim.overlays import BalanceOverlay, apply_enemy_balance_overlay
from tools.diysim.sources.enemies import load_enemy_system_rules

from .runtime_catalog import EnemyRuntimeDefinition


@dataclass
class GenericEnemyRuntime:
    definition: EnemyRuntimeDefinition
    combatant: Combatant
    repetition_locks: dict[str, int]
    locked_through: dict[str, int]

    def legal_actions(self, round_number: int) -> tuple[CombatAction, ...]:
        return tuple(
            action for action in self.combatant.actions
            if round_number > self.locked_through.get(action.name, 0)
        )

    def select_action(self, round_number: int, rng: random.Random) -> CombatAction:
        legal = self.legal_actions(round_number)
        if not legal:
            raise RuntimeError(f"{self.combatant.name} has no legal generic action in round {round_number}")
        weights = tuple(action.weight for action in legal)
        if all(weight is None for weight in weights):
            return rng.choice(legal)
        if any(weight is None for weight in weights):
            raise RuntimeError(f"{self.combatant.name} mixes weighted and unweighted legal actions")
        return rng.choices(legal, weights=weights, k=1)[0]

    def commit_action(self, action: CombatAction, round_number: int) -> None:
        duration = self.repetition_locks.get(action.name)
        if duration:
            self.locked_through[action.name] = round_number + duration - 1


def build_generic_enemy_runtime(
    definition: EnemyRuntimeDefinition,
    *,
    overlay: BalanceOverlay = BalanceOverlay(),
    root: Path | None = None,
) -> GenericEnemyRuntime:
    if definition.kind != "generic" or definition.combatant is None or definition.displayed_level is None:
        raise ValueError(f"{definition.name} is not a generic executable runtime")
    load_enemy_system_rules(root=root)
    combatant = apply_enemy_balance_overlay(
        definition.combatant, overlay=overlay,
        displayed_level=definition.displayed_level, root=root,
    )
    locks = {
        action_def.action.name: action_def.repetition_lock_rounds
        for action_def in definition.actions
        if action_def.action is not None and action_def.repetition_lock_rounds
    }
    return GenericEnemyRuntime(definition, combatant, locks, {})


__all__ = ["GenericEnemyRuntime", "build_generic_enemy_runtime"]
