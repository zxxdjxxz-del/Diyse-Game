# Diyse — Six-Synthesis Cross-Balance / Consistency Audit — 2026-08-21

**Status:** APPROVED SYNTHESIS CROSS-BALANCE PASS — NOT YET MASTER-CANON PROMOTED  
**Parent authority:** v1.84 / Audit99 plus newer approved class-rework decisions.  
**Purpose:** verify that all six character-specific Synthesis effects are balanced, reciprocal without becoming mirrors, compatible with persistent unlocked abilities, and safe to carry into pair-resolution / Legacy design without reopening the completed class packages.

Reviewed Synthesis sources:
- `docs/CYANIS_VAELIRA_SYNTHESIS_WORKING_SPEC.md`
- `docs/ILYRA_SEYRIK_SYNTHESIS_WORKING_SPEC.md`
- `docs/TORREN_NIMERA_SYNTHESIS_WORKING_SPEC.md`
- `docs/CLASS_SYNTHESIS_WORKING_MODEL.md`

The standing class-rework approval rule applies: material advanced under the current “Let's continue” sequence is approved, with later explicit refinements superseding earlier conflicting drafts.

---

## 1. Audit result

**PASS. No raw-number rebalance is required.**

The six Synthesis effects occupy distinct endgame integration spaces:

| Character | Synthesis | Primary payoff |
|---|---|---|
| Cyanis | **Unified Crest** | Base Crest actions prime Crest Attunement; consumed Attunement feeds one stronger Base strike |
| Vaelira | **Unified Spectrum** | Imprints become selectable Axiomblade elements and can be maintained by matching attacks |
| Ilyra | **Mercy Unbroken** | preservation and offensive mercy alternate between Power and MP efficiency |
| Seyrik | **Tempered Ruin** | Ruin offense and preservation alternate between MP efficiency and Power |
| Torren | **Measured Passage** | Hunter's Measure and Route Fields create a quarry/route cadence |
| Nimera | **Living Proof** | Appraisal knowledge + Measure strengthens Truthshot and feeds Card reliability |

None creates a third class, second active Trait, new gauge, extra action, extra equipment/Card slot, duplicate quarry state, or weapon requirement.

---

## 2. Relative-power audit

### Cyanis — Unified Crest

**PASS.** The **+15% Power** payoff is the largest direct Synthesis Power bonus, but it is gated behind the longest authored sequence:
1. select/resolve a Crest Knight Ability to establish Crest Attunement when absent;
2. later consume Attunement with a Crest Field/Seal;
3. spend the armed bonus on the next qualifying damaging Crest Knight Ability.

The bonus is one-use and does not stack. Its larger value is justified by the multi-action setup and Attunement consumption.

### Vaelira — Unified Spectrum

**PASS.** Unified Spectrum grants no flat Power or MP reduction. Its value is flexibility and state maintenance:
- an existing Imprint may supply the Axiomblade element;
- one matching Imprint may be extended once per round.

This can improve existing Axiomblade/Imprint interactions, but it does not create Imprints, consume-free Composite Reactions, extra attacks, or unconditional penetration. No numerical reduction is required.

### Ilyra — Mercy Unbroken

**PASS.** The **+10% Power** and **-3 MP** effects are strong but mutually cadence-oriented rather than simultaneous passive buffs. The Power clause requires a qualifying Blue Warden action on another ally; the MP clause requires Vowblade to restore another ally. Self-healing alone cannot drive the loop.

The discount remains minimum 1 MP and applies to one non-Ultimate Blue Warden Ability only. No healing amount or revival value increases.

### Seyrik — Tempered Ruin

**PASS.** The **-3 MP** Ruin Warden discount is easier to establish than Ilyra's equivalent in some rotations, but the reverse **+10% Power** payoff requires Ruin Warden to restore another ally rather than merely self-Drain. This keeps the full loop tied to actual preservation behavior.

No extra Drain, healing percentage, revival strength, or Ruin Vanguard self-drawback removal is added.

### Torren — Measured Passage

**PASS.** The **-2 MP** discount is intentionally smaller than the Ilyra/Seyrik -3 MP discounts because Torren's Synthesis also benefits from two already-established high-value shared systems: **Hunter's Measure** and multi-round **Route Fields**. The War Archer → Routeweaver direction requires a measured target, while the reverse direction requires actual Field establishment/extension.

The +10% War Archer Power bonus remains measured-target-only, one-use, and non-Ultimate.

### Nimera — Living Proof

**PASS.** Living Proof has the greatest setup specificity: the enemy must both have been revealed through **Diysean Appraisal** and currently carry **Hunter's Measure**. In return it grants:
- +10% Power to the first qualifying non-Ultimate Truthshot Ability each round;
- a same-target +10 Base Hit/application-reliability bonus to the next hostile Standard Card after a qualifying Truthshot hit.

The Appraisal side remains battle knowledge, not a new combat status. The Card bonus creates no substitute benefit when a Card has no Hit/application roll.

---

## 3. Universal trigger normalization

The following consistency rules are approved for all six Synthesis effects.

### Ability identity follows origin

A learned Ability retains its **source-class identity** for Synthesis triggers regardless of which class is currently selected.

