# Diyse — Class Rework Current-State Update

**Date:** August 21, 2026  
**Status:** ACTIVE WORKING CONSOLIDATION — NOT MASTER CANON  
**Whole-project authority:** v1.84 / Audit99 plus all newer explicit user approvals and corrections.  
**Purpose:** provide one current handoff/update file containing the active class-rework architecture, approved decisions, current working proposals, and open items without forcing a reader to reconstruct the state from several separate trackers.

> This file consolidates the active working state. Detailed source specs remain authoritative for their own exact sections where they contain more detail, but this file should be updated whenever a class-rework approval materially changes the current state.

---

## 1. Terminology correction

The event formerly called the **Sixfold Accord** is now formally **The Sixfold Volition**.

- No Subclass exists before the Sixfold Volition.
- All Subclasses unlock at the Sixfold Volition.
- After the Volition, the six permanent party members begin training one another through the reciprocal donor relationships below.
- Any remaining `Sixfold Accord` wording in older working files is terminology debt only and is superseded by **Sixfold Volition**.

---

## 2. Global class architecture

### Class caps

- **Base Class cap: CL13.**
- **Subclass cap: CL13.**
- Character level cap remains **60**.
- Campaign-only completion target remains around character Level **55**, leaving Levels 56–60 useful for optional completion and split-focus players.

### Permanent class rules

- Base and Subclass CEXP are separate from Character EXP.
- Only the character's currently selected class receives CEXP.
- The unselected class receives 0 CEXP.
- All recruited permanent party members receive 100% CEXP for their selected class whether active or reserve.
- No participation requirement exists for reserve-party CEXP.
- Unrecruited characters do not gain invisible CEXP; they join at authored starting Base CL thresholds.
- Once an equipment permission or ability is legally unlocked, it remains available under the open-equipment / persistent-ability rules unless a specific rule says otherwise.

### Reciprocal training pairs

- **Cyanis ⇄ Vaelira**
- **Ilyra ⇄ Seyrik**
- **Torren ⇄ Nimera**

These are training/equipment relationships, not social exclusivity rules.

---

## 3. Universal CL13 learning schedules

### Base Class schedule

| Base CL | Major result |
|---:|---|
| CL1 | Trait I + Base Abilities 1–3 + starting equipment |
| CL2 | normal growth |
| CL3 | Base Ability 4 |
| CL4 | normal growth |
| CL5 | native advanced equipment permission where a real one exists |
| CL6 | Base Ability 5 + Trait II |
| CL7 | normal growth |
| CL8 | normal growth |
| CL9 | Base Ability 6 |
| CL10 | normal growth |
| CL11 | normal growth |
| CL12 | Trait III |
| CL13 | Base Ultimate |

Do not fabricate a CL5 equipment reward for symmetry when the Base tradition has no honest new permission.

### Subclass schedule

| Subclass CL | Major result |
|---:|---|
| CL1 | donor basic Primary + Trait I + Ability 1 |
| CL2 | normal growth |
| CL3 | donor Armor |
| CL4 | Ability 2 |
| CL5 | donor native advanced equipment permission / Secondary package where applicable |
| CL6 | Trait II |
| CL7 | Ability 3 |
| CL8 | normal growth |
| CL9 | Ability 4 |
| CL10 | normal growth; Equipment Mastery becomes eligible separately |
| CL11 | Ability 5 |
| CL12 | Trait III |
| CL13 | Subclass Ultimate |

Each Subclass therefore contains **five normal abilities**, a three-rank Trait, and one Ultimate.

---

## 4. CEXP working model

Shared Base/Subclass cumulative thresholds remain:

| CL | Cumulative CEXP | To next |
|---:|---:|---:|
| 1 | 0 | 150 |
| 2 | 150 | 200 |
| 3 | 350 | 250 |
| 4 | 600 | 350 |
| 5 | 950 | 400 |
| 6 | 1,350 | 450 |
| 7 | 1,800 | 500 |
| 8 | 2,300 | 550 |
| 9 | 2,850 | 600 |
| 10 | 3,450 | 700 |
| 11 | 4,150 | 800 |
| 12 | 4,950 | 1,050 |
| 13 | **6,000** | — |

### Recruitment Base CLs

- Cyanis — Ch0, CL1.
- Ilyra — Ch0, CL1.
- Torren — Ch1, CL4 working.
- Nimera — Ch3, CL4 working.
- Vaelira — Ch4, CL7 working.
- Seyrik — Ch6, **CL8 explicit decision**.

