from __future__ import annotations

import pytest

from tools.diysim.combat import AdvancedBattleScenario, Combatant
from tools.diysim.progression import Stats
from tools.diysim.sources.enemies import load_enemy_system_rules
from tools.diysim.sources.party import load_party_rules


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


def test_advanced_runtime_uses_repo_active_party_cap() -> None:
    rules = load_party_rules()
    enemy = (_unit("Enemy", "enemy"),)
    at_cap = tuple(_unit(f"Hero {index}", "party") for index in range(rules.active_battle_party))
    over_cap = at_cap + (_unit("One Too Many", "party"),)

    AdvancedBattleScenario(at_cap, enemy)
    with pytest.raises(ValueError, match=str(rules.active_battle_party)):
        AdvancedBattleScenario(over_cap, enemy)
