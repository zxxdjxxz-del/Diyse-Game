# Diyse — Card / Prime Balance Verification
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


## Standard Cards
- 24 identities
- 3 equipped per character
- MP-consuming
- reusable
- no charges/deck/draw/discard.

Test:
- exact current MP cost;
- legal target;
- Base Hit;
- formula;
- status rider;
- no accidental duplicate/deck subsystem.

## Primes
- 12 identities
- 6 Story + 6 Major Hunt
- Story: Recovered → Awakened
- Major Hunt: acquired Awakened
- 2 Prime slots per character after Sixfold Volition.

Invocation costs:
- Recovered Story 50 MP
- Awakened Story 80 MP
- Major Hunt 90 MP
- Prime commands 0 additional MP.

## Recovered
Test:
- invocation consumes one selected ordinary action;
- exactly one signature action;
- dismissal in the same ordinary round;
- no three-round Recovered direct-control state.

## Awakened
Test:
- party suspended;
- Prime directly controlled for 3 Prime rounds;
- one Prime command per Prime round;
- party cannot act/be targeted during manifestation;
- normal party resumes after dismissal.

## Availability/cooldown
Test:
- each Prime identity once per battle per genuine fresh body;
- after normal dismissal, 3 full normal party rounds before another unused equipped Prime;
- fresh-body transition refreshes Prime availability;
- same-bar state does not.

## Access
Story bearer association must not owner-lock current battle use.
