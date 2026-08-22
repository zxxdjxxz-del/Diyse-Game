# Audit106 — Item, Equipment, Catalog, Economy, and Audit104/105 Reconciliation Lock

**Authority:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.91 / Audit106**  
**Date:** August 22, 2026  
**Status:** **LOCKED / CONTROLLING** for the item/equipment catalog architecture, consumable architecture, ordinary-equipment catalog, exceptional-equipment count and rarity structure, item economy, Standard-Card acquisition pacing where explicitly listed, and the Audit104/Audit105 reconciliation rules below.

Audit106 inherits all compatible **v1.90 / Audit105**, **v1.89 / Audit104**, **v1.88 / Audit103**, and earlier canon unless explicitly superseded or clarified below.

The pre-promotion repository `main` head checked immediately before this promotion was:
- `1d4ad5f468b84ce2d38dab5141e54bb170dd2967`

---

## 0. Reconciliation contract

This audit promotes the current item/equipment work without regressing newer whole-project canon.

### Player-level authority
- **Player level cap remains 70.**
- Any item-audit language that justified late equipment specifically because the cap had moved from 50 to 60 is **SUPERSEDED / HISTORICAL**.
- The late Relic expansion remains valid as equipment-density architecture, but final raw stats must be tuned against the **Level-70** EXP/stat curve.
- Exact raw Attack/Magic/DEF/Magic DEF/Spirit/Speed values are **not locked by Audit106** and must wait until the Level-70 EXP rebalance and natural-stat curve are revalidated.

### Current class names control item references
Use the Audit104 names:
- Cyanis — **Crest Knight / Crest Arcanist**
- Vaelira — **Green Arcanist / Axiomblade**
- Ilyra — **Blue Warden / Vowblade**
- Seyrik — **Ruin Vanguard / Ruin Warden**
- Torren — **War Archer / Routeweaver**
- Nimera — **Cardweaver / Truthshot**

The item-audit labels `Crest Magus`, `Prism Archer`, `Sixfold Knight`, and `Ruin Healer` are superseded wherever they appeared only as stale Subclass names.

### Six-Legacy authority from Audit104 remains controlling
Audit104 locked exactly **six Synthesis Legacies**, one per Base tradition. Audit106 does **not** restore the superseded 17-Legacy architecture as 17 Legacy-rarity items.

To preserve the approved item-design work without contradicting Audit104:
- the six Audit104 Legacy identities remain the only **Legacy-rarity** items;
- eleven additional voice-first capstone items developed in the item audit are reclassified as **Capstone Relics**;
- the exceptional-equipment total therefore remains **70** rather than discarding those eleven designs.

This produces:
- **64 Relics**
- **6 Legacies**
- **70 exceptional equipment pieces**

Ordinary equipment remains **48**, so the full equipment catalog remains:
- **118 total equipment pieces**

---

## 1. Player-facing item taxonomy

Player-facing inventory categories are:
1. **Consumables**
2. **Equipment**
   - Weapons
   - Secondaries
   - Armor
3. **Forge Components**
4. **Project Items**
5. **Key Items**

**Cards remain outside ordinary inventory.**

Rules:
- Consumables use a technical stack cap of **99** unless an individual item says otherwise.
- Forge Components are non-sellable, non-discardable, and not battle-usable.
- Project Items are unique authored objects, non-sellable and non-discardable.
- Registered Project Items may move into Kessara's Project Log rather than remaining as clutter in active inventory.
- Cards are unique unlocks, do not use quantity stacks, and are never sold or discarded.
- Standard Cards remain unlimited-use under their established Card rules.

Stable production IDs should survive display-name changes. Recommended prefixes remain:
- `CON_`
- `WPN_`
- `SEC_`
- `ARM_`
- `FORGE_`
- `PROJ_`
- `KEY_`
- `CARD_STD_`
- `CARD_PRM_`
- `KPROJ_`
- `PASS_`
- `LEGACY_`
- `EFFECT_`

Save data should persist stable IDs/flags, not display strings or derived values.

---

## 2. Consumables — exactly 20

The practical consumable catalog is exactly **20**.

### HP restoration — 4
1. **Field Salve** — basic single-target fixed HP restoration.
2. **Restorative Salve** — stronger single-target fixed HP restoration.
3. **Vital Salve** — major single-target fixed HP restoration.
4. **Company Salve** — active-party percentage HP restoration.

### MP restoration — 3
5. **Flow Tonic** — basic single-target fixed MP restoration.
6. **Deepflow Tonic** — stronger single-target fixed MP restoration.
7. **Reservoir Tonic** — major percentage MP restoration; not a normal-shop item.

