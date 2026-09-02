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

## 2 — Story-Owned Enemy Placement / Timing Dependencies
**DEFERRED UNTIL RELEVANT STORY/DIALOGUE WORK**

Examples include:
- False-Warrant Adept exact placement/role;
- Highland Resistance Fighter exact Chapter-5 placement;
- Crown Engine Technician exact story placement;
- bounded Hunt return/unlock timing where the story trigger is not yet exact.

Economy consequence:
> exact G for story-dependent special encounters remains deferred until the owning scene role is finalized.

## 3 — Chapters 5–13 Exact Dialogue
Chapters 0–4 are line-complete.

Immediate next dialogue work:
- complete the approved Chapter-5 Seyrik/Rhazek beat rewrite;
- then line-author Chapter 5;
- continue Chapters 6–13 through the current story/scene-ID architecture.

Optional Side Quest / Character Quest exact dialogue remains open where not separately completed.

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
After targeted representative certification and implementation reconciliation, run campaign-only, light, typical, heavy, and completionist routes plus boss/Hunt/Elite, **economy**, save/load, exploit, readability, input, and Android performance QA.

Economy QA validates the closed owner-domain G calibration rather than treating the numeric economy as still unauthored.

## 8 — Intentionally Open Story / Lore Details
Keep explicitly open details unresolved until separately approved, including the sole Entity-fragment survival mechanism, Chapter-10 research-trail specifics, final survey prop, and unresolved formal chapter titles.

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
