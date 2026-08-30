# Diyse — Audio State / Transition Requirements
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in current reorganized domains.  
**Music supersession authority:** later Complete Master Canon explicitly marks **ALL whole-project music OPEN / under separate redevelopment** and supersedes the older v1.53–v1.57 regional-music prescriptions as active canon.  
**Research preservation:** older approved/researched music material remains valuable development evidence but is **not automatically current soundtrack canon** unless explicitly promoted.  
**Runtime checkpoint:** `3fd07e92eda04f31ba613a654b3b1b28071f44e6`; no production music/SFX/audio asset library is present in the inspected Godot repository.


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
