# Diyse — Active Work Queue

This queue tracks unresolved/reopened work only. Closed owner-domain values remain closed unless a current test or explicit user revision changes them.

## 1 — Mandatory-Route Enemy Difficulty Recalibration
**ACTIVE — v105 four-point same-gear boss sensitivity complete / boss-local retune list confirmed**

User-directed correction:
> **The mandatory route should be harder, with more KOs when the player has skipped optional progression.**

Current global sensitivity hypothesis:
> **Enemy direct-damage Power × 1.20**

This remains a test layer, not yet a wholesale owner-file rewrite.

Core comparison rule:
- mandatory and higher-level routes use the **same ordinary equipment**;
- same normal-stock Consumables;
- same active party and competent tactical policy;
- no Relic/Legacy gear advantage in the core comparison;
- KO/wipe/resource pressure matters more than merely proving the fight can be won.

For the v105 pure-level isolation, even the selected classes / learned ability package is held to the mandatory snapshot so only Player Level changes.

Working reports:
- `../16_BALANCE_AND_TESTING/TRUE_BATTLES/CH5_DEEPFORGE_DIFFICULTY_RECALIBRATION_WORKING_v103.md`
- `../16_BALANCE_AND_TESTING/TRUE_BATTLES/CH5_DEEPFORGE_ASSEMBLY_TUNING_CANDIDATE_v103.md`
- `../16_BALANCE_AND_TESTING/GLOBAL_ENEMY_POWER_20_PERCENT_SENSITIVITY_v104.md`
- `../16_BALANCE_AND_TESTING/CH6_ENEMY_POWER_20_PERCENT_SENSITIVITY_v104.md`
- `../16_BALANCE_AND_TESTING/CH7_ENEMY_POWER_20_PERCENT_SENSITIVITY_v104.md`
- `../16_BALANCE_AND_TESTING/FOUR_POINT_BOSS_LEVEL_SENSITIVITY_v105.md`

### Current design conclusion
Do **not** keep raising the whole-roster scalar to fix weak bosses.

Working two-layer model:
1. **global enemy direct-damage floor around ×1.20**;
2. **boss-specific action-density / mechanic / offensive tuning on top of that floor**.

### Boss-local retune list
- First Command Warden
- Furnace Tyrant
- Crownstorm Roc
- Matron Zevraya — Reservoir action-density correction
- Revision Arbiter
- Commander Rhazek → Bastion Devourer
- Emperor Vaelkor → Sovereign Panoply — lighter local climax-pressure pass than Rhazek

Next balance actions:
1. define the local pressure correction for **First Command Warden** as the early-game model;
2. finish/promote the already-promising Zevraya Reservoir structural candidate when approved;
3. retune **Rhazek** locally under the ×1.20 floor;
4. apply the resulting late-boss pressure standard to **Vaelkor**;
5. decide whether ×1.20 can be promoted as the global enemy direct-Power baseline;
6. only after the late-game mandatory curve is anchored, return to Reconstituted Entity → The Last Command.

## 2 — Economy / G Payout Recalibration
**ACTIVE — currency rename/structure synchronized; exact payout tables reopened**

Current locked economy structure:
- currency = **G**;
- retired currency name = **Auren**;
- **1 economy unit = 200 G**;
- starting wallet = **2,500 G**;
- completionist direct-cash target = roughly **650,000 G**;
- protected/nonlethal resolved encounters may award G;
- Regional and Major Hunts should give strong G regardless of separate permanent rewards;
- premium Consumables are purchasable from the start of the normal shop economy;
- every Consumable-selling shop carries **1 Emergency Kit + 1 Reservoir Tonic + 1 Emergency Rally**, no automatic restock;
- ordinary enemies have no random item/junk economy.

Exact G still to synchronize/re-author:
1. ordinary formation ledger;
2. optional Elite payouts;
3. mandatory story/protected/nonlethal encounter payouts;
4. mandatory non-battle chapter amounts;
5. Side Quest direct G;
6. Character Quest direct G;
7. Regional Hunt G;
8. Major Hunt G;
9. final resale tables where display-scale synchronization remains pending;
10. whole-campaign mandatory/completionist simulation around the ~650,000 G target.

Owner domain:
`../12_ECONOMY_AND_REWARDS/`

## 3 — Story-Owned Enemy Placement / Timing Dependencies
**DEFERRED UNTIL RELEVANT STORY/DIALOGUE WORK**

Examples include:
- False-Warrant Adept exact placement/role;
- Highland Resistance Fighter exact Chapter-5 placement;
- Crown Engine Technician exact story placement;
- bounded Hunt return/unlock timing where the story trigger is not yet exact.

Economy consequence:
> exact G for story-dependent special encounters remains deferred until the owning scene role is finalized.

## 4 — Chapters 5–13 Exact Dialogue
Chapters 0–4 are line-complete.

Immediate next dialogue work:
- complete the approved Chapter-5 Seyrik/Rhazek beat rewrite;
- then line-author Chapter 5;
- continue Chapters 6–13 through the current story/scene-ID architecture.

Optional Side Quest / Character Quest exact dialogue remains open where not separately completed.

## 5 — Production Implementation
Reconcile current canon with runtime, including:
- removal of stale Mastery Point assumptions;
- current Prime behavior and tests;
- **G** semantics and current economy fixtures;
- production equipment/item fixtures;
- versioned save schema;
- current chapter/scene assumptions;
- production menus, combat UI, loadout UI, shop stock/persistence, and Kessara copy UI.

Implementation must consume owner-domain values rather than recreate them.

## 6 — Visual Production / Style Certification
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

## 7 — Audio / Music Redevelopment
Final soundtrack identity, cue hierarchy, regional language, battle/boss/Hunt/Prime music, leitmotifs, diegetic scope, voice scope, SFX palette, and mix/implementation targets remain open.

## 8 — Whole-Game Playtest / QA
After targeted representative certification and implementation reconciliation, run campaign-only, light, typical, heavy, and completionist routes plus boss/Hunt/Elite, economy, save/load, exploit, readability, input, and Android performance QA.

## 9 — Intentionally Open Story / Lore Details
Keep explicitly open details unresolved until separately approved, including the sole Entity-fragment survival mechanism, Chapter-10 research-trail specifics, final survey prop, and unresolved formal chapter titles.

## Rule
Do not use this queue to silently modify a closed owner-domain rule. When a working item is resolved, update the owning numbered domain first, then remove/archive its working tracker.
