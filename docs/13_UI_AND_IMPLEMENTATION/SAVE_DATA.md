# Diyse — Save Data

**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.

## IMPLEMENTED FOUNDATION
Current save system:
- JSON;
- current schema version: **3**;
- proof path: `user://diyse_7b5g_save.json`;
- explicit schema migration support from v1 → v2 → v3;
- invalid JSON safe failure;
- missing-save safe failure;
- unknown future schema rejected;
- load clears stale transient random-encounter handoff state.

The proof path/name is:
> **not final production naming authority**

## Current schema-v3 serialized fields
Current `GameState.to_save_dict()` stores:
- `schema_version`;
- `area`;
- `field_position`;
- legacy proof `party`;
- production `character_roster`;
- production `active_party_ids`;
- `inventory`;
- `standard_cards`;
- `primes`;
- `equipment`;
- `relic_inventory`;
- `forge_components`;
- `flags`;
- `rewards`;
- `wallet_g`.

`wallet_g` is the persistent party G balance. It is separate from the legacy proof battle-result payload currently stored under `rewards.gold`.

The old four-entry `party` array remains serialized only while existing proof battle/exploration code depends on it. It is **not** the permanent-roster authority.

## Production permanent-roster state
Schema v3 introduces stable permanent character records for exactly:
- `cyanis` → Cyanis;
- `ilyra` → Ilyra;
- `torren` → Torren;
- `nimera` → Nimera;
- `vaelira` → Vaelira;
- `seyrik` → Seyrik.

Each record currently stores:
- stable `character_id`;
- current first-name-only `display_name`;
- `recruited` state;
- an intentionally empty/extensible `persistent_state` envelope for later owner-domain progression/loadout migration.

Current new-game production baseline:
- Cyanis recruited;
- active party = Cyanis;
- Ilyra, Torren, Nimera, Vaelira and Seyrik exist as stable roster records but are not yet recruited.

Active-party persistence is separate from recruitment state and is capped at:
> **4**

Only recruited permanent characters may be stored in `active_party_ids`; duplicate/unknown IDs are invalid.

## Schema-v1 → v2 migration
Schema v1 had no persistent party wallet.

The migration therefore:
- preserves existing v1 state;
- adds `wallet_g` at the current authoritative starting baseline of **2,500 G** when the old save has no wallet field;
- does **not** reinterpret or convert `rewards.gold` into party G;
- preserves absent pre-Kessara `relic_inventory` / `forge_components` as empty ownership state.

## Schema-v2 → v3 migration
Schema v2 had no production permanent-roster/active-party layer.

The migration therefore:
- preserves the existing four-character proof `party` fixture as legacy proof state;
- creates all six permanent stable character records;
- introduces the canonical Cyanis-only production recruitment/active-party baseline;
- does **not** infer that Ilyra, Torren or Nimera are recruited merely because they happened to exist in the old four-character proof fixture;
- preserves an existing v2 `wallet_g` exactly;
- normalizes the in-memory record to schema v3 before `GameState` applies it.

This is deliberate compatibility behavior for proof saves, not an assertion that the old proof fixture represented campaign recruitment.

## Runtime-only transient state
Not serialized:
- `transient_encounter`;
- `transient_encounter_return`.

Loading a disk save clears them.

This remains the correct architectural separation.

## Production schema requirement
The final production save must eventually represent current authoritative state including, as applicable:
- recruited permanent roster;
- active party;
- player Level/EXP;
- Base/Subclass CL/CEXP;
- selected class;
- automatic Mastery unlock state or derivable progress;
- learned Abilities/Traits/Ultimates;
- persistent **G** wallet;
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

## Currency authority
Current player-facing currency is:
> **G**

Current starting wallet:
> **2,500 G**

Retired player-facing currency:
> **Auren**

The technical proof key `rewards.gold` is not current currency authority and must not be exposed as Gold/Auren or treated as the persistent party wallet.

## Stable IDs
Persistent content should use stable semantic IDs, not:
- display names;
- final art paths;
- scene-node references.

Character display names are normalized from the current stable-ID map on load so stale persisted surname text cannot overrule current identity authority.

## Versioning
Any incompatible production schema change must:
- increment schema version;
- provide a deliberate migration/rejection path;
- never silently reinterpret an old field as a different mechanic.
