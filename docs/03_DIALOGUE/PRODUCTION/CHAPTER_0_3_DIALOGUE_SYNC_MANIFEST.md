# DIYSE — Chapters 0–3 Dialogue Synchronization Manifest

**Status:** PENDING DERIVED-OUTPUT GENERATION — ATOMIC DIALOGUE REMAINS CURRENT AUTHORITY

## What is current

The Chapter 0–3 standalone atomic dialogue files are the current exact wording authority and have completed the current character/performance audit set, including:

- Person-Brain performance rules;
- Ilyra role-balance (`Grace is not a dialogue assignment`);
- Cyanis non-functional leadership balance;
- Torren social-comfort progression (`Sparse is an early-state tendency, not a permanent voice quota`);
- Maevra familiarity + rank + friendship progression;
- Torren/Nimera Chapter-3 first-contact timing;
- mature-adult speech/profanity calibration;
- natural-turn/floor-holding audit;
- spoken-dialogue vs narration audit.

The atomic files remain authoritative even while the combined read-throughs and reader are awaiting regeneration.

## Derived outputs awaiting regeneration

The following are currently derived/stale products and must not override the atomics:

- `CHAPTER_00/CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`
- `CHAPTER_01/CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`
- `CHAPTER_02/CHAPTER_02_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`
- `CHAPTER_03/CHAPTER_03_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`
- the Chapters 0–3 spoiler-free exact-dialogue reader / novelization

## Synchronization machinery

Current synchronizer:

`tools/dialogue/sync_current_dialogue.py`

Current workflow:

`.github/workflows/dialogue-sync.yml`

The synchronizer is designed to:

1. resolve the current atomic sources in canonical order;
2. fail on missing or ambiguous source patterns;
3. verify protected dialogue anchors;
4. reject the retired Chapter-3 `Resource` Face list and require `Memory`;
5. reject a Chapter-1 Nimera reference before her Chapter-3 meeting;
6. regenerate all four combined read-throughs from the atomics without rewriting dialogue;
7. record per-source SHA-256 values in this manifest;
8. update chapter/master synchronization status only after generation succeeds;
9. rebuild the spoiler-free exact-dialogue DOCX from the same atomic source set;
10. support `--check` so future drift is detectable.

The workflow now triggers on the current Chapter 0–3 atomic dialogue filename families as well as changes to the synchronizer/workflow itself.

## Current execution blocker

The GitHub Actions job is currently failing before execution begins. The latest Dialogue Sync run produces a failed job with **no steps and no job logs**, and the repository's ordinary Godot workflow is showing the same runner-launch behavior on the same commits.

Therefore this is presently an **execution-runner issue, not a dialogue-source or synchronizer failure**. No generated output is marked current until the synchronizer actually completes and its `--check` verification passes.

Railway was also checked for a non-deploying one-off repository command. Railway does not provide one without creating/changing a deployment, so the live DIYSE character-agent services were intentionally left untouched.

## Completion rule

A derived Chapter 0–3 manuscript or reader may be described as current only after:

`python tools/dialogue/sync_current_dialogue.py --check`

returns success against the repository state that generated it.

Until then:

> **Atomic dialogue = current exact authority. Combined manuscripts/reader = derived products pending regeneration.**
