# Diyse — Class Rework Current Update — 2026-08-21

**Status:** ACTIVE CLASS-REWORK CONSOLIDATION — APPROVED ITEMS BELOW ARE NOT YET PROMOTED INTO A NEW WHOLE-PROJECT MASTER-CANON AUDIT  
**Parent whole-project authority:** v1.84 / Audit99 plus newer explicit class-rework decisions.  
**Purpose:** one current handoff/update file collecting the active class-rework architecture, explicit approvals, unresolved items, and the current state of all six reciprocal Subclass paths.

## Approval sweep — August 21, 2026

The user explicitly clarified that the class-rework proposals advanced under repeated **“Let’s continue”** responses in this sequence are approvals, not merely permission to keep brainstorming.

**Conflict rule:** when a later pass refined or replaced an earlier version, the **latest refinement controls** and the older contradictory draft is superseded.

The approval sweep currently covers the material actually designed for:
- **Cyanis — Crest Knight / Crest Arcanist** — approved full current package;
- **Vaelira — Green Arcanist / Axiomblade** — approved full current package;
- **Ilyra — Blue Warden / Vowblade** — approved full current package;
- **Seyrik — Ruin Vanguard / Ruin Reclaimer** — approved mechanical CL13 package; naming polish remains open;
- **Torren — War Archer / Routeweaver** — approved preserve-first identity/equipment/spine; CL11/final numerical rebase remains open rather than invented;
- **Nimera — Cardweaver / Truthshot** — approved full current package.

Detailed files:
- `docs/CYANIS_VAELIRA_SUBCLASS_WORKING_SPEC.md`
- `docs/VAELIRA_CYANIS_SUBCLASS_WORKING_SPEC.md`
- `docs/ILYRA_SEYRIK_SUBCLASS_WORKING_SPEC.md`
- `docs/SEYRIK_ILYRA_SUBCLASS_WORKING_SPEC.md`
- `docs/TORREN_NIMERA_SUBCLASS_WORKING_SPEC.md`
- `docs/NIMERA_TORREN_SUBCLASS_WORKING_SPEC.md`

---

## 1. Current architecture

- Base Class cap: **CL13**.
- Subclass cap: **CL13**.
- Base and Subclass CEXP are separate.
- CEXP goes only to the currently selected class.
- All recruited permanent characters receive full CEXP to their selected class whether active or reserve.
- No Subclass exists before the **Sixfold Volition**.
- At the Sixfold Volition, all six Subclasses unlock and the permanent party begins reciprocal cross-training.
- Reciprocal pairs: **Cyanis ⇄ Vaelira**, **Ilyra ⇄ Seyrik**, **Torren ⇄ Nimera**.
- Equipment and unlocked abilities remain persistently usable under the open-equipment/open-ability rules; Subclass selection controls its stat package, Trait, and Subclass-only abilities.
- Equipment slots remain **Weapon / Secondary / Armor**.

### Terminology

The current event/system name is **Sixfold Volition**. Remaining `Sixfold Accord` wording is stale terminology and should be treated as superseded.

---

## 2. Class EXP / CL13 model

### Character-level pacing target

| Chapter | Character level target |
|---|---|
| Ch0 | no EXP |
| Ch1 | 1 → 5 |
| Ch2 | 5 → 9 |
| Ch3 | 9 → 13 |
| Ch4 | 13 → 17 |
| Ch5 | 17 → 22 |
| Ch6 | 22 → 27 |
| Ch7 | 27 → 32 |
| Ch8 | 32 → 37 |
| Ch9 | 37 → 42 |
| Ch10 | 42 → 47 |
| Ch11 | 47 → 53 |
| Ch12 | launch around 53, campaign-only finish around 55; hard cap 60 |

### Recruitment / starting Base CL

| Character | Recruitment | Starting Base CL |
|---|---|---:|
| Cyanis | Ch0 | CL1 |
| Ilyra | Ch0 | CL1 |
| Torren | Ch1 | CL4 *(working)* |
| Nimera | Ch3 | CL4 *(working)* |
| Vaelira | Ch4 S022 | CL7 *(working)* |
| Seyrik | Ch6 | **CL8 approved** |

### CL thresholds