### Fresh post-Volition Subclass pacing proof

A mostly Subclass-focused path is expected to land approximately at:

- end Ch7: CL5;
- end Ch8: CL7;
- end Ch9: CL9;
- end Ch10: CL10 / Equipment Mastery eligibility;
- Ch11: CL11 then CL12;
- Ch12: CL13 / Ultimate.

The detailed chapter encounter averages and authored-combat budgets remain in `docs/CLASS_CEXP_WORKING_MODEL.md`.

---

## 5. Mastery / Relic / Legacy working model

The inherited board remains **9 one-point nodes**:

- 4 Core Mastery nodes;
- 4 Subclass Mastery nodes;
- 1 Synthesis node.

Inherited MP grants remain the working basis at character Levels 5, 10, 15, 20, 27, 34, 42, 50 plus 1 MP from the Sixfold Volition, for exactly 9 MP total. Unspent MP may be banked.

### Current working eligibility

- Core 1 — Base CL3 *(proposal)*
- Core 2 — Base CL5 *(proposal)*
- Core 3 — Base CL7 *(proposal)*
- Core 4 — Base CL9 *(proposal)*
- Subclass 1 — Subclass CL3 *(proposal)*
- Subclass 2 — Subclass CL5 *(proposal)*
- Subclass 3 — Subclass CL7 *(proposal)*
- **Subclass 4 / Equipment Mastery — Subclass CL10 — explicit approved decision**

### Equipment Mastery — approved global rule

- Equipment Mastery remains Subclass Mastery Node 4.
- Reaching Subclass CL10 makes the node eligible.
- Spending 1 MP on it grants legal access to the donor Base tradition's **Relic**.
- Ordinary donor equipment is learned earlier through Subclass CL1–5.
- Legacy access is later and separate.

### Synthesis — current proposal

Leading rule remains:

- Base CL13;
- Subclass CL13;
- all 4 Core nodes purchased;
- all 4 Subclass nodes purchased;
- character-specific resolution/story gate complete;
- 1 MP available to buy Synthesis.

Legacy permission is intended to sit downstream of Synthesis / full completion. Exact Legacy wording and character resolution conditions remain open.

---

## 6. Base equipment identities

| Character | Base Class | Primary | Secondary / slot rule |
|---|---|---|---|
| Cyanis | Crest Knight | Swords | Shield; second Sword unlocked as advanced permission |
| Ilyra | Blue Warden | **Wardrods** | Focus; Shield unlocked as advanced permission |
| Torren | War Archer | **Great Bows** | Great Bow occupies Weapon + Secondary |
| Nimera | Cardweaver | Conduits | Focus if Secondary is free; two-handed Conduits occupy both slots |
| Vaelira | Green Arcanist | Arcane Staffs | Focus |
| Seyrik | Ruin Vanguard | Two-Handed Swords | occupies Weapon + Secondary |

Important: donor equipment is not cherry-picked. The recipient learns the donor Base tradition's complete legal ordinary equipment package and native advanced permission, staged by Subclass CL.

---

## 7. Current Subclass pair status

### Cyanis ← Vaelira

**Preserve-first working identity: Crest Magus.** Existing authored mechanics remain the starting point rather than a total redesign.

Current preserve-first spine:
- Geometric Lance
- Crest Lattice
- Nullifying Seal
- Pattern Collapse
- Trait: Geometric Authority
- Ultimate: Perfect Geometry

Needs the fifth normal Subclass ability and final CL13 rebalance.

### Vaelira ← Cyanis

**APPROVED subclass name: AXIOMBLADE.**  
**Pairing:** **Vaelira — Green Arcanist / Axiomblade**.

Explicitly approved architecture:
- no ordinary ally intercept;
- CL4 normal ability is an **attack**;
- subclass remains offensive/martial rather than turning Vaelira into a second Cyanis;
- her advanced subclass attack must work with her native **Arcane Staff** as well as learned Swords;
- **Staff + Focus** and **Staff + Shield** are required supported advanced-loadout expressions;
- exact Power, MP, durations, penetration values, and other balance numbers remain provisional unless separately approved.

Current working Axiomblade spine:

**Trait — Prismatic Discipline** *(working name)*
- Rank I: recent standard-element damage can elementalize the next damaging Axiomblade ability through the following round; no new gauge.
- Rank II: current proposal rewards Crested Advance / Refracted Counter momentum.
- Rank III: current proposal grants penetration when an elementalized attack hits a matching existing Imprint.

