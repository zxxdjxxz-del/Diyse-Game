# Diyse — Chapters 0–4 Region / Place-Name Dialogue Audit

**Date:** 2026-08-27  
**Scope:** Chapter 0–4 current-facing dialogue, dialogue staging/narration, optional Character-Life material, and Chapter 4 Crown Prototype Hunt authoring/runtime.  
**Purpose:** Remove retired geography/place terminology without reopening approved dramatic content.

---

## Current terminology used by this audit

Current-facing geography must use the latest terminology authority:

- **The Westways** — not `Edgelands`; older western-region `Borderlands` wording is retired from current-facing prose.
- **The Greyspires** — not `Diysereach` or formal regional `Highlands`.
- **Yahtrenhold** — not `Southhold`, `Crownhold`, or `The Crownhold`.
- **Black Host Territory** — not `Blackstone` as a region/place designation.
- **The Blackspine** — not formal `Black Mountains`.
- **Westguard** — not the retired settlement names `Westreach` or temporary `Yahtrens Stand`.

Chapter 4 current-facing place/entity terminology additionally uses:

- **Reaction Annex** — not `Sixfold Annex`.
- **Reaction Node** — not `Sixfold Node`.
- **Reaction Conduit** — not `Elemental Hexarch`.
- **Regulation Crucible** — not `Sixfold Crucible`.

Ordinary descriptive uses of words such as `highlands`, `water`, or `wind` are not automatically geography/system labels and must be judged in context.

---

# 1. AUTHORING-SOURCE AUDIT

## Chapter 0

Chapter 0 production dialogue exists directly as runtime Resources rather than a separate Markdown transcript directory.

Audited:
- S001–S006
- C01–C02

**Result:** CLEAN for retired current-facing region/place names.

Current-facing S001 staging already uses **Westways road**.

Legacy `LOC_BORDERLANDS_*` implementation identifiers remain internal technical IDs and are not dialogue text. They are outside this terminology-only authoring pass and should be migrated only through a reference-safe engineering change.

---

## Chapter 1

Audited:
- S007–S011
- C03–C05

**Result:** CLEAN. No retired current-facing region/place terminology found.

---

## Chapter 2

Audited:
- S012–S016
- C06–C07

**Result:** CLEAN. No retired current-facing region/place terminology found.

---

## Chapter 3

Audited:
- S017–S021
- H01–H04

### Corrections made

#### S020 — Oath Sentinel
Retired:
> Old Crown outpost in the Crownhold. Abandoned.

Current:
> Old Crown outpost in Yahtrenhold. Abandoned.

#### S021 — Four Answers, Not One
Retired staging identified Cresthaven as an abandoned `Crownhold` outpost.

Current staging identifies it as an abandoned **Yahtrenhold** outpost.

### Remaining Chapter 3 source
S017, S018, S019, H01, H02, H03, and H04 were clean.

**Chapter 3 authoring-source result:** CLEAN after the S020/S021 corrections.

---

## Chapter 4

Audited:
- S022–S026
- C08
- C09
- H05
- HUNT_04_CROWN_PROTOTYPE

### Corrections made

#### S022 — Brilliant Answer
Retired:
> current Crown map of the Crownhold.

Current:
> current Crown map of Yahtrenhold.

#### HUNT_04_CROWN_PROTOTYPE
Retired current-facing `Sixfold Annex` placement/area wording was replaced with **Reaction Annex**, including the post-chapter return and Prototype Testing area headings.

### Remaining Chapter 4 source
S023–S026, C08, C09, and H05 were clean for the retired geography/place-name set.

**Chapter 4 authoring-source result:** CLEAN after S022 and Crown Prototype Hunt corrections.

---

# 2. RUNTIME RESOURCE AUDIT

Current-facing runtime dialogue/staging was also checked.

## Clean runtime material

- Chapter 0 S001–S006, C01–C02: clean.
- Chapter 4 S023–S026, C08, C09, H05: clean.
- Crown Prototype runtime spoken/staging material contains no current-facing `Sixfold Annex` wording.

Chapter 4 still contains internal implementation IDs such as `LOC_SIXFOLD_ANNEX`, `LOC_SIXFOLD_REGULATION_CORE`, and `LOC_SIXFOLD_ANNEX_PROTOTYPE`. Existing Resource notes identify these as legacy internal location IDs retained pending environment-ID migration. **Do not rename them as a prose cleanup.**

## Runtime source synchronization completed

The three generated/runtime Resources that retained pre-correction current-facing wording have now been synchronized:

1. `game/content/dialogue/chapter_03/S020.tres`
   - now reads `Old Crown outpost in Yahtrenhold. Abandoned.`
   - regenerated from the corrected locked Markdown source through `tools/dialogue/compile_chapter_03.py`.

2. `game/content/dialogue/chapter_03/S021.tres`
   - staging now identifies the abandoned outpost with **Yahtrenhold**, not Crownhold.
   - regenerated from the corrected locked Markdown source through `tools/dialogue/compile_chapter_03.py`.

3. `game/content/dialogue/chapter_04/S022.tres`
   - staging now reads `current Crown map of Yahtrenhold.`
   - synchronized as a bounded runtime terminology correction without changing unrelated dialogue.

The isolated regeneration diff was limited to these intended source/runtime terminology effects; S020's spoken-sequence checksum changed as expected because Mirena's spoken line changed, while the other dramatic content remained intact.

---

# 3. CLOSED RESULT

**Chapters 0–4 authoring dialogue, current-facing staging/narration, and applicable runtime dialogue Resources are clean for the audited retired place/region names.**

Corrections applied in this sweep:
- S020: Crownhold → Yahtrenhold in source and runtime.
- S021: Crownhold → Yahtrenhold in source and runtime staging.
- S022: Crownhold → Yahtrenhold in source and runtime staging.
- Crown Prototype authoring: Sixfold Annex → Reaction Annex.

No additional retired current-facing place/region names were found in the audited Chapter 0–4 dialogue set.

Legacy technical identifiers are intentionally excluded from prose renaming and remain a separate reference-safe engineering migration concern.

**Audit status: CLOSED.**
