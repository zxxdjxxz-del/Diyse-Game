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

Detailed compiler and live-runtime contracts are included later in this file.
The Agent System and scene-construction authority now lives in `README.md`.

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
- a safe story-memory **index** for authorization without exposing full private memory content;
- current runtime state;
- optimistic story revision;
- character-local knowledge behavior.

The runtime brain passed to the model includes all current behavioral layers that exist in the YAML, including reasoning, initiative, affection, failure/repair, performance, authority, relationship-expression, register, and self-care progression where defined.

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
- **person_runtime_contexts** for per-character hard context, relationship dimensions, epistemic state, scene-local motive state, open threads, and memory authorization;
- curated map/recent-gameplay/encounter context;
- current floor/knowledge constraints;
- allowed information transfers;
- required exact-line anchors;
- beat/cost limits.

For authored story generation, persistent story memory is **deny-by-default** unless the relevant person's runtime context explicitly authorizes it.

Supported authorization shapes currently include:
- `{"mode":"none"}` — no persistent story memory;
- `{"mode":"explicit_ids","authorized_memory_ids":[...]}` — exact memory IDs;
- `{"mode":"scene_ids","authorized_scene_ids":[...]}` — memories originating in explicitly authorized prior scenes;
- `{"mode":"all_committed_story"}` — compatibility mode for known forward-only authoring only.

Historical rewrites and regeneration passes should **not** use `all_committed_story` because later committed memories may exist.

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
- a route conversation must use an authored stop with movement locked; encounter pressure may be preserved across that stop without resetting.

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

New durable memories should carry enough provenance for later authorization where applicable:
- source scene;
- source story position;
- acquisition mode;
- people present;
- privacy/visibility scope;
- epistemic status at acquisition/current status;
- relationship linkage;
- salience;
- unresolved/open-thread linkage.

Do not store every line merely because it occurred.

Retrieval is explicitly two-stage:
1. authorization;
2. salience.

Relevance is never permission.

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


---

## 17. Repository authority compiler — detailed contract

This section contains the detailed repository-authority compiler contract.

### Purpose

The Scene Orchestrator should not be handed a giant undifferentiated repository dump and asked to decide what is current.

The authority compiler creates a deterministic scene request seed from **explicit current owning sources**. It exists to make the current one-canon / authority-precedence rules operational before any model writes a line.

The chain is:

> current repository authority → deterministic compiler → scene authority packet → live gameplay/state merge → Dialogue Director → Person Agents → Editor → Canon Checker → Godot packet

The compiler is not a story writer and does not decide scene content.

### Hard source rules

The compiler accepts current `docs/` authority only.

It rejects as scene authority:
- `docs/90_WORKING/`;
- `docs/99_ARCHIVE/`;
- `docs/03_DIALOGUE/LINE_COMPLETE/` historical transcripts;
- pre-reorganization `docs/chapters/` paths.

A missing requested Markdown heading is a **fatal compile error**. The compiler does not silently widen retrieval to the whole file.

Historical wording may still be consulted manually as provenance where current policy permits, but it is not allowed to leak into the generated authority packet merely because the current source is shorter.

### What is compiled automatically

Every scene packet receives a bounded current guardrail set covering:
- current master authority state;
- authority precedence / no-silent-resurrection rule;
- current party/chapter/combat/Card/economy terminology;
- story → dialogue handoff / cleanup rule;
- global Dialogue Engine regeneration rule;
- critical implementation-facing overrides.

When at least two permanent party members are present, the current permanent-six relationship map is also included automatically.

For each named participant, the compiler packages that participant's current file from `01_CHARACTERS` as a profile source. The profile is still subordinate to the owning domain and is not a second canon copy.

### Scene spec responsibilities

A scene spec must explicitly name:
- `scene_id`;
- `chapter_id`;
- `story_position`;
- participants;
- scene purpose;
- one or more current `02_STORY` source sections;
- any additional current scene-specific authority needed;
- any static scene-context seed that is genuinely established;
- any allowed information transfers;
- any exact-line anchors that are still explicitly preserved;
- maximum beat count and production-cost ceiling.

