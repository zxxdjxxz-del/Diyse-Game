# Diyse — Active Engineering Canon Guardrails

This file is the implementation-facing authority index. It does not replace the canon audits. Compatible older locks remain active where not superseded; later explicit approved corrections win.

## Current whole-project authority

**Diyse: HD-2D JRPG Clean Active Complete Master Canon v2.19 / Audit134 — Regional Hunt Raw-Stat Recertification Lock**  
**Date:** August 27, 2026

Newest authority chain:
- **v2.19 / Audit134** — all 11 Regional-Hunt raw stats and recommended levels; Throne of Emperor Vaelkor current two-form raw split.
- **v2.18 / Audit133** — numbered-chapter optional Elite raw stats; 12 current Elites; no current Ch10 optional Elite.
- **v2.17 / Audit132** — Ch9–13 mandatory named/special raw combat stats; completes mandatory-story raw-stat recertification.
- **v2.16 / Audit131** — Ch5–8 mandatory named/special raw combat stats; Deepforge Colossus current two-form conversion.
- **v2.15 / Audit130** — Regulation Crucible Form-I HP = **2,400**; Ch4 climax body total = **5,300**.
- **v2.14 / Audit129** — compatible Ch1–4 mandatory named/special raw combat stats.
- **v2.13 / Audit128** — exact mandatory named/story EXP+CEXP placement Ch9–13.
- **v2.12 / Audit127** — exact mandatory named/story placement Ch5–8.
- **v2.11 / Audit126** — exact mandatory named/story placement Ch1–4.
- **v2.10 / Audit125** — mandatory formation EXP/CEXP allocation.
- **v2.09 / Audit124** — optional player EXP + pre-Last-Shelter Lv70 cap proof.
- **v2.08 / Audit123** — class Ability MP certification, CL13 CEXP curve, Mastery schedule, player-level spine.
- **v2.07 / Audit122** — Base Hit/Evasion and current Bleed lifecycle.
- **v2.06 / Audit121** — current classes/Faces, removed systems, equipment/items, Ch4 four-element reconciliation.
- compatible Audit120–Audit113 remain active where not superseded.