### Revival — 2
8. **Rousing Salts** — revive one ally at low percentage max HP.
9. **Greater Rousing Salts** — revive one ally at a higher percentage max HP.

### Status treatment — 4
10. **[Status-A] Remedy** — dedicated treatment for one already-canon ordinary harmful-status family; exact display name remains pending the status-label pass.
11. **[Status-B] Remedy** — dedicated treatment for a second already-canon ordinary harmful-status family; exact display name remains pending.
12. **General Remedy** — removes one eligible ordinary removable harmful status.
13. **Full Remedy** — removes all eligible ordinary removable harmful statuses from one conscious ally, subject to protected/scripted exclusions.

### Tactical — 5
14. **Smoke Cord** — guaranteed escape from eligible ordinary random encounters only.
15. **Ward Seal** — grants an emergency Barrier to one ally using existing Barrier rules.
16. **Null Powder** — removes one eligible removable positive effect from an enemy.
17. **Breach Charge** — breaks or damages an eligible Barrier/Guard state under normal boss-protection rules.
18. **Balance Seal** — stabilizes eligible ordinary negative stat changes.

### Exceptional — 2
19. **Emergency Kit** — complete single-ally restorative: HP + MP plus eligible cleanse/stat restoration; does not revive.
20. **Emergency Rally** — revives all KO'd active-party members at low HP and provides substantial active-party HP recovery; no MP restoration or cleanse.

### Consumable rules
- Battle items consume the user's normal action.
- No elemental-bomb ladder.
- No generic fixed-damage consumable ladder.
- No consumable Cards.
- No Prime-copy consumables.
- No permanent stat-seed system.
- No boss-bypass items.
- MP recovery remains scarcer and more expensive than HP recovery.

### Availability
Regular core shop stock:
- Field Salve
- Restorative Salve
- Flow Tonic
- Rousing Salts
- [Status-A] Remedy
- [Status-B] Remedy
- General Remedy
- Smoke Cord

Later/specialist stock:
- Vital Salve
- Company Salve
- Deepflow Tonic
- Greater Rousing Salts
- Full Remedy
- Ward Seal
- Null Powder
- Breach Charge
- Balance Seal

Not normal-shop stock:
- Reservoir Tonic
- Emergency Kit
- Emergency Rally

Cresthaven consolidates normal consumable access after its Chapter-5 expansion. Reward-only exceptional consumables should remain non-sellable unless separately changed.

### Relative price anchors
Using **Field Salve = 1.0** economy unit:
- Field Salve 1.0
- Restorative Salve 2.5
- Vital Salve 6
- Company Salve 10
- Flow Tonic 4
- Deepflow Tonic 10
- Reservoir Tonic 18 equivalent reward value
- Rousing Salts 3
- Greater Rousing Salts 8
- each dedicated status Remedy 0.75
- General Remedy 2.5
- Full Remedy 7
- Smoke Cord 0.5
- Ward Seal 4
- Null Powder 3.5
- Breach Charge 5
- Balance Seal 3
- Emergency Kit 15 equivalent reward value
- Emergency Rally 25 equivalent reward value

Final currency denomination remains open.

---

## 3. Equipment slots and legality

Functional slots remain:
- **Weapon**
- **Secondary**
- **Armor**

Once an equipment family is legally unlocked, that access persists regardless of selected Base/Subclass under Audit104 open-equipment rules.

### Base weapon families
- Cyanis / Crest Knight — **Swords**
- Ilyra / Blue Warden — **Wardrods**
- Torren / War Archer — **Great Bows**
- Nimera / Cardweaver — **Conduits**
- Vaelira / Green Arcanist — **Arcane Staffs**
- Seyrik / Ruin Vanguard — **Two-Handed Swords**

### Slot geometry
- Cyanis Swords are one-handed; Secondary may be Shield or second Sword where legal.
- Ilyra Wardrods are one-handed; Secondary may be Shield or Focus where legal.
- Torren Great Bows consume **Weapon + Secondary**.
- Seyrik Two-Handed Swords consume **Weapon + Secondary**.
- Vaelira Arcane Staffs are one-slot unless an individual record says otherwise.
- Ordinary Cardweaver Conduits listed in this audit are one-slot.
- Audit104's advanced donor architecture may include **two-handed Conduits**; any such Conduit must explicitly consume Weapon + Secondary. Audit106 supersedes the older blanket claim that every possible Conduit in the game is one-handed.
- **Decisive Record** remains explicitly one-slot under Audit104.

