# Diyse — Save Data

**Status:** ACTIVE UI / IMPLEMENTATION SPEC
**Authority:** current repository UI/implementation domain; cross-domain gameplay/content rules defer to their current numbered owner domains.

**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## IMPLEMENTED FOUNDATION
Current proof save system:
- JSON
- schema version: **1**
- canonical default path: `user://diyse_save.json`
- compatibility fallback path: `user://diyse_7b5g_save.json`
- version check
- invalid JSON safe failure
- missing-save safe failure
- unknown future schema rejected
- load clears stale transient random-encounter handoff state.

Default load/has-save behavior checks the canonical path first and falls back to the old 7B.5G proof filename only when the canonical file is absent. The next ordinary save writes the canonical path, so legacy proof saves move forward without a schema bump or destructive rename.

The path remains implementation-level naming rather than story/gameplay canon.

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
- current G;
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

## Currency storage

Current runtime/save state uses:
> `rewards.g`

Current player-facing currency is:
> **G**

Schema-v1 compatibility accepts the retired `rewards.gold` key on load and normalizes it to `rewards.g` before the state is re-saved. Reward amounts and economy balance remain independently rebuild-pending; this key migration does not certify old proof values.

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
