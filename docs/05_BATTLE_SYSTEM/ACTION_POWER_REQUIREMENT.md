# Diyse — Action Potency Requirement

**Status:** ACTIVE IMPLEMENTATION REQUIREMENT  
**Authority:** `BATTLE_SYSTEM_MASTER.md` §8

Every action that deals ordinary scalable direct HP damage must define an explicit numeric **Potency**.

Qualitative labels such as light, strong, heavy, very heavy, or powerful may describe role but never replace the numeric value.

## Required formats

- single hit: exact Potency
- multi-hit: exact per-hit Potency, with exact total where useful
- reaction/counter: triggered scalable direct damage defines its own Potency
- summoned/autonomous attack: every scalable direct-damage action defines Potency
- copied/echoed scalable damage: conversion rule must be explicit and bounded

Fixed/percentage damage states its fixed/percentage rule instead of fake Potency.

Non-damaging support/healing/revival/information/field/stance actions use Potency only where their owning formula actually scales from Potency.

## Universal Attack

**Potency 1.00 / Physical / Neutral**

## Closure gate

A combat kit cannot be numerically certified while a scalable direct-damage action lacks Potency or another explicit current damage rule.

Future boss/encounter certification should validate HP/duration, offense, action Potencies/fixed rules, statuses/riders, timeline interaction, and form/state behavior against the current TURN / EXECUTION system.
