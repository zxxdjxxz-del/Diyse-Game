# Diyse — Active Engineering Canon Guardrails

This file is an implementation-facing authority index and compact guardrail summary. It does **not** replace the canon audits. If it omits a compatible older lock, that lock remains active. If it conflicts with a later master audit or explicit approved correction, the later authority wins.

## Current whole-project authority

**Diyse: HD-2D JRPG Clean Active Complete Master Canon v2.05 / Audit120 — Critical Hit and Direct-Damage Formula Lock**  
**Date:** August 26, 2026

Current newest authority chain:

- **v2.05 / Audit120** — controlling Physical/Magical/Hybrid direct-damage formula and Critical Hit system.
- **v2.04 / Audit119** — compatible Card/Prime MP, MP-restorative ladder, named-combat resistance, Prime status/scaling, progression directives, side-quest tracker reconciliation.
- **v2.03 / Audit118** — exact ordinary-equipment and Relic numerical/source catalog, settled Legacy Traits, Forge source matrix.
- **v2.02 / Audit117** — equipment/Relic/Legacy structure, Synthesis removal, donor-access/class-progression reconciliation.
- **v2.01 / Audit116** — compatible Standard-Card and Prime command definitions.
- **v2.00 / Audit115** — compatible global status/element/Ruin/class-Ability normalization.
- **v1.98 / Audit113** — current 13-chapter reindex.
- compatible older audits remain active where not superseded.

Current domain pointers:

- **Current Critical/direct-damage authority:** `docs/canon/AUDIT120_CRITICAL_HIT_AND_DIRECT_DAMAGE_FORMULA_LOCK.md`
- **Compatible combat/resource/Prime/progression reconciliation:** `docs/canon/AUDIT119_POST_AUDIT116_COMBAT_RESOURCE_PRIME_AND_PROGRESSION_RECONCILIATION_LOCK.md`
- **Exact ordinary/Relic/Legacy-Trait/Forge numerical catalog:** `docs/canon/AUDIT118_COMPLETE_EQUIPMENT_TRACKER_DELTA_PROMOTION_AND_NUMERICAL_CATALOG_LOCK.md`
- **Equipment/Legacy/class-access structure:** `docs/canon/AUDIT117_ITEM_EQUIPMENT_LEGACY_AND_CLASS_PROGRESSION_RECONCILIATION_LOCK.md`
- Compatible Card/Prime command authority: `docs/canon/AUDIT116_STANDARD_CARD_PRIME_RESOURCE_AND_COMMAND_RECONCILIATION_LOCK.md`
- Compatible global status/element/Ruin/class-Ability authority: `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md`
- Current chapter reindex: `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`
- Current Chapter-10 story authority: `docs/canon/AUDIT112_CHAPTER_10_THE_LAST_BLANK_MIRENA_EASTERN_WAYFINDER_CALDER_AND_BURIED_REGISTRY_CLOSURE.md`
- Current surface-map / region authority: `docs/canon/AUDIT111_FINAL_WORLD_MAP_REGION_TERMINOLOGY_AND_VISUAL_AUTHORITY_CLOSURE.md`
- Travel / point-of-no-return authority: `docs/canon/AUDIT109_WORLD_MAP_ROAD_TRAVEL_AND_LAST_SHELTER_POINT_OF_NO_RETURN_CLOSURE.md`

---

# Conflict order for current work

1. **Audit120** controls the direct-damage equation and Critical Hit rules.
2. **Audit119** controls compatible Standard-Card/Prime MP values, 21-consumable MP ladder, named resistance hierarchy, Prime status/scaling rules, and progression/side-quest corrections.
3. **Audit118** controls exact ordinary/Relic stats, Relic Traits/placements, settled Legacy Traits, and the exact Forge source matrix.
4. **Audit117** controls compatible equipment/Legacy/class-access structure and Synthesis removal.
5. **Audit116** controls compatible Card/Prime command identities/effects not changed by later audits.
6. **Audit115** controls compatible status/element/Ruin/class-Ability effects.
7. **Audit113** controls current chapter labels.
8. Compatible older domain locks remain active.

The historical cumulative tracker is design history, not authority by itself.

---

# Universal direct-damage / Critical system — Audit120

## Physical

> **BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)**

> **EffectiveDefense = CurrentDefense × (1 - EffectiveDefensePenetration)**

## Magical

> **BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)**

> **EffectiveSpirit = CurrentSpirit × (1 - EffectiveSpiritPenetration)**

