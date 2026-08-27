# Diyse — Audit121: Current Systems, Item/Equipment, and Progression Reconciliation Lock

**Master-canon version:** **v2.06 / Audit121**  
**Date:** August 27, 2026  
**Status:** **MASTER CANON — CONTROLLING**  
**Parent authority:** **v2.05 / Audit120** plus all compatible older locks.  
**Purpose:** Promote the approved post-Audit120 equipment, consumable, combat-cleanup, Chapter-4 element, terminology, Prime-command, commerce, and progression-direction decisions into master canon while explicitly preserving the remaining CEXP and Ability-MP balance work as open.

Where this audit conflicts with Audit120 or older audits, **Audit121 controls only for the domains explicitly changed below**. Audit120 remains controlling for compatible direct-damage and Critical rules. Audit119–Audit115 and compatible older audits remain active where not superseded here.

---

# 1. System removals and terminology firewall

## 1.1 Barrier is removed globally

**Barrier does not exist as a current Diyse combat mechanic.**

Do not use Barrier in:
- class Abilities;
- enemy actions;
- equipment or Traits;
- consumables;
- Standard Cards or Primes;
- encounter states;
- damage-order language.

Do not invent a replacement shield-HP gauge merely to preserve old Barrier text.

Any older Audit120/Audit119 wording that lists Barrier among later-stage damage modifiers is superseded. **Guard** remains a valid ordinary defensive choice/state where authored.

## 1.2 Brace does not exist

**Brace does not exist.** Do not use it in combat, equipment, enemy, Card, or Ability wording.

## 1.3 Global Break/Stagger system is removed

There is no global Break/Stagger meter or contribution system.

**Staggered** remains a normal harmful status only where explicitly authored.

## 1.4 Hit terminology

There is no natural `Accuracy` stat. Use **Base Hit** and **Evasion** under the current hit/evasion architecture.

---

# 2. Current permanent classes and Faces

Permanent six:

| Character | Base Class | Subclass | Face |
|---|---|---|---|
| Cyanis | Crest Knight | **Crest Arcanist** | Might |
| Ilyra | Blue Warden | Vowblade | Grace |
| Torren | War Archer | Routeweaver | **Acuity** |
| Nimera | Cardweaver | **Proofhunter** | Change |
| Vaelira | **Green Arcanist** | **Axiomblade** | Elements |
| Seyrik | Ruin Vanguard | **Ruin Warden** | Ruin |

Superseded current-name assumptions include Crest Magus, Sixfold Knight, Prism Archer as Vaelira's current Base Class, and Ruin Healer.

**Resource** as Torren's Face is retired; the current Face is **Acuity**.

---

# 3. Class Mastery / donor-access architecture

Synthesis remains removed.

Each permanent character has exactly:
- **4 Core Masteries**;
- **4 Subclass Masteries**;
- **8 active Mastery nodes total**.

Current eligibility structure:

### Core
- Node 1 — Base CL3
- Node 2 — Base CL6
- Node 3 — Base CL9
- Node 4 — Base CL12

### Subclass
- Node 1 — Subclass CL3
- Node 2 — Subclass CL5
- Node 3 / Equipment Mastery — Subclass CL7
- Node 4 / Legacy Mastery — Subclass CL11

Purchasing Subclass Mastery 3 grants the linked donor's Relic access. Purchasing Subclass Mastery 4 grants the linked donor's Legacy access.

Reciprocal donor pairs:
- Cyanis ⇄ Vaelira
- Ilyra ⇄ Seyrik
- Torren ⇄ Nimera

Linked donor access uses the donor's **actual obtained item**. There is no duplicate shared artifact and no universal off-owner nerf. The item's Trait travels with the item.

A character's own native Base-class Legacy does **not** require Synthesis or donor Legacy Mastery.

---

# 4. Progression direction — current target and open work

Player level cap remains **70**.

The controlling pacing target is now:

> **A normal-route character should be about to max their full class progression around player Level 62.**

Intent:
- class growth remains meaningful deep into the game;
- the full class system is not finished around Lv50;
- Lv62–70 provides a meaningful late/endgame window using completed builds.

