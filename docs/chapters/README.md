# Diyse — Chapter Authority Index

**Current whole-project authority:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.98 / Audit113** (August 23, 2026).

This directory is the repository-facing implementation/recovery index for chapter authority. Current chapter numbers must follow Audit113; historical pre-insertion chapter numbers are provenance only.

## Current mandatory chapter spine

| Chapter | Current identity / title | Repository authority state |
|---|---|---|
| 0 | The Broken Convoy | CLOSED / early-game exact authority |
| 1 | Brackenwall and the Wayfinder | CLOSED / line-complete repo source |
| 2 | The Drowned Oath | CLOSED / line-complete repo source |
| 3 | The Old City and Last Sentinel | CLOSED / line-complete corrected repo source |
| 4 | The Seventh Reaction | CLOSED / exact production source |
| 5 | inherited current Chapter 5 | detailed production frontier remains separate |
| 6 | inherited current Chapter 6 | macro/story authority inherited |
| 7 | The Prison of Names | first full-six chapter; Sixfold Volition at end/Cresthaven return |
| 8 | current Westguard/Varkesh-era predecessor chapter material | inherited current authority |
| 9 | Larkspire / Crownfall / Rhazek | inherited current authority |
| 10 | **The Last Blank** | Audit112 story architecture locked; ~55–65 min target |
| 11 | **Crown Engine / Calder / Custodian / Truth** | current macro authority; detailed scene production pending |
| 12 | **The Reforged March** | final Black Host campaign; Vhalmarch Forward Hub; Vaelkor; cleanup |
| 13 | **The Last Command** | final Ancient domain / Entity / Final Severance / ending |

## Post-insertion reindex — hard rule

Chapter 10 — The Last Blank was inserted after Chapter 9.

Therefore:
- former Chapter 10 → **current Chapter 11**;
- former Chapter 11 → **current Chapter 12**;
- former Chapter 12 → **current Chapter 13**.

Do not implement old late-game chapter numbers merely because an historical audit filename still contains them.

Controlling reconciliation:
`docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`

## Current late-game operational sources

### Chapter 10
`chapter_10/CHAPTER_10_THE_LAST_BLANK_STORY_STRUCTURE_LOCK.md`

Full story authority:
`docs/canon/AUDIT112_CHAPTER_10_THE_LAST_BLANK_MIRENA_EASTERN_WAYFINDER_CALDER_AND_BURIED_REGISTRY_CLOSURE.md`

### Chapter 11
`chapter_11/CHAPTER_11_CURRENT_SCOPE.md`

Current Chapter 11 is **Crown Engine / Calder / Custodian / Truth**. It does **not** contain the Forward Hub/Vaelkor campaign.

### Chapter 12
`chapter_12/CHAPTER_12_REFORGED_MARCH_FORWARD_HUB_AND_CLEANUP_LOCK.md`

`chapter_12/ACCEPTANCE_LOG.md`

Current Chapter 12 is the final Black Host campaign formerly labeled Chapter 11. **Vhalmarch** is the Forward Hub after Varkesh defeat/capture.

### Chapter 13
`chapter_13/CHAPTER_13_MACRO_STORY_STRUCTURE_LOCK.md`

`chapter_13/ACCEPTANCE_LOG.md`

Current Chapter 13 is the former Chapter-12 final Ancient-domain operation.

## Current point of no return

Starting Chapter 13 is deliberate but is **not** the irreversible lock.

Audit109 controls:

**Last Shelter → Reactor Galleries = true point of no return.**

The player may enter Chapter 13 and advance through the Last Weapon Archive / Last Weapon Archon / Last Shelter while retaining supported return to eligible world content.

Any older chapter file saying `Chapter 12 launch` or `Chapter 13 launch` is itself the true PONR is stale.

## Current late-game terminology

Use:
- **Yahtrenhold**, not The Crownhold / Southhold;
- **Black Host Territory**, not Blackstone as region name;
- **The Blackspine**, not Black Mountains;
- **Westguard**, not Westreach / Yahtrens Stand;
- **Vhalmarch** = Chapter-12 Forward Hub;
- **Acuity / Last Cartographer**, not Resource / Last Measure.

## Closure state — Chapters 0–4

| Chapter | Closed scene set | Repository state |
|---|---|---|
| 0 | S001–S006 + C01/C02 | Exact dialogue Resources merged/validated; later canon overlays control incompatible historical terminology. |
| 1 | S007–S011 + C03–C05 | Line-complete source + production Resources; source parity/continuity validated. |
| 2 | S012–S016 + C06/C07 | Line-complete source + production Resources; source parity/continuity validated. |
| 3 | S017–S021 + H01–H04 | Line-complete corrected source + production Resources; continuity/Cresthaven validation passed. |
| 4 | S022–S026 + C08/C09/H05 + Crown Prototype | Exact production dialogue source closed; runtime/static validation present where implemented. |

There is no Chapters 0–4 story/dialogue authoring backlog.

## Exact dialogue source

Use `dialogue/README.md` as the scene-level source index.

Chapters 1–4 have exact scene-level Markdown under `docs/chapters/dialogue/`. Chapter lock/index documents are implementation guardrails and should not reconstruct exact wording when line-complete source exists.

## HD-2D conversion closure

Completed Chapters 0–4 passed HD-2D Conversion Audit Pass 1 plus cross-chapter consistency/cost consolidation.

Controlling production record:
`docs/production/HD2D_CHAPTERS_00_04_CONVERSION_AUDIT_PASS_1.md`

Current presentation consequences remain:
- HD-2D is the sole active presentation target;
- field characters ~80 px;
- battle characters ~200–220 px;
- large high-resolution dialogue portraits;
- four active party members left / enemies right / open center action lane;
- layered authored environments and restrained cameras;
- random encounters begin as normal campaign grammar from Chapter 1.

## Implementation boundary

A bounded implementation correction may update stable IDs, Resource metadata, internal labels, cue support, triggers, maps, presentation assets, battle-background consumers, or other runtime plumbing without reopening approved wording, scene purpose, relationships, geography, knowledge firewalls, party-state changes, or outcomes.

Historical audit version numbers and old acceptance IDs remain useful provenance, but **current chapter folders and current chapter numbers control implementation**.

For late-game work, never use the pre-insertion `chapter_11 = Forward Hub/Vaelkor` or `chapter_12 = final domain` arrangement.
