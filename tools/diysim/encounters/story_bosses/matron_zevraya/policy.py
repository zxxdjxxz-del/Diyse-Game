"""Repo-backed CL9-era player action package for Matron Zevraya simulation."""
from __future__ import annotations

from dataclasses import dataclass, replace
from functools import lru_cache
from pathlib import Path
import re

from tools.diysim.combat.basic_attack import basic_attack_action
from tools.diysim.combat.models import CombatAction, CombatUnit, StatusRider
from tools.diysim.sources import SourceGapError, load_ability_source, load_trait_source, parse_authored_action_text, read_repo_text


@dataclass(frozen=True)
class ZevrayaPolicyConfig:
    mend_below_hp_fraction: float = 0.48
    renewal_two_allies_below_fraction: float = 0.62
    lifeline_below_hp_fraction: float = 0.34


@dataclass(frozen=True)
class ZevrayaPartyActions:
    crest_rend: CombatAction
    wardens_valor: CombatAction
    mend: CombatAction
    clear_warding: CombatAction
    renewal: CombatAction
    revive_mp_cost: int
    revive_fraction: float
    lifeline_mp_cost: int
    sizing_shot: CombatAction
    colossus_draw: CombatAction
    measured_colossus_penetration: float
    hunter_measure_full_rounds: int
    hunter_measure_party_crit_bonus: int
    hunter_measure_torren_crit_bonus: int
    prism_lance: CombatAction
    spectrum_cascade: CombatAction
    elemental_round_discount: int
    gentle_continuance_bonus: float
    basic_attack: CombatAction


def _direct_action(ability: str, class_name: str, *, chosen_element: str | None = None, root: Path | None = None) -> CombatAction:
    source = load_ability_source(ability, class_name=class_name, root=root)
    parsed = parse_authored_action_text(ability, source.owner_effect)
    if source.fixed_mp is None:
        raise SourceGapError(f"{class_name} / {ability} lacks fixed MP authority")
    if parsed.power is None:
        raise SourceGapError(f"{class_name} / {ability} lacks direct-damage Power")

    damage_kind = parsed.damage_kind
    if damage_kind is None:
        authored_kind = re.search(r"\b(Physical|Magical|Hybrid)\b", source.owner_effect, re.I)
        if authored_kind:
            damage_kind = authored_kind.group(1).lower()
        else:
            raise SourceGapError(f"{class_name} / {ability} lacks direct-damage axis")

    if parsed.element_mode == "fixed" and parsed.element is not None:
        element = parsed.element
    else:
        fixed = re.search(
            r"\b(?:Physical|Magical|Hybrid)\s*/\s*(Neutral|Colorless|Fire|Ice|Lightning|Earth|Ruin)\b",
            source.owner_effect,
            re.I,
        )
        if fixed:
            element = fixed.group(1).lower()
        elif chosen_element is not None:
            element = chosen_element
        else:
            raise SourceGapError(f"{class_name} / {ability} requires a player element choice")

    def_pen = re.search(r"(\d+)% Defense penetration", source.owner_effect, re.I)
    spr_pen = re.search(r"(\d+)% Spirit penetration", source.owner_effect, re.I)
    return CombatAction(
        name=ability,
        mp_cost=source.fixed_mp,
        target_scope=parsed.target_scope or "one",
        damage_kind=damage_kind,  # type: ignore[arg-type]
        element=element,  # type: ignore[arg-type]
        power=parsed.power,
        base_hit=parsed.base_hit,
        defense_penetration=int(def_pen.group(1)) / 100.0 if def_pen else 0.0,
        spirit_penetration=int(spr_pen.group(1)) / 100.0 if spr_pen else 0.0,
        physical_weight=parsed.physical_weight,
        magical_weight=parsed.magical_weight,
        status_riders=tuple(StatusRider(status, chance) for status, chance in parsed.status_chances),
    )


