# Chapter 0 — Dialogue Authoring Status

**Status:** COMPLETE CURRENT WORKING PRODUCTION  
**Chapter:** 0 — The Broken Convoy

Current cumulative production manuscript:
`docs/03_DIALOGUE/PRODUCTION/CHAPTER_00/CHAPTER_00_DIALOGUE_MANUSCRIPT.md`

Current standalone production scenes are stored in:
`docs/03_DIALOGUE/PRODUCTION/CHAPTER_00/`

## Authority state

Chapter 0 is assembled end-to-end through the rehearsal-first Dialogue Engine process: B01 → B07, optional C01 `Six Minutes`, and the explicit departure to Brackenwall.

The old Chapter-0 `LINE_COMPLETE` transcript set has been removed from the live repository tree. The temporary quick-pass cumulative manuscript and old casing-overlay manuscript have also been removed. Git history remains the archive for those superseded versions.

The current production manuscript is the dialogue version to use going forward. It may still receive bounded implementation/playtest edits; `complete current working production` is not a permanent immutable line lock.

## Pipeline continuity

Chapter 0 is one of the two reference implementations for the locked forward dialogue workflow. The same rehearsal-first Agent Brain system used here and in Chapter 1 is mandatory for Chapters 2–13 and future Diyse dialogue unless explicitly revised by the user.

Owning lock:
`docs/03_DIALOGUE/AGENT_SYSTEM/CHAPTER_0_1_PIPELINE_CONTINUITY_LOCK.md`

Required sequence:
**scene/world state → independent Person Agent Brain rehearsals → Dialogue Editor → invisible Canon/Knowledge Checker → economical HD-2D staging/implementation**.

## Key continuity

- first incomplete Card flare: B04, fully ends before P05;
- B05: concealed Ruin Vanguard Pursuer, Card inert;
- B06: combined Riftmaw + Convoy War-Sorcerer boss, second flare;
- recovery casing breaks during B06; Card survives intact;
- B07 onward: Cyanis carries the Card itself;
- C01 `Six Minutes` is the current optional Character-Life scene;
- Chapter 0 ends only through explicit departure to Brackenwall.

## Runtime note

Legacy Godot dialogue resources under `game/content/dialogue/chapter_00/` are implementation assets from the earlier script generation and are **not current written dialogue authority**. They must be regenerated/replaced from the current production manuscript before Chapter 0 dialogue implementation is considered synchronized. Do not treat those `.tres` files as a competing locked chapter.
