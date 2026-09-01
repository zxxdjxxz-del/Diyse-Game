# Diyse — Global Enemy Direct-Damage Power +20% Sensitivity — v104

**Status:** **WORKING TEST MODIFIER / NOT OWNER CANON**  
**Reason:** mandatory-route difficulty recalibration after v103 same-gear testing showed enemy offense is too forgiving.  
**Primary anchor:** Chapter 5 Deepforge recalibration.

## Test hypothesis
Apply one clean global enemy-offense scalar:

> **Enemy direct-damage Power × 1.20**

This is a sensitivity experiment before editing individual enemy owners.

Because Diyse's direct-damage formulas multiply by `Power / 100`, a +20% Power scalar produces approximately **+20% direct damage** from the affected hit before Crit, Defend/direct-damage reduction, and other legal final modifiers.

## Scope
For this sensitivity layer, multiply the authored direct-damage Power of hostile actions by **1.20** for:
- ordinary enemies;
- Elites;
- authored/protected hostile combatants;
- mandatory named/story bosses;
- Regional Hunts;
- Major Hunts;
- hostile support actors/objects when they actually deal ordinary direct damage;
- an enemy Basic Attack if an encounter legally uses the universal 100-Power Attack command.

Apply the scalar to each authored hit of a multihit action individually.

## Explicitly unchanged
Do **not** multiply:
- HP;
- ATK / MAG / DEF / Spirit / Speed / Evasion / Status Resistance;
- Base Hit;
- Crit chance or Crit multiplier;
- status application chance;
- Burn/Bleed magnitude;
- fixed damage;
- percentage-Max-HP damage;
- healing or repair values;
- shields/temporary stat changes;
- AI weights, repetition locks or cooldowns;
- number of enemy turns;
- encounter composition;
- boss form architecture;
- Prime rules.

Support actions with `Power: N/A` remain N/A.

## Test arithmetic rule
During sensitivity simulation, use the exact multiplier rather than pre-rounding owner values:

> **TestPower = AuthoredPower × 1.20**

If the scalar is later promoted into canon, owner-file Powers can be rounded cleanly as a separate implementation pass.

---

# Early-game safety check — Chapter 1

Chapter-1 ordinary formations contain 3–4 enemies. Current ordinary direct-damage Powers range mostly from 115–160, with the Hollow Watch Ballista's marked Heavy Bolt at 200.

Representative conversions:
- Black Host Raider — 120 / 145 → **144 / 174**;
- Black Host Crossbowman — 125 / 155 → **150 / 186**;
- Brackenwall Reaver — 130 / 150 → **156 / 180**;
- Briar Boar — 160 / 145 → **192 / 174**;
- Hollow Watch Ballista — 135 / marked 200 → **162 / marked 240**.

Against the existing Lv2 Hollow Watch benchmark, a 240-Power marked Ballista shot remains far below a raw one-shot:
- Cyanis — roughly **37 HP** vs 267 Max HP;
- Ilyra — roughly **51 HP** vs 254 Max HP;
- Maevra — roughly **56 HP** vs 267 Max HP.

Representative old Hollow Watch Castellan direct hits also scale cleanly:
- 44 damage → about **53**;
- 50 → about **60**;
- 30 → about **36**;
- 41 → about **49**.

Initial safety read:
> **+20% does not create an obvious Chapter-1 one-shot problem.**

The early-game risk to watch is cumulative formation focus and attrition, not single-hit lethality.

---

# Chapter-5 ordinary formation conversion

Current Chapter-5 ordinary formations contain 4–6 enemies, so a +20% global direct-Power scalar raises total potential formation offense without adding HP or turns.

| Enemy | Current direct Powers | +20% test Powers |
|---|---|---|
| Furnace Cohort | 160 / 185 | **192 / 222** |
| Black Host Forge Guard | 175 / 200 | **210 / 240** |
| Siege Engineer | 170 Fire / 130 AoE | **204 / 156** |
| Furnace Servitor | 150 / defeat 80 AoE | **180 / 96** |
| Ruin Hammerman | 210 / 190 Ruin | **252 / 228** |
| Deepforge Repair Frame | 145 / 155 Lightning | **174 / 186** |
| Deepforge Lifter | 195 / 220 | **234 / 264** |
| Molten Crawler | 165 Fire / 130 AoE / 150 | **198 / 156 / 180** |

