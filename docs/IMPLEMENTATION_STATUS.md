# Diyse — Current Implementation Status

**Written authority checkpoint:** **v2.08 / Audit123**  
**Presentation target:** HD-2D  
**Active repository:** `zxxdjxxz-del/Diyse-Game`

## Current closure / implementation state

- Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level.
- Chapter 4 four-element S022–S026 script/dialogue-runtime synchronization is complete.
- Shared HD-2D runtime foundation: IMPLEMENTED.
- **Audit123** closes class Ability MP certification, the 6,000-CEXP CL13 curve, chapter-level CEXP structure, exact 8-point Mastery schedule, restored late-game player-level anchors, and exact Ch8–13 mandatory EXP budgets.
- **Audit122** supplies exact Base Hit/Evasion and current Bleed runtime.
- **Audit121** supplies current system removals, class/Face names, 17/17 Legacy mechanics, Relic cleanup, 20-consumable economy/placement, Chapter-4 four-element reconciliation, commerce/location corrections, and Prime numeric sync.
- **Audit120** supplies compatible direct-damage and Critical rules.
- **Audit118** remains the implementation source for the closed 38/38 ordinary-equipment catalog and compatible Relic/Forge data.

The previous statements that the class Ability MP check, CEXP redo, and Mastery timing were still open are superseded.

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

Do not implement a natural Accuracy stat.

Critical:
- base 5%
- flat percentage-point bonuses
- ordinary random cap 50%
- eligible multiplier 1.5×
- hit/evasion resolves first
- Crit does not bypass Defense/Spirit.

Removed systems:
- Barrier does not exist.
- Brace does not exist.
- no global Break/Stagger meter.
- Staggered is an ordinary harmful status only.
- Guard remains valid.

Bleed:
- damages each round and again when the affected character acts;
- clears only on full-HP restoration, eligible harmful-status clear, or eligible item.

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
Current exact Base/Subclass MP tables are in Audit123 and require no further base-cost rebase.

General bands:
- routine 10–24 MP;
- premium non-Ultimate 26–40 MP;
- Ultimate 52–64 MP.

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

Synthesis is removed.

Exactly 8 active Masteries:
- 4 Core
- 4 Subclass

Eligibility:
- Core — Base CL3 / 6 / 9 / 12
- Subclass — CL3 / 5 / 7 / 11

Exact automatic Mastery Point grants:
- Lv5
- Lv10
- Lv15
- Lv20
- Sixfold Volition
- Lv40
- Lv50
- Lv60

No ninth point and no Lv70 surplus point.

Subclass Mastery 3 purchase → donor Relic access. Subclass Mastery 4 purchase → donor Legacy access. The actual obtained donor item is used; no duplicate shared artifact.

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

Late ordinary enemy bands:
- Ch8 Lv32–37
- Ch9 Lv37–42
- Ch10 Lv42–47
- Ch11 Lv47–52
- Ch12 Lv52–57
- Ch13 pre-Shelter Lv57–60
- Ch13 post-Shelter Lv60–62

Expected ordinary encounter planning centers remain 225 total; Chapter 4 remains 19. These are planning centers, not quotas.

---

# Cards / Primes

Standard Cards:
- exactly 24
- maximum 3 equipped
- reusable and MP-consuming
- current MP range 18–48
- Acuity quartet = Faultline Sight / Measured Response / Predicted Impact / Decisive Interval
- Predicted Impact = Magical/Colorless, P180, BH110, 28 MP, 30% Stun.

Prime Invocation:
- Recovered Story 50 MP
- Awakened Story 80 MP
- Awakened Major Hunt 90 MP
- manifested commands 0 additional MP

Prismatic Deluge = 90×4 = 360 listed Power per target.
Regulator Fang = 250 Power / 25% Spirit penetration.

---

# Equipment / items

Current equipment:
- 38 ordinary
- 36 Relics
- 17 native Legacies
- 91 total

Current consumables = 20.

The ordinary-equipment architecture, Legacy mechanical set, and consumable architecture are closed. Remaining item/equipment work is naming/presentation/implementation polish unless explicitly reopened.

---

# Chapter 4

Current Chapter 4 uses exactly Fire / Ice / Lightning / Earth.

Reaction Conduit replaces Elemental Hexarch. Regulation Crucible uses four chambers with two active at once. S022–S026 Markdown and matching dialogue `.tres` resources are synchronized.

---

# Remaining implementation-progress work

1. optional player EXP source-by-source re-certification;
2. Light / Standard / Heavy formation EXP;
3. exact formation CEXP allocations;
4. named/story EXP and CEXP package placement;
5. progression-dependent named-enemy/boss raw-stat recertification.
