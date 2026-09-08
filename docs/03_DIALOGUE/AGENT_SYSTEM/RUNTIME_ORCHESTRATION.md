# Diyse Dialogue Engine — Runtime Orchestration

**Status:** ACTIVE CANARY IMPLEMENTATION AUTHORITY  
**Domain:** `03_DIALOGUE/AGENT_SYSTEM`  
**Runtime:** `external-services/canary/`

This document defines how the current canary turns the Dialogue Engine design into a scene-building service.
It does not make generated wording canon by itself. Current owning story/character/world/system documents remain authoritative.

---

## 1. Runtime flow

The current scene pipeline is:

> **Scene Job → Dialogue Director → Person Agents → Beat Editor → Canon Checker → Godot Handoff → Human Approval → Story-Memory Commit**

The Director, Person Agents, Editor and Canon Checker all receive the unified scene-construction context rather than operating as isolated prose generators.

The Director must reason from:
- story position and required/forbidden information;
- people present;
- map/sub-area/cell role;
- recent gameplay;
- encounter pressure and recovery state;
- lived-world/economic context actually established;
- dialogue readiness;
- economical HD-2D staging;
- production-cost ceiling.

Person Agents receive the Director beat target plus observable scene history, so later dialogue can respond to what actually happened in earlier beats.

---

## 2. Runtime files

### Persistent Person Agent
`external-services/canary/person_agent.py`

A single generic service implementation hosts any YAML brain present in:
`external-services/canary/brains/`

Select the person with:
`CHARACTER_ID=<brain file stem>`

The service discovers brain IDs at runtime rather than hard-coding the permanent six.

It exposes:
- `GET /health`
- `GET /v1/identity`
- `GET /v1/context-snapshot`
- `POST /v1/turn`
- `POST /v1/commit`
- `POST /v1/open-conversation`

`/v1/context-snapshot` supplies the orchestration layer with the current story revision and public runtime state needed for safe optimistic commits.

### Scene Orchestrator
`external-services/canary/scene_orchestrator.py`

It exposes:
- `GET /health`
- `POST /v1/scene/build`
- `POST /v1/scene/commit`

Container target:
`external-services/canary/Dockerfile.orchestrator`

---

## 3. Participant sources

Every speaking/materially reacting person must have a current person source.

### A. Persistent source
Preferred for recurring people whose continuity should survive across scenes.

The Orchestrator calls that person's deployed Person Agent through an entry in `AGENT_URLS_JSON`.

Example conceptual mapping:
```json
{
  "cyanis": "https://...",
  "maevra": "https://...",
  "othmar": "https://..."
}
```

A persistent source provides:
- current approved brain synthesis;
- personal story memory;
- current runtime state;
- optimistic story revision;
- character-local knowledge behavior.

### B. Profile-only source
Fallback for a person who has current character authority but no deployed persistent service yet.

The scene request supplies:
`participant_profiles[character_id]`

The Orchestrator runs that profile through the same Person-Agent behavior contract for the current scene.

Profile-only participants:
- may speak/react normally;
- must obey the same knowledge firewall and scene grammar;
- do **not** gain silently committed persistent memory;
- return memory proposals separately if the Canon Checker believes durable continuity should later be promoted.

### Hard rule
The Director may not invent a generic NPC voice for a named participant merely because no persistent deployment exists.
A named participant must have either:
- a configured persistent agent; or
- an explicit current profile supplied to the scene job.

---

## 4. Current brain library

The canary brain library now contains runtime synthesis for the permanent six plus recurring supporting/antagonist people already deep-characterized in current authority.

Permanent six:
- `cyanis`
- `ilyra`
- `torren`
- `nimera`
- `vaelira`
- `seyrik`

Recurring supporting set currently synthesized:
- `maevra`
- `kessara`
- `talia`
- `edda`
- `mirena`
- `lysara`
- `alaric`
- `nalia`

Major antagonist set currently synthesized:
- `othmar`
- `rhazek`
- `zevraya`
- `varkesh`
- `vaelkor`
- `reconstituted_entity`

A YAML brain remains **runtime synthesis**, not independent canon. If it conflicts with its `source_authority`, the source authority wins and the brain must be regenerated.

Prince Consort Cassian and one-off/minor NPCs remain profile-fallback candidates until sufficient current character authority justifies a persistent brain.

---

## 5. Scene-build contract

`POST /v1/scene/build` receives a scene job containing, at minimum:
- request ID;
- scene ID;
- story position;
- canon snapshot ID;
- participants;
- scene purpose.

Normal authored requests should also include:
- current story/scene authority packet;
- participant profiles for any non-deployed named people;
- location/sub-area/cell role;
- entry/exit context;
- recent gameplay;
- encounter pressure;
- current world-life conditions that are actually established;
- allowed information transfers;
- any required exact-line anchors;
- production-cost ceiling.

Unknown map/economy/story facts should remain unknown/open rather than being fabricated to fill the packet.

---

## 6. Director behavior

The Director outputs a beat plan rather than final dialogue.

It chooses:
- scene mode;
- qualitative dialogue readiness;
- movement lock;
- encounter policy;
- staging tier;
- which people are eligible to participate in each beat;
- whether silence is appropriate;
- what each beat must land/avoid;
- return-to-gameplay behavior.

The Director is specifically prevented from treating physical map/play state as incidental.

Examples:
- an AMBER active route should bias toward shorter exchanges;
- a RED pursuit should not become a five-minute camp conversation;
- a story-bearing cell can use one short environmental observation instead of a full stop scene;
- a post-boss recovery threshold may earn silence before the next objective;
- walking dialogue may temporarily suppress encounter triggering without resetting encounter pressure.

