# Diyse — Current Implementation Status

**Written authority checkpoint:** **v2.04 / Audit119**  
**Presentation target:** HD-2D  
**Active repository:** `zxxdjxxz-del/Diyse-Game`

## Current closure / implementation state

- Chapters **0–4** remain COMPLETE/CLOSED at story/dialogue authority level.
- Chapters 0–4 HD-2D Conversion Audit Pass 1: COMPLETE / APPROVED.
- Cross-chapter HD-2D consistency/cost consolidation for Chapters 0–4: COMPLETE / PASS / GREEN.
- Shared HD-2D runtime foundation: IMPLEMENTED.
- Chapters 0–4 HD-2D presentation sidecars/environment-state hookup: IMPLEMENTED where previously recorded.
- Final visual asset replacement remains production work where not already implemented.
- Detailed late-game scene/runtime implementation remains pending.
- Exact **ordinary-equipment and surviving-Relic stats/source data** are closed under Audit118 and may be implemented directly.
- Audit119 now supplies current **universal direct-damage math, Standard-Card MP, Prime Invocation MP/scaling/control, named resistance hierarchy, and MP-restorative ladder**.
- Exact 17-piece Legacy raw-stat/capstone-perk values remain pending approval and must not be implemented from working v600 yet.
- Exact current Base/Subclass Ability MP values after the latest class-kit identities remain open; preserve the higher-cost direction but do not implement stale old tables as final.

---

## Current numerical implementation guardrails

### Direct damage
Use Audit119:

> **Component Damage = Weight × (Power / 100) × Offense × 1.50 × [150 / (150 + Effective Defensive Stat)]**

Physical = Attack vs Defense. Magical = Magic vs Spirit. Same-axis penetration caps at 75%. No hidden AoE penalty or universal random damage variance.

Universal Critical payout/order remains open.

### Standard Cards
- exactly 24
- maximum 3 equipped per character
- reusable and MP-consuming
- current MP range **18–48**, not the old Audit116 12–36 range

### Prime Invocation
Current costs:
- Recovered Story — **50 MP**
- Awakened Story — **80 MP**
- Awakened Major Hunt — **90 MP**
- Prime commands after manifestation — 0 additional MP

`Reactive` is retired; use **Recovered → Awakened**.

Prime status/scaling implementation must follow Audit119, including default 80% status susceptibility and one-command Freeze/Stun hard-control ceiling per manifestation.

### Consumables
Current Consumable count = **21**.

MP ladder:
- Flow Tonic 50
- Deepflow Tonic 80
- Highflow Tonic 120
- Reservoir Tonic 75% Max MP
- Emergency Kit 60% Max MP as its MP component

Exact HP-restorative numbers remain open.

---

## Current late-game chapter structure

Chapter 10 — The Last Blank was inserted after Chapter 9.

Current operational interpretation:
- **Chapter 10 — The Last Blank** — story architecture locked under Audit112; detailed line-complete/runtime implementation pending.
- **Chapter 11 — Crown Engine** — Calder / Custodian / Truth; detailed scene production pending.
- **Chapter 12 — The Reforged March** — final Black Host campaign / Varkesh / Vhalmarch / Vorathen / Vaelkor / cleanup.
- **Chapter 13 — The Last Command** — final Ancient domain / Last Weapon / Entity / Final Severance / ending.

Pre-insertion mapping:
- old Ch10 → current Ch11
- old Ch11 → current Ch12
- old Ch12 → current Ch13

Do not wire runtime content against the old late-game numbering.

---

## Current point of no return

Audit109 controls:

> **Last Shelter → Reactor Galleries = true irreversible threshold**

Launching Chapter 13 is deliberate but not itself irreversible. Do not disable all world return at Chapter-13 start.

---

## Current class / Mastery implementation state

Current Base/Subclass identities:
- Cyanis — Crest Knight / Crest Magus
- Ilyra — Blue Warden / Vowblade
- Torren — War Archer / Routeweaver
- Nimera — Cardweaver / Sixfold Knight
- Vaelira — Prism Archer / Green Arcanist
- Seyrik — Ruin Vanguard / Ruin Healer

