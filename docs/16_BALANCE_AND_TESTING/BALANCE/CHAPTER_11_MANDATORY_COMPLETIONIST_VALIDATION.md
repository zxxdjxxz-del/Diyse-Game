# Chapter 11 — Mandatory vs Completionist Enemy/Boss Validation

**Version:** v87  
**Status:** **PASS / VALIDATED WITH ACTION-WEIGHT AND TECHNICIAN-PLACEMENT DEPENDENCIES**  
**Power-audit status:** **CLOSED — no direct-damage Power changed**

## Purpose
Validate current Chapter 11 — **Crown Engine / Calder / Custodian / Truth** — against the player state that actually exists at each encounter point rather than treating **Lv52** as the whole chapter baseline.

Chapter 11 uses the post-Volition combat framework:
- all six permanent characters are available;
- active battle party remains **maximum 4**;
- Subclasses are legal throughout;
- optional EXP/CEXP, equipment, Relics/Legacies, Cards, Primes, Hunts, and Character Quests are allowed to create a real completionist advantage;
- fixed authored enemies do not dynamically scale upward to erase that advantage.

The direct-damage Power audit remains closed. No Chapter-11 action requires a Power retune.

---

## 1. Chapter-level progression anchors
Mandatory campaign spine:
> **Lv47 chapter start → Lv52 chapter end**

Fixed Chapter-11 mandatory EXP:
- Chapter-10 clear: **237,600 EXP = Lv47**;
- ordinary allocation: **45,300 EXP**;
- named/story allocation: **16,200 EXP**;
- Chapter-11 clear: **299,100 EXP = Lv52**.

Current exact story-boss allocation already fixes the major internal anchors:
- pre-Calder ordinary route: **+27,000 EXP**;
- mandatory pre-Calder: **264,600 EXP = Lv49**;
- Calder/Living Anchor clear: **+4,000 → 268,600 EXP = Lv49**;
- deeper administrative-domain ordinary route: **+18,300**;
- mandatory pre-Custodian: **286,900 EXP = Lv51**;
- Custodian/direct-contact reward: **+2,500 → 289,400 EXP = Lv51**;
- later truth/reckoning/clear rewards finish at **299,100 EXP = Lv52**.

### Practical mandatory route bands
- Crown Engine opening: **Lv47→48**;
- late Crown Engine / Calder approach: **Lv48→49**;
- Calder: **Lv49**;
- deeper Custodian domain: **Lv49→51**;
- Custodian: **Lv51**;
- chapter resolution: **Lv51→52**.

### Completionist route
Fixed optional advantage available by Chapter-11 entry under current authored content:
- available Side Quests — **5,500 EXP**;
- all six Character Quests — **55,000 EXP**;
- Regional Hunts #1–#9 — **43,200 EXP**;
- Major Hunts #1–#4 — **31,500 EXP**.

Total fixed optional advantage:
> **135,200 EXP**

Therefore:
- Chapter-11 completionist start: **372,800 EXP = Lv57**;
- pre-Calder: **399,800 EXP = Lv59**;
- pre-Custodian: **422,100 EXP = Lv60**;
- Chapter-11 clear without RH#10: **434,300 EXP = Lv61**.

Regional Hunt #10 — Authority Remnant grants **13,000 EXP**, but its exact within-Chapter-11 access relative to S062/S063 remains unresolved. It is therefore not assumed in the fixed pre-boss proof.

If it is legally cleared before the Custodian:
> **435,100 EXP = Lv61** pre-Custodian.

At full Chapter-11 clear plus RH#10:
> **447,300 EXP = Lv61**, only 800 EXP short of Lv62.

Optional Elite/incidental combat can also move the high side within the same general **Lv60–61** neighborhood.

---

## 2. Party / Subclass / Prime boundary
Throughout Chapter 11:
- all six permanent characters are available;
- only **4** act in battle;
- Subclasses are legal;
- current post-Volition Prime-slot rules are legal where the relevant Primes have been acquired/awakened;
- no guest expands the active cap.

The **v91 CEXP recalibration** now places normal full class completion at ~Lv55–60. True-battle testing must use the resulting Class-Level breadth; Chapter-11 enemies are not pre-emptively inflated.

---

## 3. Recovered Chapter-11 formation authority
The approved Chapter-11 composition/weight set was recovered from the late working tracker and restored to:
> `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_11_FORMATIONS.md`

Only **composition and weight** are recovered. Historical phase-specific enemy levels and old formation EXP rows are superseded by the current v87 individual raw bodies and current progression budgets.

