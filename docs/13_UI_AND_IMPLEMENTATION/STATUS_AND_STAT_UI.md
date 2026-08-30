# Diyse — Status & Stat UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Current core combat-stat labels
Use:
- HP
- MP
- Attack
- Magic
- Defense
- Spirit
- Speed
- Evasion
- Status Resistance

## No natural Accuracy
Do not put `Accuracy` on the ordinary character stat sheet as a natural stat.

Actions may show:
> **Base Hit**

when that information is useful.

## Status Resistance
Raw general bands:
- 0 — Normal
- 5 — Resistant
- 10 — Highly Resistant
- 15 — Exceptional

Exact UI representation may be numeric, descriptive, or both.
It must not imply these values are percentages.

## Harmful statuses
Universal current harmful statuses:
- Burn
- Freeze
- Stun
- Staggered
- Bleed

Do not restore generic:
- Poison;
- Slow;
- Silence;
- Blind;
- old Break state

unless a later specific authority explicitly reintroduces one.

## Guard / Defend
Guard remains valid as a deliberate defensive state where current rules support it.
`Defend` is the player's permanent command label.

Do not display `Brace`.