CL1 0; CL2 150; CL3 350; CL4 600; CL5 950; CL6 1350; CL7 1800; CL8 2300; CL9 2850; CL10 3450; CL11 4150; CL12 4950; CL13 6000.

The retired 4,800-CEXP CL12 table must not return.

### Fresh Subclass pacing after Volition

- Ch7: 978 → CL5
- Ch8: 1978 → CL7
- Ch9: 2946 → CL9
- Ch10: 4050 → CL10
- Ch11: 5308 → CL12
- Ch12: 6008 → CL13

This places Equipment Mastery around end-Ch10, Ability 5 in Ch11, Trait III later Ch11, and Ultimate in Ch12.

### Universal Subclass schedule

| Subclass CL | Unlock |
|---:|---|
| CL1 | donor basic Primary + Trait I + Ability 1 |
| CL3 | donor Armor |
| CL4 | Ability 2 |
| CL5 | donor native advanced equipment / Secondary package where real |
| CL6 | Trait II |
| CL7 | Ability 3 |
| CL9 | Ability 4 |
| CL10 | Equipment Mastery eligibility separately |
| CL11 | Ability 5 |
| CL12 | Trait III |
| CL13 | Ultimate |

Subclasses use five normal abilities.

---

## 3. Mastery / equipment model

- Nine-point inherited architecture: **4 Core + 4 Subclass + 1 Synthesis**, each costing 1 MP.
- Working Core gates: CL3 / CL5 / CL7 / CL9.
- Working Subclass gates: CL3 / CL5 / CL7 / **CL10**.
- **Equipment Mastery is explicitly approved as Subclass Node 4 at CL10** and grants the donor Relic.
- Ordinary donor equipment arrives earlier through CL1–5.
- Legacy access remains later and downstream of Synthesis/full completion.
- Banking Mastery Points is legal.

A donor passes the donor Base tradition's **complete legal ordinary equipment package**; do not cherry-pick and do not chain permissions beyond the reciprocal partner.

| Recipient | Donor progression |
|---|---|
| Vaelira ← Cyanis | Swords → Crest armor → Shield + second-Sword permission |
| Cyanis ← Vaelira | Arcane Staffs → Green Arcanist armor → Focus |
| Seyrik ← Ilyra | Wardrods → Warding armor → Shield + legal Blue Warden Secondary package |
| Ilyra ← Seyrik | Two-Handed Swords → Ruin armor; no fake CL5 family |
| Torren ← Nimera | one-slot Conduits → Cardweaver armor → two-handed Conduits + Focus where legal |
| Nimera ← Torren | Great Bows → War Archer armor; no fabricated CL5 Secondary |

---

## 4. Approved reciprocal subclass packages

### Cyanis ← Vaelira — APPROVED Crest Arcanist

**Pairing:** **Cyanis — Crest Knight / Crest Arcanist**.  
Approved stats: **MP +10% / Magic +10% / Spirit +6% / Attack -6%**.

Approved progression:
- Trait **Crest Resonance**;
- CL1 **Arcane Lance** + **Crest Attunement**;
- CL4 **Warding Crest**;
- CL7 **Nullifying Seal**;
- CL9 **Arcane Rupture**;
- CL11 **Elemental Convergence**;
- CL13 **Crest Dominion**.

Approved Mastery: **Arcane Force / Warded Ground / Sealbreaker / Equipment Mastery**.

Key approved mechanics include Colorless magical penetration, specialized Crest Fields/seals, anti-structure control, the chosen-standard-element CL11 attack, and Crest Dominion's hostile-Field removal/suppression plus Dominion Crest Field.

Detailed authority: `docs/CYANIS_VAELIRA_SUBCLASS_WORKING_SPEC.md`.

### Vaelira ← Cyanis — APPROVED Axiomblade

**Pairing:** **Vaelira — Green Arcanist / Axiomblade**.  
Approved stats: **HP +6% / Attack +6% / Magic +6% / Defense +8% / Speed -6%**.

Approved progression:
- Trait **Formal Equivalence**;
- CL1 **First Principle**;
- CL4 **Proven Advance**;
- CL7 **Counterproof**;
- CL9 **Axiom Rend**;
- CL11 **Equivalent Form**;
- CL13 **Final Axiom**.

Approved Mastery: **Foundational Proof / Proven Position / Exact Rebuttal / Equipment Mastery**.

