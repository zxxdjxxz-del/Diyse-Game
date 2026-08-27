# Diyse — Current Working Tracker

**Date:** August 27, 2026  
**Working revision:** **v48**  
**Master-canon baseline:** **v2.07 / Audit122**  
**Status:** **ACTIVE WORKING TRACKER — MASTER CANON OUTRANKS THIS FILE**

Primary authority:
- `docs/canon/AUDIT122_BASE_HIT_EVASION_AND_BLEED_RUNTIME_LOCK.md`
- `docs/canon/AUDIT121_CURRENT_SYSTEMS_ITEM_EQUIPMENT_AND_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT119_POST_AUDIT116_COMBAT_RESOURCE_PRIME_AND_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md`
- `docs/ACTIVE_CANON.md`
- `AGENTS.md`

Historical cumulative trackers remain provenance only.

---

# Current closed state

## Combat/system cleanup
- Barrier does not exist.
- Brace does not exist.
- No global Break/Stagger meter.
- Staggered is an ordinary harmful status only.
- Guard remains valid.
- no natural Accuracy stat.
- Base Hit/Evasion formula is closed under Audit122:
  - `AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers`
  - `EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers`
  - `FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)`
- Bleed damages each round and again when the affected character acts.
- Bleed clears only on full-HP restoration, eligible harmful-status clear, or eligible item.
- Audit120 direct-damage/Critical formulas remain compatible and active.

## Classes / Faces
- Cyanis — Crest Knight / Crest Arcanist — Might
- Ilyra — Blue Warden / Vowblade — Grace
- Torren — War Archer / Routeweaver — Acuity
- Nimera — Cardweaver / Proofhunter — Change
- Vaelira — Green Arcanist / Axiomblade — Elements
- Seyrik — Ruin Vanguard / Ruin Warden — Ruin

## Class Ability MP certification — CLOSED / 12 OF 12 PASS
The v467 Base-class and v469 Subclass working MP rebases have now completed the Audit121-required certification pass against:
- Audit115-normalized Ability functions;
- Power / healing / targeting / status / penetration packages;
- current Mastery/Trait MP reductions;
- Standard Card MP costs;
- Prime Invocation costs;
- MP recovery consumables;
- representative working Max-MP packages;
- late-game Legacy MP support.

Result:
# **NO AUTHORED BASE MP COST CHANGES REQUIRED**

Certified Base bands:
- routine floor: **10–16 MP** by class;
- premium non-Ultimate: **30–40 MP** by class;
- Ultimate: **52–60 MP**.

Certified Subclass bands:
- routine floor: **14–18 MP listed**;
- premium non-Ultimate: **34–38 MP**;
- Ultimate: **60–64 MP**.

Current certified Mastery/Trait reductions remain:
- Crest Knight / Clear Channel: Resonant Pulse **12 → 11 MP**;
- War Archer / Patient Aim: Watchful Aim **20 → 18 MP**;
- Cardweaver / Tight Weave: Weave Guard **18 → 16 MP**;
- Green Arcanist / Efficient Spectrum: first eligible elemental Base Ability each ordinary round **−2 MP**;
- Ruin Vanguard / Controlled Unmaking: Unmaking Blow **30 → 28 MP**;
- Crest Arcanist / Crest Resonance Rank I: all MP-costing Crest Arcanist Abilities **−2 MP**.

No separate MP cost is created for Gentle Continuance.

Resource hierarchy remains coherent:
- Standard Cards: **18–48 MP**;
- Recovered Story Prime: **50 MP**;
- Awakened Story Prime: **80 MP**;
- Awakened Major Hunt Prime: **90 MP**.

Late Legacy MP recovery/discount effects are treated as intentional capstone exceptions and do not cause wholesale class-cost inflation.

Exact percentage-cost-modifier rounding/order remains a separate runtime arithmetic detail unless already established by a more specific implementation authority.

## Mastery architecture
- Synthesis removed.
- 4 Core + 4 Subclass Masteries = 8 active nodes.
- Core eligibility = Base CL3 / 6 / 9 / 12.
- Subclass eligibility = CL3 / 5 / 7 / 11.
- donor pairs: Cyanis↔Vaelira, Ilyra↔Seyrik, Torren↔Nimera.
- donor Relic access = purchase Subclass Mastery 3.
- donor Legacy access = purchase Subclass Mastery 4 / Legacy Mastery.
- donor use equips the original obtained item; no duplicate shared artifact.

## Equipment
- 38 ordinary
- 36 Relics
- 17 native Legacies
- 91 total
- ordinary 38/38 architecture remains closed under Audit118.
- Legacy 17/17 raw stats/perks/Traits are final under Audit121.
- Relic Barrier/Brace/Break-era stale mechanics are cleaned under Audit121.