Base/Subclass cap = **CL13**.

Subclass donor access:
- CL1 donor Primary
- CL3 donor Armor
- CL5 donor Secondary
- CL7 Mastery 3 / Equipment Mastery purchase → donor Relic access
- CL11 Mastery 4 / Legacy Mastery purchase → donor Legacy access

**Synthesis is removed.** Do not implement a Synthesis node, Synthesis MP cost, Synthesis passive, or old Base-CL13/Subclass-CL13 eligibility gate.

The old Mastery Point schedule was built for nine nodes. Only eight active Mastery nodes remain; exact grant schedule is still open.

---

## Equipment / Relic / Legacy implementation state

Current active catalog:
- **38 ordinary**
- **36 Relics**
- **17 native Legacies**
- **91 total**

Audit118 is the exact implementation source for:
- all 38 ordinary raw-stat lines;
- ordinary first-acquisition/source map;
- Cresthaven ordinary backfill/relative values;
- all 36 surviving Relic stat/Trait packages;
- all 36 Relic placements;
- settled Legacy Traits;
- exact 30-slot Forge Component role/source matrix.

Slot rules:
- Ilyra — Wardrod Primary; Shield or Focus Secondary.
- Torren Great Bow — Weapon + Secondary.
- Vaelira Arcane Staff — one-slot Primary; Focus legal.
- Seyrik Two-Handed Sword — Weapon + Secondary.
- Nimera ordinary/surviving Relic Conduits — one-slot.
- Nimera native Legacy Conduit — Weapon + Secondary.

All 12 Subclass Relics are removed. Six separate shared-Legacy artifacts are removed.

Native Legacy completion requires Base CL13 + 4 Core Masteries + Character Quest/resolution + unique Legacy Component + precursor + Gate A + Gate B + Kessara availability.

Gate A releases the weapon. Gate B releases remaining package pieces.

Forge economy:
- 30 components total
- 12 Legacy-gate-specific
- 18 Relic-copy-specific
- categories non-interchangeable

Relic copy: one identical extra copy maximum per already-obtained Relic; max quantity 2. Legacies remain unique.

Equipment power hierarchy: **Ordinary < Relic < Legacy**.

Exact 17-Legacy raw stats and Max-HP/Max-MP/Accuracy/Evasion perk assignments are pending. Legacy elemental/status/perk/passive treatment also remains an explicit open design question.

---

## Progression / enemy numerical status

Current high-level locks:
- player level cap 70
- Chapter 0 grants no character levels
- Chapters 1–7 deliberately lower than a near-linear curve
- faster progression begins after Chapter 7
- expected Chapter-12 campaign-only clear target = **Lv60**
- distribute added late EXP backward through Chapter 9 onward
- enemy strength and kill EXP rise within a chapter from start to end
- weak/old enemies award substantially reduced kill EXP to overlevelled parties

The exact old v494–v503 chapter-level/enemy/encounter tables are **not current implementation authority**.

Detailed current Ch1–13 player bands, enemy bands, encounter counts, per-formation EXP, and diminishing-return percentages remain pending the dedicated progression pass.

Named-combat resistance should follow Audit119's 125/100/80/60/0 elemental framework and 100/80/60/0 status-susceptibility framework. Exact Major-Hunt static profiles are in Audit119.

Retained late-Hunt raw-stat anchors:
- Final Archive Arbiter — 43,100 HP / 229 ATK / 244 MAG / 194 DEF / 198 Spirit / 50 SPD
- The Unfinished World — 78,000 HP / 304 ATK / 318 MAG / 226 DEF / 232 Spirit / 61 SPD

Other named-enemy raw arrays should be re-certified against the current progression pass before final implementation if they depend on the reopened level curve.

---

## Current ordinary Side-Quest status

Do not use the stale v480–v493 cumulative-tracker reduction branch.

