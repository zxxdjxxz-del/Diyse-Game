# Diyse — Chapter 3 Mandatory-vs-Completionist Validation

**Version:** v79  
**Status:** **ADJUSTED / VALIDATED**  
**Scope:** Chapter 3 ordinary formations, authored nonlethal encounters, optional Elite, First Command Warden, and Regional Hunt #3  
**Power-audit boundary:** **CLOSED — no direct-damage Power coefficient changed in this pass**

## 1. Actual chapter-level spine
Chapter 3 is not validated at one flat level.

Mandatory-route checkpoints:
- **Chapter start / S017:** Lv9
- **S018 lawful confrontations:** Lv9
- **S019 early Suppressed Archives / Nimera recruitment:** Lv9 trending into Lv10
- **S019–S020 repeatable Archive / command-route combat:** Lv10 trending into Lv11
- **First Command Warden:** **Lv11 mandatory baseline**
- **Post-Warden / chapter close:** Lv12 trending to exact Lv13 chapter-clear target

Completionist checkpoints:
- authored optional EXP available before Chapter 3 can place the party around **Lv10 at chapter start**;
- by First Command Warden, fixed optional progression supports **Lv12, close to Lv13**;
- incidental optional Elite/extra authored combat may tip the high-side party to Lv13 before the Warden.

The chapter-clear normal-route anchor remains **Lv13**.

## 2. Party-state chronology

### Before Nimera joins
Active battle party:
- Cyanis
- Ilyra
- Torren
- **Maevra — guest combatant**

Maevra is not a narrative-only companion. Her current working combat package is included in all relevant Chapter 3 calculations:
- party-synchronized Character Level while playable;
- fixed guest spear **+18 ATK**;
- Commander's Harness **+9 DEF / +9 Spirit**;
- EVA 5 / SR 5;
- Linebreaker Thrust **165 Power / 15% DEF penetration / 10 MP**;
- Spear Sweep **120 Power AoE / 12 MP**;
- Hold Formation **+10% DEF/Spirit / 2 rounds / 14 MP**;
- Advance Order **+10% ATK / 2 rounds / 14 MP**;
- Decisive Thrust **235 Power / 25% DEF penetration / 18 MP**.

This remains a **working balance reference**, not a new permanent-class progression system.

### After Nimera joins in S019
Combat roster becomes:
- Cyanis
- Ilyra
- Torren
- Nimera
- Maevra (guest)

Battle hard cap remains **4 active party members**. The player selects four from the five available combatants once the choose-four state is active.

The first scripted Archive Scribe Engine onboarding battle must also obey the four-active-character cap while making Nimera battle-available; it must never instantiate five active player bodies.

## 3. Recovered Chapter-3 formation authority
The reorganized v78 package retained the enemy identities and current raw bodies/Powers but omitted the previously approved formation-composition table.

Restore the following **composition/weight authority only**. Old formation EXP values and old enemy raw lines are not restored; current v79 enemy files control those numbers.

### Opening / hostile perimeter
| Formation | Composition | Weight |
|---|---|---:|
| Way-Fort Patrol | 2 Way-Fort Marauders + 1 Rift Boltman | 30% |
| Rift Screen | 1 Way-Fort Marauder + 2 Rift Boltmen + 1 Black Host Ward-Sorcerer | 45% |
| Marauder Push | 2 Way-Fort Marauders + 1 Rift Boltman + 1 Black Host Ward-Sorcerer | 25% |

### Suppressed Archives
| Formation | Composition | Weight |
|---|---|---:|
| Archive Judgment | 1 Archive Scribe Engine + 1 Judgment Frame + 1 Erasure Wisp | 30% |
| Erasure File | 2 Archive Scribe Engines + 2 Erasure Wisps + 1 Judgment Frame | 45% |
| Judgment Stack | 2 Judgment Frames + 1 Archive Scribe Engine + 1 Erasure Wisp | 25% |

