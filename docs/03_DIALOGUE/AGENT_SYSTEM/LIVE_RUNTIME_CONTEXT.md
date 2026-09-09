# Diyse Dialogue Engine — Live Runtime Context Boundary

**Status:** ACTIVE IMPLEMENTATION CONTRACT  
**Godot implementation:** `game/dialogue/dialogue_runtime_context_builder.gd`  
**Runtime context schema:** `diyse_dialogue_runtime_context_v1`

## Purpose

The repository authority compiler answers:
> What is currently true in Diyse canon for this authored scene?

The live runtime context answers:
> What is observably happening in this particular playthrough at the instant the scene starts?

Those are deliberately separate channels.

A generated scene request therefore has two different sources of truth:
- `authority_packet` — current repository-owned story/character/world/system authority;
- `scene_context.runtime_observable` — curated live/provisional game observations.

Runtime observation can influence dialogue timing, fatigue, map awareness and encounter pacing. It does **not** gain permission to rewrite canon.

## Why raw GameState is forbidden

The current proof `GameState` still contains implementation-era data that is useful for engineering regression but is not safe Dialogue Engine context. Examples include stale Face labels, proof equipment identities, proof Prime/bearer data and an internal `gold` reward key.

Therefore:
> **Never serialize `GameState`, `GameState.to_save_dict()`, or another raw save/state container into a Dialogue Engine request.**

The current builder reads only:
- `current_area`;
- `field_position`.

Everything else must come through an explicitly curated runtime channel.

## Curated runtime sections

### Field
Captured automatically from the supplied GameState node when available:
- current area ID;
- field position as JSON-safe x/y/z numbers.

This is runtime positioning, not lore authority.

### Map
Current allowed map-observation fields:
- `cell_id`;
- `area_phase`;
- `dialogue_readiness` (`GREEN`, `AMBER`, `RED`);
- `location_name`;
- `visible_facts`;
- `route_state`;
- `time_context`;
- `context_status`.

Allowed `context_status` values:
- `current_runtime`;
- `provisional_runtime`;
- `observed_runtime`;
- `unknown_runtime`.

The builder adds:
> `authority = runtime_observation_not_story_authority`

For current provisional grayboxes or map blockouts, use `provisional_runtime`. Do not promote their topology to story canon merely because the player is standing inside that engineering scene.

### Recent gameplay
Current allowed fields:
- `recent_events`;
- `recent_combat_summary`;
- `recovery_state`;
- `fatigue_context`;
- `current_task`.

These should be brief, observable summaries. They are not a route for copying a combat log, inventory dump or author-only analysis into the scene.

### Interaction
Current allowed fields:
- `movement_enabled`;
- `input_locked`;
- `interaction_id`;
- `interaction_kind`.

### Encounter pressure
Captured automatically from the supplied field encounter controller when available:
- enabled;
- authored pause state;
- battle-active state;
- context-configured state;
- encounter area ID;
- normalized accumulated pressure;
- transition grace;
- whether an encounter is already pending.

It deliberately does **not** expose formation IDs, pending enemy lists, EXP rewards or implementation calibration such as world-units-per-S.

## Protected compiled fields

Runtime merge may not alter:
- request ID;
- scene ID;
- continuity namespace;
- story position;
- canon snapshot ID;
- participants;
- participant profiles;
- scene purpose;
- authority packet;
- allowed information transfers;
- exact-line anchors;
- maximum beat count;
- production-cost ceiling.

`current_floor_state` is also left untouched by the automatic live merge. It may contain carefully authored knowledge/state constraints, but the runtime builder will not fill it from raw `GameState.flags`.

If `scene_context.runtime_observable` is already present in a compiled request seed, the merge fails. That namespace belongs to the live runtime boundary.

## Raw-state rejection

The runtime input validator rejects raw/state-container keys such as:
- inventory;
- equipment;
- Standard Card container;
- Prime container;
- Relic inventory;
- Forge Components;
- flags;
- rewards;
- `gold`;
- proof bearer/progression internals.

Unknown top-level/nested fields also fail instead of being silently forwarded.

All caller-supplied runtime values must be JSON-safe. Godot objects/resources/vectors cannot be inserted through the curated input; the builder performs its own explicit Vector3 conversion for field position.

## Canon-snapshot gate

The runtime builder receives the expected deployment/runtime canon snapshot ID.

It rejects the merge if:
- the compiled request has no snapshot;
- the compiled request snapshot differs from the expected runtime snapshot;
- the authority packet snapshot differs from the request seed.

This is an early local guard. The external Orchestrator and Person Agents retain their own snapshot checks.

## Current validation

Headless validation:
> `tests/dialogue/validate_dialogue_runtime_context_builder.gd`

The test deliberately supplies the existing proof `GameState`—including its stale/internal data—and verifies that only the safe area/position subset reaches `runtime_observable`.

It also verifies:
- compiled protected fields cannot be overwritten;
- map observations retain provisional/non-authoritative labeling;
- encounter pressure/grace is merged;
- raw inventory/equipment/Prime/flag/economy fields are rejected;
- snapshot mismatch fails;
- a compiled seed cannot spoof `runtime_observable`.

## Remaining map integration

The builder now provides the safe merge boundary, but each production field/map still needs a small current map-context provider that can identify its live cell/phase/readiness without pretending provisional blockout data is canon.

Until those providers exist, map context is supplied explicitly to the builder through the same validated schema.

The intended production chain is:

> compiled current authority seed → live GameState/encounter capture + current map provider → curated runtime request → external Scene Orchestrator
