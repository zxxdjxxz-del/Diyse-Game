# Diyse — Six-Subclass Cross-Balance / Consistency Audit — 2026-08-21

**Status:** APPROVED CLASS-REWORK CROSS-BALANCE PASS — NOT YET MASTER-CANON PROMOTED  
**Parent authority:** v1.84 / Audit99 plus newer approved class-rework decisions.  
**Purpose:** verify that all six reciprocal Subclasses are mechanically distinct, internally consistent, progression-compatible, equipment-legal, and balanced closely enough to proceed to Synthesis / Legacy design without reopening the completed class packages unnecessarily.

Approved subclass sources:
- `docs/CYANIS_VAELIRA_SUBCLASS_WORKING_SPEC.md` — Crest Arcanist
- `docs/VAELIRA_CYANIS_SUBCLASS_WORKING_SPEC.md` — Axiomblade
- `docs/ILYRA_SEYRIK_SUBCLASS_WORKING_SPEC.md` — Vowblade
- `docs/SEYRIK_ILYRA_SUBCLASS_WORKING_SPEC.md` — Ruin Warden
- `docs/TORREN_NIMERA_SUBCLASS_WORKING_SPEC.md` — Routeweaver
- `docs/NIMERA_TORREN_SUBCLASS_WORKING_SPEC.md` — Truthshot

The user's standing class-rework approval rule applies: material advanced under the current “Let's continue” sequence is approved, and a later explicit refinement supersedes an older conflicting version.

---

## 1. Audit result

**PASS.** No broad raw-number rebalance is required before Synthesis design.

The six Subclasses occupy different tactical spaces and no current package is judged to invalidate its owner's Base Class or collapse into a duplicate of the donor's Base Class.

| Subclass | Primary tactical identity | Late-game payoff |
|---|---|---|
| **Crest Arcanist** | high-cost magical Crest control, penetration, Fields/seals | AoE Colorless control + Dominion Crest Field |
| **Axiomblade** | flexible martial/caster translation by weapon loadout | AoE chosen-element attack + party Elemental Guard |
| **Vowblade** | offensive sustain / hybrid pressure / mercy-through-damage | very high single-target Hybrid strike + party stabilization |
| **Ruin Warden** | conversion healing, drain sharing, cleansing, revival | AoE damage converted into party recovery/protection |
| **Routeweaver** | hybrid route control, Fields, Card sequencing, utility | non-damaging major party Route Field |
| **Truthshot** | accurate Great-Bow quarry exploitation / hard-target pressure | high-penetration single-target finisher |

This asymmetry is intentional. Equal CL does not require equal Power values because MP cost, targeting, penetration, healing, Field control, Prepared effects, weapon opportunity cost, and conditional requirements differ substantially.

---

## 2. Selected-Subclass stat-package audit

Approved packages remain unchanged:

- **Crest Arcanist:** MP +10% / Magic +10% / Spirit +6% / Attack -6%
- **Axiomblade:** HP +6% / Attack +6% / Magic +6% / Defense +8% / Speed -6%
- **Vowblade:** HP +8% / Attack +10% / Spirit +8% / Defense -6%
- **Ruin Warden:** HP +6% / MP +8% / Magic +6% / Spirit +6% / Speed -4%
- **Routeweaver:** MP +8% / Attack +6% / Magic +6% / Accuracy +6% / Defense -6%
- **Truthshot:** Attack +8% / Accuracy +8% / Speed +6% / Defense -6%

Do **not** rebalance these by simple arithmetic sum. Accuracy, MP, Speed, HP, Attack, Magic, Spirit, and defensive stats do not have identical combat value, and each package is tied to a distinct role and equipment opportunity cost.

**Audit decision:** no stat-package changes.

---

## 3. Progression / Power-curve audit

### CL1 identity abilities

The intentionally different CL1 Power values remain approved:
- Crest Arcanist / Arcane Lance — 220 Colorless Magical, 16 MP, 25% Spirit penetration
- Axiomblade / First Principle — 150, 6 MP
- Vowblade / Vital Edge — 185 Hybrid, 8 MP + authored self-heal
- Ruin Warden / Siphon Rune — 165 Hybrid, 8 MP + Drain
- Routeweaver / Throughline — 160 Hybrid, 7 MP + Measure accuracy interaction
- Truthshot / Measured Shot — 120 Physical, 6 MP + applies Hunter's Measure

