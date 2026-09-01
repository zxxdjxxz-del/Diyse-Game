# Diyse — Enemy Reward Handoff

**Status:** CURRENT AUREN / DROP HANDOFF AUTHORITY

## Ownership
`09_ENEMIES_AND_ENCOUNTERS` owns:
- enemy identity;
- level/stat body;
- encounter formation;
- combat kit;
- lethal/nonlethal/protected encounter architecture.

`10_PROGRESSION_AND_EXP` owns:
- Player EXP;
- CEXP;
- diminishing-return behavior where applicable.

`12_ECONOMY_AND_REWARDS` owns:
- Auren payout tuning;
- economic reward density;
- non-EXP reward balancing.

`08_ITEMS_AND_EQUIPMENT` owns:
- exact item identity/effect;
- authored equipment/material source identity.

## Formation/event-level Auren rule
Auren is attached to the resolved **formation or authored event**, not to every individual enemy body.

Therefore:
- an authored special enemy inserted into an ordinary formation uses that formation's single Auren payout;
- support/summoned/generated bodies add **0 extra Auren**;
- a named enemy body does not create a second bounty simply because it has its own combat file;
- scripted encounter wrappers may explicitly set a different payout, including 0.

This prevents body-count exploitation and duplicate rewards.

## Current fixed authored non-boss encounters
### Chapter 0 authored combat
All Chapter-0 authored combat encounters award:
> **0 Auren**

Chapter 0 is a level-static/tutorial-disaster sequence and does not establish an early farming or looting economy.

This includes the final Broken Convoy confrontation in S005.

### Chapter 2 — Hold the Junction / S016
Direct Auren:
> **0**

Reason:
- mandatory extraction rearguard;
- battle ends directly back into the extraction sequence;
- its exact authored progression reward is already handled separately;
- no additional per-body bounty is added.

### Chapter 3 — S018 Lawful Authority Confrontation I
**Ivory Watch Detail** direct Auren:
> **0**

This is a nonlethal lawful-authority confrontation. No personal loot or per-officer bounty is awarded.

### Chapter 3 — S018 Lawful Authority Confrontation II
**Ivory Adjudicator Sereth** direct Auren:
> **0**

This is a protected-threshold nonlethal confrontation and does not award a personal bounty.

## Character Quest authored bosses
Character Quest boss/climax encounters award:
> **0 separate direct Auren**

because their Auren is already contained in the Character Quest completion package.

Owning economy detail:
`CHARACTER_QUEST_REWARD_BOUNDARY.md`

## Story-placement-dependent authored encounters
Do **not** assign exact Auren yet to identities whose exact mandatory/nonlethal/story role is still explicitly unresolved.

Current deferred examples include:
- False-Warrant Adept;
- Highland Resistance Fighter;
- Weather Crown Shield Guard;
- Blood Husk;
- Perfected Soldier;
- Beast Handler + Bound Rift Hound;
- Resistance Saboteur;
- Controlled Prisoner;
- Command-Seal Warden;
- Crown Engine Technician;
- Compelled Relay Bearer.

Their exact reward status must be resolved only after the owning story/dialogue placement is line-complete.

Lord-Marshal Kharvek is already handled as the Chapter-12 optional Elite economy and must not receive a second authored-encounter Auren line.

## Drop firewall
Do not assume a universal random-drop table.

Ordinary encounters may use occasional explicitly authored Consumable drops if separately approved, but no global probability table is created here.

Do not introduce by default:
- low-percentage weapon farming;
- low-percentage armor farming;
- sell-only junk;
- generic monster-part crafting economy.

Permanent equipment that advances progression should be reliably authored rather than dependent on repeated RNG farming.
