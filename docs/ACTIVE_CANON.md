# Diyse — Active Engineering Canon Guardrails

This is an implementation-facing summary. It does **not** replace the authoritative Complete Master Canon or newer explicit user corrections. If this summary conflicts with a later canon artifact, the later authority wins.

## Current whole-project authority — CORRECTED

**Diyse: HD-2D JRPG Clean Active Complete Master Canon v1.88 / Audit103 — Quest Architecture, Character Quest and Ordinary Side-Quest Closure**  
**Date:** August 21, 2026

The corrected forward authority sequence is:
- **v1.84 / Audit99** — Random-Encounter Runtime Implementation and Production-Readiness Closure.
- **v1.85 / Audit100** — Enemy Asset Reuse and Palette-Swap Production Efficiency Lock.
- **v1.86 / Audit101** — Major Hunt Architecture and Unlock Closure.
- **v1.87 / Audit102** — Major Hunt Difficulty and Progression Balance Closure.
- **v1.88 / Audit103** — Quest Architecture, Character Quest and Ordinary Side-Quest Closure.

The recent class-rework work occurs **after Audit103**. It is approved design but is **not yet assigned a valid master-canon audit number** in this file. The next available promotion slot is **v1.89 / Audit104**, subject to reconciliation with inherited Audit103 quest/Legacy-Component authority.

The mistakenly created `AUDIT100_RECIPROCAL_CLASS_SYNTHESIS_AND_LEGACY_ARCHITECTURE_LOCK.md` was invalid because Audit100 was already occupied by the Enemy Asset Reuse closure. It has been removed.

## Project foundation

- Diyse is an **HD-2D JRPG**.
- Field sprites target approximately **80 px**; battle sprites approximately **200–220 px**; dialogue uses large high-resolution portraits.
- Standard combat frame: up to four active party members staggered left, enemies right, open center action/VFX lane.
- Target runtime: approximately **25 hours**.
- Permanent roster: exactly six; maximum active battle party: four.
- Dialogue is one authored continuity; no dialogue wheel, morality route, affinity-response system, romance route/system, or selectable protagonist personality.
- **Current player level cap: 70.** Any older repository summary still stating an absolute Level-60 cap is superseded by the later authority inherited by Audit103.
- Exact quest EXP and the final Level-70 progression rebalance remain deferred; Audit103 explicitly leaves those numbers open.

## Audit103 quest architecture — controlling

- Exactly **6 standalone Character Quests**, one for each permanent party member.
- Character Quests target approximately **30 minutes each**.
- Exactly **3 Character Quest bosses**: Elemental Forecast Construct, Crest Load Warden, Revision Custodian.
- Seyrik, Ilyra, and Torren use authored non-boss Character-Quest climaxes.
- Exactly **10 ordinary non-story/non-Hunt side quests**; the older working target of 12 is retired.
- Each Character Quest grants that character's **Legacy Component** as its primary mechanical reward.
- Character Quests are optional and may not gate mandatory Story Primes, mandatory lore, required abilities, or main-plot comprehension.
- Once unlocked, Character Quests and ordinary side quests remain available until the Chapter 12 point of no return unless explicitly superseded later.
- **Sixfold Volition** is the formal current term; `Sixfold Accord` is deprecated.

Character Quests:
1. Vaelira — **The Sky No One Chose** — after Sixfold Volition — boss: Elemental Forecast Construct.
2. Cyanis — **The Weight of the Crest** — after Chapter 7 — boss: Crest Load Warden.
3. Nimera — **The Archive That Remembers** — after Chapter 8 — boss: Revision Custodian.
4. Seyrik — **The Name That Remains** — after Chapter 8 — no full boss.
5. Ilyra — **Mercy Has a Voice** — after Chapter 9 once optional travel resumes — no full boss.
6. Torren — **The Road That Returns** — after Chapter 10 — no full boss.

Ordinary side quests:
1. Edda Harth — **The Marks We Leave**.
2. Dunmere neighborhood waterkeeper — **The Water Between Houses**.
3. Crown Princess Mirena — **A Measure of Bread**.
4. Ivorybridge bridgekeeper / lampwright — **The Dark Span**.
5. Stonewake forge steward — **One Fire Burning**.
6. Crown Princess Mirena — **The Crown's Debt**.
7. Talia Rell — **The Third Caravan**.
8. Talia Rell — **The Living List**.
9. Edda Harth — **When the Roads Open**.
10. Crown Princess Mirena — **What We Build After**.

## Audit99 random-encounter/runtime authority — inherited where compatible

Audit103 does not erase the tested Audit99 random-encounter implementation. Compatible Audit99 engineering rules remain active, including:
- random encounters use hidden eligible-movement-distance pressure;
- pressure is fed by actual resolved horizontal displacement after collision resolution;
- standing still, wall-pushing with zero displacement, vertical-only displacement, and movement-disabled displacement do not count;
- menus/cutscenes/dialogue/authored pauses suspend pressure;
- maximum **8 simultaneously active enemies**;
- exact immediate formation repeats are suppressed when alternatives exist;
- transient random-encounter handoff is not serialized into saves;
- area tuning retains same-ecology / new-ecology / safe-reset semantics;
- Greenhollow's old proof conversion remains engineering-only rather than production canon.

Any Audit98/Audit99 player-level progression values that depended on a Level-60 cap are subordinate to the later **Level-70** authority and the still-pending final progression rebalance.

## World / map authority

The exact approved Yahtrea map remains the controlling surface-world visual/spatial master. Do not move, regenerate, reinterpret, simplify, add, remove, or reconnect geography unless explicitly approved.

