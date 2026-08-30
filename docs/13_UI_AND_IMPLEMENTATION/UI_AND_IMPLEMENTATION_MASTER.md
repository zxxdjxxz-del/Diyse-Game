# Diyse — UI & Implementation Master
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Production target
- Godot
- Android/APK first-class target
- HD-2D
- landscape
- reference composition: **1920×1080 / 16:9**
- wider Android displays reveal additional horizontal scenery instead of stretching critical composition
- rendering baseline currently uses Godot GL Compatibility
- UI scales through `canvas_items` in the proof project

## Core UI priorities
1. readable on Android landscape;
2. fast command entry;
3. current system truth visible without obsolete gauges;
4. stable data-driven content rather than hardcoded story/item text in generic UI code;
5. clear current-facing names even where legacy technical IDs remain;
6. no player-dialogue-choice architecture;
7. no hidden second system introduced for presentation convenience.

## Permanent battle commands
Exactly:
> **Attack / Ability / Card / Item / Defend**

The UI must not add:
- Brace;
- Break;
- Limit;
- Rune;
- Summon as a separate universal command;
- a sixth resource-specific command.

Prime invocation is accessed through the current Card/Prime loadout architecture, not by inventing another permanent command.

## Core menu domains that must be representable
- party / formation
- character status
- class / selected class / Class Level / CEXP
- Masteries
- Abilities
- equipment
- Standard Cards
- Prime Cards
- inventory / materials
- quests / Hunts
- world map / travel
- shops / Quartermaster / services
- save/load/options

Exact final menu hierarchy remains an **OPEN PRODUCTION UX** decision.

## System-display firewall
Current-facing UI must use:
- Spirit
- Evasion
- Status Resistance
- Acuity
- Last Cartographer
- Sixfold Volition
- Auren
- Weapon / Secondary / Armor
- Locked / Unlocked Masteries

It must not display:
- Accuracy as a natural character stat;
- MDEF as the primary current label;
- Resource Face;
- Last Measure;
- Mastery Points;
- Synthesis;
- Accessory slot;
- Barrier meter;
- Brace;
- Break/Stagger gauge.
