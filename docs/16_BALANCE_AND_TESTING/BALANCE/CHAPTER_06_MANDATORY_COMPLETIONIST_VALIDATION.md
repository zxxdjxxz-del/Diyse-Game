# Chapter 6 — Mandatory vs Completionist Enemy/Boss Validation

**Version:** v82  
**Status:** **PASS / VALIDATED WITH EXPLICIT PLACEMENT DEPENDENCIES**  
**Power-audit status:** **CLOSED — no direct-damage Power changed**

## Purpose
Validate Chapter 6 against the player state that actually exists at each point rather than treating **Lv27** as the whole-chapter baseline.

This pass also fixes the combat-party boundary around Seyrik:
- Cyanis, Ilyra, Torren, Nimera, and Vaelira are the permanent playable roster during the chapter;
- the active battle party remains **maximum 4**;
- Seyrik is an enemy/story identity through his forced-disengagement encounter;
- Seyrik becomes a permanent playable character only in the chapter-end recruitment resolution;
- therefore Seyrik does **not** contribute a sixth playable body to any Chapter-6 encounter being validated here.

The direct-damage Power audit remains closed. Existing Powers are retained unless a specific encounter fails its intended role.

---

## 1. Chapter-level anchors
Current Chapter-6 progression:

> **Lv22 chapter start → Lv23 Crownstorm Roc → Lv24 Matron Zevraya → Lv25 Masked Seyrik → Lv27 chapter end**

Mandatory EXP anchors:
- Chapter start: **44,400 EXP = Lv22**
- Crownstorm Roc pre-boss planning point: **~49,400 EXP = Lv23**
- Matron Zevraya pre-boss planning point: **~57,500 EXP = Lv24**
- immediate post-Zevraya / Masked Seyrik: **~62,000 EXP = Lv25**, close to Lv26
- Chapter end: **69,300 EXP = Lv27**

Fixed optional advantage available before Chapter 6 from established pre-Chapter-6 content:
> **12,200 EXP**

Therefore the fixed-content completionist comparison is approximately:
- Crownstorm Roc: **~61,600 EXP = Lv25**
- Matron Zevraya: **~69,700 EXP = Lv27**
- Masked Seyrik: **~74,200 EXP = Lv27 approaching Lv28**
- high-side with legal Chapter-6 optional content/incidental combat: **~Lv28–29**

Regional Hunt #6 is not inserted into the fixed pre-Zevraya proof because its exact within-chapter S### unlock relative to Zevraya remains unresolved.

### Party state
Playable permanent roster before chapter-end recruitment:
- Cyanis
- Ilyra
- Torren
- Nimera
- Vaelira

Active battle party:
> **maximum 4**

Seyrik:
> hostile/authored story identity until his post-fight recruitment resolution; not a player-party option during the Chapter-6 combat sequence.

Completionist advantage comes from:
- higher Player Level;
- optional prior EXP/rewards;
- stronger legal equipment, Cards, Relics and Prime use;
- party optimization among the five playable permanent characters;

not from a fifth simultaneous action or early Seyrik access.

---

## 2. Weather Crown ordinary enemies — early chapter
Relevant identities:
- Weather Crown Adept — Lv23 / 560 HP
- Storm Feather — Lv23 / 430 HP
- Crown Perch Sentinel — Lv24 / 700 HP
- Storm Roc Juvenile — Lv24 / 760 HP
- Black Host Sky Skirmisher — Lv24 / 590 HP
- Weather Crown Parasite — Lv24 / 470 HP

Target player state:
- mandatory **Lv22→23**
- completionist **Lv24→25**

Using the active natural-stat curve and conservative pre/early-Chapter-6 armor, the heaviest ordinary single-target attacks remain approximately in the **8–18% Max-HP** band on healthy chapter-appropriate characters. Vaelira remains the intended fragile outlier; stronger physical hits are still well below one-action KO territory.

