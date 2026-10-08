# Diyse — Action Potency Requirement

**Status:** ACTIVE IMPLEMENTATION REQUIREMENT  
**Authority:** `BATTLE_SYSTEM_MASTER.md` §8

Every action that deals ordinary scalable direct HP damage must define an explicit numeric **Potency**.

Required authoring:
- single hit: exact Potency;
- multi-hit: exact per-hit Potency, with total where useful;
- reaction/counter: its own Potency when scalable;
- summoned/autonomous scalable attack: exact Potency;
- copied/echoed scalable damage: explicit bounded conversion rule.

Fixed/percentage damage states its own fixed/percentage rule instead.

Universal Attack:
> **Potency 1.00 / Physical / Neutral**

A combat kit cannot be numerically certified while a scalable direct-damage action lacks Potency or another explicit current damage rule.
