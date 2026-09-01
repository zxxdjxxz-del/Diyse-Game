"""Repo-backed smart party policy for First Command Warden true-battle work."""
from __future__ import annotations

from dataclasses import dataclass, replace
from functools import lru_cache
from pathlib import Path
import re

from tools.diysim.combat.basic_attack import basic_attack_action
from tools.diysim.combat.derived_stats import effective_attack, effective_magic
from tools.diysim.combat.living_archive import (
    LivingArchiveRecord,
    LivingArchiveState,
    materialize_echo_weave,
)
from tools.diysim.combat.models import CombatAction, CombatUnit, StatusRider, TemporaryModifierSpec
from tools.diysim.sources import (
    SourceGapError,
    load_ability_source,
    load_trait_source,
    parse_authored_action_text,
    read_repo_text,
)

HARMONIZED_STATE_KEY = "harmonized_crest_prime"
LIVING_ARCHIVE_STATE_KEY = "living_archive"


@dataclass(frozen=True)
class WardenPolicyConfig:
    """Competent prepared policy used for the working S020 snapshot."""

    mend_below_hp_fraction: float = 0.50
    renewal_two_allies_below_fraction: float = 0.60

    def __post_init__(self) -> None:
        if not 0.0 < self.mend_below_hp_fraction < 1.0:
            raise ValueError("mend_below_hp_fraction must be between 0 and 1")
        if not 0.0 < self.renewal_two_allies_below_fraction < 1.0:
            raise ValueError("renewal threshold must be between 0 and 1")


@dataclass(frozen=True)
class WardenPartyActions:
    crest_strike: CombatAction
    resonant_pulse: CombatAction
    harmonized_crest_multiplier: float
    wardens_valor: CombatAction
    cinder_shot: CombatAction
    sizing_shot: CombatAction
    colossus_draw: CombatAction
    weave_burst: CombatAction
    mend: CombatAction
    clear_warding: CombatAction
    renewal: CombatAction
    gentle_continuance_bonus: float
    hunter_measure_full_rounds: int
    hunter_measure_party_crit_bonus: int
    hunter_measure_torren_crit_bonus: int
    measured_colossus_penetration: float
    living_archive_capacity: int
    echo_weave_potency: float
    echo_weave_cost_scale: float
    echo_weave_minimum_mp: int
    basic_attack: CombatAction


