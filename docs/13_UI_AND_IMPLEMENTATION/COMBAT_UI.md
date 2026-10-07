# Diyse — Combat UI

**Status:** ACTIVE UI / IMPLEMENTATION SPEC  
**Authority:** gameplay behavior defers to `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`.  

## Permanent commands

Exactly:

**Attack / Abilities / Cards / Item / Defend / Swap**

Prime manifestation is handled through its own special access path and is not assumed to be a universal always-visible command.

## Timeline presentation

Diyse uses an ordered TURN / EXECUTION timeline rather than discrete rounds.

The UI must make clear:

- whose TURN is active;
- visible future TURN markers;
- visible queued EXECUTION markers;
- projected EXECUTION and next-TURN position before command confirmation;
- current Quick/Slow where relevant;
- Delay/Interrupt eligibility and remaining standard Delay applications where relevant.

If a TURN and EXECUTION share the same exact timeline position, the EXECUTION resolves first under global authority.

## Party display

Must support:

- **4 active permanent party members**;
- **2 reserves**;
- HP;
- MP;
- current statuses/buffs/debuffs;
- conscious/KO state;
- Defend/Ward state where relevant;
- equipped Card/Prime access surfaces as required;
- clear active-TURN ownership.

Reserve characters are normally off-field for targeting, but remain part of battle continuation and hidden timing.

## Status naming

Current player-facing names include:

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

- multiple active enemies up to the current encounter cap;
- targetability;
- KO/dead state;
- boss/form identity;
- queued action intent where not intentionally concealed;
- target/group intent where not intentionally concealed;
- current Interruptible / Delay-only / Uninterruptible eligibility.

## Targeting

A queued single-enemy action whose original target becomes invalid automatically retargets the next valid enemy in stable encounter order. The UI should not ask for a second target confirmation in that case.

Ally-targeting/non-enemy actions do not auto-retarget unless their owning action explicitly says they do.

## No obsolete meters/surfaces

Do not display or implement as universal systems:

- ATB gauge;
- whole-party Confirm Round flow;
- Break/Stagger gauge;
- Accuracy/Evasion meter;
- Status Resistance meter;
- hidden weapon-power value;
- default character-specific resource gauges;
- former round-based Prime cooldown counter.
