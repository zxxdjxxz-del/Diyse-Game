# AGENTS.md — Diyse Engineering Contract

This file governs AI-assisted engineering work in the Diyse implementation repository.

## Authority routing

Before changing gameplay code, production content, data, UI, dialogue, progression, encounters, or saves:

1. read `docs/00_MASTER_CONTROL/CURRENT_CANON_STATUS.md`;
2. read `docs/00_MASTER_CONTROL/AUTHORITY_AND_CHANGE_CONTROL.md`;
3. read `docs/00_MASTER_CONTROL/CANON_QUICK_REFERENCE.md`;
4. read the owning numbered subject domain;
5. read `docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_AUTHORITY_PRECEDENCE.md` for implementation-facing conflicts;
6. read `docs/90_WORKING/` only when the subject is explicitly open/reopened.

If a newer explicit user correction conflicts with repository text, do not silently reinterpret it. Surface the conflict and update the owning authority through the approved workflow.

## Source precedence

Use the precedence defined by the organized canon library. In implementation terms:

1. newest explicit approved user correction;
2. current organized domain authority;
3. current master-control cross-domain rule;
4. current operational implementation requirement;
5. proof runtime;
6. archived/historical material.

Proof code demonstrates architecture. It does not restore stale mechanics, names, currencies, progression, or UI concepts.

## Repository boundaries

Do not delete or replace runtime/build/test infrastructure merely because canon documentation is reorganized.

Preserve unless a task explicitly changes them:

- `.github/`
- `.gitignore`
- `project.godot`
- `export_presets.cfg`
- `game/`
- `tests/`
- `tools/`

## Canon duplication rule

Do not turn this file into another full canon snapshot.

Detailed game rules belong in their owning `docs/` domain. This file should route engineering work to those sources so root guidance does not become stale duplicate authority.

## Known proof-runtime warning

Before production implementation, check:

`docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`

Known proof data/behavior may intentionally remain in runtime until migrated. Do not treat its presence as design approval.

## Validation

For any implementation change:

- run the relevant focused test(s);
- run applicable smoke/regression gates;
- preserve stable IDs and save compatibility where required;
- verify current-facing terminology;
- do not weaken tests merely to make stale behavior pass.

For documentation-only transitions, additionally verify that all root guidance paths resolve into the organized `docs/` library.
