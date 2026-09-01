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

## Chapter-5 ordinary full-status isolation
A 5,000-run-per-formation design-layer isolation pass was run at the current phase-appropriate mandatory levels:
- opening formations — Lv18;
- middle formations — Lv19;
- late formations — Lv20;
- active four — Cyanis / Ilyra / Torren / Vaelira;
- same conservative Chapter-4-or-earlier ordinary equipment used by the Deepforge same-gear benchmark;
- no Prime;
- current Burn / Bleed / Stun / Staggered behavior included;
- normal target priority, healing and status-clearing policy;
- each formation begins at full HP / full MP so this is encounter-isolation pressure, not a whole-dungeon attrition proof.

Key results:

| Formation | Current any-KO | ×1.20 any-KO | Current mean direct damage | ×1.20 mean direct damage |
|---|---:|---:|---:|---:|
| Opening Heat Line | 0% | **0%** | ~597 | **~724** |
| Middle Crawler Floor | 0% | **0.08%** | ~815 | **~986** |
| Late Heavy Foundry | 0% | **0.08%** | ~859 | **~1,048** |
| Late Forge Lock | 0.02% | **0.22%** | ~1,082 | **~1,325** |

All nine recovered Chapter-5 ordinary formations remained effectively reliable clears in encounter isolation.

Interpretation:
> **The +20% scalar increases ordinary encounter attrition and focus-fire consequence without turning Chapter-5 random formations into routine death traps.**

A later whole-dungeon attrition pass still needs to test how repeated encounters consume healing/MP/items between recovery points.

---

# Furnace Tyrant — Chapter-5 named-fight sensitivity

A 10,000-run-per-line design-layer model compared current direct Power against ×1.20 using the same conservative ordinary equipment on both route references.

Route anchors:
- mandatory — **Lv18**;
- completionist — **Lv20**;
- no Relic/Legacy advantage in the core comparison.

## Mandatory Lv18

| Policy | Current | ×1.20 |
|---|---|---|
| Smart cooling/support-clear | 100% wins / **0.12% any-KO** / median 10 | **99.99% wins / 0.55% any-KO / median 11** |
| Aggressive high-Heat | 100% wins / **0.89% any-KO** / median 7 | **100% wins / 3.60% any-KO / median 7** |

Mean ending HP:
- smart — ~76.0% current → **~73.1% at ×1.20**;
- aggressive — ~66.7% current → **~60.5% at ×1.20**.

No meaningful wipe pattern emerged in this model.

## Completionist Lv20 — same equipment
- smart ×1.20 — **100% wins / 0% any-KO observed**;
- aggressive ×1.20 — **100% wins / 0.08% any-KO**.

Interpretation:
> **The global +20% scalar helps Furnace Tyrant but does not make the fight threatening enough under competent mandatory-route play.**

Furnace Tyrant should therefore remain flagged for encounter-specific difficulty tuning even if the global ×1.20 baseline is later promoted.

This is evidence for a global floor plus local boss tuning, not evidence against the scalar.

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

## Deepforge ×1.20 rerun — structural assembly candidate
The same v103 harness was rerun with the preferred assembly correction:
- Guard Press provides its functional defensive modifier without consuming a selected boss action;
- Repair Arm uses its bounded conditional passive repair rather than diluting the attack menu;
- Command Loom remains the accuracy function;
- both routes use the exact same ordinary equipment and normal-stock preparation;
- no Relic/Legacy advantage is given to completionist.

5,000-run same-gear sensitivity:

| Route | Win rate | Any-KO | Wipe |
|---|---:|---:|---:|
| **Lv20 mandatory — rush** | **92.82%** | **48.98%** | **7.18%** |
| **Lv20 mandatory — dismantle all** | **99.56%** | **21.74%** | **0.44%** |
| **Lv22 completionist — rush** | **100%** | **1.96%** | **0% observed** |
| **Lv22 completionist — dismantle all** | **100%** | **1.02%** | **0% observed** |

Interpretation:
1. **Mandatory vs completionist separation is strong even with identical gear.**
2. **Ignoring the assembly mechanic is now a legitimate risk.** Nearly half of mandatory rush runs see at least one KO and roughly 7% wipe.
3. **Respecting the mechanic matters.** Dismantling cuts mandatory KO incidence from ~49% to ~22% and wipe incidence from ~7.2% to below 0.5%.
4. **Optional progression buys margin for error.** Lv22 completionist remains very safe on the exact same equipment.
5. The boss still does not rely on one-shot design; the pressure comes from sustained offense, statuses, assembly consequences and recovery decisions.

Deepforge therefore becomes the first strong evidence that:
> **×1.20 is a viable global enemy-offense baseline when the encounter's own mechanics are structurally sound.**

The assembly action-density correction remains necessary; the scalar by itself does not repair the old Guard Press / Repair Arm incentive problem.

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

# Current verdict after Chapter 5

> **STRONGLY PROMISING AS GLOBAL BASELINE / NOT YET CANONICAL OWNER VALUES**

Chapter-5 evidence currently says:
- ordinary formations — **PASS the +20% safety/attrition screen**;
- Furnace Tyrant — **still too safe; local boss tuning remains required**;
- Deepforge Colossus with the structural assembly correction — **lands near the desired mandatory/completionist difficulty profile at ×1.20**.

Immediate next sensitivity action:
> carry the same **enemy direct-damage Power ×1.20** layer into Chapter 6 ordinary formations and named bosses before deciding whether the scalar should be promoted globally.
