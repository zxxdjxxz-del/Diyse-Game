"""Parse Matron Zevraya's current two-form encounter from repository authority."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from tools.diysim.combat.models import CombatAction, Combatant, StatusRider
from tools.diysim.progression import Stats
from tools.diysim.sources import (
    SourceGapError,
    extract_heading_block,
    extract_markdown_table,
    parse_authored_action_text,
    read_repo_text,
)
from tools.diysim.sources.markdown import parse_int

OWNER_PATH = "docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/MATRON_ZEVRAYA.md"
SENSITIVITY_PATH = "docs/16_BALANCE_AND_TESTING/CH6_ENEMY_POWER_20_PERCENT_SENSITIVITY_v104.md"


@dataclass(frozen=True)
class FiniteTargetSource:
    name: str
    hp: int
    defense: int
    spirit: int
    evasion: int
    status_resistance: int


@dataclass(frozen=True)
class PhysicalSupportActorSource:
    name: str
    hp: int
    attack: int
    defense: int
    spirit: int
    speed: int
    evasion: int
    status_resistance: int
    action: CombatAction


@dataclass(frozen=True)
class HealingDamageActionRule:
    action: CombatAction
    heal_from_actual_damage_fraction: float
    successful_use_cap: int | None = None


@dataclass(frozen=True)
class PlatingRule:
    defense_bonus: float
    spirit_bonus: float
    duration_rounds: int
    repetition_lock_rounds: int


@dataclass(frozen=True)
class ReconstructionRule:
    heal_amount: int
    successful_use_cap: int


@dataclass(frozen=True)
class ConductionRule:
    name: str
    power: int
    base_hit: int
    cycle: tuple[str, ...]
    stun_chance: int
    freeze_chance: int
    repetition_lock_rounds: int


@dataclass(frozen=True)
class ZevrayaRepoData:
    blood_matron: Combatant
    perfected_war_mother: Combatant
    form1_core_actions: tuple[CombatAction, ...]
    crimson_arc: CombatAction
    form2_core_actions: tuple[CombatAction, ...]
    form1_locks: dict[str, int]
    form2_locks: dict[str, int]
    reservoirs: dict[str, FiniteTargetSource]
    sustenance_draw: HealingDamageActionRule
    perfected_siphon: HealingDamageActionRule
    armor_plating: PlatingRule
    warbody_plating: PlatingRule
    controlled_reconstruction: ReconstructionRule
    weather_conduction: ConductionRule
    perfected_conduction: ConductionRule
    brood_organism: PhysicalSupportActorSource
    perfected_brood_organism: PhysicalSupportActorSource
    crimson_trigger_fraction: float
    non_diluting_candidate_documented: bool


def _full_stats(row: dict[str, str]) -> Stats:
    required = ("HP", "ATK", "MAG", "DEF", "Spirit", "SPD")
    missing = [column for column in required if column not in row]
    if missing:
        raise SourceGapError(f"{OWNER_PATH} full combat body missing columns: {', '.join(missing)}")
    return Stats(
        hp=parse_int(row["HP"]),
        mp=parse_int(row["MP"]) if "MP" in row else 0,
        attack=parse_int(row["ATK"]),
        magic=parse_int(row["MAG"]),
        defense=parse_int(row["DEF"]),
        spirit=parse_int(row["Spirit"]),
        speed=parse_int(row["SPD"]),
    )


def _boss_from_form(text: str, heading: str, name: str) -> Combatant:
    block = extract_heading_block(text, heading)
    row = extract_markdown_table(block, "Raw line")[0]
    return Combatant(
        name=name,
        side="enemy",
        stats=_full_stats(row),
        evasion=parse_int(row["EVA"]),
        status_resistance=parse_int(row["SR"]),
        rank="major_boss",
    )


def _fixed_action(text: str, name: str) -> CombatAction:
    block = extract_heading_block(text, name)
    source = parse_authored_action_text(name, block)
    missing = source.missing("target_scope", "damage_kind", "power", "base_hit")
    if missing or source.element_mode != "fixed" or source.element is None:
        detail = ", ".join(missing) if missing else "fixed element"
        raise SourceGapError(f"{OWNER_PATH} has incomplete {name} authority: {detail}")
    return CombatAction(
        name=name,
        target_scope=source.target_scope,  # type: ignore[arg-type]
        damage_kind=source.damage_kind,  # type: ignore[arg-type]
        element=source.element,  # type: ignore[arg-type]
        power=source.power,
        base_hit=source.base_hit,
        physical_weight=source.physical_weight,
        magical_weight=source.magical_weight,
        status_riders=tuple(StatusRider(status, chance) for status, chance in source.status_chances),
    )


def _lock(text: str, name: str) -> int:
    block = extract_heading_block(text, name)
    match = re.search(r"(\d+)-round repetition lock", block, re.I)
    if not match:
        raise SourceGapError(f"{OWNER_PATH} lacks {name} repetition lock")
    return int(match.group(1))


def _healing_damage_rule(text: str, name: str, *, cap: int | None = None) -> HealingDamageActionRule:
    block = extract_heading_block(text, name)
    heal = re.search(r"restores HP equal to \*\*(\d+)% of actual direct damage dealt\*\*", block, re.I)
    if not heal:
        raise SourceGapError(f"{OWNER_PATH} lacks {name} damage-to-heal fraction")
    if cap is None:
        cap_match = re.search(r"\*\*(\d+) successful uses?", block, re.I)
        cap = int(cap_match.group(1)) if cap_match else None
    return HealingDamageActionRule(
        action=_fixed_action(text, name),
        heal_from_actual_damage_fraction=int(heal.group(1)) / 100.0,
        successful_use_cap=cap,
    )


def _plating(text: str, heading: str) -> PlatingRule:
    block = extract_heading_block(text, heading)
    bonus = re.search(r"Defense \+(\d+)% / Spirit \+(\d+)% through the end of the following round", block, re.I)
    if not bonus:
        raise SourceGapError(f"{OWNER_PATH} lacks exact {heading} bonuses")
    return PlatingRule(
        defense_bonus=int(bonus.group(1)) / 100.0,
        spirit_bonus=int(bonus.group(2)) / 100.0,
        duration_rounds=1,
        repetition_lock_rounds=_lock(text, heading),
    )


def _conduction(text: str, heading: str) -> ConductionRule:
    block = extract_heading_block(text, heading)
    power = re.search(r"\*\*(\d+) Power\*\*", block)
    hit = re.search(r"Base Hit \*\*(\d+)\*\*", block, re.I)
    cycle = re.search(
        r"(?:visible cycle:\s*)?(?:\*\*)?Gale\s*→\s*Storm\s*→\s*Frost(?:\s*→\s*repeat)?(?:\*\*)?",
        block,
        re.I,
    )
    stun = re.search(r"Storm:[\s\S]*?\*\*(\d+)% Stun\*\*", block, re.I)
    freeze = re.search(r"Frost:[\s\S]*?\*\*(\d+)% Freeze\*\*", block, re.I)
    if not (power and hit and cycle and stun and freeze):
        raise SourceGapError(f"{OWNER_PATH} lacks complete {heading} cycle authority")
    return ConductionRule(
        name=heading,
        power=int(power.group(1)),
        base_hit=int(hit.group(1)),
        cycle=("gale", "storm", "frost"),
        stun_chance=int(stun.group(1)),
        freeze_chance=int(freeze.group(1)),
        repetition_lock_rounds=_lock(text, heading),
    )


def _finite_targets(text: str) -> dict[str, FiniteTargetSource]:
    rows = extract_markdown_table(text, "LIFE-FORCE RESERVOIRS")
    result: dict[str, FiniteTargetSource] = {}
    for row in rows:
        name = row["Reservoir"].strip()
        result[name] = FiniteTargetSource(
            name=name,
            hp=parse_int(row["HP"]),
            defense=parse_int(row["DEF"]),
            spirit=parse_int(row["Spirit"]),
            evasion=parse_int(row["EVA"]),
            status_resistance=parse_int(row["SR"]),
        )
    expected = {"Sustenance", "Armor", "Brood", "Conduction"}
    if set(result) != expected:
        raise SourceGapError(f"{OWNER_PATH} expected Reservoirs {sorted(expected)}, found {sorted(result)}")
    return result


def _support_actor(
    text: str,
    source_heading: str,
    action_name: str,
    *,
    display_name: str | None = None,
) -> PhysicalSupportActorSource:
    block = extract_heading_block(text, source_heading)
    values: dict[str, int] = {}
    for label in ("HP", "ATK", "DEF", "Spirit", "SPD", "EVA", "SR"):
        match = re.search(rf"^- {re.escape(label)}\s+\*\*(\d+)\*\*|^- {re.escape(label)}(\d+)$", block, re.I | re.M)
        if match:
            values[label] = int(match.group(1) or match.group(2))
    for label in ("EVA", "SR"):
        if label not in values:
            match = re.search(rf"^- {label}(\d+)$", block, re.I | re.M)
            if match:
                values[label] = int(match.group(1))
    missing = [label for label in ("HP", "ATK", "DEF", "Spirit", "SPD", "EVA", "SR") if label not in values]
    if missing:
        raise SourceGapError(f"{OWNER_PATH} {source_heading} missing: {', '.join(missing)}")
    return PhysicalSupportActorSource(
        name=display_name or source_heading,
        hp=values["HP"],
        attack=values["ATK"],
        defense=values["DEF"],
        spirit=values["Spirit"],
        speed=values["SPD"],
        evasion=values["EVA"],
        status_resistance=values["SR"],
        action=_fixed_action(text, action_name),
    )


def load_zevraya_repo_data(*, root: Path | None = None) -> ZevrayaRepoData:
    text = read_repo_text(OWNER_PATH, root=root)
    sensitivity = read_repo_text(SENSITIVITY_PATH, root=root)

    form1 = _boss_from_form(text, "FORM I — BLOOD MATRON", "Matron Zevraya — Blood Matron")
    form2 = _boss_from_form(text, "FORM II — PERFECTED WAR MOTHER", "Matron Zevraya — Perfected War Mother")

    form1_core_names = ("Ritual Incision", "Alteration Lance", "Surgical Sweep", "Ruin Infusion")
    form2_core_names = ("Perfected Tearing Blade", "Ruin Scythe", "Warbody Crush", "Perfected Ruin Wave")
    form1_core = tuple(_fixed_action(text, name) for name in form1_core_names)
    form2_core = tuple(_fixed_action(text, name) for name in form2_core_names)

    trigger = re.search(r"CRIMSON BROOD[\s\S]*?Begins at:\s*>\s*\*\*(\d+)% Form-I HP\*\*", text, re.I)
    reconstruction = re.search(r"Controlled Reconstruction[\s\S]*?restore \*\*(\d+) HP\*\*[\s\S]*?\*\*(\d+) successful use", text, re.I)
    if not (trigger and reconstruction):
        raise SourceGapError(f"{OWNER_PATH} lacks Crimson Brood trigger/reconstruction authority")

    documented_candidate = all(
        phrase in sensitivity
        for phrase in (
            "continuous functional **Defense +15% / Spirit +15%**",
            "bounded conditional passive trigger",
            "does not replace a selected attack",
        )
    )

    return ZevrayaRepoData(
        blood_matron=form1,
        perfected_war_mother=form2,
        form1_core_actions=form1_core,
        crimson_arc=_fixed_action(text, "Crimson Arc"),
        form2_core_actions=form2_core,
        form1_locks={name: _lock(text, name) for name in form1_core_names},
        form2_locks={name: _lock(text, name) for name in form2_core_names},
        reservoirs=_finite_targets(text),
        sustenance_draw=_healing_damage_rule(text, "Sustenance Draw"),
        perfected_siphon=_healing_damage_rule(text, "Perfected Siphon"),
        armor_plating=_plating(text, "Adaptive Plating"),
        warbody_plating=_plating(text, "Warbody Plating"),
        controlled_reconstruction=ReconstructionRule(
            heal_amount=int(reconstruction.group(1)),
            successful_use_cap=int(reconstruction.group(2)),
        ),
        weather_conduction=_conduction(text, "Weather Conduction"),
        perfected_conduction=_conduction(text, "Perfected Conduction"),
        brood_organism=_support_actor(text, "Crimson Brood Organism", "Brood Rend"),
        perfected_brood_organism=_support_actor(
            text,
            "Brood survived",
            "Perfected Brood Rend",
            display_name="Perfected Brood Organism",
        ),
        crimson_trigger_fraction=int(trigger.group(1)) / 100.0,
        non_diluting_candidate_documented=documented_candidate,
    )


__all__ = [
    "ConductionRule",
    "FiniteTargetSource",
    "HealingDamageActionRule",
    "OWNER_PATH",
    "PhysicalSupportActorSource",
    "PlatingRule",
    "ReconstructionRule",
    "SENSITIVITY_PATH",
    "ZevrayaRepoData",
    "load_zevraya_repo_data",
]