The exact **8-point Mastery Point grant schedule is not yet locked**. The current simulation-only candidate is:
- Lv5
- Lv10
- Lv15
- Lv20
- Sixfold Volition
- Lv40
- Lv50
- Lv60

Do not implement those exact late grant levels as final until the progression redo closes.

## Still OPEN / REQUIRED

1. **Full CEXP/class-progression redo** against the current 13-chapter structure and Lv62 completion target.
2. **Final class Ability MP check/certification pass** across all 6 Base and 6 Subclass kits.
3. Exact 8-point Mastery grant cadence, finalized with the CEXP pass.
4. Detailed Ch1–13 player EXP, enemy-level, encounter-count, formation-EXP, and diminishing-return calibration.
5. Progression-dependent named-enemy/boss raw-stat recertification.

Current Ability functions/kits are not reopened by the MP check. Existing MP tables are working starting data, not a final cross-kit certification result.

Chapter 0 remains level-static: **no character levels are gained in Chapter 0**.

---

# 5. Equipment catalog state

Current active equipment catalog:
- **38 ordinary equipment**
- **36 Relics**
- **17 native Legacies**
- **91 total equipment pieces**

The 38/38 ordinary-equipment numerical/source/shop structure already promoted by Audit118 remains active. Do not redo that catalog unless a later audit explicitly reopens it.

Hierarchy remains:

> **Ordinary < Relic < Legacy**

Legacies must be stronger overall than Relics, while narrow specialist Relic wins remain legal.

---

# 6. Final native Legacy equipment — 17 / 17

## Cyanis

### Move or I Move You. — Sword
- +74 ATK / +55 MAG
- Perk: +10 percentage points applicable Defense/Spirit penetration on eligible damaging Sword actions.
- **Legacy Trait — Forced Opening:** against a Guarding enemy, gain an additional +15pp applicable penetration and +15% final damage. Does not automatically remove Guard.

### That Was Dumb. — Shield
- +30 DEF / +28 Spirit
- Perk: +12 Status Resistance
- **Legacy Trait — Bad Choice:** once per round after eligible single-target hostile direct damage, the next eligible damaging action before the end of the following round gains +15% final damage and +10pp applicable Defense/Spirit penetration. One pending instance maximum; refreshes rather than stacks; no free counter.

### That Didn't Do Shit. — Heavy Armor
- +50 DEF / +42 Spirit
- Perk: Max HP +12%
- **Legacy Trait — Still Standing:** take 8% less eligible direct damage normally; this becomes 15% less direct damage at or below 40% Max HP. Values do not stack.

## Ilyra

### I Said Enough. — Wardrod
- +58 ATK / +63 MAG
- Perk: +10% direct-healing potency
- **Legacy Trait — Final Warning:** after a real eligible heal or harmful-status removal on another conscious ally, the next eligible damaging action before the end of the following round gains +15% final damage and +15pp applicable Defense/Spirit penetration. One pending maximum; empty heals/cleanses do not trigger it.

### Try Me Instead. — Shield
- +28 DEF / +30 Spirit
- Perk: Max HP +8%
- **Legacy Trait — Sanctuary:** while the wearer is conscious, other conscious active allies at or below 50% Max HP take 8% less eligible direct damage. No redirect or target change.

### No. Stay Here. — Focus
- +22 MAG / +28 Spirit
- Perk: Max MP +12%
- **Legacy Trait — Stay With Me:** once per round after the first eligible Ability that actually heals, cleanses a harmful status, or revives an ally, restore 8% of the wearer's Max MP after resolution. The full action cost must be payable first. Items/Cards/Primes do not trigger it.

### Get Behind Me. — Warding Armor
- +34 DEF / +44 Spirit
- Perk: Max HP +10%
- **Legacy Trait — Immediate Shelter:** an eligible healing Ability used on a conscious ally who begins at or below 30% Max HP gains +20% action Speed and +15% direct-healing potency for the qualifying low-HP target. On multi-target healing, the Speed bonus applies if at least one target qualifies; potency applies per qualifying target.

## Torren