Crest Arcanist's larger opening number is paid for by substantially higher MP cost and specialization. Truthshot's smaller opening number establishes the shared quarry state that powers the rest of the kit. No flattening is required.

### CL11 abilities

The CL11 set also passes without raw-number changes:
- Elemental Convergence — elemental magical penetration / self Guard
- Equivalent Form — loadout-sensitive flexible attack
- Vow of Severance — 250 Hybrid / 30% penetration / Defense + Spirit Down
- Reclaimed Breath — revival rather than damage
- Forced Passage — 260 Hybrid / 30% penetration / hostile-Field removal
- Corroboration — 4-hit 240 Physical package with Measure scaling

The fact that Ruin Warden's CL11 is non-damaging is deliberate; revival is the late-game completion of Seyrik's learned preservation doctrine.

### Ultimates

The Ultimate set is intentionally split rather than normalized to one damage template:
- **Crest Dominion:** 330 AoE Colorless Magical + major control Field
- **Final Axiom:** 320 AoE chosen element + party matching Elemental Guard
- **Mercy's Final Edge:** 520 single-target Hybrid + self/party recovery + short DR
- **Mercy Through Ruin:** 320 AoE Colorless Magical + party heal/cleanse/Total Defense
- **Open the Way:** no direct damage; major multi-round Route Field
- **Final Annotation:** 360 single-target Physical + very high accuracy/penetration and conditional hard-target/Measure payoff

**Audit decision:** no Ultimate Power changes. Final universal Ultimate MP-cost convention remains a separate global rule.

---

## 4. Weapon-gating / persistent-ability audit

The open-equipment/open-ability system does **not** require every Ability to work with every weapon. Weapon requirements are legal when the ability itself explicitly establishes them.

Approved matrix:

| Subclass | Weapon rule |
|---|---|
| **Crest Arcanist** | **weapon-independent once learned**; Crest spells do not require an Arcane Staff |
| **Axiomblade** | damaging techniques require a legal **Sword or Arcane Staff** expression where authored; Equivalent Form has explicit loadout branches |
| **Vowblade** | **weapon-independent across Wardrod / Two-Handed Sword expressions** |
| **Ruin Warden** | **weapon-independent across Two-Handed Sword / Wardrod expressions** |
| **Routeweaver** | **weapon-independent across Great Bow / Conduit expressions** |
| **Truthshot** | **Great-Bow-gated**; its damaging techniques are actual War Archer bow arts and require a Great Bow equipped |

Truthshot's Great-Bow gate is intentionally stricter than Routeweaver/Vowblade/Ruin Warden because the subclass's combat grammar is literal archery: prepared shots, pinning shots, multishot pressure, and a final bow finisher. Open abilities persist as learned permissions, but an unavailable weapon requirement can still make the command temporarily unusable under the current loadout.

Abilities never inherit the equipped weapon's ordinary Attack hit pattern unless explicitly authored.

---

## 5. Hybrid-formula normalization

Every Hybrid Ability should expose its stat split and applicable defensive treatment in implementation-facing data.

Already explicit:
- Vowblade damaging abilities — **50% Attack / 50% Spirit Hybrid**
- Routeweaver damaging abilities — **50% Attack / 50% Magic Hybrid**

Approved clarification for Ruin Warden:
- **Siphon Rune** — one authored hit, **60% Attack / 40% Magic Hybrid**, using the applicable Defense / Spirit contributions before the Hybrid result is combined.

This deliberately echoes Seyrik's native Ruin Vanguard hybrid language while leaving the rest of Ruin Warden's offensive healing kit primarily Colorless Magical / Spirit-facing.

---

## 6. Trait and resource audit

PASS.

None of the six Subclasses creates a prohibited personal gauge or separate action economy.