def _mend(*, root: Path | None = None) -> CombatAction:
    source = load_ability_source("Mend", class_name="Blue Warden", root=root)
    hp = re.search(r"(\d+)% target Max HP", source.owner_effect, re.I)
    magic = re.search(r"([0-9.]+)\s*[×x]\s*Ilyra", source.owner_effect, re.I)
    owner_text = read_repo_text(source.owner_path, root=root)
    mastery = re.search(r"Gentle Hands[^\n]*Mend gains \+(\d+)% healing potency", owner_text, re.I)
    if source.fixed_mp is None or not (hp and magic and mastery):
        raise SourceGapError("Blue Warden / Mend lacks exact CL9 healing authority")
    return CombatAction(
        name="Mend",
        action_kind="heal",
        mp_cost=source.fixed_mp,
        target_side="ally",
        target_scope="one",
        heal_max_hp_percent=int(hp.group(1)) / 100.0,
        heal_magic_scaling=float(magic.group(1)),
        healing_potency=1.0 + int(mastery.group(1)) / 100.0,
    )


def _clear_warding(*, root: Path | None = None) -> CombatAction:
    source = load_ability_source("Clear Warding", class_name="Blue Warden", root=root)
    heal = re.search(r"restore\s+(\d+)% target Max HP", source.owner_effect, re.I)
    sr = re.search(r"\+(\d+) Status Resistance for (\d+) rounds", source.owner_effect, re.I)
    if source.fixed_mp is None or not (heal and sr):
        raise SourceGapError("Blue Warden / Clear Warding lacks exact CL9 authority")
    from tools.diysim.combat.models import TemporaryModifierSpec
    return CombatAction(
        name="Clear Warding",
        action_kind="heal",
        mp_cost=source.fixed_mp,
        target_side="ally",
        target_scope="one",
        heal_max_hp_percent=int(heal.group(1)) / 100.0,
        clear_harmful_statuses=1,
        temporary_modifiers=(TemporaryModifierSpec(
            effect_id="Clear Warding",
            duration_rounds=int(sr.group(2)),
            status_resistance_flat=int(sr.group(1)),
        ),),
    )


def _renewal(*, root: Path | None = None) -> CombatAction:
    source = load_ability_source("Renewal", class_name="Blue Warden", root=root)
    hp = re.search(r"(\d+)% target Max HP", source.owner_effect, re.I)
    magic = re.search(r"([0-9.]+)\s*[×x]\s*Ilyra", source.owner_effect, re.I)
    if source.fixed_mp is None or not (hp and magic):
        raise SourceGapError("Blue Warden / Renewal lacks exact healing authority")
    return CombatAction(
        name="Renewal",
        action_kind="heal",
        mp_cost=source.fixed_mp,
        target_side="ally",
        target_scope="all",
        heal_max_hp_percent=int(hp.group(1)) / 100.0,
        heal_magic_scaling=float(magic.group(1)),
    )


def _blue_warden_specials(*, root: Path | None = None) -> tuple[int, float, int]:
    revive = load_ability_source("Revive", class_name="Blue Warden", root=root)
    lifeline = load_ability_source("Lifeline", class_name="Blue Warden", root=root)
    text = read_repo_text(revive.owner_path, root=root)
    mastered = re.search(r"Revive recovery 35% → \*\*(\d+)% target Max HP\*\*", text, re.I)
    if revive.fixed_mp is None or lifeline.fixed_mp is None or not mastered:
        raise SourceGapError("Blue Warden lacks exact CL9 Revive/Lifeline authority")
    return revive.fixed_mp, int(mastered.group(1)) / 100.0, lifeline.fixed_mp


def _gentle_continuance_bonus(*, root: Path | None = None) -> float:
    trait = load_trait_source(class_name="Blue Warden", root=root)
    rank_one = next((rank for rank in trait.ranks if rank.label == "Rank I"), None)
    if rank_one is None:
        raise SourceGapError("Blue Warden / Gentle Continuance lacks Rank I")
    match = re.search(r"additional \*\*(\d+)% target Max HP\*\*", rank_one.effect, re.I)
    if not match:
        raise SourceGapError("Blue Warden / Gentle Continuance lacks exact Rank-I bonus")
    return int(match.group(1)) / 100.0


