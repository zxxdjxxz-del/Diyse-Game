# Diyse — Completed Chapters 0–4 Authority Index

**Current whole-project authority:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.73 / Audit88** (August 19, 2026).

This directory is the repository-facing implementation/recovery index for the completed early-game chapters. It exists so implementation work can use already-approved scenes without reopening story, dialogue, characterization, relationship progression, knowledge firewalls, gameplay outcomes or HD-2D conversion decisions.

## Closure state

| Chapter | Title | Closed scene set | Repository state |
|---|---|---|---|
| 0 | The Broken Convoy | S001–S006 + C01/C02 | Exact dialogue Resources merged/validated; later canon overlays control incompatible historical internal terminology. |
| 1 | Brackenwall and the Wayfinder | S007–S011 + C03–C05 | Line-complete source + production `.tres` Resources; exact source-parity and whole-chapter continuity validated. |
| 2 | The Drowned Oath | S012–S016 + C06/C07 | Line-complete source + production `.tres` Resources; exact source-parity and whole-chapter continuity validated. |
| 3 | The Old City and Last Sentinel | S017–S021 + H01–H04 | Line-complete corrected source + production `.tres` Resources; exact source-parity and whole-chapter continuity/Cresthaven validation passed. |
| 4 | The Seventh Reaction | S022–S026 + C08/C09/H05 + Crown Prototype | Exact production dialogue source closed; `.tres` conversion/static validation present where currently implemented; runtime smoke/in-engine completion remains separate implementation QA. |

There is no Chapters 0–4 story/dialogue authoring backlog.

## HD-2D conversion closure

All completed Chapters 0–4 have now passed **HD-2D Conversion Audit, Pass 1** plus a cross-chapter consistency/cost-consolidation pass.

Controlling production record:

`docs/production/HD2D_CHAPTERS_00_04_CONVERSION_AUDIT_PASS_1.md`

Key global consequences:

- HD-2D is the sole active presentation target.
- Field characters ~80 px.
- Battle characters ~200 px.
- Large high-resolution dialogue portraits.
- Four active party members left / enemies right / open center battle lane.
- Layered authored environments, restrained cameras and selective geometry.
- Small reusable battle-background families derived from field geography.
- Chapter 0 retains seven authored tutorial encounters; normal random-encounter grammar begins in Chapter 1.
- Exact visual masters and exact Yahtrea world-map geography remain controlling.
- Older affordable-`2.5D` notes are reinterpreted as economical HD-2D staging rather than active presentation authority.

## Exact dialogue source

Use `dialogue/README.md` as the scene-level source index.

Chapters 1–4 have exact scene-level Markdown under `docs/chapters/dialogue/`. Chapter lock/index documents are implementation guardrails and should not be used to reconstruct exact wording when line-complete source exists.

Chapter 0 exact line/cue data remains the merged Resource set at commit `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5` where compatible with later canon.

## Authority order

1. Newer explicit user correction.
2. Complete Master Canon **v1.73 / Audit88**.
3. Audit88 HD-2D conversion record.
4. Line-complete scene files under `docs/chapters/dialogue/`.
5. Validated production Resources where compatible with exact source.
6. Chapter lock/index files in this directory.
7. Compatible earlier approved material only where it does not conflict with the above.

## Chapter 3 geography / Prime chronology lock

Chapter 3 travels:

**Caelora → Old City / Suppressed Archives → separate Cresthaven**

The final S020→S021 handoff proves the false order's assembly, has Torren copy a routing display, returns the party to Mirena, identifies Cresthaven as an abandoned Crown outpost in Southhold and begins S021 the next morning with Mirena already establishing the headquarters.

S021 identifies/unlocks Last Sentinel but does not manifest it. First verified modern Prime manifestation occurs in S022's Elder Briarhide encounter.

## Chapter 4 roster / Prime lock

Chapter 4 starts with permanent travelers Cyanis / Ilyra / Torren / Nimera. Maevra is not the default traveling member. Vaelira joins permanently during S022, taking the permanent roster to five while battle formation remains choose-four.

S022's Last Sentinel use establishes the first approved C3/V4 early-game event and the reusable Prime presentation pipeline.

## Implementation boundary

A bounded implementation correction may update stable IDs, Resource metadata, internal labels, cue support, triggers, maps, presentation assets, battle-background consumers or other runtime plumbing without reopening approved wording, scene purpose, protected beats, relationships, geography, knowledge firewall, party-state changes or outcomes.

Historical internal names such as `Broken Champion's Ward` remain non-player-facing legacy handles and do not override current canon.

## Next frontier

- **Closed-chapter story/dialogue authoring:** none for Chapters 0–4.
- **Completed-chapter HD-2D conversion audit:** COMPLETE / PASS / GREEN.
- **Follow-on runtime implementation:** may now implement Chapters 0–4 against Audit88 without rewriting them.
- **Next inherited scene-production/audit frontier:** Chapter 5 — **The Mountain Engine**, unless the user explicitly chooses another task.