### Should've Moved. — Great Bow, 2H
- +95 ATK
- Perk: +10 Base Hit
- **Legacy Trait — Predicted Line:** against Hunter's Measure, gain +10% final damage and +10pp Critical Chance. If the measured enemy has not acted this round, use the stronger tier instead: +15% final damage and +15pp Critical Chance. No hidden-information read or turn-order change.

### Figured You'd Come This Way. — Medium Armor
- +42 DEF / +33 Spirit / +3 SPD
- Perk: Evasion +10
- **Legacy Trait — Prepared Ground:** once per round, on the first qualifying single-target action from an enemy that has not acted this round, take 15% less eligible direct damage from that enemy through the end of the current round. One enemy per round.

## Nimera

### Good Fuck, Definitely. Good Fuck. — 2H Conduit
- +60 ATK / +82 MAG
- Perk: +10% final damage on eligible normal Conduit Attack / Conduit-tagged damaging actions.
- **Legacy Trait — Better Version:** for a legal Conduit action that supports both Physical and Magical resolution, the player chooses Physical or Magical at selection. Element, Power, hits, target, cost, and status package are unchanged. No hidden-defense reading. Standard Cards and Primes are unchanged.

### Hold On. That's Useful. — Focus
- +22 MAG / +22 Spirit / +8 SPD
- Perk: Standard Card action Speed +10%
- **Legacy Trait — Keep That:** once per round, the first eligible beneficial temporary effect on the wearer that would expire naturally or be removed by an eligible hostile dispel/purge is preserved through the end of the following round. Each effect application can be preserved only once.

### Fuck It. New Plan. — Light Ritual Armor
- +32 DEF / +42 Spirit
- Perk: while the wearer has an eligible harmful status or ordinary negative stat change, +10% action Speed.
- **Legacy Trait — New Plan:** the first qualifying pressure each round creates one matching two-round compensation; only one can be active and a new one replaces the old:
  - ATK Down / MAG Down → +15% final damage
  - DEF Down → 20% less eligible direct Physical damage
  - Spirit Down → 20% less eligible direct Magical damage
  - Speed Down → +25 Status Resistance
  - harmful status applied → +25 Status Resistance
  - eligible elemental damage → 20% less damage from that same element
- The original penalty is not removed.

## Vaelira

### There's Your Problem. — Arcane Staff
- +12 ATK / +83 MAG
- Perk: elemental damaging Staff actions gain +10pp Spirit penetration.
- **Legacy Trait — Correct Answer:** when elemental damage hits an actual elemental weakness, gain +15% final damage and +10pp harmful-status application chance only for an already-authored matching status rider. Does not reveal hidden affinity information.

### That Saves Me the Trouble. — Focus
- +24 MAG / +24 Spirit / +5 SPD
- Perk: Max MP +12%
- **Legacy Trait — Borrowed Answer:** once per round after the wearer takes eligible direct elemental damage greater than 0, for that same element through the end of the following round: eligible damaging Abilities of that element cost 20% less MP (minimum 1) and deal +12% final damage. One active element; later triggers replace it. Does not grant an element.

### Oh, I Can Use That. — Light Caster Armor
- +29 DEF / +50 Spirit / +4 SPD
- Perk: 10% less eligible direct elemental damage.
- **Legacy Trait — Useful Pressure:** the first time each round the wearer takes eligible direct elemental damage greater than 0, eligible elemental damaging actions gain +15% final damage through the end of the following round. Does not grant an element.

## Seyrik

### You Are Finished. — 2H Sword
- +105 ATK / +7 MAG
- Perk: +10pp Critical Chance
- **Legacy Trait — End It:** against an enemy with at least one eligible harmful status or ordinary negative stat change, gain +15% final damage and +15pp Defense penetration. Does not apply, consume, or extend the condition.

### You Should Have Killed Me. — Battle Heavy Armor
- +56 DEF / +34 Spirit
- Perk: Max HP +15%
- **Legacy Trait — Still Dangerous:** after eligible hostile direct damage greater than 0, through the end of the following round gain +15% ATK, +15% MAG, and +10pp application chance for already-authored harmful-status riders. Refreshes rather than stacks; no mitigation, heal, or counter is added.

