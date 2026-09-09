# Diyse Dialogue Engine — Runtime Orchestration

**Status:** ACTIVE CANARY IMPLEMENTATION AUTHORITY  
**Domain:** `03_DIALOGUE/AGENT_SYSTEM`  
**External runtime:** `external-services/canary/`

Generated wording is not canon merely because the canary produced it. Current owning story/character/world/system documents remain authoritative, and production dialogue still requires review/promotion.

---

## 1. Current end-to-end chain

> **Current repository authority → authority compiler → curated live runtime merge → Scene Orchestrator → Dialogue Director → Person Agents → Beat Editor → Canon Checker → Godot handoff → controlled preview/import → human approval → optional story-memory commit**

Static authority and live observation are separate channels:
- `authority_packet` = repository-owned current authority;
- `scene_context.runtime_observable` = curated live/provisional game observations.

Live observations may influence dialogue and staging. They do not rewrite canon.

See:
- `AUTHORITY_PACKET_COMPILER.md`
- `LIVE_RUNTIME_CONTEXT.md`
- `SCENE_CONSTRUCTION_STACK.md`

---

## 2. Repository authority compiler

Tool:
> `tools/dialogue/compile_scene_authority.py`

Input:
> `diyse_scene_authority_spec_v1`

Output authority packet:
> `diyse_scene_authority_packet_v1`

The compiler:
- requires explicit current `02_STORY` sections;
- packages current participant character authority;
- includes current global guardrails and relevant permanent-six relationship authority;
- fingerprints source files/sections, participant profiles, scene spec and bundle;
- rejects working/archive/historical dialogue sources as current scene authority;
- requires explicit current `03_DIALOGUE` proof for any exact-line anchor;
- does not invent runtime state, map facts, encounter pressure or C/V presentation tiers.

A missing requested Markdown heading is fatal rather than permission to widen retrieval.

---

## 3. Curated live-state assembly

Godot files:
- `game/dialogue/dialogue_runtime_context_builder.gd`
- `game/dialogue/dialogue_map_context_provider.gd`
- `game/dialogue/dialogue_scene_request_assembler.gd`

The runtime builder deliberately does **not** serialize raw `GameState`.

Safe automatic GameState capture is currently limited to:
- current area ID;
- field position.

The map-provider contract supplies current observable:
- cell/phase;
- qualitative dialogue readiness;
- location label;
- visible facts;
- route/time context;
- runtime authority status.

Provisional grayboxes/blockouts should identify themselves as `provisional_runtime`.

Encounter capture includes pressure/pause/pending state without exposing formations, reward payloads or implementation calibration.

Raw inventory/equipment/Card/Prime/Relic/Forge/flags/rewards/`gold`/bearer/progression containers are not valid Dialogue Engine runtime context.

Compiled authority fields cannot be overwritten during runtime merge.

---

## 4. Persistent Person Agent

Entry point:
> `external-services/canary/person_agent.py`

Container:
> `external-services/canary/Dockerfile`

Select the deployed person with:
> `CHARACTER_ID=<brain file stem>`

Current service endpoints:
- `GET /health`
- `GET /v1/identity`
- `GET /v1/context-snapshot`
- `POST /v1/turn`
- `POST /v1/commit`
- `POST /v1/open-conversation`

Persistent Person Agents provide:
- current brain synthesis;
- personal story memory;
- current runtime state;
- optimistic story revision;
- character-local knowledge behavior.

YAML brains are runtime synthesis, never independent canon.

Current brain library contains the permanent six plus recurring supporting/major antagonist profiles already synthesized in the repo.

---

## 5. Participant-source rule

Every named participant must have one of:

### Persistent source
A deployed Person Agent listed in `AGENT_URLS_JSON`.

### Profile-only source
A current character profile supplied in:
> `participant_profiles[character_id]`

Profile-only people may speak/react normally but do not silently gain committed persistent memory.

Hard rule:
> The Director may not fabricate a generic NPC voice because a named person's persistent deployment is missing.

---

## 6. Scene Orchestrator

Entry point:
> `external-services/canary/scene_orchestrator.py`

Container:
> `external-services/canary/Dockerfile.orchestrator`

Endpoints:
- `GET /health`
- `POST /v1/scene/build`
- `POST /v1/scene/commit`

A normal build request contains:
- request/scene ID;
- story position;
- canon snapshot;
- participants;
- scene purpose;
- current authority packet;
- participant profiles where needed;
- curated map/recent-gameplay/encounter context;
- current floor/knowledge constraints;
- allowed information transfers;
- required exact-line anchors;
- beat/cost limits.

Unknown facts stay unknown. The request is not padded with invented map/economy/story detail.

---

## 7. Dialogue Director

The Director produces a **beat plan**, not final prose.

It chooses:
- scene mode;
- qualitative readiness;
- movement lock;
- encounter policy;
- staging intent;
- eligible people for each beat;
- whether silence is appropriate;
- what each beat must land/avoid;
- return-to-gameplay behavior.

The Director must treat gameplay context as part of the scene:
- AMBER routes bias shorter;
- RED pursuit cannot become a long camp conversation;
- post-battle/recovery thresholds may earn silence;
- walking dialogue may suppress encounter triggering without resetting accumulated pressure.

---

## 8. Person-Agent candidate pass

For each beat, only Director-selected eligible people are queried.

