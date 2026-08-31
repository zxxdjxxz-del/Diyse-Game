# Diyse — Ability Rules
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Master-canon class/resource authority:** **v2.08 / Audit123**, with compatible **Audit115** class normalization and later current working corrections.  
**Authority treatment:** explicit/newer working corrections are preserved as working overrides when they have not yet been promoted into the audit chain.


## Universal class-Ability rules

- **MP** is the universal ordinary Ability resource.
- Do not create character-specific combat gauges/resources.
- Every damaging Ability is explicitly authored as **Physical**, **Magical**, or **Hybrid**.
- Damage type is authored by the Ability; equipment does not choose it.
- Learned Abilities remain weapon-independent once learned unless an individual current rule explicitly says otherwise.
- Element/affinity is separate from damage type.
- Global damage, penetration, Base Hit/Evasion, application reliability, Critical, elements, and harmful-status rules are owned by `05_BATTLE_SYSTEM`.

## Application reliability

When a class effect grants `+N application reliability`, use `05_BATTLE_SYSTEM/APPLICATION_RELIABILITY.md`.

The bonus is **+N percentage points** to an eligible chance-based application check. It is not Base Hit, does not invent a secondary effect, does not turn an automatic effect into a roll, and does not bypass immunity/protected/scripted legality.

## Ruin
For **character Abilities** that actually deal Ruin damage:

> **Hybrid / Ruin = 75% Attack / 25% Magic**

unless a later explicit rule changes that specific Ability.

Ruin is a special affinity/school, not a fifth standard element.

## Healing
Healing uses **Magic** as its output stat where a healing coefficient is authored.

**Spirit is the defensive magic-resistance stat.**

Do not restore old healing text that scales from Spirit merely because an archived file used that terminology.

## Prepared/setup effects and class states
Prepared states and class setup states may exist when explicitly authored, but:
- they are not universal harmful statuses;
- they do not create extra ordinary actions by default;
- they do not recreate removed global gauges.

Default lifecycle, KO behavior, battle-end clearing, target/body replacement, refresh/replacement, and class-state category boundaries are owned by:
> `CLASS_STATE_LIFECYCLE.md`

Individual class sheets still own the exact trigger, subject, duration, payload, consumption rule, and any explicit lifecycle override for their state.

Prepared/delayed-action flow remains additionally subject to `05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`. Awakened Prime suspension/pause behavior remains owned by `07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md`.

## Removed class-mechanic firewalls
Do not restore:
- Card Seals;
- Imprints;
- global Break/Stagger meter;
- Barrier;
- Brace;
- global Rune-effect system.

`Rune` may survive in an Ability name such as **Siphon Rune** without creating a Rune subsystem.


## Explicit Power requirement
Every class Ability that deals direct damage must state an exact numeric Power.

Multi-hit actions must state exact per-hit Power or exact total plus split.

Non-damaging class commands use:
> **Power: N/A — no direct damage**

See `05_BATTLE_SYSTEM/ACTION_POWER_REQUIREMENT.md`.


## Base Hit completion for true-battle resolution
Unless an owning current Ability explicitly prints another Base Hit, a permanent-character or story-guest direct-damage Ability uses **Base Hit 100** under `05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md`. Explicit action values and modifiers override/add normally.
