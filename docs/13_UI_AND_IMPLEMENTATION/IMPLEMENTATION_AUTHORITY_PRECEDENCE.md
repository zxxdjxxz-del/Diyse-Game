# Diyse — Implementation Authority Precedence
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


When implementation-facing sources disagree:

1. newest explicit user correction;
2. current reorganized domain authority;
3. newest compatible master-canon audit;
4. current operational chapter/system file;
5. proof runtime;
6. historical audit/prototype source.

## Critical current override: Mastery
The existing repository documentation still says:
> exactly 8 automatic Mastery Points

That is stale under the newer v85 working authority.

Current implementation requirement:
> **Mastery Points do not exist.**

Masteries unlock automatically by Class Level.

Do not implement:
- point currency;
- point counter;
- spend button;
- banked points;
- respec/refund;
- replacement talent currency.

## Critical current override: Story Prime access
Old proof runtime is bearer-locked around `first_champion`.

Current production requirement:
- Story bearer is narrative association;
- after acquisition, any active permanent character may equip an acquired Prime in a legal Prime slot;
- after Sixfold Volition, each permanent character has **2 Prime slots**.

## Critical current override: currency
Proof state uses `gold`.
Current game currency:
> **Auren**

Any production persistence/UI migration must map to current Auren authority rather than exposing `gold` as the final player-facing currency.

## Critical current override: final chapter IDs
Production ID conventions must support:
> `chapter_00` through `chapter_13`

Older authoring docs stopping at `chapter_12` are stale after the Chapter-10 insertion.
