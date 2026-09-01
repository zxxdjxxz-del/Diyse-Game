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

If a required value is missing from repository authority, `diysim` raises a **source-gap error**. It does not infer the value from sample damage, memory, historical files, or a hidden fallback.

See `ARCHITECTURE.md` for the full routing contract.

## Repository sources currently parsed

The working source adapters currently read from the owning files in:

- `docs/05_BATTLE_SYSTEM/` — damage, hit/evasion, criticals, elements, statuses.
- `docs/06_CLASSES_AND_ABILITIES/` — selected-class stat packages, Ability master metadata, individual Ability owner files, Power index, Traits.
- `docs/09_ENEMIES_AND_ENCOUNTERS/` — enemy/boss bodies, actions, AI/state rules.
- `docs/10_PROGRESSION_AND_EXP/` — natural stat and Player EXP authority.
- `docs/16_BALANCE_AND_TESTING/` — certification evidence when a regression comparison needs it.
- `docs/90_WORKING/` — only when an explicitly requested experimental overlay is being tested.

Reusable source adapters now include:

- progression and global combat-rule loaders;
- Ability registry → individual class-owner resolution with MP cross-checking;
- Trait-package/rank parsing;
- common authored-action text parsing that leaves absent fields explicitly missing;
- a repository source-integrity audit.

Parsed values may be cached **in memory for one process**. They are never written back into simulator-owned canon snapshots.

## Source audit

Before a balance run, the source layer can verify that current repo authority still resolves cleanly:

```bash
python -m tools.diysim.cli audit-sources
```

The audit checks current progression authority, global combat authority, every registered class Ability against its individual owner file, and the current Trait register. It reports source problems; it does not compare against simulator-owned expected values.

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

It reads current Hollow Watch values from the current boss/certification files and resolves Crest Knight, Blue Warden, and Trait authority through the shared `sources/` adapters rather than maintaining encounter-local copies of class data.

The runtime owns only encounter behavior such as the Fortress → Walking state change, Ballista preparation cycle, repetition locks and the chosen simulation policy.

### Current source gaps

The current repo does not state every field needed to execute the full authored encounter without inference. The adapter currently reports these gaps:

- Maevra Linebreaker — exact current Power / Defense penetration / MP owner definition;
- Fortress Slam — exact current damage type / element in its owner action line;
- Iron Pursuit — exact current damage type / element in its owner action line;
- Wall-Shear Sweep — exact current damage type / element in its owner action line.

Therefore the Hollow Watch full simulation intentionally stops with `SourceGapError` until the owning repository authority is repaired. Historical/recovered values are **not stored inside `diysim`** and are not silently substituted.

## CLI examples

Run from repository root:

```bash
python -m tools.diysim.cli audit-sources
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

The example scenario JSON files are **synthetic engine examples**, not Diyse canon, fallback data, or certified encounter data.

`--heal-trigger` on `hollow-watch` is a simulator policy parameter, not a combat rule.

The CLI emits JSON so results can later feed reports, optimization passes, a UI, or CI regression gates without changing the calculation core.