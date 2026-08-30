# Diyse — Battle Flow UI States
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `68b66e129fa7e34dac69501786d00a1023ad0fd4`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


Production combat UI must support these logical states even if the final layout differs:

## Round start / turn order
- beginning-of-round effects and state checks resolve;
- the normal round's actor order is established from current effective Speed and tie rules;
- the UI must be able to communicate which combatant is currently acting;
- an ATB gauge is not required or implied.

## Player-character turn
When a player-controlled character's turn arrives:
- that acting character is highlighted clearly;
- the normal command list is available;
- the player selects command, content, and legal target as applicable;
- only that acting character's decision is being made;
- once confirmed, that action resolves before the next normal actor's turn.

There is no production requirement to queue the whole party before resolution and no universal **Confirm Round** button.

## Enemy/entity turn
When an enemy/entity turn arrives:
- player command selection is inactive for that normal turn;
- enemy AI chooses from the legitimate current battle state;
- its action and resulting reactions/state changes resolve before the next normal turn begins.

## In-turn resolution
- the current actor's selected action package resolves completely;
- animations, reactions, damage/healing, costs, statuses, and resulting state changes are presented before advancing to the next normal actor;
- later player characters may therefore make decisions using the state created by earlier turns in the same round.

## Round complete
After all eligible normal actors have completed or lost their turns:
- end-of-round processing resolves;
- status changes remain readable;
- the next round begins and a new Speed-based order is established.

## Prime invocation / Prime control
- Prime invocation occurs as a selected Card/Prime action on the acting character's turn;
- Recovered and Awakened states behave differently;
- Awakened Prime suspends the ordinary party and enters direct-control Prime rounds;
- the established Prime restoration and two-full-normal-round spacing rules remain owned by `07_CARDS`.

## Victory / defeat / authored nonlethal
The UI must support:
- ordinary victory;
- defeat;
- authored nonlethal resolution;
- fresh-form continuation without premature reward payout.

## Reward timing
Same-bar phase changes:
- no separate first-clear payout.

Fresh-form boss:
- combined reward after final form unless separately authored.

Exact reward-panel animation/presentation:
> OPEN PRODUCTION UX.
