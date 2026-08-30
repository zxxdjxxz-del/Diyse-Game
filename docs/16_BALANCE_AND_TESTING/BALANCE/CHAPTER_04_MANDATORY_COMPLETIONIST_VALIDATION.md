# Chapter 4 — Mandatory vs Completionist Enemy/Boss Validation

**Version:** v80  
**Status:** **PASS / VALIDATED**  
**Power-audit status:** **CLOSED — no direct-damage Power changed**

## Purpose
Validate Chapter 4 at the party state that actually exists at each encounter point rather than treating the chapter as one flat level.

This pass does **not** reopen enemy Power authoring. Existing Power remains authority unless a specific encounter fails its intended difficulty role.

---

## 1. Chapter-level anchors
Current Chapter-4 player progression:

> **Lv13 chapter start → ~Lv15 middle → Lv17 chapter end**

The active battle party remains capped at four throughout.

### Opening roster
Before S022:
- Cyanis
- Ilyra
- Torren
- Nimera

**Maevra is not part of the Chapter-4 default balance baseline.**

### S022 recruitment transition
After Elder Briarhide:
- Vaelira joins permanently;
- five permanent characters are available;
- only four may be active at once.

Therefore post-S022 completionist testing may optimize party composition, but it does not gain a fifth simultaneous action.

---

## 2. Mandatory vs completionist checkpoints
### Elder Briarhide — S022
Existing encounter-specific progression proof remains valid:
- mandatory: **Lv13**;
- fixed-content completionist: **Lv15**;
- high-side: **~Lv16**.

The encounter is intentionally fixed at **exactly four rounds**, with Last Sentinel resolving the protected Round-4 payoff. Completionists do not shorten the authored duration.

**Verdict: PASS / RETAIN.**

No raw-stat or Power change.

### Reaction Annex opening ordinary encounters
Target party state:
> **~Lv13**, with Vaelira becoming a legal party-selection option after S022.

The recovered opening formations use 4-body compositions. Current enemy strongest ordinary single-target actions remain materially threatening without approaching one-action KO territory against conservative current-equipment characters. Pressure comes from:
- four hostile actions before control/defeat reduces the field;
- elemental affinity reading;
- Bleed / Burn / Freeze / Stun / Staggered coverage;
- Element Mirror reflection punishment;
- Reaction Hound tempo.

**Verdict: PASS.**

### Reaction Annex middle ordinary encounters
Target party state:
> **~Lv15**

The middle set introduces Annex Crucible Guard into mixed formations while keeping most formations at four enemies. Current enemy bodies do not require HP inflation: increased difficulty comes from protector pressure, status coverage, mixed physical/magical axes, and formation synergy.

**Verdict: PASS.**

### Reaction Annex late ordinary encounters
Target party state:
> **~Lv17**

Late formations reach 4–5 enemies, including two-Guard pressure in Guarded Mirror. At the chapter-end party state, individual hit percentages fall relative to opening, but the larger hostile action economy and multi-role compositions correctly replace raw one-hit lethality as the main threat.

**Verdict: PASS.**

No ordinary-enemy raw-stat or Power change.

---

## 3. Protected / authored encounters
### Elemental Researcher / Annex Battle Mage / Crucible Attendant
Their kits are Power-complete, but current Chapter-4 story authority does not place them as separate random or mandatory combatants.

Boundary remains:
> **do not random-spawn them and do not invent a mandatory fight solely to exercise the kit.**

**Verdict: OPEN — DATA/PLACEMENT DEPENDENCY.**

This is a placement dependency, not a balance or Power gap.

### Reaction Conduit
Existing encounter-specific baseline:
- mandatory: **Lv13**;
- completionist: **Lv15**;
- high-side: **~Lv16**.

Current 2,400 HP protected stabilization body projects roughly:
- mandatory: ~8–9 rounds normal / ~7–8 aggressive;
- completionist: ~6–7;
- high-side: ~5–6.

The completionist advantage is useful without deleting the stabilization mechanic.

**Verdict: PASS / RETAIN.**

