# Diyse — Repository Clean-Replacement Audit v98

**Status:** WORKING / PROPOSED — repository mutation NOT executed  
**Canon impact:** NONE  
**Audited GitHub repository:** `zxxdjxxz-del/Diyse-Game`  
**Audited `main` commit:** `3fd07e92eda04f31ba613a654b3b1b28071f44e6`  
**Reorganization baseline:** v97 subject-folder package

## Result

The current organized canon package is suitable to replace the **old GitHub documentation/canon layer**, but it is **not** a whole-repository replacement by itself.

v97 contains:
- 815 Markdown files;
- 1 package-manifest JSON;
- no `.gd` scripts;
- no `.tscn` scenes;
- no `.tres` resources;
- no `project.godot`;
- no export preset;
- no CI workflows;
- no runtime tests or tools.

Therefore deleting the whole repository and uploading only the canon package would destroy the current Godot implementation foundation.

## Checkpoint integrity

The current GitHub `main` head is exactly:

`3fd07e92eda04f31ba613a654b3b1b28071f44e6`

That is the same repository checkpoint explicitly inspected by the reorganized v97 implementation/domain files. No later GitHub commit needs to be recovered before staging this transition.

## Required final repository boundary

### KEEP from current GitHub runtime

Retain these implementation/build surfaces through the documentation transition:

- `.github/`
- `.gitignore`
- `project.godot`
- `export_presets.cfg`
- `game/`
- `tests/`
- `tools/`

These are runtime/engineering assets, not obsolete canon documents.

They remain subject to later canon reconciliation. Keeping them does **not** grant stale proof data authority over the organized canon.

### REPLACE

Replace the current legacy `docs/` tree with the reorganized subject-folder library.

Recommended repo placement:

```text
docs/
  00_MASTER_CONTROL/
  01_CHARACTERS/
  02_STORY/
  03_DIALOGUE/
  04_WORLD_AND_LORE/
  05_BATTLE_SYSTEM/
  06_CLASSES_AND_ABILITIES/
  07_CARDS/
  08_ITEMS_AND_EQUIPMENT/
  09_ENEMIES_AND_ENCOUNTERS/
  10_PROGRESSION_AND_EXP/
  11_QUESTS/
  12_ECONOMY_AND_REWARDS/
  13_UI_AND_IMPLEMENTATION/
  14_ART_AND_VISUALS/
  15_AUDIO_AND_MUSIC/
  16_BALANCE_AND_TESTING/
  90_WORKING/
  99_ARCHIVE/
  README.md
  PACKAGE_MANIFEST.json
```

Package-version update summaries are transport/history artifacts and do not need to remain at the active GitHub documentation root.

### REWRITE at repository root

Do not retain current root `README.md` or `AGENTS.md` unchanged.

Both currently duplicate canon and already contain stale statements, including the removed **8 automatic Mastery Points** model.

Replace them with thin routing documents that:
- identify the repo as the active implementation line;
- point to `docs/00_MASTER_CONTROL/` for authority;
- point to the relevant numbered domain before implementation;
- state that proof runtime never overrides current domain canon;
- avoid duplicating large canon snapshots that will go stale again.

Draft replacements are staged under:

`90_WORKING/GITHUB_TRANSITION_STAGING/`

## Explicitly DO NOT carry forward as active authority

Do not recreate the current GitHub historical documentation tree beside the reorganized library.

In particular, do not keep old cumulative/audit documents active merely because they existed in `main`. Git history is sufficient provenance once the clean transition is complete.

Do not create a second `legacy_docs/` tree inside active `main` unless a later task demonstrates a concrete implementation dependency that cannot be recovered from Git history or `99_ARCHIVE`.

## Known runtime/code reconciliation that remains AFTER the docs transition

The runtime is intentionally preserved even where proof state is stale. Existing v97 implementation notes already identify high-impact gaps:

1. remove stale Mastery Point assumptions;
2. replace bearer-locked `first_champion` Prime proof behavior;
3. migrate proof `gold` to player-facing **Auren** with version-safe save handling;
4. replace proof equipment/item/party fixtures with production data;
5. expand/version the production save schema;
6. update stale chapter/scene ID assumptions through Chapter 13 / S073;
7. replace proof UI with production UI without rebuilding on stale state.

These are implementation tasks, not reasons to keep obsolete GitHub canon documentation.

## Pre-cleanup history protection

Before deleting/replacing active documentation on GitHub, create a permanent pre-transition ref at the current head.

Recommended archival ref name:

`archive/pre-v98-subject-reorganization`

The purpose is recovery only. It must not become current-facing authority.

## Transition sequence — proposed

1. Create the archival ref at current `main` head.
2. Create a migration branch from current `main`.
3. Preserve runtime/build folders and configs listed above.
4. Remove the old `docs/` contents on the migration branch.
5. Install the organized subject-folder library under `docs/`.
6. Replace root `README.md` and `AGENTS.md` with the staged thin-router versions.
7. Run stale-reference scans against active docs/root guidance.
8. Validate all internal documentation links/routing paths.
9. Run existing Godot smoke/regression tests.
10. Run Android/APK workflow validation.
11. Only after those gates pass, merge the clean migration into `main`.

## Acceptance gates

The repository transition is ready to merge only when all are true:

- one obvious current documentation authority exists;
- no old cumulative tracker is presented as active authority;
- root guidance contains no removed Mastery Point model;
- runtime/build/test/CI surfaces remain present;
- all current tests still resolve their file paths;
- Godot project opens/headless validation runs;
- Android export workflow remains intact;
- stale current-facing terminology scan passes;
- `docs/99_ARCHIVE` remains non-authoritative;
- Git history/archive ref preserves the pre-cleanup repository state.

## Current decision state

**AUDIT COMPLETE / TRANSITION DESIGN PASS.**

The next repository step is a GitHub mutation and therefore requires explicit user approval before execution.
