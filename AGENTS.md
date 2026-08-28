# AGENTS.md — Diyse Engineering Contract

This file governs AI-assisted engineering work in this repository.

## Read first

Before changing gameplay code or production content, read:
1. `docs/ACTIVE_CANON.md`
2. `docs/IMPLEMENTATION_STATUS.md`
3. `docs/chapters/README.md`
4. the relevant current chapter file under `docs/chapters/`
5. the latest controlling canon audit for the subject
6. `docs/PRESENTATION_RULES.md`
7. the relevant subsystem document
8. dialogue authoring files before dialogue Resource work

If a task conflicts with these files or a newer explicit user instruction, stop and surface the conflict. Do not silently reinterpret canon.

Historical audits and cumulative trackers are provenance, not automatic current authority.

---

# Current authority state

Whole-project written authority:

> **Diyse v2.17 / Audit132**

Newest chain:
- `docs/canon/AUDIT132_CHAPTERS_9_13_MANDATORY_NAMED_RAW_STAT_RECERTIFICATION_LOCK.md` — Ch9–13 mandatory named/special raw stats; completes mandatory story raw-stat recertification.
- `docs/canon/AUDIT131_CHAPTERS_5_8_MANDATORY_NAMED_RAW_STAT_RECERTIFICATION_LOCK.md` — Ch5–8 mandatory named/special raw stats.
- `docs/canon/AUDIT130_REGULATION_CRUCIBLE_FORM_I_HP_CORRECTION_LOCK.md` — Regulation Crucible Form-I HP = 2,400.
- `docs/canon/AUDIT129_CHAPTERS_1_4_MANDATORY_NAMED_RAW_STAT_RECERTIFICATION_LOCK.md` — Ch1–4 raw stats except Audit130 correction.
- `docs/canon/AUDIT128_CHAPTERS_9_13_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
- `docs/canon/AUDIT127_CHAPTERS_5_8_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
- `docs/canon/AUDIT126_CHAPTERS_1_4_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
- `docs/canon/AUDIT125_MANDATORY_FORMATION_EXP_CEXP_ALLOCATION_LOCK.md`
- `docs/canon/AUDIT124_OPTIONAL_EXP_AND_LEVEL_70_COMPLETIONIST_CAP_LOCK.md`
- `docs/canon/AUDIT123_CLASS_MP_CEXP_MASTERY_AND_LATE_GAME_PROGRESSION_LOCK.md`
- `docs/canon/AUDIT122_BASE_HIT_EVASION_AND_BLEED_RUNTIME_LOCK.md`
- `docs/canon/AUDIT121_CURRENT_SYSTEMS_ITEM_EQUIPMENT_AND_PROGRESSION_RECONCILIATION_LOCK.md`
- compatible older Audit120–Audit113 remain active where not superseded.

Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level. Chapter 4's four-element script/runtime state controls. HD-2D is the sole active presentation target.

---

# Combat firewall

Physical:
> `BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)`

Magical:
> `BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)`

- same-axis penetration cap 75%;
- Spirit is magical defense;
- Hybrid components resolve independently;
- no universal random damage variance;
- no hidden universal AoE penalty.

Base Hit / Evasion:
> `AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers`

> `EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers`

> `FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)`

There is no natural Accuracy stat.

Status Resistance bands:
- 0 Normal
- 5 Resistant
- 10 Highly Resistant
- 15 Exceptional
- immunity explicit only.

Critical:
- base 5%; flat pp bonuses; ordinary random cap 50%; eligible multiplier 1.5×; Crit does not bypass Defense/Spirit.

Removed systems:
- **Barrier does not exist.**
- **Brace does not exist.**
- no global Break/Stagger meter.
- Staggered is an ordinary harmful status only.
- Guard remains valid.

Bleed damages each round and again when the affected character acts. It clears only on full-HP restoration, eligible harmful-status clear, or eligible item.

Genuine fresh-HP boss transformations refresh Prime availability. Same-bar state changes do not.

---

# Current classes / Mastery

- Cyanis — Crest Knight / Crest Arcanist — Might
- Ilyra — Blue Warden / Vowblade — Grace
- Torren — War Archer / Routeweaver — Acuity
- Nimera — Cardweaver / Proofhunter — Change
- Vaelira — Green Arcanist / Axiomblade — Elements
- Seyrik — Ruin Vanguard / Ruin Warden — Ruin

Base/Subclass cap = CL13. No permanent Subclass use before Sixfold Volition at end Ch7. Synthesis is removed. Audit123 class Ability MP tables are closed.

Exactly 8 automatic Mastery Points: Lv5, Lv10, Lv15, Lv20, Sixfold Volition, Lv40, Lv50, Lv60.

Eligibility:
- Core — Base CL3 / 6 / 9 / 12
- Subclass — CL3 / 5 / 7 / 11

Subclass Mastery 3 grants donor Relic access; Subclass Mastery 4 grants donor Legacy access. Equip the actual obtained donor item; no duplicate artifact.

---

# CEXP / player progression firewall

CL13 cumulative threshold = **6,000 CEXP**. Base and Subclass CEXP are separate. Selected class gets 100%; unselected class gets 0. CEXP sent to a capped class is lost.

Normal full Base + Subclass Class-Level completion occurs during Ch12, with Seyrik around end Ch12.

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

Do not restore the rejected Lv62-at-end-Ch12 model.

---

# Progression / reward firewall

Audit124 fixed authored pre-Last-Shelter optional pool = **195,000 EXP**. Major Hunt #6 is outside the cap proof.

Audit125 expected ordinary encounter center = **225**, planning centers not quotas. Chapter 4 remains 19 expected random encounters / 5,262 ordinary EXP / 11,200 total mandatory EXP.

Exact mandatory named/story placement is closed:
- Ch1–4 Audit126
- Ch5–8 Audit127
- Ch9–13 Audit128

Optional Elites/Hunts/quests do not consume mandatory chapter reward pools. Same-bar changes pay once. Fresh-HP multi-form bosses pay one combined package after final-form clear. Fixed authored packages are exempt from ordinary lower-level enemy EXP diminishing returns. No CEXP diminishing-return subsystem exists.

Late chapter identity:
- Ch11 = Crown Engine / Calder / Custodian / Truth.
- Ch12 = Reforged March: Westguard → Blackspine → Draevensreach → Varkesh capture → Vhalmarch → Vorathen → Veiled Citadel → Vaelkor.
- Ch13 = Deepest City → Last Weapon Archive → Last Weapon Archon → Last Shelter → Reactor Galleries → Reactor–Crest Interface → Reconstituted Entity → The Last Command → Final Severance.

True final PONR = **Last Shelter → Reactor Galleries**. Normal ending ~Lv62.

---

# Current mandatory named raw-stat firewall

## Ch1–4 — Audit129 + Audit130

| Ch | Body | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
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

Regulation Crucible current minimum body total = **5,300**. Hold the Junction and Ch3 S018 confrontations are group/formation events; do not create fake singular bodies. Audit129/130 do not invent chamber HP pools.

## Ch5–8 — Audit131

| Ch | Body | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | Furnace Tyrant | 23 | 3,801 | 87 | 51 | 61 | 50 | 30 | 0 | 5 |
| 5 | Assembly Frame | 24 | **3,400** | 93 | 51 | 70 | 55 | 26 | 0 | 10 |
| 5 | Worldsmith Body | 25 | **4,000** | 101 | 62 | 73 | 60 | 29 | 0 | 10 |
| 6 | Crownstorm Roc | 26 | 5,921 | 88 | 95 | 55 | 61 | 41 | 10 | 10 |
| 6 | Masked Ruin Vanguard — Seyrik | 27 | 5,302 | 104 | 79 | 63 | 59 | 38 | 5 | 10 |
| 6 | Blood Matron | 28 | 5,283 | 74 | 104 | 65 | 74 | 38 | 5 | 10 |
| 6 | Perfected War Mother | 29 | 6,162 | 90 | 113 | 69 | 77 | 39 | 5 | 10 |
| 7 | Chainworks Behemoth | 29 | 5,135 | 109 | 57 | 77 | 59 | 32 | 0 | 5 |
| 7 | Revision Arbiter | 34 | 8,913 | 112 | 120 | 84 | 89 | 40 | 5 | 10 |
| 8 | Western Rift Engine | 36 | 9,775 | 86 | 133 | 97 | 89 | 33 | 0 | 10 |
| 8 | Marshal Varkesh | 38 | 7,326 | 140 | 93 | 93 | 85 | 44 | 5 | 10 |
| 8 | Rift Conqueror | 39 | 8,485 | 151 | 107 | 97 | 91 | 45 | 5 | 10 |

Deepforge Colossus = **7,400 minimum body HP**. Zevraya two-form total = **11,445**. Varkesh two-form total = **15,811**.

## Ch9–13 — Audit132

| Ch | Body | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
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

Key totals:
- Ch9 Rhazek = **18,893**
- Ch11 Calder/Crown Engine = **23,795**
- Ch12 Vaelkor = **30,263**
- Ch13 final Entity encounter = **34,441**

Equal Mercy Arbiter and Custodian remain mechanic/action-tax one-bar encounters. Registry Warden raw stats are closed but its exact action kit remains a separate recovery/authoring issue. Varkesh Final Capture remains one bar with beacon/capture logic. Last Weapon Archon remains one bar. Do not force monotonic HP across mechanically different encounters.

All genuine fresh-HP transitions use current Prime refresh. Same-bar states do not.

---

# Equipment / items / Cards / Primes

Current equipment catalog = 38 ordinary + 36 Relics + 17 native Legacies = **91**. Current consumables = **20**. Currency = Auren. Exactly 24 Standard Cards, max 3 equipped. Exactly 12 Primes, Recovered → Awakened only. Invocation MP = 50 / 80 / 90.

Chapter 4 uses exactly Fire / Ice / Lightning / Earth. Wind and Water are removed from the research/regulation framework. Reaction Conduit replaces Elemental Hexarch.

---

# Current open implementation work

Mandatory story raw-stat recertification is now **COMPLETE for Chapters 1–13**.

The next balance pass is:

1. **Optional Elite / Regional Hunt / Major Hunt raw-stat recertification.**

Recover existing optional raw-stat lines and compare them against current unlock/readiness levels. Preserve current identities and form architecture. Major Hunts remain stronger than player readiness. Do not add Barrier, Brace, global Break/Stagger, natural Accuracy, Synthesis, or other retired systems.