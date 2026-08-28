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
8. `docs/DIALOGUE_AUTHORING_SCHEMA.md` and `docs/STEP_7C_AUTHORING_TEMPLATE.md` before dialogue Resource work

If a task conflicts with these files or a newer explicit user instruction, stop and surface the conflict. Do not silently reinterpret canon.

Historical audits and cumulative trackers are provenance, not automatic current authority.

---

# Current authority state

Whole-project written authority:

> **Diyse v2.10 / Audit125**

Current newest chain:
- `docs/canon/AUDIT125_MANDATORY_FORMATION_EXP_CEXP_ALLOCATION_LOCK.md` — mandatory formation player-EXP/CEXP allocation and named/story remainder envelopes.
- `docs/canon/AUDIT124_OPTIONAL_EXP_AND_LEVEL_70_COMPLETIONIST_CAP_LOCK.md` — optional player EXP / Level-70 completionist proof.
- `docs/canon/AUDIT123_CLASS_MP_CEXP_MASTERY_AND_LATE_GAME_PROGRESSION_LOCK.md` — class Ability MP, CEXP, Mastery, player-level spine, late mandatory EXP and enemy bands.
- `docs/canon/AUDIT122_BASE_HIT_EVASION_AND_BLEED_RUNTIME_LOCK.md` — Base Hit/Evasion and Bleed.
- `docs/canon/AUDIT121_CURRENT_SYSTEMS_ITEM_EQUIPMENT_AND_PROGRESSION_RECONCILIATION_LOCK.md` — current classes/Faces, removed systems, Legacies, Relic cleanup, 20-consumable economy, Chapter-4 rework and current terminology.
- compatible older Audit120–Audit113 files remain active where not superseded.

Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level. Chapter 4's four-element script/runtime state controls.

HD-2D is the sole active presentation target.

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

Critical:
- base 5%;
- flat percentage-point bonuses;
- ordinary random cap 50%;
- eligible multiplier 1.5×;
- Crit does not bypass Defense/Spirit.

Removed systems:
- **Barrier does not exist.**
- **Brace does not exist.**
- no global Break/Stagger meter.
- Staggered is an ordinary harmful status only.
- Guard remains valid.

Bleed damages each round and again when the affected character acts. It clears only on full-HP restoration, eligible harmful-status clear, or eligible item.

---

# Current classes / Mastery

- Cyanis — Crest Knight / Crest Arcanist — Might
- Ilyra — Blue Warden / Vowblade — Grace
- Torren — War Archer / Routeweaver — Acuity
- Nimera — Cardweaver / Proofhunter — Change
- Vaelira — Green Arcanist / Axiomblade — Elements
- Seyrik — Ruin Vanguard / Ruin Warden — Ruin

Base/Subclass cap = CL13. No Subclass before end-Ch7 Sixfold Volition.

Audit123's class Ability MP tables are closed. Do not reopen without later authority or demonstrated failure.

Synthesis is removed.

Exactly:
- 4 Core Masteries
- 4 Subclass Masteries
- 8 active nodes
- 8 automatic Mastery Points

Eligibility:
- Core — Base CL3 / 6 / 9 / 12
- Subclass — CL3 / 5 / 7 / 11

Automatic points:
1. Lv5
2. Lv10
3. Lv15
4. Lv20
5. Sixfold Volition
6. Lv40
7. Lv50
8. Lv60

No ninth point and no Lv70 surplus point.

Subclass Mastery 3 purchase grants donor Relic access. Subclass Mastery 4 purchase grants donor Legacy access. The donor's actual obtained item is equipped; no duplicate artifact and no universal off-owner nerf.

---

# CEXP / player progression firewall

CL13 cumulative threshold = **6,000 CEXP**.

Base and Subclass CEXP are separate. Selected class gets 100%; unselected class gets 0. CEXP sent to a capped class is lost.

Pre-Volition Ch1–7 normal CEXP = **4,950**.

Post-Volition normal CEXP:
- Ch8 1,300
- Ch9 1,450
- Ch10 1,200
- Ch11 1,800
- Ch12 2,750
- Ch8–12 total **8,500**
- Ch13 catch-up/overflow **1,500**

Normal full Base+Subclass Class-Level completion occurs during Chapter 12, with Seyrik around end Ch12.

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

Do not restore the rejected Lv62-at-end-Ch12 model.

Desired sequence:
1. Class Levels complete around Ch12 / roughly Lv53–57.
2. Final Mastery point arrives around Last Shelter / Lv60.
3. Normal campaign ends around Lv62.
4. Lv62–70 is optional/completionist headroom.

---

# Optional EXP / Level-70 firewall — Audit124