No General Accessories family exists. Count remains **0**.

---

## 4. Armor profiles

Native armor identities remain:
- Cyanis — Heavy; Heavy Physical DEF / Medium Magic DEF.
- Ilyra — Medium classification; **Light-tier Physical DEF / Medium-tier Magic DEF**.
- Torren — Medium; Medium Physical DEF / Light Magic DEF.
- Nimera — Light Ritual; Light Physical DEF / Medium Magic DEF.
- Vaelira — Light caster; Light Physical DEF / Heavy Magic DEF.
- Seyrik — Heavy/Battle; Heavy Physical DEF / Light Magic DEF.

Ilyra's Medium classification must **not** be normalized upward to standard Medium physical defense.

---

## 5. Ordinary equipment — exactly 48

### 5.1 Ordinary Weapons — 27

#### Cyanis — Swords — 5
1. **Crestblade**
2. **Brackensteel**
3. **Ivory Sword**
4. **Forgeblade**
5. **Reach Saber**

#### Ilyra — Wardrods — 5
1. **Wardrod**
2. **Blue Wardrod**
3. **Ivory Wardrod**
4. **Forge Wardrod**
5. **Sanctuary Wardrod**

`Sanctuary Wardrod` is ordinary equipment and does not imply a direct connection to the Story Prime **Last Sanctuary**.

#### Torren — Great Bows — 5
1. **Yahtrean War Bow**
2. **Redwater War Bow**
3. **Ivory Longbow**
4. **Storm War Bow**
5. **Farreach Bow**

#### Nimera — Conduits — 5
1. **Twin Token**
2. **Index Tablet**
3. **Clearing Bell**
4. **Farroad Needle**
5. **Branch Codex**

Twin Token is the current display name for Nimera's starting twin-pattern Conduit concept.

#### Vaelira — Arcane Staffs — 4
1. **Arcanist Staff**
2. **Deepforge Battlestaff**
3. **Storm Staff**
4. **Waystaff**

**Deepforge Battlestaff** is approved. `Highland Battlestaff` is retired.

#### Seyrik — Two-Handed Swords — 3
1. **Ruin Vanguard Sword**
2. **Fieldbreaker**
3. **Breachblade**

### 5.2 Ordinary Armor — 12

#### Cyanis
- **Crest Plate**
- **Caeloran Plate**

#### Ilyra
- **Blue Warden Mail**
- **High Warden Mail**

`High Warden Mail` is an advanced institutional armor pattern, not a unique office/title artifact.

#### Torren
- **War Archer Gear**
- **Campaign Mail**

#### Nimera
- **Cardweaver Garb**
- **Weaver Coat**

#### Vaelira
- **Green Arcanist Garb**
- **Arcanist Weave**

`Highland Arcanist Coat` is retired.

#### Seyrik
- **Ruin Vanguard Plate**
- **Breach Plate**

### 5.3 Ordinary Secondaries — 9

#### Shields — 5
- **Yahtrean Shield**
- **Tower Shield**
- **Warding Shield**
- **Skirmisher Shield**
- **War Shield**

#### Foci — 4
- **Focus**
- **Warding Focus**
- **Battle Focus**
- **Swift Focus**

### 5.4 Ordinary source/economy rules
Ordinary equipment should remain repurchasable after first obtain, including through Cresthaven requisition/fail-safe access when an original source becomes unavailable.

Ordinary equipment resale value:
- **50%** of registered purchase/replacement value, rounded down.

Target purchase pressure:
- approximately one meaningful ordinary equipment purchase plus routine restock/checkpoint spending;
- players are not expected to buy every ordinary upgrade.

Working price bands remain:
- Weapons early 18–24; mid 32–45; advanced 55–75; final ordinary baseline 85–110.
- Two-handed weapons may sit approximately 10% above the same-tier one-handed midpoint.
- Armor early 14–20; mid 28–40; final ordinary if sold 50–65.
- Shields early 8–12; mid 18–28; advanced/final 35–50.
- Foci early 8–12; mid 20–30; advanced/final 38–55.

These are economy units relative to Field Salve = 1, not final currency denominations.

---

## 6. Ordinary income bands

Working encounter-income guidance remains:
- Ch1–2 ordinary random formation: 0.6–1 economy units.
- Ch3–5: 1.2–2.
- Ch6–8: 2.2–3.5.
- Ch9–11: 4–6.

Random encounters should supply roughly **40–50%** of routine spendable currency.

