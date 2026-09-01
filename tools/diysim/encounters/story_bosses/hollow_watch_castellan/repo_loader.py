"""Build Hollow Watch simulation inputs from authoritative repo files.

No Diyse numeric canon is stored here. Encounter-specific parsing is limited to
Hollow Watch itself; class Abilities, Traits, and Maevra's recovered guest kit
are resolved through repository source files.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import re

from tools.diysim.combat.models import CombatAction, Combatant, StatusRider
from tools.diysim.progression import Stats
from tools.diysim.sources.abilities import AbilitySource, load_ability_source
from tools.diysim.sources.markdown import extract_markdown_table, parse_int
from tools.diysim.sources.repo import SourceGapError, read_repo_text
from tools.diysim.sources.traits import load_trait_source

BOSS_PATH = "docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/HOLLOW_WATCH_CASTELLAN.md"
TRUE_BATTLE_PATH = "docs/16_BALANCE_AND_TESTING/TRUE_BATTLES/HOLLOW_WATCH_CASTELLAN_TRUE_BATTLE_v93.md"
MAEVRA_COMBAT_PATH = "docs/16_BALANCE_AND_TESTING/BALANCE/MAEVRA_GUEST_COMBAT_REFERENCE.md"


@dataclass(frozen=True)
class HollowWatchRepoData:
    cyanis: Combatant
    ilyra: Combatant
    maevra: Combatant
    castellan: Combatant
    ballista: Combatant
    watch_seal: Combatant
    crest_strike: CombatAction
    resonant_pulse: CombatAction
    mend: CombatAction
    clear_warding: CombatAction
    linebreaker_thrust: CombatAction
    fortress_actions: tuple[CombatAction, ...]
    walking_actions: tuple[CombatAction, ...]
    heavy_bolt: CombatAction
    repetition_locked_actions: frozenset[str]
    walking_trigger_hp: int
    watch_seal_reduction: float
    harmonized_rank1_multiplier: float
    gentle_continuance_threshold: float
    gentle_continuance_bonus: float
    clear_warding_sr_bonus: int
    clear_warding_sr_rounds: int


def _stats_from_row(row: dict[str, str]) -> Stats:
    return Stats(
        parse_int(row["HP"]),
        parse_int(row["MP"]) if "MP" in row else 0,
        parse_int(row["ATK"]) if "ATK" in row else 0,
        parse_int(row["MAG"]) if "MAG" in row else 0,
        parse_int(row["DEF"]) if "DEF" in row else 0,
        parse_int(row["Spirit"]) if "Spirit" in row else 0,
        parse_int(row["SPD"]) if "SPD" in row else 0,
    )


def _party_from_true_battle(text: str) -> dict[str, Combatant]:
    rows = extract_markdown_table(text, "Exact Lv2 bodies")
    result: dict[str, Combatant] = {}
    for row in rows:
        name = row["Character"]
        result[name] = Combatant(
            name,
            "party",
            _stats_from_row(row),
            evasion=parse_int(row["EVA"]),
            status_resistance=parse_int(row["SR"]),
        )
    for required in ("Cyanis", "Ilyra", "Maevra"):
        if required not in result:
            raise SourceGapError(f"{TRUE_BATTLE_PATH} lacks {required} Lv2 body")
    return result


def _power(effect: str, ability: str) -> int:
    match = re.search(r"(?:\bPower\s*(?:\*\*)?(\d+)|\b(\d+)\s+Power\b)", effect, re.I)
    if not match:
        raise SourceGapError(f"Missing explicit Power for {ability}")
    return int(match.group(1) or match.group(2))


def _damage_type_and_element(text: str, label: str) -> tuple[str, str]:
    match = re.search(
        r"\b(Physical|Magical|Hybrid)\s*/\s*(Neutral|Colorless|Fire|Ice|Lightning|Earth|Ruin)\b",
        text,
        re.I,
    )
    if not match:
        raise SourceGapError(f"Missing damage type/element for {label}")
    return match.group(1).lower(), match.group(2).lower()


def _find_action_block(text: str, name: str) -> str:
    """Return a complete action block from current heading or legacy bold forms."""
    heading = re.search(
        rf"^(?P<marks>#{{2,6}})\s+(?:\*\*)?{re.escape(name)}(?:\*\*)?\s*$",
        text,
        re.I | re.M,
    )
    if heading:
        level = len(heading.group("marks"))
        later = re.search(rf"^#{{2,{level}}}\s+", text[heading.end():], re.M)
        end = heading.end() + later.start() if later else len(text)
        return text[heading.end():end].strip()

    patterns = (
        rf"\*\*{re.escape(name)}\*\*\s*\n(?P<body>(?:-\s*[^\n]+\n?)+)",
        rf"-\s*\*\*{re.escape(name)}\*\*\s*[—-]\s*(?P<body>[^\n]+)",
    )
    for pattern in patterns:
        match = re.search(pattern, text, re.I)
        if match:
            return match.group("body").strip()
    raise SourceGapError(f"Missing exact action block for {name}")


def _linebreaker_from_repo(maevra_text: str) -> CombatAction:
    rows = extract_markdown_table(maevra_text, "Current working ability kit")
    row = next((candidate for candidate in rows if candidate.get("Ability") == "Linebreaker Thrust"), None)
    if row is None:
        raise SourceGapError(f"{MAEVRA_COMBAT_PATH} lacks Linebreaker Thrust")

    effect = row.get("Effect", "")
    kind, element = _damage_type_and_element(effect, "Linebreaker Thrust")
    penetration = re.search(r"(\d+)%\s+Defense penetration", effect, re.I)
    if not penetration:
        raise SourceGapError("Linebreaker Thrust lacks exact Defense penetration")

    return CombatAction(
        "Linebreaker Thrust",
        mp_cost=parse_int(row["MP"]),
        damage_kind=kind,
        element=element,
        power=_power(effect, "Linebreaker Thrust"),
        defense_penetration=int(penetration.group(1)) / 100.0,
    )


def collect_hollow_watch_source_gaps(*, root: Path | None = None) -> tuple[str, ...]:
    """Return every currently detectable authority gap needed by this adapter."""
    boss_text = read_repo_text(BOSS_PATH, root=root)
    maevra_text = read_repo_text(MAEVRA_COMBAT_PATH, root=root)
    gaps: list[str] = []

    try:
        _linebreaker_from_repo(maevra_text)
    except SourceGapError as exc:
        gaps.append(str(exc))

    for action_name in ("Wallbound Strike", "Bastion Sweep", "Fortress Slam", "Iron Pursuit", "Wall-Shear Sweep"):
        try:
            block = _find_action_block(boss_text, action_name)
            _damage_type_and_element(block, action_name)
            _power(block, action_name)
            if not re.search(r"Base Hit\s*(?:\*\*)?(\d+)", block, re.I):
                raise SourceGapError(f"Missing Base Hit for {action_name}")
            if not re.search(r"(?:\*\*)?(\d+) weight(?:\*\*)?", block, re.I):
                raise SourceGapError(f"Missing selection weight for {action_name}")
        except SourceGapError as exc:
            gaps.append(str(exc))

    for heading in ("Fortress Ballista", "Watch Seal"):
        try:
            row = extract_markdown_table(boss_text, heading)[0]
            parse_int(row["EVA"])
            parse_int(row["SR"])
        except (IndexError, KeyError, ValueError) as exc:
            gaps.append(f"{heading}: incomplete EVA/SR target authority ({exc})")

    return tuple(gaps)


def _raise_preflight_gaps(*, root: Path | None = None) -> None:
    gaps = collect_hollow_watch_source_gaps(root=root)
    if gaps:
        formatted = "\n- ".join(gaps)
        raise SourceGapError(
            "Hollow Watch cannot be fully simulated from current repo authority yet:\n- " + formatted
        )


def _enemy_action(text: str, name: str) -> CombatAction:
    block = _find_action_block(text, name)
    hit = re.search(r"Base Hit\s*(?:\*\*)?(\d+)", block, re.I)
    weight = re.search(r"(?:\*\*)?(\d+) weight(?:\*\*)?", block, re.I)
    if not (hit and weight):
        raise SourceGapError(f"Incomplete action authority for {name}")
    kind, element = _damage_type_and_element(block, name)
    riders: list[StatusRider] = []
    for chance, status in re.findall(
        r"(?:\*\*)?(\d+)%\s+(?:base\s+)?(Burn|Freeze|Stun|Staggered|Bleed)(?:\*\*)?",
        block,
        re.I,
    ):
        riders.append(StatusRider(status.lower(), int(chance)))
    return CombatAction(
        name,
        target_scope="all" if re.search(r"all conscious", block, re.I) else "one",
        damage_kind=kind,
        element=element,
        power=_power(block, name),
        base_hit=int(hit.group(1)),
        weight=int(weight.group(1)),
        status_riders=tuple(riders),
    )


def _direct_ability_action(source: AbilitySource) -> CombatAction:
    effect = source.owner_effect
    kind, element = _damage_type_and_element(effect, source.registry.ability)
    if source.fixed_mp is None:
        raise SourceGapError(f"{source.registry.ability} does not have a fixed MP cost")
    return CombatAction(
        source.registry.ability,
        mp_cost=source.fixed_mp,
        damage_kind=kind,
        element=element,
        power=_power(effect, source.registry.ability),
    )


def load_hollow_watch_repo_data(*, root: Path | None = None) -> HollowWatchRepoData:
    _raise_preflight_gaps(root=root)

    boss_text = read_repo_text(BOSS_PATH, root=root)
    true_text = read_repo_text(TRUE_BATTLE_PATH, root=root)
    maevra_text = read_repo_text(MAEVRA_COMBAT_PATH, root=root)
    party = _party_from_true_battle(true_text)

    boss_row = extract_markdown_table(boss_text, "Castellan raw line")[0]
    castellan = Combatant(
        "Hollow Watch Castellan",
        "enemy",
        _stats_from_row(boss_row),
        evasion=parse_int(boss_row["EVA"]),
        status_resistance=parse_int(boss_row["SR"]),
        rank="major_boss",
    )

    ballista_row = extract_markdown_table(boss_text, "Fortress Ballista")[0]
    ballista = Combatant(
        "Fortress Ballista",
        "enemy",
        _stats_from_row(ballista_row),
        evasion=parse_int(ballista_row["EVA"]),
        status_resistance=parse_int(ballista_row["SR"]),
    )

    seal_row = extract_markdown_table(boss_text, "Watch Seal")[0]
    watch_seal = Combatant(
        "Watch Seal",
        "enemy",
        _stats_from_row(seal_row),
        evasion=parse_int(seal_row["EVA"]),
        status_resistance=parse_int(seal_row["SR"]),
    )

    crest_source = load_ability_source("Crest Strike", class_name="Crest Knight", root=root)
    pulse_source = load_ability_source("Resonant Pulse", class_name="Crest Knight", root=root)
    mend_source = load_ability_source("Mend", class_name="Blue Warden", root=root)
    clear_source = load_ability_source("Clear Warding", class_name="Blue Warden", root=root)

    crest_strike = _direct_ability_action(crest_source)
    resonant_pulse = _direct_ability_action(pulse_source)

    mend_effect = mend_source.owner_effect
    mend_hp = re.search(r"(\d+)% target Max HP", mend_effect)
    mend_mag = re.search(r"([0-9.]+)\s*[×x]\s*Ilyra", mend_effect)
    if mend_source.fixed_mp is None or not (mend_hp and mend_mag):
        raise SourceGapError("Incomplete Mend healing authority in repo")
    mend = CombatAction(
        mend_source.registry.ability,
        action_kind="heal",
        mp_cost=mend_source.fixed_mp,
        target_side="ally",
        heal_max_hp_percent=int(mend_hp.group(1)) / 100.0,
        heal_magic_scaling=float(mend_mag.group(1)),
    )

    clear_effect = clear_source.owner_effect
    clear_heal = re.search(r"restore\s*(\d+)% target Max HP", clear_effect, re.I)
    clear_sr = re.search(r"grant\s*\+(\d+) Status Resistance for (\d+) rounds", clear_effect, re.I)
    if clear_source.fixed_mp is None or not (clear_heal and clear_sr):
        raise SourceGapError("Incomplete Clear Warding healing/SR authority in repo")
    clear_warding = CombatAction(
        clear_source.registry.ability,
        action_kind="heal",
        mp_cost=clear_source.fixed_mp,
        target_side="ally",
        heal_max_hp_percent=int(clear_heal.group(1)) / 100.0,
        clear_harmful_statuses=1,
    )

    heavy_text = _find_action_block(boss_text, "Heavy Bolt")
    heavy_kind, heavy_element = _damage_type_and_element(heavy_text, "Heavy Bolt")
    heavy_hit = re.search(r"Base Hit\s*(?:\*\*)?(\d+)", heavy_text, re.I)
    heavy_bleed = re.search(r"(?:\*\*)?(\d+)% base Bleed(?:\*\*)?", heavy_text, re.I)
    if not (heavy_hit and heavy_bleed):
        raise SourceGapError("Incomplete Heavy Bolt authority in repo")
    heavy_bolt = CombatAction(
        "Fire Heavy Bolt",
        damage_kind=heavy_kind,
        element=heavy_element,
        power=_power(heavy_text, "Heavy Bolt"),
        base_hit=int(heavy_hit.group(1)),
        status_riders=(StatusRider("bleed", int(heavy_bleed.group(1))),),
    )

    trigger = re.search(r"Walking State begins once HP is \*\*(\d+) or lower\*\*", boss_text)
    seal_reduction = re.search(r"\*\*(\d+)% Fortress-State direct-damage reduction\*\*", boss_text)

    crest_trait = load_trait_source(class_name=crest_source.registry.class_name, root=root)
    warden_trait = load_trait_source(class_name=mend_source.registry.class_name, root=root)
    crest_rank1 = crest_trait.ranks[0].effect
    warden_rank1 = warden_trait.ranks[0].effect
    harmonized = re.search(r"consumes the prime for \*\*\+(\d+)% final damage\*\*", crest_rank1)
    gentle = re.search(
        r"additional \*\*(\d+)% target Max HP\*\* if that target began the action below (\d+)% HP",
        warden_rank1,
    )
    if not (trigger and seal_reduction and harmonized and gentle):
        raise SourceGapError("Incomplete Hollow Watch transition/Seal/Trait authority in repo")

    fortress = (
        _enemy_action(boss_text, "Wallbound Strike"),
        _enemy_action(boss_text, "Bastion Sweep"),
    )
    walking = (
        _enemy_action(boss_text, "Fortress Slam"),
        _enemy_action(boss_text, "Iron Pursuit"),
        _enemy_action(boss_text, "Wall-Shear Sweep"),
    )
    locked = frozenset(
        action.name
        for action in (*fortress, *walking)
        if "cannot be selected on consecutive" in _find_action_block(boss_text, action.name)
        or "cannot repeat consecutively" in _find_action_block(boss_text, action.name)
    )

    return HollowWatchRepoData(
        cyanis=party["Cyanis"],
        ilyra=party["Ilyra"],
        maevra=party["Maevra"],
        castellan=castellan,
        ballista=ballista,
        watch_seal=watch_seal,
        crest_strike=crest_strike,
        resonant_pulse=resonant_pulse,
        mend=mend,
        clear_warding=clear_warding,
        linebreaker_thrust=_linebreaker_from_repo(maevra_text),
        fortress_actions=fortress,
        walking_actions=walking,
        heavy_bolt=heavy_bolt,
        repetition_locked_actions=locked,
        walking_trigger_hp=int(trigger.group(1)),
        watch_seal_reduction=int(seal_reduction.group(1)) / 100.0,
        harmonized_rank1_multiplier=1.0 + int(harmonized.group(1)) / 100.0,
        gentle_continuance_threshold=int(gentle.group(2)) / 100.0,
        gentle_continuance_bonus=int(gentle.group(1)) / 100.0,
        clear_warding_sr_bonus=int(clear_sr.group(1)),
        clear_warding_sr_rounds=int(clear_sr.group(2)),
    )


__all__ = [
    "HollowWatchRepoData",
    "collect_hollow_watch_source_gaps",
    "load_hollow_watch_repo_data",
]
