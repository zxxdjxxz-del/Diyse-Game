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

### Dialogue — Godot proof
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

Current dialogue authoring/presentation interface additionally requires:
- current map/traversal context;
- dialogue-safe traversal pacing;
- environmental-read windows;
- current B00 rigged-field-model staging where relevant;
- portrait/camera/light/sound/state cues as shared performance tools.

See:
- `../03_DIALOGUE/AGENT_SYSTEM/SCENE_CONSTRUCTION_STACK.md`
- `../03_DIALOGUE/AGENT_SYSTEM/RUNTIME_ORCHESTRATION.md`
- `IMPLEMENTATION_NOTES/AREA_TRAVERSAL_AUTHORING_INTERFACE.md`
- `DIALOGUE_UI.md`

### Dialogue Engine packet → Godot bridge
Implemented:
- `game/dialogue/dialogue_scene_packet_importer.gd` validates `diyse_dialogue_scene_packet_v1` and converts an approved generated packet plus game-side authoring metadata into `DiyseDialogueSceneDefinition`;
- imported Resources preserve story position, scene mode, dialogue readiness, movement-lock intent, encounter policy, return-to-gameplay metadata, production-cost tier and beat staging cues;
- packet validation rejects player dialogue-choice/branch fields rather than silently dropping them;
- importer does **not** infer C0–C3 or V1–V4 presentation tiers from economical/moderate/bespoke authoring cost labels; those tiers remain explicit game-side authority;
- `game/dialogue/dialogue_field_bridge.gd` applies authored field policy when a Resource-backed scene starts and restores prior field policy when it ends;
- stop scenes may lock player movement;
- authored dialogue may temporarily suppress random-encounter triggering without resetting accumulated encounter pressure;
- movement/encounter pause state is restored to its exact pre-scene value rather than blindly enabling it;
- `tests/dialogue/validate_scene_packet_importer.gd` and `tests/dialogue/validate_dialogue_field_bridge.gd` provide headless validation fixtures;
- both validators are included in `.github/workflows/godot-smoke.yml`.

Still incomplete on the Godot delivery side:
- camera/light/sound/field-model staging cues are carried through the packet/Resource and emitted by the runner, but a final production staging executor does not yet consume every cue family;
- generated packets are not yet mass-imported into final Chapter 0–13 production Resources;
- the external dialogue-memory store is not yet integrated into the main save system.

### External Dialogue Engine canary
`external-services/canary/`

#### Generic persistent Person Agent
Current active canary entrypoint:
> `person_agent.py`

Container:
> `Dockerfile`

Implemented:
- brain-file-driven character selection through `CHARACTER_ID`;
- no hard-coded permanent-six runtime ceiling;
- runtime discovery of all YAML brains packaged in `brains/`;
- persistent story memory/state store per deployed person service;
- separate open-conversation continuity;
- story revision / optimistic commit gate;
- Canon Checker PASS requirement for story commits;
- canon-snapshot mismatch rejection;
- `GET /v1/context-snapshot` for safe orchestration revision/state reads;
- arbitrary current `scene_context` on authored turns;
- automatic loading of all shared YAML contexts at startup;
- shared world/economy/dialogue/scene-construction context in every Person-Agent call.

Current runtime brain library includes **20 current person syntheses**:

Permanent six:
- Cyanis
- Ilyra
- Torren
- Nimera
- Vaelira
- Seyrik

Recurring supporting:
- Maevra
- Kessara
- Talia
- Edda
- Mirena
- Lysara
- Alaric
- Nalia

Major antagonists:
- Othmar
- Rhazek
- Zevraya
- Varkesh
- Vaelkor
- Reconstituted Entity / The Last Command

A brain being packaged does not mean a separate persistent service has already been deployed for that person. Persistence requires a Person Agent deployment configured with that brain ID.

#### Scene Orchestrator
Current active canary entrypoint:
> `scene_orchestrator.py`

