# Diyse — Current Implementation Status

**Written authority checkpoint:** **v2.10 / Audit125**  
**Presentation target:** HD-2D  
**Active repository:** `zxxdjxxz-del/Diyse-Game`

## Current closure / implementation state

- Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level.
- Chapter 4 four-element S022–S026 script/dialogue-runtime synchronization is complete.
- Shared HD-2D runtime foundation: IMPLEMENTED.
- **Audit125** closes mandatory ordinary-vs-authored player-EXP allocation, Ch9–13 formation EXP anchors, formation CEXP bands, and chapter named/story CEXP remainder envelopes.
- **Audit124** closes optional player EXP source-by-source certification and the Level-70 pre-Last-Shelter completionist cap proof.
- **Audit123** closes class Ability MP certification, the 6,000-CEXP CL13 curve, chapter-level CEXP structure, exact 8-point Mastery schedule, restored late-game player-level anchors, and exact Ch8–13 mandatory EXP budgets.
- **Audit122** supplies exact Base Hit/Evasion and current Bleed runtime.
- **Audit121** supplies current system removals, class/Face names, 17/17 Legacy mechanics, Relic cleanup, 20-consumable economy/placement, Chapter-4 four-element reconciliation, commerce/location corrections, and Prime numeric sync.

---

# Combat guardrails

Physical:
> `BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)`

Magical:
> `BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)`

Same-axis penetration cap = 75%. Spirit is the magical-defense stat. Hybrid components resolve separately.

Base Hit / Evasion:
> `AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers`

> `EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers`

> `FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)`

Removed systems:
- Barrier does not exist.
- Brace does not exist.
- no global Break/Stagger meter.
- Staggered is an ordinary harmful status only.
- Guard remains valid.

Bleed damages each round and again when the affected character acts; it clears only on full-HP restoration, eligible harmful-status clear, or eligible item.

---

# Current classes

| Character | Base | Subclass | Face |
|---|---|---|---|
| Cyanis | Crest Knight | Crest Arcanist | Might |
| Ilyra | Blue Warden | Vowblade | Grace |
| Torren | War Archer | Routeweaver | Acuity |
| Nimera | Cardweaver | Proofhunter | Change |
| Vaelira | Green Arcanist | Axiomblade | Elements |
| Seyrik | Ruin Vanguard | Ruin Warden | Ruin |

Base/Subclass cap = CL13. No permanent Subclass use before Sixfold Volition at end Ch7.

## Ability MP — CLOSED
Audit123's exact Base/Subclass MP tables are implementation authority. General bands: routine 10–24; premium non-Ultimate 26–40; Ultimate 52–64 MP.

---

# CEXP / Mastery implementation

CL13 threshold = **6,000 cumulative CEXP**.

Pre-Volition Ch1–7 CEXP = **4,950**.

Post-Volition normal CEXP:
- Ch8 1,300
- Ch9 1,450
- Ch10 1,200
- Ch11 1,800
- Ch12 2,750
- Ch8–12 total 8,500
- Ch13 catch-up/overflow 1,500

Normal full Base + Subclass Class-Level completion occurs during Ch12, with Seyrik around end Ch12.

Synthesis is removed. Exactly 8 active Masteries: 4 Core + 4 Subclass.

Automatic Mastery Points:
- Lv5
- Lv10
- Lv15
- Lv20
- Sixfold Volition
- Lv40
- Lv50
- Lv60

No ninth point and no Lv70 surplus point.

---

# Player progression implementation

Player level cap = 70. Chapter 0 grants no levels.

Mandatory-route anchors:
- End Ch1 Lv5
- End Ch2 Lv9
- End Ch3 Lv13
- End Ch4 Lv17
- End Ch5 Lv22
- End Ch6 Lv27
- End Ch7 Lv32
- End Ch8 Lv37
- End Ch9 Lv42
- End Ch10 Lv47
- End Ch11 Lv52
- End Ch12 Lv57
- **Last Shelter Lv60**
- **End Ch13 Lv62**

Late mandatory EXP budgets:
- Ch8 38,200
- Ch9 45,500
- Ch10 53,300
- Ch11 61,500
- Ch12 70,000
- Ch13 pre-Shelter 46,300
- Ch13 post-Shelter 32,700

---

# Optional player EXP — CLOSED / Audit124

