# Diyse — Turn and Round Rules
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current domain authority checked:** repository `docs/COMBAT_RULES.md`, current through **v2.20 / Audit135**, plus compatible Audit115, Audit120, Audit122, Audit135 and newer explicit user corrections.  
**Migration rule:** current explicit user corrections and current organized domain canon outrank stale/open wording inherited by v85.


## Core structure

Diyse uses traditional discrete rounds with **turn-entry command selection**.

1. Resolve beginning-of-round effects and immediate battle-state checks.
2. At the beginning of the round, establish the normal turn order for all eligible combatants using current effective **Speed** and the established tie rules.
3. That normal turn order remains fixed for the rest of the round. Speed changes during the round affect later round ordering unless an individual authored effect explicitly says otherwise.
4. When a player-controlled character's turn arrives, the player selects that character's legal action and target/content using the **current battle state at that turn**.
5. When an enemy/entity turn arrives, its AI selects one legal action using the **current legitimate battle state at that turn**. It may not inspect future player choices that have not yet been made.
6. The selected action resolves immediately, including its complete cost / action / reaction / state-change package, before the next normal combatant's turn begins.
7. **Item** and **Defend** are normal selected commands on the acting character's Speed-ordered turn. They do not receive separate universal start-of-round priority phases.
8. Party members win exact Speed ties against enemies.
9. Tied party members resolve in player-selected order.
10. Tied enemies/entities use a stable deterministic order.
11. After every eligible combatant has completed or lost its normal turn for that round, resolve end-of-round processing and begin the next round.

There is no normal full-party command queue and no universal **Confirm Round** step.

## Speed rule

Speed controls ordering only.

Speed does **not**:
- grant additional ordinary actions;
- create ATB-style extra turns;
- create a universal initiative gauge;
- allow a character to act twice merely for being much faster.

A faster combatant normally acts before a slower combatant, but both still receive at most one ordinary turn in that normal round unless an individual authored mechanic explicitly says otherwise.

Because normal initiative is fixed at the beginning of the round:
- a Speed increase or reduction applied after initiative is established does **not** reshuffle the current round;
- that Speed change still applies immediately to any other authored effect that directly reads current Speed;
- if the Speed change remains active at the next beginning-of-round initiative check, it affects that next round's ordering normally.

## Turn-entry decision rule

Ordinary player decisions are made when the relevant character's turn actually arrives.

Therefore:
- the player may react to actions and state changes that occurred earlier in the same round;
- a character is not committed at round start to an Ability, Card, Item, Defend, or target;
- enemy decisions likewise use the legitimate state that exists when that enemy's turn arrives;
- no actor may use knowledge of future unselected player commands.

## Round-based duration timing

Unless an owning current rule explicitly defines another clock, an effect written as lasting a number of **rounds** follows this default:

1. The effect becomes active immediately when its application resolves.
2. If applied during normal turn resolution, the **application round counts as the first duration round**.
3. Its first ordinary duration checkpoint is that same round's end-of-round processing.
4. A round-based Field uses the same default timing unless its owning rule explicitly says otherwise.
5. An effect created during end-of-round processing does not immediately consume a duration checkpoint at the same boundary; its first counted round is the next round.

Explicit wording such as **through the end of the following round** remains literal and overrides the generic numbered-round shorthand.

No effect is retroactive. If a round-based effect is applied after an actor has already completed its normal turn, it cannot change or undo that completed turn.

## Turn-based duration timing

An effect written in **affected turns** uses the affected unit's own turn opportunities rather than the global round counter.

- If the effect is active when that unit's normal turn arrives, that is an affected turn unless the owning effect says otherwise.
- If the effect is applied after that unit already completed its turn, the completed turn is not retroactively counted or altered.
- Losing a turn to a legal status still completes that turn opportunity for turn-counting purposes unless the owning status explicitly defines another rule.

Status-specific behavior remains owned by `STATUS_EFFECTS.md`.

## Prepared and delayed actions

The removal of the normal round command queue does **not** remove explicitly authored Preparation/delayed-action mechanics.

An explicitly authored Preparation may:
- consume the actor's current selected action;
- establish a named pending follow-up action;
- require or lock that follow-up on a later eligible turn;
- expose a response window before the follow-up resolves.

Such a pending Prepared action is **not** a restored full-party/enemy command queue. Ordinary actions still select and resolve immediately on their own turns.

If an owning action/encounter explicitly marks a pending Prepared action as **Interruptible**, a legal interrupt may interact with it according to that authored interrupt rule while it is pending. Merely being prepared or telegraphed does not automatically make an action Interruptible.

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
