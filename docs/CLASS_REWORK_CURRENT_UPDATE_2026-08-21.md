# Diyse — Class Rework Current Update — 2026-08-21

**Status:** ACTIVE WORKING CONSOLIDATION — NOT MASTER CANON  
**Parent whole-project authority:** v1.84 / Audit99 plus newer explicit class-rework decisions.  
**Purpose:** one current handoff/update file collecting the active class-rework architecture, explicit approvals, working proposals, unresolved items, and the current state of all six Base/Subclass paths.

## Approval sweep — August 21, 2026

The user explicitly clarified that the class-rework proposals advanced under their repeated **“Let’s continue”** responses in this sequence are approved. Those responses are therefore no longer to be treated as mere continuation without approval.

**Conflict rule:** when a later “Let’s continue” pass refined or replaced an earlier version, the **latest refinement controls** and the older contradictory draft is superseded.

This approval sweep promotes the current packages for:
- **Cyanis — Crest Knight / Crest Arcanist**;
- **Vaelira — Green Arcanist / Axiomblade**;
- **Ilyra — Blue Warden / Vowblade**.

Detailed approved files:
- `docs/CYANIS_VAELIRA_SUBCLASS_WORKING_SPEC.md`
- `docs/VAELIRA_CYANIS_SUBCLASS_WORKING_SPEC.md`
- `docs/ILYRA_SEYRIK_SUBCLASS_WORKING_SPEC.md`

These are approved within the class-rework project but have **not yet been promoted into a new whole-project master-canon audit**.

---

## 1. Current architecture

- Base Class cap: **CL13**.
- Subclass cap: **CL13**.
- Base and Subclass CEXP are separate.
- CEXP goes only to the currently selected class.
- All recruited permanent characters receive full CEXP to their selected class whether active or reserve.
- No Subclass exists before the **Sixfold Volition**.
- At the Sixfold Volition, all six Subclasses unlock and the permanent party begins reciprocal cross-training.
- Reciprocal pairs:
  - **Cyanis ⇄ Vaelira**
  - **Ilyra ⇄ Seyrik**
  - **Torren ⇄ Nimera**
- Equipment and unlocked abilities remain persistently usable under the open-equipment/open-ability rules; Subclass selection controls the selected class's stat package, Trait, and Subclass-only abilities.
- Equipment slots remain **Weapon / Secondary / Armor**.

### Terminology correction

The current event/system name is **Sixfold Volition**. Any remaining working-file references to **Sixfold Accord** are terminology debt and should be treated as superseded wording, not a separate event.

---

## 2. Class EXP model

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
| Ch12 | launch around 53, finish around 55; hard cap 60 |

### Recruitment / starting Base CL

| Character | Recruitment | Starting Base CL |
|---|---|---:|
| Cyanis | Ch0 | **CL1** |
| Ilyra | Ch0 | **CL1** |
| Torren | Ch1 | **CL4** *(working)* |
| Nimera | Ch3 | **CL4** *(working)* |
| Vaelira | Ch4 S022 | **CL7** *(working)* |
| Seyrik | Ch6 | **CL8** *(explicit current decision)* |

### CL thresholds

| CL | Total CEXP | Next threshold |
|---:|---:|---:|
| 1 | 0 | 150 |
| 2 | 150 | 200 |
| 3 | 350 | 250 |
| 4 | 600 | 350 |
| 5 | 950 | 400 |
| 6 | 1350 | 450 |
| 7 | 1800 | 500 |
| 8 | 2300 | 550 |
| 9 | 2850 | 600 |
| 10 | 3450 | 700 |
| 11 | 4150 | 800 |
| 12 | 4950 | 1050 |
| 13 | 6000 | cap |

The retired 4,800-CEXP CL12 table must not return.

### Ordinary encounter CEXP chapter budgets

Ch1 360; Ch2 456; Ch3 532; Ch4 608; Ch5 720; Ch6 760; Ch7 798; Ch8 810; Ch9 768; Ch10 884; Ch11 1008; Ch12 480. Full total = **8,184**.