A Person Agent may return:
- speech;
- visible action;
- silence/nonparticipation;
- uncertainty;
- misunderstanding;
- a question;
- a joke;
- refusal;
- a state-change proposal.

Later candidates see the actual prior drafted beats, so they can react to what really happened in the generated scene rather than an abstract outline.

---

## 9. Beat Editor

The Editor may reshape candidate material for:
- mature spoken rhythm;
- clarity;
- interruption;
- cinematic subtext;
- comedy timing;
- scene economy.

It may not invent substantive character knowledge or canon.

It may move meaning out of dialogue and into staging:
- facing/gesture;
- portrait expression;
- silence;
- camera hold/reframe;
- prop activity;
- light/sound change;
- background activity;
- environment state swap.

---

## 10. Exact-line anchors

Exact anchors are exceptional user-locked wording.

A required anchor must:
- name a participant speaker;
- survive verbatim;
- pass local exact-match checks;
- pass the Canon Checker.

Repository-compiled anchors must also be verified against a cited **current** `03_DIALOGUE` source section. Historical line-complete transcripts cannot silently reacquire exact wording authority.

---

## 11. Canon Checker

The final scene is audited for:
- story requirements;
- forbidden reveals;
- knowledge firewalls;
- stale terminology;
- unsupported local/economic claims;
- participant validity;
- exact anchors;
- no player dialogue choices;
- gameplay legality;
- map/traversal pacing;
- encounter-pressure integrity;
- voice differentiation;
- current HD-2D production ceiling.

A FAIL remains FAIL. It returns violations and cannot silently rewrite itself into PASS.

---

## 12. Memory / commit safety

A successful build never automatically changes story continuity.

On PASS the checker may propose conservative durable memories, such as:
- promise/conflict;
- care received/refused;
- favor;
- joke/callback;
- mistake/correction;
- follow-through;
- relationship shorthand;
- unresolved misunderstanding;
- meaningful observed event.

Do not store every line merely because it occurred.

`POST /v1/scene/commit` requires:
- `author_approved: true`;
- Canon Checker PASS;
- matching canon snapshot;
- expected previous revision for every persistent participant receiving a ledger.

Per-person services retain their own independent snapshot/revision/PASS checks.

---

## 13. Godot build transport

Build-only client:
> `game/dialogue/dialogue_orchestrator_client.gd`

It can send an assembled request to:
> `POST /v1/scene/build`

It validates request snapshot/schema before HTTP and validates response request ID, scene ID, snapshot, checker status and Godot handoff schema afterward.

A Canon Checker FAIL is still a successful transport/build response and is exposed as a rejected authored draft.

The game-side client intentionally provides **no story-memory commit helper**.

Security boundary:
> The client is for canary authoring/preview integration. Do not embed a long-lived service credential in a shipped executable.

---

## 14. Controlled preview/import

Preview controller:
> `game/dialogue/dialogue_scene_preview_controller.gd`

Packet importer:
> `game/dialogue/dialogue_scene_packet_importer.gd`

Field policy bridge:
> `game/dialogue/dialogue_field_bridge.gd`

A build returns:
> `diyse_dialogue_scene_packet_v1`

Preview behavior:
- FAIL → rejected draft, no Dialogue Resource;
- PASS → may be imported into a **temporary** `DiyseDialogueSceneDefinition` using explicit game-side authoring metadata;
- no automatic production save;
- no automatic DialogueRunner start;
- no automatic canon approval;
- no automatic Person-Agent memory commit.

The importer preserves stable IDs/current Resource architecture and does not infer C0–C3/V1–V4 from qualitative production cost.

The field bridge can apply/restore movement and encounter policy once an approved Resource-backed scene is actually run.

---

## 15. Deployment configuration

Person Agent env vars include:
- `CHARACTER_ID`
- `CANON_SNAPSHOT_ID`
- `MODEL_API_URL`
- `MODEL_API_KEY`
- `MODEL_NAME`
- `PERSISTENCE_PATH`
- `SERVICE_AUTH_TOKEN`

Scene Orchestrator env vars include:
- `CANON_SNAPSHOT_ID`
- `MODEL_API_URL`
- `MODEL_API_KEY`
- `MODEL_NAME`
- `ORCHESTRATOR_AUTH_TOKEN`
- `AGENT_AUTH_TOKEN`
- `AGENT_URLS_JSON`

Convenience permanent-six URL variables remain supported; recurring people should use stable IDs through `AGENT_URLS_JSON` when persistent deployment is desired.

---

## 16. Current implementation boundary

Implemented canary chain:
> **current repository authority → deterministic authority packet → curated live map/gameplay/encounter context → multi-agent scene build → Canon Check → validated Godot handoff → temporary current-schema preview → field-policy-ready Resource architecture**

Still separate production work:
- deploy/configure the recurring Person Agents that need persistent continuity;
- attach/update map-context providers across actual production field maps;
- author the production scene-spec library from current story/quest/dialogue authority;
- create reviewed promotion tooling that writes an approved preview into production Dialogue Resources/source control;
- implement the remaining camera/light/sound/field-model staging executor;
- regenerate, review and import all Chapter 0–13 spoken scenes;
- integrate approved external continuity with the production save system.

The architectural rule remains:

> Dialogue is built from the playable scene, living people, living world, map/gameplay rhythm and actual HD-2D production language together—not written in isolation and fitted into the game afterward.
