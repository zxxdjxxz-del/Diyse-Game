# Diyse — Audio State / Transition Requirements

**Status:** ACTIVE AUDIO IMPLEMENTATION REQUIREMENTS  
**Parent authority:** `../AUDIO_AUTHORITY_MASTER.md`

A future runtime audio controller must respect gameplay/story state.

## Required transitions
Potential transitions include:
- field → battle;
- battle → field;
- field → dialogue/cutscene;
- normal boss phase → same-bar escalation;
- fresh boss form;
- Prime invocation;
- Prime dismissal;
- victory;
- defeat;
- hub state changes;
- chapter/area transition;
- point-of-no-return warning;
- final continuous sequence.

## Rule
Audio state must not accidentally:
- fire victory music between fresh forms;
- reset a boss cue on every same-bar state change unless authored;
- overlap two area tracks indefinitely after scene transition;
- restart long cues on every minor room change unless designed to.

## Dialogue
Music may:
- continue;
- duck;
- transition;
- stop

depending on authored scene needs.

No universal rule is currently locked.