Mandatory authored combat budgets currently: 90, 100, 110, 120, 140, 160, 180, 190, 200, 220, 250, 220.

Fresh Subclass path after Volition projects approximately:
- Ch7: 978 → CL5
- Ch8: 1978 → CL7
- Ch9: 2946 → CL9
- Ch10: 4050 → CL10
- Ch11: 5308 → CL12
- Ch12: 6008 → CL13

This places Equipment Mastery around end-Ch10, Ability 5 in Ch11, Trait III later Ch11, and Ultimate in Ch12.

---

## 3. Universal CL13 schedules

### Base

| Base CL | Unlock |
|---:|---|
| CL1 | Trait I + Abilities 1–3 + starting equipment |
| CL2 | normal growth |
| CL3 | Ability 4 |
| CL4 | normal growth |
| CL5 | native advanced equipment permission where real |
| CL6 | Ability 5 + Trait II |
| CL7 | normal growth |
| CL8 | normal growth |
| CL9 | Ability 6 |
| CL10 | normal growth |
| CL11 | normal growth |
| CL12 | Trait III |
| CL13 | Ultimate |

### Subclass

| Subclass CL | Unlock |
|---:|---|
| CL1 | donor basic Primary + Trait I + Ability 1 |
| CL2 | normal growth |
| CL3 | donor Armor |
| CL4 | Ability 2 |
| CL5 | donor advanced equipment / Secondary package where real |
| CL6 | Trait II |
| CL7 | Ability 3 |
| CL8 | normal growth |
| CL9 | Ability 4 |
| CL10 | normal growth; Equipment Mastery becomes eligible separately |
| CL11 | Ability 5 |
| CL12 | Trait III |
| CL13 | Ultimate |

Base kits remain six normal abilities. Subclasses use five normal abilities.

---

## 4. Mastery / Relic / Legacy model

The inherited nine-point architecture remains:
- 4 Core Mastery nodes;
- 4 Subclass Mastery nodes;
- 1 Synthesis node;
- each costs 1 MP.

Working Core gates: CL3 / CL5 / CL7 / CL9.  
Working Subclass gates: CL3 / CL5 / CL7 / **CL10**.

### Explicit decision — Equipment Mastery

- Equipment Mastery remains **Subclass Mastery Node 4**.
- It becomes eligible at **Subclass CL10**.
- Spending 1 MP on it grants access to the donor tradition's **Relic**.
- Ordinary donor equipment comes earlier through Subclass CL1–5.
- Legacy access remains later and downstream of Synthesis/full completion.

### MP sources

Working inherited sources: character Levels 5, 10, 15, 20, 27, Sixfold Volition event, 34, 42, 50 = **9 total MP**.

Banking is legal.

### Synthesis / Legacy

Current leading proposal:
- Base CL13;
- Subclass CL13;
- all four Core nodes;
- all four Subclass nodes;
- character-specific resolution/story condition;
- 1 MP for Synthesis.

Legacy permission is intended to sit downstream of Synthesis / full completion. Exact Legacy wording and character resolution conditions remain open.

---

## 5. Donor-equipment rule

A donor passes the donor Base tradition's **complete legal ordinary equipment package**. Do not cherry-pick individual equipment families and do not chain donor permissions beyond the direct reciprocal partner.

Current donor progression examples:
- Vaelira ← Cyanis: Swords → Crest armor → Shield + second-Sword permission.
- Cyanis ← Vaelira: Arcane Staffs → Green Arcanist armor → Focus.
- Seyrik ← Ilyra: Wardrods → Warding armor → Shield + legal Blue Warden Secondary package.
- Ilyra ← Seyrik: Two-Handed Swords → Ruin armor; no fake extra CL5 family.
- Torren ← Nimera: one-slot Conduits → Cardweaver armor → two-handed Conduits + Focus where legal.
- Nimera ← Torren: Great Bows → War Archer armor; no fabricated CL5 Secondary.

