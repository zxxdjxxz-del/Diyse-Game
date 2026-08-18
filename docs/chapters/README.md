# Diyse — Completed Chapters 0–3 Authority Index

**Current whole-project authority:** Diyse Clean Active Complete Master Canon **v1.64 / Audit79** (August 18, 2026).

This directory is the repository-facing implementation/recovery index for the completed early-game chapters. It exists so implementation work can translate already-approved scenes into Godot Resources without reopening story, dialogue, characterization, relationship progression, knowledge firewalls, or affordable-2.5D staging decisions.

## Closure state

| Chapter | Title | Closed scene set | Repository implementation state |
|---|---|---|---|
| 0 | The Broken Convoy | S001–S006 + C01/C02 | Exact dialogue Resources already merged/validated; later canon overlays control where they supersede old internal terminology. |
| 1 | Brackenwall and the Wayfinder | S007–S011 + C03–C05 | **Line-complete canon source present in `dialogue/chapter_01/`;** Resource conversion/validation pending. |
| 2 | The Drowned Oath | S012–S016 + C06/C07 | **Line-complete canon source present in `dialogue/chapter_02/`;** Resource conversion/validation pending. |
| 3 | The Old City and Last Sentinel | S017–S021 + H01–H04 | **Line-complete corrected canon source present in `dialogue/chapter_03/`;** Resource conversion/validation pending. |

**Closed does not mean runtime-integrated.** Chapter 0 is still the only early chapter whose complete scene set currently exists as validated production `.tres` Resources. Chapters 1–3 are line-complete authoring authority and must be translated into the accepted `DiyseDialogueSceneDefinition` schema without re-authoring them.

## Exact dialogue source

Use [`dialogue/README.md`](dialogue/README.md) as the scene-level index.

For Chapters 1–3, the scene Markdown files under `docs/chapters/dialogue/` control exact approved wording and detailed production staging. The `CHAPTER_0X_COMPLETE.md` documents remain implementation-facing lock/index files and should not be used to reconstruct dialogue from summaries when the exact scene file exists.

## Authority order

1. Newer explicit user correction.
2. Complete Master Canon **v1.64 / Audit79**.
3. Line-complete scene files in `docs/chapters/dialogue/`.
4. Chapter lock/index files in this directory.
5. Compatible earlier approved material only where it does not conflict with the above.

Chapter 0 exact line/cue data remains the merged Resource set at commit `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5` where compatible with later canon. Older internal `Broken Champion's Ward` / `First Champion` interpretation remains superseded by the neutral incomplete Card-protection interpretation documented in `CHAPTER_00_COMPLETE.md`.

## Chapter 3 geography / Cresthaven correction

Chapter 3 travels:

**Caelora → Old City / Suppressed Archives → separate Cresthaven**

The final S020→S021 handoff is now explicit in the line-complete source: the post-Warden command-record room proves how the false order was assembled; Torren copies a map-like routing display; the party returns to Mirena; Mirena identifies the destination as **Cresthaven, an abandoned Crown outpost in Southhold**; and the next morning she is already there with workers/staff establishing it as a working headquarters while the investigation continues.

Cresthaven is never the Warden chamber, a Suppressed Archive room, or a district inside Caelora.

## Affordable 2.5D baseline

Completed Chapters 0–3 passed the current feasibility baseline with no RED scene. Implement them with reusable portraits/poses, prop states, authored before/after environment states, prepared gates/routes, camera inserts, layered crowds, VFX, and silence. Do not create bespoke animation chains, physics destruction, fluid simulation, crowd AI, or actor-body copying merely because prose describes a physical action in detail.

## Next authoring frontier

**Chapter 4 — The Seventh Reaction.**

Runtime Resource conversion/validation for Chapters 1–3 is implementation work on closed material, not a reason to rewrite those chapters.