### Crown Engine opening
| Formation | Composition | Weight |
|---|---|---:|
| Engine Guard | 2 Crown Engine Sentinel + 1 Continuity Adjudicator + 1 Emergency Executor Frame | 30% |
| Continuity Cell | 1 Crown Engine Sentinel + 2 Continuity Adjudicator + 1 Emergency Executor Frame | 45% |
| Executor Screen | 2 Crown Engine Sentinel + 1 Continuity Adjudicator + 2 Emergency Executor Frame | 25% |

Current combined HP:
- Engine Guard — **6,480**;
- Continuity Cell — **6,620**;
- Executor Screen — **8,380**.

### Custodian domain — middle
| Formation | Composition | Weight |
|---|---|---:|
| Protocol Line | 2 Administrative Sentinel + Permission Scribe + Element Matrix + Grace Curator | 30% |
| Bastion Filing | Administrative Sentinel + Permission Scribe + Might Bastion + Grace Curator + Change Schema | 45% |
| Matrix Screen | Administrative Sentinel + Might Bastion + 2 Element Matrix + Permission Scribe + Change Schema | 25% |

Current combined HP:
- Protocol Line — **7,200**;
- Bastion Filing — **7,770**;
- Matrix Screen — **9,390**.

### Custodian domain — late
| Formation | Composition | Weight |
|---|---|---:|
| Administrative Lock | 2 Administrative Sentinel + Permission Scribe + Might Bastion + Grace Curator | 30% |
| Sixfold Archive | Administrative Sentinel + Permission Scribe + Might Bastion + Element Matrix + Grace Curator + Change Schema | 45% |
| Trial Stack | Administrative Sentinel + 2 Might Bastion + Element Matrix + Permission Scribe + Change Schema | 25% |

Current combined HP:
- Administrative Lock — **7,730**;
- Sixfold Archive — **9,290**;
- Trial Stack — **9,920**.

All formations remain below the global 8-enemy hard cap.

---

## 4. Ordinary-enemy incoming-pressure validation
Use **Vaelira's Green Arcanist natural body with no equipment HP/Defense/Spirit** as the deliberately fragile incoming-damage reference. Actual geared parties are safer.

### Crown Engine — Lv47→49 mandatory
Representative strongest actions against the appropriate route-level body:
- Crown Engine Sentinel — Sentinel Blade: **~12.8% Max HP** at Lv47;
- Continuity Adjudicator — Continuity Verdict: **~12.3%** at Lv48;
- Continuity Adjudicator — Ruin Citation: **~11.0%**;
- Emergency Executor Frame — Emergency Crush: **~16.1%** at Lv49;
- Emergency Executor Frame — Execution Sweep: **~11.1% per target**.

The opening formation threat therefore comes from 4–5-body action economy, Stun/Staggered pressure, and Guard turns rather than one-action deletion.

### Deeper administrative domain — Lv49→51 mandatory
Representative strongest actions:
- Administrative Sentinel — Administrative Edge: **~12.0% Max HP**;
- Permission Scribe — Permission Ray: **~11.1%**;
- Might Bastion — Might Impact: **~17.1%**;
- Might Bastion — Bastion Sweep: **~11.5% per target**;
- Element Matrix — Matrix Lance: **~12.7%**;
- Element Matrix — Matrix Wave: **~9.3% per target**;
- Grace Curator — Curator Ray: **~10.7%**;
- Change Schema — Schema Cut: **~11.0%**.

The current Element Matrix four-element rotation remains exactly Fire / Ice / Lightning / Earth. No Wind/Water state is introduced.

At the completionist **Lv57–61** range these percentages fall materially, preserving the intended optional-progression advantage.

**Verdict:**
> **PASS / RETAIN ALL CHAPTER-11 ORDINARY RAW STATS AND POWERS.**

---

## 5. Formation durability / action economy
A conservative four-character AoE reference using long-established Base-Class AoEs — Sweeping Edge, Weave Burst, Stormburst, and Fracturing Brand — with **no equipment offense added** produces roughly the following same-round per-target throughput at the relevant levels:
- Permission Scribe: roughly **2.2–2.4 serious AoE rounds**;
- Grace Curator: roughly **2.7–3.0**;
- Crown Engine Sentinel / Element Matrix / Administrative Sentinel / Change Schema: roughly **2.8–3.4**;
- Continuity Adjudicator: roughly **3.1–3.5**;
- Emergency Executor Frame: roughly **3.6–4.0**;
- Might Bastion: roughly **4.0–4.5**.

This is deliberately conservative:
- no weapon MAG/ATK bonuses;
- no Relics/Legacies;
- no Subclass optimization;
- no Standard Cards;
- no Prime use;
- no criticals/affinity exploitation;
- no stronger later abilities.

Because every enemy in a formation is being damaged simultaneously, lighter Scribes/Curators/Matrices collapse first and the enemy turn count decays before the Bastions/Executors finish. The 5–6-body Custodian-domain formations therefore act as late-game MP/status/target-priority pressure rather than six boss-health enemies.

