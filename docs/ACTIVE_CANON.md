# Diyse — Active Engineering Canon Guardrails

This file is an implementation-facing authority index and compact guardrail summary. It does **not** replace the canon audits. If it omits a compatible older lock, that lock remains active. If it conflicts with a later master audit or explicit approved correction, the later authority wins.

## Current whole-project authority

**Diyse: HD-2D JRPG Clean Active Complete Master Canon v2.02 / Audit117 — Item, Equipment, Legacy, and Class-Progression Reconciliation Lock**  
**Date:** August 26, 2026

Current newest authority chain:

- **v1.91 / Audit106** — Item, Equipment, Catalog, Economy, and Audit104/105 Reconciliation Lock.
- **v1.92 / Audit107** — Sixfold Volition, Cartographic Mystery, Calder Archive, and Chapter-Structure Reconciliation Lock.
- **v1.93 / Audit108** — Exact World Map, Location Geography, Cerythvale, and The Last Blank Closure.
- **v1.94 / Audit109** — World Map Road, Travel, and Last Shelter Point-of-No-Return Closure.
- **v1.95 / Audit110** — Exact 3D World Map Visual / Spatial Authority Lock.
- **v1.96 / Audit111** — Final World Map, Region Terminology, and Visual Authority Closure.
- **v1.97 / Audit112** — Chapter 10: The Last Blank — Mirena, Eastern Wayfinder, Calder, and Buried Registry Closure.
- **v1.98 / Audit113** — Post-Insertion Chapter Reindex and Late-Game Operational File Reconciliation Lock.
- **v1.99 / Audit114** — Prime, Combat Element / Status, and Base-Class Normalization Lock.
- **v2.00 / Audit115** — Combat, Ruin, Status, and Full Class Ability Normalization Lock.
- **v2.01 / Audit116** — Standard Card, Prime Resource, and Prime Command Reconciliation Lock.
- **v2.02 / Audit117** — Item, Equipment, Legacy, and Class-Progression Reconciliation Lock.

Current domain pointers:

- **Current item/equipment/Relic/Legacy/Forge/Subclass-access authority:** `docs/canon/AUDIT117_ITEM_EQUIPMENT_LEGACY_AND_CLASS_PROGRESSION_RECONCILIATION_LOCK.md`
- Card / Prime economy + command authority: `docs/canon/AUDIT116_STANDARD_CARD_PRIME_RESOURCE_AND_COMMAND_RECONCILIATION_LOCK.md`
- Global combat / Ruin / status / full class Ability authority: `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md`
- Compatible Prime acquisition/progression/timing baseline: `docs/canon/AUDIT114_PRIME_COMBAT_ELEMENT_STATUS_AND_BASE_CLASS_NORMALIZATION_LOCK.md`
- Current 13-chapter reindex authority: `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`
- Chapter 10 story authority: `docs/canon/AUDIT112_CHAPTER_10_THE_LAST_BLANK_MIRENA_EASTERN_WAYFINDER_CALDER_AND_BURIED_REGISTRY_CLOSURE.md`
- Final surface-map / region authority: `docs/canon/AUDIT111_FINAL_WORLD_MAP_REGION_TERMINOLOGY_AND_VISUAL_AUTHORITY_CLOSURE.md`
- Travel / point-of-no-return authority: `docs/canon/AUDIT109_WORLD_MAP_ROAD_TRAVEL_AND_LAST_SHELTER_POINT_OF_NO_RETURN_CLOSURE.md`
- Compatible older item/equipment/economy baseline: `docs/canon/AUDIT106_ITEM_EQUIPMENT_CATALOG_ECONOMY_AND_AUDIT104_105_RECONCILIATION_LOCK.md`

---

# Conflict order for current work

