# 03_DIALOGUE

**Status:** CURRENT DIALOGUE AUTHORING / RUNTIME AUTHORITY  
**Updated:** 2026-09-26

This folder is the canonical home for spoken-dialogue production, Dialogue Engine authority, scene-authoring controls, and current dialogue-runtime synchronization.

## Authority boundary

Dialogue does not own story structure or mechanics.

- Story / required outcomes / reveal timing: `02_STORY`
- Character canon: `01_CHARACTERS`
- Combat: `05_BATTLE_SYSTEM`
- Cards / Primes: `07_CARDS`
- Enemies / encounter placement: `09_ENEMIES_AND_ENCOUNTERS`
- Progression: `10_PROGRESSION_AND_EXP`
- Traversal / UI implementation: `13_UI_AND_IMPLEMENTATION`

Exact accepted spoken wording lives in current production atomics under:

> `PRODUCTION/CHAPTER_##/`

## Rehearsal-first authoring rule

Current production uses:

> **scene/world state → independent Person-Agent rehearsal → Dialogue Editor → mature-adult speech audit → invisible Canon/Knowledge Checker → economical HD-2D staging → author approval**

Primary rules:
- `AGENT_SYSTEM/REHEARSAL_FIRST_AUTHORING_LOCK.md`
- `AGENT_SYSTEM/NATURAL_TURN_LENGTH_AND_FLOOR_HOLDING_LOCK.md`
- `AGENT_SYSTEM/MATURE_ADULT_SPEECH_AND_PROFANITY_LOCK.md`
- `AGENT_SYSTEM/SPOKEN_DIALOGUE_VS_NARRATION_LOCK.md`
- `AGENT_SYSTEM/README.md`
- `AGENT_SYSTEM/RUNTIME_ORCHESTRATION.md`

Hard timing rule:

> **No spoken dialogue during player-controlled traversal or active combat.**

Route dialogue requires an authored stop. Battle dialogue belongs before combat begins or after combat has fully ended.

## Current production status

| Chapter | Current dialogue status |
|---|---|
| Ch0 | **CURRENT EXACT** — B01–B07 + C01 |
| Ch1 | **CURRENT EXACT / LOCKED** — B01–B12 + C02/C03/C04 |
| Ch2 | **CURRENT EXACT** — B01–B15 + C05 |
| Ch3 | **CURRENT EXACT** — B01–B15 + C06/C07 |
| Ch4 | **PRE-DIALOGUE** — B01–B12 scene-authority specs complete; B01 rehearsal target present; no approved exact dialogue |
| Ch5–13 | pending according to owning story authority |

Current Character-Life sequence through Chapter 3:

> **C01 → C02 → C03 → C04 → C05 → C06 → C07**

## Current synchronized Chapters 0–3 artifacts

Standalone production atomics remain exact wording authority.

Stable derived manuscripts:
- `PRODUCTION/CHAPTER_00/CHAPTER_00_DIALOGUE_MANUSCRIPT.md`
- `PRODUCTION/CHAPTER_01/CHAPTER_01_DIALOGUE_MANUSCRIPT.md`
- `PRODUCTION/CHAPTER_02/CHAPTER_02_DIALOGUE_MANUSCRIPT.md`
- `PRODUCTION/CHAPTER_03/CHAPTER_03_DIALOGUE_MANUSCRIPT.md`

Cross-chapter sync metadata:
- `PRODUCTION/CHAPTERS_00_03_DIALOGUE_SYNC_MANIFEST.md`

Current game-facing mirror:
- `game/content/dialogue/current/`
- **56 current runtime scenes**
- **2,021 spoken lines**
- generated from the current atomics
- validated by `Current Dialogue Runtime Validation`

The former sibling S-scene runtime folders for Chapters 0–3 have been retired from the live runtime layout. They are not fallback authority.

Regenerate/check with:

```text
python tools/dialogue/sync_current_dialogue.py --check
python tools/dialogue/compile_current_runtime_dialogue.py --check
```

## Chapter 4 current frontier

Current authority:
- `PRODUCTION/CHAPTER_04/CHAPTER_04_DIALOGUE_AUTHORITY_INDEX.md`
- B01–B12 canonical scene-authority specs
- B01 pre-approval rehearsal target

No Chapter-4 `_DIALOGUE.md` atomic is approved yet.

Critical timing:
- opening: Last Sentinel not yet Recovered;
- B02 Elder Thornhide: first verified modern manifestation / Recovered transition;
- B05: Vaelira permanently joins;
- B10: Seventh Reaction conclusion is complete-system emergent behavior, not a new element;
- chapter end: Last Sentinel remains Recovered, Wayfinder remains unresolved.

Current resume marker:
> `NEXT_ACTIVE_DIALOGUE_TASK.md`

## Current exact-line anchors

Protected older wording survives only where explicitly retained in current atomics.

Examples:
- Ch1 C03: `CYANIS: Old slut?` / `TORREN: Bitch.` and the later callback.
- Ch3 C06:
  - `CYANIS: I bet you use that cape to sneak up on the goats you fuck.`
  - `TORREN: You look like a walking dick in armor.`

Anchors do not lock surrounding dialogue.

## Current corrections surface

Use:
> `CURRENT_DIALOGUE_CORRECTIONS.md`

It is now a compact current-control pointer. The giant migration-era overlay was moved to archive provenance and is not live authority.

## Naming / numbering

- Dialogue filename authority: `PRODUCTION/DIALOGUE_FILE_NAMING_AUTHORITY.md`
- Character-Life numbering: `PRODUCTION/CHARACTER_LIFE_NUMBERING_LOCK.md`
- Current authority naming validator: `tools/dialogue/validate_authority_naming.py`

Stable identity belongs in filenames; mutable draft state belongs in metadata and Git history.

## What this folder owns

- approved/current spoken dialogue;
- pre-approval dialogue authoring specs and rehearsal targets;
- dialogue-specific continuity / authoring rules;
- current runtime dialogue synchronization;
- explicitly protected line anchors;
- dialogue authoring task/resume state.

## What this folder does not own

Dialogue notes may quote story/mechanical facts for context, but the owning story/system documents remain authoritative. A dialogue file must not silently become a second mechanics or story canon.