### Deep Old City / command route
| Formation | Composition | Weight |
|---|---|---:|
| Command Screen | 2 Command-Station Sentries + 1 Authority Lens + 2 Command Ring Drones | 30% |
| Authority Net | 1 Command-Station Sentry + 2 Authority Lenses + 3 Command Ring Drones | 45% |
| Station Lock | 2 Command-Station Sentries + 2 Authority Lenses + 2 Command Ring Drones | 25% |

Current body-count range remains 3–6, below the global 8-enemy hard cap.

## 4. Ordinary formation validation

### Opening pool — Lv9 mandatory / ~Lv10 completionist
Current raw bodies:
- Way-Fort Marauder — 270 HP
- Rift Boltman — 225 HP
- Black Host Ward-Sorcerer — 250 HP

Formation total HP:
- Way-Fort Patrol — **765**
- Rift Screen — **970**
- Marauder Push — **1,015**

Current single-target high actions generally remove only about one-tenth of a normal-route member's HP at this point, while Ward-Sorcerer Stun pressure creates the intended tactical tax.

**Verdict: PASS.**

No raw-stat, status-rate, formation, or Power change required.

### Suppressed Archives — Lv9→10 mandatory / Lv10→11 completionist
Current raw bodies:
- Archive Scribe Engine — 315 HP
- Judgment Frame — 365 HP
- Erasure Wisp — 210 HP

Formation total HP:
- Archive Judgment — **890**
- Erasure File — **1,415**
- Judgment Stack — **1,255**

The Scribe/Frame/Wisp mix correctly shifts pressure from simple perimeter damage toward target priority, support, and Stun/construct pressure. The five-body Erasure File is the intended high-action-economy formation but does not exceed the party's recovery envelope at the Lv9→10 point.

**Verdict: PASS.**

No Power change required.

### Command route — Lv10→11 mandatory / Lv11→12 completionist
Current raw bodies:
- Command-Station Sentry — 345 HP
- Authority Lens — 235 HP
- Command Ring Drone — 255 HP

Formation total HP:
- Command Screen — **1,435**
- Authority Net — **1,580**
- Station Lock — **1,670**

These are intentionally the chapter's densest repeatable formations. Their threat comes from six-body action economy plus support/target-priority pressure rather than inflated individual hits. At the true late-chapter level point their current direct hits remain survivable, and completionist Lv11–12 bodies gain a meaningful but nontrivial advantage.

**Verdict: PASS.**

No Power change required.

## 5. S018 authored lawful/nonlethal encounters

### Confrontation I
Bodies:
- Ivory Watch Guard — 330 HP
- Royal Polearm Officer — 390 HP
- Ivory Crossbow Sentinel — 265 HP

Mandatory player state:
> **Lv9 Cyanis + Ilyra + Torren + Maevra**

The combined 985-HP package is a short authored formation rather than a random-farm enemy pack. Individual restraint hits remain bounded; the party has enough throughput to resolve it without requiring lethal overkill or optional gear.

**Verdict: PASS.**

### Confrontation II — Ivory Adjudicator Sereth
Raw body:
> Lv12 / 950 HP / 47 DEF / 46 Spirit

Protected nonlethal threshold:
> **333 HP / 35%**

Therefore the party only needs to remove **617 effective HP** to satisfy the authored combat resolution.

At Lv9, a serious Cyanis/Ilyra/Torren/Maevra round is approximately **291 direct damage** before Guard/healing tax, so the threshold is reached in roughly 2–3 serious rounds rather than becoming a false 950-HP kill check.

**Verdict: PASS.**

Do not replace the protected threshold with 0-HP victory.

## 6. Optional Elite — Grand Inquisitor Frame

### Current access problem
Placement authority puts the Grand Inquisitor Frame on the **Suppressed Archives optional branch**, which makes its realistic first-clear player state approximately:
- mandatory: **Lv9→10**;
- completionist: **Lv10→11**.

Existing role target:
> **2–4 serious party rounds**

Old body:
> Lv14 / **1,450 HP** / 58 ATK / 62 MAG / 44 DEF / 45 Spirit

Using the true access-level party, 1,450 HP requires roughly:
- **4.6 serious rounds** for the strongest straightforward Lv9 permanent-four offense;
- about **4.8–5.2** for lower-offense legal four-member combinations containing Maevra;
- about **4.4** serious rounds even for the straightforward Lv10 completionist body before Guard/action-tax effects.

