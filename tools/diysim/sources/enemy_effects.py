"""Parser for shared enemy ``Power: N/A`` effect-action grammar.

The parser is intentionally conservative. It only returns an executable action
when the owner text provides enough authority for a shared combat primitive.
Encounter relationships, bespoke state advancement, tagged-target rules, and
other local mechanics remain explicit blockers for encounter runtimes.
"""
from __future__ import annotations

from dataclasses import dataclass
import re

from tools.diysim.combat.models import CombatAction, TemporaryModifierSpec


@dataclass(frozen=True)
class EnemyEffectParseResult:
    action: CombatAction | None
    blockers: tuple[str, ...] = ()
    minimum_round: int = 1
    maximum_uses: int | None = None
    forced_follow_up: str | None = None
    forced_by_action: str | None = None


_CORE_STAT_RE = re.compile(
    r"\b(Attack|Magic|Defense|Spirit|Speed)\s*([+\-−])\s*(\d+(?:\.\d+)?)\s*%?",
    re.I,
)
_TOTAL_DEFENSE_RE = re.compile(r"([+\-−])\s*(\d+(?:\.\d+)?)\s+Total\s+Defense\b", re.I)
_BASE_HIT_RE = re.compile(r"\bBase\s+Hit\s*([+\-−])\s*(\d+)\b", re.I)
_HEAL_FLAT_RE = re.compile(r"\b(?:restore|restores|heal|heals)\s+\*{0,2}(\d+)\s*HP\b", re.I)
_DIRECT_REDUCTION_RE = re.compile(
    r"\b(?:incoming\s+)?direct(?:\s+HP)?\s+damage\s+(?:reduction|reduced\s+by)\s*[:=]?\s*(\d+(?:\.\d+)?)%",
    re.I,
)
_FOLLOWING_ROUND_RE = re.compile(r"through\s+(?:the\s+)?end\s+of\s+(?:the\s+)?following\s+round", re.I)
_FOR_ROUNDS_RE = re.compile(r"\bfor\s+(\d+)\s+(?:full\s+)?(?:normal\s+)?rounds?\b", re.I)
_ROUND_MIN_RE = re.compile(r"\bRound\s+(\d+)\s+or\s+later\s+only\b", re.I)
_FORCED_FOLLOW_RE = re.compile(
    r"\blocks\s+\*\*([^*]+)\*\*\s+as\s+(?:the\s+)?[^\n.]*next\s+selected\s+action",
    re.I,
)


def _signed(sign: str, magnitude: str) -> float:
    value = float(magnitude)
    return -value if sign in {"-", "−"} else value


def _default_core_duration(values: dict[str, float]) -> int | None:
    magnitude = max((abs(value) for value in values.values()), default=0.0)
    if magnitude <= 10:
        return 4
    if magnitude <= 20:
        return 3
    if magnitude <= 30:
        return 2
    return None


def _duration(raw_text: str, core_values: dict[str, float]) -> int | None:
    if _FOLLOWING_ROUND_RE.search(raw_text):
        return 2
    match = _FOR_ROUNDS_RE.search(raw_text)
    if match:
        return int(match.group(1))
    if core_values:
        return _default_core_duration(core_values)
    return None


def _core_changes(raw_text: str) -> dict[str, float]:
    result: dict[str, float] = {}
    for stat, sign, magnitude in _CORE_STAT_RE.findall(raw_text):
        result[stat.lower()] = _signed(sign, magnitude)
    total_defense = _TOTAL_DEFENSE_RE.search(raw_text)
    if total_defense:
        value = _signed(total_defense.group(1), total_defense.group(2))
        result["defense"] = value
        result["spirit"] = value
    return result


def _target_side(raw_text: str, *, has_local_effect: bool) -> tuple[str | None, list[str]]:
    blockers: list[str] = []
    lowered = raw_text.lower()
    if re.search(r"target\s*:\s*\n?\s*>?\s*self\b", raw_text, re.I):
        return "self", blockers
    if re.search(r"one\s+(?:other\s+)?living\s+allied", raw_text, re.I):
        if "construct" in lowered or "machine" in lowered:
            blockers.append("effect target requires encounter roster tag")
        return "ally", blockers
    if re.search(r"all\s+(?:living\s+)?allied", raw_text, re.I):
        if "construct" in lowered or "machine" in lowered:
            blockers.append("effect target requires encounter roster tag")
        return "ally_all", blockers
    if "linked " in lowered or "recipient" in lowered or "formation relationship" in lowered:
        blockers.append("effect target/effect depends on encounter relationship")
        return None, blockers
    # Local stat/Guard-style effects without a printed external target modify
    # the acting enemy. This follows the action's own local effect clause; no
    # numeric magnitude or target substitution is invented.
    if has_local_effect:
        return "self", blockers
    return None, blockers


