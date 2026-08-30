# Diyse — Temporary Stat Changes
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current authority basis:** compatible Audit115/Audit116 stat-change language plus newer explicit status and turn-entry corrections.  
**Authority rule:** this file owns the global temporary Attack / Magic / Defense / Spirit / Speed Up/Down framework. Individual Abilities, Cards, equipment, enemies, and encounters own which changes they apply and for how long.

## Scope

This framework covers temporary combat changes to:
- Attack
- Magic
- Defense
- Spirit
- Speed

These temporary stat changes are **not universal harmful statuses**. Status Resistance does not automatically resist them, and ordinary harmful-status remedies do not automatically remove them.

This file does **not** redefine:
- Base Hit / Evasion changes;
- Status Resistance changes;
- Critical modifiers;
- penetration;
- direct-damage reduction;
- Guard;
- persistent equipment raw stats;
- persistent level, class-selection, Trait, or other non-temporary stat construction.

Those remain under their owning rules.

## All temporary core-stat Up/Down values are percentages

Temporary Attack / Magic / Defense / Spirit / Speed Up/Down effects are **always percentage-based**.

Therefore:
- `Attack +10` means **Attack +10%**;
- `Magic −15` means **Magic −15%**;
- `Defense +20` means **Defense +20%**;
- `Spirit −10` means **Spirit −10%**;
- `Speed +15` means **Speed +15%**.

Production-facing current files should print the `%` sign explicitly rather than relying on the shorthand.

There is **no ordinary temporary flat-bonus layer** for Attack, Magic, Defense, Spirit, or Speed.

This rule does **not** convert persistent/raw stat construction into percentages. Equipment raw stats, level/class stat construction, and other persistent stat values remain authored in their normal raw units.

It also does not convert different mechanics that use flat values by design. For example, `Base Hit +10`, `Evasion +5`, `Status Resistance +10`, Power changes, penetration percentage points, and direct-damage reduction keep their own owning units.

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

## Retired `Total Defense` shorthand

Older/current migrated files may contain wording such as `+10 Total Defense`, `+15 Total Defense`, `+20 Total Defense`, or `+25 Total Defense`.

`Total Defense` is **not a third stat and not a flat defensive layer**.

Interpret that legacy shorthand as equal percentage increases to the two defensive stats:
- `+10 Total Defense` = **Defense +10% / Spirit +10%**;
- `+15 Total Defense` = **Defense +15% / Spirit +15%**;
- `+20 Total Defense` = **Defense +20% / Spirit +20%**;
- `+25 Total Defense` = **Defense +25% / Spirit +25%**.

Current production-facing files should prefer the explicit `Defense +N% / Spirit +N%` wording instead of `Total Defense`.

Because these are ordinary Defense/Spirit percentage changes, they participate in the normal same-axis strongest-Up / strongest-Down rules above. They do **not** coexist as an additional separate flat layer.

Example:
- Defense +20% plus legacy `+15 Total Defense` = **Defense +20%**, not +35%;
- if no other Spirit Up is active, the same legacy package still supplies **Spirit +15%** for its own remaining duration.

## Direct-damage reduction remains separate

Direct-damage reduction is not Attack, Magic, Defense, Spirit, or Speed.

A legal direct-damage-reduction effect may coexist with percentage Defense/Spirit changes unless its owning rule explicitly prohibits that combination.

Its own stacking/resolution behavior remains under `DAMAGE_FORMULAS.md` and `GUARD.md`; it is never converted into a stat percentage merely because both mechanics are defensive.

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

## Current class normalization closures

The current class shorthand resolves as follows:
- War Archer — **Pinning Strike:** Speed −20% for 2 rounds.
- Ruin Vanguard — **Controlled Apocalypse:** Major Attack Down + Major Magic Down = Attack −30% / Magic −30% for 2 rounds.
- Crest Arcanist — **Arcane Rupture:** Minor Magic Down = Magic −10% for 2 rounds.
- Axiomblade — **Proven Advance:** Minor Defense Up + Minor Spirit Up = Defense +10% / Spirit +10% for 2 rounds.
- Vowblade — **Vow of Severance:** Minor Defense Down + Minor Spirit Down = Defense −10% / Spirit −10% for 2 rounds.
- Proofhunter — **Pin the Variable:** Speed −20% for 2 rounds.
- Routeweaver — **Clear Route:** Speed +10% for 2 rounds.
- Routeweaver — **Crossroads / Forward Route:** Speed +10% for 2 rounds.
- Routeweaver — **Crossroads / Covered Route:** Defense +15% / Spirit +15% for 2 rounds.
- Routeweaver — **Open the Way:** Speed +15% while the Route Field is active.

The owning class sheets should print those exact percentage values rather than retaining raw `+N`/`−N` core-stat shorthand.
