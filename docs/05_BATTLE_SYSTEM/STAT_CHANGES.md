# Diyse — Temporary Stat Changes
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current authority basis:** compatible Audit115/Audit116 stat-change language plus newer explicit status and turn-entry corrections.  
**Authority rule:** this file owns the global temporary Attack / Magic / Defense / Spirit / Speed Up/Down framework. Individual Abilities, Cards, equipment, enemies, and encounters own which changes they apply; this file supplies the default magnitude, duration, stacking, and cap rules unless an owning effect explicitly overrides them.

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

Production-facing current files should print the `%` sign explicitly rather than relying on shorthand.

There is **no ordinary temporary flat-bonus layer** for Attack, Magic, Defense, Spirit, or Speed.

This rule does **not** convert persistent/raw stat construction into percentages. Equipment raw stats, level/class stat construction, and other persistent stat values remain authored in their normal raw units.

It also does not convert different mechanics that use flat values by design. For example, `Base Hit +10`, `Evasion +5`, `Status Resistance +10`, Power changes, penetration percentage points, and direct-damage reduction keep their own owning units.

## Magnitude tiers and default duration

When a temporary core-stat effect uses a named tier instead of printing its own percentage, use exactly:

| Tier | Up | Down | Default duration |
|---|---:|---:|---:|
| **Minor** | **+10%** | **−10%** | **4 rounds** |
| **Standard** | **+20%** | **−20%** | **3 rounds** |
| **Major** | **+30%** | **−30%** | **2 rounds** |

For exact percentages that are not one of the named tiers, use the following default duration only when the owning effect does not print another duration:
- **1–10% magnitude:** 4 rounds;
- **11–20% magnitude:** 3 rounds;
- **21–30% magnitude:** 2 rounds;
- **above 30%:** must be explicitly authored and must state its own duration.

An explicitly authored duration overrides this default. Conditional equipment Traits, Fields, Prime handoffs, encounter states, and other bespoke effects may therefore use a different stated window when intentionally authored.

An explicitly authored numeric percentage also overrides the tier table. For example, `Speed +15%` remains +15%; it is not rounded or promoted to Standard.

Unqualified production-facing wording such as `Attack Up`, `Magic Down`, or `Defense Up` should not remain numerically ambiguous. The owning current effect should state either an exact percentage or one of the named tiers.

## Timing

A temporary stat change becomes active immediately when its application resolves unless its owning effect explicitly establishes a later start.

Therefore:
- Attack and Magic changes affect later eligible output calculations immediately;
- Defense and Spirit changes affect later eligible incoming-damage calculations immediately;
- Speed changes become active immediately as stat modifiers, but normal initiative already fixed for the current round is not reshuffled;
- if a Speed change remains active at the next beginning-of-round initiative check, it affects that round's order normally.

Numbered-round duration follows `TURN_AND_ROUND_RULES.md`:
- the application round counts as round 1 when the change is applied during normal turn resolution;
- an effect created during end-of-round processing begins counting with the next round;
- explicit wording such as `through the end of the following round` remains literal and overrides generic duration shorthand.

## Stacking and per-axis cap

Temporary core-stat modifiers **can stack**.

For each of Attack, Magic, Defense, Spirit, and Speed independently:
1. every active eligible positive modifier from a **different effect identity** contributes its full percentage;
2. every active eligible negative modifier from a **different effect identity** contributes its full percentage;
3. positive contributions are summed up to a maximum of **+40%** on that stat;
4. negative contributions are summed down to a maximum of **−40%** on that stat;
5. the capped positive and negative totals then oppose one another to produce the current net modifier.

Examples:
- Attack +10% and Attack +20% = **Attack +30%**;
- Attack +30% and Attack +30% from two different legal effect identities = **Attack +40%**, not +60%;
- Attack −20% plus Attack −30% = **Attack −40%**, not −50%;
- Attack +30% with Attack −20% = **net Attack +10%**;
- Attack +40% with Attack −40% = **net 0%**, while both sets of effects remain active on their own timers.

