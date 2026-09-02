"""Shared execution primitives for repo-parsed generic enemies."""
from __future__ import annotations

from dataclasses import dataclass, field, replace
from pathlib import Path
import random

from tools.diysim.combat.models import CombatAction, Combatant, StatusRider
from tools.diysim.overlays import BalanceOverlay, apply_enemy_balance_overlay
from tools.diysim.sources.enemies import load_enemy_system_rules

from .runtime_catalog import DynamicElementStateSpec, EnemyRuntimeDefinition


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
    dynamic_element_specs: dict[str, DynamicElementStateSpec] = field(default_factory=dict)
    dynamic_element_values: dict[str, str] = field(default_factory=dict)
    dynamic_action_sources: dict[str, str] = field(default_factory=dict)
    elemental_status_riders: dict[str, dict[str, StatusRider]] = field(default_factory=dict)

    def prepare_round(self, round_number: int, rng: random.Random) -> None:
        """Resolve battle-scoped/round-scoped authored element state.

        Random-once state is sampled exactly once per enemy instance. Round-cycle
        state is derived from the authored initial element and current round, so
        repeated selection calls within one round cannot advance it twice.
        """
        if round_number < 1:
            raise ValueError("round_number must be at least 1")
        for source, spec in self.dynamic_element_specs.items():
            if spec.mode == "random_once":
                if source not in self.dynamic_element_values:
                    if not spec.choices:
                        raise RuntimeError(f"{self.combatant.name} dynamic state {source!r} has no choices")
                    self.dynamic_element_values[source] = rng.choice(spec.choices)
            elif spec.mode == "round_cycle":
                if not spec.cycle:
                    raise RuntimeError(f"{self.combatant.name} dynamic state {source!r} has no cycle")
                self.dynamic_element_values[source] = spec.cycle[(round_number - 1) % len(spec.cycle)]
            else:
                raise RuntimeError(f"unsupported dynamic element mode {spec.mode!r}")

    def _resolve_action(self, action: CombatAction) -> CombatAction:
        source = self.dynamic_action_sources.get(action.name)
        if source is None:
            return action
        element = self.dynamic_element_values.get(source)
        if element is None:
            raise RuntimeError(
                f"{self.combatant.name} action {action.name!r} requires unresolved dynamic state {source!r}; "
                "prepare_round must run before action selection"
            )
        rider = self.elemental_status_riders.get(action.name, {}).get(element)
        return replace(
            action,
            element=element,
            status_riders=(rider,) if rider is not None else (),
        )

    def _action_by_name(self, name: str) -> CombatAction:
        try:
            action = next(action for action in self.combatant.actions if action.name == name)
        except StopIteration as exc:
            raise RuntimeError(f"{self.combatant.name} runtime references unknown action {name!r}") from exc
        return self._resolve_action(action)

    def _base_legal(self, action: CombatAction, round_number: int) -> bool:
        if round_number <= self.locked_through.get(action.name, 0):
            return False
        if round_number < self.minimum_rounds.get(action.name, 1):
            return False
        maximum = self.maximum_uses.get(action.name)
        if maximum is not None and self.use_counts.get(action.name, 0) >= maximum:
            return False
        if action.name in self.preparation_requirements:
            return False
        if action.name in self.forced_by_actions.values():
            return False
        return True

    def legal_actions(self, round_number: int) -> tuple[CombatAction, ...]:
        if self.pending_forced_action is not None:
            forced = self._action_by_name(self.pending_forced_action)
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
            self._resolve_action(action)
            for action in self.combatant.actions
            if self._base_legal(action, round_number)
        )

    def select_action(self, round_number: int, rng: random.Random) -> CombatAction:
        self.prepare_round(round_number, rng)
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
    if definition.kind not in {"generic", "formation"} or definition.combatant is None or definition.displayed_level is None:
        raise ValueError(f"{definition.name} is not executable by the shared enemy action runtime")
    load_enemy_system_rules(root=root)
    combatant = apply_enemy_balance_overlay(
        definition.combatant, overlay=overlay,
        displayed_level=definition.displayed_level, root=root,
    )
    locks = {
        item.action.name: item.repetition_lock_rounds
        for item in definition.actions
        if item.action is not None and item.repetition_lock_rounds
    }
    minimum_rounds = {
        item.action.name: item.minimum_round
        for item in definition.actions
        if item.action is not None and item.minimum_round > 1
    }
    maximum_uses = {
        item.action.name: item.maximum_uses
        for item in definition.actions
        if item.action is not None and item.maximum_uses is not None
    }
    forced_follow_ups = {
        item.action.name: item.forced_follow_up
        for item in definition.actions
        if item.action is not None and item.forced_follow_up is not None
    }
    forced_by_actions = {
        item.forced_by_action: item.action.name
        for item in definition.actions
        if item.action is not None and item.forced_by_action is not None
    }
    preparation_requirements = {
        item.action.name: item.requires_preparation
        for item in definition.actions
        if item.action is not None and item.requires_preparation is not None
    }
    dynamic_action_sources = {
        item.action.name: item.dynamic_element_source
        for item in definition.actions
        if item.action is not None and item.dynamic_element_source is not None
    }
    elemental_status_riders = {
        item.action.name: {
            element: StatusRider(status, chance)
            for element, status, chance in item.elemental_status_riders
        }
        for item in definition.actions
        if item.action is not None and item.elemental_status_riders
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
        dynamic_element_specs={spec.source: spec for spec in definition.dynamic_element_states},
        dynamic_element_values={},
        dynamic_action_sources=dynamic_action_sources,
        elemental_status_riders=elemental_status_riders,
    )


__all__ = ["GenericEnemyRuntime", "build_generic_enemy_runtime"]
