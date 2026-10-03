# Diyse Dialogue Engine Canary

This directory contains the current external Dialogue Engine canary.

## Services

### Person Agent
Entrypoint: `person_agent.py`  
Container: `Dockerfile`

The same code hosts any character brain in `brains/`.
Set:

```text
CHARACTER_ID=cyanis
```

or another brain-file stem.

The Person Agent owns character-local runtime memory/state only. Character canon remains in `docs/01_CHARACTERS/` and other owning domains.

Endpoints:
- `GET /health`
- `GET /v1/identity`
- `GET /v1/context-snapshot`
- `POST /v1/runtime-context` — reconstruct a person-local, chronology-safe context without a model call
- `POST /v1/turn`
- `POST /v1/commit`
- `POST /v1/open-conversation`

### Scene Orchestrator
Entrypoint: `scene_orchestrator.py`  
Container: `Dockerfile.orchestrator`

Endpoints:
- `GET /health`
- `POST /v1/scene/build`
- `POST /v1/scene/commit`

The Orchestrator runs:

> Director → Person-Agent candidate pass → beat Editor → Canon Checker → Godot handoff

A successful build does not automatically write story continuity. `/v1/scene/commit` requires explicit author approval plus a Canon Checker PASS and matching per-agent story revisions.

## Shared context

Every Person Agent loads all YAML files in `context/`:
- `world_life.yaml`
- `magic_and_cards.yaml`
- `economy.yaml`
- `dialogue_system.yaml`
- `naming.yaml`

This is the runtime synthesis that makes dialogue account for character life, lived magical/Card normality, the Prime knowledge firewall, world/economy pressure, map/traversal context, recent gameplay, comedy/cinematic/anime performance rules, and economical HD-2D staging together. `dialogue_system.yaml` combines the shared dialogue-life and scene-construction layers so they cannot drift apart.

## Persistent vs profile-only people

The Orchestrator can source a person in two ways.

**Persistent:** configure an agent URL in `AGENT_URLS_JSON`. This person receives their deployed brain plus committed personal memory/state.

**Profile-only:** pass `participant_profiles` in the scene request. This supports a named current-canon person who has not been deployed as a persistent service yet. Profile-only memories are proposals and are never silently committed.

The Director is not allowed to invent a generic voice for a named participant with no person source.

## Brain library

Current brain IDs include:

Permanent six:
`cyanis`, `ilyra`, `torren`, `nimera`, `vaelira`, `seyrik`

Recurring supporting:
`maevra`, `kessara`, `talia`, `edda`, `mirena`, `lysara`, `alaric`, `nalia`

Major antagonists:
`othmar`, `rhazek`, `zevraya`, `varkesh`, `vaelkor`, `reconstituted_entity`

Each brain identifies its current source-authority document. The source document wins on conflict.

## Core environment variables

Both services use:
- `CANON_SNAPSHOT_ID`
- `MODEL_API_URL`
- `MODEL_API_KEY`
- `MODEL_NAME`
- `SERVICE_VERSION` (optional version metadata override)

Person Agent:
- `CHARACTER_ID`
- `BRAIN_PROFILE_VERSION` (optional brain-profile version metadata override)
- `PERSISTENCE_PATH`
- `SERVICE_AUTH_TOKEN`
- `PORT` (default 8080)

Scene Orchestrator:
- `ORCHESTRATOR_AUTH_TOKEN`
- `AGENT_AUTH_TOKEN`
- `AGENT_URLS_JSON`
- `PORT` (default 8090)

The Orchestrator also accepts convenience permanent-six URL variables such as `CYANIS_AGENT_URL`.

## Canon / implementation docs

See:
- `docs/03_DIALOGUE/AGENT_SYSTEM/README.md` — Agent Brain + scene-construction authority
- `docs/03_DIALOGUE/AGENT_SYSTEM/RUNTIME_ORCHESTRATION.md` — compiler/runtime/service implementation authority
- `docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/AREA_TRAVERSAL_AUTHORING_INTERFACE.md`
- `docs/13_UI_AND_IMPLEMENTATION/DIALOGUE_UI.md`

## Automatic Person context construction

`runtime_context.py` is shared by the authority compiler and both service containers. Every authored scene rebuilds each person's context from protected construction inputs and approved person-local continuity before model generation. Cached/manual runtime state and the latest unsliced database state cannot override the build.

See `docs/03_DIALOGUE/AGENT_SYSTEM/AUTOMATIC_PERSON_CONTEXT.md` for structured assertions, story clocks, memory policies, migration, and limitations. `/v1/commit` requires both Canon Checker PASS and explicit author approval; the Orchestrator forwards the approved source story clock. Build endpoints remain read-only.

Offline regression: `python3 tests/dialogue/test_automatic_person_context.py` after installing `external-services/canary/requirements.txt`.
