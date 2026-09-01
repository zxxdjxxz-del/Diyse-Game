"""Build Hollow Watch simulation inputs by parsing authoritative repo files.

No Diyse numeric canon is stored in this module. Paths and parser labels are
allowed; stats, Powers, MP costs, weights, and encounter values come from the
repository at runtime.
"""
from __future__ import annotations
from dataclasses import dataclass
import re
from pathlib import Path

from tools.diysim.combat.models import CombatAction, Combatant, StatusRider
from tools.diysim.progression import Stats
from tools.diysim.sources.markdown import extract_markdown_table, parse_int
from tools.diysim.sources.repo import SourceGapError, read_repo_text

BOSS_PATH = "docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/HOLLOW_WATCH_CASTELLAN.md"
TRUE_BATTLE_PATH = "docs/16_BALANCE_AND_TESTING/TRUE_BATTLES/HOLLOW_WATCH_CASTELLAN_TRUE_BATTLE_v93.md"
CREST_KNIGHT_PATH = "docs/06_CLASSES_AND_ABILITIES/BASE_CLASSES/CREST_KNIGHT.md"
BLUE_WARDEN_PATH = "docs/06_CLASSES_AND_ABILITIES/BASE_CLASSES/BLUE_WARDEN.md"
TRAITS_PATH = "docs/06_CLASSES_AND_ABILITIES/TRAITS.md"


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
        parse_int(row.get("HP", "1")),
        parse_int(row.get("MP", "0")),
        parse_int(row.get("ATK", "0")),
        parse_int(row.get("MAG", "0")),
        parse_int(row.get("DEF", "0")),
        parse_int(row.get("Spirit", "0")),
        parse_int(row.get("SPD", "0")),
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


def _ability_row(text: str, ability: str) -> dict[str, str]:
    rows = extract_markdown_table(text, "Ability spine")
    for row in rows:
        if row.get("Ability") == ability:
            return row
    raise SourceGapError(f"Missing ability {ability!r} in repo owner file")


def _power(effect: str, ability: str) -> int:
    match = re.search(r"\b(\d+)\s+Power\b", effect)
    if not match:
        raise SourceGapError(f"Missing explicit Power for {ability}")
    return int(match.group(1))


def _find_action_line(text: str, name: str) -> str:
    patterns = (
        rf"\*\*{re.escape(name)}\*\*\s*\n-\s*([^\n]+)",
        rf"-\s*\*\*{re.escape(name)}\*\*\s*[—-]\s*([^\n]+)",
    )
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    raise SourceGapError(f"Missing exact action line for {name}")


def _enemy_action(text: str, name: str) -> CombatAction:
    line = _find_action_line(text, name)
    power = re.search(r"Power\s*\*\*(\d+)\*\*", line)
    hit = re.search(r"Base Hit\s*\*\*(\d+)\*\*", line)
    weight = re.search(r"\*\*(\d+) weight\*\*", line)
    if not (power and hit and weight):
        raise SourceGapError(f"Incomplete action authority for {name}")
    riders: tuple[StatusRider, ...] = ()
    staggered = re.search(r"\*\*(\d+)% base Staggered\*\*", line)
    if staggered:
        riders = (StatusRider("staggered", int(staggered.group(1))),)
    return CombatAction(
        name,
        target_scope="all" if "all conscious" in line else "one",
        damage_kind="physical",
        element="neutral",
        power=int(power.group(1)),
        base_hit=int(hit.group(1)),
        weight=int(weight.group(1)),
        status_riders=riders,
    )


def _linebreaker_from_repo(boss_text: str, true_battle_text: str) -> CombatAction:
    """Require an explicit repo-owned Linebreaker definition; never infer it."""
    combined = boss_text + "\n" + true_battle_text
    explicit = re.search(
        r"Linebreaker(?: Thrust)?[^\n]{0,220}?Power\s*\*\*(\d+)\*\*[^\n]{0,220}?(\d+)%\s+Defense penetration[^\n]{0,220}?(\d+)\s*MP",
        combined,
        re.I,
    )
    if not explicit:
        raise SourceGapError(
            "Maevra Linebreaker lacks an explicit current repository owner definition. "
            "Add/recover it in the appropriate repo canon file; diysim will not store or infer it."
        )
    return CombatAction(
        "Linebreaker Thrust",
        mp_cost=int(explicit.group(3)),
        damage_kind="physical",
        element="neutral",
        power=int(explicit.group(1)),
        base_hit=100,
        defense_penetration=int(explicit.group(2)) / 100.0,
    )


