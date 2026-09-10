# Chapter 1 — Dialogue Authoring Status

**Status:** COMPLETE CURRENT WORKING PRODUCTION  
**Chapter:** 1

Current cumulative production manuscript:
`docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`

Current standalone production scenes/specs are stored in:
`docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/`

## Authority state

Chapter 1 is assembled end-to-end through the rehearsal-first Dialogue Engine process: Beats 1–15 plus optional Character-Life C03–C05 during the Junction camp cleanup window.

The old Chapter-1 `LINE_COMPLETE` transcript set and the superseded pre-rehearsal cumulative working manuscript have been removed from the live repository tree. Git history remains the archive for those superseded versions.

The current production manuscript is the dialogue version to use going forward. It may still receive bounded implementation/playtest edits; `complete current working production` is not a permanent immutable line lock.

## Pipeline continuity

Chapter 1 is one of the two reference implementations for the locked forward dialogue workflow. The same rehearsal-first Agent Brain system used here and in Chapter 0 is mandatory for Chapters 2–13 and future Diyse dialogue unless explicitly revised by the user.

Owning lock:
`docs/03_DIALOGUE/AGENT_SYSTEM/CHAPTER_0_1_PIPELINE_CONTINUITY_LOCK.md`

Required sequence:
**scene/world state → independent Person Agent Brain rehearsals → Dialogue Editor → invisible Canon/Knowledge Checker → economical HD-2D staging/implementation**.

## Current Character-Life files

- `C03_TORRENS_VERSION_OF_DINNER_REHEARSAL_FIRST_DRAFT_C.md`
- `C04_WHAT_THE_MAP_SAYS_REHEARSAL_FIRST_DRAFT_A.md`
- `C05_NOT_PROFESSIONALLY_REHEARSAL_FIRST_DRAFT_D.md`

## Key continuity

- Maevra enters Chapter 1 with the arm broken during the Broken Convoy attack and remains noncombat;
- C03: all four at camp, Torren's bad food, Torren smokes only after dinner;
- C04: Cyanis/Torren modern route-map scene, preserving `old slut / old cut` at early relationship timing;
- C05: Ilyra + Maevra only, splint change, limited pain-easing magic cannot mend the bone, private Maevra/Torren conversation;
- Briarhide is not clearly seen until the immediate boss trigger;
- Junction monument is hidden until Beat 14 and Torren has never seen the exposed monument before then;
- Chapter 1 ends with departure toward Dunmere.

## Runtime note

Legacy Godot dialogue resources under `game/content/dialogue/chapter_01/` are implementation assets from the earlier script generation and are **not current written dialogue authority**. They must be regenerated/replaced from the current production manuscript before Chapter 1 dialogue implementation is considered synchronized. Do not treat those `.tres` files as a competing locked chapter.
