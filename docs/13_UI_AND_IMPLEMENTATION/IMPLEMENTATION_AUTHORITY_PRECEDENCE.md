# Diyse — Implementation Authority Precedence
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in the reorganized domains.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


When implementation-facing sources disagree:

1. newest explicit user correction;
2. current reorganized domain authority;
3. newest compatible master-canon audit;
4. current operational chapter/system file;
5. proof runtime;
6. historical audit/prototype source.

## Critical current override: Mastery
Older proof/runtime or superseded documentation may still contain an 8-point Mastery schedule.

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
Proof state may retain the technical identifier `gold` until version-safe migration work replaces or safely maps it.

Current player-facing game currency:
> **G**

Retired player-facing currency name:
> **Auren**

Any production persistence/UI migration must map proof currency state to current **G** authority. Do not expose `gold` as the final player-facing label and do not restore Auren as a second or replacement ordinary currency.

## Critical current override: final chapter IDs
Production ID conventions must support:
> `chapter_00` through `chapter_13`

Older authoring docs stopping at `chapter_12` are stale after the Chapter-10 insertion.