Relics remain separate at Equipment Mastery CL10; Legacies remain later.

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

---

## 7. Current Subclass pair status

### Cyanis ← Vaelira — APPROVED Crest Arcanist

**Pairing:** **Cyanis — Crest Knight / Crest Arcanist**.

Approved selected stat package:
- MP +10%
- Magic +10%
- Spirit +6%
- Attack -6%

Approved naming / progression:
- Trait **Crest Resonance**;
- CL1 **Arcane Lance** + rider **Crest Attunement**;
- CL4 **Warding Crest**;
- CL7 **Nullifying Seal**;
- CL9 **Arcane Rupture**;
- CL11 **Elemental Convergence**;
- CL13 **Crest Dominion**.

Approved Mastery:
- CL3 **Arcane Force**;
- CL5 **Warded Ground**;
- CL7 **Sealbreaker**;
- CL10 **Equipment Mastery** → Green Arcanist donor Relic.

Key approved mechanics:
- Crest Resonance I reduces the first MP-costing Spell-tagged Crest ability each round by 2 MP;
- Rank II grants damaging Colorless Magical Crest abilities +15% Spirit penetration;
- Rank III extends Cyanis-authored Crest Fields/Seals by +1 round up to their approved maximum;
- Arcane Lance = 220 Colorless Magical / 25% Spirit penetration;
- Warding Crest = 3-round specialized resistance/15% tagged direct-damage reduction Field;
- Nullifying Seal = dispel/anti-structure/conditional ordinary-summon Banish;
- Arcane Rupture = 205 Colorless Magical AoE + hostile Field removal + Minor Magic Down;
- Elemental Convergence = 230 Magical chosen standard element / 25% Spirit penetration + matching self Elemental Guard;
- Crest Dominion = 330 Colorless Magical AoE / 35% base Spirit penetration + hostile Field removal/suppression + 3-round Dominion Crest Field; selected Trait II raises effective penetration to 50%, Trait III extends the Field to 4 rounds.

Detailed authority: `docs/CYANIS_VAELIRA_SUBCLASS_WORKING_SPEC.md`.

### Vaelira ← Cyanis — APPROVED Axiomblade

**Pairing:** **Vaelira — Green Arcanist / Axiomblade**.

Approved selected stat package:
- HP +6%
- Attack +6%
- Magic +6%
- Defense +8%
- Speed -6%

Approved naming / progression:
- Trait **Formal Equivalence**;
- CL1 **First Principle**;
- CL4 **Proven Advance**;
- CL7 **Counterproof**;
- CL9 **Axiom Rend**;
- CL11 **Equivalent Form**;
- CL13 **Final Axiom**.

Approved Mastery:
- CL3 **Foundational Proof**;
- CL5 **Proven Position**;
- CL7 **Exact Rebuttal**;
- CL10 **Equipment Mastery** → Crest Knight donor Relic.

Key approved architecture:
- Sword expressions are Physical/Defense-facing; Staff expressions are Magical/Spirit-facing;
- Formal Equivalence stores the latest standard-element expression through the following round and the next damaging Axiomblade ability consumes it; compatible Prism Cycle takes precedence;
- Proven Advance is an attack and grants Minor Defense Up + Minor Spirit Up, with the old Elemental Guard rider removed;
- Counterproof is the one Prepared self-counter;
- Axiom Rend uses 30% relevant-defense penetration and rewards a matching existing Imprint;
- Equivalent Form supports Sword, Sword + Shield, dual Swords, Staff, Staff + Focus, and Staff + Shield;
- Final Axiom is 320 AoE with player-chosen standard element, 25% relevant-defense penetration, and matching party Elemental Guard for 2 rounds.

Detailed authority: `docs/VAELIRA_CYANIS_SUBCLASS_WORKING_SPEC.md`.

### Ilyra ← Seyrik — APPROVED Vowblade

**Pairing:** **Ilyra — Blue Warden / Vowblade**.

Approved selected stat package:
- HP +8%
- Attack +10%
- Spirit +8%
- Defense -6%