Formal modern Realms:
- **The Westways** — west; supersedes Edgelands as the regional name.
- **The Greyspires** — north / northern mountain region; supersedes Diysereach as the regional name.
- **The Crownhold** — capital/royal-core region; supersedes Southhold as the regional name.

All existing settlement and landmark names remain unchanged by the regional terminology correction.

## Post-Audit103 class-rework package — APPROVED, PENDING VALID CANON PROMOTION

The following are approved design decisions developed after Audit103. They must be preserved for the next valid canon promotion, but this summary does not misnumber them as Audit100.

### CL13 class architecture
- Base Class cap = **CL13**.
- Subclass cap = **CL13**.
- Base/Subclass CEXP are separate and go only to the selected class.
- Recruited permanent characters receive full selected-class CEXP whether active or reserve.
- Cumulative CEXP thresholds: CL1 0; CL2 150; CL3 350; CL4 600; CL5 950; CL6 1350; CL7 1800; CL8 2300; CL9 2850; CL10 3450; CL11 4150; CL12 4950; CL13 6000.
- Retired 4,800-CEXP CL12 model must not return.

### Global Ability weapon rule
**No Ability or Ultimate requires a particular equipped weapon.** Once learned, Abilities remain usable under any otherwise-legal loadout. Equipment still controls ordinary Attack, stats, slot geometry, Relic/Legacy legality, and presentation. If a technique visually implies a weapon not equipped, it uses an authored manifested/projected expression instead of disabling the command.

### Final reciprocal Subclasses
- **Cyanis — Crest Knight / Crest Arcanist**
- **Vaelira — Green Arcanist / Axiomblade**
- **Ilyra — Blue Warden / Vowblade**
- **Seyrik — Ruin Vanguard / Ruin Warden**
- **Torren — War Archer / Routeweaver**
- **Nimera — Cardweaver / Truthshot**

Key formula/state locks:
- Vowblade damaging Abilities = **50% Attack / 50% Spirit Hybrid**.
- Ruin Warden Siphon Rune = one hit, **60% Attack / 40% Magic Hybrid**.
- Routeweaver damaging Abilities = **50% Attack / 50% Magic Hybrid**.
- Hunter's Measure is shared between Torren and Nimera.
- Diysean Appraisal remains information reveal only; there is no `Appraised` status.
- Indexed remains separate.

### Mastery / Synthesis
- Mastery architecture = **4 Core + 4 Subclass + 1 Synthesis**, each costing 1 MP; banking is legal.
- **Equipment Mastery = Subclass Mastery Node 4 at Subclass CL10** and grants donor Relic access.
- Exact Core Mastery effects/final Core gate reconciliation remain open.
- Synthesis requires Base CL13 + Subclass CL13 + all eight prior Masteries + authored resolution requirement + 1 unspent MP.
- Synthesis purchase is individual and persistent; it does not create a third class, merge stat packages, activate both Traits, add actions/slots/Card slots/gauges, or create weapon requirements.

Final Synthesis names:
- Cyanis — **Unified Crest**
- Vaelira — **Unified Spectrum**
- Ilyra — **Mercy Unbroken**
- Seyrik — **Tempered Ruin**
- Torren — **Measured Passage**
- Nimera — **Living Proof**

### Mandatory late-Chapter-11 Synthesis-resolution beats
- Cyanis ⇄ Vaelira — **What Holds, What Changes** — Cresthaven staging.
- Ilyra ⇄ Seyrik — **Keep Them Alive** — Forward Hub treatment/recovery staging.
- Torren ⇄ Nimera — **Enough to Move** — Forward Hub operations/map-table staging.

These are mandatory authored continuity, not romance/affinity/player-choice scenes. Exact final dialogue and scene numbering remain for later script integration.

### Approved Legacy identities / reciprocal eligibility
- Crest Knight — **Stillpoint Aegis** — Shield.
- Green Arcanist — **Living Prism** — Focus.
- Blue Warden — **Mercy's Boundary** — Shield.
- Ruin Vanguard — **Purposebound** — Two-Handed Sword.
- War Archer — **Known Ground** — Great Bow.
- Cardweaver — **Decisive Record** — one-slot Conduit.

The reciprocal Synthesis eligibility mapping remains approved in the pair-specific Legacy specs.

### Legacy reconciliation gate before canon promotion
Audit103 already locks **six character-specific Legacy Components as Character-Quest rewards**. The newer class-rework work also approves a shared Cresthaven physical-Legacy pickup presentation. These two approved layers must be reconciled explicitly before the Legacy **acquisition presentation** is promoted into v1.89 / Audit104 so no Character-Quest reward is orphaned or silently superseded.

Until that reconciliation is approved:
- Legacy names, families, reciprocal Synthesis eligibility, and slot geometry remain approved design;
- the exact final relationship between each Character Quest Legacy Component and the Chapter-12 Cresthaven physical Legacy release remains the one unresolved integration point in the Legacy acquisition chain.

## Immediate next canon work

1. Reconcile **Audit103 Legacy Components** with the newly approved six Legacy items / Cresthaven release.
2. Then issue the class-rework promotion in the next valid slot: **v1.89 / Audit104**, not v1.85 / Audit100.
3. Reconcile Core Mastery effect text and final Core gates.
4. Finalize global direct-damage-reduction stacking.
5. Finalize the universal Ultimate MP-cost convention.
6. Perform the deliberate repository-wide `Sixfold Accord` → **Sixfold Volition** terminology sweep.
7. Run class/equipment/Mastery/Synthesis/Legacy implementation-data regression after the valid canon promotion.

Omission from this implementation-facing summary does not erase compatible older canon. Exact approved visual masters, v1.88 / Audit103 quest authority, compatible Audit99 engineering authority, and newer explicit user corrections control conflicts.