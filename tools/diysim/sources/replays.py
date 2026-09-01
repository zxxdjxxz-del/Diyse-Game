"""Parse bounded action-replay rules from current enemy owner prose.

The source layer records only values and preservation rules explicitly authored
in the repository. It does not invent replay defaults.
"""
from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class BoundedReplayRuleSource:
    name: str
    raw_text: str
    power_scale: float | None
    min_total_power: int | None
    max_total_power: int | None
    base_hit: int | None
    record_after_completion: bool
    preserve_damage_identity: bool
    preserve_target_scope: bool
    preserve_weights: bool
    preserve_hit_count: bool
    use_copier_stats: bool
    strips_secondary_mechanics: bool

    @property
    def complete(self) -> bool:
        return (
            self.power_scale is not None
            and self.min_total_power is not None
            and self.max_total_power is not None
            and self.base_hit is not None
            and self.record_after_completion
            and self.preserve_damage_identity
            and self.preserve_target_scope
            and self.preserve_weights
            and self.preserve_hit_count
            and self.use_copier_stats
            and self.strips_secondary_mechanics
        )


def _normalized_prose(raw_text: str) -> str:
    text = re.sub(r"[*_`]", "", raw_text.casefold())
    return re.sub(r"\s+", " ", text)


def parse_bounded_replay_rule_text(name: str, raw_text: str) -> BoundedReplayRuleSource:
    scale = re.search(
        r"source(?:\s+action(?:'s)?)?(?:\s+total)?\s+Power\s*[×x]\s*(0?\.\d+|\d+(?:\.\d+)?)",
        raw_text,
        re.I,
    )
    clamp = re.search(
        r"clamp\s*\(\s*round\s*\([^)]*\)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)",
        raw_text,
        re.I | re.S,
    )
    base_hit = re.search(r"\bBase Hit\s*:?\s*(?:\*\*)?(\d+)(?:\*\*)?", raw_text, re.I)
    lowered = _normalized_prose(raw_text)

    record_after_completion = (
        ("only after" in lowered and ("action completes" in lowered or "action actually completes" in lowered or "action resolves" in lowered))
        or "after the source action completes" in lowered
        or "most recent completed eligible direct-damage party action" in lowered
        or "previously completed eligible party action" in lowered
    )

    preserve_damage_identity = (
        "preserve source damage school/element" in lowered
        or "preserve source damage school / element" in lowered
        or "preserve damage school/element" in lowered
        or "preserve damage school / element" in lowered
        or "source damage school / element" in lowered
        or "source damage school/element" in lowered
    )
    preserve_target_scope = (
        "preserve source target shape" in lowered
        or "preserve target shape" in lowered
        or "source target shape" in lowered
    )
    preserve_weights = (
        "preserve source physical/magical/hybrid weighting" in lowered
        or "preserve source physical / magical / hybrid weighting" in lowered
        or "preserve physical/magical/hybrid weighting" in lowered
        or "preserve physical / magical / hybrid weighting" in lowered
        or "source physical / magical / hybrid weighting" in lowered
    )
    preserve_hit_count = (
        "preserve hit count" in lowered
        or "preserve the original hit count" in lowered
        or "preserve original hit count" in lowered
    )
    use_copier_stats = (
        "own atk/mag" in lowered
        or "own atk / mag" in lowered
        or "own atk/mag as appropriate" in lowered
    )
    strips_secondary_mechanics = (
        "does not copy" in lowered
        or "does not reproduce" in lowered
    ) and any(
        token in lowered
        for token in ("status", "penetration", "healing", "drain", "stat", "resource", "extra action")
    )

    return BoundedReplayRuleSource(
        name=name,
        raw_text=raw_text,
        power_scale=float(scale.group(1)) if scale else None,
        min_total_power=int(clamp.group(1)) if clamp else None,
        max_total_power=int(clamp.group(2)) if clamp else None,
        base_hit=int(base_hit.group(1)) if base_hit else None,
        record_after_completion=record_after_completion,
        preserve_damage_identity=preserve_damage_identity,
        preserve_target_scope=preserve_target_scope,
        preserve_weights=preserve_weights,
        preserve_hit_count=preserve_hit_count,
        use_copier_stats=use_copier_stats,
        strips_secondary_mechanics=strips_secondary_mechanics,
    )


__all__ = ["BoundedReplayRuleSource", "parse_bounded_replay_rule_text"]