Elite guidance:
- early 4–8
- mid 8–16
- advanced 15–28
- late 25–45

Regional Hunt guidance:
- early 18–28
- mid 32–50
- advanced 50–75
- late 70–100

Major Hunt guidance:
- mid 55–85
- advanced 85–125
- late 120–170

If a Hunt grants a high-value permanent item/Prime/Relic/component, reduce raw-currency payout accordingly.

Chapter-level spendable-income guidance:
- early 25–45
- mid 55–90
- advanced 95–150
- late 140–220

Chapter 12 should remain strategically minor for routine economy because the final cleanup/preparation window is already established before the point of no return.

---

## 7. Relic architecture — 64 total after reconciliation

Audit106 recognizes three Relic groups:

1. **53 established Relics from the item audit**
   - 36 Base Relic Weapons/Armors
   - 12 Subclass Relic Weapons/Armors
   - 5 Relic Secondaries
2. **11 Capstone Relics** reclassified from the obsolete 17-Legacy working branch so that Audit104's six-Legacy lock remains intact.

Total Relics:
- **64**

### 7.1 Base Relic Weapons/Armors — 36
Each character has three native Base Relic Weapons and three native Base Relic Armors.

#### Cyanis
Weapons:
- **First Measure** — precision/tempo Sword.
- **Sun Through Iron** — hybrid Crest Sword.
- **War Canticle** — multi-target command Sword.

Armor:
- **Answering Plate** — reactive defense.
- **Marchlight** — mobile Heavy armor.
- **Veilforged Plate** — mixed-defense warded Heavy armor.

#### Ilyra
Weapons:
- **Quiet Rebuke** — control-reliability Wardrod.
- **Kindled Vow** — support-to-martial Wardrod.
- **Blue Censure** — guard/posture-break Wardrod.

Armor:
- **Weight of Mercy** — physical-defense compensation while preserving Ilyra's Light-tier Physical DEF baseline.
- **Blue Silence** — deep warding/status resistance.
- **The Second Answer** — emergency-response Warden mail.

#### Torren
Weapons:
- **One Good Line** — single-target precision Great Bow.
- **Falling Compass** — multi-target volley Great Bow.
- **Dead Reckoning** — anti-evasion/known-profile Great Bow.

Armor:
- **Clear Ground** — mobile accuracy.
- **Second Bearing** — miss/correction stability.
- **Return Mark** — observation/counter-position armor.

#### Nimera
Weapons/Conduits:
- **Pair of Knives** — twin-hit physical manifested pattern.
- **Ink Without Page** — magical-profile Conduit.
- **Unbound Sigil** — wide-arc multi-target Conduit.

Armor:
- **Closed Margin** — control defense.
- **Moving Script** — Speed/Magic target-change armor.
- **Unbroken Pattern** — beneficial-state preservation armor.

#### Vaelira
Weapons:
- **One Bright Law** — single-element commitment Staff.
- **Turning Prism** — element-rotation Staff.
- **Prismwake** — multi-target elemental Staff.

Armor:
- **Burning Glass** — output caster armor.
- **Storm at Rest** — defensive caster armor.
- **Quickglass** — fast-cast/interruption-resistant caster weave.

#### Seyrik
Weapons:
- **After the Wound** — weakened-target finisher 2H Sword.
- **Black Harvest** — multi-target cleaver.
- **Graveweight** — Break/Stagger 2H Sword.

Armor:
- **Standing Dead** — maximum physical stability.
- **Red Momentum** — aggressive Heavy armor.
- **Unmoved Plate** — anti-stagger stability armor.

### 7.2 Subclass Relics — 12
Current class names control:

#### Cyanis / Crest Arcanist
- **Twofold Sun** — Arcane Staff; alternating martial/magical cadence.
- **Steel in the Light** — Light caster armor; caster stabilization.

#### Ilyra / Vowblade
- **Mercy's Edge** — Two-Handed Sword; protection/support into reprisal.
- **The Burden Given Back** — Heavy armor; healing-fed stabilization.

#### Torren / Routeweaver
- **Surveyor's Knot** — Conduit; measured physical/magical hybrid routing.
- **Lines Between** — Light Ritual armor; weapon/Conduit action-family bridge.

#### Nimera / Truthshot
- **Kindly Distance** — Great Bow; support-to-ranged follow-through.
- **Borrowed Ground** — Medium armor; physical stability/footing.

#### Vaelira / Axiomblade
- **Prism Oath** — Sword; elemental spellblade expression.
- **Bright Bastion** — Heavy armor; caster stability in Crest equipment.

