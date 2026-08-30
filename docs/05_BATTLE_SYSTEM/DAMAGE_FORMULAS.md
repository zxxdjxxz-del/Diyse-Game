# Diyse — Direct Damage Formulas
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current domain authority checked:** repository `docs/COMBAT_RULES.md`, current through **v2.20 / Audit135**, plus compatible Audit115, Audit120, Audit122, Audit135.  
**Migration rule:** current master canon outranks stale/open wording inherited by v85.


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

## Global direct-damage rules

There is:
- no hidden universal AoE penalty;
- no universal random ±damage variance.

Authored Power already accounts for target count and action identity.

Multihit actions resolve their authored hit Powers individually.

Round HP damage once at the normal final-damage step after all legal damage layers are resolved.

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
