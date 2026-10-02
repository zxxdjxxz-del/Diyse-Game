# Diyse — Implementation Authority Precedence

**Status:** ACTIVE IMPLEMENTATION PRECEDENCE  
**Cross-domain rule:** current gameplay/content owner domains outrank proof code and historical implementation notes.

When implementation-facing sources disagree:

1. newest explicit user correction;
2. current owning repository domain authority;
3. current operational chapter/system or cross-domain handoff file;
4. current implementation-status/divergence documentation where it does not conflict with owning gameplay authority;
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
Current runtime and schema-v1 save state use `rewards.g`. Legacy schema-v1 `rewards.gold` values are accepted on load and normalize to `rewards.g`; preserve this compatibility when extending production persistence.

Current player-facing game currency:
> **G**

Retired player-facing currency name:
> **Auren**

Production persistence/UI extensions must retain the current **G** storage/presentation contract and legacy-save normalization. Currency-key migration is complete; detailed economy calibration remains open. Do not expose `gold` as the final player-facing label and do not restore Auren as a second or replacement ordinary currency.

## Critical current override: final chapter IDs
Production ID conventions must support:
> `chapter_00` through `chapter_13`

Older authoring docs stopping at `chapter_12` are stale after the Chapter-10 insertion.
