# Diyse — Application Reliability
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current authority basis:** current Base Hit/Evasion, harmful-status, class, Card, and equipment wording reconciled under the fixed turn-entry battle model.  
**Authority rule:** this file owns the meaning and resolution of **application reliability**. Individual Abilities, Cards, Traits, equipment, enemies, and encounters own which actions receive a reliability bonus and which effects they attempt to apply.

## Definition

`Application reliability +N` means:
> **+N percentage points to an eligible chance-based application check.**

It is a flat percentage-point modifier, not a percentage multiplier.

Examples:
- base 20% application chance +10 reliability = 30% before target-side resistance;
- base 35% chance +12 reliability = 47% before target-side resistance.

## Eligible checks

Application reliability may modify a chance-based check for an already-authored effect such as:
- Burn / Freeze / Stun / Staggered / Bleed application;
- an ordinary negative stat change that explicitly has an application chance;
- an explicitly chance-based dispel, purge, interrupt, control, or other utility application;
- another effect whose owner explicitly identifies its resolution as an application check.

The owning action still determines whether such a check exists.

## What reliability does not do

Application reliability does **not**:
- modify Base Hit or Evasion;
- modify Critical Chance unless explicitly authored separately;
- alter damage, healing, Power, penetration, duration, or magnitude;
- turn an automatic/guaranteed effect into a chance-based effect;
- turn an ineligible effect into an eligible one;
- invent a harmful status or secondary rider an action does not already possess;
- bypass explicit immunity, protected/scripted states, or encounter legality;
- make an ordinary cleanse, heal, revive, Field creation, or deterministic Field removal roll when its owner does not use an application check.

If an action must first hit before its attached effect can be attempted, the hit check still resolves first. A miss prevents a hit-attached application attempt regardless of reliability.

## Generic resolver

For an eligible ordinary chance-based application check:

> **FinalApplicationChance = BaseApplicationChance + legal application-reliability bonuses + other legal owner-specific chance modifiers - applicable target-side resistance**

Unless another owning rule explicitly defines a different clamp:
> **FinalApplicationChance = clamp(FinalApplicationChance, 5, 95)**

Explicit guarantee, immunity, forced failure, or script overrides the ordinary clamp.

Application-reliability bonuses from different legal sources add as percentage points before the final clamp. There is no separate hidden reliability stat or reliability gauge.

The same named/effect-identity bonus does not duplicate itself unless its owner explicitly says it can stack; ordinary reapplication/conditional wording controls whether that source is active.

## Harmful-status integration

For the five universal harmful statuses, the global status resolver is therefore:

> **FinalStatusChance = BaseChance + AffinityModifier + legal specialist bonuses + legal application-reliability bonuses - StatusResistance**

Then clamp to **5%–95%** except explicit immunity, guarantee, or script.

Application reliability is therefore additive with legal specialist bonuses but remains separate from the target's Status Resistance.

Example:
- Burn base chance 20%;
- +10 application reliability;
- +5pp legal specialist bonus;
- target Status Resistance 10;
- final chance = 20 + 10 + 5 - 10 = **25%**.

## `Base Hit / application reliability` wording

When a current effect says `+N Base Hit / application reliability where relevant`:
- add **+N Base Hit** to any hit check the affected action actually makes;
- add **+N percentage points application reliability** to any eligible chance-based application check the affected action actually makes.

If the action uses both kinds of checks, both bonuses may matter during their respective resolution steps.
If the action uses only one, the irrelevant half does nothing.

This wording does not merge hit chance and application chance into one roll.

## Automatic and deterministic effects

If an action says an effect occurs automatically on a successful hit or automatically when another condition is satisfied, application reliability does not alter that effect.

If a target has a separately authored independent resistance roll against an otherwise automatic effect, that resistance remains owned by its own rule. Application reliability does not silently reduce an independent resistance roll unless that owner explicitly routes the roll through this application resolver.

## Prime and suspension boundary

Application reliability belongs to the action/effect that receives it.

Ordinary-party reliability bonuses do not automatically transfer to an Awakened Prime body or Prime command during party suspension unless a Prime effect explicitly says so.

Prime commands may use application reliability only where their own current Prime text explicitly grants it or another legal Prime-local effect applies it.

## Firewall

Do not create:
- a natural Reliability character stat;
- an Accuracy synonym;
- a separate reliability meter;
- automatic immunity bypass;
- a universal resistance stat beyond the specifically authored target-side resistance already owned by the relevant mechanic.
