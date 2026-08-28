# Diyse — Line-Complete Canon Dialogue Index

**Whole-project authority:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v2.20 / Audit135** — August 27, 2026.

This directory is the controlling repository-facing **line-complete production-authoring source** for completed Chapters 1–4. These files exist so approved dialogue can be validated, implemented and maintained without recovering, paraphrasing or re-authoring closed scenes.

## Authority hierarchy

1. Newer explicit user correction.
2. Current Complete Master Canon **v2.20 / Audit135** and its inherited authority chain.
3. Later compatibility overlays for the affected chapter/system/terminology.
4. The line-complete scene files in this directory where compatible with later canon.
5. Validated production Resources where conversion is complete and compatible with exact source.
6. Implementation-facing chapter lock/index files under `docs/chapters/`.
7. Compatible earlier approved material only where it does not conflict with newer authority.

A later bounded terminology/system correction may supersede an old term in a line-complete source without reopening the scene's approved dramatic content.

## Runtime / authoring status

- Chapter 0: exact production dialogue Resources already merged/validated, subject to later canon compatibility overlays.
- Chapter 1: S007–S011 + C03–C05 converted and validated for exact source parity + whole-chapter continuity.
- Chapter 2: S012–S016 + C06/C07 converted and validated for exact source parity + whole-chapter continuity.
- Chapter 3: S017–S021 + H01–H04 converted and validated for exact source parity + whole-chapter continuity/Cresthaven locks.
- Chapter 4: S022–S026 + C08/C09/H05 + Crown Prototype exact production dialogue source is present; current four-element corrections control obsolete Sixfold/Wind/Water/Barrier wording. Production `.tres` conversion/static validation is present where currently implemented. Runtime smoke/in-engine completion remains separate implementation QA.

There is no closed Chapter 0–4 **authoring** backlog. Do not treat missing presentation/map/trigger/runtime consumers as evidence that dialogue or canon is missing.

## HD-2D presentation boundary

Audit88 converts completed Chapters 0–4 to the approved HD-2D production grammar without changing approved dramatic content.

Detailed production authority:

`docs/production/HD2D_CHAPTERS_00_04_CONVERSION_AUDIT_PASS_1.md`

Older scene-source references to affordable `2.5D` staging are historical implementation shorthand. Preserve their intended economy, but implement through the active HD-2D grammar: ~80 px field sprites, ~200–220 px battle sprites, large portraits, authored layered environments, restrained cameras, reusable battle backgrounds, state swaps and modular VFX.

## Chapter 1 — Brackenwall and the Wayfinder

Mandatory:
- `chapter_01/S007.md`
- `chapter_01/S008.md`
- `chapter_01/S009.md`
- `chapter_01/S010.md`
- `chapter_01/S011.md`

Optional Character-Life:
- `chapter_01/C03.md`
- `chapter_01/C04.md`
- `chapter_01/C05.md`

Final-version note: Audit79 C04 uses the approved **“Old whore.” / “Bitch.”** misunderstanding. Older recovered wording is superseded.

Validated Resources: `game/content/dialogue/chapter_01/`.

## Chapter 2 — The Drowned Oath

Mandatory:
- `chapter_02/S012.md`
- `chapter_02/S013.md`
- `chapter_02/S014.md`
- `chapter_02/S015.md`
- `chapter_02/S016.md`

Optional Character-Life:
- `chapter_02/C06.md`
- `chapter_02/C07.md`

Final-version note: Audit78 C07 Rewrite Draft 2 controls. **Wet sleeves** is the approved callback; Torren lights his blunt from existing coals, not a modern lighter, and the scene does not frame his weed use as impairment or vice.

Validated Resources: `game/content/dialogue/chapter_02/`.

## Chapter 3 — The Old City and Last Sentinel

Mandatory:
- `chapter_03/S017.md`
- `chapter_03/S018.md`
- `chapter_03/S019.md`
- `chapter_03/S020.md`
- `chapter_03/S021.md`

Optional hub / Character-Life:
- `chapter_03/H01.md`
- `chapter_03/H02.md`
- `chapter_03/H03.md`
- `chapter_03/H04.md`

Hard geography: **Caelora → Old City / Suppressed Archives → separate Cresthaven.**

The corrected S020→S021 handoff remains exact in dramatic structure: post-Warden records prove false-order assembly; Torren copies routing geometry; the party returns to Mirena; Mirena identifies Cresthaven as an abandoned Crown outpost in **Yahtrenhold**; the next morning she is already there establishing it as headquarters. Any older `Southhold` label is superseded by current region terminology.

S021 identifies/unlocks Last Sentinel without manifesting it. First verified modern Prime manifestation remains S022.

Validated Resources: `game/content/dialogue/chapter_03/`.

## Chapter 4 — The Seventh Reaction

Controlling exact source directory: `chapter_04/`.

Closed Chapter 4 set:
- S022–S026 mandatory story scenes
- C08
- C09
- H05
- Crown Prototype Hunt content

Current Chapter-4 compatibility overlay is the approved four-element rework promoted through Audit121 and later authority.

Hard production/content locks include:
- Chapter starts with Cyanis / Ilyra / Torren / Nimera as the traveling permanent party; Maevra is not the default Chapter 4 traveling member.
- Vaelira joins permanently during S022; choose-four remains active after roster reaches five permanents.
- S022 Elder Briarhide is the first verified modern Last Sentinel manifestation.
- Last Sentinel manifests for one legal Prime action and dismisses in the same round; Elder Briarhide retreats alive.
- Chapter 4 uses exactly **Fire / Ice / Lightning / Earth** as its research/regulation elements.
- **Reaction Annex** is the current Annex name; `Sixfold Annex` is retired current-facing terminology.
- **Reaction Conduit** replaces Elemental Hexarch and remains a harmed living researcher resolved nonlethally.
- **Regulation Crucible** replaces Sixfold Crucible. Form I uses exactly four chambers, with two active/targetable at once.
- Regulation Crucible transforms into genuine fresh-HP **The Seventh Reaction**; destroyed chamber traits stay absent; no third form.
- Wind/Water regulation states and their old special behaviors are removed rather than reassigned.
- Barrier does not exist; no replacement Barrier subsystem is introduced.
- Crown Prototype remains one enemy / one HP bar / no transformation and exposes the pre-existing Relentless Flurry Card after first clear.
- Chapter 4 expected ordinary random-encounter planning remains **19** with **5,262 ordinary EXP / 11,200 total mandatory EXP** under current progression authority; these are planning/expected values, not a hardcoded battle quota.

## Current terminology overlay

Current-facing production text must use later canon where older exact files retain historical labels:
- Yahtrenhold, not Southhold / The Crownhold;
- Reaction Annex, not Sixfold Annex;
- Reaction Node, not Sixfold Node;
- Reaction Conduit, not Elemental Hexarch;
- Regulation Crucible, not Sixfold Crucible;
- Fire / Ice / Lightning / Earth only for Chapter-4 combat-element research/regulation;
- Base Hit, not natural Accuracy;
- Spirit for magical defense;
- no Barrier, no Brace, no global Break/Stagger meter.

Ordinary environmental water, rain, condensation, or wind remain normal physical/weather descriptions when clearly not elemental-system labels.

## Next source-authoring frontier

Completed Chapters 0–4 remain closed. Later scene authoring follows the user's selected workstream and current chapter authority; do not assume Chapter 5 must always be the next task.