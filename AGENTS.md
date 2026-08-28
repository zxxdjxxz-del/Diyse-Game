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

> **Diyse v2.14 / Audit129**

Newest chain:
- `docs/canon/AUDIT129_CHAPTERS_1_4_MANDATORY_NAMED_RAW_STAT_RECERTIFICATION_LOCK.md` — Ch1–4 mandatory named/special raw stats.
- `docs/canon/AUDIT128_CHAPTERS_9_13_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md` — Ch9–13 exact named/story rewards; 13-chapter placement closure.
- `docs/canon/AUDIT127_CHAPTERS_5_8_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
- `docs/canon/AUDIT126_CHAPTERS_1_4_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
- `docs/canon/AUDIT125_MANDATORY_FORMATION_EXP_CEXP_ALLOCATION_LOCK.md`
- `docs/canon/AUDIT124_OPTIONAL_EXP_AND_LEVEL_70_COMPLETIONIST_CAP_LOCK.md`
- `docs/canon/AUDIT123_CLASS_MP_CEXP_MASTERY_AND_LATE_GAME_PROGRESSION_LOCK.md`
- `docs/canon/AUDIT122_BASE_HIT_EVASION_AND_BLEED_RUNTIME_LOCK.md`
- `docs/canon/AUDIT121_CURRENT_SYSTEMS_ITEM_EQUIPMENT_AND_PROGRESSION_RECONCILIATION_LOCK.md`
- compatible older Audit120–Audit113 remain active where not superseded.

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

Status Resistance bands:
- 0 Normal
- 5 Resistant
- 10 Highly Resistant
- 15 Exceptional
- immunity explicit only.

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

Base/Subclass cap = CL13. No permanent Subclass use before Sixfold Volition at end Ch7. Synthesis is removed.

Audit123's class Ability MP tables are closed.

Exactly 8 automatic Mastery Points:
1. Lv5
2. Lv10
3. Lv15
4. Lv20
5. Sixfold Volition
6. Lv40
7. Lv50
8. Lv60

Eligibility:
- Core — Base CL3 / 6 / 9 / 12
- Subclass — CL3 / 5 / 7 / 11

Subclass Mastery 3 grants donor Relic access; Subclass Mastery 4 grants donor Legacy access. The actual obtained donor item is equipped; no duplicate artifact.

---

# CEXP / player progression firewall

CL13 cumulative threshold = **6,000 CEXP**.

Base and Subclass CEXP are separate. Selected class gets 100%; unselected class gets 0. CEXP sent to a capped class is lost.

Normal full Base + Subclass Class-Level completion occurs during Ch12, with Seyrik around end Ch12.

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

---

# Progression / reward firewall

Audit124 fixed authored pre-Last-Shelter optional pool = **195,000 EXP**. Major Hunt #6 is outside the cap proof.

Audit125 expected ordinary encounter center = **225**, planning centers not quotas. Chapter 4 remains 19 expected random encounters / 5,262 ordinary EXP / 11,200 total mandatory EXP.

Exact mandatory named/story placement is closed:
- Ch1–4 Audit126
- Ch5–8 Audit127
- Ch9–13 Audit128

Optional Elites/Hunts/quests do not consume mandatory chapter reward pools. Same-bar changes pay once. Fresh-HP multi-form bosses pay one combined package after final-form clear. Fixed authored packages are exempt from ordinary lower-level enemy EXP diminishing returns. No CEXP diminishing-return subsystem exists.

Current late chapter identity:
- Ch11 = Crown Engine / Calder / Custodian / Truth.
- Ch12 = Reforged March: Westguard → Blackspine → Draevensreach → Varkesh capture → Vhalmarch → Vorathen → Veiled Citadel → Vaelkor.
- Ch13 = Deepest City → Last Weapon Archive → Last Weapon Archon → Last Shelter → Reactor Galleries → Reactor–Crest Interface → Reconstituted Entity → The Last Command → Final Severance.

True final PONR = **Last Shelter → Reactor Galleries**. Normal ending ~Lv62.

---

# Audit129 Ch1–4 raw-stat firewall

Early main-boss pacing target = **6–9 effective combat rounds for the complete encounter**.

| Ch | Body | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
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

Important:
- Ch1–3 main-boss HP/offense/defense lines are retained; do not inflate them.
- `Hold the Junction` and Ch3 S018 confrontations are formation-level events; do not create fake singular combat bodies.
- Regulation Crucible is now 2,200 HP Form I → 2,900 HP fresh Form II, 5,100 minimum body HP total.
- Do not copy obsolete 4,901 HP into each form.
- Audit129 does not invent chamber HP pools.
- Elder Briarhide's Recovered Last Sentinel resolution is explicitly nonlethal.

---

# Equipment / items / Cards / Primes

Current equipment catalog = 38 ordinary + 36 Relics + 17 native Legacies = **91**.
Current consumables = **20**. Currency = Auren.
Exactly 24 Standard Cards; max 3 equipped.
Exactly 12 Primes; Recovered → Awakened only. Invocation MP = 50 / 80 / 90.

---

# Chapter 4 elemental firewall

Chapter 4 uses exactly Fire / Ice / Lightning / Earth. Wind and Water are removed from the research/regulation framework.

Reaction Conduit replaces Elemental Hexarch. Regulation Crucible uses four chambers, exactly two active/targetable at once. Current climax is Regulation Crucible → The Seventh Reaction with genuine fresh Form II and no third form.

---

# Current open implementation work

After Audit129, the active progression implementation pass is:

1. **Chapters 5–8 mandatory named-enemy/boss raw-stat recertification.**

Recover current HP / ATK / MAG / DEF / Spirit / SPD / Evasion / Status Resistance and compare against final player-level and boss-duration bands. Preserve encounter mechanics and HP-bar/form architecture.

Do **not** reopen class Ability MP, the 6,000-CEXP curve, the eight-point Mastery schedule, Ch12 Class-Level completion, Last Shelter Lv60, ending Lv62, the 195,000 optional EXP pool, Audit125 formation allocation, Audits126–128 reward placement, or Audit129 Ch1–4 raw stats without explicit later authority or demonstrated failure.
