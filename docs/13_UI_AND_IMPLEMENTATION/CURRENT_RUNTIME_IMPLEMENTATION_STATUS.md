# Diyse — Current Runtime Implementation Status

**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in the reorganized domains.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are architectural evidence only; they do not restore stale mechanics, names, currencies, progression or UI concepts.

---

## 1. Project / display foundation

`project.godot`
- viewport: **1920×1080**;
- window override: 1280×720;
- stretch: `canvas_items`;
- renderer: GL Compatibility;
- mobile renderer: GL Compatibility;
- ETC2/ASTC texture compression enabled.

Exploration proof currently includes:
- CharacterBody3D field movement;
- keyboard/WASD and touch-D-pad input;
- movement lock;
- interaction proof;
- random-encounter field → combat → field handoff;
- save/load proof;
- dialogue trigger proof.

---

## 2. Dialogue — Godot authored-scene foundation

Implemented:
- Resource-backed `DiyseDialogueSceneDefinition`;
- stable scene/beat IDs;
- portrait registry indirection;
- left/right portrait slots;
- manual advance;
- true silent beats;
- movement/input lock integration;
- no player dialogue-choice architecture;
- schema validation;
- current scene metadata for story position, scene mode, readiness, movement lock, encounter policy, return-to-gameplay and qualitative production-cost tier.

Current dialogue construction/presentation authority:
- `../03_DIALOGUE/AGENT_SYSTEM/SCENE_CONSTRUCTION_STACK.md`
- `../03_DIALOGUE/AGENT_SYSTEM/RUNTIME_ORCHESTRATION.md`
- `../03_DIALOGUE/AGENT_SYSTEM/AUTHORITY_PACKET_COMPILER.md`
- `../03_DIALOGUE/AGENT_SYSTEM/LIVE_RUNTIME_CONTEXT.md`
- `IMPLEMENTATION_NOTES/AREA_TRAVERSAL_AUTHORING_INTERFACE.md`
- `DIALOGUE_UI.md`

---

## 3. Repository authority → scene request

### Static authority compiler

Implemented:
> `tools/dialogue/compile_scene_authority.py`

Input schema:
> `diyse_scene_authority_spec_v1`

Output authority schema:
> `diyse_scene_authority_packet_v1`

Current behavior:
- derives canon snapshot from current `CURRENT_CANON_STATUS.md`;
- requires explicit current `02_STORY` source sections;
- packages current participant character files as profile sources;
- automatically includes permanent-six relationship authority when relevant;
- automatically includes bounded current master/terminology/dialogue-handoff guardrails;
- extracts exact Markdown sections rather than dumping whole source files by default;
- missing or ambiguous requested headings are fatal;
- rejects `90_WORKING`, `99_ARCHIVE`, historical `03_DIALOGUE/LINE_COMPLETE`, old `docs/chapters/`, and the historical exact-source manifest as current scene authority;
- exact-line anchors require current `03_DIALOGUE` proof and literal verbatim match;
- fingerprints selected sections, source files, participant profiles, scene spec and final authority bundle with SHA-256;
- never invents live gameplay state or C0–C3 / V1–V4 presentation tiers.

Proof fixture:
> `tests/dialogue/fixtures/authority_ch1_brackenwall_protocol.json`

Validation:
> `tests/dialogue/test_scene_authority_compiler.py`

The Chapter-1 fixture deliberately uses `PROOF_CH1_BRACKENWALL_PROTOCOL` rather than guessing a current S### mapping that has not been explicitly promoted in lean story authority.

---

## 4. Compiled authority → curated live runtime request

### Runtime context builder

Implemented:
> `game/dialogue/dialogue_runtime_context_builder.gd`

Runtime schema:
> `diyse_dialogue_runtime_context_v1`

Hard boundary:
> Raw `GameState` is never serialized into Dialogue Engine context.

The current proof GameState still contains implementation-era/stale fields, so the builder reads only:
- current area ID;
- field position.

Curated caller-supplied runtime context is whitelisted for:
- map/cell/phase/readiness observations;
- recent gameplay summaries;
- interaction/movement state.

Encounter capture is reduced to:
- enabled state;
- authored pause state;
- battle-active/context-configured state;
- area ID;
- normalized accumulated pressure;
- transition grace;
- pending-encounter state.

