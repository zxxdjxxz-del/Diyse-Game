# Diyse — Open Work Audit

**Status:** CURRENT / ROUTING AUDIT

This file is the consolidated index of genuinely unfinished work. It does **not** replace owner-domain files or detailed working trackers. `ACTIVE_WORK_QUEUE.md` remains the prioritization/sequencing authority.

## 1 — Approval Needed Now

### Visual B00 — Ilyra
- Ilyra's permanent-party new-style master remains in **cleanup/remake review OPEN** state.
- The immediate decision gate is the B00 remake/clothing review against her approved character appearance and the current Diyse visual direction.
- Cyanis's high-resolution new-style master is already locked and is not part of this approval gate.

No other current production backlog should be mislabeled as requiring a fresh canon decision merely because it is unfinished.

## 2 — Production Backlog

### Playable area & route layout production
The project has macro geography and route sequencing, but does **not** yet have build-ready playable maps for the full game.

Still required:
- inventory every gameplay-relevant area/sub-area;
- create actual field/town/dungeon/facility/Hunt blockouts;
- define entrances/exits and transitions;
- map critical paths, optional loops, shortcuts and dead ends;
- establish landmarks, sightlines and navigation readability;
- define elevation and HD-2D layer composition;
- reserve encounter spaces and boss/Hunt arenas;
- place traversal gates, authored interactions, rewards and state changes;
- set approximate scale and pacing targets;
- create tool-agnostic environment-generation handoff packets.

The existing world map, `ROADS_AND_CHAPTER_TRAVEL.md`, and local quest sequences constrain this work but do not replace it.

Layout/blockout design can proceed in parallel with visual certification. Final rendered environment production should follow the relevant B01–B11 benchmark approvals.

Working pointer:
`AREA_AND_ROUTE_LAYOUT_PRODUCTION_WORKING.md`

### Visual production
- Produce the remaining permanent-party new-style masters for **Torren, Nimera, Vaelira, and Seyrik**, plus finish Ilyra after her review gate.
- Complete battle-scale and field-scale derivative validation.
- Produce/certify environment and material benchmark gates **B01–B11** before bulk environment conversion.

### Dialogue
- Complete the already-approved Chapter-5 Seyrik/Rhazek beat rewrite.
- Line-author Chapter 5 after that rewrite.
- Continue exact dialogue through Chapters 6–13 using the current scene architecture.
- Complete remaining optional Side Quest / Character Quest dialogue where not already finished.

Chapters 0–4 are line-complete and are not part of this backlog.

### Implementation
- Reconcile runtime/UI/save/test proof structures to current canon.
- Remove stale Mastery Point assumptions.
- Implement current Prime behavior and update stale Prime tests.
- Use canonical **G** semantics and closed economy fixtures.
- Replace proof item/equipment/party fixtures with production data.
- Expand/version the save schema.
- Reconcile current Chapter-13 scene assumptions.
- Build production menu/combat/loadout/shop/Kessara-copy behavior against owner-domain values.

### Audio
- Audio/music redevelopment remains genuinely **OPEN**: soundtrack identity, cue hierarchy, regional language, battle/boss/Hunt/Prime music, leitmotifs, diegetic/voice scope, SFX palette, and mix/implementation targets.

## 3 — Intentionally Unresolved / Deferred Canon

These are intentionally open and should not be guessed into canon:
- exact ancient survival mechanism of the **sole Entity fragment**;
- exact cause of the missing middle/final Chapter-10 report;
- exact document dates/IDs for the Chapter-10 research trail;
- exact final survey prop;
- exact formal chapter titles for **Ch6, Ch8, Ch9, and Ch11** unless separately approved.

Exactly one Entity fragment survives. Retired alternate explanations must not be restored while the mechanism is unresolved.

## 4 — Story-Owned Placement / Timing Dependencies

These remain deferred until the relevant story/dialogue work resolves their scene role or trigger. They are routing dependencies, not independent economy-design gaps.

Current examples include:
- False-Warrant Adept exact placement/role;
- Highland Resistance Fighter exact Chapter-5 placement;
- Crown Engine Technician exact story placement;
- bounded Hunt return/unlock timing where the story trigger is not yet exact.

Any resulting special-encounter G placement remains downstream of the story decision and must consume the closed economy framework rather than reopening it.

## 5 — Certification / QA Backlog

### Area / route gameplay certification
After representative maps exist, validate:
- route readability without excessive waypoint dependence;
- traversal time and backtracking burden;
- collision and camera behavior;
- encounter-space readability;
- shortcuts and one-way gates;
- revisit-state correctness;
- Android performance for representative environment density.

### Visual certification
- B00 party-style completion and gameplay-scale derivative checks.
- B01–B11 environment/material benchmark certification.

### Audio validation
- Validate final cue/SFX/mix implementation after the audio direction and assets exist.

### Whole-game QA
When the relevant content/implementation layers are ready, run:
- campaign-only, light, typical, heavy, and completionist routes;
- boss/Hunt/Elite regression;
- economy validation against the already-closed G calibration;
- save/load and exploit testing;
- readability/input checks;
- Android performance QA.

This is certification debt, not a reason to treat settled canon or numeric systems as unauthored.

## 6 — Retired / Closed — NOT Active

Do **not** automatically route work back into these streams:
- core **G economy / reward calibration** — closed;
- chapter-scale G liquidity validation — closed/certified;
- enemy static/paper validation — closed;
- CEXP Lv55–60 recalibration — closed v92;
- former mandatory-route enemy-difficulty queue sequence centered on **First Command Warden / global ×1.20 sensitivity / boss-local retunes** — retired from the active queue;
- legacy giant-tracker migration — complete;
- repository documentation replacement/migration — complete.

The historical v103–v105 balance reports may still be used as evidence, but they do not define the current work sequence and must not silently reactivate that retired workflow.

## 7 — Audit Corrections

- `90_WORKING/README.md` no longer lists the retired mandatory-route difficulty recalibration as a current major stream.
- `IMPLEMENTATION_FRONTIER_WORKING.md` now uses canonical **G**; stale **Auren** runtime-migration language is removed and Auren is explicitly retired.
- Playable area/route layout production is now explicitly tracked; prior audits incorrectly treated macro geography and route sequencing as if they fully covered environment production.

## Routing Rule

Use this file to answer **what is actually still unfinished**. Use `ACTIVE_WORK_QUEUE.md` to answer **what should be worked on next**. Use the owning numbered domain or specific working tracker for the detailed rules.

Do not create a new open stream merely because a closed system still needs implementation, presentation, story placement, or later QA. Playable area/route layout is a genuine production stream because the actual explorable geometry has not yet been authored.
