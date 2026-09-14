# DIYSE — Chapters 0–3 Dialogue Synchronization Manifest

**Status:** SOURCE-CLOSED / DERIVED OUTPUT GENERATION BLOCKED BY EXECUTION INFRASTRUCTURE  
**Atomic authority:** CURRENT  
**Combined manuscripts / reader:** STALE until verified regeneration

## Owning records

Source-level closure:
- `CHAPTER_00_03_FULL_SOURCE_CLOSURE_2026-09-13.md`

Derived-execution blocker:
- `CHAPTER_0_3_DERIVED_SYNC_BLOCKER_2026-09-13.md`

Synchronizer:
- `tools/dialogue/sync_current_dialogue.py`

GitHub workflow:
- `.github/workflows/dialogue-sync.yml`

Isolated fallback image:
- `tools/dialogue/Dockerfile.sync`

## What is current

The Chapter 0–3 standalone atomic dialogue files are the current exact wording authority and have completed the current source-level audit set, including:
- Person-Brain performance rules;
- Cyanis non-functional leadership balance;
- Ilyra role-balance (`Grace is not a dialogue assignment`);
- Torren social-comfort progression (`Sparse is an early-state tendency, not a permanent voice quota`);
- Maevra familiarity + rank + friendship progression;
- Torren/Nimera Chapter-3 first-contact timing;
- mature-adult speech/profanity calibration;
- natural-turn/floor-holding audit;
- spoken-dialogue vs narration audit;
- current Face/class/subclass terminology and current reveal firewalls.

The atomics remain authoritative regardless of derived-artifact state.

## Derived outputs awaiting verified regeneration

The following must not override the atomics until a successful synchronizer run and verification:
- `CHAPTER_00/CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`
- `CHAPTER_01/CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`
- `CHAPTER_02/CHAPTER_02_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`
- `CHAPTER_03/CHAPTER_03_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`
- the Chapters 0–3 spoiler-free exact-dialogue reader / novelization.

This file itself is currently a synchronization-status manifest, not a successful generated hash manifest.

## Synchronizer behavior

The repo-native synchronizer is designed to:
1. validate full source closure before deriving anything;
2. resolve the current atomic sources in canonical order;
3. fail on missing or ambiguous source patterns;
4. verify protected dialogue anchors;
5. reject retired Chapter-3 `Resource` Face wording and require `Memory`;
6. reject premature Chapter-1 Nimera knowledge;
7. regenerate all four combined read-throughs without rewriting dialogue;
8. write per-source SHA-256 values into the successful generated manifest;
9. rebuild the spoiler-free exact-dialogue DOCX from the same atomic source set;
10. support `--check` so later drift is detectable.

Required validation sequence:

```text
python tools/dialogue/sync_current_dialogue.py --source-check
python tools/dialogue/sync_current_dialogue.py
python tools/dialogue/sync_current_dialogue.py --check --no-docx
```

## Current execution blocker

This blocker is external to dialogue source content.

### GitHub Actions
Latest observed Dialogue Sync execution:
- run `34794590948`;
- job `103825131383`;
- head `12d00bf5203fdbcbd0d1c1dab2289ed0c04677a9`;
- failure before workflow step 1;
- zero recorded steps;
- job-log retrieval returned `BlobNotFound`.

An unrelated Godot workflow exhibited the same runner-launch failure on the same repo state. Do not rewrite or touch closed atomics merely to retrigger unavailable runners.

### Railway
A new isolated temporary project was attempted instead of changing a live Character Agent service. Railway refused provisioning because the current free-plan resource limit is exhausted.

No existing Railway service was changed, redeployed, deleted, or repurposed.

### Render
A disposable static-site build was attempted as another isolated runner. The connected Render workspace cannot fetch the private `zxxdjxxz-del/Diyse-Game` repository. Its existing Seyrik service uses a public bootstrap repository and was intentionally left untouched.

No existing Render service was changed or repurposed.

## Safety / authority rule

Do not work around this blocker by:
- hand-copying atomics into a supposedly exact combined manuscript;
- treating an old combined manuscript as current wording authority;
- treating the previous reader as current exact dialogue;
- modifying closed atomics merely to force a CI trigger;
- repurposing live character-agent infrastructure;
- making the private repo public.

## Completion rule

A derived Chapters 0–3 manuscript or reader may be described as current only after a successful generation and:

```text
python tools/dialogue/sync_current_dialogue.py --check --no-docx
```

returns success against the same source state.

The generated DOCX must then receive visual QA before user-facing delivery.

Until then:

> **Atomic dialogue = current exact authority. Combined manuscripts/reader = derived products pending verified regeneration.**