#### Seyrik / Ruin Warden
- **Clean Wound** — Wardrod; cleanse/purge into offense.
- **No Hand Upon Me** — Medium Warding armor; anti-control/anti-disable.

Native/shared legality remains governed by Audit104 Equipment Mastery and ordinary equipment-family legality.

### 7.3 Relic Secondaries — 5
Current promoted display names:
- **No Further** — Physical Bastion Shield.
- **The Quiet Gate** — Warding Bastion Shield.
- **Glass Hunger** — Offensive Channel Focus.
- **Second Spring** — Restorative Channel Focus.
- **One Breath Ahead** — Control/Tempo Focus.

Current Hunt routing:
- RH7 Rift Gate Colossus → **No Further**.
- RH8 Rift Siege Beast → **Glass Hunger**.
- RH9 Mercyfallen Behemoth → **Second Spring**.
- RH10 Authority Remnant → **One Breath Ahead**.
- RH11 Throne of Emperor Vaelkor → **The Quiet Gate**.

The Hunt enemy does not create the Relic; it may guard, carry, expose, or unlock access to the pre-existing artifact.

### 7.4 Capstone Relics — 11
These were developed under the obsolete 17-Legacy working branch but remain valid item designs. Audit106 reclassifies them as **Relic-rarity capstone items** rather than Legacy items.

#### Cyanis
- **Move or I Move You.** — Sword; defense/barrier breaking.
- **That Didn't Do Shit.** — Heavy armor; heavy-hit frontline stabilization.

#### Ilyra
- **I Said Enough.** — Wardrod; support into martial pressure.
- **Breathe. I've Got You.** — Focus; restorative efficiency.
- **Move. I've Got This.** — armor; emergency mitigation/response.

#### Torren
- **Figured You'd Come This Way.** — Medium armor; judgment/positioning.

#### Nimera
- **Hold On. That's Useful.** — Focus; beneficial-state preservation.
- **Fuck It. New Plan.** — Light Ritual armor; compensating adaptation.

#### Vaelira
- **There's Your Problem.** — Arcane Staff; elemental weakness amplification.
- **Oh, I Can Use That.** — Light caster armor; elemental pressure conversion.

#### Seyrik
- **You Should Have Killed Me.** — Heavy armor; surviving heavy damage into offense.

These Capstone Relics do **not** use the Character-Quest Legacy Component release chain. Their exact acquisition homes remain to be reconciled against the existing late-Relic source budget before implementation.

---

## 8. Legacy architecture — exactly 6

Audit104's six Legacy identities remain the only Legacy-rarity items.

Audit106 locks the following final **player-facing display titles** while preserving the Audit104 identity names as technical/cross-reference aliases so older quest/component files remain understandable.

| Base tradition | Audit104 identity alias | Final player-facing title | Slot |
|---|---|---|---|
| Crest Knight | Stillpoint Aegis | **That Was Dumb.** | Shield |
| Green Arcanist | Living Prism | **That Saves Me the Trouble.** | Focus |
| Blue Warden | Mercy's Boundary | **Try Me Instead.** | Shield |
| Ruin Vanguard | Purposebound | **You Are Finished.** | Two-Handed Sword |
| War Archer | Known Ground | **Should've Moved.** | Great Bow |
| Cardweaver | Decisive Record | **Good Fuck, Definitely. Good Fuck.** | one-slot Conduit |

### Legacy release / ownership
Audit104 remains controlling:
- each Character Quest grants that character's unique Legacy Component;
- the physical masterwork already exists in secured Cresthaven inventory;
- release/completion occurs during the Chapter-12 pre-point-of-no-return preparation window;
- the native owner may equip after release under normal legality;
- reciprocal partner use additionally requires that reciprocal character's Synthesis;
- no Legacy is mandatory for story completion, Story Primes, Final Severance, or ending access.

Character Quest mapping remains:
- Vaelira / The Sky No One Chose → Green Arcanist Legacy.
- Cyanis / The Weight of the Crest → Crest Knight Legacy.
- Nimera / The Archive That Remembers → Cardweaver Legacy.
- Seyrik / The Name That Remains → Ruin Vanguard Legacy.
- Ilyra / Mercy Has a Voice → Blue Warden Legacy.
- Torren / The Road That Returns → War Archer Legacy.

### Legacy mechanical identities
Final raw stats remain deferred, but these gameplay identities are controlling:

