# Diyse Balance Simulator — Section Architecture

`diysim` mirrors Diyse's organized-canon philosophy: every major simulator system gets an explicit home, but **the simulator never owns Diyse canon data**.

## Structural rule

- Shared math may live in a small common/core layer.
- Every gameplay subsystem gets its own section.
- **Stats, ability values, MP costs, enemy bodies, Powers, affinities, AI weights, encounter thresholds, progression tables, Cards, Primes, Items, and equipment values are read from the repository at runtime.**
- `diysim` may store algorithms, parsers, test/simulation policies, experimental overlay instructions, and generated reports.
- `diysim` must not maintain shadow copies of canon actor/content data.
- If an authoritative value is missing from the repo, fail with a source-gap error instead of inferring or falling back to a simulator copy.
- Canon owner data and experimental balance overlays stay separate.
- A working/sensitivity value must never silently replace owner-canon data.

## Top-level sections

### `sources/`
Owns read-only repository access and parsers/adapters for authoritative Diyse files.

Examples of source domains:
- `docs/05_BATTLE_SYSTEM/`
- `docs/06_CLASSES_AND_ABILITIES/`
- `docs/07_CARDS/`
- `docs/08_ITEMS_AND_EQUIPMENT/`
- `docs/09_ENEMIES_AND_ENCOUNTERS/`
- `docs/10_PROGRESSION_AND_EXP/`
- `docs/16_BALANCE_AND_TESTING/`
- `docs/90_WORKING/` only when an explicitly requested experimental overlay is being tested.

The source layer may cache parsed data in memory during one run, but it must not write canonical snapshots into `tools/diysim/`.

### `combat/`
Owns reusable combat-system algorithms only. Subsystems remain individually identifiable: damage, hit/evasion, criticals, elements, statuses, temporary modifiers, MP, healing, turn/round sequencing, targeting, Guard, Prepared actions, Fields, Items, Cards, and Primes.

Boss names, chapter checks, actor stat blocks, or one-fight AI data do not belong here.

### `progression/`
Owns progression algorithms: Player Level calculations, EXP/CEXP projection, route planning, encounter-count planning, and mandatory/completionist comparisons.

The curve/table values themselves must be parsed from the owning repo sources rather than duplicated here.

### `encounters/`
Encounter-specific execution logic only: composed phase/state machines, finite support cycles, authored AI restrictions, scenario-specific player policies, transition handling, and fight-local metrics.

Each encounter loader reads its actor/action/phase values from repository owner files through `sources/`. Encounter modules must not define their own copied stat/action constants.

Examples:
- `encounters/story_bosses/hollow_watch_castellan/`
- `encounters/regional_hunts/.../`
- `encounters/major_hunts/.../`

### `scenarios/`
Stores only simulation setup/policy configuration that is not itself Diyse canon, such as seed counts, comparison routes, or explicit user-requested testing assumptions.

Do **not** store copied party stats, boss stats, MP costs, Powers, or certification numbers here. Historical certification evidence should be parsed from `docs/16_BALANCE_AND_TESTING/` when needed.

### `overlays/`
Non-destructive balance experiments and sensitivities. Examples: enemy direct-Power multipliers, effective-level stat experiments, HP/ATK/DEF sweeps, or local action-density candidates.

An overlay describes a transformation to parsed owner data; it does not duplicate the owner data itself. Overlay output is never canon unless separately promoted to the owning repo domain.

### `reports/`
Generated simulation results, comparisons, and certification evidence. Reports never become rule authority by themselves.

## Source-gap rule

When a required value is absent or ambiguous in the repository:
1. stop that simulation path;
2. name the missing owner/value;
3. do not infer it from sample damage, old memory, or a simulator snapshot;
4. repair/promote the value in the correct repo owner file before resuming.

Current example: Hollow Watch can parse the Castellan, Ballista, Watch Seal, Lv2 party bodies, Crest Knight/Blue Warden actions, Traits, and v93 evidence from the repo, but Maevra's exact Linebreaker definition is not presently available in a current repo owner file. `diysim` therefore reports that source gap rather than storing the recovered external copy.

## Current compatibility layer

The root modules (`core.py`, `rules.py`, `battle.py`, `io.py`) remain temporarily as compatibility entry points while code is migrated section-by-section. New work should go into its owning section rather than enlarging those facades.

## Canon routing

Before parsing or testing a rule, consult:
1. `docs/00_MASTER_CONTROL/`;
2. the owning numbered domain;
3. `docs/90_WORKING/` only for explicitly open/reopened experiments.

For enemy/boss simulation specifically:
- `docs/09_ENEMIES_AND_ENCOUNTERS/` owns current actor/action/AI values;
- `docs/16_BALANCE_AND_TESTING/` owns certification evidence;
- `docs/90_WORKING/` owns unpromoted difficulty experiments.

## Promotion rule

When the simulator is complete and approved, the organized `tools/diysim/` package can be promoted to `main`. Experimental outputs are not automatically promoted into canon owner files.
