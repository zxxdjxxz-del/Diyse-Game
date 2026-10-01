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

## Protected / nonlethal rule — LOCKED
Protected, restrained, stabilized, captured, withdrawn, or otherwise nonlethal resolved encounters may award G.

Do **not** use:
> `nonlethal = 0 G`

as a default rule.

The reward can represent mission credit, secured resources, institutional compensation, bounty/requisition value, or another event-level handoff rather than loot from a killed body.

## Exact fixed authored non-boss payouts
### Chapter 0 authored combat
Chapter 0 remains level-static.

The prior six-row payout mapping is superseded because the current encounter order now contains:
1. B01 Black Host Raider + Black Host Crossbowman;
2. B01 Black Host Raider + Black Host Shieldbearer;
3. B01 2 War Hounds;
4. B02 Black Host Crossbowman + War Hound;
5. B02 1 War Hound;
6. B05 Ruin Vanguard Pursuer protected disengagement;
7. B06 Riftmaw + Battle Sorcerer combined final boss.

The previous Chapter-0 authored-combat envelope:
> **1,700 G**

is **retained provisionally as the chapter-level envelope**, so current mandatory-route G totals are not silently changed by encounter restructuring.

However:
> **the exact per-encounter split is REOPENED**

Do not use the old Handler / standalone Riftmaw / standalone War-Sorcerer payout rows as current encounter payouts.

The Pursuer remains an authored protected resolution rather than a separate strong-normal/optional bounty source. The combined P06 encounter must receive one authored encounter-level payout, not separate body bounties.

### Retired authored-event payout rows

The former **Hold the Junction / S016** payout and both Chapter-3 **S018 lawful-authority confrontation** payouts are retired with those encounter branches.

Do not award:
- former Hold the Junction — 1,000 G;
- former S018 lawful-authority confrontation I — 1,200 G;
- former S018 lawful-authority confrontation II — 1,400 G.

The previous **5,300 G** fixed-authored-event subtotal is therefore historical only. The only retained numeric envelope in this section is the **provisional Chapter-0 1,700 G chapter-level envelope**; exact current fixed-event G outside that envelope remains open pending the economy rebuild.

## Character Quest authored bosses
Character Quest bosses still award:
> **0 separate direct G**

because their economic payout is already contained in the Character Quest completion package. This is an anti-double-count rule, **not** a protected/nonlethal penalty.

Owning economy detail:
`CHARACTER_QUEST_REWARD_BOUNDARY.md`

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

Lord-Marshal Kharvek is now a strong normal-pool Chapter-12 identity. Do not create a second authored-event G line unless its final normal-pool placement explicitly requires one; ordinary formation-level G remains the default.

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
