# Diyse Balance Simulator — Phase 1

`diysim` is a headless Python balance tool. Phase 1 intentionally covers only mechanics whose current numeric authority is encoded here and directly testable.

## Current Phase-1 scope

- Player Levels 1–70 neutral natural-stat curve.
- Current selected-class natural-stat multipliers.
- Player cumulative EXP curve and EXP-to-next calculations.
- Base Hit / Evasion resolver.
- Direct Physical, Magical and Hybrid damage.
- Same-axis penetration with the current 75% cap.
- Eligible 1.5x Critical direct damage with the ordinary 50% random-Crit cap in simulations.
- Strongest/current direct-damage-reduction value supplied per target.
- Discrete Speed-ordered rounds with party priority on exact party-vs-enemy Speed ties.
- Seeded Monte Carlo direct-battle tests.
- Enemy HP / Attack / Defense multiplier sweeps.

Phase 1 does **not** claim to be the full production battle engine. It does not yet model MP spending, healing/revival, Items, Defend state selection, harmful statuses, Fields, elemental affinities, target redirection, prepared actions, Primes, Cards, or authored encounter scripting. Add those only from their owning canon/data authorities.

## Canon sources encoded

- `docs/05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md`
- `docs/05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md`
- `docs/05_BATTLE_SYSTEM/CRITICAL_HITS.md`
- `docs/05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`
- `docs/06_CLASSES_AND_ABILITIES/SELECTED_CLASS_STAT_PACKAGES.md`
- `docs/10_PROGRESSION_AND_EXP/NATURAL_STAT_CURVE.md`
- `docs/10_PROGRESSION_AND_EXP/PLAYER_EXP_CURVE.md`

## Run from repository root

```bash
python -m tools.diysim.cli stats 40 --class "Crest Knight"
python -m tools.diysim.cli exp --level 62
python -m tools.diysim.cli exp --current-exp 448100
python -m tools.diysim.cli hit 100 15
python -m tools.diysim.cli damage physical --attack 150 --defense 120 --power 135
python -m tools.diysim.cli simulate tools/diysim/sample_scenario.json --runs 10000 --seed 135
python -m tools.diysim.cli sweep tools/diysim/sample_scenario.json --hp 0.9,1.0,1.1 --attack 0.95,1.0,1.05 --defense 0.95,1.0,1.05 --runs 2000
```

The simulator prints JSON so reports can later feed a UI, CSV exporter, optimizer, or CI regression gate without changing the calculation core.