**CL1 — Prism Edge** *(working)*
- basic Sword attack that may inherit the recent standard element.

**CL4 — Crested Advance** *(role approved; exact values provisional)*
- direct attack, not guard/intercept;
- current proposal adds self Defense/Spirit reinforcement and optional matching Elemental Guard after the hit.

**CL7 — Refracted Counter** *(working)*
- one true prepared self-counter technique;
- lower raw counter Power than Cyanis, but can elementalize.

**CL9 — Prismatic Rend** *(working)*
- heavy penetration attack;
- current proposal gains extra payoff against a matching existing Imprint.

**CL11 — Crest Form** *(loadout architecture approved; numbers provisional)*
Must support all of:
- Sword;
- Sword + Shield;
- dual Swords;
- Arcane Staff;
- Arcane Staff + Focus;
- Arcane Staff + Shield.

Current working expressions:
- Sword: neutral Physical form;
- Sword + Shield: lower Power + self damage reduction;
- dual Swords: two-hit Physical form;
- Staff: neutral Magical form;
- Staff + Focus: Magical form with Spirit penetration;
- Staff + Shield: lower Magical Power + self damage reduction.

**CL13 — Prism Bastion** *(working proposal, not approved lock)*
- choose one standard element;
- Sword expression = Physical AoE;
- Staff expression = Magical AoE;
- current proposal includes relevant-defense penetration and matching party Elemental Guard;
- does not duplicate Arcanum Ascendant's Imprint/Field package or Cyanis's broad cleanse/Defense/Spirit package.

Current working Axiomblade Mastery proposals:
- CL3 Tempered Spectrum;
- CL5 Forward Geometry;
- CL7 Return Angle;
- CL10 Equipment Mastery → Crest Knight donor Relic.

### Ilyra ← Seyrik

**Preserve-first working identity: Vowblade.**

Existing spine:
- Vital Edge
- Mercy Returned
- Living Covenant
- Vowguard Reprisal
- Trait: Living Edge
- Ultimate: Mercy's Final Edge

Needs Ability 5 and final CL13 rebalance. Ilyra learns Seyrik's two-handed Sword / Ruin equipment tradition through donor progression while retaining her own unlocked Wardrod / Focus / Shield permissions under open equipment.

### Seyrik ← Ilyra

**Preserve-first working identity: Ruin Reclaimer.** Do not restore the retired `Ruin Healer` framing.

Existing spine:
- Siphon Rune
- Stolen Grace
- Blue Reclamation
- Withering Mercy
- Trait: Reclaimer's Mercy
- Ultimate: Mercy Through Ruin

Needs Ability 5 and final CL13 rebalance.

### Torren ← Nimera

**Preserve-first working identity: Routeweaver.**

- Torren learns Nimera's actual Cardweaver / Conduit equipment concept.
- Donor progression includes one-slot Conduits, Cardweaver armor, then two-handed Conduits + legal Focus access where applicable.
- Routeweaver remains a hybrid physical/magical field-control and selective Card-support identity, not a copy of Nimera's Base support kit.
- Needs Ability 5 and final CL13 rebalance.

### Nimera ← Torren

**Active redesign. Leading working name: Truthshot.**  
**Truthshot is NOT final canon locked yet.**

Equipment:
- CL1 Great Bows, occupying Weapon + Secondary;
- CL3 War Archer armor;
- no fabricated CL5 Secondary;
- CL10 Equipment Mastery → War Archer donor Relic.

Working stat package:
- Attack +8%
- Accuracy +8%
- Speed +6%
- Defense -6%

Working ability spine:
- CL1 **Measured Shot** — applies shared Hunter's Measure; direct Diysean Appraisal info check may improve accuracy; no Appraised status.
- CL4 **Held Argument** — prepared interrupt shot; stronger against Hunter's Measure.
- CL7 **Pin the Variable** — Speed Down/control attack; Measure improves reliability/penetration.
- CL9 **Structural Failure** — heavy Defense-penetrating attack, strong against structural targets.
- CL11 **Corroboration** — four-hit pressure; later hits improve against Measure.
- Trait **Applied Evidence** — Accuracy → Crit → penetration progression against Measure.
- Ultimate **Final Annotation** — high-accuracy, high-penetration decisive shot with Measure/hard-target payoff; does not consume Measure.

