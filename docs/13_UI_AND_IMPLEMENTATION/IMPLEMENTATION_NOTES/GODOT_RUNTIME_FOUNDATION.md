# Implementation Notes — Godot Runtime Foundation
**Historical migration provenance:** v85-era consolidated tracker.
**Authority treatment:** this repository file is current UI/implementation-domain authority within its stated scope; Audit/v85 references remain provenance only.
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


Repository checkpoint:
`3fd07e92eda04f31ba613a654b3b1b28071f44e6`

## Current source layout
Active runtime already separates:
- core state/save;
- exploration;
- dialogue;
- combat;
- content;
- equipment services;
- presentation.

The repository's `game/README.md` also anticipates a `game/ui/` production split for:
- exploration;
- dialogue;
- battle;
- menus.

That UI layer should be created as actual milestones require it, not as empty abstraction folders.

## Useful existing classes
- `game/core/state/game_state.gd`
- `game/core/save/save_manager.gd`
- `game/exploration/player_controller.gd`
- `game/exploration/touch_dpad.gd`
- `game/dialogue/dialogue_scene_definition.gd`
- `game/dialogue/dialogue_portrait_registry.gd`
- `game/dialogue/dialogue_runner.gd`
- `game/combat/battle_state.gd`
- `game/combat/round_resolver.gd`
- `game/equipment/kessara_relic_copy_service.gd`
- `game/presentation/*`

## Architecture to preserve
- content data outside generic UI;
- stable IDs;
- versioned persistence;
- deterministic round resolver;
- transient scene handoff separated from disk save;
- portrait registry indirection;
- schema validators;
- reusable HD-2D presentation contracts.

## Do not overprotect proof presentation
`combat_proof.gd` dynamically creates a large proof interface.
`field_proof.tscn` exposes proof Save/Load/Combat buttons.

Those prove interaction behavior only.
They are not production screen layouts.