The Weather Crown's danger therefore comes from:
- mixed physical/magical pressure;
- Lightning Stun / Ice Freeze riders;
- multi-enemy action economy;
- target-priority decisions;

rather than inflated individual HP or burst deletion.

**Verdict: PASS / RETAIN.**

No raw-stat or Power change.

---

## 3. Crimson Work ordinary enemies — middle/late chapter
Relevant identities:
- Ruin Vanguard Reaper — Lv25 / 820 HP
- Black Host War-Sorcerer — Lv25 / 610 HP
- Ruin Marker — Lv25 / 390 HP
- Rift Hound — Chapter-6 body — Lv25 / 720 HP
- Iron Maw — Lv26 / 980 HP
- Blood Attendant — Lv26 / 650 HP

Target player state:
- mandatory **~Lv24→26**
- completionist **~Lv27→28**

Representative conservative checks keep the strongest ordinary attacks in roughly the **7–16% Max-HP** band at their real route levels. Iron Maw correctly produces the largest physical spike, while War-Sorcerer/Blood Attendant pressure the lower-Spirit party members without approaching one-action deletion.

The HP progression from ~390–980 creates meaningful target priority without turning ordinary bodies into Elites.

**Verdict: PASS / RETAIN.**

No raw-stat or Power change.

### Formation boundary
Chapter 6 is not line-complete and the reorganized library does not contain an approved exact Chapter-6 ordinary-formation table.

This pass therefore certifies:
- individual bodies;
- current action lethality;
- durability at the proper early/mid/late level bands;
- compatibility of enemy roles in mixed formations.

It does **not** invent exact random formations, weights, scene IDs, or encounter counts.

Exact formation-level action-economy certification remains:
> **OPEN — DATA/STORY-PLACEMENT DEPENDENCY**

This is not a Power gap.

---

## 4. Authored / protected Chapter-6 identities
### Weather Crown Shield Guard
- Lv24 / 860 HP
- Shield Strike 180
- Crown Pulse 170 Lightning / 15% Stun
- Guard — Power N/A

At Weather-Crown access, the body is a sturdy authored soldier rather than an Elite and remains safe for protected/nonlethal use.

**Verdict: PASS ON KIT / OPEN — EXACT PLACEMENT.**

### Blood Husk
- Lv26 / 900 HP
- Husk Rend 205 / 20% Bleed
- Ruin Spasm 195 Ruin
- Convulsive Sweep 145 AoE

At Crimson-Work access, the body fits a dangerous authored ordinary/special identity without requiring an HP or Power change.

**Verdict: PASS ON KIT / OPEN — EXACT PLACEMENT.**

### Perfected Soldier
- Lv27 / 1,080 HP
- Perfected Cut 225
- Ruin Drive 220 / 20% Staggered
- Reconstruction Burst 150 AoE
- Stabilize 180 HP, once per battle

The once-per-battle 180-HP recovery does not create meaningful stall. At late-Chapter-6 levels the body remains below Elite-duration territory unless story composition deliberately adds encounter pressure.

**Verdict: PASS ON KIT / OPEN — EXACT PLACEMENT.**

No authored-special Power changed.

---

## 5. Optional Elite — Crimson Progenitor
Current body:
- **Lv28**
- **2,700 HP**
- ATK92 / MAG104 / DEF69 / Spirit72 / SPD38
- one bar

Current direct-damage kit:
- Progenitor Rend 245 / 25% Bleed
- Crimson Ruin 250 Ruin
- Alteration Wave 180 AoE
- Warbody Crush 270 / 25% Staggered
- Adaptive Growth — Power N/A

Plausible access:
- mandatory **~Lv24–25**
- completionist **~Lv27–28**

A conservative CL6-equivalent four-character serious offense produces approximately:
- Lv24 mandatory: **~725 HP/round** before affinity, criticals, Cards, Prime use and mastery bonuses;
- Lv25: **~800 HP/round** with Torren's Chapter-6 weapon tier represented;
- Lv27 completionist: **~835 HP/round** before optional burst layers.