Sword expressions are Physical/Defense-facing; Staff expressions are Magical/Spirit-facing. Equivalent Form supports Sword, Sword + Shield, dual Swords, Staff, Staff + Focus, and Staff + Shield. Final Axiom uses a chosen standard element and relevant-defense penetration.

Detailed authority: `docs/VAELIRA_CYANIS_SUBCLASS_WORKING_SPEC.md`.

### Ilyra ← Seyrik — APPROVED Vowblade

**Pairing:** **Ilyra — Blue Warden / Vowblade**.  
Approved stats: **HP +8% / Attack +10% / Spirit +8% / Defense -6%**.

Approved progression:
- Trait **Mercy in Steel**;
- CL1 **Vital Edge**;
- CL4 **Mercy Returned**;
- CL7 **Living Covenant**;
- CL9 **Vowkeeper's Reprisal**;
- CL11 **Vow of Severance**;
- CL13 **Mercy's Final Edge**.

Approved Mastery: **Steeled Mercy / Mercy Carried / Unbroken Covenant / Equipment Mastery**.

Damaging Vowblade abilities use authored **50% Attack / 50% Spirit Hybrid** scaling and work with Wardrods or learned Two-Handed Swords. Vowblade uses Ruin-influenced technique/presentation but does not create a seventh Ruin damage element.

Detailed authority: `docs/ILYRA_SEYRIK_SUBCLASS_WORKING_SPEC.md`.

### Seyrik ← Ilyra — APPROVED Ruin Reclaimer mechanical package

**Pairing:** **Seyrik — Ruin Vanguard / Ruin Reclaimer**. Do not restore `Ruin Healer`.  
Approved stats: **HP +6% / MP +8% / Magic +6% / Spirit +6% / Speed -4%**.

Approved equipment:
- CL1 Wardrods;
- CL3 Warding / Blue Warden armor;
- CL5 Shield + legal Focus access;
- CL10 Equipment Mastery → Blue Warden donor Relic.

Approved current progression/mechanics:
- Trait **Reclaimer's Mercy** — Drain recovery sharing starts at 15%, rises to 25% at Rank II, and Rank III adds +10 Total Defense to direct Ruin Reclaimer healing recipients under inherited timing;
- CL1 **Siphon Rune** — 165 Hybrid / 8 MP; 35% Drain recovery capped at 20% Max HP;
- CL4 **Stolen Grace** — 170 Colorless Magical / 10 MP; chosen ally heals from 30% of eligible damage + 0.35× Spirit, capped at 25% Max HP;
- CL7 **Blue Reclamation** — 10 MP; 18% Max HP + 0.90× Spirit heal, remove 1 ordinary harmful status, +10 Total Defense through following round;
- CL9 **Withering Mercy** — 150 Colorless Magical AoE / 18 MP / 2-round cooldown; distributes healing equal to 12% of total eligible damage, capped at 15% Max HP per ally;
- CL11 **Reclaimed Breath** — 24 MP; revive one incapacitated permanent ally at 25% Max HP; no summons/devices/Prime Manifestations;
- CL13 **Mercy Through Ruin** — 320 Colorless Magical AoE; all conscious allies heal 25% Max HP + 1.00× Spirit, remove 1 ordinary harmful status, and gain +20 Total Defense for 2 rounds.

Approved Mastery: **Deeper Siphon** (35%→40% Siphon recovery) / **Shared Grace** (0.35→0.45 Spirit coefficient) / **Pure Reclamation** (Blue Reclamation removes one additional ordinary harmful status) / **Equipment Mastery**.

The mechanics are approved. A naming-polish pass remains open and may reduce repeated `Reclaimer / Reclamation / Reclaimed / Mercy` language without reopening the kit.

Detailed authority: `docs/SEYRIK_ILYRA_SUBCLASS_WORKING_SPEC.md`.

### Torren ← Nimera — APPROVED Routeweaver preserve-first package

**Pairing:** **Torren — War Archer / Routeweaver**.

Approved identity/equipment:
- Routeweaver is the retained subclass name and identity;
- Torren learns Nimera's actual Cardweaver/Conduit tradition;
- CL1 one-slot Conduits;
- CL3 Cardweaver armor;
- CL5 two-handed Conduits + Focus where legal;
- CL10 Equipment Mastery → Cardweaver donor Relic;
- subclass remains hybrid physical/magical field-control with selective Card support, not a Cardweaver copy.

