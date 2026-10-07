# Diyse — Battle Flow UI States

**Status:** ACTIVE UI / IMPLEMENTATION SPEC  
**Authority:** gameplay behavior defers to `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`.  

Production combat UI must support the current ordered **TURN / EXECUTION** timeline.

## Timeline

The battle UI must clearly distinguish:

- **TURN** markers — command opportunities;
- **EXECUTION** markers — queued actions waiting to resolve.

When a player TURN is active, time pauses for command selection.

Before confirmation, the UI should show the selected action's projected EXECUTION position and the acting character's projected next TURN.

## Player TURN

When a player-controlled character's TURN arrives:

- highlight that character clearly;
- expose the legal command list;
- allow command/content/target selection;
- allow voluntary Swap with a conscious reserve;
- if the selected action is Immediate, resolve it now;
- otherwise create its future EXECUTION marker;
- schedule the user's next TURN under the current Return/Speed rules.

A character with one of its own actions still pending cannot receive another command TURN before that EXECUTION resolves.

## Enemy TURN / intent

Enemy TURNs use the same timeline language.

Queued enemy actions normally expose readable intent, target/group where not intentionally concealed, Execution category, and current Delay/Interrupt eligibility.

## Interactive marker inspection

Queued EXECUTION inspection should expose at minimum:

- actor;
- action name/intent where not concealed;
- target/group where not concealed;
- Execution category;
- current Interruptible / Delay-only / Uninterruptible state;
- whether standard Delay applications remain;
- visible timing/special conditions.

TURN inspection may expose projected TURN, Quick/Slow, Delay eligibility, and remaining Delay applications.

Inspection costs no TURN/time. Legal Delay/Interrupt targets should be directly selectable when choosing those effects.

## Resolution

An authored action resolves through its complete hit/effect sequence before automatic reactions and before battle outcome is checked. Emergency KO replacement is never inserted into the middle of a multi-hit or mixed-effect sequence.

## Reserves

The visible party supports **4 active + 2 reserve** permanents.

Reserve characters have hidden personal TURN cycles for status/timer processing. Voluntary Swap and KO emergency replacement use different timing rules as defined by the battle master.

## Prime

Prime manifestation uses the stable Prime foundation, but exact Recovered/Awakened manifestation timeline presentation is **parked** until the dedicated Prime sequencing pass. Do not hard-code the former Prime-round UI.

## Battle end

The UI must support:

- Victory;
- Defeat;
- Mutual KO resolving to Defeat by default;
- successful Escape;
- authored nonlethal/story outcomes;
- multi-form continuation without premature reward payout.
