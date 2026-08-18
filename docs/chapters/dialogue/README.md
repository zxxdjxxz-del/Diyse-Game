# Diyse — Line-Complete Canon Dialogue Index

**Whole-project authority:** Diyse Clean Active Complete Master Canon **v1.64 / Audit79** — August 18, 2026.

This directory is the controlling repository-facing **line-complete production-authoring source** for Chapters 1–3. These files exist so the approved dialogue can be converted into `DiyseDialogueSceneDefinition` Resources without recovering, paraphrasing, or re-authoring the scenes again.

## Authority hierarchy

1. Newer explicit user correction.
2. Complete Master Canon **v1.64 / Audit79**.
3. The line-complete scene files in this directory.
4. The implementation-facing chapter lock/index files in `docs/chapters/`.
5. Compatible earlier approved material only where it does not conflict with the above.

Chapter-specific transcript checkpoints inherited into v1.64:

- **Chapter 1:** Audit79 line-complete lock.
- **Chapter 2:** Audit78 line-complete lock, inherited unchanged into v1.64.
- **Chapter 3:** Audit77 line-complete lock plus the bounded S020→S021 Cresthaven correction carried into v1.64.

## Runtime status

These Markdown files are **canon/production-authoring source**, not proof that Chapters 1–3 have already been integrated into the live Godot runtime.

- Chapter 0: exact production dialogue Resources are already merged/validated, subject to later compatibility overlays.
- Chapters 1–3: exact authoring is closed and line-complete here; `.tres` Resource conversion/validation is still pending.

Resource conversion may normalize stable IDs, cue metadata, portrait-registry references, and other implementation-only fields. It may **not** rewrite approved dialogue, scene outcomes, knowledge firewalls, relationship progression, party-state changes, geography, or encounter/boss rules.

## Chapter 1 — Brackenwall and the Wayfinder

Mandatory:
- [S007 — Brackenwall / Protocol](chapter_01/S007.md)
- [S008 — Hollow Watch / What Woke Up](chapter_01/S008.md)
- [S009 — Greenhollow / What the Map Has Wrong](chapter_01/S009.md)
- [S010 — Briar Passage / The Route I Would Take](chapter_01/S010.md)
- [S011 — Wayfinder Junction / Six Ways Through](chapter_01/S011.md)

Optional Character-Life:
- [C03 — Torren's Version of Dinner](chapter_01/C03.md)
- [C04 — What the Map Says](chapter_01/C04.md)
- [C05 — Two Professionals Complaining About Cyanis](chapter_01/C05.md)

Important final-version note: Audit79 C04 uses the approved **“Old whore.” / “Bitch.”** misunderstanding. The older recovered `Whore/Shore` reconstruction is superseded.

## Chapter 2 — The Drowned Oath

Mandatory:
- [S012 — Dunmere / Poisoned Waterworks](chapter_02/S012.md)
- [S013 — Sunken Archive / Archive Leviathan](chapter_02/S013.md)
- [S014 — Prisoner Galleries](chapter_02/S014.md)
- [S015 — Red Transfer Bastion / Commander Rhazek](chapter_02/S015.md)
- [S016 — Extraction Causeway](chapter_02/S016.md)

Optional Character-Life:
- [C06 — Three People Who Know Each Other Now](chapter_02/C06.md)
- [C07 — Bad Dreams, No Questions](chapter_02/C07.md)

Important final-version note: Audit78 C07 Rewrite Draft 2 controls. The earlier protected C07 line set is retired. **Wet sleeves** is the approved callback; Torren lights his blunt from existing coals, not a modern lighter, and the scene does not frame his weed use as impairment or vice.

## Chapter 3 — The Old City and Last Sentinel

Mandatory:
- [S017 — Containment at Caelora](chapter_03/S017.md)
- [S018 — Order That Should Not Exist](chapter_03/S018.md)
- [S019 — Scholar in Redacted Stacks](chapter_03/S019.md)
- [S020 — Oath Sentinel](chapter_03/S020.md)
- [S021 — Four Answers, Not One](chapter_03/S021.md)

Optional hub / Character-Life:
- [H01 — Nimera Takes Over a Table](chapter_03/H01.md)
- [H02 — Torren and Maevra, Unsupervised](chapter_03/H02.md)
- [H03 — Ilyra and Nimera](chapter_03/H03.md)
- [H04 — Last Sentinel Is Not Invited](chapter_03/H04.md)

### Corrected S020→S021 handoff

The final bounded correction is part of the controlling text in the linked S020/S021 files:

1. Defeating the First Command Warden clears the command state and unlocks a command-record room.
2. The room preserves separate authentic judicial/custody inputs and the third false order assembled from them, proving **how** the order was falsely assembled.
3. Torren recognizes a second routing display as map-like and makes a practical copy.
4. The party returns to Mirena in Caelora with the evidence and Torren's map.
5. Mirena recognizes the destination as **Cresthaven**, an abandoned Crown outpost in Southhold.
6. The party stops for the night.
7. S021 begins the next morning with Mirena already at Cresthaven with workers, records staff, medical support, supplies, and security converting the abandoned outpost into the party's working headquarters while the investigation continues.

Hard geography remains:

**Caelora → Old City / Suppressed Archives → separate Cresthaven.**

Cresthaven is never the Warden chamber, a Suppressed Archive room, or a Caeloran district.