It deliberately excludes formations, enemy lists, reward payloads and implementation calibration.

Explicitly rejected from live dialogue context:
- inventory;
- equipment;
- Standard Card container;
- Prime container;
- Relic inventory;
- Forge Components;
- flags;
- rewards;
- `gold`;
- proof bearer/progression internals.

Compiled protected fields—including authority packet, scene ID, participants, exact anchors and canon snapshot—cannot be overwritten during live merge.

### Map provider contract

Implemented:
> `game/dialogue/dialogue_map_context_provider.gd`

A map may expose only its current observable dialogue context. Runtime map observations are labeled as non-canon authority and can explicitly use `provisional_runtime` for grayboxes/blockouts.

### Request assembler

Implemented:
> `game/dialogue/dialogue_scene_request_assembler.gd`

Current chain:
> compiled scene seed + map provider + safe GameState area/position + recent gameplay + encounter controller → final `/v1/scene/build` request

Validation:
- `tests/dialogue/validate_dialogue_runtime_context_builder.gd`
- `tests/dialogue/validate_dialogue_scene_request_assembler.gd`

Current remaining map work:
- production field maps still need to attach/update the standard provider with their current cell/phase/readiness data;
- the existing Chapter-0 graybox remains provisional and must not become story authority merely because it supplies runtime observations.

---

## 5. External Dialogue Engine canary

Runtime root:
> `external-services/canary/`

### Generic persistent Person Agent

Current entrypoint:
> `person_agent.py`

Implemented:
- brain-file-driven `CHARACTER_ID`;
- runtime discovery of YAML brains;
- persistent story memory/state per deployed person service;
- separate open-conversation continuity;
- optimistic story revision;
- Canon Checker PASS commit requirement;
- canon-snapshot mismatch rejection;
- `GET /v1/context-snapshot`;
- arbitrary scene context;
- automatic shared-context loading.

Current brain library contains **20 runtime syntheses**:
- permanent six: Cyanis, Ilyra, Torren, Nimera, Vaelira, Seyrik;
- recurring supporting: Maevra, Kessara, Talia, Edda, Mirena, Lysara, Alaric, Nalia;
- major antagonists: Othmar, Rhazek, Zevraya, Varkesh, Vaelkor, Reconstituted Entity / The Last Command.

A packaged brain is runtime synthesis only. It does not mean a persistent service is deployed, and it never outranks its current character authority file.

### Scene Orchestrator

Current entrypoint:
> `scene_orchestrator.py`

Pipeline:
> **Scene Job → Dialogue Director → Person-Agent candidates → Beat Editor → Canon Checker → Godot handoff → explicit author-approved commit**

Implemented:
- Director receives story purpose, participants, current authority packet, map/cell/traversal state, recent gameplay, encounter pressure, lived-world/economy context, readiness, exact anchors, HD-2D staging context and production ceiling;
- Director creates beat plan rather than final prose;
- only selected eligible people are queried per beat;
- later candidates see actual prior drafted beats;
- silence/nonparticipation are valid;
- Editor lightly shapes wording without permission to invent substantive canon;
- Canon Checker audits story/reveal/knowledge/map/gameplay/voice/cost constraints;
- FAIL remains FAIL and returns violations;
- PASS may propose conservative durable memory;
- build never automatically commits continuity;
- `/v1/scene/commit` requires explicit `author_approved: true`, PASS, matching snapshot and expected prior revisions;
- build returns `diyse_dialogue_scene_packet_v1`.

Named participants must have either:
1. a configured persistent Person Agent; or
2. an explicit current profile supplied in the request.

The Director may not invent a generic NPC voice because a deployment is missing.

---

## 6. Godot ↔ external build canary

### Build-only Orchestrator client

Implemented:
> `game/dialogue/dialogue_orchestrator_client.gd`

Purpose:
- canary authoring/preview integration with `POST /v1/scene/build`;
- not a shipping-story-memory client.

Current behavior:
- validates assembled request and canon snapshot before HTTP;
- validates runtime-context schema when present;
- HTTPS required except localhost HTTP for development;
- optional bearer auth supplied at runtime;
- auth token is not serialized into request body;
- prevents simultaneous builds through one `HTTPRequest`;
- validates response request ID, scene ID, canon snapshot, Canon Checker status and Godot handoff schema;
- Canon Checker FAIL is a valid authored build result, not a transport failure;
- intentionally has no `/v1/scene/commit` helper.