def _war_archer_values(*, root: Path | None = None) -> tuple[int, int, int, float, int, int]:
    sizing = load_ability_source("Sizing Shot", class_name="War Archer", root=root)
    text = read_repo_text(sizing.owner_path, root=root)
    duration = re.search(r"remainder of the current round plus the next \*\*(\d+) full normal rounds\*\*", text, re.I)
    party_crit = re.search(r"all party members gain \*\*\+(\d+) percentage points Critical Chance\*\*", text, re.I)
    torren_crit = re.search(r"Rank II[^\n]*\*\*\+(\d+) percentage points Critical Chance\*\*", text, re.I)
    measured_pen = re.search(r"Colossus Draw[^\n]*penetration becomes \*\*(\d+)%\*\*", text, re.I)
    sizing_mastery = re.search(r"Veteran's Eye[^\n]*Sizing Shot \*\*(\d+)\s*→\s*(\d+) Power\*\*", text, re.I)
    heavy_draw = re.search(r"Heavy Draw[^\n]*Colossus Draw[^\n]*\*\*(\d+)\s*→\s*(\d+) Power\*\*", text, re.I)
    if not (duration and party_crit and torren_crit and measured_pen and sizing_mastery and heavy_draw):
        raise SourceGapError("War Archer lacks exact CL9 Measure/mastery authority")
    return (
        int(duration.group(1)),
        int(party_crit.group(1)),
        int(torren_crit.group(1)),
        int(measured_pen.group(1)) / 100.0,
        int(sizing_mastery.group(2)),
        int(heavy_draw.group(2)),
    )


def _green_discount(*, root: Path | None = None) -> int:
    source = load_ability_source("Spectrum Cascade", class_name="Green Arcanist", root=root)
    text = read_repo_text(source.owner_path, root=root)
    match = re.search(r"first eligible elemental Green Arcanist Base Ability each ordinary round costs (\d+) less MP", text, re.I)
    if not match:
        raise SourceGapError("Green Arcanist lacks Efficient Spectrum authority")
    return int(match.group(1))


@lru_cache(maxsize=4)
def load_zevraya_party_actions(*, root: Path | None = None) -> ZevrayaPartyActions:
    full_rounds, party_crit, torren_crit, measured_pen, sizing_power, colossus_power = _war_archer_values(root=root)
    revive_mp, revive_fraction, lifeline_mp = _blue_warden_specials(root=root)
    sizing = replace(_direct_action("Sizing Shot", "War Archer", root=root), power=sizing_power)
    colossus = replace(_direct_action("Colossus Draw", "War Archer", root=root), power=colossus_power)
    return ZevrayaPartyActions(
        crest_rend=_direct_action("Crest Rend", "Crest Knight", root=root),
        wardens_valor=_direct_action("Warden's Valor", "Blue Warden", root=root),
        mend=_mend(root=root),
        clear_warding=_clear_warding(root=root),
        renewal=_renewal(root=root),
        revive_mp_cost=revive_mp,
        revive_fraction=revive_fraction,
        lifeline_mp_cost=lifeline_mp,
        sizing_shot=sizing,
        colossus_draw=colossus,
        measured_colossus_penetration=measured_pen,
        hunter_measure_full_rounds=full_rounds,
        hunter_measure_party_crit_bonus=party_crit,
        hunter_measure_torren_crit_bonus=torren_crit,
        prism_lance=_direct_action("Prism Lance", "Green Arcanist", chosen_element="earth", root=root),
        spectrum_cascade=_direct_action("Spectrum Cascade", "Green Arcanist", chosen_element="earth", root=root),
        elemental_round_discount=_green_discount(root=root),
        gentle_continuance_bonus=_gentle_continuance_bonus(root=root),
        basic_attack=basic_attack_action(),
    )


def lowest_hp_ally(party: list[CombatUnit]) -> CombatUnit | None:
    conscious = [unit for unit in party if unit.alive]
    return min(conscious, key=lambda unit: (unit.hp / unit.max_hp, unit.stable_index)) if conscious else None


def controlled_ally(party: list[CombatUnit]) -> CombatUnit | None:
    controlled = [unit for unit in party if unit.alive and (unit.has_status("stun") or unit.has_status("freeze") or unit.has_status("staggered"))]
    if not controlled:
        return None
    return min(controlled, key=lambda unit: (0 if unit.has_status("freeze") else 1 if unit.has_status("stun") else 2, unit.stable_index))


def with_measure_crit(action: CombatAction, bonus: int) -> CombatAction:
    base = 5.0 if action.crit_chance is None else action.crit_chance
    return replace(action, crit_chance=base + bonus)


__all__ = [
    "ZevrayaPartyActions",
    "ZevrayaPolicyConfig",
    "controlled_ally",
    "load_zevraya_party_actions",
    "lowest_hp_ally",
    "with_measure_crit",
]
