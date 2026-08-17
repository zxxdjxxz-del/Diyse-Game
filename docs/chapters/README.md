# Diyse — Completed Chapters 0–3 Authority Index

**Current story/dialogue authority:** Complete Master Canon **v1.60 / Audit75** (August 17, 2026).

This directory is the repository-facing recovery package for the four completed early-game chapters. It exists so implementation work can translate the already-approved chapters into Godot Resources without repeatedly reopening story, dialogue, characterization, pair progression, knowledge firewalls, or 2.5D staging decisions.

## Closure state

| Chapter | Title | Closed scene set | Repository implementation state |
|---|---|---|---|
| 0 | The Broken Convoy | S001–S006 + C01/C02 | Exact dialogue Resources already merged/validated; later canon overlays control interpretation where they supersede old internal terminology. |
| 1 | Brackenwall and the Wayfinder | S007–S011 + C03–C05 | Story/dialogue/2.5D authority CLOSED. Resource conversion/validation still pending. |
| 2 | The Drowned Oath | S012–S016 + C06/C07 | Story/dialogue/2.5D authority CLOSED. Resource conversion/validation still pending. |
| 3 | The Old City and Last Sentinel | S017–S021 + H01–H04 | Story/dialogue/2.5D authority CLOSED. Resource conversion/validation still pending. |

**Closed does not mean runtime-integrated.** Chapter 0 is the only one of these four whose complete scene set currently exists as validated `.tres` production Resources in this repository. Chapters 1–3 are closed authoring authority and must be translated into the accepted `DiyseDialogueSceneDefinition` schema without re-authoring them.

## Authority order

1. Newer explicit user correction.
2. Complete Master Canon v1.60 / Audit75.
3. The closed chapter authority files in this directory.
4. Compatible approved production dialogue/source artifacts.
5. Historical or exploratory material only when it does not conflict with the above.

Chapter 0 exact line/cue data remains the merged Resource set at commit `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5` **where compatible with later canon**. In particular, older internal `Broken Champion's Ward` / `First Champion` interpretations are superseded by the neutral incomplete Card-protection interpretation documented in `CHAPTER_00_COMPLETE.md`.

## Chapter 3 geography lock

Chapter 3 travels:

**Caelora → Old City / Suppressed Archives → separate Cresthaven**

Cresthaven is not a room, wing, chamber, or district inside Caelora's Old City. S021 and H04 are staged at the separate Cresthaven site.

## Affordable 2.5D baseline

Completed Chapters 0–3 passed the current feasibility baseline with no RED scene. Implement them with reusable portraits/poses, prop states, authored before/after environment states, prepared gates/routes, camera inserts, layered crowds, VFX, and silence. Do not create bespoke animation chains, physics destruction, fluid simulation, crowd AI, or actor-body copying merely because prose describes a physical action in detail.

## Next authoring frontier

**Chapter 4 — The Seventh Reaction.**

Runtime Resource conversion/validation for Chapters 1–3 is implementation work on closed material, not a reason to rewrite those chapters.