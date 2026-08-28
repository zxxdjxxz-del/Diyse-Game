# Diyse — Current Implementation Status

**Written authority checkpoint:** **v2.18 / Audit133**  
**Presentation target:** HD-2D  
**Active repository:** `zxxdjxxz-del/Diyse-Game`

## Current closure / implementation state

- Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level.
- Chapter 4 four-element S022–S026 script/dialogue-runtime synchronization is complete.
- Shared HD-2D runtime foundation remains implemented.
- **Audit133** closes numbered-chapter optional Elite raw stats: 12 current Elites, no approved Ch10 optional Elite.
- **Audit132** closes Chapters 9–13 mandatory named/special raw combat stats and completes the mandatory-story raw-stat layer for all 13 chapters.
- **Audit131** closes Chapters 5–8 mandatory named/special raw combat stats.
- **Audit130** corrects Regulation Crucible Form-I HP to 2,400.
- **Audit129** closes compatible Chapters 1–4 mandatory named/special raw combat stats.
- **Audits126–128** close exact mandatory named/story EXP+CEXP placement for all 13 chapters.
- **Audit125** closes mandatory ordinary-vs-authored EXP allocation and formation CEXP bands.
- **Audit124** closes optional player EXP and the pre-Last-Shelter Lv70 completionist proof.
- **Audit123** closes class Ability MP certification, 6,000-CEXP CL13 curve, exact 8-point Mastery schedule, player-level spine and chapter EXP budgets.
- **Audit122** closes Base Hit/Evasion and current Bleed runtime.
- **Audit121** supplies current system removals, classes/Faces, equipment/items, Chapter-4 four-element reconciliation and Prime numeric sync.

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

Status Resistance = 0 Normal / 5 Resistant / 10 Highly Resistant / 15 Exceptional; immunity explicit only. There is no natural Accuracy stat.

Removed systems:
- Barrier does not exist.
- Brace does not exist.
- no global Break/Stagger meter.
- Staggered is an ordinary harmful status.
- Guard remains valid.

Bleed damages each round and again whenever the affected character acts; it clears only on full-HP restoration, eligible harmful-status clear, or eligible item.

Genuine fresh-HP boss forms refresh Prime availability. Same-bar changes do not.

---

# Current classes / progression

| Character | Base | Subclass | Face |
|---|---|---|---|
| Cyanis | Crest Knight | Crest Arcanist | Might |
| Ilyra | Blue Warden | Vowblade | Grace |
| Torren | War Archer | Routeweaver | Acuity |
| Nimera | Cardweaver | Proofhunter | Change |
| Vaelira | Green Arcanist | Axiomblade | Elements |
| Seyrik | Ruin Vanguard | Ruin Warden | Ruin |

Base/Subclass cap = CL13. No permanent Subclass use before Sixfold Volition at end Ch7. Synthesis is removed. Ability MP is CLOSED under Audit123.

CL13 = **6,000 cumulative CEXP**. Exactly 8 automatic Mastery Points: Lv5, Lv10, Lv15, Lv20, Sixfold Volition, Lv40, Lv50, Lv60.

Player-level anchors:
- Ch1 Lv5
- Ch2 Lv9
- Ch3 Lv13
- Ch4 Lv17
- Ch5 Lv22
- Ch6 Lv27
- Ch7 Lv32
- Ch8 Lv37
- Ch9 Lv42
- Ch10 Lv47
- Ch11 Lv52
- Ch12 Lv57
- **Last Shelter Lv60**
- **normal ending Lv62**
- cap Lv70

Normal full Base + Subclass Class-Level completion occurs during Ch12, with Seyrik around end Ch12.

---

# Reward / progression implementation

Pre-Last-Shelter authored optional pool = **195,000 EXP**. Major Hunt #6 is excluded from the cap proof.

Expected ordinary encounter center = **225 total**, planning centers not quotas. Chapter 4 remains 19 expected random encounters / 5,262 ordinary EXP / 11,200 total EXP.

Exact mandatory named/story placement is CLOSED for all chapters under Audits126–128.

Implementation firewall:
- optional Elites/Hunts/quests do not consume mandatory chapter pools;
- same-bar changes pay once;
- fresh-HP multi-form bosses pay one combined package after final form;
- authored nonlethal clears can receive full progression;
- fixed authored packages are exempt from ordinary lower-level enemy EXP diminishing returns;
- no separate CEXP diminishing-return system.

Ch13 true PONR = **Last Shelter → Reactor Galleries**. Final boss = exactly Reconstituted Entity → The Last Command, two genuine full-HP forms, no third form.

---

# Current raw-stat state

Mandatory named/special raw body stats are CLOSED for all chapters:
- Ch1–4 — Audit129 + Audit130
- Ch5–8 — Audit131
- Ch9–13 — Audit132

Current key endurance totals:
- Ch4 Crucible → Seventh Reaction = 5,300
- Ch5 Deepforge = 7,400
- Ch6 Zevraya = 11,445
- Ch8 Varkesh = 15,811
- Ch9 Rhazek = 18,893
- Ch11 Calder/Crown Engine = 23,795
- Ch12 Vaelkor = 30,263
- Ch13 final Entity = 34,441

Optional Elite raw stats are CLOSED under Audit133:
- **12 current numbered-chapter optional Elites**
- **no approved Ch10 optional Elite**
- recovered HP/ATK/MAG/DEF/Spirit/SPD retained
- current Evasion/Status Resistance added
- typical duration ~2–4 serious party rounds
- tier principle = **Ordinary < Elite << Regional Hunt**
- old 60%/80% per-status tables are not restored as a second generic resistance system.

---

# Equipment / Cards / Chapter 4

- equipment = 38 ordinary + 36 Relics + 17 Legacies = 91
- consumables = 20
- Standard Cards = 24
- Primes = 12, Recovered → Awakened only
- Prime Invocation MP = 50 / 80 / 90
- Ch4 uses exactly Fire / Ice / Lightning / Earth
- Reaction Conduit replaces Elemental Hexarch
- Regulation Crucible Form I = 2,400 HP; Seventh Reaction = fresh 2,900 HP

---

# Active implementation frontier

1. **11 Regional Hunt raw-stat recertification**
2. **6 Major Hunt raw-stat recertification**

Preserve current Hunt identities, unlocks, form architecture and fixed authored tuning. Do not add dynamic scaling or retired systems.