No raw-stat or Power change.

---

## 4. Optional Elite — Annex Duelist
Current body:
- **Lv18**
- **1,700 HP**
- one bar;
- Fire → Ice → Lightning → Earth at 75% / 50% / 25%;
- intended duration: roughly **2–4 serious party rounds**.

At the plausible Lv15–17 Annex access band, a representative aggressive four-character party can remove roughly one quarter to one third of the Duelist's HP per serious round before defensive/elemental play, leaving the four state thresholds visible without turning the encounter into a sponge.

Completionist gearing/party selection can shorten the fight, but not so severely that the elemental-state identity is routinely erased before it appears.

**Verdict: PASS / RETAIN 1,700 HP.**

No raw-stat or Power change.

---

## 5. Mandatory boss — Regulation Crucible → The Seventh Reaction
### Actual pre-boss party levels
Current progression proof:
- mandatory route immediately pre-boss: **Lv15**;
- fixed-content completionist: **Lv17**;
- high-side: **~Lv18**.

### Form I — Regulation Crucible
Retain:
- Lv18;
- **2,400 HP core**;
- four 300-HP chambers;
- exactly two active/targetable chambers at a time;
- destroyed chamber slots stay empty;
- core-only windows remain possible.

### Form II — The Seventh Reaction
Retain:
- Lv19;
- **2,900 fresh HP**;
- genuine fresh-body transformation;
- current fresh-HP Prime refresh applies.

Existing projected full-encounter timing remains appropriate:
- mandatory Lv15: **~13–15 rounds** depending on chamber-control route;
- completionist Lv17: **~10–12 rounds**;
- high-side ~Lv18: **~9–11 rounds**.

This is the desired relationship: optional progression provides a strong advantage without making the chapter boss dynamically scale or disappear before its mechanics resolve.

**Verdict: PASS / RETAIN BOTH FORMS.**

No raw-stat or Power change.

---

## 6. Regional Hunt #4 — Crown Prototype
Current recommendation:
> **Lv20**

Current body:
- Lv20;
- **6,503 HP**;
- one bar;
- no transformation.

The Hunt can be accessed around the Chapter-4 return window while a mandatory chapter-clear party is roughly Lv17 and a completionist party may be around Lv18. That earlier access is intentionally **below recommendation** and should not force the Hunt down to chapter-clear difficulty.

Validate the proper fight at its recommended Lv20 benchmark. At Lv20 current incoming damage remains substantial but non-deleting, while 6,503 HP preserves Hunt-scale endurance.

**Verdict: PASS / RETAIN.**

Do not weaken Crown Prototype to Lv17 merely because the branch becomes reachable before its recommendation.

---

## 7. Formation recovery
The accepted Chapter-4 formation compositions and weights were restored to:

`09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_04_FORMATIONS.md`

Recovered compositions are used as formation authority only. Historical phase-specific enemy stats and obsolete formation-EXP rows were **not** restored.

---

## 8. v80 change ledger
### Numerical changes
> **NONE**

### Power changes
> **NONE**

### Restored organization data
- Chapter-4 opening/middle/late formation compositions and weights restored to their owning folder.
- Chapter-4 party-state boundary made explicit: Maevra is not the default Chapter-4 fifth; Vaelira joins after S022; active battle cap remains four.

### Remaining Chapter-4 dependency
- Elemental Researcher / Annex Battle Mage / Crucible Attendant exact separate battle placement remains unresolved and must not be invented.

---

# Final Chapter-4 verdict
> **PASS / VALIDATED**

Chapter 4 works at its actual progression points:
- opening **Lv13**;
- middle **~Lv15**;
- late/chapter-end **~Lv17**;
- mandatory Crucible pre-boss **Lv15**;
- completionist Crucible pre-boss **Lv17**;
- Crown Prototype proper recommendation **Lv20**.

The Power audit remains closed.

## Next frontier
> **Chapter 5 — Lv17 start → Lv22 end**, using exact in-chapter encounter positions and the party roster that exists at each point.
