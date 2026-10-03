# Chapter 1 — Dialogue Authoring Status

**Status:** CURRENT 12-BEAT PRODUCTION STRUCTURE / WRITTEN DIALOGUE CURRENT  
**Chapter:** 1  
**Current structure date:** 2026-09-25

## Current written authority

Use the current Chapter-1 production set:
- `docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CHAPTER_01_DIALOGUE_AUTHORITY_INDEX.md`
- `docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CHAPTER_01_DIALOGUE_MANUSCRIPT.md`
- standalone Beat files `CH01_B01` through `CH01_B12`
- Character-Life scenes `C02`, `C03`, and `C04`

The current story owner is:
> `docs/02_STORY/CHAPTERS/CHAPTER_01.md`

## Current structure

Chapter 1 uses **12 mandatory beats**:

1. Brackenwall / Protocol
2. Briar Passage / First Traversal
3. Greenhollow / Torren
4. Hollow Watch Approach
5. Hollow Watch Surface / Garrison
6. Hollow Watch Excavation
7. Hollow Watch Landscape Depiction
8. Greenhollow Resolution / Torren Recruitment
9. Southern Briar Passage
10. Thornhide Stalker
11. The Junction / Hidden Monument
12. Junction Camp / Cleanup / next-morning handoff

Retired pre-restructure Beat-13–15 numbering must not be treated as current Chapter-1 structure.

## Current Character-Life files

- `../PRODUCTION/CHAPTER_01/C02_TORRENS_VERSION_OF_DINNER_DIALOGUE.md`
- `../PRODUCTION/CHAPTER_01/C03_WHAT_THE_MAP_SAYS_DIALOGUE.md`
- `../PRODUCTION/CHAPTER_01/C04_NOT_PROFESSIONALLY_DIALOGUE.md`

## Key continuity

- Maevra enters Chapter 1 with the arm broken during the Broken Convoy attack and remains noncombat.
- Cyanis + Ilyra are the opening combat party.
- Torren joins combat for Hollow Watch and becomes permanent in Greenhollow after Hollow Watch resolves.
- Hollow Watch underground is a short Construct-only Diysean corridor after the excavation transition.
- Shield Construct is a fixed stronger encounter, not a miniboss.
- Watch Castellan / Six-Channel / forced-inner material is retired.
- Southern Briar has no Cistern Hunt hook.
- **Thornhide Stalker** is the Chapter-1 final boss; **Thornhide** is the species terminology used in ordinary dialogue/sign references.
- the creature is not clearly seen until the immediate boss trigger.
- the Junction monument remains hidden until the authored clearing interaction.
- Chapter 1 ends with continuation toward Dunmere.

## Pipeline continuity

Use the current Agent Brain / dialogue workflow:
**scene authority → Person Agent context → dialogue generation/editing → Canon/Knowledge validation → author approval → implementation**.

No walking dialogue and no mid-battle dialogue.

## Runtime note

Current Chapter-1 runtime dialogue resources live under:
> `game/content/dialogue/current/chapter_01/`

Written production files remain the dialogue authority. Runtime resources must be validated against those current files before implementation is considered synchronized; stale legacy mirrors must not override the written authority.