#### That Was Dumb. — Crest Knight Shield
Defense feeds offense. After an eligible Barrier gain or Shield-supported mitigation, the next damaging action receives a bounded damage/Break benefit. No free counterattack.

#### That Saves Me the Trouble. — Green Arcanist Focus
After taking eligible elemental damage, the next legal spell of that same element receives an MP-efficiency and output benefit. It never grants an element the wearer cannot otherwise use.

#### Try Me Instead. — Blue Warden Shield
Once per round, may reduce an eligible single-target hit aimed at a critically pressured ally, with the wearer taking a smaller portion of the prevented damage. No instant-KO/scripted-effect redirection.

#### You Are Finished. — Ruin Vanguard Two-Handed Sword
Execution weapon: increased damage against enemies below a finishing threshold, with a stronger high-risk payoff when the wearer is also critically injured. No instant kill/boss bypass.

#### Should've Moved. — War Archer Great Bow
Acuity finisher: increased precision/output against already-known target vulnerabilities/configurations, stronger when acting before the target. Does not reveal information or alter turn order.

#### Good Fuck, Definitely. Good Fuck. — Cardweaver one-slot Conduit
Adaptive Conduit: for eligible Conduit attacks, use the more favorable legal supported physical/magical profile from already-known combat data. Does not reveal hidden defenses, affect Cards, or bypass immunity.

### Provisional numerical values
The percentages previously used in the working item audit are retained as **production-test values only**, not final canon numbers, because Level-70 EXP/natural-stat rebalance must occur first.

---

## 9. Exceptional-equipment totals

After Audit104 reconciliation:
- Base Relic W/A: 36
- Subclass Relic W/A: 12
- Relic Secondaries: 5
- Capstone Relics: 11
- **Relics total: 64**
- **Legacies total: 6**
- **Exceptional total: 70**
- Ordinary equipment: 48
- **Total equipment: 118**

Practical item/equipment catalog floor:
- 20 Consumables
- 118 Equipment
- **138 practical Consumable + Equipment entries**

Cards remain separate.

Forge Components, Project Items, and Key Items are additional inventory records and are not included in the 138 count.

---

## 10. Relic / Legacy power-budget rules

Ordinary equipment remains the raw-stat baseline.

Relative effect architecture:
- final ordinary: raw-stat baseline approximately 100; little or no signature effect.
- Relic: specialized sidegrade, normally around raw 95–108 plus one bounded signature effect.
- late/capstone Relic: may sit toward the upper end of the Relic raw-stat band but must remain below Legacy culmination power.
- Legacy: highest effect budget in the equipment system, but not automatically the highest value in every raw stat.

Working passive guidance remains:
- Relic sustained broad bonus: approximately 5–8%.
- Relic conditional bonus: approximately 8–12%, with ~15% reserved for strongly constrained cases.
- Legacy broad bonus: approximately 8–12%.
- Legacy conditional bonus: approximately 12–18%.
- Avoid permanent unconditional ~20%+ damage items.
- Strong two-item same-axis exceptional combinations should normally stay near **20–25% sustained advantage** over comparable final ordinary packages, with higher spikes permitted only under meaningful layered conditions.

Two-handed weapon balance must be checked against an equivalent one-handed Weapon + Secondary package.

The item-audit family offensive-package index remains a valid tuning scaffold, not final raw stats:
- Sword 100
- Wardrod 88–94
- Great Bow 128–135
- Conduit 94–102
- Arcane Staff 96–104
- Two-Handed Sword 132–140

Dual-Sword Secondary contribution remains a working approximately 55–65% of a same-tier primary Sword's Attack/Magic budget, pending final raw-stat pass.

---

## 11. Kessara / Forge architecture

Kessara remains a **small authored project system**, not recipe spam.

No:
- junk-material economy
- ore/herb ladders
- crafting EXP
- random rolls
- +1 to +5 upgrade ladder
- low-percentage mandatory farming

Forge Components:
- dedicated Forge inventory category
- non-sellable
- non-discardable
- no battle use
- technical stack cap 99
- UI text may say `Used by Kessara`

Current Face-linked component names:
- Might — **Creststeel Billet**
- Elements — **Prismglass Plate**
- Grace — **Warding Silver Coil**
- Acuity — **Calibration Gearset**
- Change — **Pattern Crystal**
- Ruin — **Black Ore Segment**

`Regulator Gearset` is superseded by **Calibration Gearset**.

### Audit104 Legacy reconciliation
The older working use labels `Legacy Gate A / Legacy Gate B` for generic Forge Components are **superseded**.