Same-axis penetration adds in percentage points and remains capped at **75%**.

## Hybrid

Resolve authored Physical and Magical weighted components independently, then combine them. Character-Ability Ruin remains **75% Attack / 25% Magic** where Audit115 applies.

## Critical Hits

- base Critical Chance = **5%**;
- Critical Chance modifiers are flat **percentage-point additions**;
- ordinary random Critical Chance cap = **50%**;
- eligible Critical damage multiplier = **1.5×**;
- Base Hit/Evasion check resolves before the Critical roll;
- a miss receives no Critical roll;
- each authored direct hit in a multihit action rolls Crit independently by default;
- one single authored Hybrid hit uses one Critical roll on the combined eligible direct-damage result;
- eligible Magical direct hits use the same 1.5× multiplier;
- Crit does not bypass Defense/Spirit;
- Crit does not automatically improve harmful-status application;
- Burn, Bleed, explicitly no-Crit copied/echo damage, indirect Max-HP damage unless explicitly authored otherwise, and healing cannot Crit.

After normal formula/penetration resolution, a Critical multiplies eligible resolved direct damage by **1.5**, then remaining later-stage affinity/final-damage/target-side/Guard/Barrier/interception modifiers resolve under the normal global order. Round at the normal final-damage step.

There is no universal random ±damage variance.

Use **Base Hit**, not `Accuracy`, as the canonical hit-stat term.

---

# Elements / harmful statuses / named resistance

Standard elements:
- Fire
- Ice
- Lightning
- Earth

Universal harmful statuses:
- Burn
- Freeze
- Stun
- Staggered
- Bleed

Ruin is a special affinity/school, not a fifth standard element.

Named-combat elemental multipliers:
- Weak 125%
- Neutral 100%
- Resistant 80%
- Strongly Resistant 60%
- Immune 0%

Named-combat harmful-status susceptibility:
- Normal 100%
- Resistant 80%
- Strongly Resistant 60%
- Immune 0%

Bosses, Hunts, and Elites should be more resistant than ordinary enemies without blanket-immunity design. Major-Hunt exact static resistance profiles are in Audit119.

Audit115 remains controlling for compatible status timing/duration/magnitude rules.

---

# Standard Cards — current resource guardrail

Exactly **24 Standard Cards**. Each character may equip **3**.

Cards are reusable, consume the user's selected action, and cost MP. There is no draw/deck/discard/charge/duplicate/rank system.

Current exact MP costs:

### Might
- Iron Testament — 22
- Sunder the Gate — 28
- Relentless Flurry — 30
- March of Blades — 32
- Sanguine Alloy — 26

### Elements
- Cinder Judgment — 24
- Winterglass Spear — 26
- Thunder Chain — 32
- Confluence Sigil — 34
- Worldsplitter — 38

### Grace
- Restoration — 28
- Merciful Reprisal — 28
- Wellspring — 36
- Dawn Recall — 44

### Acuity
- Faultline Sight — 18
- Measured Response — 24
- Predicted Impact — 28
- Decisive Interval — 36

### Change
- Burden Shift — 26
- Reversal Engine — 40
- Split Moment — 48

### Ruin
- Calamity Lance — 34
- Devouring Singularity — 42
- Zero Hour — 48

Current range: **18–48 MP**.

Audit116's older 12–36 MP table is superseded. Card effects/powers remain controlled by Audit116 where compatible.

Four exact acquisition homes remain open under Audit116: Restoration, Cinder Judgment, Iron Testament, Sunder the Gate.

---

# Prime framework — current Audit119 resource/scaling guardrail

Exactly **12 Prime Cards**: 6 Story + 6 Major-Hunt.

Progression is exactly:

> **Recovered → Awakened**

`Reactive` is a retired temporary tracker label.

Current Invocation MP:
- Recovered Story Prime — **50 MP**
- Awakened Story Prime — **80 MP**
- Awakened Major-Hunt Prime — **90 MP**
- manifested Prime commands — **0 additional MP**

Awakened Prime behavior:
- suspends/replaces the ordinary active party;
- exactly **3 Prime rounds**;
- one selected Prime command per Prime round;
- **3 full normal-party-round shared cooldown** after dismissal;
- once per identity per battle unless a genuine fresh-HP boss form refreshes it.

No Prime XP, Prime levels, duplicate progression, or upgrade-material system.

### Prime status/control
Default harmful-status susceptibility = **80%** for all five canonical statuses unless individually authored otherwise.