1. **Audit117** controls equipment, Relics, Legacies, Forge components, donor equipment access, and the Subclass milestones explicitly changed there.
2. **Audit116** controls Standard-Card distribution/effects/MP, Prime Invocation MP, and promoted Prime command packages.
3. **Audit115** controls global damage/status/element/Ruin/class-Ability rules.
4. **Audit114** controls compatible Prime acquisition/progression/timing not changed by Audit116.
5. **Audit113** controls current chapter labels after the Chapter-10 insertion.
6. Compatible older domain locks remain active.

The historical cumulative item/equipment/Card tracker is design history, not authority by itself.

---

# Core combat / status baseline

Exactly four standard elements:

- Fire
- Ice
- Lightning
- Earth

Linked harmful statuses:

- Fire → Burn
- Ice → Freeze
- Lightning → Stun
- Earth → Staggered

Ruin is a special affinity/school, **not** a fifth standard element.

Universal harmful statuses are exactly:

- Burn
- Freeze
- Stun
- Staggered
- Bleed

Every harmful-status rider is explicit. Element/affinity does not automatically inflict its associated status.

Audit115 Bleed rule:

- 2% target Max HP when the affected unit successfully acts;
- maximum one Bleed proc per round;
- lost actions do not proc Bleed;
- any successful HP heal restoring at least 1 HP removes Bleed after the heal;
- Regen restoring at least 1 HP also removes Bleed.

Removed global systems must not return under renamed equivalents:

- Card Seals
- Rune-effect system
- Imprints
- Break/Stagger meter

---

# Standard Cards — current Audit116 guardrails

Exactly **24 Standard Cards**.

Current Face distribution:

- Might — **5**
- Elements — **5**
- Grace — **4**
- Acuity — **4**
- Change — **3**
- Ruin — **3**

Each permanent character may equip a maximum of **3 Standard Cards**.

Standard Cards:

- consume the user's normal selected action;
- are reusable after acquisition;
- cost MP;
- currently span **12–36 MP**;
- are not a charge/deck/draw/discard/duplicate/rank system.

Current lineups:

### Might
- Iron Testament
- Sunder the Gate
- Relentless Flurry
- March of Blades
- Sanguine Alloy

### Elements
- Cinder Judgment
- Winterglass Spear
- Thunder Chain
- Confluence Sigil
- Worldsplitter

### Grace
- Restoration
- Merciful Reprisal
- Wellspring
- Dawn Recall

### Acuity
- Faultline Sight
- Measured Response
- Predicted Impact
- Decisive Interval

### Change
- Burden Shift
- Reversal Engine
- Split Moment

### Ruin Face
- Calamity Lance
- Devouring Singularity
- Zero Hour

Important supersessions:

- Chosen Course → **Measured Response**.
- Glassform Rupture → **Burden Shift**.
- Spatial Guillotine → **Split Moment**.
- Sanguine Alloy is **Might**.
- Worldsplitter is **Elements / Earth**.
- Audit106's 4-per-Face Standard-Card matrix is superseded.

Four exact Card acquisition homes remain open in Audit116: Restoration, Cinder Judgment, Iron Testament, Sunder the Gate.

---

# Prime Card / manifestation framework — current Audit116 guardrails

Exactly **12 Prime Cards**:

- 6 Story Primes
- 6 Major-Hunt Primes

Progression is exactly:

> **Recovered → Awakened**

Awakened is final. There is no Concordant, Prime XP, Prime levels, duplicate-upgrade system, or Prime-upgrade material system.

Recovered Story Prime:
- one strong manifestation action in the current ordinary round;
- then dismisses.

Awakened Prime:
- replaces/suspends the active ordinary party;
- exactly **3 Prime rounds**;
- one selected Prime command per Prime round;
- frozen/off-field party state does not tick or become targetable unless a return/handoff effect explicitly resolves;
- after dismissal: **3 full normal-round shared Prime cooldown**;
- once per Prime identity per battle / genuine fresh-HP boss form;
- a genuine fresh-HP boss form refreshes that identity's use/cooldown.

Current Invocation MP:

- Recovered Story Prime — **60 MP**
- Awakened Story Prime — **75 MP**
- Awakened Major-Hunt Prime — **75 MP**
- manifested Prime commands — **0 additional MP**

