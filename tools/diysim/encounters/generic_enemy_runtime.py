"""Shared execution primitives for repo-parsed generic enemies."""
from __future__ import annotations

from dataclasses import dataclass, field
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
    minimum_rounds: dict[str, int] = field(default_factory=dict)
    maximum_uses: dict[str, int] = field(default_factory=dict)
    use_counts: dict[str, int] = field(default_factory=dict)
    forced_follow_ups: dict[str, str] = field(default_factory=dict)
    forced_by_actions: dict[str, str] = field(default_factory=dict)
    preparation_requirements: dict[str, str] = field(default_factory=dict)
    pending_forced_action: str | None = None

    def _action_by_name(self, name: str) -> CombatAction:
        try:
            return next(action for action in self.combatant.actions if action.name == name)
        except StopIteration as exc:
            raise RuntimeError(f"{self.combatant.name} runtime references unknown action {name!r}") from exc

    def _base_legal(self, action: CombatAction, round_number: int) -> bool:
        if round_number <= self.locked_through.get(action.name, 0):
            return False
        if round_number < self.minimum_rounds.get(action.name, 1):
            return False
        maximum = self.maximum_uses.get(action.name)
        if maximum is not None and self.use_counts.get(action.name, 0) >= maximum:
            return False
        # A prepared follow-up is not legal in the ordinary pool. It enters
        # through pending_forced_action after its preparation resolves.
        if action.name in self.preparation_requirements:
            return False
        # Reload-style actions are likewise only legal when forced by their
        # owning preceding action.
        if action.name in self.forced_by_actions.values():
            return False
        return True

    def legal_actions(self, round_number: int) -> tuple[CombatAction, ...]:
        if self.pending_forced_action is not None:
            forced = self._action_by_name(self.pending_forced_action)
            # Authored prepared follow-ups override the ordinary candidate
            # pool. Repetition locks do not erase a required follow-up; owner
            # text would need to explicitly make the pending action illegal.
            if round_number < self.minimum_rounds.get(forced.name, 1):
                raise RuntimeError(
                    f"{self.combatant.name} forced action {forced.name!r} is not yet round-legal"
                )
            maximum = self.maximum_uses.get(forced.name)
            if maximum is not None and self.use_counts.get(forced.name, 0) >= maximum:
                raise RuntimeError(
                    f"{self.combatant.name} forced action {forced.name!r} exceeded its use cap"
                )
            return (forced,)
        return tuple(
            action for action in self.combatant.actions
            if self._base_legal(action, round_number)
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
        if self.pending_forced_action == action.name:
            self.pending_forced_action = None

        self.use_counts[action.name] = self.use_counts.get(action.name, 0) + 1
        duration = self.repetition_locks.get(action.name)
        if duration:
            self.locked_through[action.name] = round_number + duration - 1

        forced = self.forced_follow_ups.get(action.name)
        if forced is None:
            forced = self.forced_by_actions.get(action.name)
        if forced is not None:
            if self.pending_forced_action is not None:
                raise RuntimeError(
                    f"{self.combatant.name} cannot queue {forced!r}; "
                    f"{self.pending_forced_action!r} is already pending"
                )
            self.pending_forced_action = forced


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
    minimum_rounds = {
        action_def.action.name: action_def.minimum_round
        for action_def in definition.actions
        if action_def.action is not None and action_def.minimum_round > 1
    }
    maximum_uses = {
        action_def.action.name: action_def.maximum_uses
        for action_def in definition.actions
        if action_def.action is not None and action_def.maximum_uses is not None
    }
    forced_follow_ups = {
        action_def.action.name: action_def.forced_follow_up
        for action_def in definition.actions
        if action_def.action is not None and action_def.forced_follow_up is not None
    }
    # RuntimeActionDefinition stores this relation on the forced action itself;
    # invert it so committing the preceding action queues the forced action.
    forced_by_actions = {
        action_def.forced_by_action: action_def.action.name
        for action_def in definition.actions
        if action_def.action is not None and action_def.forced_by_action is not None
    }
    preparation_requirements = {
        action_def.action.name: action_def.requires_preparation
        for action_def in definition.actions
        if action_def.action is not None and action_def.requires_preparation is not None
    }
    return GenericEnemyRuntime(
        definition=definition,
        combatant=combatant,
        repetition_locks=locks,
        locked_through={},
        minimum_rounds=minimum_rounds,
        maximum_uses=maximum_uses,
        use_counts={},
        forced_follow_ups=forced_follow_ups,
        forced_by_actions=forced_by_actions,
        preparation_requirements=preparation_requirements,
    )


__all__ = ["GenericEnemyRuntime", "build_generic_enemy_runtime"]
