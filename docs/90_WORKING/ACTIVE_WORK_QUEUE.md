# Diyse — Active Work Queue

This queue tracks unresolved/reopened work only. Closed owner-domain values remain closed unless a current test or explicit user revision changes them.

## 1 — Story-Owned Enemy Placement / Timing Dependencies
**DEFERRED UNTIL RELEVANT STORY/DIALOGUE WORK**

Examples include:
- False-Warrant Adept exact placement/role;
- Highland Resistance Fighter exact Chapter-5 placement;
- Crown Engine Technician exact story placement;
- bounded Hunt return/unlock timing where the story trigger is not yet exact.

Economy consequence:
> exact G for story-dependent special encounters remains deferred until the owning scene role is finalized.

## 2 — Chapter 4 Dialogue Rewrite + Later-Chapter Dialogue
Chapters **0–3** are line-complete.

Chapter 4's current story/beat structure is established, but its exact dialogue rewrite remains **OPEN**.

Chapters 5–13 remain development-in-progress and require additional dialogue/story work; do not treat them as line-complete merely because older scene architecture exists.

Current dialogue backlog:
- rewrite Chapter 4 against the current redesigned beat structure;
- preserve the approved Chapter-5 Seyrik/Rhazek rewrite work as later-chapter source material;
- continue Chapters 5–13 only through their current development-in-progress authority.

Optional Side Quest / Character Quest exact dialogue remains open where not separately completed.

## 3 — Playable Area & Route Layout Production
**ACTIVE / PHASE A INVENTORY COMPLETE ENOUGH / PHASE B BLUEPRINT + GRAYBOX STARTED**

The current world map and macro travel order do **not** constitute production-ready playable maps.

Completed in the current pass:
- created `PLAYABLE_AREA_INVENTORY_WORKING.md` covering mandatory Chapters 0–13, persistent hubs, Character Quests, Side Quests, Regional Hunts and Major Hunts;
- established layout maturity states L0–L3;
- confirmed that current production areas are not yet L3 build-ready topology;
- created `AREA_LAYOUTS/BLUEPRINT_001_CH00_CONVOY_WRECK_ROUTE.md`;
- created the provisional Godot graybox `game/exploration/maps/chapter_00/chapter_00_graybox.tscn` plus its route builder;
- reconciled S005 to the Field Triage Camp perimeter and added S006's bounded player-controlled survivor sweep before Brackenwall;
- added focused Godot CI validation for the Chapter-0 graybox structure.

Current next deliverable:
> **Validate/play Blueprint 001's Chapter-0 graybox, revise scale/camera/topology from traversal evidence, then explicitly promote the approved topology to L3.**

Validation targets:
- scene loads cleanly in Godot;
- Android touch navigation works;
- camera variants A/B/C are compared;
- Wreck Field reads without minimap dependence;
- S003 recovery-line logic is spatially obvious;
- S005 camp-edge/east-cut staging matches exact dialogue;
- S006 recovery sweep remains short, bounded and no-combat;
- route pacing and transition seams are acceptable.

Layout/blockout work may proceed before final environment-material certification. Final rendered environment production remains downstream of relevant B01–B11 style/material approvals.

Working pointers:
- `AREA_AND_ROUTE_LAYOUT_PRODUCTION_WORKING.md`
- `PLAYABLE_AREA_INVENTORY_WORKING.md`
- `AREA_LAYOUTS/BLUEPRINT_001_CH00_CONVOY_WRECK_ROUTE.md`

## 4 — Production Implementation
Reconcile current canon with runtime, including:
- removal of stale Mastery Point assumptions;
- current Prime behavior and tests;
- canonical **G** terminology while detailed economy values remain rebuild-pending;
- production equipment/item fixtures;
- versioned save schema;
- current chapter/scene assumptions;
- production menus, combat UI, loadout UI, shop stock/persistence, and Kessara copy UI.

Implementation must consume owner-domain values rather than recreate them.

## 5 — Visual Production / Style Certification
**ACTIVE**

Current immediate gate:
> **B00 Permanent Party Character Style Anchor**

Current B00 state:
- Cyanis, Ilyra, Torren, Nimera, Vaelira, and Seyrik — exact permanent-party masters **LOCKED**;
- battle-scale and field-scale derivative validation remains pending.

Environment/material certification B01–B11 also remains open. Do not bulk-convert the environment library until the benchmark set reads as one coherent game at gameplay scale.

Working pointer:
`VISUAL_PRODUCTION_WORKING.md`

## 6 — Audio / Music Redevelopment
Final soundtrack identity, cue hierarchy, regional language, battle/boss/Hunt/Prime music, leitmotifs, diegetic scope, voice scope, SFX palette, and mix/implementation targets remain open.

## 7 — Whole-Game Playtest / QA
Run campaign-only, light, typical, heavy, and completionist routes plus boss/Hunt/Elite, **economy**, save/load, exploit, readability, input, and Android performance QA when the relevant implementation/content layers are ready.

Economy QA belongs **after the planned economy rebuild/recalibration**; current numeric G tables are provisional planning material.

## 8 — Intentionally Open Story / Lore Details
Keep explicitly open details unresolved until separately approved, including the sole Entity-fragment survival mechanism, Chapter-10 research-trail specifics, final survey prop, and unresolved formal chapter titles.

## Balance-workflow routing note
The former `Mandatory-Route Enemy Difficulty Recalibration` queue item and its First Command Warden / ×1.20 boss-local sequence are **not an active task in this queue anymore**.

The v103–v105 sensitivity/true-battle reports remain available as historical or analytical evidence in `16_BALANCE_AND_TESTING`, but they do not define the current work sequence and must not be used to automatically route the next task back to First Command Warden, the ×1.20 test floor, or the old boss-local retune list.

Any future balance changes should follow the separately established current handling process or a new explicit instruction, rather than reviving this retired queue workflow.

## Deferred stream — Economy rebuild / recalibration
The detailed G economy is **not closed current authority**.

Current routing:
- currency terminology remains **G**;
- existing prices, payouts, liquidity totals, Hunt cash, shop values, and completionist totals remain provisional working/reference data;
- do not spend cleanup time propagating or polishing G totals;
- reopen detailed economy design when the planned economy rebuild begins;
- story/encounter cleanup must not infer structural canon from old payout tables.

## Rule
Do not use this queue to silently modify a closed owner-domain rule. When a working item is resolved, update the owning numbered domain first, then remove/archive its working tracker.