That means the old body misses its own Elite duration target before accounting for Inquisitor Guard.

### Targeted correction
Grand Inquisitor Frame HP:
> **1,450 → 1,200**

Retain:
- Lv14
- ATK 58
- MAG 62
- DEF 44
- Spirit 45
- SPD 29
- EVA 0
- SR 10
- Bleed immunity
- every action Power
- every Base Hit value
- Stun rate
- repetition locks
- Guard effect

At 1,200 HP:
- strong Lv9 offense lands around **3.8–4.0 serious rounds**;
- lower-offense legal Lv9 four-member groups remain around the low-four-round range rather than five-plus;
- completionist Lv10–11 parties gain the intended faster clear without deleting the Elite instantly.

**Verdict: ADJUSTED / VALIDATED.**

This is a targeted HP calibration, not a reopening of the Power audit.

## 7. First Command Warden

Current boss body:
> Lv14 / 2,850 HP / 72 ATK / 72 MAG / 43 DEF / 43 Spirit

Actual pre-boss route states:
- mandatory fixed pre-boss EXP: **11,280 total → Lv11**, 820 short of Lv12;
- completionist fixed pre-boss EXP: **14,280 total → Lv12**, 120 short of Lv13;
- completionist high-side can reach **Lv13** through additional authored optional content.

Representative raw serious-round throughput against the Warden before mechanics:
- Lv11 permanent four: ~**342** → ~8.3 raw serious rounds;
- Lv11 Cyanis/Ilyra/Torren/Maevra: ~**326** → ~8.7;
- lowest-offense legal representative four tested at Lv11: ~**308** → ~9.3;
- Lv12 completionist permanent four: ~**359** → ~8.0;
- Lv13 high-side permanent four: ~**370** → ~7.7.

Command Seals, Ring pressure, healing, defense choices, and the same-bar 45% state change naturally extend those raw values into the existing intended boss window.

Maevra therefore does **not** break the Warden calibration, and benching a higher-offense permanent member for her does not make the boss unreasonable.

**Verdict: PASS.**

Retain all current Warden stats/Powers/thresholds.

## 8. Regional Hunt #3 — Archive Judgment Engine

Unlock:
> after the immediate Chapter-3 story resolution / return window

Recommended level:
> **Lv15**

Current body:
> Lv15 / 4,928 HP / 58 ATK / 67 MAG / 46 DEF / 48 Spirit

The normal Chapter-3 clear party is only about **Lv13**, so immediate access is intentionally below recommendation. Do not weaken the Hunt to the moment it becomes visible.

At the recommended Lv15 reference, a four-permanent-character serious direct-damage round with conservative carried gear is roughly **388 damage**, yielding about **12.7 raw serious rounds** before the Hunt's reversal/guard/resource mechanics. Better completionist equipment and optional progression shorten that meaningfully without collapsing Hunt-scale endurance.

**Verdict: PASS.**

No stat or Power change required.

## 9. Placement/data dependency retained

### False-Warrant Adept
Power/raw material is not the issue.

Exact Chapter-3 placement remains unresolved. Therefore:
> **OPEN — DATA/PLACEMENT DEPENDENCY**

Do not add it to repeatable random formations until story placement is deliberately closed.

## 10. Chapter-3 final verdict

### Adjusted
- **Grand Inquisitor Frame HP 1,450 → 1,200**

### Retained
- all nine ordinary enemy raw bodies and direct-damage Powers;
- recovered Chapter-3 formation compositions/weights;
- lawful nonlethal bodies and protected-resolution rules;
- First Command Warden complete current package;
- Archive Judgment Engine complete current package.

### Power audit
> **CLOSED — ZERO DIRECT-DAMAGE POWER VALUES CHANGED**

### Chapter status
> **CHAPTER 3 — ADJUSTED / VALIDATED, with False-Warrant Adept retained as an explicit placement dependency**

## Next frontier
> **Chapter 4**, using its actual chapter-start/intermediate/end levels and the exact point Vaelira becomes battle-available.
