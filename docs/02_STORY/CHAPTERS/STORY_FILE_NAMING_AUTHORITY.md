# DIYSE — Story File Naming Authority

**Status:** CURRENT GLOBAL STORY FILE NAMING AUTHORITY  
**Effective:** 2026-09-26  
**Scope:** current files under `docs/02_STORY/CHAPTERS/`.

## Purpose

Current story filenames should expose stable structural identity and file role without encoding temporary workflow state.

Git history owns draft history. File metadata owns current status.

## Primary chapter authority

The mandatory chapter master is:

```text
CHAPTER_##.md
```

Example:

```text
CHAPTER_03.md
```

This remains the primary story authority for the chapter unless a later explicit authority says otherwise.

## Compact beat structure

When a chapter has a separate compact/cumulative beat structure, use:

```text
CHAPTER_##_BEAT_STRUCTURE.md
```

Do not encode `WORKING`, `CURRENT`, or revision letters into this stable filename.

## Beat-specific supporting story files

Supplemental beat development that remains current uses:

```text
CH##_B##_SCENE_NAME_STORY_SUPPORT.md
```

Example:

```text
CH03_B13_RETURN_TO_MIRENA_CRESTHAVEN_IDENTIFIED_STORY_SUPPORT.md
```

These files supplement the chapter master and never silently override it.

## Beat-specific hard locks

A narrow current lock uses:

```text
CH##_B##_TOPIC_LOCK.md
```

A lock spanning adjacent beats may use:

```text
CH##_B##_TO_B##_TOPIC_LOCK.md
```

Examples:

```text
CH03_B14_FIRST_COMMAND_WARDEN_FINAL_MESSAGE_LOCK.md
CH03_B12_TO_B13_MIRENA_MEETING_LOCK.md
CH01_B09_TO_B10_THORNHIDE_REVEAL_LOCK.md
```

## Character-Life story support

Structural support for a canonical Character-Life scene uses:

```text
CH##_C##_SCENE_NAME_STORY_SUPPORT.md
```

Example:

```text
CH03_C06_NIMERA_TAKES_OVER_A_TABLE_STORY_SUPPORT.md
```

The `C##` ID must match the current global Character-Life numbering authority.

## Chapter-wide locks and audits

A chapter-wide lock may retain the chapter-master family:

```text
CHAPTER_##_TOPIC_LOCK.md
```

A dated audit/provenance record may use:

```text
CHAPTER_##_TOPIC_AUDIT_YYYY-MM-DD.md
```

Dates are appropriate for audits/provenance, not for canonical scene identity.

## Mutable-state words

Do not use these as part of a canonical current story filename:

- `WORKING`;
- `CURRENT`;
- `DRAFT_A`, `DRAFT_B`, etc.;
- `FINAL`;
- `REVISION`;
- `CORRECTION`.

A current correction should be promoted into a semantic `_LOCK.md`, `_STORY_SUPPORT.md`, or the chapter master itself.

## Historical material

Superseded beat packets belong under:

```text
HISTORICAL/CHAPTER_##/
```

Historical files preserve their old filenames when useful for provenance. They are not current authority and must not be cited by scene-authority specs.

## Beat numbering

Live mandatory beat numbering is continuous within the current chapter structure.

Retired beats do not reserve current B-numbers. When a structure changes:
1. revise the chapter master;
2. renumber the current live sequence;
3. migrate current references;
4. archive superseded packets;
5. preserve former numbering through Git/history rather than ghost live slots.

## Current early-game examples

- Chapter 1 Thornhide reveal lock: `CH01_B09_TO_B10_THORNHIDE_REVEAL_LOCK.md`;
- Chapter 2 compact structure: `CHAPTER_02_BEAT_STRUCTURE.md`;
- Chapter 3 compact structure: `CHAPTER_03_BEAT_STRUCTURE.md`;
- Chapter 3 current beat support/locks: `CH03_B##_...`;
- Chapter 3 Character-Life story support: `CH03_C06_...`, `CH03_C07_...`.

## Conflict rule

If an older support packet disagrees with the current chapter master:
1. the current chapter master wins;
2. later explicit user corrections/current semantic locks may narrow it;
3. this file governs filename grammar, not story content;
4. historical files never override live authority.

> **Stable structural identity in filenames; mutable production state in metadata and Git.**
