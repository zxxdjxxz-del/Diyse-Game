# Game Source Layout

This directory contains the current Godot gameplay implementation and implementation-facing content.

## Current top-level layout

```text
game/
  characters/    character runtime/presentation implementation
  combat/        battle systems and combat runtime
  content/       implementation-facing authored/runtime content
  core/          shared state, save, data and core services
  dialogue/      dialogue runtime integration
  equipment/     equipment runtime
  exploration/   field traversal, interaction and map runtime
  presentation/  presentation/runtime sidecars and related support
```

Subdirectories should exist because current implementation work needs them, not to pre-create speculative architecture.

## Authority boundary

This folder is implementation, not the primary design/canon library.

Before changing runtime behavior or production-facing content, follow:
- `docs/00_MASTER_CONTROL/DIYSE_MASTER_INDEX.md`;
- the owning numbered `docs/` domain;
- `docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_AUTHORITY_PRECEDENCE.md`;
- `docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md` when proof/runtime behavior may be stale.

Proof data and placeholder implementations may remain while systems are migrated. Their presence does not make them current design authority.

Systems should remain replaceable as authored content matures; implementation should not require unfinished chapters or provisional content to be treated as final canon.
