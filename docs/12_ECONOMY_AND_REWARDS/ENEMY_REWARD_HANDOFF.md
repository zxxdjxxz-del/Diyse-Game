# Diyse — Enemy Reward Handoff

**Status:** CURRENT G / DROP HANDOFF AUTHORITY

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
- G payout tuning;
- economic reward density;
- non-EXP reward balancing.

`08_ITEMS_AND_EQUIPMENT` owns:
- exact item identity/effect;
- authored equipment/material source identity.

## Formation/event-level G rule
G is attached to the resolved **formation or authored event**, not to every individual enemy body.

Therefore:
- an authored special enemy inserted into an ordinary formation uses that formation's single G payout;
- support/summoned/generated bodies add **0 extra G** unless explicitly authored;
- a named enemy body does not create a second bounty simply because it has its own combat file;
- scripted encounter wrappers may explicitly set a different payout.

This prevents body-count exploitation and duplicate rewards.

## Protected / nonlethal rule — CURRENT
Protected, restrained, stabilized, captured, withdrawn, or otherwise nonlethal resolved encounters may award G.

Do **not** use:
> `nonlethal = 0 G`

as a default rule.

The reward can represent mission credit, secured resources, institutional compensation, bounty/requisition value, or another event-level handoff rather than loot from a killed body.

The old fixed zero-G assumptions for Chapter 0, Hold the Junction, S018 lawful-authority confrontations, and Character Quest bosses are therefore retired pending the active payout recalibration.

## Story-placement-dependent authored encounters
Do not assign exact G yet to identities whose exact mandatory/nonlethal/story role is still explicitly unresolved.

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

Lord-Marshal Kharvek is already handled as the Chapter-12 optional Elite economy and must not receive a second authored-encounter G line.

## Random-drop rule — CLOSED
Ordinary enemies and ordinary formations have:
> **no random Consumable drop table**

There are no low-percentage normal-enemy drops for:
- Consumables;
- weapons;
- armor;
- Forge Components;
- Relics;
- vendor-trash/junk.

Consumables enter the economy through:
- normal unlimited shop stock once unlocked;
- limited premium one-copy-per-shop stock;
- authored chests/caches;
- story field issue;
- quest completion packages;
- other explicitly authored guaranteed rewards.

### Authored exception boundary
A specific named encounter may still receive a **guaranteed authored item reward** if separately approved.
That is not a random drop table and must be written explicitly into the encounter/reward source architecture.

## Permanent-reward firewall
Do not introduce by default:
- low-percentage weapon farming;
- low-percentage armor farming;
- sell-only junk;
- generic monster-part crafting economy.

Permanent equipment that advances progression should be reliably authored rather than dependent on repeated RNG farming.