Primary newest files:
- `docs/canon/AUDIT134_REGIONAL_HUNT_RAW_STAT_RECERTIFICATION_LOCK.md`
- `docs/canon/AUDIT133_OPTIONAL_ELITE_RAW_STAT_RECERTIFICATION_LOCK.md`
- `docs/canon/AUDIT132_CHAPTERS_9_13_MANDATORY_NAMED_RAW_STAT_RECERTIFICATION_LOCK.md`
- `docs/canon/AUDIT131_CHAPTERS_5_8_MANDATORY_NAMED_RAW_STAT_RECERTIFICATION_LOCK.md`
- `docs/canon/AUDIT130_REGULATION_CRUCIBLE_FORM_I_HP_CORRECTION_LOCK.md`
- `docs/canon/AUDIT129_CHAPTERS_1_4_MANDATORY_NAMED_RAW_STAT_RECERTIFICATION_LOCK.md`
- `docs/canon/AUDIT128_CHAPTERS_9_13_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
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

Hybrid components resolve independently. Same-axis penetration cap = **75%**. **Spirit** is magical defense. No universal random damage variance or hidden universal AoE penalty.

Base Hit / Evasion:
> `AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers`

> `EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers`

> `FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)`

There is no natural Accuracy stat.

Status Resistance:
- 0 Normal
- 5 Resistant
- 10 Highly Resistant
- 15 Exceptional
- immunity explicit only.

Removed systems:
- Barrier does not exist.
- Brace does not exist.
- no global Break/Stagger meter.
- Staggered is an ordinary harmful status only.
- Guard remains valid.

Bleed damages each round and whenever the affected character acts; it clears only by full-HP restoration, eligible harmful-status clear, or eligible item.

Genuine fresh-HP boss transformations refresh Prime availability. Same-bar state changes do not.

---

# Classes / progression

| Character | Base | Subclass | Face |
|---|---|---|---|
| Cyanis | Crest Knight | Crest Arcanist | Might |
| Ilyra | Blue Warden | Vowblade | Grace |
| Torren | War Archer | Routeweaver | Acuity |
| Nimera | Cardweaver | Proofhunter | Change |
| Vaelira | Green Arcanist | Axiomblade | Elements |
| Seyrik | Ruin Vanguard | Ruin Warden | Ruin |

Base/Subclass cap = CL13. No Subclass use before end-Ch7 Sixfold Volition. Synthesis is removed. Class Ability MP certification is **CLOSED** under Audit123.

CL13 cumulative CEXP = **6,000**. Base/Subclass CEXP are separate; selected class receives 100%, unselected receives 0, and CEXP sent to a capped selected class is lost.

Exactly 8 automatic Mastery Points: Lv5, Lv10, Lv15, Lv20, Sixfold Volition, Lv40, Lv50, Lv60.

Player cap = 70. Chapter 0 grants no levels.

Mandatory-route anchors:
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
- **End Ch13 Lv62**

Class Levels complete during Ch12; Seyrik is the limiting normal-route case near end Ch12. Lv62–70 remains optional/completionist headroom.

---

# EXP / reward firewall

Audit124 fixed authored pre-Last-Shelter optional pool = **195,000 EXP**. Major Hunt #6 = 24,000 EXP and is excluded from the cap proof.

Audit125 expected ordinary encounter center = **225**, planning centers not quotas. Chapter 4 remains 19 expected random encounters / 5,262 ordinary EXP / 11,200 total mandatory EXP.

Exact mandatory named/story placement is closed under Audits126–128.

Optional Elites/Hunts/quests do not consume mandatory chapter pools. Same-bar changes pay once. Fresh-HP multi-form bosses pay one combined reward after final-form clear. Fixed authored packages are exempt from ordinary lower-level enemy EXP diminishing returns. No separate CEXP diminishing-return system exists.

Ch13 true PONR = **Last Shelter → Reactor Galleries**. Normal route reaches ~Lv60 at Last Shelter and ~Lv62 at ending. Final boss remains exactly **Reconstituted Entity → The Last Command**, two genuine full-HP forms, no third form.

---

# Mandatory raw-stat closure

Controlling chain:
- Ch1–4 — Audit129 + Audit130
- Ch5–8 — Audit131
- Ch9–13 — Audit132

All 13 chapters' mandatory named/special raw body stats are recertified for Level, HP, Attack, Magic, Defense, Spirit, Speed, Evasion, and Status Resistance.

Key endurance totals:
- Ch4 Regulation Crucible → Seventh Reaction = **5,300**
- Ch5 Deepforge Colossus = **7,400**
- Ch6 Zevraya → Perfected War Mother = **11,445**
- Ch8 Varkesh → Rift Conqueror = **15,811**
- Ch9 Rhazek → Bastion Devourer = **18,893**
- Ch11 Calder → Crown-Bound Living Anchor = **23,795**
- Ch12 Vaelkor → Sovereign Panoply = **30,263**
- Ch13 Reconstituted Entity → The Last Command = **34,441**

Do not fabricate unresolved chamber/assembly/support-object HP merely to complete a table.

---

# Optional Elite raw-stat firewall — Audit133

There are **12 current numbered-chapter optional Elites**. **Current Chapter 10 has no approved optional Elite.** Chapter 0's Ruin Vanguard Pursuer remains structural/tutorial and is outside this table.

Typical optional-Elite duration = **2–4 serious party rounds**. A materially overlevelled party should be able to dismantle an old Elite quickly.

Audit133 retains recovered Elite HP/ATK/MAG/DEF/Spirit/SPD values and adds current EVA/SR. It does not restore older 60%/80% per-status tables as a second generic resistance resolver.

Tier principle:
> **Ordinary < Elite << Regional Hunt**

---

# Regional Hunt raw-stat firewall — Audit134

Regional Hunt recommended levels are **preparedness targets, not access gates**. Fixed tuning remains active; returning later is intentional.

| # | Hunt | Rec. Lv | HP / architecture |
|---:|---|---:|---|
| 1 | Cistern Devourer | 7 | **2,706** one bar |
| 2 | Transfer Executioner | 11 | **3,760** one bar |
| 3 | Archive Judgment Engine | 15 | **4,928** one bar |
| 4 | Crown Prototype | 20 | **6,503** one bar |
| 5 | Whitehorn Ravager | 26 | **8,678** one bar |
| 6 | Winterglass Titan | 32 | **10,879** one bar |
| 7 | Rift Gate Colossus | 38 | **13,276** one bar |
| 8 | Rift Siege Beast | 44 | **15,875** one bar |
| 9 | Mercyfallen Behemoth | 50 | **18,882** one bar |
| 10 | Authority Remnant | 56 | **21,913** one bar |
| 11 | Throne of Emperor Vaelkor | 61–62 | **11,800 Sealed + fresh 14,200 Walking = 26,000** |

Hunts #1–10 retain recovered HP/ATK/MAG/DEF/Spirit/SPD values under Audit134 and receive current EVA/SR authoring.

Throne of Emperor Vaelkor:
- Sealed Throne — Lv61, 11,800 HP, 228 ATK, 234 MAG, 172 DEF, 168 Spirit, 50 SPD, EVA0, SR10;
- Walking Throne — Lv62, 14,200 HP, 240 ATK, 221 MAG, 166 DEF, 159 Spirit, 58 SPD, EVA0, SR10;
- genuine fresh-HP transition refreshes Prime availability;
- Authority/Renewal Attendant functions remain current;
- no Attendant HP is invented by Audit134;
- no third form.

Current tier principle:
> **Ordinary < Elite < mandatory story boss < Regional Hunt < Major Hunt**

---

# Equipment / Cards / Primes / Chapter 4

Current equipment catalog = 38 ordinary + 36 Relics + 17 Legacies = **91**. Consumables = **20**. Currency = Auren.

Exactly 24 Standard Cards, max 3 equipped. Exactly 12 Primes, Recovered → Awakened only. Invocation MP = 50 / 80 / 90.

Chapter 4 uses exactly Fire / Ice / Lightning / Earth. Wind and Water are not research/regulation elements. Reaction Conduit replaces Elemental Hexarch. Regulation Crucible uses four chambers with exactly two active/targetable and transforms into genuine fresh-HP **The Seventh Reaction**; no third form.

---

# Active frontier

## **6 Major Hunt raw-stat recertification**

Preserve Major-Hunt identities, unlocks, Prime rewards, form architecture, fixed authored tuning, and no dynamic scaling. Major Hunts remain above Regional Hunts in total challenge and mechanic density.