A scene spec may also provide protected `person_runtime_contexts` for any participant. This is the preferred authoring surface for:
- persistent-memory authorization;
- relationship runtime dimensions;
- epistemic status for scene-relevant beliefs/claims/suspicions;
- scene-local wants, avoidances, attention, and willingness to speak;
- open relationship/conversation threads;
- other hard per-person constraints that must survive the live-runtime merge.

The compiler emits `memory_authorization: {"mode":"none"}` for participants without an explicit memory policy. Persistent story memory is therefore unavailable by default rather than silently broadening retrieval.

A scene spec may also provide `person_runtime_contexts` for the named participants. This is the preferred authoring surface for:
- memory authorization;
- relationship runtime dimensions;
- epistemic status;
- scene-local wants/avoidances;
- open threads;
- willingness/unwillingness to discuss;
- other hard per-person constraints that should survive live-runtime merge.

The compiler normalizes these by participant and emits `memory_authorization: {"mode":"none"}` for any participant without an explicit policy.

The compiler does **not** infer an old S### mapping from historical line-complete material. If current story authority has not yet mapped a rewritten lean beat to a specific production scene ID, the spec must not pretend that mapping is closed.

### Exact-line anchors

Exact-line anchors are exceptional.

Every exact-line anchor in a spec must:
1. name a participant speaker;
2. provide the literal required text;
3. cite a **current** `03_DIALOGUE` source/section;
4. appear verbatim in that current source.

If the literal line is absent from the cited current source, compilation fails.

This prevents an old historically locked transcript from becoming exact production dialogue merely because a legacy compiler or test still contains it.

### Runtime-state boundary

Repository compilation cannot know live gameplay state.

The compiler deliberately does not invent:
- current HP/MP or injury state;
- fatigue after the player's actual route;
- recent battle sequence;
- current random-encounter pressure;
- exact field position;
- live map-cell state that can vary at runtime;
- current persistent Person-Agent memory/revision;
- C0–C3 cutscene tier;
- V1–V4 VFX tier.

These must be supplied/merged at scene-build time by the game/orchestration layer when relevant.

### Fingerprints

Every compiled source carries:
- repository path;
- full-file SHA-256;
- selected-section SHA-256;
- selected text.

The final authority packet also carries a deterministic bundle SHA-256. The default request ID contains the first 12 characters of that bundle fingerprint.

This does not make a packet permanent authority. It makes stale packets detectable and reviewable.

### Proof fixture

Current deterministic proof:
> `tests/dialogue/fixtures/authority_ch1_brackenwall_protocol.json`

It intentionally uses:
> `PROOF_CH1_BRACKENWALL_PROTOCOL`

rather than asserting an unresolved current S### mapping.

Validation:
> `python3 tests/dialogue/test_scene_authority_compiler.py`

The test verifies current snapshot derivation, exact section extraction, character routing, relationship inclusion, source fingerprints, archive/working/history rejection, missing-heading failure, and current exact-anchor verification.

### Example usage

From repository root:

```bash
python3 tools/dialogue/compile_scene_authority.py \
  tests/dialogue/fixtures/authority_ch1_brackenwall_protocol.json \
  --output /tmp/ch1_brackenwall_authority.json
```

The resulting `request_seed` is shaped for the current `/v1/scene/build` request. Before production submission, merge live runtime state that the scene actually requires and ensure the Orchestrator deployment uses the same `canon_snapshot_id`.

---

## 18. Live runtime context — detailed contract

This section contains the detailed live-runtime context contract.

### Purpose

The repository authority compiler answers:
> What is currently true in Diyse canon for this authored scene?

The live runtime context answers:
> What is observably happening in this particular playthrough at the instant the scene starts?

Those are deliberately separate channels.

A generated scene request therefore has two different sources of truth:
- `authority_packet` — current repository-owned story/character/world/system authority;
- `scene_context.runtime_observable` — curated live/provisional game observations.

Runtime observation can influence dialogue timing, fatigue, map awareness and encounter pacing. It does **not** gain permission to rewrite canon.

### Why raw GameState is forbidden

The current proof `GameState` still contains implementation-era data that is useful for engineering regression but is not safe Dialogue Engine context. Examples include stale Face labels, proof equipment identities, proof Prime/bearer data and an internal `gold` reward key.

