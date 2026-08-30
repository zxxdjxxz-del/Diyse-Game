# Diyse — Standard Card UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Standard Card loadout
Each permanent character:
> **3 Standard Card slots**

Cards are:
- reusable;
- selected actions;
- MP-consuming;
- not charge-based.

## No deck UI
Do not implement:
- draw pile;
- hand;
- discard;
- shuffle;
- deck size;
- duplicate rank;
- card XP;
- card fusion.

## Current Card display
A Card screen should be able to communicate:
- name;
- Face;
- MP cost;
- target;
- formula/type where relevant;
- Power/Base Hit where relevant;
- effect/status rider;
- equipped character/slot.

Exact sorting/filter UI:
> OPEN.

## Battle Card command
`Card` is the permanent command.

The content selection under that command must be able to distinguish:
- equipped Standard Cards;
- legal equipped Primes.

Do not create a separate universal Summon command merely to present Primes.
