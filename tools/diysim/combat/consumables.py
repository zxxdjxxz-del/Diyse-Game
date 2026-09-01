"""Prepared-inventory and consumable resolution for true-battle simulations."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re
from typing import Literal, Sequence

from ..common import round_half_up
from ..sources import ConsumableSource, SourceGapError, load_consumable
from .models import CombatUnit, StatusName
from .status_runtime import clear_bleed_if_full

TargetScope = Literal["one", "all"]
_HARMFUL_STATUSES: tuple[StatusName, ...] = ("burn", "freeze", "stun", "staggered", "bleed")


@dataclass(frozen=True)
class ConsumableEffect:
    name: str
    target_scope: TargetScope
    hp_flat: int = 0
    hp_fraction: float = 0.0
    mp_flat: int = 0
    mp_fraction: float = 0.0
    revive_hp_fraction: float = 0.0
    revive_mp_fraction: float = 0.0
    clear_named_statuses: frozenset[StatusName] = frozenset()
    clear_one_harmful_status: bool = False
    clear_all_harmful_statuses: bool = False

    @property
    def is_revival(self) -> bool:
        return self.revive_hp_fraction > 0.0


@dataclass
class PreparedInventory:
    counts: dict[str, int]
    used: dict[str, int] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for name, count in self.counts.items():
            if not name:
                raise ValueError("consumable name cannot be empty")
            if count < 0:
                raise ValueError(f"consumable count cannot be negative: {name}")
        self.counts = dict(self.counts)
        self.used = dict(self.used)

    def remaining(self, name: str) -> int:
        return self.counts.get(name, 0)

    def available(self, name: str) -> bool:
        return self.remaining(name) > 0

    def consume(self, name: str) -> None:
        if not self.available(name):
            raise ValueError(f"prepared inventory has no remaining {name}")
        self.counts[name] -= 1
        self.used[name] = self.used.get(name, 0) + 1

    @property
    def total_used(self) -> int:
        return sum(self.used.values())


def _percentage(pattern: str, text: str) -> float:
    match = re.search(pattern, text, re.I)
    return int(match.group(1)) / 100.0 if match else 0.0


def parse_consumable_effect(source: ConsumableSource) -> ConsumableEffect:
    text = source.function
    lowered = text.casefold()
    target_scope: TargetScope = "all" if "all conscious" in lowered or "all ko active-party" in lowered else "one"

    hp_flat_match = re.search(r"Restore\s+([\d,]+)\s+HP\b", text, re.I)
    mp_flat_match = re.search(r"Restore\s+([\d,]+)\s+MP\b", text, re.I)

    hp_fraction = _percentage(r"Restore\s+(\d+)%\s+Max HP", text)
    mp_fraction = _percentage(r"Restore\s+(\d+)%\s+Max MP", text)
    revive_hp_fraction = _percentage(r"Revive.*?at\s+(\d+)%\s+Max HP", text)
    revive_mp_fraction = _percentage(r"\+\s*(\d+)%\s+Max MP", text) if "Revive" in text else 0.0

    named: set[StatusName] = set()
    for status in _HARMFUL_STATUSES:
        if re.search(rf"\b{status}\b", text, re.I):
            named.add(status)

    clear_one = "Remove one eligible ordinary harmful status" in text
    clear_all = (
        "Remove all eligible ordinary harmful statuses" in text
        or "remove all eligible negative status effects" in lowered
    )

    recognized = any(
        (
            hp_flat_match,
            mp_flat_match,
            hp_fraction,
            mp_fraction,
            revive_hp_fraction,
            named,
            clear_one,
            clear_all,
        )
    )
    if not recognized:
        raise SourceGapError(f"Consumable effect is not yet resolvable: {source.name} — {source.function}")

    return ConsumableEffect(
        name=source.name,
        target_scope=target_scope,
        hp_flat=int(hp_flat_match.group(1).replace(",", "")) if hp_flat_match else 0,
        hp_fraction=hp_fraction,
        mp_flat=int(mp_flat_match.group(1).replace(",", "")) if mp_flat_match else 0,
        mp_fraction=mp_fraction,
        revive_hp_fraction=revive_hp_fraction,
        revive_mp_fraction=revive_mp_fraction,
        clear_named_statuses=frozenset(named),
        clear_one_harmful_status=clear_one,
        clear_all_harmful_statuses=clear_all,
    )


def load_consumable_effect(name: str, *, root: Path | None = None) -> ConsumableEffect:
    return parse_consumable_effect(load_consumable(name, root=root))


def _clear_statuses(target: CombatUnit, effect: ConsumableEffect) -> None:
    if effect.clear_all_harmful_statuses:
        for status in _HARMFUL_STATUSES:
            target.statuses.pop(status, None)
        return
    if effect.clear_named_statuses:
        for status in effect.clear_named_statuses:
            target.statuses.pop(status, None)
        return
    if effect.clear_one_harmful_status:
        for status in _HARMFUL_STATUSES:
            if status in target.statuses:
                target.statuses.pop(status, None)
                return


def resolve_consumable_on_target(effect: ConsumableEffect, target: CombatUnit) -> None:
    """Resolve one target of a consumable after its inventory count is spent."""
    if effect.is_revival:
        if target.alive:
            raise ValueError(f"{effect.name} requires a KO target")
        target.hp = max(1, round_half_up(target.max_hp * effect.revive_hp_fraction))
        if effect.revive_mp_fraction:
            target.mp = min(target.max_mp, round_half_up(target.max_mp * effect.revive_mp_fraction))
    else:
        if not target.alive:
            raise ValueError(f"{effect.name} cannot target a KO unit")
        hp_restore = effect.hp_flat + round_half_up(target.max_hp * effect.hp_fraction)
        mp_restore = effect.mp_flat + round_half_up(target.max_mp * effect.mp_fraction)
        if hp_restore:
            target.hp = min(target.max_hp, target.hp + hp_restore)
            clear_bleed_if_full(target)
        if mp_restore:
            target.mp = min(target.max_mp, target.mp + mp_restore)

    _clear_statuses(target, effect)


def use_consumable(
    inventory: PreparedInventory,
    effect: ConsumableEffect,
    *,
    target: CombatUnit | None = None,
    party: Sequence[CombatUnit] | None = None,
) -> int:
    """Spend one item and resolve it. Return the number of affected targets."""
    inventory.consume(effect.name)
    if effect.target_scope == "one":
        if target is None:
            raise ValueError(f"{effect.name} requires one target")
        resolve_consumable_on_target(effect, target)
        return 1

    if party is None:
        raise ValueError(f"{effect.name} requires party targets")
    targets = [unit for unit in party if (not unit.alive if effect.is_revival else unit.alive)]
    for unit in targets:
        resolve_consumable_on_target(effect, unit)
    return len(targets)


__all__ = [
    "ConsumableEffect",
    "PreparedInventory",
    "load_consumable_effect",
    "parse_consumable_effect",
    "resolve_consumable_on_target",
    "use_consumable",
]
