# Diyse — Temporary Stat Changes
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current authority basis:** compatible Audit115/Audit116 stat-change language plus newer explicit status and turn-entry corrections.  
**Authority rule:** this file owns the global temporary Attack / Magic / Defense / Spirit / Speed Up/Down framework and the inherited `Total Defense` shorthand. Individual Abilities, Cards, equipment, enemies, and encounters own which changes they apply and for how long.

## Scope

This framework covers temporary combat changes to:
- Attack
- Magic
- Defense
- Spirit
- Speed
- flat `Total Defense` packages

These temporary stat changes are **not universal harmful statuses**. Status Resistance does not automatically resist them, and ordinary harmful-status remedies do not automatically remove them.

This file does **not** redefine:
- Base Hit / Evasion changes;
- Critical modifiers;
- penetration;
- direct-damage reduction;
- Guard;
- persistent equipment raw stats;
- persistent level, class-selection, Trait, or other non-temporary stat construction.

Those remain under their owning rules.

## Percentage tiers

When a temporary stat effect uses a named tier instead of printing its own percentage, use exactly:

| Tier | Up | Down |
|---|---:|---:|
| **Minor** | **+10%** | **−10%** |
| **Standard** | **+20%** | **−20%** |
| **Major** | **+30%** | **−30%** |

An explicitly authored numeric percentage overrides the tier table. For example, an authored `Speed +15%` remains +15%; it is not rounded or promoted to Standard.

Unqualified production-facing wording such as `Attack Up`, `Magic Down`, or `Defense Up` should not remain numerically ambiguous. The owning current effect should state either an exact percentage or one of the named tiers.

## Timing

A temporary stat change becomes active immediately when its application resolves unless its owning effect explicitly establishes a later start.

Therefore:
- Attack and Magic changes affect later eligible output calculations immediately;
- Defense and Spirit changes affect later eligible incoming-damage calculations immediately;
- Speed changes become active immediately as stat modifiers, but normal initiative already fixed for the current round is not reshuffled;
- if a Speed change remains active at the next beginning-of-round initiative check, it affects that round's order normally.

Numbered-round duration follows `TURN_AND_ROUND_RULES.md` unless the owning effect prints another timing boundary.

## Percentage stacking by stat axis

For each stat independently:
1. among active percentage **Up** effects, use only the strongest Up value on that stat;
2. among active percentage **Down** effects, use only the strongest Down value on that stat;
3. the strongest Up and strongest Down may coexist and oppose one another;
4. same-sign percentage effects never add together merely because they come from different sources.

Example:
- Attack +20% and Attack +10% active together = **Attack +20%**, not +30%;
- if Attack −30% is also active, the active percentage result on that axis is **net −10%** while all three effects remain present on their own timers.

Each source keeps its own duration independently. When a stronger modifier ends, a weaker still-active modifier can become the governing modifier for the remainder of its own duration.

Reapplying the same named temporary stat effect refreshes its authored duration unless that effect explicitly says otherwise; it does not create an additive copy.

## Status-rider interaction

A harmful status that carries a stat reduction participates in the same same-axis percentage rule.

Current examples:
- Burn's Defense −10% / Spirit −10%;
- Staggered's Attack −20% / Magic −20% / Speed −20%.

Those reductions therefore do not add to a separate same-axis negative percentage modifier. The strongest active reduction on that stat governs, with independent durations preserved.

## Total Defense — exact meaning

`Total Defense +N` is inherited shorthand for one temporary defensive package that grants:

> **Defense +N and Spirit +N as flat bonuses for the same authored duration.**

It is **not**:
- a third defensive stat;
- a percentage increase;
- direct-damage reduction;
- Guard;
- Barrier;
- a replacement for Defense or Spirit.

Examples:
- `+10 Total Defense` = **Defense +10 / Spirit +10**;
- `+15 Total Defense` = **Defense +15 / Spirit +15**;
- `+20 Total Defense` = **Defense +20 / Spirit +20**;
- `+25 Total Defense` = **Defense +25 / Spirit +25**.

This definition applies wherever current Abilities, Standard Cards, Primes, or encounter effects use the exact `Total Defense` wording.

### Total Defense stacking

Multiple active `Total Defense` packages do **not** add together.

Use only the **strongest active Total Defense value**. Every source retains its own duration, so a weaker still-active package resumes after a stronger one expires.

Reapplying the same named source refreshes that source's authored duration unless its owner explicitly says otherwise.

A `Total Defense` package may coexist with percentage Defense/Spirit changes because they are different modifier layers.

## Flat modifiers and resolution order

An explicitly flat temporary modifier such as `+10 Speed` remains flat and is not converted into a percentage tier.

For a legal ordinary stat calculation that contains both temporary percentage and temporary flat modifiers:

1. establish the persistent combat stat from level/class/equipment and other persistent construction;
2. resolve the active percentage Up/Down result for that stat;
3. apply the legal temporary flat modifier for that stat, including the governing `Total Defense` value where applicable.

Therefore a target with 100 Defense, Defense +10%, and +15 Total Defense has **125 Defense** while both effects are active.

Persistent equipment raw stats are part of the established persistent combat stat and are not temporary flat modifiers under this rule.

## Direct-damage reduction remains separate

Direct-damage reduction is not Defense, Spirit, or Total Defense.

A legal direct-damage-reduction effect may coexist with Total Defense and percentage Defense/Spirit changes unless its owning rule explicitly prohibits that combination.

Its own stacking/resolution behavior remains under the owning damage/defensive-effect rules rather than being converted into Total Defense.

## High-rank enemies

Ordinary temporary stat changes do not receive a universal Regional-Hunt / Major-Hunt duration or magnitude conversion merely because the target is high rank.

They remain legal at their authored magnitude/duration unless:
- the owning action gives a specific high-rank rule;
- the owning encounter gives a specific resistance/immunity/override;
- another current global rule explicitly supersedes them.

This is separate from the high-rank conversion rules for the five universal harmful statuses.

## Removal / restoration

Ordinary harmful-status cleanse does not remove ordinary temporary stat changes unless explicitly authored to do so.

Eligible stat-restoration effects such as **Balance Seal** and class effects explicitly capable of clearing ordinary negative stat changes may restore the affected axis toward normal according to their owning rules.

Positive Total Defense is an ordinary positive temporary effect where the owning purge/removal rule is legally able to remove such effects.

## Current class normalization closures

The current incomplete class shorthand is resolved as follows:
- War Archer — **Pinning Strike:** Speed −20% for 2 rounds.
- Ruin Vanguard — **Controlled Apocalypse:** Major Attack Down + Major Magic Down = Attack −30% / Magic −30% for 2 rounds.
- Crest Arcanist — **Arcane Rupture:** Minor Magic Down = Magic −10% for 2 rounds.
- Axiomblade — **Proven Advance:** Minor Defense Up + Minor Spirit Up = Defense +10% / Spirit +10% for 2 rounds.
- Vowblade — **Vow of Severance:** Minor Defense Down + Minor Spirit Down = Defense −10% / Spirit −10% for 2 rounds.
- Proofhunter — **Pin the Variable:** Speed −20% for 2 rounds.

The owning class sheets should print those exact values rather than retaining deferred or unqualified shorthand.