- **Crest Attunement**, **Formal Equivalence current expression**, and **Field Weaving sequencing states** are temporary authored states, not personal resource bars.
- **Living Covenant** is a normal self stance.
- **Hunter's Measure** is an established shared quarry state, not a new Nimera-only mark.
- Prepared effects remain subject to the one-armed Prepared-effect rule.
- No Subclass adds extra Standard Card slots, extra Card actions, draw/discard mechanics, or extra ordinary actions.

Every Subclass remains functional without its selected Trait active; Traits improve the selected-class expression rather than being required for unlocked abilities to resolve legally.

---

## 7. Mastery audit

PASS.

All six Subclass boards preserve the approved four-node model:
- Subclass Node 1 — CL3
- Subclass Node 2 — CL5
- Subclass Node 3 — CL7
- **Subclass Node 4 / Equipment Mastery — CL10**

Equipment Mastery consistently grants the donor Relic and does not delay ordinary donor equipment until late game.

Mastery Nodes 1–3 primarily improve CL1–9 tools rather than making CL11/CL13 abilities arrive incomplete. This distribution remains desirable and unchanged.

---

## 8. Defense / damage-reduction consistency rule

Several approved abilities use percentage **direct-damage reduction** while others use **Total Defense**. These are intentionally distinct concepts.

This class-rework pass does **not** establish additive stacking of multiple percentage direct-damage-reduction effects.

Approved implementation boundary:
- each Subclass keeps its authored DR percentage;
- overlapping DR effects use the final global combat-modifier stacking rule once that rule is normalized;
- no class spec may assume that two different 10%/15%/20% DR effects simply add together unless a later global rule explicitly says so.

This preserves current class numbers without accidentally creating an unreviewed party-wide additive mitigation engine.

---

## 9. Timing-language normalization

For class-rework implementation text, phrases such as:
- `through the following round`
- `through end following round`
- `through the end of the following round`

are to be normalized to the player/engine meaning:

**through the end of the following round**

unless an individual effect explicitly establishes a different timing boundary.

This is a wording normalization, not a duration buff or nerf.

---

## 10. Reciprocal-pair balance

### Cyanis ⇄ Vaelira
The pair shares elemental/Crest logic without becoming mirror kits. Vaelira's Base element/Imprint systems can feed Axiomblade, while Crest Arcanist remains Colorless/control-forward and only selectively borrows elemental choice.

### Ilyra ⇄ Seyrik
The pair is deliberately inverse:
- Vowblade turns violence into survival.
- Ruin Warden turns Ruin into preservation.

Their healing overlap is acceptable because Blue Warden remains Ilyra's superior pure-healing identity, while both Subclasses require offense/conversion or weaker revival rules to approach that space.

### Torren ⇄ Nimera
Hunter's Measure is the explicit shared tactical language. Routeweaver owns Fields/Card sequencing; Truthshot owns direct quarry exploitation. The pair can cooperate without requiring both characters in the active four.

No additional cross-pair synergy is added in this pass. **Synthesis** is the correct place to build the final paired payoff.

---

## 11. Production / readability audit

PASS.

The existing presentation plans remain viable:
- Vowblade and Ruin Warden deliberately invert blue-white Grace / violet Ruin dominance.
- Routeweaver reuses Great Bow, Conduit, line, Field, and Card-junction assets.
- Axiomblade's Sword/Staff expression can share core body-animation families with weapon-specific strike/cast variants.
- Crest Arcanist relies primarily on spell/Field/seal VFX rather than bespoke weapon animation.
- Truthshot should reuse Torren's Great-Bow animation grammar with Nimera-specific analytical timing/VFX rather than requiring a second full bow-animation library.

No cross-balance change requires a new expensive presentation system.

---

## 12. Approved conclusion / next gate

The six current Subclass packages are **stable enough to proceed to reciprocal Synthesis design**.

This audit does not promote the class rework into whole-project master canon yet. Remaining gates:
1. design the three reciprocal **Synthesis** effects and paired Legacy-resolution requirements;
2. finalize Core Mastery effect text / Synthesis eligibility wording;
3. normalize the global direct-damage-reduction stacking rule and universal Ultimate cost convention;
4. perform the deliberate stale-terminology sweep to **Sixfold Volition**;
5. run final implementation/data regression review;
6. promote the completed package through a new master-canon audit.