Prime Invocation must remain a **severe MP commitment**. Old 0-MP Invocation and intermediate 40/48 values are superseded.

### Story Primes
- Last Sentinel — Might — Cyanis
- Last Cartographer — Acuity — Torren
- Last Convergence — Elements — Vaelira
- Last Scribe — Change — Nimera
- Last Sanctuary — Grace — Ilyra
- Last Erasure — Ruin — Seyrik

`Last Measure` remains superseded.

### Major-Hunt Primes
- Dawn Shepherd — Grace — Ashen Whitehorn
- Oathbound Colossus — Might — Crownless Siege Marshal / Crownless War Engine
- Living Revision — Change — Concordance Guardian
- Prismatic Leviathan — Elements — Worldscar Leviathan
- Parallax Host — Acuity — Final Archive Arbiter
- Starfall Engine — Ruin — The Unfinished World / Worldheart

`Sheltering Host` remains superseded.

Current Major-Hunt Prime structural notes:

- no current Major-Hunt Prime requires a standalone passive;
- Living Revision Continuance has no healing;
- Prismatic Leviathan has no passive, heal command, or Colorless offense;
- Adaptive Scales is removed;
- Prismatic Repair/Tidal Repair is removed;
- Cryostatic Sanctuary is replaced by Prismatic Mantle;
- Sixfold Deluge is replaced by Prismatic Deluge;
- overlap among thematically related Prime commands is allowed and is not itself a redesign requirement.

Exact command tables are controlled by Audit116.

---

# Ruin formula scope

Audit115 controls **character Ability** Ruin damage as:

> Hybrid / Ruin — 75% Attack / 25% Magic

Prime commands are a separate command class. Audit116's individually authored Prime formulas are controlling for Last Erasure and Starfall Engine and are **not** silently rewritten to the character-Ability 75/25 formula.

---

# Current classes / equipment identity guardrail — Audit117

Permanent six:

- Cyanis — **Crest Knight / Crest Magus**
- Ilyra — **Blue Warden / Vowblade**
- Torren — **War Archer / Routeweaver**
- Nimera — **Cardweaver / Sixfold Knight**
- Vaelira — **Prism Archer / Green Arcanist**
- Seyrik — **Ruin Vanguard / Ruin Healer**

Base and Subclass caps are both **CL13**.

Current Subclass milestones:

- CL1 — donor Primary + first Subclass ability + Trait I
- CL3 — Subclass Mastery 1 eligibility + donor Armor
- CL4 — new Subclass ability
- CL5 — Subclass Mastery 2 eligibility + donor Secondary where applicable
- CL6 — Trait II
- CL7 — Subclass Mastery 3 eligibility + new ability + **donor Relic access**
- CL9 — new ability
- CL10 — **new ability**
- CL11 — **Subclass Mastery 4 eligibility + donor Legacy access**
- CL12 — Trait III
- CL13 — Subclass Ultimate + cap

**Synthesis is removed.** Do not implement a Synthesis node, Synthesis MP, Synthesis passive, or Base-CL13/Subclass-CL13 Synthesis eligibility gate.

Ilyra's primary weapon family remains **Wardrods**; Shield and Focus are Secondary options. No sword assumption returns.

Important slot rules:

- Torren Great Bow = Weapon + Secondary.
- Vaelira Arcane Staff = one-slot Primary and may pair with Focus.
- Seyrik Two-Handed Sword = Weapon + Secondary.
- Nimera ordinary / surviving Relic Conduits = one-slot.
- Nimera native Legacy Conduit = **Weapon + Secondary**.

---

# Current equipment / Relic / Legacy guardrail — Audit117

Current active equipment count is **91**:

- **38 ordinary** — 16 Weapons / 15 Armors / 4 Shields / 3 Foci
- **36 Relics**
- **17 native Legacies**

All 12 Subclass Relics are removed. The six separate shared-Legacy artifacts are removed.

