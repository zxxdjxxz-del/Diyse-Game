# Diyse Balance Simulator — Working Tool

`diysim` is a headless Python balance tool for testing Diyse progression and combat without manually replaying every balance permutation.

It is being developed on `tooling/diysim-phase1`. Keep it off `main` until it is validated and explicitly approved.

## Core rule: Diyse data stays in Diyse

The simulator does **not** own a second copy of canon.

- `sources/` reads current values from the repository's owning files.
- `combat/` implements reusable battle algorithms.
- `progression/` implements progression calculations using repo-loaded curves/tables.
- `encounters/` implements fight-specific state machines and test policies while consuming repo-loaded actor/action data.
- `overlays/` describes non-destructive experiments applied to loaded owner data.
- `reports/` contains generated results only.
- `scenarios/` is limited to synthetic/demo inputs or non-canon simulation-policy configuration; real Diyse actor/enemy values are not copied there.

If a required value is missing from repository authority, `diysim` raises a **source-gap error**. It does not infer the value from sample damage, memory, or a hidden fallback.

See `ARCHITECTURE.md` for the full routing contract.

## Repository sources currently parsed

The working source adapters currently read from the owning files in:

- `docs/05_BATTLE_SYSTEM/` — damage, hit/evasion, criticals, elements, statuses.
- `docs/06_CLASSES_AND_ABILITIES/` — selected-class stat packages, current class actions, Traits.
- `docs/09_ENEMIES_AND_ENCOUNTERS/` — enemy/boss bodies, actions, AI/state rules.
- `docs/10_PROGRESSION_AND_EXP/` — natural stat and Player EXP authority.
- `docs/16_BALANCE_AND_TESTING/` — certification evidence when a regression comparison needs it.
- `docs/90_WORKING/` — only when an explicitly requested experimental overlay is being tested.

Parsed values may be cached **in memory for one process**. They are never written back into simulator-owned canon snapshots.

## Implemented calculation/runtime layers

Current work includes:

- natural stat construction and selected-class multipliers from repo authority;
- Player EXP/level lookup from the published current table;
- Base Hit/Evasion;
- Physical/Magical/Hybrid direct damage;
- penetration, Crit, affinity and status rules loaded from battle-system owners;
- MP affordability and cost helpers;
- direct healing;
- Burn, Freeze, Stun, Staggered and Bleed timing;
- temporary flat Status Resistance support;
- simple and richer seeded Monte Carlo runtimes;
- route/encounter EXP projection;
- non-destructive balance sweeps.

The full production battle engine is **not** implemented yet. Prepared states, full temporary core-stat stacking, Regen, Items, Guard decision logic, Fields, redirection/interception, full multihit/follow-up packages, summons, Cards, Primes and much of the encounter roster remain future sections.

## Hollow Watch integration

`encounters/story_bosses/hollow_watch_castellan/` is the first authored encounter adapter.

It parses current Hollow Watch values directly from:

- `docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/HOLLOW_WATCH_CASTELLAN.md`;
- `docs/16_BALANCE_AND_TESTING/TRUE_BATTLES/HOLLOW_WATCH_CASTELLAN_TRUE_BATTLE_v93.md`;
- the current Crest Knight / Blue Warden / Trait owners in `docs/06_CLASSES_AND_ABILITIES/`.

The runtime owns only encounter behavior such as the Fortress → Walking state change, Ballista preparation cycle, repetition locks and the chosen simulation policy.

### Current source gap

The current repo does not expose Maevra's exact **Linebreaker** definition in an owning current file. Therefore the Hollow Watch full simulation intentionally stops with `SourceGapError` until that repository authority is repaired. The recovered external/historical value is **not stored inside `diysim`**.

## CLI examples

Run from repository root:

```bash
python -m tools.diysim.cli stats 40 --class "Crest Knight"
python -m tools.diysim.cli exp --level 62
python -m tools.diysim.cli exp --current-exp 448100
python -m tools.diysim.cli hit 100 15
python -m tools.diysim.cli damage physical --attack 150 --defense 120 --power 135
python -m tools.diysim.cli simulate tools/diysim/scenarios/examples/basic_direct.json --runs 10000 --seed 135
python -m tools.diysim.cli simulate-advanced tools/diysim/scenarios/examples/advanced_combat.json --runs 10000 --seed 135
python -m tools.diysim.cli hollow-watch --runs 20000 --seed 93
python -m tools.diysim.cli sweep tools/diysim/scenarios/examples/basic_direct.json --hp 0.9,1.0,1.1 --attack 0.95,1.0,1.05 --defense 0.95,1.0,1.05 --runs 2000
python -m tools.diysim.cli route tools/diysim/progression/examples/sample_route.json
python -m tools.diysim.cli solve-exp --start-level 20 --target-level 24 --target-progress 0.5 --encounters 18 --fixed-exp 4300
```

The example scenario JSON files are **synthetic engine examples**, not Diyse canon or certified encounter data.

`--heal-trigger` on `hollow-watch` is a simulator policy parameter, not a combat rule.

The CLI emits JSON so results can later feed reports, optimization passes, a UI, or CI regression gates without changing the calculation core.
