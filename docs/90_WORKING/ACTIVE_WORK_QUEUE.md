# Diyse — Active Work Queue

This queue tracks unresolved/reopened work only. Closed owner-domain values remain closed unless a current test demonstrates a specific failure.

## 1 — Mandatory-Route Enemy Difficulty Recalibration
**ACTIVE — v105 four-point same-gear boss sensitivity complete / boss-local retune list confirmed**

User-directed correction:
> **The mandatory route should be harder, with more KOs when the player has skipped optional progression.**

Current global sensitivity hypothesis:
> **Enemy direct-damage Power × 1.20**

This remains a test layer, not yet a wholesale owner-file rewrite.

Core comparison rule:
- mandatory and higher-level routes use the **same ordinary equipment**;
- same normal-stock consumables;
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

### Current evidence
**Chapter 5 ordinary formations:**
- +20% increases attrition/focus pressure without producing routine encounter-isolation wipes;
- late Forge Lock rose only to ~0.22% any-KO in the full-status isolation sample.

**Deepforge Colossus — structural assembly candidate + ×1.20:**
- Lv20 mandatory rush — **92.82% wins / 48.98% any-KO / 7.18% wipes**;
- Lv20 mandatory dismantle — **99.56% wins / 21.74% any-KO / 0.44% wipes**;
- Lv22 same-gear higher-level rush — **100% wins / 1.96% any-KO**;
- Lv22 same-gear higher-level dismantle — **100% wins / 1.02% any-KO**.

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

### v105 mandatory-vs-max-level same-equipment boss curve
Pure Player-Level isolation under ×1.20, no Prime:

| Chapter boss | Mandatory | Max-preboss | Mandatory any-KO | Max-level any-KO | Wipes |
|---|---:|---:|---:|---:|---:|
| First Command Warden | Lv11 | Lv13 | **~0.13%** | **~0.01%** | 0% |
| Zevraya → Perfected War Mother | Lv24 | Lv28 | **~4.4–4.8%** | **~0.7–1.0%** | 0% |
| Rhazek → Bastion Devourer | Lv40 | Lv50 | **~0.45–0.5%** | **~0–0.02%** | 0% |
| Vaelkor → Sovereign Panoply | Lv56 | Lv67 | **~6.8–7.0%** | **~0.3–0.4%** | 0% observed |

Interpretation:
- the same-equipment level advantage clearly buys safety;
- ×1.20 alone is still insufficient for First Command Warden and Rhazek;
- Zevraya responds but still benefits far more from the already-open Reservoir structural correction;
- Vaelkor responds strongly and likely needs a smaller local pressure pass than Rhazek;
- pushing the whole roster above ×1.20 merely to fix low-pressure bosses is inefficient.

Supplemental boss-only scan to ×1.35 confirmed the same pattern: First Command Warden and Rhazek remain very safe while Zevraya/Vaelkor rise much faster. This confirms an architecture/action-density issue rather than a universal-damage-floor issue.

### Current design conclusion
Do **not** keep raising the whole-roster scalar to fix weak bosses.

Working two-layer model:
1. **global enemy direct-damage floor around ×1.20**;
2. **boss-specific action-density / mechanic / offensive tuning on top of that floor**.

The +20% global hypothesis remains strongly promising for ordinary enemies and structurally sound encounters.

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

Prior v93–v102 reports remain valid historical measurements and mechanical-rule evidence. From Chapter 5 onward, their old difficulty PASS/RETAIN verdicts are provisional under the new standard.

## 2 — Story-Owned Enemy Placement / Timing Dependencies
**DEFERRED UNTIL RELEVANT STORY/DIALOGUE WORK**

Examples include:
- False-Warrant Adept exact placement/role;
- Highland Resistance Fighter exact Chapter-5 placement;
- Crown Engine Technician exact story placement;
- bounded Hunt return/unlock timing where the story trigger is not yet exact.

These are placement/timing dependencies, not missing enemy combat sheets.

Economy consequence:
> any exact Auren line for these story-dependent special encounters remains deferred until their owning scene role is finalized. This does **not** reopen the core economy design.

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
- Auren semantics and the now-closed reward economy;
- production equipment/item fixtures;
- versioned save schema;
- current chapter/scene assumptions;
- production menus, combat UI, loadout UI, shop stock/persistence, and Kessara copy UI.

Economy numeric/reward design is closed in `12_ECONOMY_AND_REWARDS`; implementation must consume those values rather than recreate them.

## 5 — Visual Production / Style Certification
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

## 6 — Audio / Music Redevelopment
Final soundtrack identity, cue hierarchy, regional language, battle/boss/Hunt/Prime music, leitmotifs, diegetic scope, voice scope, SFX palette, and mix/implementation targets remain open.

## 7 — Whole-Game Playtest / QA
After targeted representative certification and implementation reconciliation, run campaign-only, light, typical, heavy, and completionist routes plus boss/Hunt/Elite, **economy**, save/load, exploit, readability, input, and Android performance QA.

Economy QA should validate the closed owner-domain assumptions rather than treating the numeric economy as still unauthored.

## 8 — Intentionally Open Story / Lore Details
Keep explicitly open details unresolved until separately approved, including the sole Entity-fragment survival mechanism, Chapter-10 research-trail specifics, final survey prop, and unresolved formal chapter titles.

## Closed stream — Core Economy / Rewards
The independent economy-design stream is **CLOSED**.

Current owner-domain calibration includes:
- ~**30,127 Auren** mandatory-route direct-cash center;
- ~**13.56k** ordinary-formation Auren (~45% of mandatory direct cash);
- **8,490** mandatory story-boss Auren;
- **8,080** exact mandatory non-battle Auren delivery map;
- **19,390** total current optional direct cash;
- ~**49,517 Auren** full direct-cash completionist reference before resale/extra encounters;
- exact ordinary/optional/Hunt/quest reward packages;
- exact Consumable resale;
- no random ordinary-enemy loot economy;
- exactly 9 Regional Markets;
- Kessara fee **600 Auren**;
- finite reward-only supply **3 Reservoir Tonic / 4 Emergency Kit / 2 Emergency Rally**.

Do not reopen this stream merely for vendor presentation, UI binding, story-placement-dependent special encounters, or later economy QA. Reopen only for a demonstrated balance/exploit failure or explicit design revision.

## Rule
Do not use this queue to silently modify a closed owner-domain rule. When a working item is resolved, update the owning numbered domain first, then remove/archive its working tracker.
