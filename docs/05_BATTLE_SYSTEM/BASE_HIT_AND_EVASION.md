# Diyse — Base Hit and Evasion
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current domain authority checked:** repository `docs/COMBAT_RULES.md`, current through **v2.20 / Audit135**, plus compatible Audit115, Audit120, Audit122, Audit135 and newer explicit battle-system corrections.  
**Migration rule:** current master canon outranks stale/open wording inherited by v85.


## No natural Accuracy stat

Diyse has no natural character `Accuracy` stat.

Use:
- **Base Hit** — authored on the action;
- **Evasion** — target-side avoidance property.

Application reliability is a separate chance-based secondary/utility-effect modifier owned by `APPLICATION_RELIABILITY.md`; it is not Accuracy and does not modify the hit roll.

## Resolver

> **AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers**

> **EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers**

> **FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)**

Roll an integer from **1–100**.

- Roll ≤ Final Hit Chance → hit
- Roll > Final Hit Chance → miss

Ordinary clamp:
- minimum **5%**
- maximum **100%**

Explicit guaranteed-hit, forced-miss, immunity, or scripted overrides may bypass the ordinary clamp only when directly authored.


## Permanent-character / guest default

For **Basic Attack** and learned **permanent-character or story-guest direct-damage Abilities**, if the owning current action sheet does not print a separate Base Hit value, use:

> **Base Hit = 100**

This is the standard reliable-action baseline and closes the migration omission where normalized player Ability sheets retained Power/MP/effects but omitted a repeated `100` Base Hit field.

Boundaries:
- an explicitly authored Base Hit always overrides this default;
- explicit `+Base Hit` modifiers add after the action's base value under the normal resolver;
- Standard Cards and Prime commands use their own authored Base Hit values and are **not** rewritten by this rule;
- enemy actions/support objects continue using their owning action sheets;
- scripted guaranteed-hit/forced-miss rules still override the ordinary resolver where explicitly authored.

## Authoring bands

Normal reference targets:
- standard reliable action — about **100 Base Hit**
- heavy / deliberately less reliable — about **90–95**
- precision — about **105–115**
- exceptional precision — up to about **120**

The action's exact authored Base Hit always controls.

## Evasion

Evasion does not automatically scale upward with level.

Current practical reference bands inherited by the design:
- ordinary target — **0**
- evasive — about **5–10**
- specialist evasive — about **15–20**
- extreme authored evasive — about **25–30**
- rare temporary authored effects may exceed 30.

`Evasion +X` means flat points unless the effect explicitly says percentage.

## Modifier ordering

Percentage modifiers apply to the authored/base value first.

Flat point modifiers apply afterward.

## Hit versus application

Hit/Evasion and secondary application are separate checks.

For a damaging hit with an attached harmful-status or other hit-attached chance-based rider:

1. resolve Base Hit / Evasion;
2. a miss deals no direct damage and does not reach that hit's Critical roll;
3. a miss also prevents that hit-attached rider from attempting application;
4. on a hit, resolve any eligible chance-based application separately under `APPLICATION_RELIABILITY.md` and the rider's owning rule.

A modifier written as `+N Base Hit / application reliability where relevant` may affect both stages separately if the action actually uses both; it never combines them into one roll.

## Current Staggered boundary

Current **Staggered does not modify Base Hit or Evasion**.

Its current universal stat package is:
- Attack −20%;
- Magic −20%;
- Speed −20%.

Older text mapping Staggered to `Accuracy −20%`, `Base Hit −20%`, or Evasion penalties is retired and must not be restored.
