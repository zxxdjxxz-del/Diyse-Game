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

## 2 — Chapters 5–13 Exact Dialogue
Chapters 0–4 are line-complete.

Immediate next dialogue work:
- complete the approved Chapter-5 Seyrik/Rhazek beat rewrite;
- then line-author Chapter 5;
- continue Chapters 6–13 through the current story/scene-ID architecture.

Optional Side Quest / Character Quest exact dialogue remains open where not separately completed.

## 3 — Playable Area & Route Layout Production
**ACTIVE / MAY PROCEED IN PARALLEL WITH VISUAL BENCHMARK WORK**

The current world map and macro travel order do **not** yet constitute production-ready playable maps.

Open work includes:
- inventory every gameplay-relevant field, route, town/hub slice, dungeon, facility, quest site and Hunt site;
- create actual playable footprints/blockouts;
- define entrances/exits, critical paths, optional loops, shortcuts and traversal gates;
- place landmarks and sightline anchors;
- define elevation and HD-2D foreground/midground/background composition;
- reserve encounter spaces and boss/Hunt arenas;
- place authored interactions, rewards, transitions and state changes;
- set rough traversal/pacing targets;
- create environment-generation handoff packets that preserve canonical geography and route topology.

Layout/blockout work can begin before final environment-material certification. Final rendered environment production remains downstream of the relevant B01–B11 style/material approvals.

Immediate next deliverable:
> **Playable Area Inventory** — one complete checklist of all playable areas/sub-areas and their current layout readiness.

Working pointer:
`AREA_AND_ROUTE_LAYOUT_PRODUCTION_WORKING.md`

## 4 — Production Implementation
Reconcile current canon with runtime, including:
- removal of stale Mastery Point assumptions;
- current Prime behavior and tests;
- **G** semantics and closed economy fixtures;
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
- Cyanis — high-resolution new-style master **LOCKED**;
- Ilyra — **cleanup/remake review OPEN**;
- Torren, Nimera, Vaelira, Seyrik — new-style masters pending;
- battle-scale and field-scale derivative validation pending.

Environment/material certification B01–B11 also remains open. Do not bulk-convert the environment library until the benchmark set reads as one coherent game at gameplay scale.

Working pointer:
`VISUAL_PRODUCTION_WORKING.md`

## 6 — Audio / Music Redevelopment
Final soundtrack identity, cue hierarchy, regional language, battle/boss/Hunt/Prime music, leitmotifs, diegetic scope, voice scope, SFX palette, and mix/implementation targets remain open.

## 7 — Whole-Game Playtest / QA
Run campaign-only, light, typical, heavy, and completionist routes plus boss/Hunt/Elite, **economy**, save/load, exploit, readability, input, and Android performance QA when the relevant implementation/content layers are ready.

Economy QA validates the closed owner-domain G calibration rather than treating the numeric economy as still unauthored.

## 8 — Intentionally Open Story / Lore Details
Keep explicitly open details unresolved until separately approved, including the sole Entity-fragment survival mechanism, Chapter-10 research-trail specifics, final survey prop, and unresolved formal chapter titles.

## Balance-workflow routing note
The former `Mandatory-Route Enemy Difficulty Recalibration` queue item and its First Command Warden / ×1.20 boss-local sequence are **not an active task in this queue anymore**.

The v103–v105 sensitivity/true-battle reports remain available as historical or analytical evidence in `16_BALANCE_AND_TESTING`, but they do not define the current work sequence and must not be used to automatically route the next task back to First Command Warden, the ×1.20 test floor, or the old boss-local retune list.

Any future balance changes should follow the separately established current handling process or a new explicit instruction, rather than reviving this retired queue workflow.

## Closed stream — Core G Economy / Rewards
The independent economy-design stream is **CLOSED**.

Current owner-domain calibration includes:
- currency **G**;
- **1 economy unit = 200 G**;
- starting wallet **2,500 G**;
- ~**316,900 G** mandatory-route direct-cash center;
- ~**135,600 G** ordinary-formation income (~42.8% of mandatory direct G);
- **92,700 G** mandatory story-boss/named-encounter G;
- **5,300 G** fixed authored combat/event G;
- **80,800 G** mandatory non-battle delivery map;
- **329,600 G** total authored optional direct G;
- ~**646,500 G** full direct-cash completionist reference before resale/extra encounters;
- **116,500 G** Regional Hunt cash;
- **134,000 G** Major Hunt cash;
- strong Hunt cash regardless of separate permanent rewards;
- protected/nonlethal resolution does not default to 0 G;
- exact ordinary equipment/Consumable resale;
- ordinary equipment catalog value **251,000 G**;
- no random ordinary-enemy loot economy;
- exactly 9 Regional Markets;
- Kessara fee **6,000 G** per successful copy;
- premium Consumables available as one-copy-per-Consumable-shop limited stock with no automatic restock.

Do not reopen this stream merely for vendor presentation, UI binding, story-placement-dependent special encounters, or later economy QA. Reopen only for a demonstrated balance/exploit failure or explicit design revision.

## Rule
Do not use this queue to silently modify a closed owner-domain rule. When a working item is resolved, update the owning numbered domain first, then remove/archive its working tracker.