Freeze/Stun together may deny at most **one selected Prime command per manifestation**. After that loss, that Prime is Freeze/Stun immune for the remainder of the manifestation. Prime-local statuses vanish on dismissal.

### Prime manifestation scaling
Reference Level = highest current level among the four active permanent party members at Invocation, clamped 1–70.

Neutral baseline:
- HP = 2.25 × Neutral HP(L)
- ATK = 4.75 × Neutral ATK(L)
- MAG = 4.75 × Neutral MAG(L)
- DEF = 1.65 × Neutral DEF(L)
- Spirit = 1.65 × Neutral Spirit(L)
- SPD = Neutral SPD(L) + 8

State/identity multipliers are defined in Audit119. If the neutral natural-growth curve changes in the dedicated progression pass, regenerate Prime arrays from the same architecture unless explicitly reopened.

Retained late-Major-Hunt anchors:
- Final Archive Arbiter — **43,100 HP / 229 ATK / 244 MAG / 194 DEF / 198 Spirit / 50 SPD**
- The Unfinished World — **78,000 HP / 304 ATK / 318 MAG / 226 DEF / 232 Spirit / 61 SPD**

The Unfinished World remains **78,000 HP**.

---

# Consumables / MP recovery — current Audit119 guardrail

Current Consumable count: **21**.

MP-restorative ladder:
- Flow Tonic — **50 MP**
- Deepflow Tonic — **80 MP**
- Highflow Tonic — **120 MP**
- Reservoir Tonic — **75% Max MP**
- Emergency Kit — **60% Max MP** as its MP component

Highflow Tonic is the late purchasable fixed-value tier. Reservoir Tonic remains rare/reward-only. Exact shop placement/pricing remains open.

Exact HP-restorative values and Emergency Rally final values remain open; do not promote the provisional v479 numbers by assumption.

---

# Current classes / Subclass access — Audit117

Permanent six:
- Cyanis — **Crest Knight / Crest Magus**
- Ilyra — **Blue Warden / Vowblade**
- Torren — **War Archer / Routeweaver**
- Nimera — **Cardweaver / Sixfold Knight**
- Vaelira — **Prism Archer / Green Arcanist**
- Seyrik — **Ruin Vanguard / Ruin Healer**

Base/Subclass caps are **CL13**.

Current Subclass equipment milestones:
- CL1 — donor Primary
- CL3 — donor Armor + Mastery 1 eligibility
- CL5 — donor Secondary + Mastery 2 eligibility
- CL7 — new ability + Mastery 3 / Equipment Mastery eligibility; **purchasing it grants donor Relic access**
- CL10 — new Subclass ability
- CL11 — Mastery 4 / Legacy Mastery eligibility; **purchasing it grants donor Legacy access**
- CL12 — Trait III
- CL13 — Ultimate / cap

**Synthesis is removed.** There is no Synthesis node, MP cost, passive, or Base-CL13/Subclass-CL13 Synthesis gate.

The old nine-point Mastery Point schedule requires reconciliation because only **8 active Mastery nodes** remain.

---

# Equipment / Relic / Legacy guardrail — Audits117–118

Current active equipment:
- **38 ordinary**
- **36 Relics**
- **17 native Legacies**
- **91 total**

All 12 Subclass Relics are removed. Six separate shared-Legacy artifacts are removed.

Exact ordinary stats/source map, Relic stats/Traits/placements, settled Legacy Traits, Cresthaven relative-value rules, and the exact 30-slot Forge source matrix are controlled by **Audit118**.

Slot firewalls:
- Ilyra — Wardrod Primary; Shield or Focus Secondary.
- Torren Great Bow — Weapon + Secondary.
- Vaelira Arcane Staff — one-slot Primary; Focus legal.
- Seyrik 2H Sword — Weapon + Secondary.
- Nimera ordinary/surviving Relic Conduits — one-slot.
- Nimera native Legacy Conduit — **Weapon + Secondary**.

Native Legacy completion requires:
- Base CL13;
- four Core Masteries;
- Character Quest/resolution;
- unique Character Quest Legacy Component;
- unique Legacy precursor;
- dedicated Gate A and Gate B materials;
- Kessara project availability.

Gate A releases the Legacy weapon. Gate B releases the rest of the package.

Forge economy:
- 5 Face components per Face / 30 total;
- 2 Legacy-gate-specific per Face / 12 total;
- 3 Relic-copy-specific per Face / 18 total;
- categories are non-interchangeable.

