# Diyse — Combat SFX Requirements
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in current reorganized domains.  
**Music supersession authority:** later Complete Master Canon explicitly marks **ALL whole-project music OPEN / under separate redevelopment** and supersedes the older v1.53–v1.57 regional-music prescriptions as active canon.  
**Research preservation:** older approved/researched music material remains valuable development evidence but is **not automatically current soundtrack canon** unless explicitly promoted.  
**Runtime checkpoint:** `3fd07e92eda04f31ba613a654b3b1b28071f44e6`; no production music/SFX/audio asset library is present in the inspected Godot repository.


The sound system must distinguish at minimum:

## Core actions
- Attack
- Ability
- Card
- Item
- Defend

## Result states
- hit
- miss
- critical hit
- KO
- recovery/healing
- MP/resource payment feedback if represented sonically
- victory
- defeat
- authored nonlethal resolution

## Elements
Exactly:
- Fire
- Ice
- Lightning
- Earth

Do not build standard combat-element SFX categories for Wind or Water.

## Harmful statuses
Need readable application/active/clear feedback for:
- Burn
- Freeze
- Stun
- Staggered
- Bleed

## Ruin
Ruin requires a distinct sonic family from the four standard elements.

It is not a fifth element in an element wheel.

## Boss structure
Audio must support:
- same-bar escalation without fake victory;
- fresh-form transition;
- support-object destruction;
- final-form victory only at actual encounter completion.

## Retargeting
Automatic hostile retarget should resolve cleanly without a confusing second player-selection sound.
