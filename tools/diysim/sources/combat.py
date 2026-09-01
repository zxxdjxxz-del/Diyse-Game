"""Parse global combat-rule values from authoritative repository Markdown."""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re

from .repo import SourceGapError, find_repo_root, read_repo_text

CRIT_PATH = "docs/05_BATTLE_SYSTEM/CRITICAL_HITS.md"
DAMAGE_PATH = "docs/05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md"
HIT_PATH = "docs/05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md"
ELEMENTS_PATH = "docs/05_BATTLE_SYSTEM/ELEMENTS.md"
STATUS_PATH = "docs/05_BATTLE_SYSTEM/STATUS_EFFECTS.md"


@dataclass(frozen=True)
class CombatRules:
    base_crit_chance: float
    crit_chance_cap: float
    crit_multiplier: float
    penetration_cap: float
    min_hit_chance: int
    max_hit_chance: int
    default_player_base_hit: int
    basic_attack_power: int
    affinity_damage_multipliers: dict[str, float]
    linked_statuses: dict[str, str]
    linked_status_affinity_modifiers: dict[str, int | None]
    status_chance_min: float
    status_chance_max: float
    burn_rounds: int
    burn_rates: dict[str, float]
    burn_defense_penalty: float
    burn_spirit_penalty: float
    freeze_guaranteed_rounds: int
    freeze_persist_chance: float
    freeze_max_rounds: dict[str, int]
    stun_turns: int
    stun_loss_chances: dict[str, float]
    staggered_rounds: dict[str, int]
    staggered_attack_penalty: float
    staggered_magic_penalty: float
    staggered_speed_penalty: float
    bleed_initial_rates: dict[str, float]
    bleed_escalated_rates: dict[str, float]
    bleed_escalation_turns: int


def _pct(pattern: str, text: str, label: str) -> float:
    match = re.search(pattern, text, re.I | re.S)
    if not match:
        raise SourceGapError(f"Missing combat source value: {label}")
    return float(match.group(1)) / 100.0


def _num(pattern: str, text: str, label: str) -> float:
    match = re.search(pattern, text, re.I | re.S)
    if not match:
        raise SourceGapError(f"Missing combat source value: {label}")
    return float(match.group(1))


