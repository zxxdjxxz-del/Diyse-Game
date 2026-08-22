# Diyse — Active Engineering Canon Guardrails

This is an implementation-facing summary. It does **not** replace the authoritative Complete Master Canon or newer explicit user corrections. If this summary conflicts with a later canon artifact, the later authority wins.

## Current whole-project authority

**Diyse: HD-2D JRPG Clean Active Complete Master Canon v1.91 / Audit106 — Item, Equipment, Catalog, Economy, and Audit104/105 Reconciliation Lock**  
**Date:** August 22, 2026

Immediate forward chain:
- **v1.84 / Audit99** — Random-Encounter Runtime Implementation and Production-Readiness Closure.
- **v1.85 / Audit100** — Enemy Asset Reuse and Palette-Swap Production Efficiency Lock.
- **v1.86 / Audit101** — Major Hunt Architecture and Unlock Closure.
- **v1.87 / Audit102** — Major Hunt Difficulty and Progression Balance Closure.
- **v1.88 / Audit103** — Quest Architecture, Character Quest and Ordinary Side-Quest Closure.
- **v1.89 / Audit104** — Reciprocal Class, Synthesis, Legacy, and Legacy-Component Integration Lock.
- **v1.90 / Audit105** — Acuity Face, Story Prime, and Resource Reconciliation Lock.
- **v1.91 / Audit106** — Item, Equipment, Catalog, Economy, and Audit104/105 Reconciliation Lock.

Current item/equipment/economy canon file:
- `docs/canon/AUDIT106_ITEM_EQUIPMENT_CATALOG_ECONOMY_AND_AUDIT104_105_RECONCILIATION_LOCK.md`

Current Acuity/reconciliation canon file:
- `docs/canon/AUDIT105_ACUITY_FACE_STORY_PRIME_AND_RESOURCE_RECONCILIATION_LOCK.md`

Current class/Synthesis/Legacy canon file:
- `docs/canon/AUDIT104_RECIPROCAL_CLASS_SYNTHESIS_LEGACY_AND_LEGACY_COMPONENT_INTEGRATION_LOCK.md`

Legacy Component reconciliation authority:
- `docs/LEGACY_COMPONENT_AND_SECURED_RELEASE_RECONCILIATION_2026-08-22.md`

Quest terminology clarification:
- `docs/canon/REGIONAL_SIDE_QUEST_TERMINOLOGY_CLARIFICATION_2026-08-22.md`

---

## Project foundation

- Diyse is an **HD-2D JRPG**.
- Field sprites target approximately **80 px**; battle sprites approximately **200–220 px**; dialogue uses large high-resolution portraits.
- Standard combat frame: up to four active party members staggered left, enemies right, open center action/VFX lane.
- Target runtime: approximately **25 hours**.
- Permanent roster: exactly six; maximum active battle party: four.
- Dialogue is one authored continuity; no dialogue wheel, morality route, affinity-response system, romance route/system, or selectable protagonist personality.
- **Current player level cap: 70.**
- CL13 is the Base/Subclass class-level cap and does not replace the player-level cap.

---

## Audit106 item / equipment authority — controlling

### Catalog counts
- Consumables: **20**.
- Ordinary Weapons: **27**.
- Ordinary Armor: **12**.
- Ordinary Secondaries: **9**.
- Ordinary Equipment: **48**.
- Relics: **64** after Audit104 reconciliation.
- Legacies: **6**.
- Exceptional Equipment: **70**.
- Total Equipment: **118**.
- Consumables + Equipment practical catalog: **138**.
- Standard Cards: **24**.
- Prime Cards: **12** under Prime canon.
- General Accessories: **0**.

### Level-70 reconciliation
All old item-audit language built around an absolute Level-60 cap is superseded. The late Relic expansion remains valid as catalog/progression architecture, but final raw stats must be tuned against the **Level-70 EXP and natural-stat curve**.

Do not lock exact equipment raw stats before:
1. Level-70 EXP rebalance;
2. natural character-stat revalidation;
3. enemy/boss stat revalidation.

### Inventory taxonomy
Player-facing inventory:
- Consumables
- Equipment: Weapons / Secondaries / Armor
- Forge Components
- Project Items
- Key Items

Cards remain outside ordinary inventory.

