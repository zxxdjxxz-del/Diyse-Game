# Diyse — Implementation Authority Precedence

**Status:** ACTIVE IMPLEMENTATION PRECEDENCE

When implementation-facing sources disagree:

1. newest explicit user correction;
2. current owning repository domain authority;
3. current operational chapter/system or cross-domain handoff file;
4. current implementation-status/divergence documentation where it does not conflict with owning gameplay authority;
5. proof runtime as implementation evidence only.

## Mastery implementation requirement

> **Mastery Points do not exist.**

Masteries unlock automatically by Class Level.

Production implementation must not add:
- point currency;
- point counter;
- spend button;
- banked points;
- respec/refund;
- replacement talent currency.

## Story Prime access

Current production requirement:
- Story bearer is narrative association;
- after acquisition, any active permanent character may equip an acquired Prime in a legal Prime slot;
- from Chapter-4 Prime-loadout access until Sixfold Volition, each permanent character has **1 Prime slot**;
- after Sixfold Volition, each permanent character has **2 Prime slots**.

## Currency

Current runtime and supported schema-v1 save compatibility normalize incoming `rewards.gold` values to `rewards.g`.

Current player-facing game currency:
> **G**

Production persistence/UI extensions must retain the current **G** storage/presentation contract and supported save normalization. Detailed economy calibration remains open.

## Final chapter IDs

Production ID conventions must support:
> `chapter_00` through `chapter_13`
