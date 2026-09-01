from __future__ import annotations

import pytest

from tools.diysim.combat import AdvancedBattleScenario, Combatant
from tools.diysim.progression import Stats
from tools.diysim.sources.enemies import load_enemy_system_rules


def _unit(name: str, side: str) -> Combatant:
    return Combatant(name, side, Stats(100, 0, 10, 10, 10, 10, 10))


def test_advanced_runtime_uses_repo_simultaneous_enemy_cap() -> None:
    rules = load_enemy_system_rules()
    party = (_unit("Hero", "party"),)
    at_cap = tuple(_unit(f"Enemy {index}", "enemy") for index in range(rules.max_active_enemies))
    over_cap = at_cap + (_unit("One Too Many", "enemy"),)

    AdvancedBattleScenario(party, at_cap)
    with pytest.raises(ValueError, match=str(rules.max_active_enemies)):
        AdvancedBattleScenario(party, over_cap)
