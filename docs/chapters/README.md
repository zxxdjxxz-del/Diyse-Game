# Diyse — Chapter Authority Index

**Current whole-project authority:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.74 / Audit89** (August 20, 2026).

This directory is the repository-facing implementation/recovery index for completed early-game chapters and later chapter-specific macro locks. It exists so implementation work can use already-approved material without reopening story, dialogue, characterization, relationship progression, knowledge firewalls, gameplay outcomes or HD-2D conversion decisions.

## Closure state — Chapters 0–4

| Chapter | Title | Closed scene set | Repository state |
|---|---|---|---|
| 0 | The Broken Convoy | S001–S006 + C01/C02 | Exact dialogue Resources merged/validated; later canon overlays control incompatible historical internal terminology. |
| 1 | Brackenwall and the Wayfinder | S007–S011 + C03–C05 | Line-complete source + production `.tres` Resources; exact source-parity and whole-chapter continuity validated. |
| 2 | The Drowned Oath | S012–S016 + C06/C07 | Line-complete source + production `.tres` Resources; exact source-parity and whole-chapter continuity validated. |
| 3 | The Old City and Last Sentinel | S017–S021 + H01–H04 | Line-complete corrected source + production `.tres` Resources; exact source-parity and whole-chapter continuity/Cresthaven validation passed. |
| 4 | The Seventh Reaction | S022–S026 + C08/C09/H05 + Crown Prototype | Exact production dialogue source closed; `.tres` conversion/static validation present where currently implemented; runtime smoke/in-engine completion remains separate implementation QA. |

There is no Chapters 0–4 story/dialogue authoring backlog.

## Later chapter macro locks

Audit89 adds repository-facing macro-story authority for Chapters 11–12 without claiming line-complete scene production:

- `chapter_11/CHAPTER_11_FORWARD_HUB_AND_FINAL_CLEANUP_WINDOW_LOCK.md`
  - Varkesh defeat/capture now precedes Forward Hub establishment;
  - post-Vaelkor cleanup and deliberate Chapter 12 launch remain locked.
- `chapter_11/ACCEPTANCE_LOG.md`
  - CH11-A002 records the Audit89 Chapter 11 campaign/Elite/Hunt/Vaelkor alignment.
- `chapter_12/CHAPTER_12_MACRO_STORY_STRUCTURE_LOCK.md`
  - locks the Chapter 12 physical progression, fragment reveal, Last Weapon Archon, Reconstituted Entity → Last Command, Final Severance and aftermath.
- `chapter_12/ACCEPTANCE_LOG.md`
  - CH12-A001 records the Audit89 final-operation authority.

Whole-project controlling promotion:

`docs/canon/AUDIT89_CHAPTERS_11_12_MACRO_STORY_STRUCTURE_AND_FINAL_ACT_CAUSALITY_LOCK.md`

These later chapter files are macro structure, **not** line-complete dialogue.

## HD-2D conversion closure

All completed Chapters 0–4 have passed **HD-2D Conversion Audit, Pass 1** plus a cross-chapter consistency/cost-consolidation pass.

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

Chapters 11–12 do **not** yet have line-complete dialogue under Audit89; future scene work must be derived from the macro locks rather than invented from obsolete material.

## Authority order

1. Newer explicit user correction.
2. Complete Master Canon **v1.74 / Audit89**.
3. Audit89 Chapters 11–12 macro-story/final-act causality lock where applicable.
4. Audit88 HD-2D conversion record for Chapters 0–4.
5. Line-complete scene files under `docs/chapters/dialogue/` where they exist.
6. Validated production Resources where compatible with exact source.
7. Chapter lock/index files in this directory.
8. Compatible earlier approved material only where it does not conflict with the above.

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

Audit89 similarly does not authorize silent changes to Chapter 11–12 knowledge/reveal order, Varkesh→Forward Hub timing, Elite/Hunt categories, Vaelkor forms, Last Weapon survival mechanism, final-boss forms, Final Severance functions or aftermath outcome.

## Next frontier

- **Closed-chapter story/dialogue authoring:** none for Chapters 0–4.
- **Completed-chapter HD-2D conversion audit:** COMPLETE / PASS / GREEN.
- **Follow-on runtime implementation:** may implement Chapters 0–4 against Audit88 without rewriting them.
- **Chapters 11–12:** macro story locked under Audit89; detailed scene production remains future work.
- **Next inherited scene-production/audit frontier:** Chapter 5 — **The Mountain Engine**, unless the user explicitly chooses another task.
