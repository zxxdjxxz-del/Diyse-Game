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

> **Diyse v2.20 / Audit135**

Newest chain:
- `docs/canon/AUDIT135_MAJOR_HUNT_RAW_STAT_RECERTIFICATION_LOCK.md` — all 6 Major-Hunt recommended levels/raw stats; Crownless fresh-form split; The Unfinished World one-bar superboss budget.
- `docs/canon/AUDIT134_REGIONAL_HUNT_RAW_STAT_RECERTIFICATION_LOCK.md` — all 11 Regional-Hunt recommended levels/raw stats; Throne of Emperor Vaelkor current two-form split.
- `docs/canon/AUDIT133_OPTIONAL_ELITE_RAW_STAT_RECERTIFICATION_LOCK.md` — 12 current numbered-chapter optional Elites; no Ch10 optional Elite.
- `docs/canon/AUDIT132_CHAPTERS_9_13_MANDATORY_NAMED_RAW_STAT_RECERTIFICATION_LOCK.md` — Ch9–13 mandatory named/special raw stats; completes mandatory-story raw-stat recertification.
- `docs/canon/AUDIT131_CHAPTERS_5_8_MANDATORY_NAMED_RAW_STAT_RECERTIFICATION_LOCK.md` — Ch5–8 mandatory named/special raw stats.
- `docs/canon/AUDIT130_REGULATION_CRUCIBLE_FORM_I_HP_CORRECTION_LOCK.md` — Regulation Crucible Form-I HP = 2,400.
- `docs/canon/AUDIT129_CHAPTERS_1_4_MANDATORY_NAMED_RAW_STAT_RECERTIFICATION_LOCK.md` — compatible Ch1–4 raw stats.
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
- Spirit = magical defense;
- Hybrid components resolve independently;
- no universal random damage variance;
- no hidden universal AoE penalty.

Base Hit / Evasion:
> `AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers`

> `EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers`

> `FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)`

There is no natural Accuracy stat.

Status Resistance bands: 0 Normal / 5 Resistant / 10 Highly Resistant / 15 Exceptional; immunity explicit only.

Removed systems:
- Barrier does not exist.
- Brace does not exist.
- no global Break/Stagger meter.
- Staggered is an ordinary harmful status.
- Guard remains valid.

Bleed damages each round and whenever the affected character acts. It clears only on full-HP restoration, eligible harmful-status clear, or eligible item.

Genuine fresh-HP boss transformations refresh Prime availability. Same-bar state changes do not.

---

# Current classes / Mastery / progression

- Cyanis — Crest Knight / Crest Arcanist — Might
- Ilyra — Blue Warden / Vowblade — Grace
- Torren — War Archer / Routeweaver — Acuity
- Nimera — Cardweaver / Proofhunter — Change
- Vaelira — Green Arcanist / Axiomblade — Elements
- Seyrik — Ruin Vanguard / Ruin Warden — Ruin

Base/Subclass cap = CL13. No permanent Subclass use before end-Ch7 Sixfold Volition. Synthesis is removed. Audit123 class Ability MP tables are CLOSED.

CL13 cumulative CEXP = **6,000**. Base/Subclass CEXP are separate. Selected class gets 100%; unselected gets 0; CEXP sent to a capped class is lost.

Exactly 8 automatic Mastery Points: Lv5, Lv10, Lv15, Lv20, Sixfold Volition, Lv40, Lv50, Lv60.

Mandatory-route anchors: Ch1 5 / Ch2 9 / Ch3 13 / Ch4 17 / Ch5 22 / Ch6 27 / Ch7 32 / Ch8 37 / Ch9 42 / Ch10 47 / Ch11 52 / Ch12 57 / **Last Shelter 60** / **End Ch13 62** / cap 70.

Class Levels complete during Ch12; Seyrik is the limiting normal-route case around end Ch12.

---

# Reward / encounter firewall

Audit124 authored pre-Last-Shelter optional pool = **195,000 EXP**. Major Hunt #6 is outside the cap proof.

