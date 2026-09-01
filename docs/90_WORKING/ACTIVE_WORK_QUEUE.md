# Diyse — Active Work Queue

This queue tracks unresolved/reopened work only. Closed owner-domain values remain closed unless a current test demonstrates a specific failure.

## 1 — Mandatory-Route Enemy Difficulty Recalibration
**ACTIVE — v104 global +20% enemy direct-Power sensitivity / boss-local retune list forming**

User-directed correction:
> **The mandatory route should be harder, with more KOs when the player has skipped optional progression.**

Current global sensitivity hypothesis:
> **Enemy direct-damage Power × 1.20**

This remains a test layer, not yet a wholesale owner-file rewrite.

Core comparison rule:
- mandatory and completionist use the **same ordinary equipment**;
- same normal-stock consumables;
- same active party and competent tactical policy;
- no completionist Relic/Legacy gear advantage in the core comparison;
- route differences come primarily from actual Player Level / CEXP / learned abilities;
- KO/wipe/resource pressure matters more than merely proving the fight can be won.

Working reports:
- `../16_BALANCE_AND_TESTING/TRUE_BATTLES/CH5_DEEPFORGE_DIFFICULTY_RECALIBRATION_WORKING_v103.md`
- `../16_BALANCE_AND_TESTING/TRUE_BATTLES/CH5_DEEPFORGE_ASSEMBLY_TUNING_CANDIDATE_v103.md`
- `../16_BALANCE_AND_TESTING/GLOBAL_ENEMY_POWER_20_PERCENT_SENSITIVITY_v104.md`
- `../16_BALANCE_AND_TESTING/CH6_ENEMY_POWER_20_PERCENT_SENSITIVITY_v104.md`
- `../16_BALANCE_AND_TESTING/CH7_ENEMY_POWER_20_PERCENT_SENSITIVITY_v104.md`

### Current evidence
**Chapter 5 ordinary formations:**
- +20% increases attrition/focus pressure without producing routine encounter-isolation wipes;
- late Forge Lock rose only to ~0.22% any-KO in the full-status isolation sample.

**Deepforge Colossus — structural assembly candidate + ×1.20:**
- Lv20 mandatory rush — **92.82% wins / 48.98% any-KO / 7.18% wipes**;
- Lv20 mandatory dismantle — **99.56% wins / 21.74% any-KO / 0.44% wipes**;
- Lv22 completionist same gear rush — **100% wins / 1.96% any-KO**;
- Lv22 completionist same gear dismantle — **100% wins / 1.02% any-KO**.

This is the first strong desired difficulty profile.

**Furnace Tyrant:**
- global ×1.20 helps but remains too safe under competent play;
- local boss tuning still required.

**Crownstorm Roc:**
- Lv23 mandatory ×1.20 smart line remains around **0.8% any-KO / ~0.02% wipes** in the calibrated sensitivity;
- local boss tuning required.

**Matron Zevraya:**
- current Reservoir support-action structure has the same action-density inversion problem discovered in Deepforge;
- non-diluting structural sensitivity + ×1.20 produces approximately **44% any-KO / 0.6% wipes** on Lv24 mandatory dismantle and **9% any-KO / 0 observed wipes** on Lv27 same-gear completionist dismantle;
- structural candidate is promising but not owner canon.

**Revision Arbiter:**
- historical v100 mandatory result was **1 KO / 20,000**;
- calibrated ×1.20 sensitivity still lands only around **0.2–0.3% any-KO** with no meaningful wipe tail;
- even large boss-only Power escalation remains inefficient because the encounter contains many low-pressure/action-tax turns;
- local pressure/mechanic tuning required.

### Current design conclusion
Do **not** keep raising the whole-roster scalar to fix weak bosses.

Working two-layer model:
1. **global enemy direct-damage floor around ×1.20**;
2. **boss-specific action-density / mechanic / offensive tuning on top of that floor**.

The +20% global hypothesis remains strongly promising for ordinary enemies and structurally sound encounters.

### Boss-local retune list opened by v104
- Furnace Tyrant
- Crownstorm Roc
- Matron Zevraya — Reservoir action-density correction
- Revision Arbiter
- later Rhazek / Vaelkor to be rechecked under the same model

Next balance actions:
1. use the established Rhazek true-battle harness as the next late-game ×1.20 representative;
2. then recheck Vaelkor;
3. decide whether ×1.20 can be promoted as the global enemy direct-Power baseline;
4. return to the boss-local retune list rather than increasing the universal scalar beyond 20%;
5. only after the late-game mandatory curve is anchored, return to Reconstituted Entity → The Last Command.

Prior v93–v102 reports remain valid historical measurements and mechanical-rule evidence. From Chapter 5 onward, their old difficulty PASS/RETAIN verdicts are provisional under the new standard.

## 2 — Story-Owned Enemy Placement / Timing Dependencies
**DEFERRED UNTIL RELEVANT STORY/DIALOGUE WORK**

Examples include:
- False-Warrant Adept exact placement/role;
- Highland Resistance Fighter exact Chapter-5 placement;
- Crown Engine Technician exact story placement;
- bounded Hunt return/unlock timing where the story trigger is not yet exact.

These are placement/timing dependencies, not missing enemy combat sheets.

## 3 — Chapters 5–13 Exact Dialogue
Chapters 0–4 are line-complete.

Immediate next dialogue work:
- complete the approved Chapter-5 Seyrik/Rhazek beat rewrite;
- then line-author Chapter 5;
- continue Chapters 6–13 through the current story/scene-ID architecture.

Optional Side Quest / Character Quest exact dialogue remains open where not separately completed.

## 4 — Economy / Reward Exact Gaps
Complete unresolved:
- Side Quest Auren rewards;
- Side Quest consumable/material bundles;
- Character Quest monetary add-ons;
- unresolved Hunt Auren payouts;
- consumable resale rules;
- Kessara Relic-copy service fee, if any.

## 5 — Production Implementation
Reconcile current canon with runtime, including:
- removal of stale Mastery Point assumptions;
- current Prime behavior and tests;
- Auren semantics;
- production equipment/item fixtures;
- versioned save schema;
- current chapter/scene assumptions;
- production menus, combat UI, and loadout UI.

## 6 — Visual Production / Style Certification
**ACTIVE**

Current immediate gate:
> **B00 Permanent Party Character Style Anchor**

Current B00 state:
- Cyanis — high-resolution new-style master **LOCKED**;
- Ilyra — **cleanup/remake review OPEN**;
- Torren, Nimera, Vaelira, Seyrik — new-style masters pending;
- battle-scale and field-scale derivative validation pending.

Environment/material certification B01–B11 also remains open. Do not bulk-convert the 3,214-file environment library until the benchmark set reads as one coherent game at gameplay scale.

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