Legacy audit: **17/17 final**, donor audit **6/6 PASS**, 2H commitment audit PASS.

---

# 7. Relic stale-mechanic cleanup

The following current Relic corrections supersede Barrier/Brace/Break-era wording:

- **Quiet Rebuke — Wardrod +48 ATK / +52 MAG — Measured Correction:** eligible Wardrod actions with an authored harmful status/control/negative-stat change gain +12 application reliability. If one successfully applies, the next eligible Wardrod attack against that target before the end of the following round gains +5% final damage.
- **Kindled Vow — Wardrod +44 ATK / +58 MAG — Vow in Motion:** after a real heal/cleanse on another ally, the next eligible Wardrod attack before the end of the following round gains +8% final damage and +10 Base Hit.
- **Blue Censure — Wardrod +52 ATK / +55 MAG — Break the Posture:** against a Guarding enemy, +8% final damage and +15pp applicable Defense/Spirit penetration. The name does not imply a global Break meter.
- **The Second Answer — Warding Armor +27 DEF / +36 Spirit — Answer Quickly:** once per round when a conscious ally enters/begins an action at or below 30% HP, the next eligible healing Ability before the end of the following round gains +15% action Speed and +8% direct-healing potency for the qualifying low-HP target.
- **No Further — Shield +29 DEF / +12 Spirit / -4 SPD — Hold the Impact:** once per round after eligible direct Physical damage of at least 12% Max HP, through the end of the following round gain +10% Defense and take 8% less direct Physical damage. Earth damage received 80%; incoming ordinary Staggered application ×0.80.
- **The Quiet Gate — Shield +16 DEF / +27 Spirit / -1 SPD — Nothing Through:** +15 Status Resistance; 12% resistance to ordinary negative-stat-change application; 5% less eligible direct Magical damage; Lightning damage received 80%.
- **Second Spring — Focus +17 MAG / +23 Spirit — Return Strength:** eligible direct-healing Abilities +10% potency; if the target is at or below 50% HP, total +15%; wearer +10 Status Resistance.
- **Blue Silence — Warding Armor +23 DEF / +39 Spirit — Warden's Quiet:** +15 Status Resistance; 12% resistance to ordinary negative-stat-change application; after successfully resisting an eligible harmful status or ordinary negative stat change, +8% Spirit through the end of the following round. Refreshes rather than stacks.

No current Relic depends on Barrier, Brace, or the deleted global Break/Stagger system.

---

# 8. Consumables — 20 / 20 current catalog

Currency is **Auren**.

> **1 economy unit = 20 Auren**

Current consumables:

| ID | Item | Effect | Purchase / reward value |
|---|---|---|---:|
| C01 | Field Salve | restore **250 HP** to one ally | **20 Auren** |
| C02 | Restorative Salve | restore **750 HP** to one ally | **50 Auren** |
| C03 | Vital Salve | restore **1,500 HP** to one ally | **120 Auren** |
| C04 | Grand Salve | restore **2,250 HP** to one ally | **240 Auren** |
| C05 | Company Salve | restore **30% Max HP** to all conscious active-party members | **200 Auren** |
| C06 | Flow Tonic | restore **50 MP** to one conscious ally | **80 Auren** |
| C07 | Deepflow Tonic | restore **80 MP** | **200 Auren** |
| C08 | Highflow Tonic | restore **120 MP** | **360 Auren** |
| C09 | Reservoir Tonic | restore **75% Max MP** | **640 Auren equivalent; reward-only** |
| C10 | Rousing Salts | revive one unconscious ally at **25% Max HP** | **60 Auren** |
| C11 | Greater Rousing Salts | revive one unconscious ally at **50% Max HP + 25% Max MP** | **160 Auren** |
| C12 | Trauma Remedy | remove **Burn / Bleed** | **15 Auren** |
| C13 | Stability Remedy | remove **Freeze / Stun / Staggered** | **15 Auren** |
| C14 | General Remedy | remove one eligible ordinary harmful status | **50 Auren** |
| C15 | Full Remedy | remove all eligible ordinary harmful statuses | **140 Auren** |
| C16 | Blinding Mist | guaranteed escape from an eligible ordinary random encounter | **10 Auren** |
| C17 | Null Seal | remove one eligible positive effect from an enemy | **70 Auren** |
| C18 | Balance Seal | restore eligible ordinary negative stat changes toward normal | **60 Auren** |
| C19 | Emergency Kit | one conscious ally: restore **75% Max HP + 60% Max MP** plus its established eligible cleanse/negative-stat restoration; does not revive | **300 Auren equivalent; reward-only** |
| C20 | Emergency Rally | revive **all unconscious active-party members** at **60% Max HP + 35% Max MP**; no harmful-status cleanse or negative-stat restoration | **500 Auren equivalent; reward-only** |