### Equipment slots / geometry
Functional slots:
- Weapon
- Secondary
- Armor

Base weapon families:
- Cyanis — Swords
- Ilyra — Wardrods
- Torren — Great Bows
- Nimera — Conduits
- Vaelira — Arcane Staffs
- Seyrik — Two-Handed Swords

Important geometry:
- Torren Great Bows = Weapon + Secondary.
- Seyrik Two-Handed Swords = Weapon + Secondary.
- Cyanis Swords are one-handed; Secondary may be Shield or second Sword where legal.
- Ilyra Wardrods are one-handed; Secondary may be Shield or Focus where legal.
- Listed ordinary Cardweaver Conduits are one-slot.
- Audit104 permits authored advanced/two-handed Conduits; any such item must explicitly consume Weapon + Secondary.
- Cardweaver Legacy alias `Decisive Record` remains one-slot.

Once equipment access is legally unlocked, it persists under Audit104 open-equipment rules.

### Armor profiles
- Cyanis — Heavy / Heavy Physical DEF / Medium Magic DEF.
- Ilyra — Medium classification / **Light-tier Physical DEF / Medium-tier Magic DEF**.
- Torren — Medium / Medium Physical DEF / Light Magic DEF.
- Nimera — Light Ritual / Light Physical DEF / Medium Magic DEF.
- Vaelira — Light caster / Light Physical DEF / Heavy Magic DEF.
- Seyrik — Heavy/Battle / Heavy Physical DEF / Light Magic DEF.

Never normalize Ilyra's Physical DEF upward merely because the armor-class label is Medium.

### Consumables — exactly 20
HP:
- Field Salve
- Restorative Salve
- Vital Salve
- Company Salve

MP:
- Flow Tonic
- Deepflow Tonic
- Reservoir Tonic

Revival:
- Rousing Salts
- Greater Rousing Salts

Status:
- [Status-A] Remedy — exact display name pending existing-status label pass
- [Status-B] Remedy — exact display name pending
- General Remedy
- Full Remedy

Tactical:
- Smoke Cord
- Ward Seal
- Null Powder
- Breach Charge
- Balance Seal

Exceptional:
- Emergency Kit
- Emergency Rally

Battle items consume a normal action. No elemental-bomb ladder, generic damage-item ladder, consumable Cards, Prime-copy items, stat seeds, or boss-bypass consumables. MP restoration remains scarcer than HP restoration.

### Ordinary equipment — 48
Weapons — 27:
- Cyanis: Crestblade; Brackensteel; Ivory Sword; Forgeblade; Reach Saber.
- Ilyra: Wardrod; Blue Wardrod; Ivory Wardrod; Forge Wardrod; Sanctuary Wardrod.
- Torren: Yahtrean War Bow; Redwater War Bow; Ivory Longbow; Storm War Bow; Farreach Bow.
- Nimera: Twin Token; Index Tablet; Clearing Bell; Farroad Needle; Branch Codex.
- Vaelira: Arcanist Staff; **Deepforge Battlestaff**; Storm Staff; Waystaff.
- Seyrik: Ruin Vanguard Sword; Fieldbreaker; Breachblade.

Armor — 12:
- Cyanis: Crest Plate; Caeloran Plate.
- Ilyra: Blue Warden Mail; High Warden Mail.
- Torren: War Archer Gear; Campaign Mail.
- Nimera: Cardweaver Garb; Weaver Coat.
- Vaelira: Green Arcanist Garb; Arcanist Weave.
- Seyrik: Ruin Vanguard Plate; Breach Plate.

Secondaries — 9:
- Shields: Yahtrean Shield; Tower Shield; Warding Shield; Skirmisher Shield; War Shield.
- Foci: Focus; Warding Focus; Battle Focus; Swift Focus.

`Highland Battlestaff` and `Highland Arcanist Coat` are retired. **Deepforge Battlestaff** is approved.

### Ordinary economy
- Ordinary equipment resells for **50%** of registered purchase/replacement value, rounded down.
- Ordinary equipment becomes repurchasable after first obtain; Cresthaven requisition/fail-safe access prevents permanent loss when original sources close.
- Player expectation is roughly one meaningful ordinary equipment purchase plus routine restock/checkpoint spending, not buying every upgrade.
- Field Salve = 1.0 relative economy unit for current tuning.

