# Diyse — Torren ⇄ Nimera Synthesis Working Spec

**Status:** APPROVED PAIR-SPECIFIC SYNTHESIS DESIGN + RESOLUTION BEAT — NOT YET MASTER-CANON PROMOTED  
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

## 5. Approved resolution / integration story beat — Enough to Move

### Placement

- **Late Chapter 11** at the **Forward Hub**, during the same mandatory preparation/operations window used for the other endgame integration beats and before Chapter 12's point of no return.
- Use the existing operations / map-table staging. No bespoke location is required.
- Exact final scene number remains for later script integration.
- The scene is **mandatory authored continuity**, not a missable camp event, optional mentorship scene, or dialogue-choice reward.
- Completing it satisfies the **character-resolution / integration prerequisite for both Torren and Nimera**. It does not automatically purchase Synthesis; each still needs the full mechanical gate and 1 MP.

### Setup

A routine **resupply / courier movement** for the Forward Hub has to be routed through recently contested ground before the next operational push. The movement itself is background logistics, not a new quest or branching mission.

The available information is useful but incomplete:
- an older route map is reliable about terrain but not recent damage;
- a fresh scout report confirms part of the corridor but not the entire path;
- Black Host movement indicates one approach may be watched;
- one alternate route is physically possible but slower and harder to extract from if conditions change.

Torren looks over the map and quickly marks the route he would take.

Nimera does not tell him he is wrong. She asks him to show her **why**.

Torren initially gives the veteran answer: because the signs line up. Nimera's problem is not that she distrusts him; it is that a route only one person can justify is not yet useful enough to hand to someone else.

### First failed solution — judgment that cannot be transferred

Torren walks Nimera through what he noticed:
- the way Black Host patrol spacing leaves one section suspiciously quiet;
- the terrain feature that makes the obvious approach worse than it looks on a map;
- the scout detail that matters more than three other details because it changes where an ambush can actually be supported.

His conclusion is sound, but most of the reasoning initially exists only in his head.

Nimera points out the practical failure: if Torren is not the one leading the movement, the next person receives a line on a map and an instruction to trust whoever drew it.

Torren does not become defensive about experience. He recognizes that veteran instinct which cannot be explained dies with the veteran—or, more immediately, becomes useless the moment the veteran is somewhere else.

This is not framed as intuition being inferior to analysis. The flaw is **untransmitted judgment**.

### Second failed solution — knowledge that never closes

Nimera then reconstructs the route in her own way.

She annotates every known fact, marks unresolved possibilities, and develops multiple valid branches for what might happen if each uncertain report proves wrong.

The result is accurate, careful, and nearly unusable under time pressure.

Torren asks one practical question: **which remaining unknown would actually change the route?**

Nimera realizes that several uncertainties she has preserved no longer matter to the decision. They are real unknowns, but they are not decisive unknowns.

This is not framed as careful analysis being wasteful. The flaw is treating **complete knowledge** as the prerequisite for responsible action.

### Integrated solution — evidence with a decision point

They rebuild the route briefing together.

Torren externalizes the judgment he would normally carry implicitly:
- what observation matters;
- what conclusion it supports;
- which terrain feature turns that conclusion into a route choice.

Nimera strips away information that is true but non-decisive and keeps only the conditions that would change the plan.

The finished route contains:
- one primary path;
- one clearly defined fallback;
- the specific observable condition that tells the courier team when to switch from one to the other;
- enough reasoning that another competent person can understand the choice without Torren or Nimera standing beside them.

The route is neither Torren's unexplained instinct nor Nimera's complete tree of possibilities. It is **a decision another person can execute because the evidence has been reduced to what matters**.

### Reciprocal reversal

Before they finish, Nimera points to one section and makes the route call first, using Torren's field logic rather than waiting for every source to agree.

Torren asks her why.

She gives him the short version: the one observation, the one implication, and the one action it supports.

Torren accepts it.

Then Torren adds one note to the map explaining a judgment he would previously have left unspoken.

Nimera does not add three more qualifications to it.

That small reversal is the actual integration point.

### Character resolution

**Torren learns:** experience is not diminished by making it explicit. Judgment becomes more valuable when another person can see the route from evidence to decision rather than merely being told to trust the veteran who already sees it.

This completes the emotional logic behind **Routeweaver** and **Measured Passage**: finding the way is not only choosing correctly; it is making the path legible enough for others to follow.

**Nimera learns:** uncertainty does not invalidate a decision. The purpose of knowledge is not to preserve every possible answer forever; it is to identify which facts are decisive enough to act on and which unknowns can remain unknown without changing the choice.

This completes the emotional logic behind **Truthshot** and **Living Proof**: proof is valuable because it resolves action, not because it eliminates the existence of uncertainty.

Neither character becomes the other's stereotype. Torren does not turn into an archivist. Nimera does not abandon rigor for instinct.

### Tone / dialogue boundary

- Keep the scene practical, dry, and rooted in their established map / field-planning language.
- Torren should not lecture Nimera about youth or inexperience.
- Nimera should not treat Torren's experience as superstition that needs to be replaced by formal analysis.
- Their friction comes from two competent people noticing different failure modes in one another's process.
- Allow understated humor around the fact that Torren's first explanation is essentially “because that's the bad road,” followed by Nimera making him unpack what that actually means.
- Exact final dialogue remains deferred to the later dialogue/script pass.

Possible dialogue intent, **not locked final wording**:
- Nimera asks, “What would have to be different for you to choose the other road?”
- Torren later turns the same question back on her when her map accumulates too many branches.
- One of them observes that being uncertain and being undecided are not the same thing.

### Closing image

The finished route sheet is left on the operations table for the actual courier team.

It is visibly simpler than Nimera's first annotated version and more explicit than Torren's first single-line route.

A runner arrives, studies it for a few seconds, points to the fallback marker, and correctly explains when the team should use it.

Torren and Nimera exchange a glance. Neither corrects the runner.

The map works **without them**.

That is the closing proof.

### Production / implementation boundaries

- Reuse the existing Forward Hub operations/map-table environment family.
- Reuse ordinary map, marker, route-line, and briefing animations; no new cinematic system or unique environment asset is required.
- No new named NPC, quest branch, combat encounter, boss, item reward, or lore artifact is introduced.
- The courier/resupply movement is background operational continuity only and must not create a missable outcome or player choice.
- The only system result is marking the **Torren Synthesis story prerequisite complete** and the **Nimera Synthesis story prerequisite complete**.
- If the remaining mechanical gates are incomplete, the Mastery interface may show the narrative prerequisite as completed while the Synthesis node remains unavailable.

---

## 6. Remaining pair work

- Finalize the Torren/Nimera **Legacy mapping, names, and acquisition presentation**.
- Integrate **Enough to Move** into the final Chapter 11 script numbering and dialogue pass without changing its approved story function.
