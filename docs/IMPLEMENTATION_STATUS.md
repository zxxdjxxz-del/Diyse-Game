# Diyse — Current Implementation Status

**Written authority checkpoint:** **v2.14 / Audit129**  
**Presentation target:** HD-2D  
**Active repository:** `zxxdjxxz-del/Diyse-Game`

## Current closure / implementation state

- Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level.
- Chapter 4 four-element S022–S026 script/dialogue-runtime synchronization is complete.
- Shared HD-2D runtime foundation remains implemented.
- **Audit129** closes Chapters 1–4 mandatory named/special raw combat stats.
- **Audit128** closes exact mandatory named/story player-EXP + CEXP placement for Chapters 9–13 and completes all 13 chapters.
- **Audit127** closes exact mandatory named/story placement for Chapters 5–8.
- **Audit126** closes exact mandatory named/story placement for Chapters 1–4.
- **Audit125** closes mandatory ordinary-vs-authored EXP allocation, formation CEXP bands, and chapter authored envelopes.
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

Status Resistance bands = 0 Normal / 5 Resistant / 10 Highly Resistant / 15 Exceptional; immunity explicit only.

Removed systems:
- Barrier does not exist.
- Brace does not exist.
- no global Break/Stagger meter.
- Staggered is an ordinary harmful status only.
- Guard remains valid.
- there is no natural Accuracy stat.

Bleed damages each round and again when the affected character acts; it clears only on full-HP restoration, eligible harmful-status clear, or eligible item.

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

---

# Reward/progression implementation

Pre-Last-Shelter authored optional pool = **195,000 EXP**. Major Hunt #6 is excluded from the cap proof.

Expected ordinary encounter center = **225 total**, planning centers not quotas. Chapter 4 remains 19 expected random encounters / 5,262 ordinary EXP / 11,200 total EXP.

Exact mandatory named/story placement is CLOSED:
- Ch1–4 Audit126
- Ch5–8 Audit127
- Ch9–13 Audit128

Implementation firewall:
- optional Elites/Hunts/quests do not consume mandatory chapter pools;
- same-bar changes pay once;
- fresh-HP multi-form bosses pay one combined package after final form;
- authored nonlethal clears can receive full progression;
- fixed authored packages are exempt from ordinary lower-level enemy EXP diminishing returns;
- no separate CEXP diminishing-return system.

Ch13 true PONR = **Last Shelter → Reactor Galleries**. Final boss = exactly Reconstituted Entity → The Last Command, two genuine full-HP forms, no third form.

---

# Audit129 implementation target — Chapters 1–4 raw stats

Early main-boss target = **6–9 effective combat rounds for the complete encounter**.

| Ch | Mandatory body | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Briarhide Stalker | 4 | 850 | 34 | 18 | 22 | 20 | 29 | 10 | 0 |
| 1 | Hollow Watch Castellan | 6 | 1,758 | 36 | 27 | 27 | 24 | 25 | 0 | 5 |
| 2 | Archive Leviathan | 9 | 2,592 | 34 | 45 | 31 | 33 | 25 | 0 | 5 |
| 2 | Rhazek — Bastion Master | 10 | 2,700 | 49 | 31 | 36 | 32 | 26 | 5 | 5 |
| 3 | First Command Warden | 14 | 3,723 | 57 | 57 | 43 | 43 | 29 | 0 | 10 |
| 4 | Elder Briarhide | 14 | 2,100 | 64 | 28 | 44 | 39 | 36 | 10 | 5 |
| 4 | Reaction Conduit | 17 | 3,100 | 50 | 72 | 47 | 52 | 32 | 5 | 5 |
| 4 | Regulation Crucible Form I | 18 | 2,200 | 54 | 73 | 51 | 53 | 28 | 0 | 10 |
| 4 | The Seventh Reaction Form II | 19 | 2,900 | 60 | 80 | 55 | 57 | 30 | 0 | 10 |

Implementation notes:
- Hollow Watch Castellan, Archive Leviathan, Rhazek, and First Command Warden retain their historical HP/offense/defense values.
- Hold the Junction and Ch3 S018 lawful-authority confrontations are group/formation events; do not implement fake singular boss bodies.
- Current Ch4 climax minimum body HP = **5,100**, split 2,200 Form I + fresh 2,900 Form II.
- Do not duplicate obsolete 4,901 HP across both current forms.
- Audit129 does not invent chamber subtarget HP.
- Elder Briarhide's Recovered Last Sentinel hit remains scripted nonlethal.

---

# Equipment / Cards / Chapter 4

- 38 ordinary equipment + 36 Relics + 17 Legacies = 91 equipment pieces.
- 20 consumables.
- 24 Standard Cards.
- 12 Primes, Recovered → Awakened only.
- Chapter 4 uses exactly Fire / Ice / Lightning / Earth. Reaction Conduit replaces Elemental Hexarch.
- Regulation Crucible uses four chambers with exactly two active/targetable and transforms into genuine fresh-HP **The Seventh Reaction**; no third form.

---

# Active implementation frontier

## Chapters 5–8 mandatory named-enemy / boss raw-stat recertification

Recover existing HP / ATK / MAG / DEF / Spirit / SPD / Evasion / Status Resistance for mandatory named combat in Chapters 5–8 and compare against the final player-level and boss-duration bands.

Preserve encounter mechanics, HP-bar/form architecture, fresh-form behavior, current formulas, statuses and elements. Do not reintroduce Barrier, Brace, global Break/Stagger, natural Accuracy, Synthesis or other retired systems.
