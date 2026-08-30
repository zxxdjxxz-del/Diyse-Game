# Diyse — Save Data
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## IMPLEMENTED FOUNDATION
Current proof save system:
- JSON
- schema version: **1**
- proof path: `user://diyse_7b5g_save.json`
- version check
- invalid JSON safe failure
- missing-save safe failure
- unknown future schema rejected
- load clears stale transient random-encounter handoff state.

The proof path/name is:
> **not final production naming authority**

## Current schema-v1 serialized fields
Current proof `GameState.to_save_dict()` stores:
- `schema_version`
- `area`
- `field_position`
- `party`
- `inventory`
- `standard_cards`
- `primes`
- `equipment`
- `relic_inventory`
- `forge_components`
- `flags`
- `rewards`

`relic_inventory` and `forge_components` are optional when loading older schema-v1 saves so pre-Kessara v1 proof saves remain compatible.

## Runtime-only transient state
Not serialized:
- `transient_encounter`
- `transient_encounter_return`

Loading a disk save clears them.

This is correct architectural separation.

## Production schema requirement
The final production save must eventually represent current authoritative state including, as applicable:
- current recruited roster;
- active party;
- player Level/EXP;
- Base/Subclass CL/CEXP;
- selected class;
- automatic Mastery unlock state or derivable progress;
- learned Abilities/Traits/Ultimates;
- current Auren;
- Consumables;
- ordinary equipment;
- Relic quantities/copies;
- Legacy ownership/project state;
- Forge/Legacy Components;
- Standard Card ownership/loadouts;
- Prime ownership/state/loadouts/use-independent persistent state;
- quests/Hunts/world flags;
- map/travel unlocks;
- story scene/world-state flags;
- character/quest completion states;
- settings that should persist.

Do not serialize a Mastery Point currency.

## Currency migration
Current proof uses:
> `rewards.gold`

Current canon uses:
> **Auren**

Production schema must migrate/version this safely rather than merely relabeling a stale proof field with no compatibility plan.

## Stable IDs
Persistent content should use stable semantic IDs, not:
- display names;
- final art paths;
- scene-node references.

## Versioning
Any incompatible production schema change must:
- increment schema version;
- provide a deliberate migration/rejection path;
- never silently reinterpret an old field as a different mechanic.