def _direct_action(ability: str, class_name: str, *, root: Path | None = None) -> CombatAction:
    source = load_ability_source(ability, class_name=class_name, root=root)
    parsed = parse_authored_action_text(ability, source.owner_effect)
    if source.fixed_mp is None:
        raise SourceGapError(f"{class_name} / {ability} lacks fixed MP authority")
    if parsed.damage_kind is None or parsed.power is None:
        raise SourceGapError(f"{class_name} / {ability} lacks direct-damage identity")
    if parsed.element_mode != "fixed" or parsed.element is None:
        raise SourceGapError(f"{class_name} / {ability} lacks fixed element authority")
    penetration = re.search(r"(\d+)% Defense penetration", source.owner_effect, re.I)
    return CombatAction(
        name=ability,
        mp_cost=source.fixed_mp,
        target_scope=parsed.target_scope or "one",
        damage_kind=parsed.damage_kind,  # type: ignore[arg-type]
        element=parsed.element,  # type: ignore[arg-type]
        power=parsed.power,
        base_hit=parsed.base_hit,
        defense_penetration=int(penetration.group(1)) / 100.0 if penetration else 0.0,
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


def _clear_warding(*, root: Path | None = None) -> CombatAction:
    source = load_ability_source("Clear Warding", class_name="Blue Warden", root=root)
    if source.fixed_mp is None:
        raise SourceGapError("Blue Warden / Clear Warding lacks fixed MP authority")
    heal = re.search(r"restore\s+(\d+)% target Max HP", source.owner_effect, re.I)
    sr = re.search(r"\+(\d+) Status Resistance for (\d+) rounds", source.owner_effect, re.I)
    if not (heal and sr):
        raise SourceGapError("Blue Warden / Clear Warding lacks exact heal/SR authority")
    return CombatAction(
        name="Clear Warding",
        action_kind="heal",
        mp_cost=source.fixed_mp,
        target_side="ally",
        target_scope="one",
        heal_max_hp_percent=int(heal.group(1)) / 100.0,
        clear_harmful_statuses=1,
        temporary_modifiers=(
            TemporaryModifierSpec(
                effect_id="Clear Warding",
                duration_rounds=int(sr.group(2)),
                status_resistance_flat=int(sr.group(1)),
            ),
        ),
    )


def _renewal(*, root: Path | None = None) -> CombatAction:
    source = load_ability_source("Renewal", class_name="Blue Warden", root=root)
    if source.fixed_mp is None:
        raise SourceGapError("Blue Warden / Renewal lacks fixed MP authority")
    hp = re.search(r"(\d+)% target Max HP", source.owner_effect, re.I)
    magic = re.search(r"([0-9.]+)\s*[×x]\s*Ilyra", source.owner_effect, re.I)
    if not (hp and magic):
        raise SourceGapError("Blue Warden / Renewal lacks exact healing formula")
    return CombatAction(
        name="Renewal",
        action_kind="heal",
        mp_cost=source.fixed_mp,
        target_side="ally",
        target_scope="all",
        heal_max_hp_percent=int(hp.group(1)) / 100.0,
        heal_magic_scaling=float(magic.group(1)),
    )


def _gentle_continuance_bonus(*, root: Path | None = None) -> float:
    trait = load_trait_source(class_name="Blue Warden", root=root)
    rank_one = next((rank for rank in trait.ranks if rank.label == "Rank I"), None)
    if rank_one is None:
        raise SourceGapError("Blue Warden / Gentle Continuance lacks Rank I authority")
    match = re.search(r"additional \*\*(\d+)% target Max HP\*\*", rank_one.effect, re.I)
    if not match:
        raise SourceGapError("Blue Warden / Gentle Continuance lacks exact Rank-I healing bonus")
    return int(match.group(1)) / 100.0


def _harmonized_crest_multiplier(*, root: Path | None = None) -> float:
    trait = load_trait_source(class_name="Crest Knight", root=root)
    rank_one = next((rank for rank in trait.ranks if rank.label == "Rank I"), None)
    if rank_one is None:
        raise SourceGapError("Crest Knight / Harmonized Crest lacks Rank I authority")
    match = re.search(r"\*\*\+(\d+)% final damage\*\*", rank_one.effect, re.I)
    if not match:
        raise SourceGapError("Crest Knight / Harmonized Crest lacks exact Rank-I damage bonus")
    return 1.0 + int(match.group(1)) / 100.0


def _war_archer_measure_values(*, root: Path | None = None) -> tuple[int, int, int, float, int, int]:
    sizing = load_ability_source("Sizing Shot", class_name="War Archer", root=root)
    text = read_repo_text(sizing.owner_path, root=root)
    duration = re.search(r"remainder of the current round plus the next \*\*(\d+) full normal rounds\*\*", text, re.I)
    party_crit = re.search(r"all party members gain \*\*\+(\d+) percentage points Critical Chance\*\*", text, re.I)
    torren_crit = re.search(r"Rank II[^\n]*\*\*\+(\d+) percentage points Critical Chance\*\*", text, re.I)
    measured_pen = re.search(r"Colossus Draw[^\n]*penetration becomes \*\*(\d+)%\*\*", text, re.I)
    veteran_eye = re.search(r"Veteran's Eye[^\n]*Sizing Shot \*\*(\d+)\s*→\s*(\d+) Power\*\*", text, re.I)
    heavy_draw = re.search(r"Heavy Draw[^\n]*Colossus Draw[^\n]*\*\*(\d+)\s*→\s*(\d+) Power\*\*", text, re.I)
    if not (duration and party_crit and torren_crit and measured_pen and veteran_eye and heavy_draw):
        raise SourceGapError("War Archer lacks exact CL6 Hunter's Measure / mastery authority")
    return (
        int(duration.group(1)),
        int(party_crit.group(1)),
        int(torren_crit.group(1)),
        int(measured_pen.group(1)) / 100.0,
        int(veteran_eye.group(2)),
        int(heavy_draw.group(2)),
    )


def _cardweaver_archive_values(*, root: Path | None = None) -> tuple[int, float, float, int]:
    echo = load_ability_source("Echo Weave", class_name="Cardweaver", root=root)
    text = read_repo_text(echo.owner_path, root=root)
    capacity = re.search(r"Rank I retains the last \*\*(\d+)\*\* eligible allied actions", text, re.I)
    potency = re.search(r"Quick Study[^\n]*\*\*(\d+)%\s*→\s*(\d+)%\*\*", text, re.I)
    cost_scale = re.search(r"Echo Weave costs \*\*(\d+)% of the recorded action's authored Base MP\*\*", text, re.I)
    minimum = re.search(r"minimum \*\*(\d+) MP\*\*", text, re.I)
    if not (capacity and potency and cost_scale and minimum):
        raise SourceGapError("Cardweaver lacks exact CL4 Living Archive / Echo Weave authority")
    return (
        int(capacity.group(1)),
        int(potency.group(2)) / 100.0,
        int(cost_scale.group(1)) / 100.0,
        int(minimum.group(1)),
    )


@lru_cache(maxsize=4)
def load_warden_party_actions(*, root: Path | None = None) -> WardenPartyActions:
    """Parse the working S020 learned package once per source root."""
    (
        full_rounds,
        party_crit,
        torren_crit,
        measured_pen,
        sizing_mastered_power,
        colossus_mastered_power,
    ) = _war_archer_measure_values(root=root)
    archive_capacity, echo_potency, echo_cost_scale, echo_minimum = _cardweaver_archive_values(root=root)
    sizing = replace(
        _direct_action("Sizing Shot", "War Archer", root=root),
        power=sizing_mastered_power,
    )
    colossus = replace(
        _direct_action("Colossus Draw", "War Archer", root=root),
        power=colossus_mastered_power,
    )
    return WardenPartyActions(
        crest_strike=_direct_action("Crest Strike", "Crest Knight", root=root),
        resonant_pulse=_direct_action("Resonant Pulse", "Crest Knight", root=root),
        harmonized_crest_multiplier=_harmonized_crest_multiplier(root=root),
        wardens_valor=_direct_action("Warden's Valor", "Blue Warden", root=root),
        cinder_shot=_direct_action("Cinder Shot", "War Archer", root=root),
        sizing_shot=sizing,
        colossus_draw=colossus,
        weave_burst=_direct_action("Weave Burst", "Cardweaver", root=root),
        mend=_mend(root=root),
        clear_warding=_clear_warding(root=root),
        renewal=_renewal(root=root),
        gentle_continuance_bonus=_gentle_continuance_bonus(root=root),
        hunter_measure_full_rounds=full_rounds,
        hunter_measure_party_crit_bonus=party_crit,
        hunter_measure_torren_crit_bonus=torren_crit,
        measured_colossus_penetration=measured_pen,
        living_archive_capacity=archive_capacity,
        echo_weave_potency=echo_potency,
        echo_weave_cost_scale=echo_cost_scale,
        echo_weave_minimum_mp=echo_minimum,
        basic_attack=basic_attack_action(),
    )


def lowest_hp_ally(party: list[CombatUnit]) -> CombatUnit | None:
    conscious = [unit for unit in party if unit.alive]
    if not conscious:
        return None
    return min(conscious, key=lambda unit: (unit.hp / unit.max_hp, unit.stable_index))


def _control_target(party: list[CombatUnit]) -> CombatUnit | None:
    controlled = [unit for unit in party if unit.alive and (unit.has_status("stun") or unit.has_status("staggered"))]
    if not controlled:
        return None
    return min(controlled, key=lambda unit: (0 if unit.has_status("stun") else 1, unit.stable_index))


def _with_measure_crit(action: CombatAction, bonus: int) -> CombatAction:
    base = 5.0 if action.crit_chance is None else action.crit_chance
    return replace(action, crit_chance=base + bonus)


def _nimera_unit(party: list[CombatUnit]) -> CombatUnit:
    return next(unit for unit in party if unit.template.name == "Nimera")


def _living_archive(party: list[CombatUnit], actions: WardenPartyActions) -> LivingArchiveState:
    nimera = _nimera_unit(party)
    existing = nimera.tactical_states.get(LIVING_ARCHIVE_STATE_KEY)
    if isinstance(existing, LivingArchiveState):
        return existing
    state = LivingArchiveState(capacity=actions.living_archive_capacity)
    nimera.tactical_states[LIVING_ARCHIVE_STATE_KEY] = state
    return state


def _canonical_record_action(action: CombatAction, actions: WardenPartyActions) -> CombatAction | None:
    """Strip source-actor-only temporary Trait/target-context bonuses before recording."""
    by_name = {
        actions.crest_strike.name: actions.crest_strike,
        actions.resonant_pulse.name: actions.resonant_pulse,
        actions.wardens_valor.name: actions.wardens_valor,
        actions.cinder_shot.name: actions.cinder_shot,
        actions.sizing_shot.name: actions.sizing_shot,
        actions.colossus_draw.name: actions.colossus_draw,
        actions.mend.name: actions.mend,
        actions.clear_warding.name: actions.clear_warding,
        actions.renewal.name: actions.renewal,
    }
    return by_name.get(action.name)


def _record_for_nimera(
    actor: CombatUnit,
    party: list[CombatUnit],
    actions: WardenPartyActions,
    *,
    category: str,
    action: CombatAction,
) -> None:
    if actor.template.name == "Nimera" or category != "Ability":
        return
    canonical = _canonical_record_action(action, actions)
    if canonical is None:
        return
    _living_archive(party, actions).observe_completed_action(
        canonical,
        source_actor=actor.template.name,
        category="ability",
        authored_base_mp=canonical.mp_cost,
    )


def _damage_score(actor: CombatUnit, action: CombatAction, *, target_is_ring: bool) -> float:
    if action.power is None:
        return 0.0
    if action.damage_kind == "physical":
        offense = effective_attack(actor)
    elif action.damage_kind == "magical":
        offense = effective_magic(actor)
    else:
        physical = 0.5 if action.physical_weight is None else action.physical_weight
        magical = 0.5 if action.magical_weight is None else action.magical_weight
        offense = effective_attack(actor) * physical + effective_magic(actor) * magical
    targets = 2 if target_is_ring and action.target_scope == "all" else 1
    return offense * action.power * action.final_damage_multiplier * targets


def _choose_cyanis_action(
    actor: CombatUnit,
    actions: WardenPartyActions,
    *,
    sealed_category: str | None,
    hunter_measure_active: bool,
    target_is_ring: bool,
) -> tuple[str, CombatAction, CombatUnit | None]:
    if sealed_category == "Ability":
        attack = actions.basic_attack
        if hunter_measure_active and not target_is_ring:
            attack = _with_measure_crit(attack, actions.hunter_measure_party_crit_bonus)
        return "Attack", attack, None

    prime = actor.tactical_states.get(HARMONIZED_STATE_KEY)
    if prime == "magical" and actor.mp >= actions.resonant_pulse.mp_cost:
        action = replace(
            actions.resonant_pulse,
            final_damage_multiplier=(
                actions.resonant_pulse.final_damage_multiplier * actions.harmonized_crest_multiplier
            ),
        )
    elif prime == "physical" and actor.mp >= actions.crest_strike.mp_cost:
        action = replace(
            actions.crest_strike,
            final_damage_multiplier=(
                actions.crest_strike.final_damage_multiplier * actions.harmonized_crest_multiplier
            ),
        )
    elif actor.mp >= actions.crest_strike.mp_cost:
        action = actions.crest_strike
    elif actor.mp >= actions.resonant_pulse.mp_cost:
        action = actions.resonant_pulse
    else:
        attack = actions.basic_attack
        if hunter_measure_active and not target_is_ring:
            attack = _with_measure_crit(attack, actions.hunter_measure_party_crit_bonus)
        return "Attack", attack, None

    if hunter_measure_active and not target_is_ring:
        action = _with_measure_crit(action, actions.hunter_measure_party_crit_bonus)

    if action.damage_kind == "physical":
        actor.tactical_states[HARMONIZED_STATE_KEY] = "magical"
    elif action.damage_kind == "magical":
        actor.tactical_states[HARMONIZED_STATE_KEY] = "physical"
    return "Ability", action, None


def _choose_torren_action(
    actor: CombatUnit,
    actions: WardenPartyActions,
    *,
    sealed_category: str | None,
    hunter_measure_active: bool,
    target_is_ring: bool,
) -> tuple[str, CombatAction, CombatUnit | None]:
    if sealed_category == "Ability":
        attack = actions.basic_attack
        if hunter_measure_active and not target_is_ring:
            attack = _with_measure_crit(
                attack,
                actions.hunter_measure_party_crit_bonus + actions.hunter_measure_torren_crit_bonus,
            )
        return "Attack", attack, None

    if target_is_ring:
        if actor.mp >= actions.colossus_draw.mp_cost:
            return "Ability", actions.colossus_draw, None
        if actor.mp >= actions.cinder_shot.mp_cost:
            return "Ability", actions.cinder_shot, None
        return "Attack", actions.basic_attack, None

    if not hunter_measure_active and actor.mp >= actions.sizing_shot.mp_cost:
        return "Ability", actions.sizing_shot, None
    if hunter_measure_active and actor.mp >= actions.colossus_draw.mp_cost:
        return "Ability", replace(
            _with_measure_crit(
                actions.colossus_draw,
                actions.hunter_measure_party_crit_bonus + actions.hunter_measure_torren_crit_bonus,
            ),
            defense_penetration=actions.measured_colossus_penetration,
        ), None
    if actor.mp >= actions.cinder_shot.mp_cost:
        cinder = actions.cinder_shot
        if hunter_measure_active:
            cinder = _with_measure_crit(
                cinder,
                actions.hunter_measure_party_crit_bonus + actions.hunter_measure_torren_crit_bonus,
            )
        return "Ability", cinder, None
    attack = actions.basic_attack
    if hunter_measure_active:
        attack = _with_measure_crit(
            attack,
            actions.hunter_measure_party_crit_bonus + actions.hunter_measure_torren_crit_bonus,
        )
    return "Attack", attack, None


def _choose_nimera_action(
    actor: CombatUnit,
    party: list[CombatUnit],
    actions: WardenPartyActions,
    *,
    sealed_category: str | None,
    hunter_measure_active: bool,
    target_is_ring: bool,
) -> tuple[str, CombatAction, CombatUnit | None]:
    if sealed_category == "Ability":
        attack = actions.basic_attack
        if hunter_measure_active and not target_is_ring:
            attack = _with_measure_crit(attack, actions.hunter_measure_party_crit_bonus)
        return "Attack", attack, None

    archive = _living_archive(party, actions)
    best_echo: CombatAction | None = None
    best_score = -1.0
    for record in archive.records:
        if record.action.action_kind != "damage" or record.action.target_side != "enemy":
            continue
        echo = materialize_echo_weave(
            record,
            potency=actions.echo_weave_potency,
            cost_scale=actions.echo_weave_cost_scale,
            minimum_mp=actions.echo_weave_minimum_mp,
        )
        if actor.mp < echo.mp_cost:
            continue
        if hunter_measure_active and not target_is_ring:
            echo = _with_measure_crit(echo, actions.hunter_measure_party_crit_bonus)
        score = _damage_score(actor, echo, target_is_ring=target_is_ring)
        if score > best_score:
            best_echo = echo
            best_score = score

    weave = actions.weave_burst
    if hunter_measure_active and not target_is_ring:
        weave = _with_measure_crit(weave, actions.hunter_measure_party_crit_bonus)
    weave_score = _damage_score(actor, weave, target_is_ring=target_is_ring)

    if best_echo is not None and (actor.mp < weave.mp_cost or best_score >= weave_score):
        return "Ability", best_echo, None
    if actor.mp >= weave.mp_cost:
        return "Ability", weave, None
    if best_echo is not None:
        return "Ability", best_echo, None
    attack = actions.basic_attack
    if hunter_measure_active and not target_is_ring:
        attack = _with_measure_crit(attack, actions.hunter_measure_party_crit_bonus)
    return "Attack", attack, None


def _choose_ilyra_action(
    actor: CombatUnit,
    party: list[CombatUnit],
    actions: WardenPartyActions,
    *,
    sealed_category: str | None,
    hunter_measure_active: bool,
    target_is_ring: bool,
    config: WardenPolicyConfig,
) -> tuple[str, CombatAction, CombatUnit | None]:
    control_target = _control_target(party)
    if control_target is not None and actor.mp >= actions.clear_warding.mp_cost:
        return "Ability", actions.clear_warding, control_target

    wounded = [
        unit for unit in party
        if unit.alive and unit.hp / unit.max_hp < config.renewal_two_allies_below_fraction
    ]
    if len(wounded) >= 2 and actor.mp >= actions.renewal.mp_cost:
        return "Ability", actions.renewal, None

    heal_target = lowest_hp_ally(party)
    if (
        heal_target is not None
        and heal_target.hp / heal_target.max_hp < config.mend_below_hp_fraction
        and actor.mp >= actions.mend.mp_cost
    ):
        return "Ability", actions.mend, heal_target

    offensive = actions.wardens_valor
    if hunter_measure_active and not target_is_ring:
        offensive = _with_measure_crit(offensive, actions.hunter_measure_party_crit_bonus)
    can_ability = actor.mp >= offensive.mp_cost
    if sealed_category == "Ability":
        attack = actions.basic_attack
        if hunter_measure_active and not target_is_ring:
            attack = _with_measure_crit(attack, actions.hunter_measure_party_crit_bonus)
        return "Attack", attack, None
    if can_ability:
        return "Ability", offensive, None
    attack = actions.basic_attack
    if hunter_measure_active and not target_is_ring:
        attack = _with_measure_crit(attack, actions.hunter_measure_party_crit_bonus)
    return "Attack", attack, None


def choose_player_action(
    actor: CombatUnit,
    party: list[CombatUnit],
    actions: WardenPartyActions,
    *,
    sealed_category: str | None,
    hunter_measure_active: bool = False,
    target_is_ring: bool = False,
    config: WardenPolicyConfig,
) -> tuple[str, CombatAction, CombatUnit | None]:
    """Choose an ordinary action without reading future enemy actions."""
    if actor.template.name == "Cyanis":
        result = _choose_cyanis_action(
            actor,
            actions,
            sealed_category=sealed_category,
            hunter_measure_active=hunter_measure_active,
            target_is_ring=target_is_ring,
        )
    elif actor.template.name == "Ilyra":
        result = _choose_ilyra_action(
            actor,
            party,
            actions,
            sealed_category=sealed_category,
            hunter_measure_active=hunter_measure_active,
            target_is_ring=target_is_ring,
            config=config,
        )
    elif actor.template.name == "Torren":
        result = _choose_torren_action(
            actor,
            actions,
            sealed_category=sealed_category,
            hunter_measure_active=hunter_measure_active,
            target_is_ring=target_is_ring,
        )
    elif actor.template.name == "Nimera":
        result = _choose_nimera_action(
            actor,
            party,
            actions,
            sealed_category=sealed_category,
            hunter_measure_active=hunter_measure_active,
            target_is_ring=target_is_ring,
        )
    else:
        raise ValueError(f"unsupported Warden policy character: {actor.template.name}")

    category, action, target = result
    _record_for_nimera(
        actor,
        party,
        actions,
        category=category,
        action=action,
    )
    return result


__all__ = [
    "HARMONIZED_STATE_KEY",
    "LIVING_ARCHIVE_STATE_KEY",
    "WardenPartyActions",
    "WardenPolicyConfig",
    "choose_player_action",
    "load_warden_party_actions",
    "lowest_hp_ally",
]