The six Audit104 Legacies use the fixed Character-Quest Legacy Component → secured Cresthaven release chain and do **not** require generic material lists, recipes, currency fees, or Forge-component gates.

Kessara may still restore authored Relics and support other fixed projects, but the exact post-Audit104 Forge-Component pickup/use count must be revalidated before implementation. The old `5 obtainable / 4 required per Face` schedule is retained as a historical tuning target, **not locked**, until its two former Legacy uses per Face are reassigned or removed.

Kessara's 12 authored Relic-project concept remains valid:
- 6 Base Relic projects
- 6 Subclass Relic projects

Do not expand this into a mandatory 24-project grind merely because the Relic catalog grew.

---

## 12. Standard Cards — 24 total

Exactly **24 Standard Cards**, four per Face. Standard Cards remain unlimited-use and enemies do not use Diysean Cards.

### Might
- **Iron Testament**
- **Sunder the Gate**
- **Relentless Flurry**
- **March of Blades**

### Elements
- **Cinder Judgment**
- **Confluence Sigil**
- **Winterglass Spear**
- **Thunder Chain**

### Grace
- **Restoration**
- **Merciful Reprisal**
- **Wellspring**
- **Dawn Recall**

### Acuity
- **Faultline Sight**
- **Chosen Course**
- **Predicted Impact**
- **Decisive Interval**

### Change
- **Glassform Rupture**
- **Reversal Engine**
- **Spatial Guillotine**
- **Sanguine Alloy**

### Ruin
- **Devouring Singularity**
- **Worldsplitter**
- **Calamity Lance**
- **Zero Hour**

Audit105 Acuity definitions and exact Acuity source homes remain controlling.

### Current Standard-Card acquisition pacing
Audit106 promotes the item-audit chapter-density correction:

#### Chapter 1 — 2
- **Faultline Sight** — Hollow Watch Castellan first clear; Audit105-locked.
- **Iron Testament** — protected Ancient-route / Hollow Watch military cache.

#### Chapter 2 — 2
- **Restoration** — Sunken Archive protected recovery/triage cache.
- **Sunder the Gate** — Red Transfer Bastion protected siege/access-control cache.

Regional Hunt #2 remains a no-protected-unique-Card boundary.

#### Chapter 3 — 3
- **Glassform Rupture** — protected Ancient repository.
- **Reversal Engine** — Regional Hunt #3 / Archive Judgment Engine.
- **Merciful Reprisal** — Ilyra's `Mercy Has a Voice` content in the Chapter-3 availability window for item pacing.

#### Chapter 4 — 3
- **Cinder Judgment** — Reaction Annex / regulation-system protected cache.
- **Relentless Flurry** — Regional Hunt #4 / Crown Prototype.
- **March of Blades** — Major Hunt #1 / Ashen Whitehorn, available by Chapter 4.

#### Chapter 5 — 2
- **Chosen Course** — Deepforge Colossus first clear; Audit105-locked.
- **Dawn Recall** — Regional Hunt #5.

#### Chapter 6 — 4
- **Winterglass Spear** — Crownstorm Roc / Weather Crown stabilization.
- **Thunder Chain** — Regional Hunt #6.
- **Calamity Lance** — Matron Zevraya.
- **Sanguine Alloy** — optional Zevraya laboratory sealed cache.

#### Chapter 7 — 1
- **Spatial Guillotine** — Warden of Nameless / Revision Arbiter source.

#### Chapter 8 — 1
- **Confluence Sigil** — Major Hunt #4.

#### Chapter 9 — 2
- **Wellspring** — Equal Mercy Arbiter.
- **Predicted Impact** — Regional Hunt #9 / Mercyfallen Behemoth; Audit105-locked.

#### Chapter 10 — 3
- **Devouring Singularity** — Custodian reconciliation.
- **Worldsplitter** — Regional Hunt #10 / Authority Remnant.
- **Decisive Interval** — Major Hunt #5 / Final Archive Arbiter; Audit105-locked.

#### Chapter 11 — 1
- **Zero Hour** — Major Hunt #6.

Total curve:
- **2 → 2 → 3 → 3 → 2 → 4 → 1 → 1 → 2 → 3 → 1 = 24**

Early Chapters 1–4 therefore contain **10 / 24** Standard Cards.

If a newer quest/hunt scene-numbering pass moves the associated content window, move the Card with its authored source rather than duplicating the Card.

---

## 13. Acuity item/equipment terminology

Acuity remains the formal Face.