Container:
> `Dockerfile.orchestrator`

Implemented pipeline:
> **Scene Job → Dialogue Director → Person-Agent candidates → Beat Editor → Canon Checker → Godot handoff → explicit author-approved commit**

Implemented orchestration behavior:
- Director receives story purpose, participants, current authority packet, map/cell/traversal state, recent gameplay, encounter pressure, lived-world/economy context, dialogue readiness, exact-line anchors, HD-2D staging context, and production-cost ceiling;
- Director creates beat plan rather than final prose;
- only selected eligible people are queried per beat;
- later Person-Agent candidates see the actual prior drafted beats;
- silence/nonparticipation are valid candidate outcomes;
- Editor lightly shapes selected candidates for mature spoken rhythm, cinematic subtext, comedy timing, anime-readable performance and scene economy without permission to invent substantive canon;
- local hard checks validate required exact-line anchors and participant identity;
- Canon Checker audits knowledge firewall, story requirements, local/economic claims, gameplay legality, traversal/encounter compatibility, voice differentiation and production ceiling;
- a FAIL returns violations and is not silently rewritten into a PASS;
- a PASS may produce conservative durable-memory ledgers for persistent participants;
- build does not automatically commit continuity;
- `/v1/scene/commit` requires explicit `author_approved: true`, Canon Checker PASS, matching canon snapshot and expected prior revision per persistent person;
- build returns `diyse_dialogue_scene_packet_v1` as a Godot-facing authoring handoff.

#### Persistent and profile-only participants
The Orchestrator now supports two person sources:

1. **Persistent Person Agent** — configured through `AGENT_URLS_JSON` and backed by a brain, memory and current state.
2. **Profile-only Person Agent** — scene request supplies current `participant_profiles` for a named person who is not yet deployed persistently.

Hard rule:
> a named participant must have a real person source; the Director may not silently invent a generic NPC voice because no deployed agent exists.

Profile-only memory is proposal-only and is not automatically committed.

#### Shared scene context
Current shared context includes:
- lived world;
- lived economy;
- dialogue life/craft;
- unified scene construction.

The unified scene-construction context tells Director/agents/editor/checker to account for:
- map cell and area phase;
- recent exploration/combat;
- encounter pressure and recovery;
- dialogue readiness;
- what the environment already communicates visually;
- mature-adult naturalism;
- comedy timing;
- cinematic subtext;
- anime-readable expression;
- current B00 rigged-model + portrait staging;
- economical HD-2D production cost.

Important boundary:
- shared runtime context is synthesis, not canon authority;
- it cannot invent a map condition, shortage, price, character preference, story fact, or numerical pacing target that current owning sources have not established;
- exact ongoing area-study minute/count targets remain research-only unless separately locked.

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

See `../05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md` and `IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md` before production combat implementation.

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

Dialogue-agent persistence is currently external SQLite per deployed Person Agent and remains separate from the Godot save proof until a production persistence handoff is explicitly designed.

### Kessara Relic-copy service
Implemented service logic:
- original Relic required;
- matching Face copy component required;
- max one forged duplicate per individual Relic;
- max quantity 2;
- max 3 forged Relics per Face because exactly 3 copy components exist per Face;
- wrong-Face component rejected;
- Legacies rejected from Relic registration;
- copy uses same Relic identity, not a new item definition.

## NOT YET FINAL PRODUCTION UI / DIALOGUE DELIVERY
The repository still does not establish final:
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
- final Android safe-area/touch layout;
- production deployment topology for every recurring Person Agent;
- automatic repository-to-scene authority-packet compiler;
- production staging executor for every generated camera/light/sound/model cue family;
- regeneration/approval/import of every Chapter 0–13 spoken scene;
- production integration of external Person-Agent memory with the main save system.

The proof screens and current Dialogue Engine canary now demonstrate a real multi-agent authoring/orchestration implementation, but they do **not** mean the entire game's dialogue has already been regenerated, approved, imported and shipped.