Fixed authored pre-Last-Shelter optional EXP:
- Side Quests — 20,000
- Character Quests — 55,000
- Regional Hunts — 70,000
- Major Hunts #1–5 — 50,000
- total — **195,000 EXP**

MH6 / The Unfinished World = **24,000 EXP**, outside cap proof.

At Last Shelter:
- normal route = 415,400 / Lv60
- Lv70 = 594,100
- completionist proof = 610,400
- buffer = 16,300.

Lower-level player-EXP diminishing returns apply to ordinary/repeatable enemy-kill EXP only. Fixed authored completion/first-clear packages are exempt.

> **WEAK ENEMIES DIMINISH — AUTHORED CONTENT DOES NOT**

---

# Mandatory formation EXP/CEXP firewall — Audit125

Expected ordinary random-encounter center = **225 total**. Counts are planning centers, not quotas. Chapter 4 remains 19.

Mandatory chapter player-EXP allocation:
- Ch1 ordinary 855 / authored 745 / total 1,600
- Ch2 2,288 / 2,512 / 4,800
- Ch3 3,480 / 4,520 / 8,000
- Ch4 5,262 / 5,938 / 11,200
- Ch5 8,978 / 9,822 / 18,800
- Ch6 10,600 / 14,300 / 24,900
- Ch7 14,120 / 17,180 / 31,300
- Ch8 18,962 / 19,238 / 38,200
- Ch9 25,000 / 20,500 / 45,500
- Ch10 31,800 / 21,500 / 53,300
- Ch11 ~45,300 / ~16,200 / 61,500
- Ch12 ~47,100 / ~22,900 / 70,000
- Ch13 ~29,800 / ~49,200 / 79,000

Late player-EXP Light / Standard / Heavy anchors:
- Ch9 — **1,245 / 1,540 / 1,920**
- Ch10 — **1,700 / 2,100 / 2,500**
- Ch11 — **2,100 / 2,650 / 3,100**
- Ch12 — **2,100 / 2,600 / 3,150**
- Ch13 — **3,000 / 3,700 / 4,500**

Do not restore the old Ch12 2,500 / 3,100 / 3,700 table; it belonged to an obsolete 83,000-EXP chapter budget.

Chapter 4 is protected at:
- 19 expected random encounters
- 6/6/7 phase center
- 202.4 → 256.2 → 358.6 weighted phase averages
- 5,262 ordinary EXP
- 11,200 total mandatory EXP.

Formation CEXP Light / Standard / Heavy:
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

Current named/story CEXP remainder centers:
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

Do not apply the player-EXP lower-level diminishing-return table automatically to CEXP. Audit125 creates no CEXP diminishing-return subsystem.

---

# Equipment / items firewall

Current equipment catalog = 38 ordinary + 36 Relics + 17 native Legacies = **91**.

Current consumables = **20**. Currency = Auren.

Ordinary equipment architecture, 17/17 Legacy mechanics, Relic stale-mechanic cleanup, consumable architecture, and current economy/placement are closed unless explicitly reopened.

No equipment may depend on Barrier, Brace, or a global Break/Stagger meter.

---

# Standard Cards / Primes

Exactly 24 Standard Cards; max 3 equipped. Current Acuity quartet = Faultline Sight / Measured Response / Predicted Impact / Decisive Interval.

Predicted Impact = one enemy, Magical/Colorless, P180, BH110, 28 MP, 30% Stun.

Exactly 12 Primes; Recovered → Awakened only. Invocation MP = 50 / 80 / 90. No Prime XP/levels/duplicates.

Prismatic Deluge = 90×4 = 360. Regulator Fang = 250 Power / 25% Spirit penetration.

---

# Chapter 4 elemental firewall

Chapter 4 uses exactly Fire / Ice / Lightning / Earth. Wind and Water are removed from the research/regulation framework.

Reaction Conduit replaces Elemental Hexarch. Regulation Crucible uses four chambers, exactly two active/targetable at once.

S022–S026 Markdown and matching dialogue `.tres` resources are synchronized. Historical `SIXFOLD` strings may remain only as technical compatibility IDs, not display/lore/mechanical authority.

---

# Current open progression implementation work

After Audit125, only these progression layers remain open:
1. exact named/story player-EXP package placement by encounter/milestone;
2. exact named/story CEXP package placement by encounter/milestone;
3. progression-dependent named-enemy/boss raw-stat recertification.

Do **not** reopen class Ability MP, the 6,000-CEXP curve, the eight-point Mastery schedule, Ch12 Class-Level completion, Last Shelter Lv60, ending Lv62, the 195,000 optional EXP pool, or Audit125 formation allocation merely because named/story placement is still pending.
