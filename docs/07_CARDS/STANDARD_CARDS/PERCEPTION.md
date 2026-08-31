# Diyse — Standard Cards: Perception
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary Card/Prime authority:** compatible **Audit116**, superseded where applicable by **Audit119**, **Audit122**, later current v85 working closures, and newer explicit Face correction.  
**Current written whole-project authority:** **v2.20 / Audit135** plus newer approved turn-entry initiative corrections.

**Face identity:** Accuracy-oriented effects, Evasion, Critical Hits, and Fields; reading the battlefield, positioning, timing, openings, and controlling or exploiting space. This Face does not create a natural Accuracy stat.

## Current count
**4**

| Card | MP | Target | Formula | Power | Base Hit | Effect | Acquisition |
|---|---:|---|---|---:|---:|---|---|
| **Faultline Sight** | 18 | one enemy | Information / support | — | — | Reveal currently knowable elemental weakness/resistance, harmful-status resistance/immunity, an already-committed readable action if present, and an exposed ordinary tactical opening. Never reveals future scripts, unrevealed phases, or future random choices. | Chapter 1 — Hollow Watch Castellan / S008 |
| **Measured Response** | 24 | one conscious ally; self legal | Support | — | — | Speed +15%; Base Hit +15; 3 rounds; refreshes, does not stack. | Chapter 5 — Deepforge Colossus |
| **Predicted Impact** | 28 | one enemy | Magical / Colorless | 180 | 110 | On successful damage: 30% Stun. | Regional Hunt #9 — Mercyfallen Behemoth |
| **Decisive Interval** | 36 | one enemy | Tactical state | — | — | Apply **Decisive Opening** until the target begins its next selected action. The first qualifying allied ordinary selected direct-damage action against that target receives +25% final damage and +30 percentage points of applicable same-axis penetration; consume the Opening after that action if at least one direct-damage component successfully damages the target. If the Opening survives to a later normal-round initiative setup and the target is an eligible ordinary enemy, its base Speed-derived turn slot is moved one position later at that setup under the exact resolver below. | Major Hunt #5 — Final Archive Arbiter |

## Decisive Opening — exact resolver
Decisive Opening is a **tactical state**, not a universal harmful status.

### Lifetime
Decisive Opening begins immediately when Decisive Interval resolves and ends at the first of:
- the qualifying allied direct-damage action consumes it;
- the target begins its next selected action;
- the target is defeated, leaves battle, or is replaced by another battle body;
- battle end.

Ordinary harmful-status cleanse and Status Resistance do not remove/resist Decisive Opening unless a later explicit effect says otherwise.

Reapplying Decisive Interval to the same target:
- refreshes/replaces the existing Decisive Opening;
- does not stack another Opening;
- does not create multiple initiative shifts or multiple damage payoffs.

A genuine fresh enemy body does not inherit Decisive Opening from the prior body.

### Damage / penetration payoff
The qualifying action must be an **ordinary allied selected action that directly damages the marked target**. Prime commands do not qualify merely because the party has an Opening recorded off-field.

When the first qualifying selected direct-damage action begins resolution against the marked target:
- its eligible direct-damage component(s) against that target gain **+25% final damage**;
- its applicable same-axis penetration gains **+30 percentage points** for those component(s);
- same-axis penetration still adds normally and remains capped at **75%** under `../../05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md`.

Axis handling:
- Physical component → +30pp Defense penetration;
- Magical component → +30pp Spirit penetration;
- Hybrid action → +30pp to each applicable Physical/Magical share independently;
- unused penetration on one axis never transfers to the other.

For a multihit selected action, every eligible direct-damage component of that **one selected action** against the marked target receives the Decisive Opening payoff.

Consumption occurs **after the complete selected action resolves** if at least one eligible direct-damage component successfully dealt positive direct HP damage to the marked target.

If the entire selected action misses, is invalidated, or deals no positive direct HP damage to that target, Decisive Opening is not consumed by that action and may still be used before its normal expiry.

### Ordinary-enemy initiative delay
The initiative-delay branch applies only to an eligible **ordinary enemy**. It does not delay:
- Elites;
- Regional Hunts;
- Major Hunts;
- mandatory bosses;
- protected/scripted combatants;
- support objects that do not receive an ordinary normal-turn slot.

Decisive Interval never reshuffles an initiative order that has already been fixed for the current round.

Therefore:
- if Decisive Interval is played **before** the target's current-round turn, that already-fixed turn stays where it is; when the target later begins that selected action, Decisive Opening ends normally and no later-round delay occurs;
- if Decisive Interval is played **after** the target already acted and the Opening remains active through the next beginning-of-round initiative setup, its one eligible delay may resolve there.

At that later beginning-of-round setup:
1. build the normal base turn order from current effective Speed and normal tie rules;
2. locate the marked ordinary enemy's one normal-turn slot;
3. if another eligible normal-turn slot follows it, swap the marked enemy with that immediately following slot, moving the enemy **exactly one position later in this base order**;
4. if the marked enemy is already last, no movement occurs;
5. the Decisive initiative-delay branch is then considered resolved for that Opening and cannot shift the target again;
6. apply any later-precedence explicit initiative reinsertion effects, including Routeweaver's `immediately after Torren` routing;
7. lock the round's initiative order normally.

The Opening itself may remain active after the one-slot delay for its damage/penetration payoff until the target begins its delayed selected action or another normal expiry condition occurs.

The delay:
- does not change Speed;
- does not grant or remove actions;
- does not make the enemy choose its action early;
- does not create a pending-action queue;
- does not expose the enemy's future action choice;
- does not carry to another enemy body.

The enemy still chooses its legal action using the real battle state when its delayed turn actually arrives.

## Global references
- MP prices use the current Audit119/v85 rebase.
- Harmful statuses resolve through `../../05_BATTLE_SYSTEM/STATUS_EFFECTS.md`.
- Base Hit/Evasion resolves through `../../05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md`.
- Initiative and next-round rerouting resolve through `../../05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`.
- Penetration resolves through `../../05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md`.
- Current Bleed timing/clearing follows Audit122/current organized status authority, not stale Audit116 heal-clears-Bleed wording.