def load_hollow_watch_repo_data(*, root: Path | None = None) -> HollowWatchRepoData:
    boss_text = read_repo_text(BOSS_PATH, root=root)
    true_text = read_repo_text(TRUE_BATTLE_PATH, root=root)
    crest_text = read_repo_text(CREST_KNIGHT_PATH, root=root)
    warden_text = read_repo_text(BLUE_WARDEN_PATH, root=root)
    trait_text = read_repo_text(TRAITS_PATH, root=root)

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
    ballista = Combatant("Fortress Ballista", "enemy", _stats_from_row(ballista_row))
    seal_row = extract_markdown_table(boss_text, "Watch Seal")[0]
    watch_seal = Combatant("Watch Seal", "enemy", _stats_from_row(seal_row))

    crest_row = _ability_row(crest_text, "Crest Strike")
    pulse_row = _ability_row(crest_text, "Resonant Pulse")
    mend_row = _ability_row(warden_text, "Mend")
    clear_row = _ability_row(warden_text, "Clear Warding")

    crest_strike = CombatAction(
        "Crest Strike", mp_cost=parse_int(crest_row["MP"]), damage_kind="physical",
        element="neutral", power=_power(crest_row["Current effect"], "Crest Strike"), base_hit=100,
    )
    resonant_pulse = CombatAction(
        "Resonant Pulse", mp_cost=parse_int(pulse_row["MP"]), damage_kind="magical",
        element="colorless", power=_power(pulse_row["Current effect"], "Resonant Pulse"), base_hit=100,
    )

    mend_effect = mend_row["Current effect"]
    mend_hp = re.search(r"(\d+)% target Max HP", mend_effect)
    mend_mag = re.search(r"([0-9.]+)\s*[×x]\s*Ilyra", mend_effect)
    if not (mend_hp and mend_mag):
        raise SourceGapError("Incomplete Mend healing formula in repo")
    mend = CombatAction(
        "Mend", action_kind="heal", mp_cost=parse_int(mend_row["MP"]), target_side="ally",
        heal_max_hp_percent=int(mend_hp.group(1)) / 100.0, heal_magic_scaling=float(mend_mag.group(1)),
    )

    clear_effect = clear_row["Current effect"]
    clear_heal = re.search(r"restore\s*\*\*(\d+)% target Max HP\*\*", clear_effect, re.I)
    clear_sr = re.search(r"grant\s*\*\*\+(\d+) Status Resistance for (\d+) rounds\*\*", clear_effect, re.I)
    if not (clear_heal and clear_sr):
        raise SourceGapError("Incomplete Clear Warding healing/SR authority in repo")
    clear_warding = CombatAction(
        "Clear Warding", action_kind="heal", mp_cost=parse_int(clear_row["MP"]), target_side="ally",
        heal_max_hp_percent=int(clear_heal.group(1)) / 100.0, clear_harmful_statuses=1,
    )

    heavy_line = re.search(
        r"Fire Heavy Bolt[^\n]*?Power\s*\*\*(\d+)\*\*; Base Hit\s*\*\*(\d+)\*\*; \*\*(\d+)% base Bleed\*\*",
        boss_text,
    )
    if not heavy_line:
        raise SourceGapError("Incomplete Heavy Bolt authority in repo")
    heavy_bolt = CombatAction(
        "Fire Heavy Bolt", damage_kind="physical", element="neutral",
        power=int(heavy_line.group(1)), base_hit=int(heavy_line.group(2)),
        status_riders=(StatusRider("bleed", int(heavy_line.group(3))),),
    )

    trigger = re.search(r"Walking State begins once HP is \*\*(\d+) or lower\*\*", boss_text)
    seal_reduction = re.search(r"\*\*(\d+)% Fortress-State direct-damage reduction\*\*", boss_text)
    harmonized = re.search(r"Rank I[^\n]*consumes the prime for \*\*\+(\d+)% final damage\*\*", trait_text)
    gentle = re.search(
        r"Gentle Continuance[\s\S]{0,600}?Rank I[^\n]*additional \*\*(\d+)% target Max HP\*\* if that target began the action below (\d+)% HP",
        trait_text,
    )
    if not (trigger and seal_reduction and harmonized and gentle):
        raise SourceGapError("Incomplete Hollow Watch transition/Seal/Trait authority in repo")

    fortress = (_enemy_action(boss_text, "Wallbound Strike"), _enemy_action(boss_text, "Bastion Sweep"))
    walking = (
        _enemy_action(boss_text, "Fortress Slam"),
        _enemy_action(boss_text, "Iron Pursuit"),
        _enemy_action(boss_text, "Wall-Shear Sweep"),
    )
    locked = frozenset(
        action.name
        for action in (*fortress, *walking)
        if "cannot be selected on consecutive" in _find_action_line(boss_text, action.name)
        or "cannot repeat consecutively" in _find_action_line(boss_text, action.name)
    )

    return HollowWatchRepoData(
        cyanis=party["Cyanis"], ilyra=party["Ilyra"], maevra=party["Maevra"],
        castellan=castellan, ballista=ballista, watch_seal=watch_seal,
        crest_strike=crest_strike, resonant_pulse=resonant_pulse,
        mend=mend, clear_warding=clear_warding,
        linebreaker_thrust=_linebreaker_from_repo(boss_text, true_text),
        fortress_actions=fortress, walking_actions=walking, heavy_bolt=heavy_bolt,
        repetition_locked_actions=locked,
        walking_trigger_hp=int(trigger.group(1)),
        watch_seal_reduction=int(seal_reduction.group(1)) / 100.0,
        harmonized_rank1_multiplier=1.0 + int(harmonized.group(1)) / 100.0,
        gentle_continuance_threshold=int(gentle.group(2)) / 100.0,
        gentle_continuance_bonus=int(gentle.group(1)) / 100.0,
        clear_warding_sr_bonus=int(clear_sr.group(1)),
        clear_warding_sr_rounds=int(clear_sr.group(2)),
    )


__all__ = ["HollowWatchRepoData", "load_hollow_watch_repo_data"]
