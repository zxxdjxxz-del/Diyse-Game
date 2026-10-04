# Diyse-Game

Active Godot implementation repository for **Diyse**, an HD-2D, party-based, command-driven turn-based JRPG targeting Android.

## Current project authority

The repository's current written authority lives in the organized subject library under `docs/`.

Read in this order:

1. `docs/00_MASTER_CONTROL/DIYSE_MASTER_INDEX.md`
2. `docs/00_MASTER_CONTROL/AUTHORITY_AND_CHANGE_CONTROL.md`
3. `docs/00_MASTER_CONTROL/CANON_QUICK_REFERENCE.md`
4. the relevant numbered subject domain
5. `docs/90_WORKING/` only when the subject is explicitly open/reopened

When sources conflict, follow `docs/00_MASTER_CONTROL/AUTHORITY_AND_CHANGE_CONTROL.md`.

Current cross-domain terminology handoffs:
- classes → `docs/00_MASTER_CONTROL/CLASS_TERMINOLOGY_CURRENT.md`
- Faces → `docs/00_MASTER_CONTROL/FACE_TERMINOLOGY_CURRENT.md`

Git history is the recovery mechanism; `main` is the current production surface.

## Character visual masters

Current exact character source/reference masters are repository-backed under:

`asset_sources/characters/current/`

Their production authority order and matching visual-lock documents are indexed in:

`docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md`

Use that index's current source-authority order for exact appearance. A registered approved source fingerprint controls while repository binary synchronization is pending.

## Implementation status

Current runtime architecture and known code/canon divergences are tracked under:

- `docs/13_UI_AND_IMPLEMENTATION/CURRENT_RUNTIME_IMPLEMENTATION_STATUS.md`
- `docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`
- `docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/VALIDATION_AND_TEST_GATES.md`

The existing Godot runtime is an implementation foundation. Proof data and proof behavior do not override current domain canon.

## Repository layout

- `game/` — runtime game implementation
- `tests/` — automated/regression validation
- `tools/` — project tooling
- `docs/` — current organized canon, design, implementation requirements, and explicitly open working material
- `asset_sources/` — source/reference art and other production inputs, separated by provenance/storage rules
- `.github/` — CI/workflows
- `project.godot` — Godot project definition
- `export_presets.cfg` — export configuration

## Engineering workflow

Before implementing or changing production content:

1. read the master-control authority files;
2. read the owning numbered domain;
3. check implementation divergence notes;
4. preserve stable IDs and current terminology;
5. implement only values/rules supported by current owners;
6. run the relevant tests and project validation.

The goal is one current authority surface with Git providing recovery when genuinely needed.