Blinding Mist does not work on bosses, elites, or protected encounters. Null Seal does not remove protected/scripted effects.

Reward-only first guaranteed copies:
- **Reservoir Tonic:** Chapter 8, deeper Horizon Vault protected reserve cache in the severance-gallery leg.
- **Emergency Kit:** Chapter 8, protected field-medical supply cache during the western counteroffensive before the Varkesh climax.
- **Emergency Rally:** Major Hunt #5, **Final Archive Arbiter**, additional deterministic first-clear reward.

Reward-only items do not enter normal shop, Regional Market, Cresthaven Quartermaster, or Vhalmarch requisition stock.

---

# 9. Commerce endpoints

Normal stock carries forward once unlocked unless a specific story scarcity rule says otherwise.

Current Regional Markets:
1. Brackenwall
2. Dunmere
3. Caelora
4. Ivorybridge
5. Stonewake
6. Frostmere
7. **Westguard**
8. Larkspire
9. Cerythvale

**Westguard** is the current production name replacing both **Westreach** and the intermediate **Yahtrens Stand** label. Older source prose referring to the same settlement should normalize to Westguard.

Not Regional Markets:
- Greenhollow
- Ashford
- Veycross
- Deepforge
- Emberforge

**Cresthaven Quartermaster** is the long-term normal-stock consolidation/requisition endpoint.

**Vhalmarch** is a Chapter-11 **Forward Supply / Requisition** endpoint, not a civilian Regional Market. After capture/stabilization it may carry all normal-stock consumables unlocked by then and limited current-campaign ordinary replacement equipment. Cresthaven remains the full ordinary-equipment catalog because Vhalmarch ↔ Cresthaven permanent two-way fast travel is available in that campaign window.

---

# 10. Standard Card synchronization

The current Acuity quartet is:
1. Faultline Sight
2. **Measured Response**
3. Predicted Impact
4. Decisive Interval

`Chosen Course` is historical/rejected.

### Predicted Impact
- one enemy
- Magical / Colorless
- Power **180**
- Base Hit **110**
- **28 MP**
- on a successful damaging hit: **30% Stun**
- no Defense/Spirit penetration
- no Staggered rider
- no Break/Stagger-meter contribution
- no hidden-weakness requirement

The four previously unresolved early Standard Card homes are now closed:
- **Iron Testament** — Chapter 1 Hollow Watch / Ancient-route protected cache
- **Restoration** — Chapter 2 Sunken Archive protected recovery/triage cache
- **Sunder the Gate** — Chapter 2 Red Transfer Bastion protected siege/access-control cache
- **Cinder Judgment** — Chapter 4 Reaction Annex / regulation-system protected cache

---

# 11. Prime command numerical synchronization

## Prismatic Deluge

Target: all enemies. Magical elemental sequence.

Resolve:
1. Fire — **90 Power**
2. Ice — **90 Power**
3. Lightning — **90 Power**
4. Earth — **90 Power**

Total listed Power per target if all waves resolve:

> **360**

Linked status checks:
- Fire → Burn
- Ice → Freeze
- Lightning → Stun
- Earth → Staggered
- 15% base chance per wave
- maximum 1 newly inflicted harmful status per target for the full command
- later status checks on that target are suppressed after the first successful new status; later damage waves still resolve.

No Colorless convergence hit.

## Regulator Fang

