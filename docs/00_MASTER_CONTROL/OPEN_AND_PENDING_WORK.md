# Diyse — Open & Pending Work

This is the cross-domain summary of work that remains genuinely unresolved. Detailed sequencing lives in `../90_WORKING/ACTIVE_WORK_QUEUE.md`; this file must not become a competing second backlog.

## Priority 1 — Story-owned enemy placement / timing dependencies — DEFERRED
Owner:
Story/dialogue + `09_ENEMIES_AND_ENCOUNTERS`

Examples include:
- False-Warrant Adept exact placement/role;
- Highland Resistance Fighter exact Chapter-5 placement;
- Crown Engine Technician exact story placement;
- bounded Hunt return/unlock timing where the story trigger is not yet exact.

Any payout detail for a still-unplaced special authored encounter remains deferred until its owning scene role is finalized **and** the planned economy rebuild/recalibration is ready.

## Priority 2 — Chapter 4 onward exact dialogue — ACTIVE / OPEN
Owner:
Story/dialogue domains

Chapters 0–3 are source-closed and synchronized.

**Chapter 4 — The Seventh Reaction** is the current active Dialogue Engine production frontier under its current 12-beat pre-dialogue story authority.

Immediate dialogue work remains:
- line-author Chapter 4 through the current rehearsal-first Person-Brain pipeline;
- after Chapter 4, finish the approved Chapter-5 Seyrik/Rhazek beat rewrite as needed for the current chapter structure;
- line-author Chapter 5;
- continue Chapters 6–13 through current scene-ID architecture.

Optional Side Quest / Character Quest exact dialogue remains open where not separately completed.

## Priority 3 — Playable area & route layout production — ACTIVE
Owners:
`04_WORLD_AND_LORE` + story/encounter/art/implementation domains

The project has closed macro geography and established route sequences, but it does **not** yet have production-ready playable geometry for the full game.

Open work includes:
- complete playable-area inventory;
- actual route/town/dungeon/facility/Hunt blockouts;
- entrances/exits and transitions;
- critical paths, optional loops, shortcuts and traversal gates;
- landmark/sightline navigation;
- HD-2D elevation/layer composition;
- encounter-space and boss/Hunt-arena planning;
- interaction/reward/state-change placement;
- approximate traversal/pacing targets;
- tool-agnostic AI/environment-generation handoff packets.

Layout/blockout work may proceed in parallel with visual benchmark work. Final rendered environment generation remains downstream of the relevant B01–B11 approvals.

Working pointer:
`90_WORKING/AREA_AND_ROUTE_LAYOUT_PRODUCTION_WORKING.md`

## Priority 4 — Implementation reconciliation — OPEN
Owner:
`13_UI_AND_IMPLEMENTATION`

High-impact engineering work:
- remove stale Mastery Point implementation assumptions;
- replace proof bearer-locked `first_champion` Prime behavior;
- reconcile proof `gold` technical identifiers to player-facing **G** terminology; do not promote old proof numeric values while detailed economy is rebuild-pending;
- replace proof equipment/item content with current production fixtures;
- implement current Prime persistent-spend/restoration behavior;
- build production save schema/migrations;
- build production menus/combat UI/loadout UI/shop stock and Kessara UI;
- preserve stable IDs or provide save-safe migration where technical names change.

## Priority 5 — Visual production / style certification — ACTIVE
Owner:
`14_ART_AND_VISUALS`

The B00 character identity/master setup is no longer an unresolved repository gate:
- the permanent six have current repository-backed exact masters;
- Maevra and Mirena are part of the current exact-source lock set;
- Kessara remains separately locked by her current repository master/visual authority;
- character visual authority is routed through `14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md`;
- current source masters live in `asset_sources/characters/current/`.

Do **not** reopen character identity from older render/prose material merely because later production stages remain active.

Remaining visual-production work includes downstream runtime translation/certification and the relevant B01–B11 environment/material/VFX approvals. Do not bulk-convert the environment/material library until the applicable benchmark certification is coherent at gameplay scale.

## Priority 6 — Full production playtest / QA — LATER
Owner:
`16_BALANCE_AND_TESTING`

When the relevant implementation/content layers are ready:
- campaign route playtests;
- light / typical / heavy / completionist route playtests;
- boss/Hunt/Elite regressions;
- economy validation after the planned economy rebuild/recalibration, using actual combat-consumption behavior;
- resource attrition checks;
- optional overlevel checks;
- Prime regressions;
- save/load and exploit QA;
- area-route readability, traversal and collision QA;
- Android performance/input/readability QA.

## Later — Music/audio
Owner:
`15_AUDIO_AND_MUSIC`

Current final soundtrack:
> **entirely OPEN**

## Intentionally open story/lore details
Keep explicitly bounded unknowns unresolved until separately approved, including the sole Entity-fragment survival mechanism and other owner-file items explicitly marked OPEN.

## Active balance stream — enemy ability / difficulty + progression revalidation
Owners:
`09_ENEMIES_AND_ENCOUNTERS` + `10_PROGRESSION_AND_EXP` + `16_BALANCE_AND_TESTING`

Status:
> **OPEN / REBUILD + RECERTIFICATION PENDING**

Current boundary:
- enemy abilities/action kits and direct-damage Powers will be redone/revalidated;
- existing enemy stats/Powers remain reference inputs unless explicitly revised;
- mandatory/completionist difficulty certification must be rerun after the current kits exist;
- Player EXP/CEXP allocation is also rebuild-pending, with **Lv55–60** retained as the class-completion target window;
- old v89–v105 PASS/sensitivity results remain historical evidence only where their tested assumptions were superseded.

Retired routing remains retired:
- do not apply a standing ×1.20 global Power floor;
- do not retune First Command Warden next;
- do not restore the former boss-local sequence.

This active stream is the newer redesign/revalidation boundary, not a revival of the retired queue.

## Deferred stream — Economy rebuild / recalibration
Owner:
`12_ECONOMY_AND_REWARDS`

Status:
> **REBUILD / RECALIBRATION PENDING**

Current cross-domain rule:
- player-facing currency terminology remains **G**;
- **Auren** remains retired;
- existing prices, payouts, shop values, liquidity totals, Hunt cash, Kessara fees, and completionist totals are provisional planning/history data;
- cleanup/consolidation should not rebalance or propagate those numbers;
- detailed economy work resumes when the planned economy rebuild begins.

## Rule
Do not use this index to silently reopen a closed owner-domain rule.
