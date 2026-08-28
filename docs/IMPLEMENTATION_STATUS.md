# Diyse — Current Implementation Status

**Written authority checkpoint:** **v2.17 / Audit132**  
**Presentation target:** HD-2D  
**Active repository:** `zxxdjxxz-del/Diyse-Game`

## Current closure / implementation state

- Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level.
- Chapter 4 four-element S022–S026 script/dialogue-runtime synchronization is complete.
- Shared HD-2D runtime foundation remains implemented.
- **Audit132** closes Chapters 9–13 mandatory named/special raw combat stats and completes the mandatory-story raw-stat layer for all 13 chapters.
- **Audit131** closes Chapters 5–8 mandatory named/special raw combat stats.
- **Audit130** corrects Regulation Crucible Form-I HP to 2,400.
- **Audit129** closes compatible Chapters 1–4 mandatory named/special raw combat stats.
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

Status Resistance bands = 0 Normal / 5 Resistant / 10 Highly Resistant / 15 Exceptional; immunity explicit only. There is no natural Accuracy stat.

Removed systems:
- Barrier does not exist.
- Brace does not exist.
- no global Break/Stagger meter.
- Staggered is an ordinary harmful status only.
- Guard remains valid.

Bleed damages each round and again when the affected character acts; it clears only on full-HP restoration, eligible harmful-status clear, or eligible item.

Genuine fresh-HP boss transformations refresh Prime availability. Same-bar state changes do not.

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

# Mandatory raw-stat implementation targets

## Chapters 1–4 — Audit129 + Audit130

| Ch | Mandatory body | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Briarhide Stalker | 4 | 850 | 34 | 18 | 22 | 20 | 29 | 10 | 0 |
| 1 | Hollow Watch Castellan | 6 | 1,758 | 36 | 27 | 27 | 24 | 25 | 0 | 5 |
| 2 | Archive Leviathan | 9 | 2,592 | 34 | 45 | 31 | 33 | 25 | 0 | 5 |
| 2 | Rhazek — Bastion Master | 10 | 2,700 | 49 | 31 | 36 | 32 | 26 | 5 | 5 |
| 3 | First Command Warden | 14 | 3,723 | 57 | 57 | 43 | 43 | 29 | 0 | 10 |
| 4 | Elder Briarhide | 14 | 2,100 | 64 | 28 | 44 | 39 | 36 | 10 | 5 |
| 4 | Reaction Conduit | 17 | 3,100 | 50 | 72 | 47 | 52 | 32 | 5 | 5 |
| 4 | Regulation Crucible Form I | 18 | **2,400** | 54 | 73 | 51 | 53 | 28 | 0 | 10 |
| 4 | The Seventh Reaction Form II | 19 | 2,900 | 60 | 80 | 55 | 57 | 30 | 0 | 10 |

Current Ch4 climax body total = **5,300**. No chamber HP pools are invented.

## Chapters 5–8 — Audit131

| Ch | Mandatory body | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | Furnace Tyrant | 23 | 3,801 | 87 | 51 | 61 | 50 | 30 | 0 | 5 |
| 5 | Deepforge Colossus — Assembly Frame | 24 | 3,400 | 93 | 51 | 70 | 55 | 26 | 0 | 10 |
| 5 | Deepforge Colossus — Worldsmith Body | 25 | 4,000 | 101 | 62 | 73 | 60 | 29 | 0 | 10 |
| 6 | Crownstorm Roc | 26 | 5,921 | 88 | 95 | 55 | 61 | 41 | 10 | 10 |
| 6 | Masked Ruin Vanguard — Seyrik | 27 | 5,302 | 104 | 79 | 63 | 59 | 38 | 5 | 10 |
| 6 | Blood Matron | 28 | 5,283 | 74 | 104 | 65 | 74 | 38 | 5 | 10 |
| 6 | Perfected War Mother | 29 | 6,162 | 90 | 113 | 69 | 77 | 39 | 5 | 10 |
| 7 | Chainworks Behemoth | 29 | 5,135 | 109 | 57 | 77 | 59 | 32 | 0 | 5 |
| 7 | Warden of the Nameless / Revision Arbiter | 34 | 8,913 | 112 | 120 | 84 | 89 | 40 | 5 | 10 |
| 8 | Western Rift Engine | 36 | 9,775 | 86 | 133 | 97 | 89 | 33 | 0 | 10 |
| 8 | Marshal Varkesh | 38 | 7,326 | 140 | 93 | 93 | 85 | 44 | 5 | 10 |
| 8 | Rift Conqueror | 39 | 8,485 | 151 | 107 | 97 | 91 | 45 | 5 | 10 |