Do not restore:
- Resource Face equipment terminology
- Regulator Gearset
- Bastion Reserve
- Stormglass Relay
- Prismatic Reserve
- Lifeward Transfer
- Last Measure
- Sheltering Host

Torren's War Archer equipment should express Acuity through:
- perception
- judgment
- known-target precision
- route/position reading
- timing
- anticipation

Torren's Routeweaver remains a **Change** Subclass under Audit105/Audit104 even when its equipment aesthetics use Torren's personal gold/amber route-line language.

---

## 14. Region terminology in item names/sources

Current formal regional names:
- **The Greyspires**
- **The Westways**
- **The Crownhold**

Retired as current regional labels:
- Highlands
- Diysereach
- Edgelands
- Southhold

Settlement names remain valid unless separately changed.

Current ordinary item catalog contains no active retired regional-name dependency. `Deepforge Battlestaff` is the approved replacement for the old `Highland Battlestaff` wording.

---

## 15. Production data model

Recommended item record fields remain:
- `item_id`
- `display_name`
- `description`
- `category`
- `subcategory`
- `tier`
- `face_id`
- `stack_limit`
- `sellable`
- `discardable`
- `battle_usable`
- `field_usable`
- `unique_flag`
- `sort_group`
- `icon`
- `lore_tag`
- `notes`

Keep acquisition, economy, equipment legality, stat profile, passive, Legacy Trait, consumable, Forge, Kessara project, Project Item, Key Item, and Card data as separate structures where practical.

Equipment legality should resolve from equipment-family unlocks, not static owner lists.

Two-handed slot use must be explicit in item data.

Validation should catch at minimum:
- 20 Consumables exactly
- 24 Standard Cards exactly / 4 per Face
- 12 Prime Cards total under Prime canon
- Acuity item IDs/names not regressing to Resource-era terminology
- reward-only consumables not appearing in ordinary shops
- unique Project Items not generated repeatedly
- ordinary repurchase fallback after first obtain
- two-handed equipment blocking Secondary use
- Ilyra armor profile exception
- no General Accessory records
- stable ID uniqueness
- no duplicated Card source IDs
- no owner-only exceptional-equipment resonance

---

## 16. What Audit106 supersedes from the working item tracker

The historical item tracker may remain as design history, but the following are not current-facing authority:

1. **Level-60 cap references** — superseded by Level 70.
2. **17 Legacy-rarity items** — superseded by six Audit104 Legacies + eleven Capstone Relics.
3. **Crest Magus / Prism Archer / Sixfold Knight / Ruin Healer labels** — superseded by Audit104 current Subclass names.
4. **Blanket all-Conduits-one-handed rule** — narrowed; listed ordinary Conduits are one-slot, but Audit104 permits authored two-handed Conduits.
5. **Generic Forge Components as mandatory Legacy Gate A/B materials** — superseded by Audit104's fixed Character-Quest Component → secured-Legacy release.
6. Any `Resource` Face equipment terminology — superseded by Acuity where the reference is Face/system-specific.

Historical alternatives may remain in old audit logs but may not override this file.

---

## 17. Open work after Audit106

Do **not** begin final raw-stat assignment until the following sequence is followed:

1. Rebalance / verify the **Level-70 EXP curve** and expected chapter-end/player-level bands.
2. Revalidate natural character stat growth at those levels.
3. Revalidate enemy/boss stat progression against the Level-70 curve.
4. Lock final ordinary-equipment raw-stat baselines.
5. Normalize all 64 Relics against those baselines, including the 11 reclassified Capstone Relics.
6. Lock final numerical stats/passives for the six Legacies.
7. Reconcile exact acquisition homes for the 11 Capstone Relics.
8. Reconcile Kessara Forge-Component pickup/use counts after removal of generic Legacy Gate A/B material uses.
9. Run the full **118-piece equipment power-curve audit** across Chapters 1–12.
10. Implement data only after the above balance reconciliation passes.

Until then, the previously drafted exceptional-item percentage values are valid as **playtest scaffolding**, not final numeric canon.

---

## 18. Final Audit106 count summary

- Consumables: **20**
- Ordinary Weapons: **27**
- Ordinary Armor: **12**
- Ordinary Secondaries: **9**
- Ordinary Equipment: **48**
- Relics: **64**
- Legacies: **6**
- Exceptional Equipment: **70**
- Total Equipment: **118**
- Consumables + Equipment: **138**
- Standard Cards: **24**
- Prime Cards: **12** under Prime canon
- General Accessories: **0**

**Audit106 is the current item/equipment/economy reconciliation authority.**