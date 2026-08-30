# Diyse — Turn and Round Rules
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current domain authority checked:** repository `docs/COMBAT_RULES.md`, current through **v2.20 / Audit135**, plus compatible Audit115, Audit120, Audit122, Audit135.  
**Migration rule:** current master canon outranks stale/open wording inherited by v85.


## Core structure

Diyse uses traditional discrete rounds.

1. Resolve beginning-of-round effects and immediate battle-state checks.
2. Each enemy locks one legal action using the legitimate beginning-of-round state and may not inspect unconfirmed player commands.
3. The player selects one action for every conscious active party member before confirming the round.
4. Resolve **Item** actions first, ordered by current effective Speed.
5. Resolve **Defend** actions second, ordered by current effective Speed.
6. Resolve all remaining party and enemy actions from highest to lowest current effective Speed.
7. Party members win exact Speed ties against enemies.
8. Tied party members resolve in player-selected order.
9. Tied enemies/entities use a stable deterministic order.
10. Finish complete action/reaction/state-change packages, then resolve end-of-round processing.

## Speed rule

Speed controls ordering only.

Speed does **not**:
- grant additional ordinary actions;
- create ATB-style extra turns;
- create a universal initiative gauge;
- allow a character to act twice merely for being much faster.

## Command list

Exactly:
- Attack
- Ability
- Card
- Item
- Defend

Do not introduce universal:
- Swap
- Reserve
- Assist
- Row
- Move
- Wait
- Timeline
- personal-resource commands

without explicit change control.

## Party size

Maximum active permanent-party size:
# **4**
