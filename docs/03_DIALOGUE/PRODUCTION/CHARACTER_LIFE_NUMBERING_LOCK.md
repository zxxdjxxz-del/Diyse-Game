# DIYSE — Character-Life Canonical Numbering Lock

**Status:** CURRENT CANONICAL NUMBERING AUTHORITY  
**Scope:** active Character-Life scenes across the current dialogue production set  
**Effective:** 2026-09-12; canonical source-key migration completed 2026-09-26

## Rule

Active Character-Life scenes use one continuous chronological sequence beginning at **C01**. Retired, cut, superseded, or experimental scene IDs do **not** reserve numbers in the live sequence.

Canonical Character-Life IDs now match their active atomic filenames and scene IDs directly. Historical development labels remain Git provenance only and are not used by current story, dialogue, sync, or runtime selection.

## Current canonical sequence

| Canonical ID | Chapter | Scene | Current atomic |
|---|---:|---|---|
| **C01** | 0 | **Six Minutes** | `CHAPTER_00/C01_SIX_MINUTES_DIALOGUE.md` |
| **C02** | 1 | **Torren's Version of Dinner** | `CHAPTER_01/C02_TORRENS_VERSION_OF_DINNER_DIALOGUE.md` |
| **C03** | 1 | **What the Map Says** | `CHAPTER_01/C03_WHAT_THE_MAP_SAYS_DIALOGUE.md` |
| **C04** | 1 | **Not Professionally** | `CHAPTER_01/C04_NOT_PROFESSIONALLY_DIALOGUE.md` |
| **C05** | 2 | **Still Burns** | `CHAPTER_02/C05_STILL_BURNS_DIALOGUE.md` |
| **C06** | 3 | **Nimera Takes Over a Table** | `CHAPTER_03/C06_NIMERA_TAKES_OVER_A_TABLE_DIALOGUE.md` |
| **C07** | 3 | **Ilyra and Nimera** | `CHAPTER_03/C07_ILYRA_AND_NIMERA_DIALOGUE.md` |

## Retired-number rule

Older development references such as Chapter-1 source keys C03/C04/C05, Chapter-2 source key C06, Chapter-3 H01/H03, the retired Chapter-2 C07 concept, and Chapter-3 H02/H04 concepts are historical only. They do not block reuse of a number or override the canonical live sequence.

The former separate Chapter-2 C07 concept remains retired; useful material already folded into **C05 — Still Burns** stays there. The canonical live **C07** is **Ilyra and Nimera** in Chapter 3.

## Source-key rule

> **Current source key = canonical Character-Life ID.**

Active files, scene IDs, chapter authority indexes, synchronization tooling, and runtime compilation must use C01–C07 directly. Do not create new alias/source-key numbering.

Historical filenames remain recoverable through Git history only.

## Conflict rule

If an active document disagrees about a Character-Life number:
1. this numbering lock and later explicit user corrections;
2. chapter dialogue authority index;
3. chapter cleanup/availability authority;
4. Git history only as provenance.

> **Current live Character-Life sequence through Chapter 3: C01–C07, with no gaps and no active legacy source-key aliases.**
