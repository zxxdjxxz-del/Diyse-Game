# Diyse — Current Implementation Status

**Written authority checkpoint:** **v2.13 / Audit128**  
**Presentation target:** HD-2D  
**Active repository:** `zxxdjxxz-del/Diyse-Game`

## Current closure / implementation state

- Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level.
- Chapter 4 four-element S022–S026 script/dialogue-runtime synchronization is complete.
- Shared HD-2D runtime foundation remains implemented.
- **Audit128** closes exact mandatory named/story player-EXP + CEXP placement for Chapters 9–13 and completes all 13 chapters.
- **Audit127** closes exact mandatory named/story placement for Chapters 5–8.
- **Audit126** closes exact mandatory named/story placement for Chapters 1–4.
- **Audit125** closes mandatory ordinary-vs-authored EXP allocation, late formation EXP anchors, formation CEXP bands, and chapter named/story envelopes.
- **Audit124** closes optional player EXP and the pre-Last-Shelter Level-70 completionist proof.
- **Audit123** closes class Ability MP certification, the 6,000-CEXP CL13 curve, exact 8-point Mastery schedule, late player-level spine and chapter EXP budgets.
- **Audit122** closes Base Hit/Evasion and current Bleed runtime.
- **Audit121** supplies current system removals, classes/Faces, 17/17 Legacies, Relic cleanup, 20-consumable economy/placement, Chapter-4 four-element reconciliation and Prime numeric sync.

---

# Combat guardrails

Physical:
> `BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)`

Magical:
> `BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)`

Same-axis penetration cap = 75%. Spirit is magical defense. Hybrid components resolve independently.

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
- there is no natural Accuracy stat.

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

Base/Subclass cap = CL13. No permanent Subclass use before Sixfold Volition at end Ch7. Synthesis is removed.

Ability MP is CLOSED under Audit123 with no authored base-cost changes.

---

# CEXP / Mastery / player progression

CL13 = **6,000 cumulative CEXP**.

Pre-Volition Ch1–7 CEXP = **4,950**.

Post-Volition normal CEXP:
- Ch8 1,300
- Ch9 1,450
- Ch10 1,200
- Ch11 1,800
- Ch12 2,750
- Ch13 1,500 catch-up/overflow

Normal full Base + Subclass Class-Level completion occurs during Ch12, with Seyrik around end Ch12.

Automatic Mastery Points:
- Lv5
- Lv10
- Lv15
- Lv20
- Sixfold Volition
- Lv40
- Lv50
- Lv60

Player-level anchors:
- Ch7 end Lv32
- Ch8 end Lv37
- Ch9 end Lv42
- Ch10 end Lv47
- Ch11 end Lv52
- Ch12 end Lv57
- **Last Shelter Lv60**
- **normal ending Lv62**
- cap Lv70

---

# Reward/progression implementation

## Optional EXP
Pre-Last-Shelter authored optional pool = **195,000 EXP**. Broad completionist route reaches Lv70 before Last Shelter with a 16,300 EXP proof buffer. Major Hunt #6 is excluded from the cap proof.

## Mandatory formation allocation
Expected ordinary encounter center = 225 total, planning centers not quotas. Chapter 4 remains 19 expected random encounters / 5,262 ordinary EXP / 11,200 total EXP.

## Exact mandatory named/story placement
All 13 chapters are CLOSED:
- Ch1–4 — Audit126
- Ch5–8 — Audit127
- Ch9–13 — Audit128

Implementation firewall:
- optional Elites/Hunts/quests do not consume mandatory chapter pools;
- same-bar changes pay once;
- fresh-HP multi-form bosses pay one combined package after the final form;
- authored nonlethal clears can receive full progression;
- fixed authored packages are exempt from ordinary lower-level enemy EXP diminishing returns;
- no separate CEXP diminishing-return system.

### Ch12 current identity
Current Chapter 12 is **The Reforged March**: Westguard-side campaign → Blackspine → Draevensreach → Varkesh live capture → Vhalmarch Forward Hub → Vorathen → Veiled Citadel → Vaelkor. Do not place these events in Chapter 11.

### Ch13 current identity
Current Chapter 13 order:
**Deepest City → Last Weapon Archive → Last Weapon Archon → Last Shelter → Reactor Galleries → Reactor–Crest Interface → Reconstituted Entity → Crest Integration / The Last Command → Final Severance → aftermath.**

True PONR = **Last Shelter → Reactor Galleries**.

Ch13 8 ordinary-encounter planning center splits 5 pre-Shelter / 3 post-PONR. Pre-Shelter segment totals 46,300 EXP to ~Lv60; post-PONR totals 32,700 to ~Lv62.

Final boss = exactly two genuine full-HP forms: Reconstituted Entity → The Last Command. No third form.

---

# Equipment / Cards / Chapter 4

- 38 ordinary equipment + 36 Relics + 17 Legacies = 91 equipment pieces.
- 20 consumables.
- 24 Standard Cards.
- 12 Primes, Recovered → Awakened only.
- Chapter 4 uses exactly Fire / Ice / Lightning / Earth in its research/regulation framework. Live S022–S026 source and dialogue Resources are synchronized.

---

# Active implementation frontier

## Progression-dependent named-enemy / boss raw-stat recertification

Recover existing HP / ATK / MAG / DEF / Spirit / SPD / Evasion / Status Resistance for mandatory named enemies and bosses and compare against the final chapter player-level bands.

Preserve encounter mechanics, HP-bar/form architecture, fresh-form behavior, current formulas, statuses and elements. Do not reintroduce Barrier, Brace, global Break/Stagger, natural Accuracy, Synthesis or other retired systems.
