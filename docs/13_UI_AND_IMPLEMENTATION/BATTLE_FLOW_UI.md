# Diyse — Battle Flow UI States
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


Production combat UI must support these logical states even if the final layout differs:

## Normal round selection
- current acting character highlighted;
- command choice;
- target/content selection;
- previously queued actions reviewable enough to avoid accidental confirmation;
- Confirm Round enabled only when all conscious party actions are selected.

## Normal resolution
- command selection locked;
- animations/log/result presentation resolve in canonical order;
- no mid-resolution player reprogramming of queued ordinary actions.

## Round complete
- status changes readable;
- next-round transition.

## Prime invocation / Prime control
- Prime invocation occurs as a selected Card/Prime action;
- Recovered and Awakened states behave differently;
- Awakened Prime suspends ordinary party and enters direct-control Prime rounds.

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