The effective temporary core-stat multiplier is therefore bounded to the range:
> **60% to 140% of the pre-temporary constructed stat**

unless a specific scripted encounter state explicitly overrides the normal cap.

Apply the net temporary percentage to the already-constructed combat stat after natural stat, selected-class multiplier, and persistent/raw equipment additions. Round the final temporarily modified stat to the nearest whole number after the net percentage is applied.

## Same-effect reapplication

The same named/effect-identity modifier on the same target does **not** create another generic stack.

Reapplication:
- refreshes that effect's duration;
- replaces its own prior magnitude if the newly applied magnitude is different;
- does not add a second copy of itself unless the owning effect explicitly says it is self-stackable.

Different effect identities may stack normally even when they modify the same stat.

Each active effect keeps its own independent duration. When one expires or is removed, the remaining active effects are immediately re-summed under the same ±40% cap.

## Status-rider interaction

A harmful status that carries a stat reduction participates in the same stacking/cap framework.

Current examples:
- Burn contributes **Defense −10% / Spirit −10%** while Burn remains active;
- Staggered contributes **Attack −20% / Magic −20% / Speed −20%** while Staggered remains active.

Status-carried stat changes use the **status's own duration**, not the generic magnitude-duration table above.

Burn and Staggered still do not stack with duplicate copies of themselves because their status rules govern reapplication. Their stat riders **do** stack with different ordinary stat-reduction effects up to the normal −40% per-axis cap.

Example:
- Staggered Attack −20% plus Controlled Apocalypse Attack −30% = **Attack −40%** while both remain active;
- when Controlled Apocalypse expires, Staggered's −20% continues for its remaining status duration.

## Awakened Prime suspension and stat-duration clocks

Awakened Prime rounds are distinct from normal party rounds.

When an Awakened Prime replaces/suspends the active party:
- an ordinary party member's active normal-round temporary Attack/Magic/Defense/Spirit/Speed modifiers remain recorded;
- **Prime rounds do not consume their normal-round duration checkpoints**;
- those suspended-party modifiers do **not** automatically transfer to or modify the Prime body;
- when the party returns, the modifiers resume with the same remaining normal-round duration they had when suspension began.

Prime-local temporary core-stat modifiers:
- affect the Prime body only;
- use an explicitly authored Prime-round/action window where stated;
- disappear when that Prime dismisses unless the command explicitly creates a separate return-to-party effect.

For current Prime text, the phrases **`authored window`**, **`next window`**, or **`next-Prime-round window`** attached to a Prime-local core-stat modifier are normalized to:
> **active immediately through the end of the next Prime round, or until dismissal if dismissal occurs first**

A Prime return-to-party stat modifier begins when the party returns. If it says `N full normal rounds`, that wording is literal. If a return stat modifier has no explicit duration, use the normal magnitude-based default duration from this file in normal party rounds.

Current Prime normalization examples:
- Last Sentinel — Unbroken March Defense +15% / Spirit +15%: through end next Prime round.
- Last Sentinel — Hold the Line Defense +25% / Spirit +25%: through end next Prime round.
- Last Sentinel — Last Bastion return Defense +20% / Spirit +20%: **3 normal rounds** by the Standard-duration default unless separately re-authored.
- Last Sanctuary — Hallowed Wave Defense +15% / Spirit +15%: through end next Prime round.
- Last Sanctuary — Consecrated Refuge Defense +25% / Spirit +25%: through end next Prime round or dismissal.
- Dawn Shepherd — Shepherd's Wake Defense +15% / Spirit +15%: through end next Prime round.
- Oathbound Colossus — Siege Ram Defense +10% / Spirit +10%: through end next Prime round.
- Oathbound Colossus — Iron Oath Defense +25% / Spirit +25%: through end next Prime round.

## Encounter-state duration override

