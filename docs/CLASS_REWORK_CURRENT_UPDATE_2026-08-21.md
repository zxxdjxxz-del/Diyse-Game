# Diyse — Class Rework Current Update — 2026-08-21

**Status:** APPROVED POST-AUDIT103 CLASS-REWORK PACKAGE — PENDING VALID MASTER-CANON PROMOTION  
**Parent whole-project authority:** **v1.88 / Audit103 — Quest Architecture, Character Quest and Ordinary Side-Quest Closure**  
**Next valid promotion slot:** **v1.89 / Audit104**  
**Purpose:** implementation/handoff ledger for the CL13 class rework, reciprocal Subclasses, Mastery/Synthesis, equipment inheritance, pair-resolution beats, Legacy mapping, and remaining reconciliation/normalization work.

## Numbering correction

The class-rework package must **not** be labeled v1.85 / Audit100.

Correct inherited sequence:
- v1.84 / Audit99 — Random-Encounter Runtime Implementation and Production-Readiness Closure.
- v1.85 / Audit100 — Enemy Asset Reuse and Palette-Swap Production Efficiency Lock.
- v1.86 / Audit101 — Major Hunt Architecture and Unlock Closure.
- v1.87 / Audit102 — Major Hunt Difficulty and Progression Balance Closure.
- v1.88 / Audit103 — Quest Architecture, Character Quest and Ordinary Side-Quest Closure.

Therefore the class-rework canon promotion, once reconciliation is complete, belongs at **v1.89 / Audit104**.

The erroneous repository Audit100 class-promotion file has been removed.

## Approval rule

The user explicitly clarified that class-rework material advanced under repeated **“Let's continue”** responses in this sequence is approved. When a later pass refines or replaces an earlier version, the **latest refinement controls**.

## Detailed current files

Subclass specs:
- `docs/CYANIS_VAELIRA_SUBCLASS_WORKING_SPEC.md`
- `docs/VAELIRA_CYANIS_SUBCLASS_WORKING_SPEC.md`
- `docs/ILYRA_SEYRIK_SUBCLASS_WORKING_SPEC.md`
- `docs/SEYRIK_ILYRA_SUBCLASS_WORKING_SPEC.md`
- `docs/TORREN_NIMERA_SUBCLASS_WORKING_SPEC.md`
- `docs/NIMERA_TORREN_SUBCLASS_WORKING_SPEC.md`

Cross-class / Synthesis:
- `docs/CLASS_REWORK_CROSS_BALANCE_AUDIT_2026-08-21.md`
- `docs/CLASS_SYNTHESIS_WORKING_MODEL.md`
- `docs/CYANIS_VAELIRA_SYNTHESIS_WORKING_SPEC.md`
- `docs/ILYRA_SEYRIK_SYNTHESIS_WORKING_SPEC.md`
- `docs/TORREN_NIMERA_SYNTHESIS_WORKING_SPEC.md`
- `docs/CLASS_SYNTHESIS_CROSS_BALANCE_AUDIT_2026-08-21.md`

Legacy:
- `docs/CYANIS_VAELIRA_LEGACY_WORKING_SPEC.md`
- `docs/ILYRA_SEYRIK_LEGACY_WORKING_SPEC.md`
- `docs/TORREN_NIMERA_LEGACY_WORKING_SPEC.md`

---

## 1. Current class architecture — approved

- Base Class cap: **CL13**.
- Subclass cap: **CL13**.
- Base and Subclass CEXP are separate.
- CEXP goes only to the currently selected class.
- All recruited permanent characters receive full CEXP to their selected class whether active or reserve.
- No Subclass exists before the **Sixfold Volition**.
- At the Sixfold Volition all six Subclasses unlock and reciprocal cross-training begins.
- Reciprocal pairs: **Cyanis ⇄ Vaelira**, **Ilyra ⇄ Seyrik**, **Torren ⇄ Nimera**.
- Equipment and unlocked Abilities remain persistently usable; selected class controls its stat package and Trait.
- Equipment slots remain **Weapon / Secondary / Armor**.

### Global Ability weapon rule — approved

**No Ability or Ultimate requires a particular equipped weapon.** Once learned, every Ability remains usable with any otherwise-legal equipment loadout.

Equipment still matters for ordinary Attack, stats/defenses, Weapon/Secondary slot geometry, Relic/Legacy legality, and presentation. If an Ability visually implies a weapon not carried, presentation adapts through manifested/projected weapon expression rather than disabling the command.

### Whole-project level-cap correction

The current whole-project player level cap inherited from v1.88 / Audit103 is **70**. Earlier class-rework notes that called 60 the hard player-level cap are stale and must not be promoted.

The CL13 class system and its 6,000-CEXP thresholds are separate from the player-level cap. Exact final player EXP / late-game progression rebalance under Level 70 remains outside this class-rework ledger.

---

## 2. CEXP / CL13 progression — approved

Class thresholds:
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

The retired **4,800-CEXP CL12** table must not return.

Fresh Subclass begins at **CL1 with 0 CEXP toward CL2**.