Authored / Elite Chapter-5 reference:
- Highland Resistance Fighter — 165 / 185 / 125 AoE → **198 / 222 / 150**;
- Ruin Forgemaster — 240 / 225 / 210 / 175 AoE → **288 / 270 / 252 / 210**.

Important ordinary-encounter watchpoint:
> **Late Chapter-5 formations can contain 5–6 active enemies.**

The scalar therefore needs formation-level testing for first-round focus/spike behavior even if every individual hit remains reasonable.

---

# Deepforge Colossus conversion

Using the current owner Powers before any assembly rewrite:

## Assembly Frame
- Construction Hammer — 205 → **246**;
- Load-Bearing Sweep — 140 → **168**;
- Forge Discharge — 195 → **234**;
- Clamp and Draw — 170 → **204**.

## Worldsmith Body
- Worldsmith Clamp — 225 → **270**;
- Foundry Arc — 215 → **258**;
- Construction Sweep — 155 → **186**;
- Worldline Crush — 260 → **312**;
- Forge Collapse — 300 → **360**.

Against the same-gear mandatory Lv20 party, the current unguarded Forge Collapse benchmark of roughly 178–223 damage becomes approximately:
- Cyanis — **214 / 1,015 HP**;
- Ilyra — **252 / 967 HP**;
- Torren — **246 / 967 HP**;
- Vaelira — **268 / 793 HP**.

This remains approximately **21–34% Max HP before Defend**. Standard Defend still halves eligible direct damage.

This is materially harder but is not an unavoidable one-shot package.

## Relationship to the v103 +15% structural candidate
The preferred v103 assembly-rewrite candidate used approximately +15% direct Power and produced:
- mandatory Lv20 rush — 96.665% wins / 37.37% any-KO / 3.335% wipes;
- mandatory Lv20 dismantle — 99.87% wins / 14.165% any-KO / 0.13% wipes;
- completionist Lv22 same-gear rush — 100% wins / 0.58% any-KO;
- completionist Lv22 same-gear dismantle — 100% wins / 0.315% any-KO.

A global +20% scalar is only:
> **1.20 / 1.15 = 1.0435**

or about **4.35% more direct damage than that +15% candidate**.

Therefore the +20% experiment should remain in the same broad difficulty neighborhood rather than behaving like the rejected brute-force +45% Power-only package. Exact KO/wipe distributions must still be rerun under the +20% scalar before locking owner values.

The assembly action-density correction remains necessary; the global scalar does not by itself fix the Guard Press / Repair Arm incentive problem.

---

# Late-game reference — Vaelkor

Representative major telegraph:
- Sovereign Overrun resolution — 390 Power → **468 test Power**.

No HP, raw stats, Overrun timing, preparation window, status behavior, or Prime interaction changes in this sensitivity layer.

The old v102 mandatory no-Prime result was only 1.98% any-KO despite a 21-round median, which is exactly the type of long-but-safe result this scalar is intended to pressure.

---

# What this experiment is trying to determine

The +20% global Power scalar is promising if it produces all of the following:
1. ordinary encounters consume more healing/MP and punish careless focus without producing routine opening-round wipes;
2. mandatory-route chapter bosses generate temporary KOs often enough to require recovery play;
3. same-gear completionist parties remain substantially safer because of Player Level/CEXP/ability advantage;
4. telegraphed boss mechanics become dangerous when ignored but remain answerable when respected;
5. Major Hunts and the final completionist superboss remain allowed to exceed the ordinary global difficulty floor through their own mechanics/tuning.

## Do not infer
A successful +20% sensitivity does **not** automatically mean every individual Power must be permanently multiplied by exactly 1.20.

After representative testing, specific outliers may need:
- less than +20% because of multi-enemy burst or multihit architecture;
- exactly +20%;
- more than +20% where a climax/Hunt remains too safe.

The scalar is a whole-roster baseline experiment, not a prohibition on encounter-specific tuning.

# Current verdict

> **APPROVED FOR GLOBAL SENSITIVITY TESTING / NOT YET CANONICAL OWNER VALUES**

Immediate balance direction:
> use **enemy direct-damage Power ×1.20** as the common test layer, beginning with early ordinary formations + Chapter-5 Deepforge and carrying the same scalar through later representative bosses before deciding whether to promote it globally.
