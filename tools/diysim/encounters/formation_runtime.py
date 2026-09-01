"""Shared runtime for repo-owned ordinary enemy formations."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import random

from tools.diysim.combat.action_resolution import resolve_effect
from tools.diysim.combat.models import CombatAction, CombatUnit
from tools.diysim.overlays import BalanceOverlay

from .formation_catalog import EncounterFormationDefinition
from .generic_enemy_runtime import GenericEnemyRuntime, build_generic_enemy_runtime
from .runtime_catalog import RuntimeActionDefinition


@dataclass
class FormationEnemyInstance:
    runtime: GenericEnemyRuntime
    unit: CombatUnit


@dataclass(frozen=True)
class FormationActionSelection:
    actor_index: int
    action: CombatAction
    ally_targets: tuple[int, ...] = ()
    source_action_name: str | None = None


@dataclass
class FormationRuntime:
    definition: EncounterFormationDefinition
    enemies: list[FormationEnemyInstance]

    def action_definition(self, actor_index: int, action_name: str) -> RuntimeActionDefinition:
        runtime = self.enemies[actor_index].runtime
        return next(
            item for item in runtime.definition.actions
            if item.action is not None and item.action.name == action_name
        )

    def eligible_allies(self, actor_index: int, action_def: RuntimeActionDefinition) -> tuple[int, ...]:
        actor = self.enemies[actor_index].unit
        result: list[int] = []
        required_tags = set(action_def.target_tags)
        for index, instance in enumerate(self.enemies):
            if not instance.unit.alive:
                continue
            if action_def.exclude_actor and index == actor_index:
                continue
            if instance.unit.side != actor.side:
                continue
            if required_tags and not required_tags.issubset(instance.unit.template.runtime_tags):
                continue
            result.append(index)
        return tuple(result)

    def _fallback(self, actor_index: int, action_def: RuntimeActionDefinition) -> CombatAction | None:
        if action_def.fallback_action is None:
            return None
        return self.enemies[actor_index].runtime._action_by_name(action_def.fallback_action)

    def select_action(self, actor_index: int, round_number: int, rng: random.Random) -> FormationActionSelection:
        runtime = self.enemies[actor_index].runtime
        legal = runtime.legal_actions(round_number)
        if not legal:
            raise RuntimeError(f"{runtime.combatant.name} has no legal action in round {round_number}")

        weights = tuple(action.weight for action in legal)
        if all(weight is None for weight in weights):
            chosen = rng.choice(legal)
        elif any(weight is None for weight in weights):
            raise RuntimeError(f"{runtime.combatant.name} mixes weighted and unweighted legal actions")
        else:
            chosen = rng.choices(legal, weights=weights, k=1)[0]

        action_def = self.action_definition(actor_index, chosen.name)
        if not action_def.formation_required:
            return FormationActionSelection(actor_index, chosen, (), chosen.name)

        eligible = self.eligible_allies(actor_index, action_def)
        if not eligible:
            fallback = self._fallback(actor_index, action_def)
            if fallback is None:
                remaining = tuple(action for action in legal if action.name != chosen.name)
                if not remaining:
                    raise RuntimeError(
                        f"{runtime.combatant.name} selected {chosen.name!r} with no legal formation target"
                    )
                if all(action.weight is None for action in remaining):
                    replacement = rng.choice(remaining)
                elif any(action.weight is None for action in remaining):
                    raise RuntimeError(f"{runtime.combatant.name} mixes weighted and unweighted legal actions")
                else:
                    replacement = rng.choices(remaining, weights=[action.weight for action in remaining], k=1)[0]
                return FormationActionSelection(actor_index, replacement, (), chosen.name)
            return FormationActionSelection(actor_index, fallback, (), chosen.name)

        targets = eligible if chosen.target_scope == "all" else (rng.choice(eligible),)
        return FormationActionSelection(actor_index, chosen, targets, chosen.name)

    def commit_action(self, selection: FormationActionSelection, round_number: int) -> None:
        # Cooldowns/use caps belong to the action that actually executes. If a
        # formation-only action falls back, its authored fallback is what the
        # enemy spent its turn using.
        self.enemies[selection.actor_index].runtime.commit_action(selection.action, round_number)

    def resolve_ally_effect(self, selection: FormationActionSelection) -> tuple[int, ...]:
        if selection.action.action_kind != "effect" or not selection.ally_targets:
            return ()
        actor = self.enemies[selection.actor_index].unit
        restored: list[int] = []
        for target_index in selection.ally_targets:
            target = self.enemies[target_index].unit
            restored.append(resolve_effect(actor, selection.action, target))
        return tuple(restored)


def build_formation_runtime(
    definition: EncounterFormationDefinition,
    *,
    overlay: BalanceOverlay = BalanceOverlay(),
    root: Path | None = None,
) -> FormationRuntime:
    if not definition.runtime_ready:
        blockers = "; ".join(definition.blockers) or "contains non-shared runtime members"
        raise ValueError(f"formation {definition.name!r} is not runtime-ready: {blockers}")

    enemies: list[FormationEnemyInstance] = []
    stable_index = 0
    for member in definition.members:
        assert member.enemy is not None
        for _ in range(member.count):
            runtime = build_generic_enemy_runtime(member.enemy, overlay=overlay, root=root)
            enemies.append(FormationEnemyInstance(runtime, CombatUnit(runtime.combatant, stable_index)))
            stable_index += 1
    return FormationRuntime(definition, enemies)


__all__ = [
    "FormationActionSelection", "FormationEnemyInstance", "FormationRuntime",
    "build_formation_runtime",
]