Universal Subclass schedule:
- CL1 donor basic Primary + Trait I + Ability1
- CL3 donor Armor
- CL4 Ability2
- CL5 honest donor advanced equipment/Secondary where real
- CL6 TraitII
- CL7 Ability3
- CL9 Ability4
- CL10 Equipment Mastery eligibility
- CL11 Ability5
- CL12 TraitIII
- CL13 Ultimate

Current recruitment/Base-CL notes that remain working rather than final whole-project promotion:
- Cyanis Ch0 CL1
- Ilyra Ch0 CL1
- Torren Ch1 CL4 *(working)*
- Nimera Ch3 CL4 *(working)*
- Vaelira Ch4 S022 CL7 *(working)*
- Seyrik Ch6 CL8 *(approved earlier)*

---

## 3. Equipment inheritance / Mastery — approved where settled

Donor ordinary equipment progression:
- Vaelira ← Cyanis: Swords → Crest armor → Shield + second-Sword permission
- Cyanis ← Vaelira: Arcane Staffs → Green Arcanist armor → Focus
- Seyrik ← Ilyra: Wardrods → Warding armor → Shield + Focus where legal
- Ilyra ← Seyrik: Two-Handed Swords → Ruin armor; no fake CL5 reward
- Torren ← Nimera: one-slot Conduits → Cardweaver armor → two-handed Conduits + Focus where legal
- Nimera ← Torren: Great Bows → War Archer armor; no fabricated CL5 Secondary

Nine-point Mastery architecture remains **4 Core + 4 Subclass + 1 Synthesis**, each costing 1 MP. Banking is legal.

**Equipment Mastery = Subclass Node 4 at CL10** and grants donor Relic access. Ordinary donor equipment arrives earlier through CL1–5. Legacy is downstream of Synthesis.

Still open:
- final Core Mastery effect text;
- final Core gate schedule;
- any still-unresolved early Subclass Mastery-node effect/gate text other than Equipment Mastery at CL10.

---

## 4. Approved reciprocal Subclasses

- **Cyanis — Crest Knight / Crest Arcanist** — Trait **Crest Resonance**; Arcane Lance / Warding Crest / Nullifying Seal / Arcane Rupture / Elemental Convergence / Crest Dominion.
- **Vaelira — Green Arcanist / Axiomblade** — Trait **Formal Equivalence**; First Principle / Proven Advance / Counterproof / Axiom Rend / Equivalent Form / Final Axiom.
- **Ilyra — Blue Warden / Vowblade** — Trait **Mercy in Steel**; Vital Edge / Mercy Returned / Living Covenant / Vowkeeper's Reprisal / Vow of Severance / Mercy's Final Edge.
- **Seyrik — Ruin Vanguard / Ruin Warden** — Trait **Ruin's Mercy**; Siphon Rune / Stolen Grace / Restoring Ward / Withering Mercy / Reclaimed Breath / Mercy Through Ruin. **Ruin Warden supersedes Ruin Reclaimer and Ruin Healer.**
- **Torren — War Archer / Routeweaver** — Trait **Field Weaving**; Throughline / Clear Route / Crossroads / Covered Crossing / Forced Passage / Open the Way.
- **Nimera — Cardweaver / Truthshot** — Trait **Applied Evidence**; Measured Shot / Held Argument / Pin the Variable / Structural Failure / Corroboration / Final Annotation.

Key formula/state locks:
- Vowblade damaging Abilities = **50% Attack / 50% Spirit Hybrid**.
- Ruin Warden Siphon Rune = one-hit **60% Attack / 40% Magic Hybrid**.
- Routeweaver damaging Abilities = **50% Attack / 50% Magic Hybrid**.
- Hunter's Measure is shared between Torren and Nimera.
- Diysean Appraisal is information reveal only; no `Appraised` status.
- Indexed remains separate.
- All six Subclasses are weapon-independent at the Ability/Ultimate legality layer.

The six-Subclass cross-balance audit is **PASS** with no broad raw-number rebalance.

---

## 5. Approved universal Synthesis architecture

Synthesis is the ninth and final Mastery node.

Eligibility requires:
**Base CL13 + Subclass CL13 + all four Core Masteries + all four Subclass Masteries + authored character resolution/integration condition + 1 available MP**.

Each Synthesis grants:
1. one permanent character-specific Base/Subclass integration passive;
2. paired Legacy eligibility under the final reciprocal mapping.

Synthesis does not create a third class, merge stat packages, activate both Traits, add actions/slots/Card slots, add a gauge, copy a partner's whole kit, or create a weapon requirement.

A learned Ability retains its **source-class identity** for Synthesis triggers regardless of current class selection.

---

## 6. Approved six Synthesis effects

### Cyanis — Unified Crest
A selected/resolved Crest Knight Ability can establish Crest Attunement when absent. Consuming Attunement with a Crest Field/Seal arms **+15% Power** for the next damaging Crest Knight Ability before the end of the following round.

### Vaelira — Unified Spectrum
A damaging Axiomblade Ability may use an existing target Imprint's element without consuming it. Once per round, a matching hit extends that Imprint **+1 round** up to authored maximum. Prism Cycle retains precedence; no automatic Composite Reaction.