Linked donor access uses the **existing obtained item**, not a duplicate shared artifact:

- Subclass CL7 → linked donor's obtained Relics
- Subclass CL11 → linked donor's obtained native Legacies

Native owners never need donor permission for their own equipment.

Native Legacy completion requires:

- Base CL13
- all 4 Core Masteries
- Character Quest / resolution
- unique Character Quest Legacy Component
- unique Legacy precursor
- Gate A material
- Gate B material
- Kessara project availability

Gate A releases the Legacy weapon. Gate B releases the rest of the package.

Forge economy:

- 5 Face components per Face / 30 total
- 2 Legacy-gate-specific per Face / 12 total
- 3 Relic-copy-specific per Face / 18 total
- Legacy-gate and Relic-copy variants are non-interchangeable

Relic-copy forging:

- original Relic must already be obtained;
- one matching-Face copy component creates one identical extra copy;
- max quantity per Relic = 2;
- Legacies remain unique.

Equipment power hierarchy:

> **Ordinary < Relic < Legacy**

Legacies should generally sit modestly above Relics in broad raw power and may carry explicit capstone perks such as **Max HP, Max MP, Accuracy, and Evasion**. Exact 17-piece Legacy numerical values/perk assignments remain pending approval and are not yet master-canon numbers.

Final Relic / Legacy / Legacy-Component names remain deferred until dialogue is substantially more complete.

---

# Current chapter-number firewall

The game has **13 chapters** after insertion of Chapter 10 — The Last Blank.

Late spine:

- Ch9 — Larkspire / Crownfall / Rhazek.
- Ch10 — The Last Blank.
- Ch11 — Crown Engine / Calder / Custodian / Truth.
- Ch12 — The Reforged March / final Black Host campaign / Vaelkor / cleanup.
- Ch13 — The Last Command / final Ancient domain / Last Shelter / Final Severance / ending.

Old references where Chapter 10=Crown Engine, Chapter 11=Vaelkor campaign, or Chapter 12=final domain are stale.

Last Shelter remains the true irreversible point of no return under Audit109.

---

# Current map / region firewall

Audit111 remains the final surface-world visual/terminology authority where compatible.

Current macro-region terminology includes:

- **BLACK HOST TERRITORY**
- **THE WESTWAYS**
- **THE GREYSPIRES**
- **YAHTRENHOLD**

The Blackspine remains the canonical mountain-range/frontier name even though its label is intentionally omitted on the final approved map.

Westguard is the current proper name replacing Westreach / Yahtrens Stand for the same locked location.

Surface macro geography is closed unless explicitly reopened.

---

# Open production / balance frontier after Audit117

Immediate unresolved / deferred items include:

1. Approve or revise the exact **17-Legacy raw-stat + HP/MP/Accuracy/Evasion perk package**; Audit117 promotes only the tier direction, not the pending numbers.
2. Resolve the global **Accuracy vs Evasion** hit-resolution formula.
3. Resolve the universal **Critical-hit multiplier / resolution order** where still open.
4. Revalidate the **Level-70 EXP / expected chapter-level scaffold**, natural character growth, enemy/boss progression, and current Ch1–13 encounter calibration in the dedicated progression pass.
5. Resolve exact Prismatic Deluge Power / Prime resistance values and the four still-open Standard-Card acquisition homes under Audit116 where applicable.
6. Finalize remaining Forge-component / Legacy-precursor presentation details and Kessara Relic-copy service implementation/economy details.
7. Complete remaining Consumable/shop/economy reconciliation and final currency denomination.
8. Keep final Relic / Legacy / Legacy-Component naming deferred until dialogue is substantially more complete.
9. Implement and regression-test promoted Card/Prime/equipment/progression data.

Omission from this summary does not erase compatible older canon. **Audit117, Audit116, Audit115, Audit114, Audit113, Audit112, Audit111, Audit109, Audit107, Audit106, Audit105, Audit104, Audit103, compatible prior canon, exact visual authorities, and newer explicit user-approved corrections control conflicts.**
