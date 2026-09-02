# Diyse — Current Runtime Implementation Status
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in the reorganized domains.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.

## IMPLEMENTED FOUNDATION — current repository

### Project/display
`project.godot`
- viewport: **1920×1080**
- window override: 1280×720
- stretch: `canvas_items`
- renderer: GL Compatibility
- mobile renderer: GL Compatibility
- ETC2/ASTC texture compression enabled

### Exploration proof
Implemented:
- CharacterBody3D field movement;
- keyboard arrows / WASD;
- touch D-pad input;
- movement-enable lock;
- interaction proof;
- random-encounter field → combat → field handoff;
- save/load proof;
- dialogue trigger proof.

### Dialogue
Implemented:
- Resource-backed `DiyseDialogueSceneDefinition`;
- stable scene/beat IDs;
- portrait registry indirection;
- left/right portrait slots;
- manual advance;
- true silent beats;
- movement/input lock integration;
- no choice/response architecture;
- schema validation;
- narrow compatibility normalization preventing the retired Acuity/Change Face list from leaking through an older generated line-complete Resource.

Current `game/characters/placeholders/` and the proof portrait registry remain **proof-only runtime stand-ins**. Exact production character appearance is controlled by the repository masters under `asset_sources/characters/current/` and the production authority index in `14_ART_AND_VISUALS`.

### Permanent roster / active party
Implemented production-capable state foundation:
- stable permanent IDs: `cyanis`, `ilyra`, `torren`, `nimera`, `vaelira`, `seyrik`;
- exactly six permanent roster records;
- first-name-only display identities normalized from stable IDs;
- recruitment state separate from active-party membership;
- active-party maximum **4**;
- duplicate, unknown and unrecruited active-party entries rejected;
- current production new-game baseline: Cyanis recruited/active; later permanent characters present but unrecruited;
- reserved per-character `persistent_state` envelope for later progression/loadout migration without inventing final values.

The legacy four-entry `party` array remains in GameState solely for proof battle/exploration compatibility. Its membership and proof HP/MP values are not permanent-roster or final-stat authority.

### Combat proof
The current runtime implements architectural proof for:
- discrete rounds;
- command selection;
- target selection;
- Speed ordering/tie behavior;
- hostile retargeting;
- Standard Card proof;
- Prime direct-control proof;
- field return after generated encounter.

However, its **normal round-control implementation is now legacy proof behavior**, specifically:
- whole-party action selection before resolution;
- round confirmation;
- enemy action locking at round start;
- Item/Defend/ordinary priority sorting.

Current production authority instead uses:
- discrete rounds with Speed-based normal turn order established at round start;
- command/target selection when each player character's turn arrives;
- immediate resolution of that turn before the next normal actor;
- enemy AI decision when the enemy/entity turn arrives;
- no universal Item/Defend priority phases;
- no whole-party queue or Confirm Round requirement.

See `05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md` and `IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md` before production combat implementation.

### Persistence / G wallet
Implemented:
- versioned JSON save manager;
- current schema **v3**;
- deliberate schema-v1 → v2 → v3 migration;
- safe missing-save failure;
- invalid JSON rejection;
- unsupported future-schema rejection;
- GameState serialization;
- persistent `wallet_g` state;
- current starting wallet baseline **2,500 G**;
- wallet credit / affordability / spend operations;
- v1 migration does **not** reinterpret legacy `rewards.gold` as the wallet;
- v2 → v3 migration creates the six-character production roster without inferring recruitment from the old four-character proof party;
- production `character_roster` and `active_party_ids` round-trip through save/load;
- Kessara Relic-copy ownership fields;
- transient random-encounter state excluded from disk save.

The old `rewards.gold` key still exists inside proof battle-result payloads. It is implementation debt isolated from the persistent G wallet and must not become current-facing currency text.

### Kessara Relic-copy service
Implemented service/state logic:
- original Relic required;
- matching Face copy component required;
- max one forged duplicate per individual Relic;
- max quantity 2;
- max 3 forged Relics per Face because exactly 3 copy components exist per Face;
- wrong-Face component rejected;
- Legacies rejected from Relic registration;
- copy uses same Relic identity, not a new item definition;
- current Face set canonicalized as **Might / Elements / Grace / Perception / Memory / Ruin**;
- retired Resource/Acuity/Change values remain accepted only as compatibility inputs and normalize to Perception/Memory;
- exact service fee **6,000 G**;
- insufficient-G rejection without component/item mutation;
- successful fee deduction + component consumption + forged-copy state committed through one GameState transaction;
- invalid/cancelled-equivalent attempts charge **0 G**.

Still not final:
- service unlock/menu timing;
- production confirmation/presentation;
- original-vs-copy visual treatment.

### Current implementation frontier
Next structural state layer:
> **class / Face / per-character loadout state**

This must build on stable permanent character IDs rather than the legacy proof `party` dictionaries and must not restore Mastery Points.

## NOT YET FINAL PRODUCTION UI
The proof repository does not yet establish final:
- main menu;
- party/formation screen;
- full character status screen;
- class/CEXP/Mastery screen;
- production equipment UI;
- Card/Prime loadout UI;
- inventory/material UI;
- quest/Hunt log;
- world-map/travel UI;
- shop/Quartermaster UI;
- production save-slot UI;
- final combat HUD/layout;
- Kessara service menu;
- final Android safe-area/touch layout.

The proof screens demonstrate behavior, not final visual/UX authority.
