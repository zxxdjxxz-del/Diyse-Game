# Diyse — Active Engineering Canon Guardrails

This file is an implementation-facing authority index and compact guardrail summary. It does **not** replace the canon audits. If it omits a compatible older lock, that lock remains active. If it conflicts with a later master audit or explicit approved correction, the later authority wins.

## Current whole-project authority

**Diyse: HD-2D JRPG Clean Active Complete Master Canon v2.01 / Audit116 — Standard Card, Prime Resource, and Prime Command Reconciliation Lock**  
**Date:** August 25, 2026

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

Current domain pointers:

- Card / Prime economy + command authority: `docs/canon/AUDIT116_STANDARD_CARD_PRIME_RESOURCE_AND_COMMAND_RECONCILIATION_LOCK.md`
- Global combat / Ruin / status / full class Ability authority: `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md`
- Compatible Prime acquisition/progression/timing baseline: `docs/canon/AUDIT114_PRIME_COMBAT_ELEMENT_STATUS_AND_BASE_CLASS_NORMALIZATION_LOCK.md`
- Current 13-chapter reindex authority: `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`
- Chapter 10 story authority: `docs/canon/AUDIT112_CHAPTER_10_THE_LAST_BLANK_MIRENA_EASTERN_WAYFINDER_CALDER_AND_BURIED_REGISTRY_CLOSURE.md`
- Final surface-map / region authority: `docs/canon/AUDIT111_FINAL_WORLD_MAP_REGION_TERMINOLOGY_AND_VISUAL_AUTHORITY_CLOSURE.md`
- Travel / point-of-no-return authority: `docs/canon/AUDIT109_WORLD_MAP_ROAD_TRAVEL_AND_LAST_SHELTER_POINT_OF_NO_RETURN_CLOSURE.md`
- Item/equipment/economy architecture: `docs/canon/AUDIT106_ITEM_EQUIPMENT_CATALOG_ECONOMY_AND_AUDIT104_105_RECONCILIATION_LOCK.md`

---

# Conflict order for current combat/Card/Prime work

1. **Audit116** controls Standard-Card distribution/effects/MP, Prime Invocation MP, and the Prime command packages explicitly promoted there.
2. **Audit115** controls global damage/status/element/Ruin/class-Ability rules.
3. **Audit114** controls compatible Prime acquisition/progression/timing not changed by Audit116.
4. **Audit113** controls current chapter labels after the Chapter-10 insertion.
5. Compatible older domain locks remain active.

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

# Current classes / equipment identity guardrail

Audit115 plus compatible Audit104/106 equipment authority remain active.

Permanent six:

- Cyanis — Crest Knight / Crest Arcanist
- Ilyra — Blue Warden / Vowblade
- Torren — War Archer / Routeweaver
- Nimera — Cardweaver / Truthshot
- Vaelira — Green Arcanist / Axiomblade
- Seyrik — Ruin Vanguard / Ruin Warden

Ilyra's primary weapon family remains **Wardrods**; Shield and Focus are Secondary options under current equipment legality. No sword assumption returns.

Open equipment / persistent unlocked-family access remains governed by current Audit104/106 rules.

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

# Open production / balance frontier after Audit116

Immediate dependency order:

1. Revalidate the **Level-70 EXP / expected chapter-level scaffold**.
2. Revalidate natural character stat growth.
3. Revalidate enemy/boss stat progression.
4. Finalize character/Prime numerical stat arrays.
5. Certify Ability/Card/Prime numerical power and MP against the Level-70 curve.
6. Resolve exact Prismatic Deluge Power and Prime Status-Resistance/susceptibility values.
7. Resolve the four still-open Standard-Card acquisition homes.
8. Complete Audit106 deferred equipment numerical work: ordinary baselines, Relic normalization, Legacy numbers, Capstone-Relic homes, Forge counts, and the 118-piece power curve.
9. Implement and regression-test the promoted Card/Prime data.

Omission from this summary does not erase compatible older canon. **Audit116, Audit115, Audit114, Audit113, Audit112, Audit111, Audit109, Audit107, Audit106, Audit105, Audit104, Audit103, compatible prior canon, exact visual authorities, and newer explicit user-approved corrections control conflicts.**