That places 2,700 HP at approximately:
- mandatory: **~3.5–4 serious rounds**;
- completionist: **~3–3.5 serious rounds**;

before Adaptive Growth/defensive variance.

This is exactly the intended optional-Elite band.

**Verdict: PASS / RETAIN 2,700 HP.**

No raw-stat or Power change.

---

## 6. Mandatory boss — Crownstorm Roc
Actual route anchors:
- mandatory **Lv23**
- completionist **Lv25**
- high-side **~Lv26**

Retain:
- Lv26
- **4,800 HP**
- ATK100 / MAG112 / DEF60 / Spirit66 / SPD43
- Perched Sovereign → Stormbound at 50% HP
- one continuous bar
- no HP refill / no free action / no Prime refresh on transition

Current duration certification remains appropriate:
- mandatory normal **~9–10 rounds**
- completionist **~7–8 rounds**
- high-side **~6–7 rounds**

The boss is intentionally ahead of the mandatory party in raw level. Completionist progression shortens the fight without erasing Stormbound.

**Verdict: PASS / FORMALLY VALIDATED v82.**

No raw-stat or Power change.

---

## 7. Mandatory boss — Matron Zevraya → Perfected War Mother
Actual route anchors:
- mandatory **Lv24**
- completionist fixed **Lv27**
- high-side **~Lv28**

Retain architecture:
> Blood Matron → Crimson Brood same-bar state → fresh Perfected War Mother

Blood Matron:
- Lv28 / **4,400 HP**
- four finite Reservoir targets

Perfected War Mother:
- Lv29 / **5,200 fresh HP**
- surviving Reservoir functions may carry forward
- genuine fresh body refreshes Prime availability

Current complete encounter duration remains appropriate:
- mandatory **~15–17 rounds**
- completionist **~12–14 rounds**
- high-side **~11–13 rounds**

The long duration is justified by the encounter's major story-boss role and by finite strategic choices around Reservoir destruction. Chapter 6 also introduces **Deepflow Tonic (80 MP)** to normal stock, giving the mandatory route a legal resource-recovery tier appropriate for this length.

**Verdict: PASS / FORMALLY VALIDATED v82.**

No raw-stat, Reservoir, support, or Power change.

---

## 8. Mandatory authored nonlethal — Masked Ruin Vanguard Seyrik
Actual route anchors:
- immediate post-Zevraya mandatory **Lv25**, close to Lv26
- fixed completionist **Lv27 approaching Lv28**
- high-side **~Lv28–29**

Retain:
- Lv27
- **4,000 HP**
- protected disengagement floor at **20% Max HP = 800 HP**
- party therefore removes only **3,200 effective HP**
- no Cards / Prime use / Controlled Apocalypse / Shardfang in the enemy encounter
- recognizable Ruin Vanguard coefficients retained

Current duration remains appropriate:
- mandatory **~7–8 rounds**
- completionist **~5–6 rounds**

This fight occurs immediately after the long Zevraya encounter, so the existing reduced HP and protected floor are important resource-attrition controls. The current legal MP-restoration stock and the inability of Seyrik to use the full eventual player-owned arsenal keep the sequence demanding without requiring further nerfs.

Seyrik becomes playable only **after** this encounter and the recruitment resolution.

**Verdict: PASS / FORMALLY VALIDATED v82.**

No raw-stat or Power change.

---

## 9. Regional Hunt #6 — Winterglass Titan
Current recommendation:
> **Lv32**

Current body:
- Lv32
- **10,879 HP**
- ATK101 / MAG125 / DEF90 / Spirit94 / SPD34
- Frozen Shell → Thawed Core at 50%, same bar

Chapter-6 access does **not** mean Chapter-6-route difficulty.

