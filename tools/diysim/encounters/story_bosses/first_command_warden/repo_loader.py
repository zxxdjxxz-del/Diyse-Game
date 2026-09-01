"""Parse the current First Command Warden owner package from repository authority."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from tools.diysim.combat.models import CombatAction, Combatant, StatusRider
from tools.diysim.progression import Stats
from tools.diysim.sources import (
    FunctionalAnalogueRuleSource,
    SourceGapError,
    extract_heading_block,
    extract_markdown_table,
    parse_authored_action_text,
    parse_functional_analogue_rule_text,
    read_repo_text,
)
from tools.diysim.sources.markdown import parse_int

OWNER_PATH = "docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/FIRST_COMMAND_WARDEN.md"


@dataclass(frozen=True)
class CommandSealRule:
    duration_rounds: int
    repetition_lock_rounds: int
    categories: tuple[str, ...]
    reprisal: CombatAction


@dataclass(frozen=True)
class MajorRulingRule:
    preparation_rounds: int
    repetition_lock_rounds: int
    ring_realign_rounds: int
    action: CombatAction


@dataclass(frozen=True)
class StateBProtectionRule:
    disrupted_reduction: float
    disrupted_rounds: int
    undisrupted_reduction: float
    undisrupted_rounds: int


@dataclass(frozen=True)
class FirstCommandWardenRepoData:
    displayed_level: int
    warden: Combatant
    command_ring: Combatant
    state_a_actions: tuple[CombatAction, ...]
    state_b_actions: tuple[CombatAction, ...]
    repetition_locks: dict[str, int]
    command_seal: CommandSealRule
    major_ruling: MajorRulingRule
    recorded_analogue: FunctionalAnalogueRuleSource
    state_b_trigger_fraction: float
    state_b_protection: StateBProtectionRule


def _stats_from_row(row: dict[str, str]) -> Stats:
    return Stats(
        hp=parse_int(row["HP"]),
        mp=parse_int(row["MP"]) if "MP" in row else 0,
        attack=parse_int(row["ATK"]) if "ATK" in row else 0,
        magic=parse_int(row["MAG"]) if "MAG" in row else 0,
        defense=parse_int(row["DEF"]) if "DEF" in row else 0,
        spirit=parse_int(row["Spirit"]) if "Spirit" in row else 0,
        speed=parse_int(row["SPD"]) if "SPD" in row else 0,
    )


def _damage_action(text: str, name: str) -> CombatAction:
    block = extract_heading_block(text, name)
    source = parse_authored_action_text(name, block)
    missing = source.missing("target_scope", "damage_kind", "power", "base_hit")
    if missing or source.element_mode != "fixed" or source.element is None:
        detail = ", ".join(missing) if missing else "fixed element"
        raise SourceGapError(f"{OWNER_PATH} has incomplete {name} action authority: {detail}")

    riders = tuple(StatusRider(status, chance) for status, chance in source.status_chances)
    return CombatAction(
        name=name,
        target_scope=source.target_scope,  # type: ignore[arg-type]
        damage_kind=source.damage_kind,  # type: ignore[arg-type]
        element=source.element,  # type: ignore[arg-type]
        power=source.power,
        base_hit=source.base_hit,
        physical_weight=source.physical_weight,
        magical_weight=source.magical_weight,
        status_riders=riders,
    )


def _lock_rounds(text: str, action_name: str) -> int | None:
    patterns = (
        rf"{re.escape(action_name)}[^\n]*?(\d+)-round repetition lock",
        rf"{re.escape(action_name)}[^\n]*?has a (\d+)-round repetition lock",
    )
    for pattern in patterns:
        match = re.search(pattern, text, re.I)
        if match:
            return int(match.group(1))
    block = extract_heading_block(text, action_name)
    match = re.search(r"(\d+)-round repetition lock", block, re.I)
    return int(match.group(1)) if match else None


def _command_seal(text: str) -> CommandSealRule:
    block = extract_heading_block(text, "Command Seal")
    duration = re.search(r"Duration:\s*>\s*\*\*(\d+) rounds\*\*", block, re.I | re.S)
    lock = re.search(r"Command Seal itself has a (\d+)-round repetition lock", block, re.I)
    if not (duration and lock):
        raise SourceGapError(f"{OWNER_PATH} lacks exact Command Seal duration/lock")

    categories_match = re.search(
        r"ordinary command category:\s*(?P<body>(?:\n- [^\n]+)+)",
        block,
        re.I,
    )
    if not categories_match:
        raise SourceGapError(f"{OWNER_PATH} lacks Command Seal category list")
    categories = tuple(
        line.removeprefix("- ").strip()
        for line in categories_match.group("body").strip().splitlines()
    )
    return CommandSealRule(
        duration_rounds=int(duration.group(1)),
        repetition_lock_rounds=int(lock.group(1)),
        categories=categories,
        reprisal=_damage_action(text, "Seal Reprisal"),
    )


def _major_ruling(text: str) -> MajorRulingRule:
    ring_block = extract_heading_block(text, "Command Ring")
    ruling_block = extract_heading_block(text, "Major Ruling")
    preparation = re.search(r"Preparation:\s*>\s*\*\*(\d+) full round", ruling_block, re.I | re.S)
    lock = re.search(r"(\d+)-round repetition lock after resolution", ruling_block, re.I)
    realign = re.search(r"may align again after \*\*(\d+) full rounds\*\*", ring_block, re.I)
    if not (preparation and lock and realign):
        raise SourceGapError(f"{OWNER_PATH} lacks exact Major Ruling preparation/lock/realign timing")
    return MajorRulingRule(
        preparation_rounds=int(preparation.group(1)),
        repetition_lock_rounds=int(lock.group(1)),
        ring_realign_rounds=int(realign.group(1)),
        action=_damage_action(text, "Major Ruling"),
    )


def _state_b_protection(text: str) -> StateBProtectionRule:
    block = extract_heading_block(text, "Earlier Ring handling → opening protection")
    disrupted = re.search(
        r"disrupted at least one Major Ruling[\s\S]*?\*\*(\d+)% direct-damage reduction for (\d+) round",
        block,
        re.I,
    )
    undisrupted = re.search(
        r"disrupted no Major Rulings[\s\S]*?\*\*(\d+)% direct-damage reduction for (\d+) rounds?",
        block,
        re.I,
    )
    if not (disrupted and undisrupted):
        raise SourceGapError(f"{OWNER_PATH} lacks State-B opening-protection values")
    return StateBProtectionRule(
        disrupted_reduction=int(disrupted.group(1)) / 100.0,
        disrupted_rounds=int(disrupted.group(2)),
        undisrupted_reduction=int(undisrupted.group(1)) / 100.0,
        undisrupted_rounds=int(undisrupted.group(2)),
    )


def load_first_command_warden_repo_data(*, root: Path | None = None) -> FirstCommandWardenRepoData:
    text = read_repo_text(OWNER_PATH, root=root)

    warden_row = extract_markdown_table(text, "Current raw line")[0]
    displayed_level = parse_int(warden_row["Lv"])
    warden = Combatant(
        name="First Command Warden",
        side="enemy",
        stats=_stats_from_row(warden_row),
        evasion=parse_int(warden_row["EVA"]),
        status_resistance=parse_int(warden_row["SR"]),
        rank="major_boss",
    )

    ring_row = extract_markdown_table(text, "### Command Ring")[0]
    command_ring = Combatant(
        name="Command Ring",
        side="enemy",
        stats=_stats_from_row(ring_row),
        evasion=parse_int(ring_row["EVA"]),
        status_resistance=parse_int(ring_row["SR"]),
    )

    state_a_actions = (
        _damage_action(text, "Authority Lance"),
        _damage_action(text, "Judgment Pulse"),
    )
    state_b_actions = (
        _damage_action(text, "Warden Crush"),
        _damage_action(text, "Challenged Verdict"),
        _damage_action(text, "Command Collapse"),
    )

    locks: dict[str, int] = {}
    for action_name in ("Judgment Pulse", "Challenged Verdict", "Command Collapse"):
        value = _lock_rounds(text, action_name)
        if value is not None:
            locks[action_name] = value

    command_seal = _command_seal(text)
    locks["Command Seal"] = command_seal.repetition_lock_rounds
    major_ruling = _major_ruling(text)
    locks["Major Ruling"] = major_ruling.repetition_lock_rounds

    analogue_block = extract_heading_block(text, "Recorded action system")
    analogue = parse_functional_analogue_rule_text(analogue_block)
    if not analogue.complete:
        raise SourceGapError(f"{OWNER_PATH} has incomplete Recorded Analogue authority")

    trigger = re.search(r"State B begins at \*\*(\d+)% HP\*\*", text, re.I)
    if not trigger:
        raise SourceGapError(f"{OWNER_PATH} lacks exact State-B trigger")

    return FirstCommandWardenRepoData(
        displayed_level=displayed_level,
        warden=warden,
        command_ring=command_ring,
        state_a_actions=state_a_actions,
        state_b_actions=state_b_actions,
        repetition_locks=locks,
        command_seal=command_seal,
        major_ruling=major_ruling,
        recorded_analogue=analogue,
        state_b_trigger_fraction=int(trigger.group(1)) / 100.0,
        state_b_protection=_state_b_protection(text),
    )


__all__ = [
    "CommandSealRule",
    "FirstCommandWardenRepoData",
    "MajorRulingRule",
    "OWNER_PATH",
    "StateBProtectionRule",
    "load_first_command_warden_repo_data",
]
