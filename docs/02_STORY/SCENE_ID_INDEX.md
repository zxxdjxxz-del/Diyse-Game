# Diyse — Mandatory Story Scene-ID Index
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, read through all later explicit user corrections and current domain migrations.  
**Primary story authorities:** current chapter index; current lean chapter structures; Audits 91/92/107/109/112/113; current Chapter-11/12/13 operational projections; current Prime/character/world corrections.  
**Domain rule:** this folder owns mandatory story structure, chapter purpose, scene order, reveal order, recruitment/Prime milestones, interchapter causality, and story-state outcomes. Exact spoken dialogue belongs in `03_DIALOGUE`; battle numbers in `09_ENEMIES_AND_ENCOUNTERS`; progression numbers in `10_PROGRESSION_AND_EXP`.

## Scene-ID rule after Dialogue Engine restructuring

A retained S### range identifies the stable mandatory **scene-routing IDs** that survive into current implementation. It does **not** mean the historical exact transcript remains current wording.

Current all-dialogue regeneration authority applies:
- current lean `02_STORY` structure owns what each retained scene function must accomplish;
- `03_DIALOGUE` owns regenerated spoken wording;
- historical line-complete dialogue is reference/provenance only unless an individual exact line is explicitly preserved by current authority;
- inserted encounter/story beats do not automatically receive new S### IDs merely because the lean chapter now contains more story beats than the historical scene count.

| Chapter | Mandatory scene IDs | Current routing status |
|---|---|---|
| Ch0 | S001–S006 | **IDs retained; lean scene functions current; spoken dialogue regeneration pending** |
| Ch1 | S007–S011 | **IDs retained; current lean structure controls; detailed beat→S### routing requires current mapping where not explicit** |
| Ch2 | S012–S016 | **IDs retained; current lean structure/dialogue regeneration controls** |
| Ch3 | S017–S021 | **IDs retained; current lean structure/dialogue regeneration controls** |
| Ch4 | S022–S026 | **IDs retained; current lean structure + four-element overlay control** |
| Ch5 | current detailed S-range not promoted here | beat/macro authority |
| Ch6 | includes S035 / S036 inherited anchors | macro/beat authority |
| Ch7 | current detailed S-range not promoted here | macro authority |
| Ch8 | current detailed S-range not promoted here | macro authority |
| Ch9 | S047–S050 | macro locked |
| Ch10 | S051–S061 | detailed story skeleton locked |
| Ch11 | S062–S065 | macro locked |
| Ch12 | S066–S069 | macro locked; reciprocal-pair resolution beats have no standalone S### IDs |
| Ch13 | S070–S073 | macro locked |

## Current Chapter-0 routing clarification

Chapter 0 currently has **eight lean mandatory story beats** but retains **six S### dialogue-routing IDs**.

Current mapping:
- **S001** → Beat 1 — Convoy / Opening Ambush;
- **S002** → Beat 2 — Wreck Field;
- **S003** → Beat 3 — Evacuation Relay Decision;
- **S004** → Beat 4 — Field Triage Camp / Ilyra / First Incomplete Response;
- **Beat 5 — Concealed Ruin Vanguard / Seyrik** → mandatory encounter/story placement, **no standalone S### ID**;
- **Beat 6 — Riftmaw** → mandatory encounter/boss placement, **no standalone S### ID**;
- **S005** → Beat 7 — Final Broken Convoy Confrontation / Second Incomplete Response;
- **S006** → Beat 8 — Aftermath / Survivor Recovery / Overnight Camp.

Therefore current S004 must not flow directly into S005. Required current sequence is:

> **S004 → Beat 5 concealed Seyrik encounter → noncombat triage/repositioning interval → Beat 6 Riftmaw encounter → noncombat field/triage interval → S005 → S006**

The inserted Beat-5/Beat-6 encounter placements may use encounter-local pre/post microbeats or battle presentation hooks where needed, but those hooks do not become new S### IDs unless `02_STORY` explicitly promotes new scene IDs later.

Existing Chapter-0 `.tres` Resources and historical tests that still stage S004 → S005 directly are legacy implementation proof and must be regenerated/reworked before production Chapter-0 delivery.

## Current Chapter-10 scene sequence
- S051 — The Missing Middle
- S052 — East of Cerythvale
- S053 — The Old Road
- S054 — Another Wayfinder
- S055 — What the Crown Did Here
- S056 — The Prime Research
- S057 — The Convoy
- S058 — Real Pieces
- S059 — Where They Stopped
- S060 — Beyond the Excavation
- S061 — The Order That Was Missing

## Current Chapter-11 sequence
- S062 — The Living Anchor
- S063 — The Custodian
- S064 — The Truth Beneath the Empire
- S065 — First Reckoning

## Current Chapter-12 sequence
- S066 — Into the Imperial Heartland
- S067 — The March That Refuses Empire Logic
- S068 — Varkesh Taken Alive
- S069 — Emperor Vaelkor Draeven

## Current Chapter-13 sequence
- S070 — The Deepest City
- S071 — The Reconstituted Entity
- S072 — No One Is Last Command
- S073 — Last Command

Do not reuse the pre-insertion S051–S062 numbering for old late-game material.