Validation:
> `tests/dialogue/validate_dialogue_orchestrator_client.gd`

Security rule:
> Do not embed a long-lived service credential in a shipped game executable. This client is a canary authoring/preview bridge unless a later deployment architecture explicitly changes that rule.

### Controlled preview gate

Implemented:
> `game/dialogue/dialogue_scene_preview_controller.gd`

Behavior:
- accepts a validated external build plus explicit game-side authoring metadata;
- requires participant metadata to match the assembled request;
- Canon Checker FAIL becomes preview rejection and produces no Dialogue Resource;
- Canon Checker PASS may be translated through the current packet importer into a temporary `DiyseDialogueSceneDefinition`;
- current no-choice/schema/portrait/presentation validation still applies;
- preview does **not** save the Resource into production content;
- preview does **not** start the DialogueRunner automatically;
- preview does **not** mark wording approved/canon;
- preview does **not** commit Person-Agent memory.

Validation:
> `tests/dialogue/validate_dialogue_scene_preview_controller.gd`

---

## 7. Godot packet import / field policy

Implemented:
- `game/dialogue/dialogue_scene_packet_importer.gd` converts `diyse_dialogue_scene_packet_v1` + explicit authoring metadata into `DiyseDialogueSceneDefinition`;
- `game/dialogue/dialogue_field_bridge.gd` applies/restores movement and encounter policy when a Resource-backed scene runs;
- walking dialogue may suppress encounter triggering without resetting accumulated pressure;
- movement/encounter pause state is restored to its exact pre-scene value.

The importer does **not** infer C0–C3 / V1–V4 from economical/moderate/bespoke.

Validation:
- `tests/dialogue/validate_scene_packet_importer.gd`
- `tests/dialogue/validate_dialogue_field_bridge.gd`

Still incomplete:
- final production staging executor for all camera/light/sound/field-model cue families;
- mass regeneration/approval/import of Chapter 0–13 production dialogue;
- approved external dialogue-memory integration with the production save system.

---

## 8. Combat / persistence proof status

Combat proof still demonstrates architecture for rounds, command/target selection, Speed ordering, hostile retargeting, Standard Cards, Prime direct-control and field return.

Its normal round-control flow remains legacy proof behavior in places. Current production battle authority is in:
> `../05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`

and implementation divergences are tracked in:
> `IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`

Persistence proof includes:
- versioned JSON saves;
- schema checks;
- invalid/future save rejection;
- GameState serialization;
- Kessara Relic-copy ownership fields;
- transient random-encounter state excluded from disk saves.

External Person-Agent SQLite continuity remains separate from the production game save.

---

## 9. Current CI caveat

All new Dialogue Engine validators are listed in:
> `.github/workflows/godot-smoke.yml`

Recent hosted `Godot Smoke Validation` jobs are still failing **before any workflow steps start** and report no executed steps/runner details. The latest checked run after the new build client showed the same pre-step failure.

Therefore:
- repository presence/wiring of the validators is verified;
- a fresh successful hosted execution result is **not** currently available;
- do not interpret the Actions failure as a discovered GDScript test failure because no test step is being launched.

---

## 10. Not yet final production delivery

Still open:
- final main menu / party / status / class / equipment / Card / inventory / quest / world-map / shop / save-slot / combat HUD UI;
- final Android safe-area/touch layout;
- persistent deployment topology for the recurring Person Agents that should retain story memory;
- production scene-spec library mapping every current story/Character-Life/Hunt/dialogue scene to exact active authority sections;
- production map-provider feeds across actual field maps;
- author-approved promotion tooling that writes reviewed preview output into production Dialogue Resources without bypassing source control/review;
- final staging executor for generated camera/light/sound/model cues;
- regeneration, approval and import of all Chapter 0–13 spoken scenes;
- production integration of approved Person-Agent continuity with the main save system.

The current repository now demonstrates the complete **authoring canary chain** from current repository authority through curated live game context, multi-agent generation, Canon Check, Godot transport, temporary preview import and field-policy plumbing. It does **not** mean generated dialogue has been automatically promoted to shipping canon.
