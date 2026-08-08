# AGENTS.md — Diyse Engineering Contract

This file governs AI-assisted engineering work in this repository.

## Read first

Before changing gameplay code, read:

1. `docs/ACTIVE_CANON.md`
2. `docs/TECHNICAL_PROOF.md`
3. the subsystem document relevant to the task

If a task conflicts with these files or with a newer explicit user instruction, stop and flag the conflict. Do not silently reinterpret canon.

## Hard rules

- This is a fresh Godot/GDScript implementation.
- Do **not** copy, port, import, or mechanically translate code from the older `zxxdjxxz-del/Diyse` repository unless the task explicitly authorizes a named piece of code.
- Historical prototypes may be consulted only for lessons or evidence when specifically requested.
- Diyse is 2.5D: real 3D environments/depth/lighting/traversal combined with stylized 2D/2.5D character presentation.
- Diyse has no player dialogue-choice system. Do not create dialogue wheels, response menus, affinity dialogue, tone selections, persuasion trees, or branching player-spoken responses.
- Combat is discrete round-based command combat, not real-time or timeline combat.
- Maximum active permanent battle party is four.
- Permanent battle commands are Attack / Ability / Card / Item / Defend.
- MP is the universal ordinary Ability resource. Do not invent character-specific gauges/resources.
- Do not invent mechanics, terminology, characters, Cards, classes, resources, or story outcomes to fill gaps.
- Keep systems and authored content separate. Prefer data-driven definitions where practical.
- Do not hard-code content records into engine logic merely because the current proof uses placeholders.
- Do not optimize around placeholder assets in a way that prevents final assets from replacing them.
- Do not change canon/specification documents as a side effect of implementing code.

## Engineering behavior

- Implement one bounded milestone at a time.
- Preserve deterministic behavior where the combat rules require it.
- Add automated tests or deterministic validation for pure logic whenever practical.
- Keep platform-specific code isolated.
- Treat Android as a first-class target, not a later port.
- Prefer simple, readable GDScript over clever abstractions.
- Avoid large god objects. Keep exploration, dialogue, combat, save/state, UI, and content loading separable.
- Any temporary shortcut must be clearly marked and must not masquerade as production architecture.

## Step 7B.5 rule

The current repository phase is a technical proof. The goal is not to make a content-rich demo; it is to prove the architecture that the full game would depend on.

A feature is not considered proven merely because code exists. It must satisfy the acceptance criteria in `docs/TECHNICAL_PROOF.md`, including Android-device validation where required.
