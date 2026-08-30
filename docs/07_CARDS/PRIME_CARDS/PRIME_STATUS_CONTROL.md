# Diyse — Prime Status and Control Rules
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary Card/Prime authority:** compatible **Audit116**, superseded where applicable by **Audit119**, **Audit122**, and later current v85 working closures.  
**Current written whole-project authority:** **v2.20 / Audit135**.  


Primes are not blanket-immune to harmful statuses.

Default Prime application susceptibility:
> **80%**

for:
- Burn
- Freeze
- Stun
- Staggered
- Bleed

Prime-local statuses disappear on dismissal and do not transfer to the returning party.

## Burn
- 80% susceptibility;
- normal Prime-local Burn value;
- cannot outlive remaining manifestation duration.

## Bleed
Prime-specific handling remains a dedicated manifestation exception:
- 80% susceptibility;
- full Prime-local Bleed action value;
- bounded to the Prime manifestation's own round/action handling.

Global current Bleed rules remain in `05_BATTLE_SYSTEM/STATUS_EFFECTS.md`.

## Staggered
- 80% susceptibility;
- full Speed / Base Hit / Evasion penalty.

## Freeze
- 80% susceptibility;
- may deny at most **1 selected Prime command per application**;
- then ends;
- successful direct Physical damage still breaks Freeze after the hit where the global rule applies.

## Stun
- 80% susceptibility;
- **20%** chance to lose the selected Prime command on an affected Prime turn;
- one Stun application may cause at most one lost Prime command.

## Control Guard
Across one 3-round manifestation:

> Freeze and Stun together may deny at most **1 selected Prime command**.

After that one hard-control loss, the Prime becomes Freeze/Stun immune for the rest of that manifestation.

This prevents a three-round manifestation from being reduced to zero usable commands while preserving status interaction.