def _forced_by_action(action_name: str, raw_text: str) -> str | None:
    pattern = re.compile(
        rf"(?im)^\s*(?:[-*]\s*)?(?:\*\*)?(.+?)(?:\*\*)?\s+forces\s+(?:\*\*)?{re.escape(action_name)}(?:\*\*)?\s+as\s+[^\n.]*next\s+selected\s+action"
    )
    match = pattern.search(raw_text)
    return re.sub(r"\*+", "", match.group(1)).strip() if match else None


def parse_enemy_effect_action(action_name: str, raw_text: str) -> EnemyEffectParseResult:
    blockers: list[str] = []
    core_values = _core_changes(raw_text)
    base_hit_match = _BASE_HIT_RE.search(raw_text)
    heal_match = _HEAL_FLAT_RE.search(raw_text)
    reduction_match = _DIRECT_REDUCTION_RE.search(raw_text)

    base_hit_flat = _signed(*base_hit_match.groups()) if base_hit_match else 0.0
    heal_flat = int(heal_match.group(1)) if heal_match else 0
    direct_reduction = float(reduction_match.group(1)) / 100.0 if reduction_match else 0.0
    has_local_effect = bool(core_values or base_hit_match or heal_match or reduction_match)

    target, target_blockers = _target_side(raw_text, has_local_effect=has_local_effect)
    blockers.extend(target_blockers)

    minimum_round = 1
    round_match = _ROUND_MIN_RE.search(raw_text)
    if round_match:
        minimum_round = int(round_match.group(1))

    maximum_uses = 1 if re.search(r"\bonce\s+per\s+battle\b", raw_text, re.I) else None
    forced_follow_match = _FORCED_FOLLOW_RE.search(raw_text)
    forced_follow_up = forced_follow_match.group(1).strip() if forced_follow_match else None
    forced_by_action = _forced_by_action(action_name, raw_text)

    # Preparation/reload actions can be executable scheduler actions even when
    # they have no immediate numeric battlefield effect.
    scheduler_only = forced_follow_up is not None or forced_by_action is not None

    if re.search(r"\bInterruptible\s+Preparation\b|formation relationship", raw_text, re.I):
        blockers.append("effect requires encounter-specific preparation/relationship runtime")
    if re.search(r"\badvances?\b.*\bstate\b|\bstate\s+one\s+step\b", raw_text, re.I):
        blockers.append("effect advances authored encounter state")
    if re.search(r"\bHard\s+cap\b[\s\S]*successful\s+uses", raw_text, re.I):
        blockers.append("effect successful-use cap requires outcome-aware runtime")
    if re.search(r"\bchoose|\bselect\b.*\b(?:mode|stance|protocol|forecast)\b", raw_text, re.I):
        blockers.append("effect requires authored state/mode choice")

    duration = _duration(raw_text, core_values)
    if core_values and duration is None:
        blockers.append("core-stat effect above 30% requires explicit duration")

    modifier: TemporaryModifierSpec | None = None
    if has_local_effect and not blockers:
        modifier_duration = duration or (2 if base_hit_match or reduction_match else 1)
        modifier = TemporaryModifierSpec(
            effect_id=action_name,
            duration_rounds=modifier_duration,
            attack_percent=core_values.get("attack", 0.0),
            magic_percent=core_values.get("magic", 0.0),
            defense_percent=core_values.get("defense", 0.0),
            spirit_percent=core_values.get("spirit", 0.0),
            speed_percent=core_values.get("speed", 0.0),
            base_hit_flat=int(base_hit_flat),
            direct_damage_reduction=direct_reduction,
        )

    if not has_local_effect and not scheduler_only and not blockers:
        blockers.append("non-damage effect has no shared executable primitive")
    if target is None and has_local_effect and not blockers:
        blockers.append("non-damage effect target is not resolved")

    if blockers:
        return EnemyEffectParseResult(
            None, tuple(dict.fromkeys(blockers)), minimum_round, maximum_uses,
            forced_follow_up, forced_by_action,
        )

    target_side = "self" if target == "self" else "ally"
    target_scope = "all" if target == "ally_all" else "one"
    action = CombatAction(
        action_name,
        action_kind="effect",
        target_side=target_side,
        target_scope=target_scope,
        heal_flat=heal_flat,
        temporary_modifiers=(modifier,) if modifier is not None else (),
    )
    return EnemyEffectParseResult(
        action, (), minimum_round, maximum_uses, forced_follow_up, forced_by_action,
    )


__all__ = ["EnemyEffectParseResult", "parse_enemy_effect_action"]
