# Diyse — Line-Complete Canon Dialogue Index

**Whole-project authority:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.73 / Audit88** — August 19, 2026.

This directory is the controlling repository-facing **line-complete production-authoring source** for completed Chapters 1–4. These files exist so approved dialogue can be validated, implemented and maintained without recovering, paraphrasing or re-authoring closed scenes.

## Authority hierarchy

1. Newer explicit user correction.
2. Complete Master Canon **v1.73 / Audit88** and its inherited authority chain.
3. The line-complete scene files in this directory.
4. Validated production Resources where conversion is complete and compatible with exact source.
5. Implementation-facing chapter lock/index files under `docs/chapters/`.
6. Compatible earlier approved material only where it does not conflict with newer authority.

## Runtime / authoring status

- Chapter 0: exact production dialogue Resources already merged/validated, subject to later canon compatibility overlays.
- Chapter 1: S007–S011 + C03–C05 converted and validated for exact source parity + whole-chapter continuity.
- Chapter 2: S012–S016 + C06/C07 converted and validated for exact source parity + whole-chapter continuity.
- Chapter 3: S017–S021 + H01–H04 converted and validated for exact source parity + whole-chapter continuity/Cresthaven locks.
- Chapter 4: S022–S026 + C08/C09/H05 + Crown Prototype exact production dialogue source is present; production `.tres` conversion/static validation is present where currently implemented. Runtime smoke/in-engine completion remains separate implementation QA.

There is no closed Chapter 0–4 **authoring** backlog. Do not treat missing presentation/map/trigger/runtime consumers as evidence that dialogue or canon is missing.

## HD-2D presentation boundary

Audit88 converts completed Chapters 0–4 to the approved HD-2D production grammar without changing exact dialogue.

Detailed production authority:

`docs/production/HD2D_CHAPTERS_00_04_CONVERSION_AUDIT_PASS_1.md`

Older scene-source references to affordable `2.5D` staging are historical implementation shorthand. Preserve their intended economy, but implement through the active HD-2D grammar: ~80 px field sprites, ~200 px battle sprites, large portraits, authored layered environments, restrained cameras, reusable battle backgrounds, state swaps and modular VFX.

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

The corrected S020→S021 handoff remains exact: post-Warden records prove false-order assembly; Torren copies routing geometry; the party returns to Mirena; Mirena identifies Cresthaven as an abandoned Crown outpost in Southhold; the next morning she is already there establishing it as headquarters.

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

Hard production/content locks include:

- Chapter starts with Cyanis / Ilyra / Torren / Nimera as the traveling permanent party; Maevra is not the default Chapter 4 traveling member.
- Vaelira joins permanently during S022; choose-four remains active after roster reaches five permanents.
- S022 Elder Briarhide is the first verified modern Last Sentinel manifestation.
- Last Sentinel manifests for one legal Prime action and dismisses in the same round; Elder Briarhide retreats alive.
- Elemental Hexarch is a harmed living researcher resolved nonlethally.
- Sixfold Crucible is a genuine two-form boss with fresh Form-II HP/MP and inherited survivor traits.
- Crown Prototype remains one enemy / one HP bar / no transformation and exposes the pre-existing Relentless Flurry Card after first clear.
- Random encounter quantity in Annex/Regulation traversal is area-driven; do not hardcode an expected approximate battle count into source authority.

## Next source-authoring frontier

Completed Chapters 0–4 remain closed. The next inherited exact scene-authoring/production frontier is **Chapter 5 — The Mountain Engine**, unless the user explicitly selects a different task.