Fixed authored pre-Last-Shelter cap-proof pool = **195,000 EXP**:
- Side Quests 20,000
- Character Quests 55,000
- Regional Hunts 70,000
- Major Hunts #1–5 50,000

MH6 = 24,000 outside cap proof.

At Last Shelter:
- normal route = 415,400 / Lv60
- Lv70 = 594,100
- completionist proof = 610,400
- buffer = 16,300.

Fixed authored packages are exempt from lower-level enemy EXP diminishing returns.

---

# Formation EXP/CEXP — CLOSED / Audit125

Expected ordinary encounter center = **225 total**; Chapter 4 remains 19. These are planning centers, not quotas.

Mandatory player-EXP allocation:

| Ch | Ordinary | Named/story | Total |
|---:|---:|---:|---:|
| 1 | 855 | 745 | 1,600 |
| 2 | 2,288 | 2,512 | 4,800 |
| 3 | 3,480 | 4,520 | 8,000 |
| 4 | 5,262 | 5,938 | 11,200 |
| 5 | 8,978 | 9,822 | 18,800 |
| 6 | 10,600 | 14,300 | 24,900 |
| 7 | 14,120 | 17,180 | 31,300 |
| 8 | 18,962 | 19,238 | 38,200 |
| 9 | 25,000 | 20,500 | 45,500 |
| 10 | 31,800 | 21,500 | 53,300 |
| 11 | ~45,300 | ~16,200 | 61,500 |
| 12 | ~47,100 | ~22,900 | 70,000 |
| 13 | ~29,800 | ~49,200 | 79,000 |

Late player-EXP formation anchors:
- Ch9 — 1,245 / 1,540 / 1,920
- Ch10 — 1,700 / 2,100 / 2,500
- Ch11 — 2,100 / 2,650 / 3,100
- Ch12 — **2,100 / 2,600 / 3,150**
- Ch13 — 3,000 / 3,700 / 4,500

Ch12's player-EXP formation anchors are rebased from the obsolete 83,000-EXP Ch12 model to preserve the intended ordinary-vs-authored reward share under the current 70,000 chapter budget.

Formation CEXP bands:
- Ch1 8 / 10 / 12
- Ch2 10 / 12 / 15
- Ch3 12 / 15 / 18
- Ch4 14 / 18 / 22
- Ch5 17 / 21 / 26
- Ch6 20 / 25 / 31
- Ch7 23 / 29 / 36
- Ch8 26 / 33 / 41
- Ch9 30 / 38 / 47
- Ch10 32 / 40 / 50
- Ch11 36 / 45 / 56
- Ch12 42 / 53 / 66
- Ch13 46 / 58 / 72

Named/story CEXP remainder centers:
- Ch1 ~172
- Ch2 ~220
- Ch3 ~264
- Ch4 ~304
- Ch5 ~367
- Ch6 ~461
- Ch7 ~631
- Ch8 ~687
- Ch9 ~837
- Ch10 ~586
- Ch11 ~1,015
- Ch12 **~1,786**
- Ch13 ~1,032

No CEXP diminishing-return system is created.

---

# Cards / Primes

Standard Cards: exactly 24, max 3 equipped, reusable and MP-consuming. Predicted Impact = P180, Magical/Colorless, BH110, 28 MP, 30% Stun.

Prime Invocation = 50 / 80 / 90 MP. Prismatic Deluge = 90×4 = 360. Regulator Fang = 250 Power / 25% Spirit penetration.

---

# Equipment / items

Current equipment = 38 ordinary + 36 Relics + 17 native Legacies = 91 total. Current consumables = 20.

Ordinary equipment architecture, Legacy mechanics, Relic cleanup, consumable architecture, pricing and current placement are closed.

---

# Chapter 4

Current Chapter 4 uses exactly Fire / Ice / Lightning / Earth. Reaction Conduit replaces Elemental Hexarch. Regulation Crucible uses four chambers with two active at once. S022–S026 Markdown and matching dialogue `.tres` resources are synchronized.

Protected progression allocation:
- 19 expected ordinary encounters
- ordinary EXP 5,262
- total mandatory EXP 11,200.

---

# Remaining implementation-progress work

1. exact named/story player-EXP package placement by encounter/milestone;
2. exact named/story CEXP package placement by encounter/milestone;
3. progression-dependent named-enemy/boss raw-stat recertification.
