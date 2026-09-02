# Game Source Layout

This directory contains the Godot gameplay implementation and proof/runtime content.

Current implementation authority is routed through:
- `docs/00_MASTER_CONTROL/CURRENT_CANON_STATUS.md`
- `docs/00_MASTER_CONTROL/AUTHORITY_AND_CHANGE_CONTROL.md`
- the owning numbered domain
- `docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_AUTHORITY_PRECEDENCE.md`
- `docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`

Proof runtime content never overrides current canon.

## Character visual boundary

`game/characters/placeholders/` contains **proof-only runtime stand-ins**. They are not current character appearance authority and must not be used as subject references for production redraws/models.

Current exact source/reference character masters live under:
`asset_sources/characters/current/`

Their controlling production index is:
`docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md`

The source masters are not automatically deployable runtime assets. Production portraits/models/other runtime derivatives should be created in the appropriate runtime asset lane while remaining faithful to the master-image authority.

## Current subsystem direction

```text
game/
  core/
    state/
    save/
    data/
    events/
  exploration/
    actors/
    camera/
    interaction/
    maps/
  dialogue/
    runner/
    portraits/
    staging/
  combat/
    battle_state/
    resolver/
    actions/
    targeting/
    effects/
    statuses/
    cards/
    primes/
    ai/
  characters/
    data/
    presentation/
  content/
    characters/
    abilities/
    cards/
    enemies/
    items/
    encounters/
  ui/
    exploration/
    dialogue/
    battle/
    menus/
```

This is a direction, not permission to create empty abstraction layers in advance. Create folders/classes when the current milestone actually needs them.

Systems should not depend on final authored content being complete. Placeholder proof data must be replaceable without rewriting the engine.

## Terminology migration rule

Player-facing/runtime production data should use current terminology. Stable legacy technical IDs may remain temporarily where save/content migration requires them, but they must be mapped rather than exposed as current names.

Current handoffs:
- classes → `docs/00_MASTER_CONTROL/CLASS_TERMINOLOGY_CURRENT.md`
- Faces → `docs/00_MASTER_CONTROL/FACE_TERMINOLOGY_CURRENT.md`
- retired labels → `docs/00_MASTER_CONTROL/RETIRED_TERMINOLOGY_MAP.md`
