# Diyse Balance Simulator — Working Tool

`diysim` is a headless Python balance tool for testing Diyse progression and combat math without manually playing every balance permutation.

The tool is being built on `tooling/diysim-phase1` and should remain off `main` until the simulator is complete enough, validated, and explicitly approved.

## Sectioned structure

Everything in the simulator has an explicit home. See `ARCHITECTURE.md` for the routing contract.

- `combat/` — reusable battle-system mechanics, split by subsystem.
- `progression/` — Player Level, EXP, CEXP, route and encounter-planning math.
- `content/characters/` — permanent playable-character definitions.
- `content/guests/` — temporary/story guest definitions.
- `content/ordinary_enemies/` — ordinary enemies and chapter variants.
- `content/elites/` — optional Elites.
- `content/story_bosses/` — mandatory/story-boss reusable definitions.
- `content/regional_hunts/` — Regional Hunts.
- `content/major_hunts/` — Major Hunts.
- `content/support_objects/` — Ballistae, Seals, Rings, Reservoirs, Anchors, Frames, Nodes, and other supports/components.
- `encounters/` — executable fight-specific phase/state machines, AI restrictions, policies, and fight-local metrics.
- `scenarios/` — composed battle/test setups and historical/current benchmark records.
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
- Current universal harmful-status application resolver and effective Status Resistance.
- Reusable temporary flat Status Resistance modifiers with numbered-round duration and same-effect refresh/replace identity.
- Burn round timing, Defense/Spirit penalties, and high-rank damage conversion.
- Freeze affected-round timing, persistence, Physical-hit removal, and high-rank maximum durations.
- Stun affected-turn action-loss timing and high-rank action-loss conversion.
- Staggered Attack/Magic/Speed penalties, duration refresh, fixed-current-round initiative behavior, and high-rank duration conversion.
- Bleed action proc + end-of-round proc cadence, third-turn escalation, high-rank conversion, non-refreshing age, and full-HP removal.
- Direct healing formulas using target Max HP plus caster Magic.
- Full-heal Bleed removal and basic harmful-status clearing support.
- Explicit final-damage action multipliers for authored effects such as Harmonized Crest.
- Single-target and all-target action scopes.
- Advanced Monte Carlo summaries with win/wipe/KO rates, round counts, remaining party HP, and remaining party MP.
- JSON loading for the richer Phase 2 combat schema.
- `simulate-advanced` CLI command.

The first authored encounter-specific runtime is now **Hollow Watch Castellan**. Its own package handles:
- Fortress → Walking same-bar transition;
- Watch Seal 10% Fortress direct-damage reduction;
- Ballista Prepare → Fire → Reload with fixed visible target and destruction cancellation;
- Fortress/Walking weighted action sheets and repetition locks;
- Lv2 Cyanis/Ilyra/Maevra smart-policy benchmark;
- Harmonized Crest Rank I;
- Gentle Continuance Rank I;
- Clear Warding +5 Status Resistance / 2 rounds;
- separate `v93_oracle` historical MP economy and `current` MP economy.

The historical v93 oracle is intentionally not treated as current campaign output after the later global 15% character-Ability MP reduction. `diysim` can run either ruleset explicitly.

## Not implemented yet

The simulator does **not** yet claim to be the full production battle engine. Remaining major systems include:

- Revival and Lifeline/other Prepared states.
- Full temporary Attack/Magic/Defense/Spirit/Speed stat-change stacking/caps.
- Regen.
- Items.
- Guard/Defend decision logic.
- Fields.
- Target redirection/interception.
- Multi-hit and follow-up action packages beyond a simple one-resolution action.
- Summons such as Shardfang.
- Standard Cards.
- Prime manifestation/readiness/rest rules.
- Generalized encounter-state scripting for the rest of the roster.
- Current-canon full party ability libraries and enemy data import.

Do not use retired true-battle ability names as golden current-canon data merely to reproduce an obsolete benchmark. When a historical certification is still useful, preserve it as a labeled historical ruleset and also run the current ruleset separately.

## Canon sources encoded

- `docs/05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md`
- `docs/05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md`
- `docs/05_BATTLE_SYSTEM/CRITICAL_HITS.md`
- `docs/05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`
- `docs/05_BATTLE_SYSTEM/ELEMENTS.md`
- `docs/05_BATTLE_SYSTEM/STATUS_EFFECTS.md`
- `docs/05_BATTLE_SYSTEM/STAT_CHANGES.md`
- `docs/06_CLASSES_AND_ABILITIES/SELECTED_CLASS_STAT_PACKAGES.md`
- `docs/06_CLASSES_AND_ABILITIES/MP_COST_RULES.md`
- `docs/06_CLASSES_AND_ABILITIES/TRAITS.md`
- `docs/06_CLASSES_AND_ABILITIES/BASE_CLASSES/CREST_KNIGHT.md`
- `docs/06_CLASSES_AND_ABILITIES/BASE_CLASSES/BLUE_WARDEN.md`
- `docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/HOLLOW_WATCH_CASTELLAN.md`
- `docs/16_BALANCE_AND_TESTING/TRUE_BATTLES/HOLLOW_WATCH_CASTELLAN_TRUE_BATTLE_v93.md`
- `docs/10_PROGRESSION_AND_EXP/NATURAL_STAT_CURVE.md`
- `docs/10_PROGRESSION_AND_EXP/PLAYER_EXP_CURVE.md`

## Run from repository root

```bash
python -m tools.diysim.cli stats 40 --class "Crest Knight"
python -m tools.diysim.cli exp --level 62
python -m tools.diysim.cli exp --current-exp 448100
python -m tools.diysim.cli hit 100 15
python -m tools.diysim.cli damage physical --attack 150 --defense 120 --power 135
python -m tools.diysim.cli simulate tools/diysim/scenarios/examples/basic_direct.json --runs 10000 --seed 135
python -m tools.diysim.cli simulate-advanced tools/diysim/scenarios/examples/advanced_combat.json --runs 10000 --seed 135
python -m tools.diysim.cli hollow-watch --ruleset v93_oracle --runs 20000 --seed 93
python -m tools.diysim.cli hollow-watch --ruleset current --runs 20000 --seed 93
python -m tools.diysim.cli sweep tools/diysim/scenarios/examples/basic_direct.json --hp 0.9,1.0,1.1 --attack 0.95,1.0,1.05 --defense 0.95,1.0,1.05 --runs 2000
python -m tools.diysim.cli route tools/diysim/progression/examples/sample_route.json
python -m tools.diysim.cli solve-exp --start-level 20 --target-level 24 --target-progress 0.5 --encounters 18 --fixed-exp 4300
```

`--heal-trigger` on `hollow-watch` is a regression-policy reconstruction parameter, not a Diyse combat rule. The v93 report preserved the smart-policy intent but not the original test harness's exact heal threshold.

`scenarios/examples/advanced_combat.json` demonstrates the richer general schema with current representable Crest Knight and Blue Warden actions plus an example enemy. Its numeric encounter tuning is illustrative only; it is not a certified balance benchmark.

`completion_rate` in a progression route is an expected-route planning input only. It can model assumptions such as completing 70% of available ordinary encounters without changing authored per-encounter rewards.

The simulator prints JSON so reports can later feed a UI, CSV exporter, optimizer, or CI regression gate without changing the calculation core.