- one enemy
- Magical
- choose Fire / Ice / Lightning / Earth
- **Power 250**
- **25% Spirit penetration**
- no harmful-status rider

Its structural overlap with Last Convergence — Elemental Crown is accepted; do not redesign it solely for uniqueness.

---

# 12. Chapter 4 — four-element rework

Chapter 4 uses exactly:
- Fire
- Ice
- Lightning
- Earth

Wind and Water are removed entirely from the Chapter-4 research/regulation framework. Do not reassign their old functions to pseudo-elements, hidden channels, or replacement states.

The **Seventh Reaction** is emergent system-level behavior produced by all four elements. It is **not**:
- a seventh element;
- Omni;
- Prismatic;
- Colorless;
- Wind;
- Water;
- a reusable player combat system.

There is no global Composite Reaction table and no Imprint system.

Current Chapter-4 enemy/boss architecture includes:
- Reaction Node
- Composite Elemental
- Reaction Hound
- Element Mirror
- Annex Crucible Guard
- authored personnel
- Elder Briarhide
- **Reaction Conduit** replacing Elemental Hexarch
- Annex Duelist
- Regulation Crucible → Seventh Reaction
- Crown Prototype

Status-expression matrix where authored:
- Fire → Burn
- Ice → Freeze
- Lightning → Stun
- Earth → Staggered

Reaction Hound's Reaction Fang remains Physical/Neutral, Base Hit 100, 25% Bleed, with its one-round repetition lock.

Annex Crucible Guard's Crucible Cleave remains Physical/Neutral, Base Hit 100, 20% Bleed, with its lock. Alignment Pulse uses the four element/status pairings at the established 15% status rate.

Reaction Conduit is one-bar/nonlethal and has four elemental expressions only. Old Wind tempo and Water Barrier/healing/stabilization states are removed and not reassigned.

Annex Duelist uses only the four elements. Its old Wind/Water states and neutral fallback Bleed are retired with no replacement Bleed.

## Regulation Crucible
- chambers: Fire / Ice / Lightning / Earth
- exactly 2 active/targetable chambers at once
- core always targetable
- dormant chambers untargetable
- destroyed chambers remain destroyed
- base rotation: Fire/Ice → Lightning/Earth → Fire/Lightning → Ice/Earth
- if a scheduled slot's chamber is destroyed, that slot stays empty; if both are destroyed, the window is core-only
- former Wind speed/cadence inheritance is removed
- former Water Barrier/restoration/stabilization inheritance is removed
- Form II is a genuine new body with fresh HP/MP; no damage carryover; only surviving chamber traits carry; no third form
- fresh-HP transformation refreshes Prime availability under the global fresh-form rule

Crown Prototype retains its four-element-compatible mechanics. **Cinder Judgment** comes from a Reaction Annex/regulation-system protected cache, not a Sixfold Crucible first-clear reward.

---

# 13. Barrier cleanup outside Chapter 4

- Chapter 9 Triage Automaton does not use Barrier; its support package is HP recovery / Regen / +10% DEF and Spirit / one harmful-status removal.
- Standard Cards have no active Barrier dependency.
- Primes have no active Barrier dependency; Last Sanctuary uses healing/revive/Regen/Total Defense.
- Chapter-4 old Barrier-replacement queue is closed by removal rather than replacement.

---

# 14. Current completion state

## Item/equipment design

Mechanically/content-architecture complete at current canon level:
- 20/20 consumables
- 38/38 ordinary equipment
- 36/36 Relics
- 17/17 Legacies

Remaining item/equipment-adjacent work is implementation/naming polish unless explicitly reopened, including final naming where previously deferred, selected pickup presentation, Kessara copy-service UI/fee, icons/descriptions, and inventory implementation.

## Major live balance work still ahead

The next substantive balance work remains:
1. **class Ability MP check/certification**;
2. **CEXP + Mastery + player-level progression redo**, targeting class completion around Lv62.

---

# 15. Promotion verdict

**Audit121 is MASTER CANON.**

It promotes the approved post-Audit120 decisions above and supersedes conflicting older tracker/audit text only in those domains.

Do not infer closure for the explicitly OPEN progression and class-Ability-MP work.