Approved naming / progression:
- Trait **Mercy in Steel**;
- CL1 **Vital Edge**;
- CL4 **Mercy Returned**;
- CL7 **Living Covenant**;
- CL9 **Vowkeeper's Reprisal**;
- CL11 **Vow of Severance**;
- CL13 **Mercy's Final Edge**.

Approved Mastery:
- CL3 **Steeled Mercy**;
- CL5 **Mercy Carried**;
- CL7 **Unbroken Covenant**;
- CL10 **Equipment Mastery** → Ruin Vanguard donor Relic.

Key approved architecture:
- damaging Vowblade abilities use authored **50% Attack / 50% Spirit Hybrid** scaling;
- Vowblade abilities work with either Wardrods or learned Two-Handed Swords; donor weapon use is not mandatory and gives no hidden ability-Power bonus;
- Vowblade does not create a seventh/Ruin damage element;
- Mercy in Steel provides controlled damage-derived sustain and a below-50%-HP damage bonus, with only its own Rank-I overflow eligible for Rank-III transfer;
- Vital Edge = 185 Hybrid / 8 MP + 15% authored damage-based self-heal;
- Mercy Returned = 215 Hybrid / 10 MP + lowest-HP ally healing;
- Living Covenant = 3-round stance +10% additional damage-derived healing and Major interruption resistance;
- Vowkeeper's Reprisal = 235 Hybrid / 12 MP with +20% final damage if the target hurt another ally last round plus ally recovery;
- Vow of Severance = 250 Hybrid / 15 MP / 30% penetration + Minor Defense Down and Minor Spirit Down for 2 rounds;
- Mercy's Final Edge = 520 Hybrid / 40% penetration + authored self-heal, party heal, and 15% party direct-damage reduction through the following round.

Approved presentation direction uses reusable Driving Strike / Committed Strike / Invocation families plus one premium Ultimate sequence. Grace remains blue-white; Seyrik's influence appears as restrained violet Ruin fractures without Black Host corruption language.

Detailed authority: `docs/ILYRA_SEYRIK_SUBCLASS_WORKING_SPEC.md`.

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
CL1 Core Element Array / Shaping Element Array / Prism Cycle; CL3 Composite Surge; CL5 Focus candidate; CL6 Elemental Field; CL9 Sixfold Ray; CL13 Arcanum Ascendant.

### Seyrik — Ruin Vanguard
CL1 Ruin Cleave / Rift Lance / Ember Brand; CL3 Fracturing Brand; CL5 unresolved honest native reward; CL6 Unmaking Blow; CL9 Call Shardfang; CL13 Controlled Apocalypse.

---

## 9. Current approved / strong working class pair names

- **Cyanis — Crest Knight / Crest Arcanist** — **APPROVED**
- **Ilyra — Blue Warden / Vowblade** — **APPROVED**
- **Torren — War Archer / Routeweaver** — preserve-first working identity
- **Nimera — Cardweaver / Truthshot** — leading working name, not yet final lock
- **Vaelira — Green Arcanist / Axiomblade** — **APPROVED**
- **Seyrik — Ruin Vanguard / Ruin Reclaimer** — preserve-first working identity

---

## 10. Immediate open work

- Move next to **Seyrik ← Ilyra / Ruin Reclaimer**: recover exact preserve-first mechanics, add Ability 5, rebase Trait/Ultimate to CL13, then naming/stat/mastery/presentation audit.
- Continue **Torren ← Nimera / Routeweaver** after Ruin Reclaimer.
- Finalize Truthshot name/stat package only when explicitly approved; its current working mechanics remain non-final.
- Reconcile Core/Subclass Mastery effect text after all six kits stabilize.
- Finalize Synthesis / Legacy character-resolution requirements.
- Synchronize remaining stale `Sixfold Accord` wording to **Sixfold Volition** in the deliberate global terminology sweep.
- Promote the complete class-rework package into a new master-canon audit only after all six reciprocal subclasses are stable.
