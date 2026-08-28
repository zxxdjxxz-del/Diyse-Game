# Diyse — Active Engineering Canon Guardrails

This file is the implementation-facing authority index. It does not replace the canon audits. Compatible older locks remain active where not superseded; later explicit approved corrections win.

## Current whole-project authority

**Diyse: HD-2D JRPG Clean Active Complete Master Canon v2.17 / Audit132 — Chapters 9–13 Mandatory Named Raw-Stat Recertification Lock**  
**Date:** August 27, 2026

Newest authority chain:
- **v2.17 / Audit132** — Ch9–13 mandatory named/special raw combat stats; completes all 13 chapters' mandatory-story raw-stat recertification.
- **v2.16 / Audit131** — Ch5–8 mandatory named/special raw combat stats; Deepforge Colossus converted to current two-form fresh-health architecture.
- **v2.15 / Audit130** — Regulation Crucible Form-I HP corrected to **2,400**; current Ch4 climax body total **5,300**.
- **v2.14 / Audit129** — Ch1–4 mandatory named/special raw combat stats.
- **v2.13 / Audit128** — exact mandatory named/story player-EXP + CEXP placement Ch9–13; completes all 13 chapters.
- **v2.12 / Audit127** — exact mandatory named/story placement Ch5–8.
- **v2.11 / Audit126** — exact mandatory named/story placement Ch1–4.
- **v2.10 / Audit125** — mandatory formation EXP/CEXP allocation and chapter authored envelopes.
- **v2.09 / Audit124** — authored optional EXP and Lv70 completionist cap proof.
- **v2.08 / Audit123** — class Ability MP certification, 6,000-CEXP CL13 curve, exact 8-point Mastery schedule, player-level spine.
- **v2.07 / Audit122** — Base Hit/Evasion and current Bleed lifecycle.
- **v2.06 / Audit121** — current classes/Faces, removed systems, equipment/items, Chapter-4 four-element rework.
- compatible Audit120–Audit113 remain active where not superseded.

