# Diyse — Torren ⇄ Nimera Synthesis Working Spec

**Status:** APPROVED PAIR-SPECIFIC SYNTHESIS DESIGN — NOT YET MASTER-CANON PROMOTED  
**Parent authority:** v1.84 / Audit99 plus newer approved class-rework decisions.  
**Related files:** `docs/CLASS_SYNTHESIS_WORKING_MODEL.md`, `docs/TORREN_NIMERA_SUBCLASS_WORKING_SPEC.md`, `docs/NIMERA_TORREN_SUBCLASS_WORKING_SPEC.md`

The user's standing class-rework approval rule applies: material advanced under the current “Let's continue” sequence is approved, with later explicit refinements superseding earlier conflicting drafts.

## 1. Pair thesis

Torren and Nimera complete the reciprocal pair through two different forms of certainty.

- **Torren:** War Archer judgment identifies the target; Routeweaver fieldcraft creates the path to exploit that judgment.
- **Nimera:** Cardweaver Appraisal establishes what is known; Truthshot turns that information and Hunter's Measure into demonstrable proof, then feeds that proof back into her Card use.

Neither Synthesis creates a new mark, gauge, extra action, extra Card slot, second Trait, or weapon requirement.

---

## 2. Torren Synthesis — Measured Passage

**Measured Passage** is Torren's permanent Synthesis passive after the universal Synthesis gate is met and the node is purchased.

### A. War Archer → Routeweaver bridge

**Once per round**, when a **damaging non-Ultimate War Archer Ability** resolves against an enemy with **Hunter's Measure**, Torren's next **non-Ultimate Routeweaver Ability** before the end of the following round costs **2 less MP**, minimum 1 MP.

Boundaries:
- one qualifying War Archer resolution arms one discount;
- the discount does not stack with itself;
- Hunter's Measure may have been applied by Torren or Nimera;
- a Prepared War Archer response may qualify when its damaging response actually resolves; merely arming the Prepared effect does not qualify;
- the discount does not alter Power, healing/cleansing, Field duration, targeting, hit count, penetration, status application, or weapon legality.

### B. Routeweaver → War Archer bridge

**Once per round**, when a **Routeweaver Ability or Ultimate** establishes or legally extends one of Torren's **Route Fields**, his next **damaging non-Ultimate War Archer Ability** against an enemy with Hunter's Measure before the end of the following round gains **+10% Power**.

Qualifying Routeweaver actions include:
- **Crossroads** when it establishes Forward Route or Covered Route;
- **Covered Crossing** when it successfully extends an active Torren Route Field;
- **Open the Way** when it establishes its Route Field.

Boundaries:
- one qualifying Field establishment/extension arms one one-use Power bonus;
- the bonus does not stack with itself;
- if Covered Crossing is used with no active Route Field and therefore extends nothing, it does not arm this clause;
- the bonus does not change Hunter's Measure duration, damage type, hit pattern, MP cost, target rules, Prepared legality, or weapon legality.

### C. Intent

Torren's endgame cadence becomes:

**measure the target → make the route cheaper to establish/exploit → use the established route to sharpen the next War Archer strike.**

This integrates his veteran quarry judgment with Nimera-derived fieldcraft without turning Routeweaver into a second War Archer or adding passive party-wide damage.

---

## 3. Nimera Synthesis — Living Proof

**Living Proof** is Nimera's permanent Synthesis passive after the universal Synthesis gate is met and the node is purchased.

### A. Cardweaver knowledge → Truthshot bridge

An enemy satisfies Living Proof's **known-target condition** when both are true:
1. Nimera has already revealed that enemy's permitted combat data through **Diysean Appraisal**; and
2. that enemy currently has **Hunter's Measure**.

This is a condition check only. It does **not** create an `Appraised`, `Verified`, `Proven`, or other new status.

**Once per round**, Nimera's first **damaging non-Ultimate Truthshot Ability** against a target satisfying that condition gains **+10% Power**.

Boundaries:
- the target must satisfy both conditions when the Ability resolves;
- Hunter's Measure may have been applied by Nimera or Torren;
- Diysean Appraisal remains information reveal only and is not converted into a combat status;
- the bonus does not alter hit count, Defense penetration, Critical Chance, status chance, MP cost, targeting, or weapon legality;
- Final Annotation does not receive this +10% Power clause.

### B. Truthshot → Cardweaver bridge

**Once per round**, when a **Truthshot Ability or Final Annotation** damages an enemy that satisfies Living Proof's known-target condition, Nimera's next **hostile Standard Card targeting that same enemy** before the end of the following round gains **+10 Base Hit / application reliability** where relevant.

Boundaries:
- one qualifying Truthshot action arms one one-use Card bonus;
- the bonus does not stack with itself;
- it applies only to the same enemy that satisfied the known-target condition;
- it does not create extra Card slots, extra Card actions, Card charges, or a draw/discard system;
- it does not create or substitute for **Indexed** and does not copy Sovereign Index;
- if the selected Standard Card has no Hit/application roll, the bonus has no additional effect rather than being converted into another benefit.

### C. Intent

Nimera's endgame cadence becomes:

**Appraise what is true → Measure the target → prove it with Truthshot → use that proof to make the next Card application more reliable.**

Living Proof therefore joins her information-driven Cardweaver identity to Torren's evidence-through-precision discipline without inventing a new analyzed-target status or turning Truthshot into a Card subsystem.

---

## 4. Pair balance boundaries

- Neither Synthesis grants flat permanent stats.
- Neither creates or duplicates Hunter's Measure; the existing shared state remains the only quarry state.
- Neither creates an `Appraised` status; Diysean Appraisal remains information reveal only.
- Neither creates extra ordinary actions, extra Card actions, extra Card slots, extra equipment slots, or a second Trait.
- Torren's MP discount is **2 MP**, one-use, non-stacking, and limited to a non-Ultimate Routeweaver Ability.
- Torren's +10% Power bonus is one-use, non-stacking, and limited to a damaging non-Ultimate War Archer Ability against Hunter's Measure.
- Nimera's +10% Truthshot Power applies only once per round, only to a non-Ultimate damaging Truthshot Ability, and only when both Appraisal knowledge and Hunter's Measure are present.
- Nimera's Standard Card reliability bonus is one-use, same-target, and does not become a generic Card-damage bonus.
- No Ability or Ultimate gains a weapon requirement.
- No additional pair bonus is granted merely for fielding Torren and Nimera together; their existing shared Hunter's Measure already provides normal pair synergy.

---

## 5. Remaining pair work

- Author the shared Torren/Nimera **resolution / integration story beat** that satisfies their individual Synthesis narrative prerequisite.
- Finalize the pair-specific **Legacy mapping, names, and acquisition presentation**.
- Run the final six-Synthesis balance pass now that all three reciprocal Synthesis pairs are mechanically complete.
