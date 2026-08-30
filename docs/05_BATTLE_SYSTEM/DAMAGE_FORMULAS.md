# Diyse — Direct Damage Formulas
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current domain authority checked:** repository `docs/COMBAT_RULES.md`, current through **v2.20 / Audit135**, plus compatible Audit115, Audit120, Audit122, Audit135 and newer explicit defensive-layer corrections.  
**Migration rule:** current explicit user corrections and current organized domain canon outrank stale/open wording inherited by v85.

## Physical

> **BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)**

> **EffectiveDefense = CurrentDefense × (1 - EffectiveDefensePenetration)**

## Magical

> **BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)**

> **EffectiveSpirit = CurrentSpirit × (1 - EffectiveSpiritPenetration)**

`Spirit` is the current defensive magic-resistance stat.

## Hybrid

Resolve authored Physical and Magical weighted components independently.

> **PhysicalComponent = PhysicalWeight × [Attack² / (Attack + EffectiveDefense)] × (Power / 100)**

> **MagicalComponent = MagicalWeight × [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)**

Then:

> **HybridNormalDirectDamage = PhysicalComponent + MagicalComponent**

Do not:
- average Attack and Magic;
- average Defense and Spirit;
- transfer unused penetration from one axis to another.

## Ruin

For **character Abilities** that actually deal Ruin damage, the current universal Ruin weighting remains:

> **75% Attack / 25% Magic**

Ruin is a special affinity/school, not a fifth standard element.

Prime commands use their own explicitly authored formulas and are not automatically forced into this character-Ability weighting.

## Penetration

Same-axis penetration:
- adds in percentage points;
- applies only to its own defensive axis;
- caps at **75%**.

Do not round the penetrated defensive stat early.

## Direct-damage-reduction layer

After the eligible direct-damage package has resolved its normal offensive/defensive calculation, apply the active direct-damage-reduction layer before the final HP-damage rounding step.

For an eligible hit:

> **ReducedDirectDamage = PreReductionDirectDamage × (1 - ActiveDirectDamageReduction)**

where `ActiveDirectDamageReduction` is expressed as a decimal fraction.

### Stacking

If more than one ordinary direct-damage-reduction percentage is active on the target:
- use only the **strongest active legal reduction**;
- do not add the percentages together;
- do not multiply separate reduction percentages together;
- every source keeps its own duration independently;
- when the strongest expires, a weaker still-active reduction may resume.

Example:
- 10% direct-damage reduction + 15% direct-damage reduction = **15%**, not 25% and not 23.5%;
- standard Guard/Defend at 50% + another 15% effect = **50%** while Guard is active.

An explicitly authored effect may define a special stacking exception, but ordinary effects do not infer one.

### Interaction with defensive stats

Direct-damage reduction is a separate layer from:
- Defense;
- Spirit;
- penetration;
- temporary percentage Defense/Spirit Up/Down.

Temporary Defense/Spirit changes resolve through `STAT_CHANGES.md` before penetration and direct-damage reduction are applied. Legacy `Total Defense` wording is not a separate layer; it resolves as equal percentage Defense/Spirit changes under `STAT_CHANGES.md`.

### Eligible damage

By default this layer applies to ordinary direct:
- Physical damage;
- Magical damage;
- Hybrid damage;
- eligible Critical direct damage;
- individual direct hits of a multihit action.

By default it does **not** reduce:
- Burn;
- Bleed;
- other indirect damage;
- fixed damage;
- percentage-Max-HP damage;
- healing;
- revival.

An explicit owning rule may override eligibility for a specific effect.

## Global direct-damage rules

There is:
- no hidden universal AoE penalty;
- no universal random ±damage variance.

Authored Power already accounts for target count and action identity.

Multihit actions resolve their authored hit Powers individually.

Resolve any eligible Critical/final-damage multipliers and the legal direct-damage-reduction layer without early integer rounding, then round HP damage once at the normal final-damage step.

## Basic Attack

The universal Attack command is:
- **100 Power**
- **Physical**
- **Neutral** unless equipment explicitly authors another affinity
- no harmful-status rider unless equipment explicitly grants one.

## Outside this formula

Separately authored indirect/fixed systems remain outside the ordinary direct-damage equation, including:
- Burn;
- Bleed;
- fixed damage;
- % Max-HP damage;
- healing;
- revival.

Critical resolution is defined separately in `CRITICAL_HITS.md`.
Temporary Attack / Magic / Defense / Spirit / Speed changes resolve through `STAT_CHANGES.md`.
Standard Guard/Defend resolves through `GUARD.md`.
