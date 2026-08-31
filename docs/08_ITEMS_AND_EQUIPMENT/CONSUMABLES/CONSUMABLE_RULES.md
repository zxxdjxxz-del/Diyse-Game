# Diyse — Consumable Use Rules
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary written equipment authority:** compatible **Audit117 / Audit118 / Audit121**, plus newer accepted v85 tracker-level equipment closures and newer explicit user corrections.  
**Current written whole-project authority:** **v2.20 / Audit135**.  
**Rule:** where v85 contains a later explicitly accepted equipment decision that has not yet been promoted, preserve it as **tracker-level final / pending formal promotion** rather than rewriting older audit history.


## Battle use
Ordinary consumable use:
- consumes the user's selected battle action;
- does not create an extra action;
- cannot exceed Max HP/Max MP;
- excess recovery is lost.

## Status cure groups
Trauma Remedy:
- Burn
- Bleed

Stability Remedy:
- Freeze
- Stun
- Staggered

General Remedy:
- one eligible ordinary harmful status

Full Remedy:
- all eligible ordinary harmful statuses

These remedies do not automatically remove:
- ordinary stat changes unless item explicitly says so;
- Fields;
- Guard;
- Hunter's Measure;
- class setup states;
- boss scripted/protected states.

## Bleed interaction
Current Audit122 behavior controls:
- ordinary partial healing does **not** clear Bleed;
- reaching full HP may clear Bleed;
- an eligible status-removal item can explicitly remove Bleed.

## Blinding Mist
Guaranteed escape applies only to eligible ordinary random encounters.
It does not trivialize:
- Elites
- Regional Hunts
- Major Hunts
- mandatory bosses
- authored no-flee encounters

## Balance Seal — exact package
Balance Seal is the dedicated ordinary stat-restoration consumable.

Target:
> **one conscious ally; self legal**

When Balance Seal resolves, remove **every eligible standalone negative temporary stat effect** currently attached to that ally.

Eligible axes include, where an effect actually exists:
- Attack;
- Magic;
- Defense;
- Spirit;
- Speed;
- Base Hit;
- Evasion;
- Status Resistance;
- another explicitly authored removable temporary stat penalty.

Balance Seal removes the underlying eligible negative effect identity, not merely the target's current net numerical deficit.

Therefore, if a target has:
- Attack +30% from one positive effect; and
- Attack −20% from a different removable negative effect,

Balance Seal removes the −20% source and leaves the +30% source intact.

If several different eligible negative stat effects are active at once, **one Balance Seal removes all of them**. It is not limited to one axis or one contribution.

### What Balance Seal does not remove
Balance Seal does **not** remove:
- Burn;
- Freeze;
- Stun;
- Staggered;
- Bleed;
- any stat rider that exists only because one of those harmful statuses remains active;
- positive stat effects;
- Fields themselves;
- Guard;
- Hunter's Measure or other class tactical/setup states merely because they are not ordinary stat effects;
- protected encounter states;
- scripted states;
- permanent/natural stats;
- equipment stats.

Status-carried penalties therefore remain tied to their status owner. Examples:
- Burn's Defense −10% / Spirit −10% remain until Burn ends or is legally removed;
- Staggered's Attack −20% / Magic −20% / Speed −20% remain until Staggered ends or is legally removed.

Balance Seal is not a harmful-status remedy and does not partially strip those riders away from an otherwise still-active status.

A continuously maintained or protected external source may also be ineligible for Balance Seal under its own rules. Balance Seal does not destroy the external source itself.

## Emergency Kit — exact package
Emergency Kit is the exceptional full-recovery / cleanse / Prime-restoration consumable.

It does **not** revive a KO character. Emergency Rally remains the party revival item.

When Emergency Kit legally resolves on a recipient:
1. restore **75% Max HP**;
2. restore **60% Max MP**;
3. remove **all eligible negative status effects** currently on that recipient, including every removable ordinary harmful status from the universal set Burn / Freeze / Stun / Staggered / Bleed;
4. remove **all eligible negative temporary stat effects** currently applied to that recipient;
5. restore **every acquired Prime identity** to Ready under `../../07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md`.

### Negative-stat cleanup
The negative-stat cleanup is intentionally broad.

It removes every removable temporary negative stat modifier currently attached to the recipient, regardless of stat axis or source, including where applicable:
- Attack;
- Magic;
- Defense;
- Spirit;
- Speed;
- Base Hit;
- Evasion;
- Status Resistance;
- another separately authored removable temporary stat penalty.

If a removed harmful status carries a stat rider, that rider ends with the status normally.

Emergency Kit does not remove positive stat effects.

Emergency Kit does not by itself erase a non-stat mechanic merely because that mechanic also caused a removable stat penalty. It removes the eligible negative stat contribution. A still-active external source may reapply its penalty later if its own rules say it continuously does so.

### Protection boundaries
Emergency Kit does not destroy or bypass:
- Fields themselves;
- Guard;
- class setup/tactical states merely because they are not harmful statuses;
- protected encounter mechanics;
- scripted states or scripted defeat/continuation rules;
- permanent/natural stats;
- equipment stats.

However, any **removable negative temporary stat contribution** attached to the recipient remains eligible for Emergency Kit even when its source is not a canonical harmful status, unless that contribution is explicitly protected/scripted.

### Prime restoration
Emergency Kit is an explicit valid Prime-restoration effect.

Its Prime restoration:
- restores **all acquired Story and Major-Hunt Prime identities**, not only currently equipped/assigned Primes;
- changes every spent acquired Prime identity back to **Ready**;
- may restore a Prime spent earlier in the same battle or in a previous battle;
- does not change a Story Prime's Recovered/Awakened progression state;
- does not acquire a Prime the player has not obtained;
- does not remove or bypass the separate **2 full normal party round** post-dismissal Prime-spacing gate.

Therefore Prime restoration and Prime invocation spacing remain separate systems: a Prime may be Ready because of Emergency Kit while still temporarily blocked from invocation until the spacing requirement is complete.

## Exceptional items
Emergency Kit does not revive.
Emergency Rally is the party revival item.

No consumable bypasses protected phase transitions or scripted defeat/continuation rules.
