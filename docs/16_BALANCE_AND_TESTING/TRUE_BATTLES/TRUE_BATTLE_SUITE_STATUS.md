# Diyse — Representative True-Battle Suite Status
**v104 WORKING — GLOBAL +20% ENEMY DIRECT-POWER SENSITIVITY ACTIVE**

## Status change
The previous v93–v102 reports remain valid records of the exact snapshots/rules they measured.

However, the acceptance standard has changed:
> **The mandatory route should be materially harder, and optional progression should produce a clear reduction in KO/wipe pressure even when equipment is held constant.**

The current whole-roster sensitivity hypothesis is:
> **Enemy direct-damage Power × 1.20**

This multiplier is a test layer, not yet a permanent rewrite of owner files.

Because Power is a linear factor in Diyse's direct-damage formulas, the scalar yields approximately +20% direct damage while leaving HP, raw stats, statuses, AI, turn count, encounter composition and fight duration architecture unchanged.

Detailed sensitivity owner:
`../GLOBAL_ENEMY_POWER_20_PERCENT_SENSITIVITY_v104.md`

---

# New core comparison standard
For the main mandatory-vs-completionist comparison:
- use the **same ordinary equipment** on both routes;
- use the **same normal-stock consumables**;
- use the same active four and competent tactical policy;
- do not give the completionist route Relic/Legacy equipment merely to make it safer;
- allow the real Player-Level / CEXP / learned-ability difference created by optional play;
- test Prime-specific advantages separately.

Primary difficulty signals:
1. temporary-KO incidence;
2. wipe incidence;
3. ending HP/MP;
4. item/recovery pressure;
5. mechanic-response pressure;
6. duration secondarily.

---

# Global +20% sensitivity boundaries
Apply ×1.20 to authored enemy direct-damage Power for:
- ordinary enemies;
- Elites;
- authored hostile combatants;
- story bosses;
- Regional Hunts;
- Major Hunts;
- hostile support actors/objects that deal ordinary direct damage.

Do not multiply:
- Burn/Bleed or other indirect damage;
- fixed/%Max-HP damage;
- healing/repair;
- status chances;
- raw stats;
- Base Hit;
- support actions with Power N/A.

Early Chapter-1 arithmetic does not show an obvious raw one-shot problem. The marked Hollow Watch Ballista 200-Power shot becomes 240 test Power and remains well below the Lv2 party's Max HP on all three benchmark targets.

---

# Current recalibration anchor
## Chapter 5 — Deepforge Colossus → Worldsmith Body
Working reports:
- `CH5_DEEPFORGE_DIFFICULTY_RECALIBRATION_WORKING_v103.md`
- `CH5_DEEPFORGE_ASSEMBLY_TUNING_CANDIDATE_v103.md`

Same-gear route anchors:
- mandatory — **Lv20**;
- completionist — **Lv22**.

Current-package competent-policy sample:
- mandatory Lv20 — **100% wins / 0.095% any-KO** over 20,000 runs;
- completionist Lv22 — **100% wins / 0.005% any-KO** over 20,000 runs.

Verdict:
> **CURRENT PACKAGE TOO SAFE FOR THE NEW MANDATORY-ROUTE STANDARD**

The preferred v103 structural candidate converted Guard Press/Repair Arm away from action-menu dilution and used approximately +15% direct Power:
- mandatory Lv20 rush — **96.665% wins / 37.37% any-KO / 3.335% wipes**;
- mandatory Lv20 dismantle — **99.87% wins / 14.165% any-KO / 0.13% wipes**;
- completionist Lv22 same-gear rush — **100% wins / 0.58% any-KO**;
- completionist Lv22 same-gear dismantle — **100% wins / 0.315% any-KO**.

The v104 +20% scalar is only about **4.35% more direct damage** than that preferred +15% candidate. It should therefore be tested as the new common baseline rather than jumping to the older rejected +45% brute-force package.

Current Deepforge test Powers under exact ×1.20:
- Assembly Frame — 246 / 168 AoE / 234 Fire / 204;
- Worldsmith — 270 / 258 Fire / 186 AoE / 312 / Forge Collapse 360 AoE.

The assembly-action-density correction remains required; a Power scalar alone does not solve that incentive.

---

# Ordinary-formation watch
The +20% layer applies to ordinary encounters as well as bosses.

Chapter 5 is the first ordinary-formation pressure anchor because late formations contain **5–6 active enemies**. Their potential direct-damage budget rises 20% without adding turns or HP.

Mandatory check:
> confirm that attrition and focus pressure increase without producing routine unavoidable opening-round wipes.

---

# Historical representative measurements
1. **Hollow Watch Castellan — Chapter 1 / S008 — v93**
   - historical measurement retained; early +20% raw-one-shot safety check currently passes.
2. **Archive Leviathan — Chapter 2 / S013 — v97**
   - historical measurement retained.
3. **Regulation Crucible → The Seventh Reaction — Chapter 4 / S024 — v99**
   - historical measurement retained.
4. **Warden of the Nameless / Revision Arbiter — Chapter 7 — v100**
   - old difficulty PASS provisional under revised standard and +20% sensitivity.
5. **Commander Rhazek → Bastion Devourer — Chapter 9 — v101**
   - old difficulty PASS provisional;
   - fresh-body / Prime-persistence findings retained.
6. **Emperor Vaelkor → Sovereign Panoply Unbound — Chapter 12 — v102**
   - old difficulty PASS provisional;
   - old mandatory no-Prime any-KO was only 1.98%; Sovereign Overrun 390 becomes **468 test Power** under v104;
   - fresh-body / Overrun / Prime-persistence findings retained.

---

# Forward order
1. Check early ordinary formations for +20% spike safety.
2. **Deepforge Colossus — Chapter 5** — assembly correction + +20% scalar; lock first new difficulty anchor.
3. Continue forward through later chapter climaxes using the same-gear method and common +20% layer.
4. Mark specific outliers below/above the global baseline only when testing justifies it.
5. Revisit Rhazek and Vaelkor.
6. **Reconstituted Entity → The Last Command** only after the late-game mandatory difficulty curve is anchored.
7. **The Unfinished World** remains the exhaustive completionist full-kit stress test.

The suite remains **ACTIVE / RECALIBRATING**. Design-layer simulations do not replace runtime QA.

## Current Bleed rule
All recalibration simulations continue using the current Bleed escalation rule:
- 3% Max HP per qualifying ordinary proc;
- escalates to 4% after three affected turns uncleared;
- mandatory-boss conversion 1.5% → 2%.