### Exceptional structure
Audit106 reconciles the obsolete 17-Legacy working branch against Audit104's locked six-Legacy architecture:
- **64 Relics** total.
- **6 Legacies** total.
- **70 exceptional pieces** total.

The 64 Relics comprise:
- 36 Base Relic Weapons/Armors
- 12 Subclass Relic Weapons/Armors
- 5 Relic Secondaries
- 11 Capstone Relics reclassified from the obsolete extra-Legacy working branch

The six Legacy-rarity items remain the Audit104 one-per-Base-tradition Synthesis Legacies.

### Six final Legacies: technical aliases + player-facing titles
Audit104 identity aliases remain valid technical/cross-reference names so existing Character-Quest/Component files remain understandable. Audit106 locks the final player-facing titles:
- Crest Knight / `Stillpoint Aegis` → **That Was Dumb.** — Shield.
- Green Arcanist / `Living Prism` → **That Saves Me the Trouble.** — Focus.
- Blue Warden / `Mercy's Boundary` → **Try Me Instead.** — Shield.
- Ruin Vanguard / `Purposebound` → **You Are Finished.** — Two-Handed Sword.
- War Archer / `Known Ground` → **Should've Moved.** — Great Bow.
- Cardweaver / `Decisive Record` → **Good Fuck, Definitely. Good Fuck.** — one-slot Conduit.

Character Quest Legacy Component → secured Cresthaven release remains controlled by Audit104. The six Legacies remain optional endgame equipment.

### Capstone Relics — 11
Reclassified from the obsolete extra-Legacy branch; they remain active item designs but are **Relics**, not Legacies:
- Cyanis: **Move or I Move You.** — Sword; **That Didn't Do Shit.** — Armor.
- Ilyra: **I Said Enough.** — Wardrod; **Breathe. I've Got You.** — Focus; **Move. I've Got This.** — Armor.
- Torren: **Figured You'd Come This Way.** — Armor.
- Nimera: **Hold On. That's Useful.** — Focus; **Fuck It. New Plan.** — Armor.
- Vaelira: **There's Your Problem.** — Arcane Staff; **Oh, I Can Use That.** — Armor.
- Seyrik: **You Should Have Killed Me.** — Armor.

Exact acquisition homes for these eleven must be reconciled before implementation; they do not use the six Character-Quest Legacy Component release chain.

### Relic Secondary names / Hunt routing
- RH7 Rift Gate Colossus → **No Further** — Physical Bastion Shield.
- RH8 Rift Siege Beast → **Glass Hunger** — Offensive Channel Focus.
- RH9 Mercyfallen Behemoth → **Second Spring** — Restorative Channel Focus.
- RH10 Authority Remnant → **One Breath Ahead** — Control/Tempo Focus.
- RH11 Throne of Emperor Vaelkor → **The Quiet Gate** — Warding Bastion Shield.

### Kessara / Forge reconciliation
Kessara remains a small authored project system, not recipe spam.

Current Forge Component names:
- Might — Creststeel Billet
- Elements — Prismglass Plate
- Grace — Warding Silver Coil
- Acuity — Calibration Gearset
- Change — Pattern Crystal
- Ruin — Black Ore Segment

`Regulator Gearset` is superseded.

The older generic `Legacy Gate A/B` Forge-component uses are superseded by Audit104's fixed Character-Quest Component → secured-Legacy release. The old 5-obtainable/4-required-per-Face material schedule must be revalidated before implementation.

Kessara's 12 authored Relic-project concept remains valid:
- 6 Base Relic projects
- 6 Subclass Relic projects

Do not expand that into a broad grind system.

### Standard Cards — 24 / chapter pacing
Exactly four Standard Cards per Face, 24 total.

Current chapter acquisition curve:
- Ch1: **2** — Faultline Sight; Iron Testament.
- Ch2: **2** — Restoration; Sunder the Gate.
- Ch3: **3** — Glassform Rupture; Reversal Engine; Merciful Reprisal.
- Ch4: **3** — Cinder Judgment; Relentless Flurry; March of Blades.
- Ch5: **2** — Chosen Course; Dawn Recall.
- Ch6: **4** — Winterglass Spear; Thunder Chain; Calamity Lance; Sanguine Alloy.
- Ch7: **1** — Spatial Guillotine.
- Ch8: **1** — Confluence Sigil.
- Ch9: **2** — Wellspring; Predicted Impact.
- Ch10: **3** — Devouring Singularity; Worldsplitter; Decisive Interval.
- Ch11: **1** — Zero Hour.