Audit125 expected ordinary encounter center = **225**, planning centers not quotas. Ch4 remains 19 expected random encounters / 5,262 ordinary EXP / 11,200 total mandatory EXP.

Exact mandatory named/story reward placement is complete under Audits126–128.

Optional Elites/Hunts/quests do not consume mandatory chapter pools. Same-bar changes pay once. Fresh-HP multi-form bosses pay one combined reward after final-form clear. Fixed authored packages are exempt from ordinary lower-level enemy EXP diminishing returns. No CEXP diminishing-return subsystem exists.

Ch13 true PONR = **Last Shelter → Reactor Galleries**.

---

# Raw-stat authority firewall

Mandatory story:
- Ch1–4 — Audit129 + Audit130
- Ch5–8 — Audit131
- Ch9–13 — Audit132

Optional Elites:
- Audit133
- 12 current numbered-chapter optional Elites
- no approved Ch10 optional Elite
- typical duration ~2–4 serious party rounds

Regional Hunts:
- Audit134 closes all 11 recommended levels and body raw stats
- recommended level = preparedness target, not access gate
- fixed tuning; no dynamic scaling
- Hunts #1–10 retain recovered raw values
- Throne of Emperor Vaelkor = Sealed Throne **11,800 HP** → fresh Walking Throne **14,200 HP**, total **26,000**
- Walking Throne receives fresh-form Prime refresh
- no Attendant HP pools invented

Major Hunts:
- Audit135 closes all 6 recommended levels and body raw stats
- fixed tuning; no dynamic scaling
- Ashen Whitehorn — Lv22, **11,270 HP**, EVA10 / SR10
- Crownless Siege Marshal — Lv28, **9,360 HP**, EVA5 / SR10
- Crownless War Engine — Lv29, fresh **11,650 HP**, EVA0 / SR10; combined **21,010 HP** and fresh-form Prime refresh
- Concordance Guardian — Lv35, **18,180 HP**, EVA5 / SR15, one continuous bar
- Worldscar Leviathan — Lv47, **30,200 HP**, EVA0 / SR10, one continuous bar
- Final Archive Arbiter — Lv58, **43,100 HP**, EVA5 / SR15, one continuous bar
- The Unfinished World — Lv70, **78,000 HP**, EVA0 / SR15, one continuous WORLDFRAME → WORLDHEART EXPOSED → FINAL CONSTRUCTION bar
- The Unfinished World uses only Earth/Staggered, Ice/Freeze, Lightning/Stun, Fire/Burn; no Water/Wind/fifth element

Tier principle:
> **Ordinary < Elite < mandatory story boss < Regional Hunt < Major Hunt**

Progression-dependent named/boss raw-stat recertification is closed across mandatory story, optional Elite, Regional Hunt, and Major Hunt layers.

Do not fabricate unresolved component/subtarget HP merely to make a table complete.

---

# Equipment / Cards / Primes

Current equipment catalog = 38 ordinary + 36 Relics + 17 Legacies = **91**. Consumables = **20**. Currency = Auren.

Exactly 24 Standard Cards, max 3 equipped. Exactly 12 Primes, Recovered → Awakened only. Invocation MP = 50 / 80 / 90.

Chapter 4 uses exactly Fire / Ice / Lightning / Earth. Wind and Water are removed from research/regulation. Reaction Conduit replaces Elemental Hexarch.

---

# Active implementation frontier

## **Kessara Relic-copy service implementation**

Preserve the already-closed copy rule:
- Relic must already be obtained;
- one matching copy component is required;
- maximum one forged duplicate per Relic;
- maximum quantity = 2;
- the duplicate is mechanically identical;
- Legacies cannot be copied.

The remaining implementation pass may determine service fee, menu timing, and original-vs-copy UI presentation. Do not reopen closed MP/CEXP/Mastery/mandatory raw-stat/Elite/Regional-Hunt/Major-Hunt layers without explicit later authority or demonstrated failure.