"""Executable Matron Zevraya prepared-play sensitivity runtime.

Owner combat values are read from repository authority. The prepared inventory,
player strategy, and v104 non-diluting Reservoir structure are explicitly
isolated as working simulation policy rather than silently promoted to canon.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import random
import statistics
from pathlib import Path
from typing import Literal

from tools.diysim.common import round_half_up
from tools.diysim.combat.action_resolution import resolve_damage, resolve_heal, roll_status
from tools.diysim.combat.consumables import PreparedInventory, use_consumable
from tools.diysim.combat.damage import direct_damage
from tools.diysim.combat.derived_stats import effective_attack, effective_defense, effective_magic, effective_spirit, effective_speed
from tools.diysim.combat.hit_evasion import adjusted_hit_chance
from tools.diysim.combat.models import CombatAction, CombatUnit, Combatant, StatusRider
from tools.diysim.combat.status_runtime import complete_turn, end_round, turn_is_blocked
from tools.diysim.overlays import BalanceOverlay, scale_direct_damage_power, scale_effective_core_stat_level
from tools.diysim.progression import Stats
from tools.diysim.sources import extract_heading_block, load_combat_rules, read_repo_text

from .policy import ZevrayaPartyActions, ZevrayaPolicyConfig, load_zevraya_party_actions, lowest_hp_ally, controlled_ally, with_measure_crit
from .prepared_policy import build_zevraya_prepared_inventory, choose_prepared_item
from .repo_loader import (
    ConductionRule,
    FiniteTargetSource,
    OWNER_PATH,
    PhysicalSupportActorSource,
    ZevrayaRepoData,
    load_zevraya_repo_data,
)
from .snapshots import load_zevraya_party_snapshot

StructureMode = Literal["owner", "non_diluting"]
Strategy = Literal["rush", "dismantle"]
FormName = Literal["blood_matron", "perfected_war_mother"]


@dataclass
class _FiniteTargetState:
    source: FiniteTargetSource
    hp: int

    @classmethod
    def from_source(cls, source: FiniteTargetSource) -> "_FiniteTargetState":
        return cls(source=source, hp=source.hp)

    @property
    def alive(self) -> bool:
        return self.hp > 0


@dataclass
class _BroodState:
    source: PhysicalSupportActorSource
    hp: int

    @classmethod
    def from_source(cls, source: PhysicalSupportActorSource) -> "_BroodState":
        return cls(source=source, hp=source.hp)

    @property
    def alive(self) -> bool:
        return self.hp > 0


@dataclass(frozen=True)
class ZevrayaBattleOutcome:
    winner: Literal["party", "enemy", "draw"]
    rounds: int
    any_party_ko: bool
    party_hp_fraction: float
    party_mp_fraction: float
    form2_reached: bool
    reservoirs_destroyed: int
    brood_deployments: int
    brood_actions: int
    items_used: int
    hunter_measure_establishments: int
    sustenance_heal_uses: int
    reconstruction_uses: int
    conduction_uses: int
    plating_uses: int
    bleed_exposed: bool
    control_exposed: bool


@dataclass(frozen=True)
class ZevrayaSimulationSummary:
    runs: int
    player_level: int
    structure_mode: StructureMode
    strategy: Strategy
    prepared_inventory: bool
    power_multiplier: float
    effective_stat_level_offset: int
    win_rate: float
    wipe_rate: float
    any_ko_rate: float
    mean_rounds: float
    median_rounds: float
    p10_rounds: float
    p90_rounds: float
    mean_remaining_party_hp: float
    mean_remaining_party_mp: float
    form2_reach_rate: float
    mean_reservoirs_destroyed: float
    mean_brood_deployments: float
    mean_brood_actions: float
    mean_items_used: float
    mean_hunter_measure_establishments: float
    mean_sustenance_heal_uses: float
    mean_reconstruction_uses: float
    mean_conduction_uses: float
    mean_plating_uses: float
    bleed_exposure_rate: float
    control_exposure_rate: float


def _party_fraction(party: list[CombatUnit], attr: str, maximum_attr: str) -> float:
    maximum = sum(getattr(unit, maximum_attr) for unit in party)
    if maximum <= 0:
        return 0.0
    return sum(max(0, getattr(unit, attr)) for unit in party) / maximum


def _percentile(values: list[int], fraction: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = round_half_up((len(ordered) - 1) * fraction)
    return float(ordered[max(0, min(len(ordered) - 1, index))])


def _random_conscious(party: list[CombatUnit], rng: random.Random) -> CombatUnit:
    legal = [unit for unit in party if unit.alive]
    if not legal:
        raise ValueError("no conscious party target")
    return rng.choice(legal)


def _branch_lock(name: str, *, root: Path | None = None) -> int:
    block = extract_heading_block(read_repo_text(OWNER_PATH, root=root), name)
    import re
    match = re.search(r"(\d+)-round repetition lock", block, re.I)
    if not match:
        raise ValueError(f"{OWNER_PATH} lacks repetition lock for {name}")
    return int(match.group(1))


def _action_locked(name: str, round_number: int, locked_through: dict[str, int]) -> bool:
    return round_number <= locked_through.get(name, 0)


def _set_lock(name: str, duration: int, round_number: int, locked_through: dict[str, int]) -> None:
    if duration > 0:
        locked_through[name] = round_number + duration


def _overlay_action(action: CombatAction, overlay: BalanceOverlay) -> CombatAction:
    return scale_direct_damage_power(action, overlay.direct_damage_power_multiplier)


def _overlay_conduction(rule: ConductionRule, overlay: BalanceOverlay) -> ConductionRule:
    return replace(rule, power=rule.power * overlay.direct_damage_power_multiplier)  # type: ignore[arg-type]


def _overlay_support(source: PhysicalSupportActorSource, overlay: BalanceOverlay) -> PhysicalSupportActorSource:
    return replace(source, action=_overlay_action(source.action, overlay))


def _overlay_data(data: ZevrayaRepoData, overlay: BalanceOverlay, *, root: Path | None = None) -> ZevrayaRepoData:
    form1_stats = data.blood_matron.stats
    form2_stats = data.perfected_war_mother.stats
    if overlay.effective_stat_level_offset:
        form1_stats = scale_effective_core_stat_level(
            form1_stats,
            displayed_level=28,
            level_offset=overlay.effective_stat_level_offset,
            root=root,
        )
        form2_stats = scale_effective_core_stat_level(
            form2_stats,
            displayed_level=29,
            level_offset=overlay.effective_stat_level_offset,
            root=root,
        )
    form1 = replace(data.blood_matron, stats=form1_stats)
    form2 = replace(data.perfected_war_mother, stats=form2_stats)
    return replace(
        data,
        blood_matron=form1,
        perfected_war_mother=form2,
        form1_core_actions=tuple(_overlay_action(action, overlay) for action in data.form1_core_actions),
        crimson_arc=_overlay_action(data.crimson_arc, overlay),
        form2_core_actions=tuple(_overlay_action(action, overlay) for action in data.form2_core_actions),
        sustenance_draw=replace(data.sustenance_draw, action=_overlay_action(data.sustenance_draw.action, overlay)),
        perfected_siphon=replace(data.perfected_siphon, action=_overlay_action(data.perfected_siphon.action, overlay)),
        weather_conduction=_overlay_conduction(data.weather_conduction, overlay),
        perfected_conduction=_overlay_conduction(data.perfected_conduction, overlay),
        brood_organism=_overlay_support(data.brood_organism, overlay),
        perfected_brood_organism=_overlay_support(data.perfected_brood_organism, overlay),
    )


def _apply_defensive_branch(boss: CombatUnit, base_stats: Stats, active: bool) -> None:
    if active:
        stats = replace(
            base_stats,
            defense=round_half_up(base_stats.defense * 1.15),
            spirit=round_half_up(base_stats.spirit * 1.15),
        )
    else:
        stats = base_stats
    boss.template = replace(boss.template, stats=stats)


def _resolve_player_damage_finite(
    actor: CombatUnit,
    action: CombatAction,
    target: _FiniteTargetState | _BroodState,
    rng: random.Random,
) -> int:
    if action.element not in {"neutral", "colorless"}:
        raise ValueError("finite support policy may only use Neutral/Colorless damage without authored support affinities")
    rules = load_combat_rules()
    evasion = target.source.evasion
    base_hit = rules.default_player_base_hit if action.base_hit is None else action.base_hit
    if rng.randint(1, 100) > adjusted_hit_chance(base_hit, evasion):
        return 0
    crit_chance = rules.base_crit_chance if action.crit_chance is None else action.crit_chance
    crit = rng.random() * 100 < max(0.0, min(rules.crit_chance_cap, crit_chance))
    power = rules.basic_attack_power if action.power is None else action.power
    physical_weight = 0.5 if action.physical_weight is None else action.physical_weight
    magical_weight = 0.5 if action.magical_weight is None else action.magical_weight
    damage = direct_damage(
        action.damage_kind,
        attack=effective_attack(actor),
        magic=effective_magic(actor),
        defense=target.source.defense,
        spirit=target.source.spirit,
        power=power,
        defense_penetration=action.defense_penetration,
        spirit_penetration=action.spirit_penetration,
        physical_weight=physical_weight,
        magical_weight=magical_weight,
        crit=crit,
    )
    target.hp = max(0, target.hp - damage)
    return damage


def _resolve_brood_damage(
    brood: _BroodState,
    party: list[CombatUnit],
    rng: random.Random,
) -> tuple[bool, bool]:
    target = _random_conscious(party, rng)
    action = brood.source.action
    rules = load_combat_rules()
    base_hit = rules.default_player_base_hit if action.base_hit is None else action.base_hit
    if rng.randint(1, 100) > adjusted_hit_chance(base_hit, target.template.evasion):
        return False, False
    crit_chance = rules.base_crit_chance if action.crit_chance is None else action.crit_chance
    crit = rng.random() * 100 < max(0.0, min(rules.crit_chance_cap, crit_chance))
    power = rules.basic_attack_power if action.power is None else action.power
    damage = direct_damage(
        "physical",
        attack=brood.source.attack,
        magic=0.0,
        defense=effective_defense(target),
        spirit=effective_spirit(target),
        power=power,
        defense_penetration=action.defense_penetration,
        spirit_penetration=action.spirit_penetration,
        crit=crit,
    )
    target.hp = max(0, target.hp - damage)
    had_bleed = target.has_status("bleed")
    if target.alive:
        for rider in action.status_riders:
            roll_status(action, rider, target, rng)
    return (not had_bleed and target.has_status("bleed")), False


def _conduction_action(rule: ConductionRule, index: int) -> CombatAction:
    phase = rule.cycle[index % len(rule.cycle)]
    if phase == "gale":
        return CombatAction(
            name=rule.name,
            target_scope="one",
            damage_kind="magical",
            element="colorless",
            power=rule.power,
            base_hit=rule.base_hit,
        )
    if phase == "storm":
        return CombatAction(
            name=rule.name,
            target_scope="one",
            damage_kind="magical",
            element="lightning",
            power=rule.power,
            base_hit=rule.base_hit,
            status_riders=(StatusRider("stun", rule.stun_chance),),
        )
    return CombatAction(
        name=rule.name,
        target_scope="one",
        damage_kind="magical",
        element="ice",
        power=rule.power,
        base_hit=rule.base_hit,
        status_riders=(StatusRider("freeze", rule.freeze_chance),),
    )


def _resolve_enemy_damage(
    boss: CombatUnit,
    action: CombatAction,
    party: list[CombatUnit],
    rng: random.Random,
) -> tuple[int, bool, bool]:
    targets = [unit for unit in party if unit.alive]
    if action.target_scope == "one":
        targets = [_random_conscious(party, rng)]
    total = 0
    bleed_exposed = False
    control_exposed = False
    for target in targets:
        before = set(target.statuses)
        total += resolve_damage(boss, action, target, rng)
        after = set(target.statuses)
        bleed_exposed = bleed_exposed or ("bleed" not in before and "bleed" in after)
        control_exposed = control_exposed or bool((after - before) & {"freeze", "stun", "staggered"})
    return total, bleed_exposed, control_exposed


def _round_order(
    party: list[CombatUnit],
    boss: CombatUnit,
    brood: _BroodState | None,
) -> list[tuple[str, object]]:
    entries: list[tuple[float, int, int, str, object]] = []
    for unit in party:
        if unit.alive:
            entries.append((-effective_speed(unit), 0, unit.stable_index, "party", unit))
    if boss.alive:
        entries.append((-effective_speed(boss), 1, boss.stable_index, "boss", boss))
    if brood is not None and brood.alive:
        entries.append((-brood.source.speed, 1, 99, "brood", brood))
    entries.sort(key=lambda item: (item[0], item[1], item[2]))
    return [(kind, obj) for _, _, _, kind, obj in entries]


def _support_target_for_strategy(
    strategy: Strategy,
    reservoirs: dict[str, _FiniteTargetState],
    brood: _BroodState | None,
    party: list[CombatUnit],
) -> _FiniteTargetState | _BroodState | None:
    if strategy == "dismantle":
        for name in ("Brood", "Conduction", "Sustenance", "Armor"):
            target = reservoirs.get(name)
            if target is not None and target.alive:
                return target
        if brood is not None and brood.alive:
            return brood
        return None

    if brood is not None and brood.alive:
        living = [unit for unit in party if unit.alive]
        if living and min(unit.hp / unit.max_hp for unit in living) < 0.55:
            return brood
    return None


def _support_action_for(actor: CombatUnit, actions: ZevrayaPartyActions, hunter_measure_active: bool) -> CombatAction:
    if actor.template.name == "Ilyra" and actor.mp >= actions.wardens_valor.mp_cost:
        return actions.wardens_valor
    if actor.template.name == "Torren" and actor.mp >= actions.colossus_draw.mp_cost:
        return actions.colossus_draw
    # Basic Attack is explicitly Neutral and avoids inventing affinities or
    # support-status behavior for Reservoir rows that do not author it.
    return actions.basic_attack


def _boss_offense_for(
    actor: CombatUnit,
    actions: ZevrayaPartyActions,
    *,
    hunter_measure_active: bool,
    multiple_hostiles: bool,
    vaelira_discount_available: bool,
) -> tuple[CombatAction, int]:
    name = actor.template.name
    if name == "Cyanis":
        action = actions.crest_rend
        if hunter_measure_active:
            action = with_measure_crit(action, actions.hunter_measure_party_crit_bonus)
        return (action, action.mp_cost)
    if name == "Ilyra":
        action = actions.wardens_valor
        if hunter_measure_active:
            action = with_measure_crit(action, actions.hunter_measure_party_crit_bonus)
        return (action, action.mp_cost)
    if name == "Torren":
        if not hunter_measure_active and actor.mp >= actions.sizing_shot.mp_cost:
            return actions.sizing_shot, actions.sizing_shot.mp_cost
        if hunter_measure_active and actor.mp >= actions.colossus_draw.mp_cost:
            action = replace(
                with_measure_crit(
                    actions.colossus_draw,
                    actions.hunter_measure_party_crit_bonus + actions.hunter_measure_torren_crit_bonus,
                ),
                defense_penetration=actions.measured_colossus_penetration,
            )
            return action, action.mp_cost
        return actions.basic_attack, 0
    if name == "Vaelira":
        action = actions.spectrum_cascade if multiple_hostiles else actions.prism_lance
        if hunter_measure_active:
            action = with_measure_crit(action, actions.hunter_measure_party_crit_bonus)
        cost = action.mp_cost
        if vaelira_discount_available:
            cost = max(1, cost - actions.elemental_round_discount)
        if actor.mp >= cost:
            return action, cost
        return actions.basic_attack, 0
    return actions.basic_attack, 0


def _trait_adjusted_heal(
    action: CombatAction,
    target: CombatUnit,
    *,
    first_direct_heal_this_round: bool,
    gentle_continuance_bonus: float,
) -> CombatAction:
    if first_direct_heal_this_round and target.hp / target.max_hp < 0.50:
        return replace(action, heal_max_hp_percent=action.heal_max_hp_percent + gentle_continuance_bonus)
    return action


def _run_zevraya_with_data(
    rng: random.Random,
    data: ZevrayaRepoData,
    *,
    player_level: int,
    structure_mode: StructureMode,
    strategy: Strategy,
    overlay: BalanceOverlay,
    policy: ZevrayaPolicyConfig,
    use_prepared_inventory: bool,
    max_rounds: int,
    root: Path | None = None,
) -> ZevrayaBattleOutcome:
    if structure_mode not in {"owner", "non_diluting"}:
        raise ValueError(f"unknown Zevraya structure mode: {structure_mode}")
    if strategy not in {"rush", "dismantle"}:
        raise ValueError(f"unknown Zevraya strategy: {strategy}")
    if structure_mode == "non_diluting" and not data.non_diluting_candidate_documented:
        raise ValueError("v104 non-diluting Zevraya structure is not documented in repository authority")

    data = _overlay_data(data, overlay, root=root)
    snapshot = load_zevraya_party_snapshot(player_level, root=root)
    actions = load_zevraya_party_actions(root=root)
    inventory = build_zevraya_prepared_inventory(root=root) if use_prepared_inventory else PreparedInventory({})

    party = [CombatUnit(template, index) for index, template in enumerate(snapshot.party)]
    boss = CombatUnit(data.blood_matron, 4)
    form: FormName = "blood_matron"
    base_boss_stats = boss.template.stats
    crimson = False
    form2_reached = False

    reservoirs = {name: _FiniteTargetState.from_source(source) for name, source in data.reservoirs.items()}
    inherited: dict[str, bool] = {}
    brood: _BroodState | None = None
    brood_deployments = 0
    brood_actions = 0

    locked_through: dict[str, int] = {}
    conduction_index = 0
    plating_expires_end_round: int | None = None
    reconstruction_used = False
    siphon_successes = 0

    any_ko = False
    bleed_exposed = False
    control_exposed = False
    hunter_measure_expires_end_round: int | None = None
    hunter_measure_establishments = 0
    measure_body: FormName | None = None

    sustenance_heal_uses = 0
    reconstruction_uses = 0
    conduction_uses = 0
    plating_uses = 0

    branch_locks = {
        "Crimson Arc": _branch_lock("Crimson Arc", root=root),
        "Sustenance Draw": _branch_lock("Sustenance Draw", root=root),
        "Perfected Siphon": _branch_lock("Perfected Siphon", root=root),
    }

    def hunter_measure_active() -> bool:
        return hunter_measure_expires_end_round is not None and measure_body == form

    def armor_functional() -> bool:
        if form == "blood_matron":
            return reservoirs["Armor"].alive
        return inherited.get("Armor", False)

    def refresh_boss_defense(round_number: int) -> None:
        nonlocal plating_expires_end_round
        if structure_mode == "non_diluting":
            _apply_defensive_branch(boss, base_boss_stats, armor_functional())
            return
        active = plating_expires_end_round is not None and round_number <= plating_expires_end_round
        _apply_defensive_branch(boss, base_boss_stats, active)

    def mark_kos() -> None:
        nonlocal any_ko
        for unit in party:
            if not unit.alive and not unit.ko_counted:
                unit.ko_counted = True
                any_ko = True

    def enter_crimson(round_number: int) -> None:
        nonlocal crimson, brood, brood_deployments, reconstruction_used, reconstruction_uses
        if crimson or form != "blood_matron" or not boss.alive:
            return
        if boss.hp / boss.max_hp > data.crimson_trigger_fraction:
            return
        crimson = True
        if reservoirs["Brood"].alive:
            brood = _BroodState.from_source(data.brood_organism)
            brood_deployments += 1
        if structure_mode == "non_diluting" and reservoirs["Sustenance"].alive and not reconstruction_used:
            # v104 explicitly converts this to a bounded conditional passive.
            # The working snapshot resolves the condition at Crimson entry so
            # no hidden HP threshold is introduced by the simulator.
            boss.hp = min(boss.max_hp, boss.hp + data.controlled_reconstruction.heal_amount)
            reconstruction_used = True
            reconstruction_uses += 1

    def enter_form2(round_number: int) -> None:
        nonlocal form, base_boss_stats, crimson, brood, form2_reached, conduction_index
        nonlocal plating_expires_end_round, hunter_measure_expires_end_round, measure_body
        if form != "blood_matron":
            return
        for name, state in reservoirs.items():
            inherited[name] = state.alive
        form = "perfected_war_mother"
        form2_reached = True
        crimson = False
        boss.template = data.perfected_war_mother
        boss.hp = boss.max_hp
        boss.mp = boss.max_mp
        boss.statuses.clear()
        boss.temporary_modifiers.clear()
        boss.tactical_states.clear()
        base_boss_stats = boss.template.stats
        plating_expires_end_round = None
        conduction_index = 0
        hunter_measure_expires_end_round = None
        measure_body = None
        brood = _BroodState.from_source(data.perfected_brood_organism) if inherited.get("Brood") else None
        if brood is not None:
            nonlocal brood_deployments
            brood_deployments += 1
        refresh_boss_defense(round_number)

    def check_body_transitions(round_number: int) -> bool:
        if boss.alive:
            enter_crimson(round_number)
            return False
        if form == "blood_matron":
            enter_form2(round_number)
            return False
        return True

    refresh_boss_defense(1)

    for round_number in range(1, max_rounds + 1):
        ilyra_direct_heal_used = False
        vaelira_elemental_used = False
        order = _round_order(party, boss, brood)

        for kind, actor_obj in order:
            if kind == "party":
                actor = actor_obj
                assert isinstance(actor, CombatUnit)
                if not actor.alive:
                    continue
                if turn_is_blocked(actor, rng):
                    complete_turn(actor, acted=False)
                    mark_kos()
                    continue

                item_decision = choose_prepared_item(actor, party, inventory, actions, root=root) if use_prepared_inventory else None
                if item_decision is not None:
                    use_consumable(inventory, item_decision.effect, target=item_decision.target)
                    complete_turn(actor, acted=True)
                    mark_kos()
                    continue

                if actor.template.name == "Ilyra":
                    ko = next((unit for unit in party if not unit.alive), None)
                    if ko is not None and actor.mp >= actions.revive_mp_cost:
                        actor.mp -= actions.revive_mp_cost
                        ko.hp = max(1, round_half_up(ko.max_hp * actions.revive_fraction))
                        complete_turn(actor, acted=True)
                        continue

                    control = controlled_ally(party)
                    if control is not None and actor.mp >= actions.clear_warding.mp_cost:
                        actor.mp -= actions.clear_warding.mp_cost
                        heal_action = _trait_adjusted_heal(
                            actions.clear_warding,
                            control,
                            first_direct_heal_this_round=not ilyra_direct_heal_used,
                            gentle_continuance_bonus=actions.gentle_continuance_bonus,
                        )
                        resolve_heal(actor, heal_action, control)
                        ilyra_direct_heal_used = True
                        complete_turn(actor, acted=True)
                        continue

                    wounded = [unit for unit in party if unit.alive and unit.hp / unit.max_hp < policy.renewal_two_allies_below_fraction]
                    if len(wounded) >= 2 and actor.mp >= actions.renewal.mp_cost:
                        actor.mp -= actions.renewal.mp_cost
                        for target in [unit for unit in party if unit.alive]:
                            heal_action = _trait_adjusted_heal(
                                actions.renewal,
                                target,
                                first_direct_heal_this_round=not ilyra_direct_heal_used,
                                gentle_continuance_bonus=actions.gentle_continuance_bonus,
                            )
                            resolve_heal(actor, heal_action, target)
                            ilyra_direct_heal_used = True
                        complete_turn(actor, acted=True)
                        continue

                    low = lowest_hp_ally(party)
                    if low is not None and low.hp / low.max_hp < policy.mend_below_hp_fraction and actor.mp >= actions.mend.mp_cost:
                        actor.mp -= actions.mend.mp_cost
                        heal_action = _trait_adjusted_heal(
                            actions.mend,
                            low,
                            first_direct_heal_this_round=not ilyra_direct_heal_used,
                            gentle_continuance_bonus=actions.gentle_continuance_bonus,
                        )
                        resolve_heal(actor, heal_action, low)
                        ilyra_direct_heal_used = True
                        complete_turn(actor, acted=True)
                        continue

                finite_target = _support_target_for_strategy(strategy, reservoirs, brood, party) if form == "blood_matron" else (
                    brood if brood is not None and brood.alive and strategy == "dismantle" else None
                )

                if finite_target is not None:
                    action = _support_action_for(actor, actions, hunter_measure_active())
                    if action.mp_cost and actor.mp >= action.mp_cost:
                        actor.mp -= action.mp_cost
                    elif action.mp_cost:
                        action = actions.basic_attack
                    _resolve_player_damage_finite(actor, action, finite_target, rng)
                    if isinstance(finite_target, _FiniteTargetState) and not finite_target.alive:
                        refresh_boss_defense(round_number)
                    complete_turn(actor, acted=True)
                    mark_kos()
                    continue

                multiple_hostiles = brood is not None and brood.alive
                action, cost = _boss_offense_for(
                    actor,
                    actions,
                    hunter_measure_active=hunter_measure_active(),
                    multiple_hostiles=multiple_hostiles,
                    vaelira_discount_available=(actor.template.name == "Vaelira" and not vaelira_elemental_used),
                )
                if cost and actor.mp < cost:
                    action = actions.basic_attack
                    cost = 0
                actor.mp -= cost
                if actor.template.name == "Vaelira" and action.name in {"Prism Lance", "Spectrum Cascade"}:
                    vaelira_elemental_used = True

                if action.target_scope == "all" and multiple_hostiles:
                    resolve_damage(actor, action, boss, rng)
                    if brood is not None and brood.alive:
                        # Spectrum Cascade is elemental; the Brood owner has no
                        # explicit affinity table. Avoid inventing one by not
                        # applying the secondary hit to the Brood in this first
                        # source-strict certification policy.
                        pass
                else:
                    damage = resolve_damage(actor, action, boss, rng)
                    if actor.template.name == "Torren" and action.name == actions.sizing_shot.name and damage > 0:
                        hunter_measure_expires_end_round = round_number + actions.hunter_measure_full_rounds
                        measure_body = form
                        hunter_measure_establishments += 1

                complete_turn(actor, acted=True)
                mark_kos()
                if check_body_transitions(round_number):
                    return ZevrayaBattleOutcome(
                        "party", round_number, any_ko,
                        _party_fraction(party, "hp", "max_hp"),
                        _party_fraction(party, "mp", "max_mp"),
                        form2_reached,
                        sum(not state.alive for state in reservoirs.values()),
                        brood_deployments, brood_actions, inventory.total_used,
                        hunter_measure_establishments, sustenance_heal_uses,
                        reconstruction_uses, conduction_uses, plating_uses,
                        bleed_exposed, control_exposed,
                    )

            elif kind == "boss":
                if not boss.alive:
                    continue
                if form == "blood_matron":
                    core = list(data.form1_core_actions)
                    if crimson:
                        core = [data.crimson_arc if action.name == "Surgical Sweep" else action for action in core]
                    locks = dict(data.form1_locks)
                    locks["Crimson Arc"] = branch_locks["Crimson Arc"]
                else:
                    core = list(data.form2_core_actions)
                    locks = dict(data.form2_locks)

                legal: list[tuple[str, object, int]] = []
                for action in core:
                    duration = locks.get(action.name, 0)
                    if not _action_locked(action.name, round_number, locked_through):
                        legal.append(("damage", action, duration))

                if form == "blood_matron":
                    if reservoirs["Sustenance"].alive and not _action_locked("Sustenance Draw", round_number, locked_through):
                        legal.append(("healing_damage", data.sustenance_draw, branch_locks["Sustenance Draw"]))
                    if reservoirs["Conduction"].alive and not _action_locked("Weather Conduction", round_number, locked_through):
                        legal.append(("conduction", data.weather_conduction, data.weather_conduction.repetition_lock_rounds))
                    if structure_mode == "owner" and reservoirs["Armor"].alive and not _action_locked("Adaptive Plating", round_number, locked_through):
                        legal.append(("plating", data.armor_plating, data.armor_plating.repetition_lock_rounds))
                    if structure_mode == "owner" and crimson and reservoirs["Sustenance"].alive and not reconstruction_used:
                        legal.append(("reconstruction", data.controlled_reconstruction, 0))
                else:
                    if inherited.get("Sustenance") and siphon_successes < (data.perfected_siphon.successful_use_cap or 0) and not _action_locked("Perfected Siphon", round_number, locked_through):
                        legal.append(("healing_damage", data.perfected_siphon, branch_locks["Perfected Siphon"]))
                    if inherited.get("Conduction") and not _action_locked("Perfected Conduction", round_number, locked_through):
                        legal.append(("conduction", data.perfected_conduction, data.perfected_conduction.repetition_lock_rounds))
                    if structure_mode == "owner" and inherited.get("Armor") and not _action_locked("Warbody Plating", round_number, locked_through):
                        legal.append(("plating", data.warbody_plating, data.warbody_plating.repetition_lock_rounds))

                if not legal:
                    raise RuntimeError("Zevraya has no legal selected action under current locks")
                action_type, payload, duration = rng.choice(legal)

                if action_type == "damage":
                    action = payload
                    assert isinstance(action, CombatAction)
                    _, new_bleed, new_control = _resolve_enemy_damage(boss, action, party, rng)
                    bleed_exposed = bleed_exposed or new_bleed
                    control_exposed = control_exposed or new_control
                    _set_lock(action.name, duration, round_number, locked_through)
                elif action_type == "healing_damage":
                    rule = payload
                    action = rule.action
                    total, new_bleed, new_control = _resolve_enemy_damage(boss, action, party, rng)
                    if total > 0:
                        boss.hp = min(boss.max_hp, boss.hp + round_half_up(total * rule.heal_from_actual_damage_fraction))
                        sustenance_heal_uses += 1
                        if form == "perfected_war_mother":
                            siphon_successes += 1
                    bleed_exposed = bleed_exposed or new_bleed
                    control_exposed = control_exposed or new_control
                    _set_lock(action.name, duration, round_number, locked_through)
                elif action_type == "conduction":
                    rule = payload
                    assert isinstance(rule, ConductionRule)
                    action = _conduction_action(rule, conduction_index)
                    conduction_index = (conduction_index + 1) % len(rule.cycle)
                    _, new_bleed, new_control = _resolve_enemy_damage(boss, action, party, rng)
                    bleed_exposed = bleed_exposed or new_bleed
                    control_exposed = control_exposed or new_control
                    conduction_uses += 1
                    _set_lock(rule.name, duration, round_number, locked_through)
                elif action_type == "plating":
                    plating_expires_end_round = round_number + 1
                    plating_uses += 1
                    refresh_boss_defense(round_number)
                    name = "Adaptive Plating" if form == "blood_matron" else "Warbody Plating"
                    _set_lock(name, duration, round_number, locked_through)
                else:
                    boss.hp = min(boss.max_hp, boss.hp + data.controlled_reconstruction.heal_amount)
                    reconstruction_used = True
                    reconstruction_uses += 1

                complete_turn(boss, acted=True)
                mark_kos()
                if check_body_transitions(round_number):
                    return ZevrayaBattleOutcome(
                        "party", round_number, any_ko,
                        _party_fraction(party, "hp", "max_hp"),
                        _party_fraction(party, "mp", "max_mp"),
                        form2_reached,
                        sum(not state.alive for state in reservoirs.values()),
                        brood_deployments, brood_actions, inventory.total_used,
                        hunter_measure_establishments, sustenance_heal_uses,
                        reconstruction_uses, conduction_uses, plating_uses,
                        bleed_exposed, control_exposed,
                    )

            else:
                brood_state = actor_obj
                assert isinstance(brood_state, _BroodState)
                if not brood_state.alive or not any(unit.alive for unit in party):
                    continue
                new_bleed, new_control = _resolve_brood_damage(brood_state, party, rng)
                brood_actions += 1
                bleed_exposed = bleed_exposed or new_bleed
                control_exposed = control_exposed or new_control
                mark_kos()

            if not any(unit.alive for unit in party):
                return ZevrayaBattleOutcome(
                    "enemy", round_number, True, 0.0,
                    _party_fraction(party, "mp", "max_mp"),
                    form2_reached,
                    sum(not state.alive for state in reservoirs.values()),
                    brood_deployments, brood_actions, inventory.total_used,
                    hunter_measure_establishments, sustenance_heal_uses,
                    reconstruction_uses, conduction_uses, plating_uses,
                    bleed_exposed, control_exposed,
                )

        end_round([*party, boss])
        mark_kos()
        if check_body_transitions(round_number):
            return ZevrayaBattleOutcome(
                "party", round_number, any_ko,
                _party_fraction(party, "hp", "max_hp"),
                _party_fraction(party, "mp", "max_mp"),
                form2_reached,
                sum(not state.alive for state in reservoirs.values()),
                brood_deployments, brood_actions, inventory.total_used,
                hunter_measure_establishments, sustenance_heal_uses,
                reconstruction_uses, conduction_uses, plating_uses,
                bleed_exposed, control_exposed,
            )
        if not any(unit.alive for unit in party):
            return ZevrayaBattleOutcome(
                "enemy", round_number, True, 0.0,
                _party_fraction(party, "mp", "max_mp"),
                form2_reached,
                sum(not state.alive for state in reservoirs.values()),
                brood_deployments, brood_actions, inventory.total_used,
                hunter_measure_establishments, sustenance_heal_uses,
                reconstruction_uses, conduction_uses, plating_uses,
                bleed_exposed, control_exposed,
            )

        if structure_mode == "owner" and plating_expires_end_round is not None and round_number >= plating_expires_end_round:
            plating_expires_end_round = None
            refresh_boss_defense(round_number + 1)
        elif structure_mode == "non_diluting":
            refresh_boss_defense(round_number + 1)

        if hunter_measure_expires_end_round is not None and round_number >= hunter_measure_expires_end_round:
            hunter_measure_expires_end_round = None
            measure_body = None

    return ZevrayaBattleOutcome(
        "draw", max_rounds, any_ko,
        _party_fraction(party, "hp", "max_hp"),
        _party_fraction(party, "mp", "max_mp"),
        form2_reached,
        sum(not state.alive for state in reservoirs.values()),
        brood_deployments, brood_actions, inventory.total_used,
        hunter_measure_establishments, sustenance_heal_uses,
        reconstruction_uses, conduction_uses, plating_uses,
        bleed_exposed, control_exposed,
    )


def run_matron_zevraya(
    rng: random.Random,
    *,
    player_level: int = 24,
    structure_mode: StructureMode = "owner",
    strategy: Strategy = "rush",
    overlay: BalanceOverlay = BalanceOverlay(),
    policy: ZevrayaPolicyConfig = ZevrayaPolicyConfig(),
    use_prepared_inventory: bool = True,
    max_rounds: int = 40,
    root: Path | None = None,
) -> ZevrayaBattleOutcome:
    return _run_zevraya_with_data(
        rng,
        load_zevraya_repo_data(root=root),
        player_level=player_level,
        structure_mode=structure_mode,
        strategy=strategy,
        overlay=overlay,
        policy=policy,
        use_prepared_inventory=use_prepared_inventory,
        max_rounds=max_rounds,
        root=root,
    )


def simulate_matron_zevraya(
    *,
    player_level: int = 24,
    structure_mode: StructureMode = "owner",
    strategy: Strategy = "rush",
    overlay: BalanceOverlay = BalanceOverlay(),
    policy: ZevrayaPolicyConfig = ZevrayaPolicyConfig(),
    use_prepared_inventory: bool = True,
    runs: int = 1_000,
    seed: int = 104,
    root: Path | None = None,
) -> ZevrayaSimulationSummary:
    if runs < 1:
        raise ValueError("runs must be positive")
    data = load_zevraya_repo_data(root=root)
    outcomes = [
        _run_zevraya_with_data(
            random.Random(seed + index),
            data,
            player_level=player_level,
            structure_mode=structure_mode,
            strategy=strategy,
            overlay=overlay,
            policy=policy,
            use_prepared_inventory=use_prepared_inventory,
            max_rounds=40,
            root=root,
        )
        for index in range(runs)
    ]
    rounds = [outcome.rounds for outcome in outcomes]
    return ZevrayaSimulationSummary(
        runs=runs,
        player_level=player_level,
        structure_mode=structure_mode,
        strategy=strategy,
        prepared_inventory=use_prepared_inventory,
        power_multiplier=overlay.direct_damage_power_multiplier,
        effective_stat_level_offset=overlay.effective_stat_level_offset,
        win_rate=sum(outcome.winner == "party" for outcome in outcomes) / runs,
        wipe_rate=sum(outcome.winner == "enemy" for outcome in outcomes) / runs,
        any_ko_rate=sum(outcome.any_party_ko for outcome in outcomes) / runs,
        mean_rounds=statistics.fmean(rounds),
        median_rounds=float(statistics.median(rounds)),
        p10_rounds=_percentile(rounds, 0.10),
        p90_rounds=_percentile(rounds, 0.90),
        mean_remaining_party_hp=statistics.fmean(outcome.party_hp_fraction for outcome in outcomes),
        mean_remaining_party_mp=statistics.fmean(outcome.party_mp_fraction for outcome in outcomes),
        form2_reach_rate=sum(outcome.form2_reached for outcome in outcomes) / runs,
        mean_reservoirs_destroyed=statistics.fmean(outcome.reservoirs_destroyed for outcome in outcomes),
        mean_brood_deployments=statistics.fmean(outcome.brood_deployments for outcome in outcomes),
        mean_brood_actions=statistics.fmean(outcome.brood_actions for outcome in outcomes),
        mean_items_used=statistics.fmean(outcome.items_used for outcome in outcomes),
        mean_hunter_measure_establishments=statistics.fmean(outcome.hunter_measure_establishments for outcome in outcomes),
        mean_sustenance_heal_uses=statistics.fmean(outcome.sustenance_heal_uses for outcome in outcomes),
        mean_reconstruction_uses=statistics.fmean(outcome.reconstruction_uses for outcome in outcomes),
        mean_conduction_uses=statistics.fmean(outcome.conduction_uses for outcome in outcomes),
        mean_plating_uses=statistics.fmean(outcome.plating_uses for outcome in outcomes),
        bleed_exposure_rate=sum(outcome.bleed_exposed for outcome in outcomes) / runs,
        control_exposure_rate=sum(outcome.control_exposed for outcome in outcomes) / runs,
    )


__all__ = [
    "Strategy",
    "StructureMode",
    "ZevrayaBattleOutcome",
    "ZevrayaSimulationSummary",
    "run_matron_zevraya",
    "simulate_matron_zevraya",
]
