# Diyse — Vaelira ← Cyanis Subclass Working Spec

**Status:** APPROVED CLASS-REWORK DESIGN — NOT YET MASTER CANON  
**Parent trackers:** `docs/CLASS_REWORK_MASTER_TRACKER.md`, `docs/CLASS_CEXP_WORKING_MODEL.md`, `docs/CLASS_MASTERY_WORKING_MODEL.md`  
**Authority boundary:** v1.84 / Audit99 plus newer explicit class-rework decisions. On August 21, 2026 the user explicitly approved the class-rework proposals that had previously been advanced under “Let’s continue.” Where an older provisional draft conflicts with a later refinement, the latest refinement below controls.

## 1. Approved identity

- **Subclass name: Axiomblade.**
- **Character/class pairing:** **Vaelira — Green Arcanist / Axiomblade**.
- Vaelira learns Cyanis's Crest Knight martial discipline without becoming a second Cyanis.
- No ordinary ally-intercept role.
- The CL4 normal ability is an **attack**.
- Damaging Axiomblade techniques support both learned **Swords** and Vaelira's native **Arcane Staffs**.
- **Staff + Focus** and **Staff + Shield** are supported advanced expressions.
- The subclass uses no new personal gauge, bespoke resource, or invented mark.

The core reciprocal contrast is intentional: Cyanis learns Vaelira's overt magical/elemental discipline through Crest Arcanist, while Vaelira learns Cyanis's disciplined martial Crest logic through Axiomblade.

## 2. Approved equipment progression

A donor passes the donor Base tradition's complete legal ordinary equipment package, staged by Subclass CL.

| Subclass CL | Equipment result |
|---:|---|
| **CL1** | Gain legal use of Cyanis's **Sword** family. |
| **CL3** | Gain legal use of **Crest Knight armor**. |
| **CL5** | Gain the complete legal Crest Knight Secondary package: **Shield** plus Cyanis's advanced permission to equip a **second Sword in Secondary**. |
| **CL10** | Equipment Mastery becomes eligible; purchasing it unlocks the Crest Knight donor **Relic**. |
| Synthesis | Later paired Legacy access under the final Synthesis rule. |

Vaelira's native Arcane Staff and Focus permissions remain legal under open equipment.

## 3. Approved selected-Subclass stat package

- **HP +6%**
- **Attack +6%**
- **Magic +6%**
- **Defense +8%**
- **Speed -6%**
- Spirit neutral

Intent: Axiomblade is genuinely martial and tougher than Green Arcanist while remaining fully compatible with Staff-based magical expressions. The old `HP +8 / Attack +8 / Defense +8 / Magic -6` draft is superseded.

## 4. Approved weapon-expression rule

For every damaging Axiomblade technique unless the ability explicitly establishes a special loadout branch:

- **Sword expression:** Physical damage against **Defense**.
- **Arcane Staff expression:** Magical damage against **Spirit**.
- Damage element is a separate property from Physical/Magical formula.
- With no elemental bridge active, Sword expressions remain neutral Physical and Staff expressions remain Colorless Magical.
- Shield, Focus, and second-Sword choices modify an ability only where that ability explicitly contains a loadout branch.

The ability does not inherit the equipped weapon's ordinary Attack hit pattern unless explicitly authored to do so.

## 5. Approved Trait — Formal Equivalence

### Rank I — CL1
When Vaelira deals damage with one of the six standard elements, that element becomes her **current expression** through the end of the following round.

Her next damaging Axiomblade ability during that window uses that element and consumes the current expression. A newer qualifying standard-element hit replaces the older stored expression.

- This is internal state, not a personal gauge; the UI may show a small elemental indicator.
- It does not create an Imprint by itself.
- It does not trigger a Composite Reaction by itself.
- Weapon formula remains Sword = Physical / Staff = Magical.
- **Prism Cycle precedence:** when Prism Cycle is active and compatible, Prism Cycle determines the element first. Formal Equivalence fills in only when Prism Cycle does not already determine the action's element.

### Rank II — CL6
After **Proven Advance resolves** or **Counterproof triggers**, Vaelira's next damaging Axiomblade ability before the end of the following round gains **+10% Power**.

### Rank III — CL12
When an Axiomblade attack is elementalized through Formal Equivalence and hits a target carrying the matching existing Imprint, it gains **15% relevant-defense penetration**:
- Sword expression → Defense penetration;
- Staff expression → Spirit penetration.

The Imprint is not consumed.

## 6. Approved five normal abilities

### CL1 — First Principle
**6 MP · one enemy · 150 Power**

- Sword: **150 Physical**.
- Staff: **150 Magical**.
- May consume Formal Equivalence's current expression.
- No Imprint, buff, penetration, or extra status rider.

### CL4 — Proven Advance
**8 MP · one enemy · 165 Power**

- Sword: **165 Physical**.
- Staff: **165 Magical**.
- May consume Formal Equivalence's current expression.
- After damage resolves, Vaelira gains **Minor Defense Up + Minor Spirit Up for 2 rounds**.
- No Elemental Guard rider.
- No redirect, ally intercept, or Prepared effect.