Approved preserve-first spine:
- **Throughline**;
- **Clear Route**;
- **Crossroads**;
- **Covered Crossing**;
- Trait **Field Weaving**;
- Ultimate **Open the Way**.

The required CL11 fifth normal ability and final CL13 numerical rebase remain open; approval does not fabricate missing content.

Detailed authority: `docs/TORREN_NIMERA_SUBCLASS_WORKING_SPEC.md`.

### Nimera ← Torren — APPROVED Truthshot

**Pairing:** **Nimera — Cardweaver / Truthshot**. The old Sixfold Knight direction is superseded.  
Approved stats: **Attack +8% / Accuracy +8% / Speed +6% / Defense -6%**.

Approved equipment:
- CL1 Great Bows occupying Weapon + Secondary;
- CL3 War Archer armor;
- no fake CL5 Secondary;
- CL10 Equipment Mastery → War Archer donor Relic.

Approved progression:
- Trait **Applied Evidence**;
- CL1 **Measured Shot** — 120 Physical / 6 MP; applies Hunter's Measure for 2 rounds; +10 Base Hit if Diysean Appraisal has already revealed permitted target data;
- CL4 **Held Argument** — 150 Physical / 8 MP Prepared interrupt response; gains Measure reliability bonuses;
- CL7 **Pin the Variable** — 145 Physical / 9 MP; Speed Down; Measure improves application and penetration;
- CL9 **Structural Failure** — 210 Physical / 12 MP; 35% Defense penetration; +15% final damage against authored structural/hard-point categories; Measure adds accuracy;
- CL11 **Corroboration** — four hits ×60 = 240 Physical / 14 MP; later hits gain cumulative Hit/Crit against Measure;
- CL13 **Final Annotation** — 360 Physical; +20 Base Hit; 50% Defense penetration; +20% final damage against Measure; +15% against approved hard-target categories; does not consume Measure.

Approved Trait ranks against Hunter's Measure: **+10 Base Hit → +10% Crit → +15% Defense penetration**.

Approved Mastery: **Exact Measure / Prepared Proof / Hard Evidence / Equipment Mastery**.

Hunter's Measure is shared between Torren and Nimera. Either can apply it and either can exploit the other's application. Diysean Appraisal remains information reveal only; there is no `Appraised` status. Indexed remains separate.

Detailed authority: `docs/NIMERA_TORREN_SUBCLASS_WORKING_SPEC.md`.

---

## 5. Base class snapshot

- **Cyanis — Crest Knight:** Crest Strike / Guardian Sigil / Harmonizing Ward / Resolute Counter / Crest Rush / Crest Rend / Crest of Companions.
- **Ilyra — Blue Warden:** Mend / Clear Warding / Renewal / Warden's Valor / Revive / Lifeline / Dawn Without End.
- **Torren — War Archer:** Driving Strike / Quarry Appraisal / Watchful Aim / Pinning Strike / Colossus Draw / Relentless Barrage / The Great Beast Falls.
- **Nimera — Cardweaver:** Diysean Appraisal / Weave Guard / Prepared Thread / Ancient Override / Face Concordance / Sovereign Index / Grand Reweaving.
- **Vaelira — Green Arcanist:** Core Element Array / Shaping Element Array / Prism Cycle / Composite Surge / Elemental Field / Sixfold Ray / Arcanum Ascendant.
- **Seyrik — Ruin Vanguard:** Ruin Cleave / Rift Lance / Ember Brand / Fracturing Brand / Unmaking Blow / Call Shardfang / Controlled Apocalypse.

---

## 6. Immediate open work

- Complete the **Ruin Reclaimer naming-polish pass**, then weapon/loadout and HD-2D presentation audit without reopening its approved mechanics.
- Complete the still-missing **Routeweaver CL11 fifth ability** and final CL13 numerical reconciliation without reopening its approved identity/equipment/spine.
- Reconcile Core/Subclass Mastery effect text after all six kits stabilize.
- Finalize Synthesis / Legacy character-resolution requirements.
- Perform the deliberate global terminology sweep from stale `Sixfold Accord` wording to **Sixfold Volition**.
- Promote the complete class-rework package into a new master-canon audit only after all six reciprocal subclasses are stable.