Examples:
- Crest Strike remains a Crest Knight Ability while Crest Arcanist is selected;
- Vital Edge remains a Vowblade Ability while Blue Warden is selected;
- Throughline remains a Routeweaver Ability while War Archer is selected.

This is necessary because unlocked Abilities persist across class selection while the selected class still controls only its stat package and Trait.

### One action, one trigger

A single Ability action can satisfy a Synthesis clause at most **once**, even if it:
- hits multiple times;
- hits multiple enemies;
- heals multiple allies;
- removes multiple harmful statuses;
- applies multiple qualifying effects.

No multihit/AoE action generates multiple stored Synthesis bonuses from one resolution.

### Armed-copy rule

Each directional Synthesis clause may hold at most **one armed copy** of its own future bonus/discount.

- Re-triggering the same clause while its copy is already armed does not stack another copy.
- The opposite directional clause is a different effect and may be armed independently if legal.
- All existing authored expiration windows remain **through the end of the following round** unless the character-specific spec says otherwise.

### Ultimate normalization

Current Synthesis Power bonuses and MP discounts **do not apply to Ultimates**.

An Ultimate may **arm a later Synthesis effect only where the character-specific spec explicitly says it can**. Current approved examples include:
- Vowblade Ultimate may arm Ilyra's next Blue Warden MP discount if it actually restores another ally;
- Ruin Warden Ultimate may arm Seyrik's next Ruin Vanguard Power bonus if it restores another ally;
- Open the Way may arm Torren's next measured War Archer Power bonus by establishing a Route Field;
- Final Annotation may arm Nimera's next same-target hostile Standard Card reliability bonus.

This avoids multiplicative Ultimate escalation while still allowing an Ultimate to conclude one side of a character's integration loop.

### Prepared/reaction normalization

Merely arming a Prepared effect never counts as a damaging Synthesis trigger. A Prepared response can qualify only when the response actually resolves and the character-specific Synthesis wording allows it.

Cyanis's Unified Crest explicitly excludes a previously armed counter reaction from masquerading as another deliberately selected Crest Knight Ability. Torren's Measured Passage explicitly allows a damaging War Archer Prepared response to qualify when it resolves against Hunter's Measure.

---

## 4. Weapon-independence audit

**PASS.**

No Synthesis effect conditions Ability legality on Sword, Staff, Wardrod, Two-Handed Sword, Great Bow, Conduit, Shield, Focus, or any other equipment family.

Equipment continues to affect ordinary Attack, stats, slot geometry, Relic/Legacy legality, and presentation. If a technique visually implies a weapon not currently equipped, the approved manifested/projected-weapon presentation rule applies.

---

## 5. State / resource audit

**PASS.**

The Synthesis layer reuses established information and combat states only:
- **Crest Attunement**;
- elemental **Imprints**;
- HP recovery / harmful-status removal events;
- **Hunter's Measure**;
- Torren-authored **Route Fields**;
- Diysean Appraisal's existing revealed-information state;
- ordinary Standard Card targeting/application rules.

It creates no `Appraised`, `Verified`, `Proven`, second Measure, second Imprint system, new route meter, mercy meter, synthesis gauge, or other player resource.

---

## 6. Action-economy audit

**PASS.**

All six Synthesis effects modify only the value or efficiency of actions the character was already legally able to take.

They grant no:
- extra ordinary action;
- follow-up action;
- free Card action;
- duplicate Prepared response;
- automatic second Ability;
- free Ultimate;
- Prime refresh.

This is especially important because persistent unlocked Abilities already allow Base/Subclass mixing without Synthesis needing to add a new command layer.

---

## 7. Pair-by-pair identity audit

### Cyanis ⇄ Vaelira

The pair passes because both use shared Crest/elemental structures differently:
- Cyanis turns deliberate Crest sequencing into Attunement/Field/Seal cadence;
- Vaelira turns Imprints into elemental translation and persistence.

They do not become mirror elemental casters.

### Ilyra ⇄ Seyrik

The pair passes because both move between offense and preservation in opposite directions:
- Ilyra begins from preservation and earns permission to press offense;
- Seyrik begins from Ruin offense and learns to route that momentum through preservation.

Neither becomes a second Blue Warden or second Ruin Vanguard.

### Torren ⇄ Nimera

The pair passes because both use **Hunter's Measure** while owning different second systems:
- Torren couples Measure to Route Fields;
- Nimera couples Measure to Appraisal knowledge and Card reliability.

The shared quarry state is sufficient pair language; no additional always-on party bonus is needed.

---

## 8. Final approved conclusion

All six character-specific Synthesis mechanics are **balanced and internally consistent enough to close mechanical Synthesis design**.

No raw-number changes are made by this audit.

The next gates are no longer Synthesis-mechanics design. They are:
1. author the three reciprocal-pair **resolution / integration story beats** that satisfy the Synthesis narrative gate;
2. finalize pair-specific **Legacy mapping, naming, and acquisition presentation**;
3. reconcile **Core Mastery** effect text;
4. normalize the global direct-damage-reduction stacking rule and universal Ultimate-cost convention;
5. perform the stale `Sixfold Accord` → **Sixfold Volition** terminology sweep;
6. run final implementation/data regression review;
7. promote the completed class-rework package into a new master-canon audit when story/Legacy/final normalization are stable.
