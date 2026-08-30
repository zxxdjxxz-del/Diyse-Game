# Diyse — Targeting and Automatic Retargeting
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current domain authority checked:** repository `docs/COMBAT_RULES.md`, current through **v2.20 / Audit135**, plus compatible Audit115, Audit120, Audit122, Audit135.  
**Migration rule:** current master canon outranks stale/open wording inherited by v85.


## Automatic hostile retargeting

If a queued player hostile action targets an enemy that is defeated before the queued action resolves during the same round:

1. retarget to the next living enemy in encounter-slot order after the original target;
2. if no later slot is living, wrap to the first living enemy;
3. if no enemies remain living, normal battle resolution proceeds.

Retargeting changes only the target.

It does **not** change:
- the selected action;
- its cost;
- its priority;
- the actor's Speed;
- the acting character.

This applies by default to:
- Attack;
- hostile/damaging Abilities;
- hostile/damaging Standard Card commands;
- equivalent directly controlled Prime hostile commands;

unless an individual action explicitly overrides the normal rule.

## Multi-target / multi-hit hit checks

Unless an action explicitly defines one shared roll:
- each authored direct hit resolves its own hit check;
- each target of a multi-target action resolves its own hit check.
