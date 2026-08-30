# Diyse — Consumable Use Rules
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary written equipment authority:** compatible **Audit117 / Audit118 / Audit121**, plus newer accepted v85 tracker-level equipment closures.  
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

## Exceptional items
Emergency Kit does not revive.
Emergency Rally is the party revival item.

No consumable bypasses protected phase transitions or scripted defeat/continuation rules.
