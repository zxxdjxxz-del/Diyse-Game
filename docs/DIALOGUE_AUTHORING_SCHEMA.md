# Diyse — Production Dialogue Authoring Schema

**Schema version:** 1  
**Established by:** Step 7B.6 Production Handoff Lock  
**Step 7C status:** ACTIVE / AUTHORIZED August 8, 2026

This document defines how authored Step 7C dialogue is represented for the Godot production line.

## Core rule

Authored dialogue is **content data**, not generic UI code.

A production scene Resource records stable semantic IDs, spoken text, portrait-expression IDs, and implementation cues. The generic dialogue runner resolves those records for presentation. Final scene text must never be embedded in `dialogue_runner.gd` or other reusable engine code.

There is no player dialogue-choice field in the production schema.

## Stable ID conventions

### Production scene IDs

Use the already-authoritative project IDs unchanged:

- mandatory sequences: `S001` through `S062`;
- Character-Life scenes: `C01` through `C23` and `H01` through `H20`;
- other already-approved quest/scene IDs remain exactly as established by their controlling source.

Technical fixtures must begin with `PROOF_` and can never be promoted into canon by renaming their text.

### Beat IDs

Every authored beat is unique inside its scene:

`<SCENE_ID>_B###`

Examples: `S001_B001`, `C20_B014`, `H10_B023`.

Beat IDs are implementation handles. Editing spoken text does not require changing a beat ID unless the beat itself is deliberately removed/replaced.

### Character IDs

Permanent party IDs are fixed:

- `cyanis`
- `ilyra`
- `torren`
- `nimera`
- `vaelira`
- `seyrik`

Approved NPC IDs use stable lowercase `snake_case` identifiers derived from the approved identity. Do not invent an NPC merely because an ID is needed.

Display names belong to the registry/content layer, not the scene's portrait path.

### Chapter IDs

- `chapter_00` through `chapter_12`
- `after_story`
- `shared` only for reusable/non-chapter production infrastructure or technical fixtures

### Completion flags

Default convention:

`scene.<scene_id_lowercase>.complete`

Example: `scene.s001.complete`.

A different flag is permitted only when an approved story/world-state specification requires it.

### Trigger IDs

Trigger IDs are namespaced stable handles, for example:

`trigger.chapter_00.s001`

The ID identifies the trigger contract; the exact gameplay condition belongs to the appropriate story/world-state data rather than dialogue UI code.

### Expression IDs

Expression IDs are lowercase `snake_case` semantic IDs registered for a character, such as `neutral` or a later approved expression identity.

A scene may reference only expressions present in the active portrait registry. Do not invent final portrait expressions inside a dialogue scene to make validation pass.

## Scene Resource fields

`DiyseDialogueSceneDefinition` currently provides:

- `schema_version`
- `scene_id`
- `chapter_id`
- `scene_kind`
- `location_id`
- `trigger_id`
- `completion_flag`
- `participants`
- `authoring_notes`
- `beats`

Supported `scene_kind` values are currently:

- `mandatory`
- `character_life`
- `quest`
- `ambient`
- `banter`
- `battle`
- `proof`

Adding a scene kind is a schema change, not something an individual scene should improvise.

## Beat fields

Each beat dictionary contains:

- `beat_id` — stable unique beat handle;
- `speaker_id` — stable character/NPC ID, or empty for a silent reaction;
- `text` — authored spoken text, or empty for a silent reaction;
- `left` — portrait slot `{character_id, expression_id}`;
- `right` — portrait slot `{character_id, expression_id}`;
- `active_side` — `left`, `right`, or `none`;
- `advance_mode` — currently `manual`;
- `cues` — implementation metadata dictionary.

If `text` is nonempty, `speaker_id` must be nonempty. A true silent beat may have both empty while portraits/staging carry the performance.

## Cue metadata

Cues are deliberately separated from spoken text. Common keys may include:

- `pause_ms`
- `staging`
- `camera`
- `movement`
- `interrupt`
- `implementation_flags`

The schema carries these cues even when a specific cue executor is not implemented yet. A scene writer should state intended presentation; generic engine code decides how supported cues are executed.

Do not encode story choices, affinity, morality, romance selection, or alternate Cyanis personalities inside cues.

## Portrait registry rule

Scene Resources reference `character_id + expression_id`, never final file paths.

`DiyseDialoguePortraitRegistry` resolves those semantic IDs to current presentation assets. This allows portrait art to be replaced or reorganized without rewriting hundreds of authored scene records.

## File layout

Production dialogue Resources should use:

`game/content/dialogue/<chapter_id>/<scene_id>.tres`

Technical fixtures stay under:

`game/content/dialogue/proof/`

Do not place production dialogue in `game/dialogue/`; that directory is for generic dialogue systems.

## No-choice guarantee

The following beat keys are explicitly forbidden by schema validation:

- `choices`
- `responses`
- `branches`
- `dialogue_choices`
- `affinity_options`
- `tone_options`

If future authored continuity requires conditional presentation based on legitimate world state, that must be designed as story/world-state gating under current canon—not converted into a player response system.

## Validation rule

Before a scene is implementation-ready it must pass schema validation for:

- required scene metadata;
- unique beat IDs;
- legal scene kind and active side;
- valid speaker IDs;
- registered portrait/expression IDs;
- valid cue dictionary;
- absence of player-choice/branch fields.

Schema validation proves structural correctness only. Canon, voice, pacing and dramatic quality remain governed by the Clean Active Master and Dialogue Development Annex. Step 7C authorization opens production authoring; it does not turn an unreviewed draft into approved canon.