### Remaining formation dependency
Current simplified individual v87 enemy files do not expose exact per-action selection weights for the full Chapter-11 ordinary roster.

Therefore exact worst-case Stun/Freeze/Staggered probability is still:
> **OPEN — ACTION-WEIGHT DATA DEPENDENCY**

This is not evidence for a raw-stat or Power retune.

---

## 6. Authored protected encounter — Crown Engine Technician
Retain:
> Lv48 / **1,260 HP** / ATK118 / MAG142 / DEF92 / Spirit98 / SPD38 / EVA0 / SR5

Current actions remain:
- Control Rod — 185 Power;
- Safety Discharge — 195 Lightning / 15% Stun;
- Emergency Vent — 135 Fire AoE;
- Protect Position — Power N/A.

At 0 HP the Technician is disabled/disarmed, not killed.

The kit is numerically safe for its chapter band and does not need retuning.

Still open:
> **exact authored scene placement**

Do not random-spawn the Technician merely to close that placement dependency.

**Verdict:**
> **PASS ON KIT / PLACEMENT DEPENDENCY RETAINED.**

---

## 7. Optional Elite — Perfect Administrator
Retain:
> **Lv55 / 5,800 HP / ATK180 / MAG198 / DEF137 / Spirit141 / SPD52 / EVA5 / SR10**

Actual validation band:
- mandatory plausible access: **~Lv49–51** depending exact optional branch placement;
- completionist: **~Lv59–61**.

On the deliberately fragile no-equipment reference at Lv49–51:
- Perfect Judgment: about **17–18% Max HP**;
- Administrative Ruin: about **16–18%**;
- Perfected Directive: about **12–13% per target**;
- Enforcement Sequence total: about **18–20%**.

At Lv59–61 completionist these strongest direct actions fall to roughly **13–15%**.

A conservative four-attacker mandatory reference using only current ordinary Chapter-11 weapon bonuses plus established CL9-or-earlier single-target abilities produces approximately **1,320–1,375 damage per serious round** against the Administrator before stronger Subclass/Card/Prime/Ultimate optimization.

Therefore 5,800 HP is approximately **4.2–4.4 conservative serious rounds** before stronger legal late-game tools. This sits on the intended Elite boundary and drops cleanly into the 2–4-round neighborhood once normal build strength is allowed.

Absolute Procedure consumes the Administrator's selected action and grants no extra turn, so it does not create hidden action-economy inflation.

**Verdict:**
> **PASS / FORMALLY VALIDATED v87 / RETAIN ALL RAW STATS AND POWERS.**

---

## 8. Mandatory boss — Chancellor Othmar Calder → Crown-Bound Living Anchor
Actual player references:
- mandatory — **Lv49**;
- completionist fixed-content — **Lv59**;
- high-side — **~Lv60**.

Retain Form I:
> Lv54 / **10,133 HP** / ATK137 / MAG193 / DEF118 / Spirit134 / SPD50 / EVA5 / SR10

Retain:
- 2 Authentication Lenses, **600 HP each**;
- each Lens +5 Total Defense / +5 Base Hit while intact;
- no independent Lens turn.

Retain fresh Form II:
> Lv55 / **13,662 HP** / ATK181 / MAG204 / DEF139 / Spirit139 / SPD47 / EVA0 / SR10

Retain:
- 2 Living Anchor Clamps, **720 HP each**;
- each Clamp +5 Total Defense while intact;
- finite Interruptible-Preparation Continuity Collapse;
- maximum 2 successful Collapse resolutions;
- genuine fresh-body Prime availability refresh at the Form-I → Form-II transition.

On the fragile no-equipment Lv49 reference:
- strongest ordinary Form-I single target is roughly **~17% Max HP**;
- Form-II normal high hits are roughly **~18%**;
- Continuity Collapse is roughly **~21% per target** if the loaded Clamp is not destroyed.

At Lv59 completionist those same peaks fall to roughly **~13–16%**.

Existing duration target remains coherent:
- mandatory — **~15–17 rounds**;
- completionist — **~12–14**;
- high-side — **~11–13**.

The two finite support sets create target-priority/action-tax decisions without adding independent enemy turns.

**Verdict:**
> **PASS / FORMALLY VALIDATED v87 / RETAIN ALL RAW STATS, SUPPORT VALUES, THRESHOLDS, AND POWERS.**

---

## 9. Mandatory boss — The Custodian
Actual player references:
- mandatory — **Lv51**;
- completionist fixed-content — **Lv60**;
- high-side — **~Lv61**.

Retain:
> Lv55 / **16,017 HP** / ATK177 / MAG190 / DEF144 / Spirit146 / SPD48 / EVA0 / SR10