## Consumables
- 20 total.
- Auren currency; 1 economy unit = 20 Auren.
- fixed Salve ladder: 250 / 750 / 1,500 / 2,250 HP.
- Company Salve = 30% Max HP party-wide.
- Flow / Deepflow / Highflow = 50 / 80 / 120 MP.
- Reservoir Tonic = 75% Max MP, reward-only.
- Emergency Kit and Emergency Rally finalized.
- normal-stock pricing and reward-only first guaranteed placements are locked in Audit121.

## Commerce / names
Regional Markets:
- Brackenwall
- Dunmere
- Caelora
- Ivorybridge
- Stonewake
- Frostmere
- Westguard
- Larkspire
- Cerythvale

Westguard replaces Westreach / Yahtrens Stand.

Cresthaven Quartermaster = full normal-stock consolidation/requisition endpoint.

Vhalmarch = forward supply/requisition, not civilian Regional Market.

## Cards / Primes
- Acuity quartet: Faultline Sight / Measured Response / Predicted Impact / Decisive Interval.
- Predicted Impact = Magical/Colorless, P180, BH110, 28 MP, 30% Stun.
- Prismatic Deluge = 90×4 = 360 total listed Power per target.
- Regulator Fang = P250 / 25% Spirit penetration.

## Chapter 4
Exactly four elements:
- Fire
- Ice
- Lightning
- Earth

Wind/Water removed from the regulation/research framework. Seventh Reaction is emergent four-element behavior, not a seventh element. Reaction Conduit replaces Elemental Hexarch. Regulation Crucible uses the four-chamber/two-active architecture locked in Audit121.

### Script/runtime synchronization — COMPLETE
The approved four-element conversion is now applied to the live Chapter-4 production files:
- canonical Markdown S022–S026;
- matching dialogue `.tres` S022–S026;
- S023/S024/S025 presentation corrections;
- Crown Prototype presentation label normalized to Reaction Annex Prototype Branch.

Chapter-local reconciliation authority:
- `docs/chapters/dialogue/chapter_04/FOUR_ELEMENT_REWORK_2026-08-27.md`

The Ch1–4 ordinary formation catalog was checked and already uses the correct current Chapter-4 roster:
- Reaction Node
- Composite Elemental
- Reaction Hound
- Element Mirror
- Annex Crucible Guard

Historical internal keys such as `LOC_SIXFOLD_ANNEX`, `LOC_SIXFOLD_REGULATION_CORE`, and `CH04_SIXFOLD_ANNEX` may remain temporarily for technical compatibility. They are not current display/canon names and must not drive mechanics. Any future rename must migrate all references/persistence keys together.

---

# Current progression direction

- Player level cap = 70.
- Chapter 0 grants no levels.
- slower progression through Ch1–7, faster after Ch7.
- normal full class completion target = **about player Lv62**.
- Lv62–70 should provide meaningful full-build play.

Simulation-only Mastery Point candidate:
- Lv5
- Lv10
- Lv15
- Lv20
- Sixfold Volition
- Lv40
- Lv50
- Lv60

This exact cadence is **not final**.

---

# ACTIVE FRONTIER

## 1. CEXP + class-progression redo
Still required against:
- Chapter 0 + Chapters 1–13;
- Subclasses unlocking at end-Ch7 Sixfold Volition;
- separate Base/Subclass CEXP;
- no Synthesis;
- 8 Mastery nodes;
- full class completion around player Lv62;
- Seyrik late-recruit catch-up;
- normal route vs completionist pacing;
- optional-content acceleration;
- donor Relic/Legacy timing.

## 2. Exact 8-point Mastery Point schedule
Finalize inside the CEXP/progression pass rather than independently.

## 3. Detailed campaign EXP/enemy calibration
Still open:
- Ch1–13 player-level bands;
- enemy-level bands;
- encounter counts;
- formation EXP;
- diminishing returns;
- named enemy/boss recertification where progression dependent.

---

# Do not reopen without explicit instruction

- Base Hit/Evasion resolver
- current Bleed lifecycle
- 38/38 ordinary equipment source/shop architecture
- 20-item consumable architecture
- 17/17 Legacy mechanical design
- Barrier/Brace removal
- global Break/Stagger removal
- Predicted Impact stale-system cleanup
- Prismatic Deluge / Regulator Fang exact numeric values
- Chapter-4 four-element framework
- Chapter-4 S022–S026 four-element script/dialogue-runtime synchronization
- certified v467 Base-class Ability MP costs
- certified v469 Subclass Ability MP costs