Hunter's Measure is shared between Torren and Nimera. Either can apply it and either can exploit the other's application. Diysean Appraisal remains information reveal only; Indexed remains the separate Card-specific state.

---

## 8. Base class identities / CL placement snapshot

### Cyanis — Crest Knight
CL1 Crest Strike / Guardian Sigil / Harmonizing Ward; CL3 Resolute Counter; CL5 second Sword; CL6 Crest Rush; CL9 Crest Rend; CL13 Crest of Companions.

### Ilyra — Blue Warden
CL1 Mend / Clear Warding / Renewal; CL3 Warden's Valor; CL5 Shield; CL6 Revive; CL9 Lifeline; CL13 Dawn Without End.

### Torren — War Archer
CL1 Driving Strike / Quarry Appraisal / Watchful Aim; CL3 Pinning Strike; CL5 unresolved honest native reward; CL6 Colossus Draw; CL9 Relentless Barrage; CL13 The Great Beast Falls.

### Nimera — Cardweaver
CL1 Diysean Appraisal / Weave Guard / Prepared Thread; CL3 Ancient Override; CL5 two-handed Conduits; CL6 Face Concordance; CL9 Sovereign Index; CL13 Grand Reweaving.

### Vaelira — Green Arcanist
CL1 Core Element Array / Shaping Element Array / Prism Cycle; CL3 Composite Surge; CL5 Focus remains leading candidate; CL6 Elemental Field; CL9 Sixfold Ray; CL13 Arcanum Ascendant.

### Seyrik — Ruin Vanguard
CL1 Ruin Cleave / Rift Lance / Ember Brand; CL3 Fracturing Brand; CL5 unresolved honest native reward; CL6 Unmaking Blow; CL9 Call Shardfang; CL13 Controlled Apocalypse.

Full exact effect text remains in the detailed class tracker / combat rules and should not be silently rewritten from this summary.

---

## 9. Current approved vs provisional boundary

### Explicit approvals / current hard working decisions

- Base CL13.
- Subclass CL13.
- Sixfold Volition terminology and all-Subclass unlock function.
- Reciprocal pairs Cyanis⇄Vaelira, Ilyra⇄Seyrik, Torren⇄Nimera.
- Open equipment / persistent unlocked ability behavior.
- Full donor ordinary-equipment package; no cherry-picking.
- Reserve recruited permanent characters receive full selected-class CEXP.
- Seyrik joins Base CL8.
- Equipment Mastery remains Subclass Node 4 and becomes eligible at Subclass CL10.
- Equipment Mastery grants donor Relic access.
- Legacy remains later than Relic / tied to full completion-Synthesis architecture.
- Ilyra primary weapon family is Wardrods; Shield or Focus secondary identity.
- Vaelira subclass name **Axiomblade**.
- Axiomblade has no ordinary ally intercept.
- Axiomblade CL4 is an attack.
- Axiomblade advanced attack supports Staff, Staff+Focus, Staff+Shield as well as learned Sword forms.

### Still provisional / needs explicit approval or final balance pass

- most exact CEXP rewards by individual formation/boss/Hunt;
- Core Mastery CL3/5/7/9 gates;
- Subclass Mastery Nodes 1–3 CL3/5/7 gates;
- Synthesis exact story conditions;
- Legacy exact wording;
- Torren and Seyrik Base CL5 rewards;
- Vaelira Base CL5 Focus final lock;
- Torren/Nimera and Vaelira/Cyanis detailed Mastery effects except global Equipment Mastery rule;
- all Axiomblade exact numbers and most ability names except the subclass name and explicit role/loadout approvals;
- Truthshot name and all Truthshot exact numbers;
- fifth abilities for the four preserve-first Subclasses;
- final global Ultimate MP/cost convention.

---

## 10. Active source files

- `docs/CLASS_REWORK_MASTER_TRACKER.md`
- `docs/CLASS_CEXP_WORKING_MODEL.md`
- `docs/CLASS_MASTERY_WORKING_MODEL.md`
- `docs/NIMERA_TORREN_SUBCLASS_WORKING_SPEC.md`
- `docs/VAELIRA_CYANIS_SUBCLASS_WORKING_SPEC.md`
- `docs/COMBAT_RULES.md`
- `docs/ACTIVE_CANON.md`

This update file is the **current class-rework handoff snapshot**. When a new approval changes the class-rework state, update both the relevant detailed source file and this consolidation file so later work can resume from one clean reference.