Deepforge total = **7,400**. Zevraya total = **11,445**. Ch8 Varkesh total = **15,811**.

## Chapters 9–13 — Audit132

| Ch | Mandatory body | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | Equal Mercy Arbiter | 40 | 10,025 | 105 | 140 | 89 | 107 | 43 | 0 | 10 |
| 9 | Commander Rhazek — Reforged Commander | 43 | 8,431 | 163 | 100 | 111 | 96 | 44 | 5 | 10 |
| 9 | Bastion Devourer | 44 | 10,462 | 175 | 131 | 107 | 104 | 46 | 0 | 10 |
| 10 | Registry Warden | 49 | 13,514 | 157 | 172 | 124 | 126 | 46 | 0 | 10 |
| 11 | Othmar Calder — Protector of Continuity | 54 | 10,133 | 137 | 193 | 118 | 134 | 50 | 5 | 10 |
| 11 | Crown-Bound Living Anchor | 55 | 13,662 | 181 | 204 | 139 | 139 | 47 | 0 | 10 |
| 11 | The Custodian | 55 | 16,017 | 177 | 190 | 144 | 146 | 48 | 0 | 10 |
| 12 | Marshal Varkesh — Final Capture | 58 | 17,106 | 226 | 148 | 144 | 131 | 55 | 5 | 10 |
| 12 | Emperor Vaelkor — Emperor of the Reforged Host | 60 | 13,648 | 223 | 209 | 155 | 150 | 54 | 5 | 10 |
| 12 | Sovereign Panoply Unbound | 61 | 16,615 | 238 | 224 | 163 | 157 | 55 | 0 | 10 |
| 13 | Last Weapon Archon | 63 | 18,424 | 236 | 220 | 160 | 160 | 56 | 0 | 15 |
| 13 | Reconstituted Entity | 63 | 15,074 | 224 | 228 | 158 | 163 | 55 | 5 | 15 |
| 13 | The Last Command | 64 | 19,367 | 247 | 247 | 168 | 168 | 58 | 5 | 15 |

Key combined body totals:
- Ch9 Rhazek = **18,893**
- Ch11 Calder/Crown Engine = **23,795**
- Ch12 Vaelkor = **30,263**
- Ch13 final boss = **34,441**

Equal Mercy Arbiter stays one bar with Mercy-Proof action tax. Registry Warden stays a technical boss and still needs exact action-kit authoring/recovery outside this raw-stat pass. Custodian stays one continuous bar with its visible 55% registration floor. Varkesh Final Capture stays one bar with beacon/capture logic. Last Weapon Archon stays one bar. Final boss remains exactly two fresh-health forms.

---

# Mandatory raw-stat closure

Mandatory named/special raw body stats are now CLOSED for all 13 chapters:
- Ch1–4 Audit129 + Audit130
- Ch5–8 Audit131
- Ch9–13 Audit132

Controlled fields: Level / HP / Attack / Magic / Defense / Spirit / Speed / Evasion / Status Resistance.

Unresolved component/subtarget HP pools are not silently invented.

---

# Equipment / Cards / Chapter 4

- 38 ordinary equipment + 36 Relics + 17 Legacies = 91 equipment pieces.
- 20 consumables.
- 24 Standard Cards.
- 12 Primes, Recovered → Awakened only.
- Chapter 4 uses exactly Fire / Ice / Lightning / Earth. Reaction Conduit replaces Elemental Hexarch.

---

# Active implementation frontier

## Optional Elite / Regional Hunt / Major Hunt raw-stat recertification

Mandatory story raw-stat certification is complete. The next balance layer is optional Elite/Hunt raw stats, using current unlock/readiness levels and fixed authored tuning.

Preserve current optional identities and form architecture. Major Hunts remain stronger than the party at readiness. Do not reintroduce Barrier, Brace, global Break/Stagger, natural Accuracy, Synthesis or other retired systems.