State A support objects remain:
- Acuity Node — **700 HP**, Power N/A, +10 Base Hit / +10 Speed;
- Ruin Containment Seal — **760 HP**, Power N/A, +10 Total Defense / −15% final direct Ruin damage taken.

Both are finite, non-attacking, non-respawning supports.

Open Reconciliation remains:
> **45% HP / same bar / no refill / no free attack / no Prime refresh**

At the fragile no-equipment Lv51 reference:
- State-A strongest direct actions are roughly **~15–17% Max HP**;
- State-B high single-target/sequence actions are roughly **~18–19%**;
- State-B AoE pressure is roughly **~9–12% per target**.

At Lv60 completionist, strongest direct actions fall to roughly **~12–15%**.

Existing duration target remains coherent:
- mandatory — **~11–12 rounds**;
- completionist — **~8–9**;
- high-side — **~7–8**.

The same-bar 45% transition deliberately becomes faster and more exposed rather than adding a second health body.

**Verdict:**
> **PASS / FORMALLY VALIDATED v87 / RETAIN ALL RAW STATS, SUPPORT VALUES, THRESHOLDS, AND POWERS.**

---

## 10. Regional Hunt #10 — Authority Remnant
Retain:
> **recommended Lv56 / 21,913 HP / ATK200 / MAG214 / DEF149 / Spirit154 / SPD51 / EVA5 / SR10**

This Hunt is fixed authored tuning. Its exact Chapter-11 access point remains unresolved, so no false S### timing is invented.

Difficulty relationship:
- mandatory Chapter-11 clear — **Lv52**, intentionally under recommendation;
- fully optional Chapter-11 entrant — **Lv57**, already around recommendation;
- completionist mid/late Chapter 11 — **Lv59–61**, meaningfully advantaged.

At the recommended Lv56 on the fragile no-equipment Green Arcanist reference:
- Authority Judgment — roughly **~22% Max HP**;
- Remnant Ray — **~21%**;
- Citation Shock — **~20%** plus 25% Stun;
- Authority Field — **~15% per target**.

Finite Echo Nodes remain:
- at 70% and 35% HP;
- maximum 2 total;
- **1,050 HP each**;
- no independent turns;
- no repair/respawn;
- each supplies finite Magic/Defense support while functional.

One continuous HP bar means no Prime availability refresh.

**Verdict:**
> **PASS / FORMALLY VALIDATED v87 / RETAIN RECOMMENDED LV56, RAW STATS, POWERS, AND ECHO ARCHITECTURE.**

Exact within-Chapter-11 access remains a story/world-state dependency, not a balance failure.

---

## 11. Post-Chapter-11 Major Hunt #5 — Final Archive Arbiter
Existing recertification remains coherent and is formally carried into the two-baseline chapter proof.

Retain:
> **recommended Lv65 / Lv65 body / 52,600 HP / ATK258 / MAG276 / DEF202 / Spirit211 / SPD56 / EVA5 / SR15**

First-access relationship:
- mandatory Chapter-11 clear — **Lv52**;
- completionist with all normally available optional EXP through Chapter 11 including RH#10 — **447,300 EXP = Lv61**, only 800 EXP short of Lv62;
- recommendation — **Lv65**.

The Arbiter therefore remains clearly above both the story-clear party and the completionist party at unlock.

Custody Protocols, Archive Burden, and Transfer Windows remain one continuous HP-bar architecture and do not refresh Prime availability.

**Verdict:**
> **PASS / FORMALLY CARRIED FORWARD v87 / NO NUMERICAL CHANGE.**

---

## 12. Chapter-11 result
### Retained unchanged
- all 9 ordinary Chapter-11 enemy raw bodies;
- all current direct-damage Powers;
- recovered formation compositions/weights;
- Crown Engine Technician kit;
- Perfect Administrator;
- Calder → Crown-Bound Living Anchor and all supports;
- The Custodian and all supports;
- Authority Remnant;
- Final Archive Arbiter post-chapter recommendation/raw line.

### Numerical changes
> **NONE**

### Direct-damage Power changes
> **NONE**

### Remaining Chapter-11 dependencies
1. exact ordinary per-action selection weights are not exposed in the current simplified owning files;
2. Crown Engine Technician exact authored scene placement remains bounded but unresolved;
3. Authority Remnant exact within-Chapter-11 access timing remains unresolved.

These are not reasons to reopen current raw stats or Power values.

## Final verdict
> **CHAPTER 11 — PASS / VALIDATED v87**

Next validation frontier:
> **Chapter 12 — Lv52 start → Lv57 end**, with all six permanent characters, four active, Subclasses legal throughout, and post-Chapter-11 optional progression carried forward normally.
