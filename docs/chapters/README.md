# Diyse — Chapter Authority Index

**Current whole-project authority:** **v2.20 / Audit135** — August 27, 2026.  
**Presentation target:** HD-2D.

This directory is the repository-facing chapter authority index. Current chapter numbers, current scene IDs, and later canon overlays control implementation. Historical pre-insertion chapter numbers remain provenance only.

---

## Current chapter spine

| Chapter | Current identity / title | Authority state |
|---|---|---|
| 0 | The Broken Convoy | CLOSED / exact early-game authority |
| 1 | Brackenwall and the Wayfinder | CLOSED / line-complete source |
| 2 | The Drowned Oath | CLOSED / line-complete source |
| 3 | The Old City and Last Sentinel | CLOSED / line-complete corrected source |
| 4 | The Seventh Reaction | CLOSED / four-element exact production authority |
| 5 | current Chapter 5 | inherited current authority |
| 6 | current Chapter 6 | inherited current authority; Seyrik recruited by end |
| 7 | The Prison of Names | Sixfold Volition at end; first full-six chapter |
| 8 | current Westguard / Varkesh-era material | inherited current authority |
| 9 | Larkspire / Crownfall / Rhazek | inherited current authority |
| 10 | **The Last Blank** | Audit112 story architecture locked |
| 11 | **Crown Engine / Calder / Custodian / Truth** | current macro authority |
| 12 | **The Reforged March** | final Black Host campaign / Vhalmarch / Vaelkor / cleanup |
| 13 | **The Last Command** | final Ancient domain / Entity / Final Severance / ending |

---

## Post-insertion reindex — hard rule

Chapter 10 — **The Last Blank** was inserted after Chapter 9.

Therefore:
- old Ch10 → current **Ch11**;
- old Ch11 → current **Ch12**;
- old Ch12 → current **Ch13**.

Controlling reconciliation:
`docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`

Current late-game scene ranges:
- Ch9 — S047–S050
- Ch10 — S051–S061
- Ch11 — S062–S065
- Ch12 — S066–S069
- Ch13 — S070–S073

The three mandatory late-Ch12 **reciprocal-pair resolution beats** do not yet have standalone S### IDs. **Synthesis is removed** and must not be used as their current system/gating label.

---

## Current operational sources

- Ch10 — `chapter_10/CHAPTER_10_THE_LAST_BLANK_STORY_STRUCTURE_LOCK.md`
- Ch11 — `chapter_11/CHAPTER_11_CURRENT_SCOPE.md`
- Ch12 — `chapter_12/CHAPTER_12_REFORGED_MARCH_FORWARD_HUB_AND_CLEANUP_LOCK.md`
- Ch13 — `chapter_13/CHAPTER_13_MACRO_STORY_STRUCTURE_LOCK.md`

Current Ch11 is Crown Engine / Calder / Custodian / Truth. It does not contain the Forward Hub/Vaelkor campaign.

Current Ch12 is the final Black Host campaign. **Vhalmarch** is the Forward Hub after Varkesh defeat/capture.

Current Ch13 is the final Ancient-domain operation.

---

## Point of no return

Starting Chapter 13 is not the irreversible lock.

> **Last Shelter → Reactor Galleries = true point of no return.**

The player may enter Chapter 13 and advance through Last Weapon Archive / Last Weapon Archon / Last Shelter while retaining supported return to eligible world content.

---

## Current terminology

Use current-facing:
- Yahtrenhold
- Black Host Territory
- The Blackspine
- Westguard
- Vhalmarch
- Vorathen
- The Veiled Citadel
- Acuity / Last Cartographer

Do not restore current-facing:
- Southhold / The Crownhold
- Blackstone
- Black Mountains
- Westreach / Yahtrens Stand
- Resource / Last Measure

---

## Current progression overlay

Audits123–128 close:
- class Ability MP certification;
- CL13 CEXP curve;
- exact 8-point Mastery schedule;
- player-level spine;
- mandatory formation EXP/CEXP allocation;
- exact mandatory named/story EXP+CEXP placement.

Normal-route anchors:
- Ch1 5
- Ch2 9
- Ch3 13
- Ch4 17
- Ch5 22
- Ch6 27
- Ch7 32
- Ch8 37
- Ch9 42
- Ch10 47
- Ch11 52
- Ch12 57
- Last Shelter 60
- End Ch13 62
- cap 70

Audits129–135 close progression-dependent raw-stat recertification for:
- mandatory named/special encounters;
- 12 numbered-chapter optional Elites;
- 11 Regional Hunts;
- 6 Major Hunts.

Fixed authored Hunt tuning remains active; no dynamic scaling.

---

## Chapters 0–4 closure

| Chapter | Closed set | Repository state |
|---|---|---|
| 0 | S001–S006 + C01/C02 | Exact dialogue Resources merged/validated. |
| 1 | S007–S011 + C03–C05 | Line-complete source + validated Resources. |
| 2 | S012–S016 + C06/C07 | Line-complete source + validated Resources. |
| 3 | S017–S021 + H01–H04 | Line-complete corrected source + continuity validation. |
| 4 | S022–S026 + C08/C09/H05 + Crown Prototype | Exact source closed; current four-element overlay controls stale terminology. |

There is no Chapters 0–4 story/dialogue authoring backlog.

Chapter 4 current-facing rules:
- exactly Fire / Ice / Lightning / Earth;
- Reaction Annex, not Sixfold Annex;
- Reaction Conduit, not Elemental Hexarch;
- Regulation Crucible → fresh **The Seventh Reaction**;
- exactly four chambers with two active/targetable at once;
- no Wind/Water regulation states;
- no Barrier;
- no third form.

Use `dialogue/README.md` as the line-complete scene-source index.

---

## HD-2D closure

Completed Chapters 0–4 passed HD-2D Conversion Audit Pass 1 and cross-chapter consistency/cost consolidation.

Controlling production record:
`docs/production/HD2D_CHAPTERS_00_04_CONVERSION_AUDIT_PASS_1.md`

Current consequences:
- HD-2D only;
- ~80 px field characters;
- ~200–220 px battle characters;
- large dialogue portraits;
- four active party members left / enemies right / open center lane;
- layered authored environments and restrained cameras;
- random encounters begin as normal campaign grammar from Chapter 1.

---

## Implementation boundary

Bounded implementation corrections may update stable IDs, Resource metadata, internal labels, cues, triggers, maps, presentation assets, battle-background consumers, or other runtime plumbing without reopening approved dialogue, scene purpose, relationships, geography, knowledge state, roster changes, or outcomes.

Historical audits remain useful provenance, but current chapter folders, current scene IDs, and later canon overlays control implementation.