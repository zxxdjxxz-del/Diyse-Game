# Diyse — Targeting and Automatic Retargeting
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current domain authority checked:** repository `docs/COMBAT_RULES.md`, current through **v2.20 / Audit135**, plus compatible Audit115, Audit120, Audit122, Audit135 and newer explicit user corrections.  
**Migration rule:** current explicit user corrections and current organized domain canon outrank stale/open wording inherited by v85.


## Normal turn-entry targeting

During ordinary round flow, a player selects an action and its legal target/content when that character's turn actually arrives.

The selected action then resolves immediately as that character's action package before the next normal combatant's turn begins.

Because ordinary player actions are no longer pre-queued for the whole round, a target defeated earlier in the round is simply unavailable when a later character reaches target selection.

## Automatic hostile retargeting

Automatic retargeting remains a safety rule for the narrower case where a selected hostile action has a legal target when chosen, but that target becomes invalid **between selection and final resolution** because of an explicit interrupt, reaction, or authored multi-step action package.

In that case:

1. retarget to the next living enemy in encounter-slot order after the original target;
2. if no later slot is living, wrap to the first living enemy;
3. if no enemies remain living, normal battle resolution proceeds.

Retargeting changes only the target.

It does **not** change:
- the selected action;
- its cost;
- the acting character;
- the already-established normal turn order.

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