Current retained ordinary quests include:
- Edda Harth — **The Marks We Leave** — after Torren joins in Ch1 / Greenhollow / low-zero required combat.
- Edda Harth — **When the Roads Open** — post-Vaelkor cleanup / current Ch12.
- Talia Rell — **The Third Caravan** — after Ch8 / Greenhollow → Ashford.
- Talia Rell — **The Living List** — after Ch10 / Ashford anchor.

Dialogue and exact final reward packages remain later work.

---

## Late-game encounter-role mapping

### Chapter 12
- dedicated conventional Black Host Elite remains separate from Hunts;
- Regional Hunt #11 — Throne of Emperor Vaelkor belongs to current Chapter 12;
- Vaelkor mandatory climax remains **Emperor of the Reforged Host → Sovereign Panoply Unbound**;
- Vaelkor defeat opens cleanup and does not automatically start Chapter 13.

### Chapter 13
- Regional Hunt: none;
- Elite: Devourer of Names;
- Calamity Memory: enemy/special-enemy ecosystem role, not Elite;
- mandatory guardian: Last Weapon Archon;
- final boss: exactly **Reconstituted Entity → The Last Command**, two genuine full-health forms, no third form.

No runtime implementation claim is implied merely by these story/category locks.

---

## Current Story Prime / final-act terminology

Use:
- Last Sentinel / Might
- Last Convergence / Elements
- Last Sanctuary / Grace
- Last Cartographer / Acuity
- Last Scribe / Change
- Last Erasure / Ruin

Do not restore Resource / Last Measure.

---

## Current world terminology

Use:
- Yahtrenhold
- Black Host Territory
- The Westways
- The Greyspires
- The Blackspine
- Westguard
- Vhalmarch
- Vorathen
- The Veiled Citadel

Do not restore Blackstone as formal region label, Westreach, Black Mountains, or The Crownhold in current-facing content.

---

## HD-2D runtime foundation

Accepted shared foundation remains under `game/presentation/`, including:
- 1920×1080 reference composition support;
- ~80 px field-character helper targets;
- ~200–220 px battle-character targets;
- party-left / enemy-right / protected center action lane;
- authored environment-state definitions;
- encounter/scene presentation metadata;
- Prime visual suspension/return hooks;
- Android decorative quality profiles;
- reusable element/Card/Prime presentation families.

Exact final art remains separate from proven runtime architecture.

---

## Chapter 0–4 dialogue / production status

- Chapter 0 — historical validated runtime set retained where compatible.
- Chapter 1 — line-complete source + production Resources.
- Chapter 2 — line-complete source + production Resources.
- Chapter 3 — corrected line-complete source + production Resources.
- Chapter 4 — exact production source closed; runtime/static conversion present where implemented.

A presentation sidecar does not by itself lock final ordinary-enemy or Elite placement.

---

## Current production boundaries

Do not silently invent:
- late-game exact dialogue before explicit scene production;
- final Legacy numbers while v600 remains pending;
- final Base/Subclass Ability MP values before the current-kit cost pass;
- the global Accuracy/Evasion or Critical formula;
- exact HP-consumable values while open;
- final Level-70 Ch1–13 EXP/enemy/encounter tables;
- final currency denomination;
- final Relic/Legacy personal names before the deferred naming/dialogue phase.

---

## Current authoritative documents

- `docs/ACTIVE_CANON.md`
- `docs/canon/AUDIT119_POST_AUDIT116_COMBAT_RESOURCE_PRIME_AND_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT118_COMPLETE_EQUIPMENT_TRACKER_DELTA_PROMOTION_AND_NUMERICAL_CATALOG_LOCK.md`
- `docs/canon/AUDIT117_ITEM_EQUIPMENT_LEGACY_AND_CLASS_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT116_STANDARD_CARD_PRIME_RESOURCE_AND_COMMAND_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md`
- `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`
- current operational chapter files

Implementation should prefer the newest domain audit and current operational chapter files over historical cumulative-tracker text.
