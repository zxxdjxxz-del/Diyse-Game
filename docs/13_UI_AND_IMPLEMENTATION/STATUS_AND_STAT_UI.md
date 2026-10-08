# Diyse — Status and Stat UI

**Status:** ACTIVE UI SPEC  
**Gameplay authority:** `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`.

## Core stats

The UI may display the current core combat stats where appropriate:

- HP
- MP
- Strength
- Magic
- Intelligence
- Defense
- Spirit
- Speed

There are no additional universal hit, evade, luck, crit-chance, or status-resistance character stats.

## Current battle states/statuses

Player-facing status/buff/debuff names:

- Quick
- Slow
- Stuck
- Asleep
- Poison
- Wounded
- Sealed
- Ward
- Regen
- Doomed
- Strength / Magic / Intelligence / Defense / Spirit Up or Down

Status displays should expose duration/countdown information when the player is entitled to know it.

Quick/Slow should communicate TURN-spacing impact. Stuck should communicate its queued-EXECUTION risk. Doomed requires a visible countdown.

Stat Up/Down should identify the affected stat and remaining affected TURNs.

Prime-local states belong to the Prime HUD and disappear when that Prime demanifests unless an explicit ability modifies the suspended party instead.