Audit105 remains controlling for the four Acuity Cards and their exact sources.

Full exact item names, roles, source details, economy ratios, production data schema, and reconciliation notes are in Audit106.

---

## Audit105 Acuity authority — controlling where Audit106 does not supersede item-facing presentation

### Six Faces
- Might
- Elements
- Grace
- **Acuity**
- Change
- Ruin

Acuity supersedes Resource/Finesse as the Face name and retains Gold as Face color unless separately revised.

Acuity centers on perception, judgment, precision, situational awareness, timing, anticipation, route/position assessment, rapid decision-making, and efficient execution.

Core shorthand:
- **Acuity turns uncertainty into a path.**
- **See → Decide → Place → Act.**

There is no dedicated Face-symbol/icon system; use neutral Face markings/notation wording.

Torren's Base class **War Archer** is Acuity-aligned. Torren's Subclass **Routeweaver** remains a **Change Face** class.

### Story Primes
- Might — Last Sentinel
- Elements — Last Convergence
- Grace — Last Sanctuary
- Acuity — Last Cartographer
- Change — Last Scribe
- Ruin — Last Erasure

Last Cartographer sees/maps the route; Last Scribe changes/rewrites the route.

### Acuity Standard Cards
- Faultline Sight — Hollow Watch Castellan first clear.
- Chosen Course — Deepforge Colossus first clear.
- Predicted Impact — RH9 Mercyfallen Behemoth first clear.
- Decisive Interval — MH5 Final Archive Arbiter first clear.

Former Resource cards Bastion Reserve, Stormglass Relay, Prismatic Reserve, and Lifeward Transfer are superseded.

### Acuity optional Prime
**Parallax Host** supersedes Sheltering Host.

Current optional Prime lineup:
- Might — Oathbound Colossus
- Elements — Prismatic Leviathan
- Grace — Dawn Shepherd
- Acuity — Parallax Host
- Change — Living Revision
- Ruin — Starfall Engine

### Final Severance order
1. Last Sentinel / Might — HOLD
2. Last Convergence / Elements — DISTINGUISH
3. Last Cartographer / Acuity — MAP
4. Last Sanctuary / Grace — PRESERVE
5. Last Scribe / Change — CONTAIN
6. Last Erasure / Ruin — END

---

## Audit103 quest architecture — inherited

- Exactly 6 standalone Character Quests, one per permanent party member.
- Exactly 3 Character Quest bosses: Elemental Forecast Construct, Crest Load Warden, Revision Custodian.
- Exactly 10 ordinary non-story/non-Hunt side quests; these are the regional side-quest layer, not a separate quest category.
- Each Character Quest grants that character's Legacy Component as principal mechanical reward.
- Character Quests remain optional and available until the Chapter-12 point of no return unless later canon says otherwise.

Character Quests:
1. Vaelira — The Sky No One Chose.
2. Cyanis — The Weight of the Crest.
3. Nimera — The Archive That Remembers.
4. Seyrik — The Name That Remains.
5. Ilyra — Mercy Has a Voice.
6. Torren — The Road That Returns.

Hunts remain separate combat-oriented optional content.

---

## Audit104 reciprocal class / Synthesis authority — inherited

### Sixfold Volition
Formal term: **The Sixfold Volition**. `Sixfold Accord` is deprecated.

Reciprocal pairs:
- Cyanis ⇄ Vaelira
- Ilyra ⇄ Seyrik
- Torren ⇄ Nimera

### CL13 architecture
Base Class cap = CL13. Subclass cap = CL13. Base/Subclass CEXP are separate.

Thresholds:
- CL1 0
- CL2 150
- CL3 350
- CL4 600
- CL5 950
- CL6 1350
- CL7 1800
- CL8 2300
- CL9 2850
- CL10 3450
- CL11 4150
- CL12 4950
- CL13 6000

### Global Ability weapon rule
No Ability or Ultimate requires a particular equipped weapon. Equipment still controls ordinary Attack, stats, slot geometry, Relic/Legacy legality, and presentation.