---

## 7. Person-Agent candidate pass

For each beat, the Orchestrator asks only the Director-selected eligible people for candidate behavior.

A Person Agent may return:
- speech;
- visible action;
- silence/nonparticipation;
- uncertainty;
- misunderstanding;
- question;
- joke;
- refusal;
- state-change proposal.

The Person Agent is not required to speak because the Director asked it for a candidate.

Each candidate must remain grounded in:
- the person's brain/profile;
- personal continuity if persistent;
- current state;
- observable prior beats;
- current scene context;
- allowed knowledge transfers.

---

## 8. Dialogue Editor

The Beat Editor selects the candidate that best serves the beat.

It may lightly reshape wording for:
- mature spoken rhythm;
- clarity;
- interruption;
- cinematic subtext;
- comedy timing;
- scene economy.

It may not invent substantive character knowledge or new canon to make a line prettier.

The Editor is also responsible for turning some meaning into staging rather than speech:
- field-model facing;
- a small gesture;
- portrait expression;
- silence;
- camera hold/reframe;
- prop action;
- light/sound change;
- background activity;
- environment state swap.

---

## 9. Exact-line anchors

`exact_line_anchors` are explicit user-locked wording only.

A required anchor must:
- use the named speaker;
- survive verbatim;
- pass the local exact-match check;
- pass the Canon Checker.

The rest of the scene remains free to regenerate around it unless separately locked.

---

## 10. Canon Checker

The Canon Checker audits the assembled scene after all beats exist.

It checks:
- current story requirements;
- forbidden reveals;
- knowledge firewalls;
- stale terminology;
- unsupported local/economic claims;
- participant validity;
- exact-line anchors;
- no player dialogue choices;
- gameplay legality;
- map/traversal pacing;
- encounter-pressure integrity;
- mature/natural voice differentiation;
- current HD-2D production ceiling.

A FAIL does not silently rewrite itself into a PASS.
The failed beat/scene returns violations for regeneration or human revision.

---

## 11. Memory and state safety

A successful build does **not** automatically modify story continuity.

On PASS, the Canon Checker may produce conservative durable-memory ledgers for persistent participants.
These should contain only things the character could plausibly retain, such as:
- promise;
- conflict;
- care received/refused;
- practical favor;
- joke/callback;
- mistake/correction;
- follow-through;
- relationship shorthand;
- unresolved misunderstanding;
- mundane continuity worth retaining;
- meaningful observed event.

Do not store every line merely because it happened.

State changes remain proposals rather than automatic whole-state replacement during scene build.

---

## 12. Explicit commit gate

`POST /v1/scene/commit` requires:
- `author_approved: true`;
- Canon Checker `PASS`;
- matching canon snapshot;
- expected previous revision for every persistent participant receiving a memory ledger.

The per-person Person Agent still independently rejects:
- non-PASS commits;
- snapshot mismatch;
- stale expected revision.

This keeps sandbox/draft generation from silently changing story continuity.

---

## 13. Godot handoff

A PASS or FAIL build returns a `godot_handoff` packet using:
`diyse_dialogue_scene_packet_v1`

The packet contains:
- scene ID;
- story position;
- scene mode;
- movement lock;
- dialogue readiness;
- production-cost tier;
- encounter policy;
- ordered beats;
- speaker ID;
- body text;
- true silent beat support;
- action;
- expression ID slot;
- portrait-side slot;
- staging cues;
- return-to-gameplay behavior.

This packet is the authoring/runtime bridge. It is not permission to bypass the current `DiyseDialogueSceneDefinition`/stable-ID production architecture. A later Godot importer should translate the packet into the current production Resource schema rather than hard-code asset paths.

---

## 14. Deployment configuration

Person Agent container:
`external-services/canary/Dockerfile`

Important env vars:
- `CHARACTER_ID`
- `CANON_SNAPSHOT_ID`
- `MODEL_API_URL`
- `MODEL_API_KEY`
- `MODEL_NAME`
- `PERSISTENCE_PATH`
- `SERVICE_AUTH_TOKEN`

Scene Orchestrator container:
`external-services/canary/Dockerfile.orchestrator`

Important env vars:
- `CANON_SNAPSHOT_ID`
- `MODEL_API_URL`
- `MODEL_API_KEY`
- `MODEL_NAME`
- `ORCHESTRATOR_AUTH_TOKEN`
- `AGENT_AUTH_TOKEN`
- `AGENT_URLS_JSON`

Convenience permanent-six URL vars are also accepted:
- `CYANIS_AGENT_URL`
- `ILYRA_AGENT_URL`
- `TORREN_AGENT_URL`
- `NIMERA_AGENT_URL`
- `VAELIRA_AGENT_URL`
- `SEYRIK_AGENT_URL`

For recurring supporting/antagonist persistence, use `AGENT_URLS_JSON` with their stable brain IDs.

---

## 15. Current implementation boundary

This is a canary authoring/runtime architecture, not a claim that every story scene has already been regenerated and imported into Godot.

Still separate work:
- deploy/configure the desired recurring Person Agent services;
- build the Godot `diyse_dialogue_scene_packet_v1` importer/validator;
- author concrete per-scene authority packets from current `02_STORY` and map designs;
- regenerate and approve Chapters 0–13 spoken scenes;
- persist only approved story continuity.

The important architectural lock is now in place:

> Dialogue is built from the playable scene, the living people, the living world, the map/gameplay rhythm, and the actual HD-2D production language together—not written in isolation and fitted into the game afterward.