def _load(root_string: str) -> CombatRules:
    root = Path(root_string)
    crit = read_repo_text(CRIT_PATH, root=root)
    damage = read_repo_text(DAMAGE_PATH, root=root)
    hit = read_repo_text(HIT_PATH, root=root)
    elements = read_repo_text(ELEMENTS_PATH, root=root)
    status = read_repo_text(STATUS_PATH, root=root)

    base_crit = _pct(r"Base Critical Chance:\s*#\s*\*\*(\d+(?:\.\d+)?)%", crit, "base crit") * 100.0
    crit_cap = _pct(r"Critical Chance cap:\s*#\s*\*\*(\d+(?:\.\d+)?)%", crit, "crit cap") * 100.0
    crit_mult = _num(r"Critical multiplier:\s*#\s*\*\*(\d+(?:\.\d+)?)×", crit, "crit multiplier")
    penetration_cap = _pct(r"caps at \*\*(\d+(?:\.\d+)?)%\*\*", damage, "penetration cap")

    clamp = re.search(r"FinalHitChance\s*=\s*clamp\([^,]+,\s*(\d+),\s*(\d+)\)", hit)
    default_hit = re.search(r"Base Hit\s*=\s*(\d+)\*\*", hit)
    basic_power = re.search(r"Basic Attack[\s\S]{0,200}?\*\*(\d+) Power\*\*", damage)
    if not (clamp and default_hit and basic_power):
        raise SourceGapError("Incomplete hit/basic-attack authority")

    affinity: dict[str, float] = {}
    for name, key in (("Weak", "weak"), ("Neutral", "neutral"), ("Resistant", "resistant"), ("Strongly Resistant", "strongly_resistant"), ("Immune", "immune")):
        match = re.search(rf"- {re.escape(name)} — \*\*(\d+)%\*\*", elements)
        if not match:
            raise SourceGapError(f"Missing affinity multiplier for {name}")
        affinity[key] = int(match.group(1)) / 100.0

    linked: dict[str, str] = {}
    for element, status_name in re.findall(r"- (Fire|Ice|Lightning|Earth) → (Burn|Freeze|Stun|Staggered)", elements):
        linked[element.lower()] = status_name.lower()
    if len(linked) != 4:
        raise SourceGapError("Incomplete element/status link table")

    weak_mod = re.search(r"Weak — \*\*\+(\d+) percentage points\*\*", elements)
    resist_mod = re.search(r"Resist — \*\*−(\d+) percentage points\*\*", elements)
    if not (weak_mod and resist_mod):
        raise SourceGapError("Incomplete linked-status affinity modifiers")
    affinity_status_mods = {
        "weak": int(weak_mod.group(1)),
        "neutral": 0,
        "resistant": -int(resist_mod.group(1)),
        "strongly_resistant": -int(resist_mod.group(1)),
        "immune": None,
    }

    chance_clamp = re.search(r"clamped to \*\*(\d+)%–(\d+)%\*\*", status)
    burn_rounds = re.search(r"## Burn[\s\S]*?Duration:\s*#\s*\*\*(\d+) rounds\*\*", status)
    burn_ordinary = re.search(r"Ordinary damage:\s*#\s*\*\*(\d+(?:\.\d+)?)% target Max HP", status)
    burn_regional = re.search(r"Regional Hunt — \*\*75%\*\* ordinary Burn damage = \*\*(\d+(?:\.\d+)?)%", status)
    burn_major = re.search(r"Major Hunt / mandatory boss — \*\*50%\*\* ordinary Burn damage = \*\*(\d+(?:\.\d+)?)%", status)
    burn_def = re.search(r"While Burn is active:[\s\S]*?Defense −(\d+)%", status)
    burn_spr = re.search(r"While Burn is active:[\s\S]*?Spirit −(\d+)%", status)

    freeze_guaranteed = re.search(r"Freeze[\s\S]*?first \*\*(\d+) affected rounds\*\* are guaranteed", status)
    freeze_persist = re.search(r"Freeze[\s\S]*?\*\*(\d+)%\*\* persistence check into affected round 3", status)
    freeze_max = re.search(r"Freeze[\s\S]*?maximum \*\*(\d+) affected rounds\*\*", status)
    freeze_regional = re.search(r"Freeze[\s\S]*?Regional Hunt — maximum \*\*(\d+) affected rounds\*\*", status)
    freeze_major = re.search(r"Freeze[\s\S]*?Major Hunt / mandatory boss — maximum \*\*(\d+) affected round", status)

    stun_turns = re.search(r"Stun[\s\S]*?lasts \*\*(\d+) affected turns\*\*", status)
    stun_ord = re.search(r"Stun[\s\S]*?\*\*(\d+)%\*\* action-loss chance", status)
    stun_reg = re.search(r"Stun[\s\S]*?Regional Hunt — \*\*(\d+)%\*\* action-loss chance", status)
    stun_major = re.search(r"Stun[\s\S]*?Major Hunt / mandatory boss — \*\*(\d+)%\*\* action-loss chance", status)

    stag_ord = re.search(r"## Staggered[\s\S]*?Duration:\s*#\s*\*\*(\d+) rounds\*\*", status)
    stag_atk = re.search(r"## Staggered[\s\S]*?Attack −(\d+)%", status)
    stag_mag = re.search(r"## Staggered[\s\S]*?Magic −(\d+)%", status)
    stag_spd = re.search(r"## Staggered[\s\S]*?Speed −(\d+)%", status)
    stag_reg = re.search(r"Staggered[\s\S]*?Regional Hunt — \*\*(\d+) rounds\*\*", status)
    stag_major = re.search(r"Staggered[\s\S]*?Major Hunt / mandatory boss — \*\*(\d+) rounds\*\*", status)

    bleed_initial = re.search(r"Initial ordinary magnitude:\s*#\s*\*\*(\d+(?:\.\d+)?)%", status)
    bleed_escalated = re.search(r"ordinary magnitude is \*\*(\d+(?:\.\d+)?)% Max HP", status)
    bleed_turns = re.search(r"completes its third turn", status)
    bleed_reg = re.search(r"Regional Hunt — \*\*75%\*\* ordinary Bleed damage = \*\*(\d+(?:\.\d+)?)% Max HP per proc initially\*\*, escalating to \*\*(\d+(?:\.\d+)?)%\*\*", status)
    bleed_major = re.search(r"Major Hunt / mandatory boss — \*\*50%\*\* ordinary Bleed damage = \*\*(\d+(?:\.\d+)?)% Max HP per proc initially\*\*, escalating to \*\*(\d+(?:\.\d+)?)%\*\*", status)

    required = [chance_clamp, burn_rounds, burn_ordinary, burn_regional, burn_major, burn_def, burn_spr,
                freeze_guaranteed, freeze_persist, freeze_max, freeze_regional, freeze_major,
                stun_turns, stun_ord, stun_reg, stun_major, stag_ord, stag_atk, stag_mag, stag_spd, stag_reg, stag_major,
                bleed_initial, bleed_escalated, bleed_turns, bleed_reg, bleed_major]
    if not all(required):
        raise SourceGapError("Incomplete universal status authority in repo")

    return CombatRules(
        base_crit_chance=base_crit,
        crit_chance_cap=crit_cap,
        crit_multiplier=crit_mult,
        penetration_cap=penetration_cap,
        min_hit_chance=int(clamp.group(1)),
        max_hit_chance=int(clamp.group(2)),
        default_player_base_hit=int(default_hit.group(1)),
        basic_attack_power=int(basic_power.group(1)),
        affinity_damage_multipliers=affinity,
        linked_statuses=linked,
        linked_status_affinity_modifiers=affinity_status_mods,
        status_chance_min=float(chance_clamp.group(1)),
        status_chance_max=float(chance_clamp.group(2)),
        burn_rounds=int(burn_rounds.group(1)),
        burn_rates={"ordinary": float(burn_ordinary.group(1))/100.0, "regional_hunt": float(burn_regional.group(1))/100.0, "major_boss": float(burn_major.group(1))/100.0},
        burn_defense_penalty=int(burn_def.group(1))/100.0,
        burn_spirit_penalty=int(burn_spr.group(1))/100.0,
        freeze_guaranteed_rounds=int(freeze_guaranteed.group(1)),
        freeze_persist_chance=int(freeze_persist.group(1))/100.0,
        freeze_max_rounds={"ordinary": int(freeze_max.group(1)), "regional_hunt": int(freeze_regional.group(1)), "major_boss": int(freeze_major.group(1))},
        stun_turns=int(stun_turns.group(1)),
        stun_loss_chances={"ordinary": int(stun_ord.group(1))/100.0, "regional_hunt": int(stun_reg.group(1))/100.0, "major_boss": int(stun_major.group(1))/100.0},
        staggered_rounds={"ordinary": int(stag_ord.group(1)), "regional_hunt": int(stag_reg.group(1)), "major_boss": int(stag_major.group(1))},
        staggered_attack_penalty=int(stag_atk.group(1))/100.0,
        staggered_magic_penalty=int(stag_mag.group(1))/100.0,
        staggered_speed_penalty=int(stag_spd.group(1))/100.0,
        bleed_initial_rates={"ordinary": float(bleed_initial.group(1))/100.0, "regional_hunt": float(bleed_reg.group(1))/100.0, "major_boss": float(bleed_major.group(1))/100.0},
        bleed_escalated_rates={"ordinary": float(bleed_escalated.group(1))/100.0, "regional_hunt": float(bleed_reg.group(2))/100.0, "major_boss": float(bleed_major.group(2))/100.0},
        bleed_escalation_turns=3,
    )


@lru_cache(maxsize=4)
def _cached(root_string: str) -> CombatRules:
    return _load(root_string)


def load_combat_rules(*, root: Path | None = None) -> CombatRules:
    repo = (root or find_repo_root()).resolve()
    return _cached(str(repo))


__all__ = ["CombatRules", "load_combat_rules"]
