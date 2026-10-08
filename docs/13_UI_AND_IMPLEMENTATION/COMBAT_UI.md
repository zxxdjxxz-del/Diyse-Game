# Diyse — Combat UI

**Status:** ACTIVE UI / IMPLEMENTATION SPEC  
**Authority:** gameplay behavior defers to `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md` and Prime behavior to `../07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md`.

## Universal command surface

Exactly:

> **Attack / Abilities / Cards / Item / Defend / Swap**

Prime Invocation is a separate special access path and appears only when legal.

## Timeline presentation

Diyse uses an ordered **TURN / EXECUTION** timeline.

The UI must make clear:

- whose TURN is active;
- visible future TURN markers;
- visible queued EXECUTION markers;
- projected EXECUTION and next-TURN position before command confirmation where knowable;
- current Quick/Slow where relevant;
- current Delay/Interrupt eligibility;
- remaining standard Delay applications where relevant.

If a TURN and EXECUTION share the same exact timeline position, EXECUTION resolves first.

## Party display

Must support:

- **4 active permanent party members**;
- **2 reserves**;
- HP;
- MP;
- current statuses/buffs/debuffs;
- conscious/KO state;
- Defend/Ward state where relevant;
- equipped Standard Card / Prime access;
- clear active-TURN ownership.

Reserve characters are normally off-field for hostile targeting while remaining part of battle continuation and hidden personal timing.

## Current status naming

- Quick
- Slow
- Stuck
- Asleep
- Poison
- Wounded
- Sealed
- Ward
- Regen
- Doomed
- Strength / Magic / Intelligence / Defense / Spirit Up or Down

## Enemy display

Must support:

- multiple active enemies up to the encounter cap;
- targetability;
- KO/dead state;
- boss/form identity;
- queued action intent where not intentionally concealed;
- target/group intent where not intentionally concealed;
- current Interruptible / Delay-only / Uninterruptible eligibility.

## Targeting presentation

A queued single-enemy action whose original target becomes invalid automatically retargets the next valid enemy in stable encounter order. The UI should not request a second target confirmation.

Ally-targeting and other non-enemy actions do not auto-retarget unless their owning action explicitly says otherwise.

## Prime presentation

Awakened manifestation must display:

- 3-segment Manifestation Meter;
- Basic / Medium / Heavy meter cost;
- current remaining meter;
- Final Return state after meter reaches 0;
- automatic Dismissal on the Prime's already-scheduled next TURN;
- Ready/Spent identity state;
- post-Prime lockout owner and personal TURN count remaining.

Detailed Prime UI is owned by `PRIME_UI.md`.