### Ilyra — Mercy Unbroken
A qualifying Blue Warden heal/cleanse on another ally arms **+10% Power** for the next damaging non-Ultimate Vowblade Ability. A Vowblade Ability/Ultimate that restores another ally arms **-3 MP** on the next non-Ultimate Blue Warden Ability, minimum 1.

### Seyrik — Tempered Ruin
A damaging non-Ultimate Ruin Vanguard Ability arms **-3 MP** on the next non-Ultimate Ruin Warden Ability, minimum 1. A Ruin Warden Ability/Ultimate that restores another ally arms **+10% Power** for the next damaging non-Ultimate Ruin Vanguard Ability.

### Torren — Measured Passage
A damaging non-Ultimate War Archer Ability resolving against Hunter's Measure arms **-2 MP** on the next non-Ultimate Routeweaver Ability, minimum 1. Establishing/legally extending a Torren Route Field arms **+10% Power** for the next damaging non-Ultimate War Archer Ability against Hunter's Measure.

### Nimera — Living Proof
Known-target condition = Diysean Appraisal already revealed permitted combat data **and** Hunter's Measure currently present. Once per round, first damaging non-Ultimate Truthshot against that target gains **+10% Power**. A qualifying Truthshot/Final Annotation hit arms **+10 Base Hit/application reliability** for the next hostile Standard Card against that same enemy where relevant.

Synthesis cross-balance result: **PASS**. No raw-number rebalance required.

---

## 7. Approved pair-resolution beats

### Cyanis ⇄ Vaelira — What Holds, What Changes
Late Chapter 11 at Cresthaven. Structure without adaptation fails; adaptation without an anchor also fails. They build a solution where only what must hold is fixed and the surrounding expression can change.

### Ilyra ⇄ Seyrik — Keep Them Alive
Late Chapter 11 at the Forward Hub treatment/recovery area. Ilyra defines what must be protected; Seyrik uses controlled Ruin only inside that boundary. Mercy is not forgiveness; restraint is not passivity; violence is not automatically decisiveness.

### Torren ⇄ Nimera — Enough to Move
Late Chapter 11 at the Forward Hub operations/map table. Torren externalizes veteran judgment; Nimera strips analysis to decisive unknowns. They produce a route another competent person can execute without either of them present.

All three beats are mandatory authored continuity, not romance/affection/player-choice scenes. Each shared beat satisfies both characters' narrative Synthesis prerequisite but does not purchase Synthesis.

---

## 8. Approved Legacy identities and reciprocal mappings

### Cyanis ⇄ Vaelira
- Crest Knight Legacy — **Stillpoint Aegis** — Shield — reciprocal wearer Vaelira after Synthesis.
- Green Arcanist Legacy — **Living Prism** — Focus — reciprocal wearer Cyanis after Synthesis.

### Ilyra ⇄ Seyrik
- Blue Warden Legacy — **Mercy's Boundary** — Shield — reciprocal wearer Seyrik after Synthesis.
- Ruin Vanguard Legacy — **Purposebound** — Two-Handed Sword — reciprocal wearer Ilyra after Synthesis.

### Torren ⇄ Nimera
- War Archer Legacy — **Known Ground** — Great Bow — reciprocal wearer Nimera after Synthesis.
- Cardweaver Legacy — **Decisive Record** — one-slot Conduit — reciprocal wearer Torren after Synthesis.

Normal slot geometry still applies. None of these items changes Ability or Ultimate legality.

Exact final Legacy numerical stats/passives and item metadata remain deferred to the production item/equipment audit.

---

## 9. Audit103 Legacy-Component reconciliation — REQUIRED BEFORE AUDIT104

Audit103 already locks the following:
- exactly six Character Quests;
- each Character Quest grants that character's **Legacy Component** as its principal mechanical reward.

The newer class-rework sequence approved a shared **Cresthaven Chapter-12 physical Legacy release** presentation for the six named Legacy items.

These two approved layers have not yet been explicitly connected. Before v1.89 / Audit104 canon promotion, we must define the relationship so the Audit103 Legacy Components are not orphaned or silently superseded.

Until that reconciliation is approved:
- the six Legacy names, equipment families, reciprocal Synthesis eligibility mappings, and slot geometries remain approved;
- the exact final acquisition chain connecting Character Quest Legacy Components to the Cresthaven physical release remains pending integration.

---

## 10. Immediate open work

1. **Reconcile Audit103 Character-Quest Legacy Components with the six named Legacy items / Cresthaven release.**
2. Promote the settled compatible package in the next valid slot: **v1.89 / Audit104**.
3. Reconcile Core Mastery effect text and final Core gates.
4. Reconcile any still-open early Subclass Mastery-node text.
5. Finalize global percentage direct-damage-reduction stacking.
6. Finalize the universal Ultimate MP-cost convention.
7. Perform the repository-wide `Sixfold Accord` → **Sixfold Volition** terminology sweep.
8. Integrate the three resolution beats into final Chapter 11 scene numbering/dialogue.
9. Run implementation/data regression across class, equipment, Mastery, Synthesis, and Legacy data.

Do not reuse v1.85 / Audit100 for this package; that number is already occupied by earlier canon.