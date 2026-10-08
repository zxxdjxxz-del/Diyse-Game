# Diyse — Enemy System Rules

**Status:** ACTIVE ENEMY / ENCOUNTER STRUCTURAL AUTHORITY  
**Authority:** current enemy/encounter owner plus `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`.

## Encounter-size cap

Maximum simultaneously active enemies:

> **8**

## Enemy action economy

Enemies use the same ordered TURN / EXECUTION framework as the party.

Unless an encounter explicitly says otherwise:

- each enemy receives one command opportunity when its TURN arrives;
- selected action schedules its next TURN at selection;
- Immediate actions resolve at once;
- queued actions create an EXECUTION marker;
- an enemy cannot receive another command TURN while its own prior action remains pending;
- Speed governs personal TURN spacing;
- high Speed does not create an unrelated extra-action subsystem.

## Information legality

Enemy AI may inspect legitimate battlefield state available at its TURN.

It may not inspect:
- uncommitted player choices;
- future random results;
- hidden selections unavailable to the encounter.

## Cards

Enemies do not use Standard Cards or Prime Cards.

## Combat rules

Enemy actions use current global:

- Physical / Magical / Hybrid output rules;
- Potency/fixed-effect authoring;
- Critical rules where eligible;
- Fire / Ice / Lightning / Earth affinities;
- current status vocabulary;
- current status susceptibility model;
- Delay / Interrupt classifications;
- targeting and retargeting;
- TURN / EXECUTION / Return timing.

Ruin may be used where explicitly authored as a special affinity/school rather than a fifth standard element.

## Status susceptibility

Chance-based status application uses the battle-system susceptibility model:

- Vulnerable ×1.5
- Normal ×1.0
- Resistant ×0.5
- Immune ×0

Boss/Hunt susceptibility is authored per status. Prefer resistance over blanket immunity where appropriate.

## Action authoring gate

Every scalable direct-damage enemy action must define exact **Potency** or another explicit current damage rule.

Every current enemy action must define the fields required by the battle system, including Execution/Return and Delay/Interrupt eligibility where applicable.

Exact enemy combat bodies/action kits are open for recertification unless their owning file has already been rebuilt under the current battle system.
