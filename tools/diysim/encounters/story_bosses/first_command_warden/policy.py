"""Conservative repo-backed party policy for First Command Warden sensitivity runs."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from tools.diysim.combat.basic_attack import basic_attack_action
from tools.diysim.combat.models import CombatAction, CombatUnit, StatusRider
from tools.diysim.sources import (
    SourceGapError,
    load_ability_source,
    parse_authored_action_text,
    read_repo_text,
)


@dataclass(frozen=True)
class WardenPolicyConfig:
    """Competent same-package policy used for v105/v106 isolation."""

    mend_below_hp_fraction: float = 0.50

    def __post_init__(self) -> None:
        if not 0.0 < self.mend_below_hp_fraction < 1.0:
            raise ValueError("mend_below_hp_fraction must be between 0 and 1")


@dataclass(frozen=True)
class WardenPartyActions:
    crest_strike: CombatAction
    wardens_valor: CombatAction
    cinder_shot: CombatAction
    weave_burst: CombatAction
    mend: CombatAction
    basic_attack: CombatAction

    def offensive_for(self, character: str) -> CombatAction:
        actions = {
            "Cyanis": self.crest_strike,
            "Ilyra": self.wardens_valor,
            "Torren": self.cinder_shot,
            "Nimera": self.weave_burst,
        }
        try:
            return actions[character]
        except KeyError as exc:
            raise ValueError(f"unsupported Warden policy character: {character}") from exc


def _direct_action(ability: str, class_name: str, *, root: Path | None = None) -> CombatAction:
    source = load_ability_source(ability, class_name=class_name, root=root)
    parsed = parse_authored_action_text(ability, source.owner_effect)
    if source.fixed_mp is None:
        raise SourceGapError(f"{class_name} / {ability} lacks fixed MP authority")
    if parsed.damage_kind is None or parsed.power is None:
        raise SourceGapError(f"{class_name} / {ability} lacks direct-damage identity")
    if parsed.element_mode != "fixed" or parsed.element is None:
        raise SourceGapError(f"{class_name} / {ability} lacks fixed element authority")
    return CombatAction(
        name=ability,
        mp_cost=source.fixed_mp,
        target_scope=parsed.target_scope or "one",
        damage_kind=parsed.damage_kind,  # type: ignore[arg-type]
        element=parsed.element,  # type: ignore[arg-type]
        power=parsed.power,
        base_hit=parsed.base_hit,
        physical_weight=parsed.physical_weight,
        magical_weight=parsed.magical_weight,
        status_riders=tuple(StatusRider(status, chance) for status, chance in parsed.status_chances),
    )


def _mend(*, root: Path | None = None) -> CombatAction:
    source = load_ability_source("Mend", class_name="Blue Warden", root=root)
    if source.fixed_mp is None:
        raise SourceGapError("Blue Warden / Mend lacks fixed MP authority")
    hp = re.search(r"(\d+)% target Max HP", source.owner_effect, re.I)
    magic = re.search(r"([0-9.]+)\s*[×x]\s*Ilyra", source.owner_effect, re.I)
    owner_text = read_repo_text(source.owner_path, root=root)
    gentle_hands = re.search(r"Gentle Hands[^\n]*Mend gains \+(\d+)% healing potency", owner_text, re.I)
    if not (hp and magic and gentle_hands):
        raise SourceGapError("Blue Warden / Mend lacks exact Chapter-3 healing/mastery authority")
    return CombatAction(
        name="Mend",
        action_kind="heal",
        mp_cost=source.fixed_mp,
        target_side="ally",
        target_scope="one",
        heal_max_hp_percent=int(hp.group(1)) / 100.0,
        heal_magic_scaling=float(magic.group(1)),
        healing_potency=1.0 + int(gentle_hands.group(1)) / 100.0,
    )


def load_warden_party_actions(*, root: Path | None = None) -> WardenPartyActions:
    return WardenPartyActions(
        crest_strike=_direct_action("Crest Strike", "Crest Knight", root=root),
        wardens_valor=_direct_action("Warden's Valor", "Blue Warden", root=root),
        cinder_shot=_direct_action("Cinder Shot", "War Archer", root=root),
        weave_burst=_direct_action("Weave Burst", "Cardweaver", root=root),
        mend=_mend(root=root),
        basic_attack=basic_attack_action(),
    )


def lowest_hp_ally(party: list[CombatUnit]) -> CombatUnit | None:
    conscious = [unit for unit in party if unit.alive]
    if not conscious:
        return None
    return min(conscious, key=lambda unit: (unit.hp / unit.max_hp, unit.stable_index))


def choose_player_action(
    actor: CombatUnit,
    party: list[CombatUnit],
    actions: WardenPartyActions,
    *,
    sealed_category: str | None,
    config: WardenPolicyConfig,
) -> tuple[str, CombatAction, CombatUnit | None]:
    """Choose category/action/heal target without reading future enemy actions."""
    if actor.template.name == "Ilyra":
        heal_target = lowest_hp_ally(party)
        if (
            heal_target is not None
            and heal_target.hp / heal_target.max_hp < config.mend_below_hp_fraction
            and actor.mp >= actions.mend.mp_cost
        ):
            return "Ability", actions.mend, heal_target

    offensive = actions.offensive_for(actor.template.name)
    can_ability = actor.mp >= offensive.mp_cost

    # Command Seal never disables a category. Smart play simply chooses the
    # other ordinary damage category when affordable/legal to avoid Reprisal.
    if sealed_category == "Ability":
        return "Attack", actions.basic_attack, None
    if sealed_category == "Attack" and can_ability:
        return "Ability", offensive, None
    if can_ability:
        return "Ability", offensive, None
    return "Attack", actions.basic_attack, None


__all__ = [
    "WardenPartyActions",
    "WardenPolicyConfig",
    "choose_player_action",
    "load_warden_party_actions",
    "lowest_hp_ally",
]
