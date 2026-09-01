# Diyse Balance Simulator — Working Tool

`diysim` is a headless Python balance tool for testing Diyse progression and combat math without manually playing every balance permutation.

The tool is being built on `tooling/diysim-phase1` and should remain off `main` until the simulator is complete enough, validated, and explicitly approved.

## Sectioned structure

Everything in the simulator has an explicit home. See `ARCHITECTURE.md` for the routing contract.

- `combat/` — battle-system mechanics, split by subsystem as implementation expands.
- `progression/` — Player Level, EXP, CEXP, route and encounter-planning math.
- `content/characters/` — permanent playable-character definitions.
- `content/guests/` — temporary/story guest definitions.
- `content/ordinary_enemies/` — ordinary enemies and chapter variants.
- `content/elites/` — optional Elites.
- `content/story_bosses/` — mandatory/story bosses.
- `content/regional_hunts/` — Regional Hunts.
- `content/major_hunts/` — Major Hunts.
- `content/support_objects/` — Ballistae, Seals, Rings, Reservoirs, Anchors, Frames, Nodes, and other supports/components.
- `scenarios/` — composed battle/test setups only.
- `overlays/` — non-destructive working balance experiments such as enemy Power ×1.20 or boss +5 effective core-stat levels.
- `reports/` — simulation/certification results and comparisons.

The existing root Python modules remain temporary compatibility entry points while working code is migrated section-by-section. New systems should not be added to a giant catch-all file.

## Stable Phase 1 scope

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
- Player-EXP route projection with per-segment level checkpoints.
- Required-average encounter EXP solver for target level checkpoints.

## Phase 2 currently implemented

Phase 2 is intentionally layered beside the simpler Phase 1 battle path while it is validated.

- MP pools, authored action MP costs, affordability checks, and 0-MP fallback basic attacks.
- Runtime MP-cost helper for compatible flat and multiplicative modifiers.
- Four-element direct-damage affinities: Weak 125%, Neutral 100%, Resistant 80%, Strongly Resistant 60%, Immune 0%.
- Linked elemental status-affinity modifier support.
- Current universal harmful-status application resolver and Status Resistance.
- Burn round timing, Defense/Spirit penalties, and high-rank damage conversion.
- Freeze affected-round timing, persistence, Physical-hit removal, and high-rank maximum durations.
- Stun affected-turn action-loss timing and high-rank action-loss conversion.
- Staggered Attack/Magic/Speed penalties, duration refresh, fixed-current-round initiative behavior, and high-rank duration conversion.
- Bleed action proc + end-of-round proc cadence, third-turn escalation, high-rank conversion, non-refreshing age, and full-HP removal.
- Direct healing formulas using target Max HP plus caster Magic.
- Full-heal Bleed removal and basic harmful-status clearing support.
- Single-target and all-target action scopes.
- Advanced Monte Carlo summaries with win/wipe/KO rates, round counts, remaining party HP, and remaining party MP.
- JSON loading for the richer Phase 2 combat schema.
- `simulate-advanced` CLI command.

The Phase 2 regression suite covers the canonical affinity table, status application math, MP modifier math, Blue Warden healing formulas, Burn/Staggered high-rank behavior, Bleed cadence/escalation, Freeze/Stun timing, MP spending, elemental weakness, and repeatable advanced Monte Carlo runs.

## Not implemented yet

The simulator does **not** yet claim to be the full production battle engine. Remaining major systems include:

- Revival and Lifeline/other Prepared states.
- Temporary Status Resistance and ordinary stat-change duration stacks beyond Burn/Staggered.
- Regen.
- Items.
- Guard/Defend decision logic.
- Fields.
- Target redirection/interception.
- Multi-hit and follow-up action packages beyond a simple one-resolution action.
- Summons such as Shardfang.
- Standard Cards.
- Prime manifestation/readiness/rest rules.
- Encounter phase/state scripting and authored enemy AI restrictions.
- Current-canon full party ability libraries and enemy data import.

Do not use retired true-battle ability names as golden data merely to reproduce an obsolete benchmark. Current organized canon is the implementation authority; older true battles can be used as requirements checklists until they are regenerated with the current kits.

## Canon sources encoded

- `docs/05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md`
- `docs/05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md`
- `docs/05_BATTLE_SYSTEM/CRITICAL_HITS.md`
- `docs/05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`
- `docs/05_BATTLE_SYSTEM/ELEMENTS.md`
- `docs/05_BATTLE_SYSTEM/STATUS_EFFECTS.md`
- `docs/06_CLASSES_AND_ABILITIES/SELECTED_CLASS_STAT_PACKAGES.md`
- `docs/06_CLASSES_AND_ABILITIES/MP_COST_RULES.md`
- `docs/06_CLASSES_AND_ABILITIES/BASE_CLASSES/BLUE_WARDEN.md`
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
python -m tools.diysim.cli simulate-advanced tools/diysim/sample_advanced_scenario.json --runs 10000 --seed 135
python -m tools.diysim.cli sweep tools/diysim/sample_scenario.json --hp 0.9,1.0,1.1 --attack 0.95,1.0,1.05 --defense 0.95,1.0,1.05 --runs 2000
python -m tools.diysim.cli route tools/diysim/sample_progression.json
python -m tools.diysim.cli solve-exp --start-level 20 --target-level 24 --target-progress 0.5 --encounters 18 --fixed-exp 4300
```

`sample_advanced_scenario.json` demonstrates the richer schema with current representable Crest Knight and Blue Warden actions plus an example enemy. Its numeric encounter tuning is illustrative only; it is not a certified balance benchmark.

`completion_rate` in a progression route is an expected-route planning input only. It can model assumptions such as completing 70% of available ordinary encounters without changing authored per-encounter rewards.

The simulator prints JSON so reports can later feed a UI, CSV exporter, optimizer, or CI regression gate without changing the calculation core.
