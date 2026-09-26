# DIYSE — Dialogue File Naming Authority

**Status:** CURRENT GLOBAL PRODUCTION NAMING AUTHORITY  
**Effective:** 2026-09-26  
**Scope:** current and future files under `docs/03_DIALOGUE/PRODUCTION/`, plus machine scene IDs that identify those atomics/specs.

## Purpose

Dialogue filenames must expose stable identity without encoding temporary workflow state.

Canonical production filenames answer:
1. what chapter/scene identity is this?
2. what human-readable scene is this?
3. what artifact type is this?

They do **not** encode mutable status such as draft letter, working pass, current/final, rehearsal method, or editor iteration.

Git history and authority metadata own revision history.

## Mandatory story beat contract

For numbered chapter beats, approved exact dialogue uses:

```text
CH##_B##_SCENE_NAME_DIALOGUE.md
```

When a scene has a scene-authority spec, the paired spec uses:

```text
CH##_B##_SCENE_NAME_SPEC.json
```

Do not invent retroactive specs solely to satisfy the filename grammar. Source-closed earlier chapters may legitimately have approved dialogue atomics without per-beat specs if those specs were never part of that chapter's production generation.

Example:

```text
CH03_B14_CRESTHAVEN_TOWER_BASE_FIRST_COMMAND_WARDEN_DIALOGUE.md
CH03_B14_CRESTHAVEN_TOWER_BASE_FIRST_COMMAND_WARDEN_SPEC.json
```

Machine `scene_id` uses the same stable key:

```text
CH03_B14_CRESTHAVEN_TOWER_BASE_FIRST_COMMAND_WARDEN
```

Human-facing prose may still say “Beat 14.” Machine identity uses `B14`.

## Pre-approval rehearsal targets

When exact spoken dialogue is not yet approved:

```text
CH##_B##_SCENE_NAME_REHEARSAL_TARGET.md
```

A rehearsal target is not exact dialogue authority.

`_DIALOGUE.md` is reserved for wording that has passed the current approval gate required by that chapter's dialogue authority index.

Do not create placeholder or empty `_DIALOGUE.md` files for unauthored scenes.

## Character-Life contract

Character-Life scenes use the global chronological namespace:

```text
C##_SCENE_NAME_DIALOGUE.md
C##_SCENE_NAME_SPEC.json
```

Current live sequence through Chapter 3 is C01–C07 with no active alias/source-key numbering.

Machine IDs may include chapter plus canonical Character-Life ID:

```text
CH03_C06_NIMERA_TAKES_OVER_A_TABLE
```

## Status/version rule

The following do **not** belong in canonical production filenames:

- `DRAFT_A`, `DRAFT_B`, etc.;
- `WORKING`;
- `CURRENT`;
- `FINAL`;
- `REHEARSAL_FIRST`;
- `NATURAL_TURN`;
- pass names or editor iteration names.

Those belong in file metadata, authority indexes, commit history, or audit documents.

## Renumbering rule

Canonical live beat numbering is continuous within the current chapter structure.

Retired developmental beats do not reserve live numbers.

If a chapter is structurally revised before final lock:
- update the live canonical B-sequence;
- migrate references atomically;
- preserve retired numbering only in Git/history;
- never keep a ghost live slot solely for provenance.

## Derived combined manuscripts

Generated chapter read-throughs use the stable filename:

```text
CHAPTER_##_DIALOGUE_MANUSCRIPT.md
```

Their generated title is **Synchronized Dialogue Manuscript**. They are derived mirrors only; standalone atomics remain exact wording authority.

Do not encode rehearsal method, draft state, `WORKING`, `CURRENT`, or `FINAL` in a generated manuscript filename. Synchronization state belongs in the manuscript metadata and sync manifest.

Cross-chapter generated sync metadata uses `CHAPTERS_00_03_DIALOGUE_SYNC_MANIFEST.md`.

Cross-chapter dated dialogue provenance/audits use the plural range prefix `CHAPTERS_00_03_...`, for example `CHAPTERS_00_03_FULL_SOURCE_CLOSURE_2026-09-13.md`. Dates are appropriate for audit/provenance records, not canonical scene identity. The generated Chapters 0–3 reader uses `DIYSE_Chapters_00-03_Spoiler_Free_Exact_Dialogue_Reader.docx`; freshness is determined by generation/validation, not a `CURRENT` filename suffix.

## Authority and historical files

Historical/superseded story packets belong outside the live authority root, such as:

```text
docs/02_STORY/CHAPTERS/HISTORICAL/CHAPTER_##/
```

Historical folders are provenance only. Scene-authority specs must not cite them as current authority.

Combined manuscripts, exact-dialogue readers, sync manifests, and runtime resources are derived artifacts. They do not determine canonical source filenames or override atomics.

## Current early-game state

- Chapter 0 mandatory dialogue: `CH00_B01`–`CH00_B07`;
- Chapter 1 mandatory dialogue: `CH01_B01`–`CH01_B12`;
- Chapter 2 mandatory dialogue: `CH02_B01`–`CH02_B15`;
- Chapter 3 mandatory dialogue: `CH03_B01`–`CH03_B15`;
- Character-Life: C01–C07;
- Chapter 4 begins directly under this contract.

## Conflict rule

If a filename, manifest, reader, runtime resource, or older audit disagrees with the current chapter dialogue authority index and this naming authority:
1. current chapter story/dialogue authority decides scene identity;
2. this file decides canonical filename grammar;
3. current atomic/spec files decide exact source identity;
4. derived artifacts are regenerated;
5. Git history supplies provenance.

> **Stable identity in filenames; mutable state in metadata and Git.**


## Automated enforcement

Run:

```text
python tools/dialogue/validate_authority_naming.py
```

The validator rejects legacy/mutable production filenames, non-contiguous live beat IDs, Character-Life numbering gaps/duplicates, malformed canonical B/C files, scene-spec IDs that disagree with their filenames, retired cross-chapter naming, and retired direct runtime dialogue chapter folders. The live runtime dialogue layout permits only `game/content/dialogue/current/` and `game/content/dialogue/proof/` alongside the root README.

GitHub Actions runs the same check through `Authority Naming Validation`.
