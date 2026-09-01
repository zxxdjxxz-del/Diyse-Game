from __future__ import annotations

from tools.diysim.battle import AdvancedBattleScenario, simulate_advanced
from tools.diysim.core import Stats
from tools.diysim.rules import Combatant


def test_advanced_monte_carlo_is_repeatable() -> None:
    party = Combatant("Hero", "party", Stats(300, 0, 100, 0, 50, 50, 40))
    enemy = Combatant("Enemy", "enemy", Stats(200, 0, 60, 0, 50, 50, 30))
    scenario = AdvancedBattleScenario((party,), (enemy,), max_rounds=20)

    first = simulate_advanced(scenario, runs=100, seed=77)
    second = simulate_advanced(scenario, runs=100, seed=77)

    assert first == second
    assert first.party_wins + first.enemy_wins + first.draws == 100
