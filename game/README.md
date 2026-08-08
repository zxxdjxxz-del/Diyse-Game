# Game Source Layout

This directory will contain the Godot gameplay implementation.

Intended top-level subsystem layout:

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
