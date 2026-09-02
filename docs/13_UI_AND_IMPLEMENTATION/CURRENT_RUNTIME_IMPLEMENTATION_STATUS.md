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
- schema validation.

Current `game/characters/placeholders/` and the proof portrait registry remain **proof-only runtime stand-ins**. Exact production character appearance is controlled by the repository masters under `asset_sources/characters/current/` and the production authority index in `14_ART_AND_VISUALS`.

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

### Persistence
Implemented:
- versioned JSON save manager;
- schema version check;
- safe missing-save failure;
- invalid JSON rejection;
- unsupported future-schema rejection;
- GameState serialization;
- Kessara Relic-copy ownership fields;
- transient random-encounter state excluded from disk save.

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
- retired Resource/Acuity/Change values remain accepted only as compatibility inputs and normalize to Perception/Memory.

Not yet implemented in this service path:
- production **6,000 G** fee debit;
- final service unlock/menu presentation.

The fee amount itself is already closed canon; the missing piece is production currency-state integration and UI/runtime timing.

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