This supersedes the older `Crested Advance` version that added a matching Elemental Guard.

### CL7 — Counterproof
**9 MP · one enemy · 145 Power · +15 Base Hit · Prepared self-counter**

- Arms one response against the next eligible single-target hostile action that resolves against Vaelira.
- After that hostile action resolves, Vaelira counters the attacker.
- Sword: **145 Physical**.
- Staff: **145 Magical**.
- The counter may consume Formal Equivalence's current expression.
- No incoming-damage reduction, self-buff, ally intercept, or AoE trigger.
- Obeys the global one-armed Prepared-effect limit.

### CL9 — Axiom Rend
**13 MP · one enemy · 225 Power · 30% relevant-defense penetration**

- Sword: **225 Physical**, 30% Defense penetration.
- Staff: **225 Magical**, 30% Spirit penetration.
- May consume Formal Equivalence's current expression.
- If elementalized and the target carries the matching existing Imprint, gains **+10% final damage**.
- Does not consume the Imprint.

### CL11 — Equivalent Form
**16 MP · one enemy · requires a legal Sword or Arcane Staff in Weapon**

| Loadout | Approved expression |
|---|---|
| **Sword only** | **200 Physical Power**. |
| **Sword + Shield** | **190 Physical Power**; after resolving, **15% direct-damage reduction through the end of the following round**. |
| **Dual Swords** | **2 × 110 Physical Power = 220 total**. |
| **Arcane Staff only** | **200 Magical Power**. |
| **Arcane Staff + Focus** | **205 Magical Power**; **20% Spirit penetration**. |
| **Arcane Staff + Shield** | **190 Magical Power**; after resolving, **15% direct-damage reduction through the end of the following round**. |

Formal Equivalence may elementalize any legal expression. With no current expression, Sword branches remain neutral Physical and Staff branches remain Colorless Magical.

Equivalent Form adds no extra Imprint, Elemental Guard, Field, counter, or secondary status beyond its authored loadout branch.

## 7. Approved Ultimate — Final Axiom

**All enemies · 320 Power · player chooses one of the six standard elements**

- Sword equipped: **320 Physical** of the chosen element + **25% Defense penetration**.
- Arcane Staff equipped: **320 Magical** of the chosen element + **25% Spirit penetration**.
- All conscious permanent allies gain the matching established **Elemental Guard for 2 rounds**.
- The chosen element is direct and does **not** depend on or consume Formal Equivalence's stored current expression.
- Shield, Focus, and second-Sword choices do not create additional Ultimate branches.
- No Imprint, Elemental Field, cleanse, broad Defense/Spirit buff package, ally intercept, or Composite Reaction is added.

## 8. Approved Subclass Mastery nodes

Each costs 1 MP under the inherited nine-point Mastery economy.

| Node | Eligibility | Approved effect |
|---:|---:|---|
| **Subclass 1 — Foundational Proof** | CL3 | **First Principle +15 Power**; if it consumes Formal Equivalence's current expression, **+5 Base Hit**. |
| **Subclass 2 — Proven Position** | CL5 | **Proven Advance +15 Power**; its Minor Defense Up and Minor Spirit Up last **+1 round**. |
| **Subclass 3 — Exact Rebuttal** | CL7 | **Counterproof +20 Power**; **Axiom Rend +10 Base Hit** against a target carrying the matching existing Imprint. |
| **Subclass 4 — Equipment Mastery** | **CL10** | Unlocks legal use of the Crest Knight donor **Relic**. |

## 9. Interaction with Green Arcanist Base abilities

- Core Element Array / Shaping Element Array can establish Formal Equivalence's current expression.
- Prism Cycle has explicit precedence when it is active and compatible.
- Existing Imprints can improve Axiom Rend and Formal Equivalence Rank III.
- Composite Surge remains the Base payoff for opposite-family reactions; Axiomblade does not create a second Composite system.
- Elemental Field remains a Green Arcanist Base battlefield-control tool.
- Arcanum Ascendant remains Vaelira's Base elemental-dominance Ultimate and is distinct from Final Axiom.

## 10. Superseded working names

The following older working labels are superseded by the approved names above:
- Prismatic Discipline → **Formal Equivalence**
- Prism Edge → **First Principle**
- Crested Advance → **Proven Advance**
- Refracted Counter → **Counterproof**
- Prismatic Rend → **Axiom Rend**
- Crest Form → **Equivalent Form**
- Prism Bastion → **Final Axiom**
- Tempered Spectrum → **Foundational Proof**
- Forward Geometry → **Proven Position**
- Return Angle → **Exact Rebuttal**

## 11. Remaining open work

The Axiomblade class package above is approved at the class-rework level. Remaining work is downstream implementation/promotion work rather than ordinary redesign:
- final runtime data implementation and regression tests;
- equipment-stat balance against final production weapon values;
- Cyanis/Vaelira Synthesis and paired Legacy resolution;
- later promotion into the appropriate master-canon audit when the whole class-rework package is ready.