A mandatory chapter-clear party is approximately **Lv27**. Completionist/high-side Chapter-6 parties are approximately **Lv28–29**, still intentionally below the recommendation.

Conservative checks:
- its strongest Thawed-Core single-target hit remains below full-HP deletion even on fragile Vaelira at Lv27;
- its AoE remains substantial but recoverable;
- basic CL6-equivalent four-person throughput projects roughly **12–13 serious rounds at Lv32** before Cards, Prime, affinities, criticals and stronger mastery/ability access.

That is appropriate Regional-Hunt endurance.

Its exact within-Chapter-6 S### unlock relative to Zevraya remains unresolved, so it is **not** used to define the fixed completionist pre-boss route.

**Verdict: PASS / RETAIN Lv32 RECOMMENDATION AND 10,879 HP.**

---

## 10. Major Hunt #1 — Ashen Whitehorn
Current unlock:
> **after Chapter 6**

Current recommendation:
> **Lv33**

First-access party state:
- mandatory chapter-clear: **~Lv27**
- all normally available optional EXP before the Hunt: **~Lv29–30**

Current body:
- Lv33
- **15,600 HP**
- ATK130 / MAG94 / DEF92 / Spirit85 / SPD44
- one bar
- Last Run at 30% HP, same bar

At Lv27 early access, Ashen Whitehorn is deliberately above route level. Even Last Run's strongest physical hit remains below a healthy full-HP one-action KO on the conservative fragile-body reference, while the large HP body makes an early attempt a true endurance challenge.

At the proper Lv33 recommendation, conservative CL6-equivalent basic serious throughput is approximately **~900 HP/round before Cards/Prime/crit/affinity/mastery burst**, leaving a long Major-Hunt-scale baseline that optional systems are expected to shorten materially.

The hierarchy remains intact:
> mandatory story boss < Regional Hunt #6 < Major Hunt #1

**Verdict: PASS / RETAIN Lv33 RECOMMENDATION AND 15,600 HP.**

No Major-Hunt Power changed.

---

## 11. v82 change ledger
### Numerical changes
> **NONE**

### Power changes
> **NONE**

### Authority/status cleanup
- Chapter-6 start/middle/end level anchors made explicit.
- Seyrik explicitly excluded from the playable Chapter-6 combat roster until after his forced-disengagement encounter and recruitment resolution.
- Crownstorm Roc, Matron Zevraya → Perfected War Mother, and Masked Seyrik promoted from preliminary boss-route recertification to Chapter-6 mandatory/completionist validation.
- Weather Crown Shield Guard / Blood Husk / Perfected Soldier remain placement dependencies, not balance gaps.
- Exact ordinary formations remain a data/story-placement dependency; none were invented.
- Winterglass Titan retained as an intentionally above-route Lv32 Regional Hunt.
- Ashen Whitehorn retained as an after-Chapter-6 Lv33 Major Hunt.

---

# Final Chapter-6 verdict
> **PASS / VALIDATED WITH EXPLICIT PLACEMENT DEPENDENCIES**

Validated route anchors:
- chapter start **Lv22 mandatory**;
- Crownstorm Roc **Lv23 mandatory / Lv25 completionist**;
- Matron Zevraya **Lv24 mandatory / Lv27 completionist**;
- Masked Seyrik **Lv25 mandatory / Lv27→28 completionist**;
- chapter end **Lv27 mandatory**;
- Winterglass Titan recommendation **Lv32**;
- Ashen Whitehorn recommendation **Lv33**, after Chapter 6.

All currently defined Chapter-6 combat bodies and optional difficulty tiers pass without numerical adjustment.

The remaining Chapter-6 combat unknowns are **formation/story placement**, not missing Power or failed raw balance.

## Next frontier
> **Chapter 7 — Lv27 start → Lv32 end**, accounting for Seyrik as a newly recruited permanent character and the exact Sixfold Volition timing at chapter end.