### Current Base/Subclass identities
- Cyanis — Crest Knight / Crest Arcanist
- Vaelira — Green Arcanist / Axiomblade
- Ilyra — Blue Warden / Vowblade
- Seyrik — Ruin Vanguard / Ruin Warden
- Torren — War Archer / Routeweaver
- Nimera — Cardweaver / Truthshot

Key formula locks:
- Vowblade damaging Abilities = 50% Attack / 50% Spirit Hybrid.
- Ruin Warden Siphon Rune = one hit, 60% Attack / 40% Magic Hybrid.
- Routeweaver damaging Abilities = 50% Attack / 50% Magic Hybrid.

### Mastery / Synthesis
Mastery architecture = 4 Core + 4 Subclass + 1 Synthesis, each costing 1 MP.

Equipment Mastery = Subclass Mastery Node 4 at Subclass CL10 and grants donor Relic access.

Synthesis eligibility:
Base CL13 + Subclass CL13 + all four Core Masteries + all four Subclass Masteries + authored resolution/integration requirement + 1 unspent MP.

Synthesis names:
- Cyanis — Unified Crest
- Vaelira — Unified Spectrum
- Ilyra — Mercy Unbroken
- Seyrik — Tempered Ruin
- Torren — Measured Passage
- Nimera — Living Proof

Mandatory late-Ch11 Synthesis-resolution beats:
- Cyanis ⇄ Vaelira — What Holds, What Changes — Cresthaven.
- Ilyra ⇄ Seyrik — Keep Them Alive — Forward Hub recovery area.
- Torren ⇄ Nimera — Enough to Move — Forward Hub operations/map table.

The six Character Quest Legacy Components and Chapter-12 secured-release flow remain controlled by Audit104; Audit106 changes only player-facing Legacy titles and item/economy reconciliation where explicitly stated.

---

## Audit99 random-encounter/runtime authority — inherited where compatible

Compatible rules remain active, including:
- random encounters use hidden eligible-movement-distance pressure;
- pressure is fed by actual resolved horizontal displacement after collision resolution;
- standing still, wall-pushing with zero displacement, vertical-only displacement, and movement-disabled displacement do not count;
- menus/cutscenes/dialogue/authored pauses suspend pressure;
- maximum **8 simultaneously active enemies**;
- exact immediate formation repeats are suppressed where alternatives exist;
- transient random-encounter handoff is not serialized into saves;
- area tuning retains same-ecology / new-ecology / safe-reset semantics.

Any older absolute Level-60 progression references are superseded by Level 70.

---

## World / map authority

The exact approved Yahtrea map remains the controlling surface-world visual/spatial master. Do not move, regenerate, reinterpret, simplify, add, remove, or reconnect geography unless explicitly approved.

Formal modern Realms:
- **The Westways** — west; supersedes Edgelands.
- **The Greyspires** — northern mountain region; supersedes Diysereach/Highlands as current region terminology.
- **The Crownhold** — capital/royal-core region; supersedes Southhold.

Settlement and landmark names remain unchanged by those regional terminology corrections.

---

## Immediate open work after Audit106

1. Rebalance / verify the **Level-70 EXP curve** and chapter-end expected levels.
2. Revalidate natural character stat growth at Level 70 progression.
3. Revalidate enemy/boss stat curves.
4. Lock final ordinary-equipment raw-stat baselines.
5. Normalize all 64 Relics, including 11 Capstone Relics, against those baselines.
6. Lock final numerical stats/passives for the six Legacies.
7. Reconcile exact acquisition homes for the 11 Capstone Relics.
8. Reconcile Kessara Forge-Component pickup/use counts after removal of generic Legacy Gate A/B uses.
9. Run the full **118-piece equipment power-curve audit** across Chapters 1–12.
10. Finalize Core Mastery effect text / gate schedule and other still-open class-system constants from Audit104.
11. Continue Audit105 downstream Acuity implementation where runtime data remains unfinished.
12. Integrate Synthesis-resolution beats into final Chapter-11 scene numbering/dialogue.
13. Run implementation/data regression across class, equipment, Mastery, Synthesis, Legacy, Card, Prime, Hunt, reward, and save data.

Omission from this summary does not erase compatible older canon. **Audit106, Audit105, Audit104, Audit103, compatible prior canon, exact visual authorities, and newer explicit user corrections control conflicts.**