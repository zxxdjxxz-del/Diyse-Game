# Diyse-Game

Active Godot implementation repository for **Diyse**, an HD-2D, party-based, command-driven turn-based JRPG targeting Android.

## Current project authority

The repository's current written authority lives in the organized subject library under `docs/`.

Read in this order:

1. `docs/00_MASTER_CONTROL/CURRENT_CANON_STATUS.md`
2. `docs/00_MASTER_CONTROL/CANON_QUICK_REFERENCE.md`
3. the relevant numbered subject domain
4. `docs/90_WORKING/` only when the subject is explicitly open/reopened
5. `docs/99_ARCHIVE/` only for provenance/history

When sources conflict, follow `docs/00_MASTER_CONTROL/AUTHORITY_AND_CHANGE_CONTROL.md`.

`docs/99_ARCHIVE/` is never current authority.

## Implementation status

Current runtime architecture and known code/canon divergences are tracked under:

- `docs/13_UI_AND_IMPLEMENTATION/CURRENT_RUNTIME_IMPLEMENTATION_STATUS.md`
- `docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`
- `docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/IMPLEMENTATION_FRONTIER.md`

The existing Godot runtime is an implementation foundation. Proof data, proof names, and historical behavior do not override current domain canon.

## Repository layout

- `game/` — runtime game implementation
- `tests/` — automated/regression validation
- `tools/` — project tooling
- `docs/` — current organized canon, design, implementation requirements, working queue, and archive
- `.github/` — CI/workflows
- `project.godot` — Godot project definition
- `export_presets.cfg` — export configuration

## Engineering workflow

Before implementing or changing production content:

1. read the master-control authority files;
2. read the owning numbered domain;
3. check implementation divergence notes;
4. preserve stable IDs and current terminology;
5. do not restore retired mechanics or names from proof code/history;
6. run the relevant tests and project validation.

The goal is one current authority surface with Git history providing recovery—not multiple competing generations of "current" documentation.