Relic-copy forging may create one identical extra copy of an already-obtained Relic; max quantity per Relic = 2. Legacies remain unique.

Equipment hierarchy:

> **Ordinary < Relic < Legacy**

Legacies may carry capstone Max HP / Max MP / **Base Hit** / Evasion perks. Exact 17-piece Legacy raw-stat/perk numbers remain pending approval.

Final Relic / Legacy / Legacy-Component / Forge-variant names remain deferred until dialogue is substantially more complete.

---

# Current progression guardrail — Audit119

- Player level cap = **70**.
- **Chapter 0 grants no character levels.**
- Chapters 1–7 intentionally progress somewhat below a near-linear curve.
- Faster progression begins after Chapter 7.
- Expected **Chapter-12 campaign-only clear target = Level 60**.
- Additional late-campaign EXP should be distributed backward through **Chapter 9 onward**, not dumped into one Chapter-12 spike.
- Enemy strength and kill EXP should increase from chapter start to chapter end rather than using one flat chapter band.
- Old/weak enemies should award substantially reduced kill EXP to an overlevelled party.
- Fixed authored quest/Hunt first-clear packages are not automatically diminished merely because the party is overlevelled.

Exact Ch1–13 player bands, enemy bands, encounter counts, per-formation EXP, and diminishing-return percentages remain deferred to the dedicated EXP rebalance. The old v494–v503 exact tracker tables are not current canon.

---

# Current chapter / point-of-no-return firewall

The game has **13 numbered chapters** plus Chapter 0.

Late spine:
- Ch9 — Larkspire / Crownfall / Rhazek
- Ch10 — **The Last Blank**
- Ch11 — **Crown Engine**
- Ch12 — **The Reforged March** / Vaelkor / cleanup
- Ch13 — **The Last Command** / Last Shelter / Final Severance / ending

Old references where Ch10=Crown Engine, Ch11=Vaelkor campaign, or Ch12=final domain are stale.

True irreversible threshold:

> **Last Shelter → Reactor Galleries**

---

# Current ordinary Side-Quest correction — Audit119

The stale v480–v493 tracker reduction branch is not current roster authority.

Current retained ordinary Side Quests include:

- **Edda Harth — The Marks We Leave** — Greenhollow; after Torren joins in Ch1; low/zero required combat; reuse existing early spaces.
- **Edda Harth — When the Roads Open** — post-Vaelkor cleanup in current Ch12; route-reopening sequel.
- **Talia Rell — The Third Caravan** — after Ch8; Greenhollow → Ashford; Recovery Depot → Old Supply Cut → Failed Handoff → Temporary Shelter → Settlement Approach.
- **Talia Rell — The Living List** — after Ch10; Ashford anchor; Recovery Office → Temporary Quarter → Alderwick → Old Census Post.

Dialogue and exact final reward packages remain deferred.

---

# Current map / region firewall

Audit111 remains the final surface-world visual/terminology authority where compatible.

Current macro terminology includes:
- **BLACK HOST TERRITORY**
- **THE WESTWAYS**
- **THE GREYSPIRES**
- **YAHTRENHOLD**
- **The Blackspine**
- **Westguard**
- **Vhalmarch**
- **Vorathen**
- **The Veiled Citadel**

Surface macro geography is closed unless explicitly reopened.

---

# Current open / deferred frontier after Audit120

Immediate unresolved items include:

1. approve/revise exact **17-Legacy raw stats + Max-HP/Max-MP/Base-Hit/Evasion assignments**;
2. finalize exact current **Base/Subclass Ability MP costs** after the latest class-kit identities;
3. resolve global **Base Hit vs Evasion** hit formula;
4. reconcile the **Mastery Point schedule for 8 active nodes**;
5. finalize HP consumables / Emergency Rally;
6. resolve exact Prismatic Deluge Power if still open;
7. resolve the four open Standard-Card acquisition homes;
8. complete the detailed current Ch1–13 EXP/enemy/encounter rebalance and progression-dependent named-enemy re-certification;
9. finish Consumable shop timing/pricing/final currency denomination;
10. finish Kessara Relic-copy service UI/fee and exact pickup presentation where still open;
11. keep final Relic/Legacy/Legacy-Component/Forge-variant naming deferred until dialogue is sufficiently complete.

Omission from this compact file does not erase compatible older canon. Audit120, Audit119, Audit118, Audit117, Audit116, Audit115, Audit113, compatible prior canon, exact visual authorities, and newer explicit user-approved corrections control conflicts.