An encounter state or phase that explicitly says a modifier lasts **for the remainder of that state**, **for the remainder of battle**, or while a named state/window is active uses that state boundary instead of the generic 4/3/2-round duration table.

Examples include:
- Last Run;
- Open Concordance;
- Prismatic Confluence;
- Archive Burden / Custody Protocol / Transfer Window;
- WORLDFRAME / WORLDHEART EXPOSED / FINAL CONSTRUCTION.

Those state modifiers still use percentage values, participate in ordinary ±40% stacking unless explicitly protected/overridden, and are removed/replaced when their owning state says so.

A selected Guard/buff action that explicitly says `through the end of the following round` keeps that literal shorter window rather than inheriting a magnitude-based default.

## Retired `Total Defense` shorthand

Older/current migrated files may contain wording such as `+10 Total Defense`, `+15 Total Defense`, `+20 Total Defense`, or `+25 Total Defense`.

`Total Defense` is **not a third stat and not a flat defensive layer**.

Interpret that legacy shorthand as equal percentage changes to Defense and Spirit:
- `+10 Total Defense` = **Defense +10% / Spirit +10%**;
- `+15 Total Defense` = **Defense +15% / Spirit +15%**;
- `+20 Total Defense` = **Defense +20% / Spirit +20%**;
- `+25 Total Defense` = **Defense +25% / Spirit +25%**;
- negative `Total Defense` values reduce both Defense and Spirit by the same percentage.

Current production-facing files should prefer explicit `Defense ±N% / Spirit ±N%` wording.

These contributions stack with different Defense/Spirit modifiers and obey the same ±40% per-axis cap.

## Direct-damage reduction remains separate

Direct-damage reduction is not Attack, Magic, Defense, Spirit, or Speed.

A legal direct-damage-reduction effect may coexist with percentage Defense/Spirit changes unless its owning rule explicitly prohibits that combination.

Its own stacking/resolution behavior remains under `DAMAGE_FORMULAS.md` and `GUARD.md`; it is never converted into a stat percentage merely because both mechanics are defensive.

## High-rank enemies

Ordinary temporary stat changes do not receive a universal Regional-Hunt / Major-Hunt duration or magnitude conversion merely because the target is high rank.

They remain legal at their authored/default magnitude and duration unless:
- the owning action gives a specific high-rank rule;
- the owning encounter gives a specific resistance/immunity/override;
- another current global rule explicitly supersedes them.

This is separate from high-rank conversion rules for the five universal harmful statuses.

## Removal / restoration

Ordinary harmful-status cleanse does not remove ordinary temporary stat changes unless explicitly authored to do so.

Eligible stat-restoration effects such as **Balance Seal** and class effects explicitly capable of clearing ordinary negative stat changes may restore affected axes toward normal according to their owning rules.

## Current class normalization closures

Current ordinary class stat-change durations are normalized to the global magnitude table unless an Ability explicitly owns a special timing window:
- War Archer — **Pinning Strike:** Speed −20% for **3 rounds**.
- Ruin Vanguard — **Controlled Apocalypse:** Attack −30% / Magic −30% for **2 rounds**.
- Crest Arcanist — **Arcane Rupture:** Magic −10% for **4 rounds**.
- Axiomblade — **Proven Advance:** Defense +10% / Spirit +10% for **4 rounds**.
- Vowblade — **Vow of Severance:** Defense −10% / Spirit −10% for **4 rounds**.
- Proofhunter — **Pin the Variable:** Speed −20% for **3 rounds**.
- Routeweaver — **Clear Route:** Speed +10% for **4 rounds**.
- Routeweaver — **Crossroads / Forward Route:** Speed +10% for **4 rounds**.
- Routeweaver — **Crossroads / Covered Route:** Defense +15% / Spirit +15% for **3 rounds**.
- Routeweaver — **Open the Way:** Speed +15% while the Route Field is active; Field duration remains separately authored.

The owning class sheets should print those exact percentage values and durations.