Therefore:
> **Never serialize `GameState`, `GameState.to_save_dict()`, or another raw save/state container into a Dialogue Engine request.**

The current builder reads only:
- `current_area`;
- `field_position`.

Everything else must come through an explicitly curated runtime channel.

### Curated runtime sections

#### Field
Captured automatically from the supplied GameState node when available:
- current area ID;
- field position as JSON-safe x/y/z numbers.

This is runtime positioning, not lore authority.

#### Map
Current allowed map-observation fields:
- `cell_id`;
- `area_phase`;
- `dialogue_readiness` (`GREEN`, `AMBER`, `RED`);
- `location_name`;
- `visible_facts`;
- `route_state`;
- `time_context`;
- `context_status`.

Allowed `context_status` values:
- `current_runtime`;
- `provisional_runtime`;
- `observed_runtime`;
- `unknown_runtime`.

The builder adds:
> `authority = runtime_observation_not_story_authority`

For current provisional grayboxes or map blockouts, use `provisional_runtime`. Do not promote their topology to story canon merely because the player is standing inside that engineering scene.

#### Recent gameplay
Current allowed fields:
- `recent_events`;
- `recent_combat_summary`;
- `recovery_state`;
- `fatigue_context`;
- `current_task`.

These should be brief, observable summaries. They are not a route for copying a combat log, inventory dump or author-only analysis into the scene.

#### Interaction
Current allowed fields:
- `movement_enabled`;
- `input_locked`;
- `interaction_id`;
- `interaction_kind`.

#### Encounter pressure
Captured automatically from the supplied field encounter controller when available:
- enabled;
- authored pause state;
- battle-active state;
- context-configured state;
- encounter area ID;
- normalized accumulated pressure;
- transition grace;
- whether an encounter is already pending.

It deliberately does **not** expose formation IDs, pending enemy lists, EXP rewards or implementation calibration such as world-units-per-S.

### Protected compiled fields

Runtime merge may not alter:
- request ID;
- scene ID;
- continuity namespace;
- story position;
- canon snapshot ID;
- participants;
- participant profiles;
- **person runtime contexts**;
- scene purpose;
- authority packet;
- allowed information transfers;
- exact-line anchors;
- maximum beat count;
- production-cost ceiling.

`current_floor_state` is also left untouched by the automatic live merge. It may contain carefully authored knowledge/state constraints, but the runtime builder will not fill it from raw `GameState.flags`.

If `scene_context.runtime_observable` is already present in a compiled request seed, the merge fails. That namespace belongs to the live runtime boundary.

### Raw-state rejection

The runtime input validator rejects raw/state-container keys such as:
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

Unknown top-level/nested fields also fail instead of being silently forwarded.

All caller-supplied runtime values must be JSON-safe. Godot objects/resources/vectors cannot be inserted through the curated input; the builder performs its own explicit Vector3 conversion for field position.

### Canon-snapshot gate

The runtime builder receives the expected deployment/runtime canon snapshot ID.

It rejects the merge if:
- the compiled request has no snapshot;
- the compiled request snapshot differs from the expected runtime snapshot;
- the authority packet snapshot differs from the request seed.

This is an early local guard. The external Orchestrator and Person Agents retain their own snapshot checks.

### Current validation

Headless validation:
> `tests/dialogue/validate_dialogue_runtime_context_builder.gd`

The test deliberately supplies the existing proof `GameState`—including its stale/internal data—and verifies that only the safe area/position subset reaches `runtime_observable`.

It also verifies:
- compiled protected fields cannot be overwritten;
- map observations retain provisional/non-authoritative labeling;
- encounter pressure/grace is merged;
- raw inventory/equipment/Prime/flag/economy fields are rejected;
- snapshot mismatch fails;
- a compiled seed cannot spoof `runtime_observable`.

### Remaining map integration

The builder now provides the safe merge boundary, but each production field/map still needs a small current map-context provider that can identify its live cell/phase/readiness without pretending provisional blockout data is canon.

Until those providers exist, map context is supplied explicitly to the builder through the same validated schema.

The intended production chain is:

> compiled current authority seed → live GameState/encounter capture + current map provider → curated runtime request → external Scene Orchestrator
