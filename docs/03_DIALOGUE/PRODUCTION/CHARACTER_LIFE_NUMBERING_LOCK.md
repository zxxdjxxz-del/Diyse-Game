# DIYSE — Character-Life Canonical Numbering Lock

**Status:** CURRENT CANONICAL NUMBERING AUTHORITY  
**Scope:** active Character-Life scenes across the current dialogue production set  
**Effective:** 2026-09-12

## Rule

Active Character-Life scenes use one continuous chronological sequence beginning at **C01**. Retired, cut, superseded, or experimental scene IDs do **not** reserve numbers in the live sequence.

Historical filenames and embedded source keys may retain an older development label when changing that key would invalidate a synchronized manuscript or provenance record. In that case the **canonical Character-Life ID in this file wins**. A legacy source key is not a current scene number.

## Current canonical sequence

| Canonical ID | Chapter | Scene | Current legacy source key, where different |
|---|---:|---|---|
| **C01** | 0 | **Six Minutes** | C01 |
| **C02** | 1 | **Torren's Version of Dinner** | C03 |
| **C03** | 1 | **What the Map Says** | C04 |
| **C04** | 1 | **Not Professionally** | C05 |
| **C05** | 2 | **Still Burns** | C06 |
| **C06** | 3 | **Nimera Takes Over a Table** | H01 |
| **C07** | 3 | **Ilyra and Nimera** | H03 |

## Retired-number rule

Older development references such as the retired Chapter-2 `C07` concept and Chapter-3 `H02/H04` concepts are historical only. They do not block reuse of a number in the canonical live Character-Life sequence.

The former separate Chapter-2 `C07` concept remains retired; useful material already folded into **C05 — Still Burns** stays there. The canonical live **C07** is now **Ilyra and Nimera** in Chapter 3.

## Source-key transition rule

The Chapter-1 and Chapter-2 synchronized manuscripts embed exact source filenames and Git blob SHAs. Until those manuscripts are next regenerated from renamed atomic files, their embedded `C03/C04/C05/C06` labels are **legacy source keys**, not canonical Character-Life numbers.

Likewise, Chapter-3 `H01/H03` filenames remain legacy source keys until the atomic files are renamed. Current chapter-level documentation must refer to them canonically as **C06/C07**.

When a Character-Life atomic source is next materially edited, its filename, internal scene ID, and any synchronized-manuscript source marker should be migrated to the canonical ID in the same change so no new legacy key is created.

## Conflict rule

If an active document disagrees about a Character-Life number:
1. this numbering lock and later explicit user corrections;
2. chapter dialogue authority index;
3. chapter cleanup/availability authority;
4. legacy source filename/header only as implementation provenance.

> **Current live Character-Life sequence through Chapter 3: C01–C07, with no gaps.**
