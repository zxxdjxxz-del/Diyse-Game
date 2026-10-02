# Diyse — Enemy System Rules

**Status:** ACTIVE ENEMY / ENCOUNTER AUTHORITY  
**Authority:** current enemy-domain owner plus later explicit approved corrections.  


## Encounter-size cap
Maximum simultaneously active enemies:
> **8**

## Enemy action economy
Unless a specific authored encounter says otherwise:
- each enemy receives one selected ordinary action per legal opportunity;
- Speed controls ordering only;
- high Speed does not grant extra ordinary actions;
- no hidden ATB/initiative system exists.

## Information legality
Enemy AI may inspect legitimate visible/completed battlefield state.

It may not inspect:
- unconfirmed player commands;
- future random results;
- hidden player selections not yet committed.

## Cards
Enemies do **not** use Standard Cards or Prime Cards.

## Damage and status
Enemy actions use the same global current:
- Physical / Magical / Hybrid damage architecture;
- Base Hit / Evasion resolver;
- Critical rules where eligible;
- four standard elements;
- five universal harmful statuses.

Standard elements:
- Fire
- Ice
- Lightning
- Earth

Universal harmful statuses:
- Burn
- Freeze
- Stun
- Staggered
- Bleed

Ruin is a special affinity/school, not a fifth standard element.

## Status Resistance
Current raw-stat bands:
- 0 — Normal
- 5 — Resistant
- 10 — Highly Resistant
- 15 — Exceptional

Explicit immunity is separately authored.
Do not restore old percentage-based status tables as a second universal resolver.

## Removed-system firewall
Enemies may not silently restore:
- Barrier;
- Brace;
- global Break/Stagger meter;
- natural Accuracy;
- Water/Wind standard elements;
- Poison or retired generic status families;
- free universal intercepts;
- extra actions merely from thresholds/Speed;
- hidden command-reading.

Guard remains valid where deliberately authored.
Staggered remains a normal harmful status.


## Explicit action-Power gate
Every enemy action that deals direct HP damage must state exact numeric Power.

No enemy, Hunt, boss, or damaging support-object kit can be numerically certified with an unspecified direct-damage coefficient.

Non-damaging actions explicitly use `Power: N/A — no direct damage`.

See `05_BATTLE_SYSTEM/ACTION_POWER_REQUIREMENT.md`.