Primary current domain files:
- `docs/canon/AUDIT132_CHAPTERS_9_13_MANDATORY_NAMED_RAW_STAT_RECERTIFICATION_LOCK.md`
- `docs/canon/AUDIT131_CHAPTERS_5_8_MANDATORY_NAMED_RAW_STAT_RECERTIFICATION_LOCK.md`
- `docs/canon/AUDIT130_REGULATION_CRUCIBLE_FORM_I_HP_CORRECTION_LOCK.md`
- `docs/canon/AUDIT129_CHAPTERS_1_4_MANDATORY_NAMED_RAW_STAT_RECERTIFICATION_LOCK.md`
- `docs/canon/AUDIT128_CHAPTERS_9_13_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
- `docs/canon/AUDIT127_CHAPTERS_5_8_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
- `docs/canon/AUDIT126_CHAPTERS_1_4_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
- `docs/canon/AUDIT125_MANDATORY_FORMATION_EXP_CEXP_ALLOCATION_LOCK.md`
- `docs/canon/AUDIT124_OPTIONAL_EXP_AND_LEVEL_70_COMPLETIONIST_CAP_LOCK.md`
- `docs/canon/AUDIT123_CLASS_MP_CEXP_MASTERY_AND_LATE_GAME_PROGRESSION_LOCK.md`
- `docs/canon/AUDIT122_BASE_HIT_EVASION_AND_BLEED_RUNTIME_LOCK.md`
- `docs/canon/AUDIT121_CURRENT_SYSTEMS_ITEM_EQUIPMENT_AND_PROGRESSION_RECONCILIATION_LOCK.md`

Historical trackers/audits are provenance, not automatic current authority.

---

# Universal combat firewall

Physical direct damage:
> `BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)`

Magical direct damage:
> `BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)`

Hybrid components resolve independently. Same-axis penetration cap = **75%**. **Spirit** is magical defense. There is no universal random damage variance or hidden universal AoE penalty.

Base Hit / Evasion:
> `AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers`

> `EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers`

> `FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)`

There is no natural Accuracy stat.

Critical:
- base 5%;
- flat percentage-point bonuses;
- ordinary random cap 50%;
- eligible multiplier 1.5×;
- Crit does not bypass Defense/Spirit.

Status Resistance numeric bands:
- 0 Normal
- 5 Resistant
- 10 Highly Resistant
- 15 Exceptional
- immunity only when explicitly authored.

Removed systems:
- **Barrier does not exist.**
- **Brace does not exist.**
- no global Break/Stagger meter.
- Staggered is an ordinary harmful status only.
- Guard remains valid.

Bleed damages each round and again when the affected character acts. It clears only on full-HP restoration, eligible harmful-status clear, or eligible item.

Genuine fresh-HP boss transformations refresh Prime availability under the current global Prime rule. Same-bar state changes do not.

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

Base/Subclass cap = CL13. No permanent Subclass use before end-Ch7 Sixfold Volition. Synthesis is removed. Class Ability MP is closed under Audit123.

CL13 cumulative CEXP = **6,000**. Base/Subclass CEXP are separate; selected class receives 100%, unselected class 0, and CEXP sent to a capped selected class is lost.

Exact automatic Mastery Points:
1. Lv5
2. Lv10
3. Lv15
4. Lv20
5. Sixfold Volition
6. Lv40
7. Lv50
8. Lv60

Player cap = 70. Chapter 0 grants no levels.

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

Class Levels complete during Ch12; Seyrik is the limiting normal-route case around end Ch12. Lv62–70 remains optional/completionist headroom.

---

# EXP / reward firewalls

Audit124 fixed authored pre-Last-Shelter optional pool = **195,000 EXP**. Major Hunt #6 = 24,000 EXP and is excluded from the cap proof.

Audit125 expected ordinary encounter center = **225 total**, planning centers not quotas. Chapter 4 remains 19 expected random encounters / 5,262 ordinary EXP / 11,200 total mandatory EXP.

Exact mandatory named/story placement is closed for all chapters:
- Ch1–4 — Audit126
- Ch5–8 — Audit127
- Ch9–13 — Audit128

Optional Elites/Hunts/quests do not consume mandatory pools. Same-bar changes pay once. Fresh-HP multi-form bosses pay one combined reward after final-form clear. Fixed authored packages are exempt from ordinary lower-level enemy EXP diminishing returns. No separate CEXP diminishing-return system exists.

Ch13 true PONR = **Last Shelter → Reactor Galleries**. Normal route reaches ~Lv60 at Last Shelter and ~Lv62 at ending. Final boss remains exactly **Reconstituted Entity → The Last Command**, two genuine full-health forms, no third form.

---

# Mandatory named raw-stat firewall — Chapters 1–4

Audit129 controls broadly; Audit130 narrowly supersedes Regulation Crucible Form-I HP.

| Ch | Mandatory named body | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Briarhide Stalker | 4 | 850 | 34 | 18 | 22 | 20 | 29 | 10 | 0 |
| 1 | Hollow Watch Castellan | 6 | 1,758 | 36 | 27 | 27 | 24 | 25 | 0 | 5 |
| 2 | Archive Leviathan | 9 | 2,592 | 34 | 45 | 31 | 33 | 25 | 0 | 5 |
| 2 | Rhazek — Bastion Master | 10 | 2,700 | 49 | 31 | 36 | 32 | 26 | 5 | 5 |
| 3 | First Command Warden | 14 | 3,723 | 57 | 57 | 43 | 43 | 29 | 0 | 10 |
| 4 | Elder Briarhide | 14 | 2,100 | 64 | 28 | 44 | 39 | 36 | 10 | 5 |
| 4 | Reaction Conduit | 17 | 3,100 | 50 | 72 | 47 | 52 | 32 | 5 | 5 |
| 4 | Regulation Crucible — Form I | 18 | **2,400** | 54 | 73 | 51 | 53 | 28 | 0 | 10 |
| 4 | The Seventh Reaction — Form II | 19 | 2,900 | 60 | 80 | 55 | 57 | 30 | 0 | 10 |

Current Ch4 two-form body total = **5,300 HP**. Audit129/130 do not invent chamber HP pools. Hold the Junction and Ch3 S018 lawful-authority confrontations are group/formation events, not fake singular bodies.

---

# Mandatory named raw-stat firewall — Chapters 5–8

| Ch | Mandatory named body | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | Furnace Tyrant | 23 | 3,801 | 87 | 51 | 61 | 50 | 30 | 0 | 5 |
| 5 | Deepforge Colossus — Assembly Frame | 24 | **3,400** | 93 | 51 | 70 | 55 | 26 | 0 | 10 |
| 5 | Deepforge Colossus — Worldsmith Body | 25 | **4,000** | 101 | 62 | 73 | 60 | 29 | 0 | 10 |
| 6 | Crownstorm Roc | 26 | 5,921 | 88 | 95 | 55 | 61 | 41 | 10 | 10 |
| 6 | Masked Ruin Vanguard — Seyrik | 27 | 5,302 | 104 | 79 | 63 | 59 | 38 | 5 | 10 |
| 6 | Matron Zevraya — Blood Matron | 28 | 5,283 | 74 | 104 | 65 | 74 | 38 | 5 | 10 |
| 6 | Perfected War Mother | 29 | 6,162 | 90 | 113 | 69 | 77 | 39 | 5 | 10 |
| 7 | Chainworks Behemoth | 29 | 5,135 | 109 | 57 | 77 | 59 | 32 | 0 | 5 |
| 7 | Warden of the Nameless / Revision Arbiter | 34 | 8,913 | 112 | 120 | 84 | 89 | 40 | 5 | 10 |
| 8 | Western Rift Engine | 36 | 9,775 | 86 | 133 | 97 | 89 | 33 | 0 | 10 |
| 8 | Marshal Varkesh | 38 | 7,326 | 140 | 93 | 93 | 85 | 44 | 5 | 10 |
| 8 | Rift Conqueror | 39 | 8,485 | 151 | 107 | 97 | 91 | 45 | 5 | 10 |

Deepforge Colossus current minimum body total = **7,400 HP**. Form-I Guard Press / Repair Arm / Command Loom remain targetable functions; no HP pools are invented by Audit131. Zevraya total = **11,445**. Varkesh total = **15,811**.

---

# Mandatory named raw-stat firewall — Chapters 9–13

Audit132 retains all recovered late-game HP/ATK/MAG/DEF/Spirit/SPD values and adds current EVA/SR authoring.

| Ch | Mandatory named body | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
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

Key endurance totals:
- Rhazek → Bastion Devourer = **18,893**
- Calder → Crown-Bound Living Anchor = **23,795**
- Vaelkor → Sovereign Panoply = **30,263**
- Reconstituted Entity → The Last Command = **34,441**

Equal Mercy Arbiter stays one bar with its Mercy-Proof action tax. Registry Warden remains a technical boss; Audit132 does not fabricate a missing move kit. Custodian stays one bar with the visible 55% registration floor. Varkesh Final Capture stays one bar with Retreat Beacon/capture architecture. Last Weapon Archon stays one bar. Exceptional SR15 on the Archon/Entity/Last Command is not immunity.

All genuine fresh-HP transitions use the current Prime-refresh rule. Same-bar changes do not.

---

# Full mandatory-story raw-stat closure

All 13 chapters' mandatory named/special raw body stats are now recertified:
- Ch1–4 — Audit129 + Audit130
- Ch5–8 — Audit131
- Ch9–13 — Audit132

Controlled fields: Level, HP, Attack, Magic, Defense, Spirit, Speed, Evasion, Status Resistance.

Do not fabricate unresolved support-component/subtarget HP merely to complete a table.

---

# Equipment / Cards / Primes / Chapter 4

Equipment catalog remains 38 ordinary + 36 Relics + 17 Legacies = **91**. Consumables = **20**. Currency = Auren.

Exactly 24 Standard Cards, max 3 equipped. Exactly 12 Primes, Recovered → Awakened only. Invocation MP = 50 / 80 / 90.

Chapter 4 uses exactly Fire / Ice / Lightning / Earth. Wind and Water are not research/regulation elements. Reaction Conduit replaces Elemental Hexarch.

---

# Active frontier

## Optional Elite / Regional Hunt / Major Hunt raw-stat recertification

Mandatory story raw-stat certification is complete. Next, recover optional Elite/Hunt raw-stat lines and compare them against their current unlock/readiness bands without dynamic scaling.

Preserve current optional-content identities and form architecture. Major Hunts remain stronger than player readiness. Do not add Barrier, Brace, global Break/Stagger, natural Accuracy, Synthesis, or other retired systems.