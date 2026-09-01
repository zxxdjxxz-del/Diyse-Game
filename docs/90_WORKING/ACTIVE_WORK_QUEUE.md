# Diyse — Active Work Queue

This queue tracks unresolved/reopened work only. Closed owner-domain values remain closed unless a current test demonstrates a specific failure.

## 1 — Mandatory-Route Enemy Difficulty Recalibration
**ACTIVE — v104 global +20% enemy direct-Power sensitivity**

User-directed correction:
> **The mandatory route should be harder, with more KOs when the player has skipped optional progression.**

Current global sensitivity hypothesis:
> **Enemy direct-damage Power × 1.20**

This is a test layer, not yet a wholesale owner-file rewrite.

Scope:
- ordinary enemies;
- Elites;
- authored/protected hostile combatants;
- mandatory named/story bosses;
- Regional Hunts;
- Major Hunts;
- hostile support actors/objects when they deal ordinary direct damage.

Unchanged during the sensitivity pass:
- HP/raw stats;
- status chances/magnitudes;
- fixed or %Max-HP damage;
- AI/turn count;
- encounter composition;
- boss architecture;
- player equipment.

Core mandatory-vs-completionist comparison rule:
- mandatory and completionist use the **same ordinary equipment**;
- same normal-stock consumables;
- same active party and competent tactical policy;
- no completionist Relic/Legacy gear advantage in the core comparison;
- route differences come primarily from actual Player Level / CEXP / learned abilities;
- KO/wipe/resource pressure matters more than merely proving the fight can be won.

Current first anchor:
> **Deepforge Colossus — Assembly Frame → Worldsmith Body — Chapter 5**

Working reports:
- `../16_BALANCE_AND_TESTING/TRUE_BATTLES/CH5_DEEPFORGE_DIFFICULTY_RECALIBRATION_WORKING_v103.md`
- `../16_BALANCE_AND_TESTING/TRUE_BATTLES/CH5_DEEPFORGE_ASSEMBLY_TUNING_CANDIDATE_v103.md`
- `../16_BALANCE_AND_TESTING/GLOBAL_ENEMY_POWER_20_PERCENT_SENSITIVITY_v104.md`

Known evidence before the +20% global pass:
- current mandatory Lv20 Deepforge competent line — **100% wins / 0.095% any-KO** over 20,000 runs;
- current completionist Lv22 same gear — **100% wins / 0.005% any-KO**;
- preferred v103 structural candidate at ~+15% Power produced mandatory rush **37.37% any-KO / 3.335% wipes**, while same-gear Lv22 completionist rush remained **0.58% any-KO / 0 observed wipes**.

The v104 scalar is only about **4.35% more direct damage** than that preferred +15% structural candidate, while remaining far below the earlier rejected +45% brute-force sensitivity.

Important Deepforge dependency:
> the Guard Press / Repair Arm action-density problem still requires the structural assembly rewrite; the +20% scalar alone does not fix that incentive.

Next balance actions:
1. test early ordinary formations under the +20% scalar for opening-round spike safety;
2. rerun Deepforge same-gear Lv20 vs Lv22 with the assembly correction and +20% scalar;
3. carry the same scalar through later representative chapter bosses;
4. identify specific outliers that need less/more than the global baseline;
5. only after the late-game curve is anchored, return to Reconstituted Entity → The Last Command.

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
