# Diyse — Open & Pending Work

This is the cross-domain index of work that remains genuinely unresolved. Closed owner-domain values remain closed unless a current test or explicit design revision reopens them.

## Priority 1 — Mandatory-route enemy difficulty recalibration — ACTIVE
Owner:
`09_ENEMIES_AND_ENCOUNTERS` + `16_BALANCE_AND_TESTING`

Current working conclusion from v105:
> **Use a global enemy direct-damage test floor around ×1.20, then tune weak bosses locally rather than raising the whole roster further.**

The ×1.20 layer is still a test layer, not yet a wholesale owner-file rewrite.

Current boss-local retune list:
- First Command Warden;
- Furnace Tyrant;
- Crownstorm Roc;
- Matron Zevraya — Reservoir action-density correction;
- Revision Arbiter;
- Commander Rhazek → Bastion Devourer;
- Emperor Vaelkor → Sovereign Panoply — lighter local climax-pressure pass than Rhazek.

Current next action:
> **First Command Warden local pressure correction under the ×1.20 global test floor.**

Older v93–v102 true-battle reports remain valid historical measurements and mechanical-rule evidence, but old PASS/RETAIN difficulty verdicts are provisional wherever the revised mandatory-danger standard reopens the fight.

Key v105 same-equipment mandatory snapshots under ×1.20:
- First Command Warden Lv11 — ~0.13% any-KO: too safe;
- Zevraya Lv24 — ~4.4–4.8% any-KO under current owner structure;
- Rhazek Lv40 — ~0.45–0.5% any-KO: too safe;
- Vaelkor Lv56 — ~6.8–7.0% any-KO: promising but still below the revised climax-danger target.

Detailed working authority:
- `../16_BALANCE_AND_TESTING/FOUR_POINT_BOSS_LEVEL_SENSITIVITY_v105.md`
- `../90_WORKING/ACTIVE_WORK_QUEUE.md`

## Priority 2 — Story-owned enemy placement / timing dependencies — DEFERRED
Owner:
Story/dialogue + `09_ENEMIES_AND_ENCOUNTERS`

Examples include:
- False-Warrant Adept exact placement/role;
- Highland Resistance Fighter exact Chapter-5 placement;
- Crown Engine Technician exact story placement;
- bounded Hunt return/unlock timing where the story trigger is not yet exact.

Exact G for any still-unplaced special authored encounter remains deferred until its owning scene role is finalized.

## Priority 3 — Chapters 5–13 exact dialogue — OPEN
Owner:
Story/dialogue domains

Chapters 0–4 are line-complete.

Immediate dialogue work remains:
- finish the approved Chapter-5 Seyrik/Rhazek beat rewrite;
- line-author Chapter 5;
- continue Chapters 6–13 through current scene-ID architecture.

Optional Side Quest / Character Quest exact dialogue remains open where not separately completed.

## Priority 4 — Implementation reconciliation — OPEN
Owner:
`13_UI_AND_IMPLEMENTATION`

High-impact engineering work:
- remove stale Mastery Point implementation assumptions;
- replace proof bearer-locked `first_champion` Prime behavior;
- reconcile proof `gold` variable/data semantics and old values to current **G** authority;
- replace proof equipment/item content with current production fixtures;
- implement current Prime persistent-spend/restoration behavior;
- build production save schema/migrations;
- build production menus/combat UI/loadout UI/shop stock and Kessara UI;
- preserve stable IDs or provide save-safe migration where technical names change.

## Priority 5 — Visual production / style certification — ACTIVE
Owner:
`14_ART_AND_VISUALS`

Current immediate gate:
> **B00 Permanent Party Character Style Anchor**

Do not bulk-convert the environment/material library until benchmark certification is complete and coherent at gameplay scale.

## Priority 6 — Full production playtest / QA — LATER
Owner:
`16_BALANCE_AND_TESTING`

After the targeted balance and implementation passes:
- campaign route playtests;
- light / typical / heavy / completionist route playtests;
- boss/Hunt/Elite regressions;
- economy validation against actual combat-consumption behavior;
- resource attrition checks;
- optional overlevel checks;
- Prime regressions;
- save/load and exploit QA;
- Android performance/input/readability QA.

## Later — Music/audio
Owner:
`15_AUDIO_AND_MUSIC`

Current final soundtrack:
> **entirely OPEN**

## Intentionally open story/lore details
Keep explicitly bounded unknowns unresolved until separately approved, including the sole Entity-fragment survival mechanism and other owner-file items explicitly marked OPEN.

## Closed stream — Core G economy / rewards
Owner:
`12_ECONOMY_AND_REWARDS`

Status:
> **CLOSED**

Current anchors:
- currency = **G**;
- 1 economy unit = **200 G**;
- starting wallet = **2,500 G**;
- mandatory direct G = **~316,900 G**;
- authored optional direct G = **329,600 G**;
- broad completionist direct-cash reference = **~646,500 G**;
- chapter-by-chapter mandatory-route liquidity validation = **PASS**;
- Kessara = **6,000 G per successful Relic copy**;
- premium Consumables = 1 of each per Consumable-selling shop from first access, no automatic restock;
- protected/nonlethal resolution does not default to 0 G;
- Hunts pay strong G regardless of separate permanent rewards.

Do not list the economy as an open numeric gap unless later playtest evidence or an explicit user revision reopens it.

## Rule
Do not use this index to silently reopen a closed owner-domain rule.
