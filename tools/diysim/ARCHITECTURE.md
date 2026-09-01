# Diyse Balance Simulator — Section Architecture

`diysim` must mirror Diyse's organized-canon philosophy: every major system and content family gets an explicit home. Do not grow a giant catch-all module or mixed data file.

## Structural rule

- Shared math may live in a small common/core layer.
- Every gameplay subsystem gets its own section.
- Every combat-content family gets its own section.
- Reusable content data and encounter-specific execution logic stay separate.
- Canon owner data and experimental balance overlays stay separate.
- Scenario definitions stay separate from reusable content definitions.
- Reports/results stay separate from inputs and rules.
- A working/sensitivity value must never silently replace owner-canon data.

## Top-level sections

### `combat/`
Owns reusable combat-system mechanics only. Subsystems should remain individually identifiable: damage, hit/evasion, criticals, elements, statuses, temporary modifiers, MP, healing, turn/round sequencing, targeting, Guard/Defend, prepared actions, Fields, Items, Cards, and Primes.

Boss names, chapter checks, support-object state machines, or one-fight AI policies do not belong here.

### `progression/`
Owns Player Level, natural stats, Player EXP, CEXP/Class Level, route projections, encounter-count planning, and completionist/mandatory progression comparisons.

### `content/characters/`
Permanent playable-character combat definitions and current legal class/loadout snapshots.

### `content/guests/`
Temporary/story guest combat definitions such as Maevra. Guest mechanics must not be hidden inside boss scenarios.

### `content/ordinary_enemies/`
Reusable ordinary enemy bodies/actions/AI definitions.

### `content/elites/`
Optional Elite definitions.

### `content/story_bosses/`
Mandatory/story boss reusable bodies, action sheets, phase definitions, AI weights/locks, and boss-local support references.

### `content/regional_hunts/`
Regional Hunt reusable definitions.

### `content/major_hunts/`
Major Hunt reusable definitions.

### `content/support_objects/`
Targetable or acting supports/components such as Ballistae, Seals, Rings, Reservoirs, Anchors, Frames, Nodes, etc. Boss files reference them rather than embedding duplicate bodies.

### `encounters/`
Encounter-specific execution logic only: composed phase/state machines, finite support cycles, authored AI restrictions, scenario-specific player policies, transition handling, and fight-local metrics.

Mirror content families beneath this section when needed, for example:
- `encounters/story_bosses/hollow_watch_castellan/`
- `encounters/regional_hunts/.../`
- `encounters/major_hunts/.../`

An encounter runtime calls reusable `combat/` primitives and references reusable `content/` definitions. It must not reimplement global damage/status math or become a switch statement containing unrelated bosses.

### `scenarios/`
Battle setups: party snapshot, enemy formation, story point, starting HP/MP, legal inventory/loadout, policy, seed/run defaults, and expected regression ranges. Scenario files compose reusable definitions; they do not own canonical actor stats or executable fight logic.

Historical-oracle scenarios and current-canon scenarios must be separate when later canon changes would otherwise make one result ambiguous.

### `overlays/`
Non-destructive balance experiments and sensitivities. Examples: global enemy direct-Power ×1.20, boss +5 effective core-stat levels, HP/ATK/DEF sweeps, local action-density candidates. Overlay data must be labeled WORKING/EXPERIMENTAL and never overwrite owner values.

### `reports/`
Generated/recorded simulation results, regression baselines, comparisons, and certification evidence. Reports never become rule authority by themselves.

## Current compatibility layer

The existing root modules (`core.py`, `rules.py`, `battle.py`, `io.py`) remain temporarily as compatibility entry points while code is migrated section-by-section. New work should be routed into the section that owns it instead of enlarging those files indefinitely.

## Canon routing

Before encoding or changing a rule, consult:
1. `docs/00_MASTER_CONTROL/`;
2. the owning numbered domain;
3. `docs/90_WORKING/` only for explicitly open/reopened experiments.

For enemy/boss simulation specifically:
- `docs/09_ENEMIES_AND_ENCOUNTERS/` owns current actor/action/AI values;
- `docs/16_BALANCE_AND_TESTING/` owns certification evidence;
- `docs/90_WORKING/` owns unpromoted difficulty experiments.

## Promotion rule

When the simulator is complete and approved, the organized `tools/diysim/` package can be promoted to `main`. Experimental overlay outputs are not automatically promoted into canon owner files.
