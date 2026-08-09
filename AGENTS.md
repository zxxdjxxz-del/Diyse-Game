# AGENTS.md — Diyse Engineering Contract

This file governs AI-assisted engineering work in this repository.

## Read first

Before changing gameplay code, read:

1. `docs/ACTIVE_CANON.md`
2. `docs/IMPLEMENTATION_STATUS.md`
3. the subsystem document relevant to the task
4. `docs/TECHNICAL_PROOF.md` when the task touches architecture proven in Step 7B.5
5. `docs/DIALOGUE_AUTHORING_SCHEMA.md` and `docs/STEP_7C_AUTHORING_TEMPLATE.md` before authoring or integrating production dialogue

If a task conflicts with these files or with a newer explicit user instruction, stop and flag the conflict. Do not silently reinterpret canon.

## Current authority state

- Whole-project written authority: **Clean Active Master Canon v1.36**.
- Technical authority: **Active Technical Annex v1.36**.
- Dialogue craft/authoring authority: **Dialogue Development Annex v1.3**; the dialogue study is complete.
- Recovery checkpoint: **v1.36 / Audit48**.
- **v1.35 / Audit47 and earlier are frozen recovery/history only.**
- Step 7B.5 technical feasibility: **COMPLETE / PASS on real Android hardware**.
- Step 7B.6 production authoring handoff: **COMPLETE / PASS**.
- Step 7C full scene writing: **ACTIVE / AUTHORIZED**.
- Step 7C Chapter 0: **COMPLETE / MERGED** — S001–S006 plus C01/C02 are approved production dialogue.
- Chapter 0 production merge: `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`.
- Next mandatory Step 7C production block: **Chapter 1 S007–S011**.
- Accepted 7B.5 gameplay baseline: `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`.
- Accepted 7B.6 production-handoff implementation merge: `96c6bdc77f39c988f2185634b4e51546f2a0d76b`.

## Step 7C workflow

Use the chapter-level workflow proven by Chapter 0:

- one production branch/PR per chapter or comparable substantial narrative block;
- review and checkpoint each scene before advancing;
- one chapter tracker rather than a new issue/PR for every scene;
- scene-specific validation plus a whole-chapter continuity/repetition/voice/runtime pass;
- full Godot and Android regression at the chapter checkpoint, or earlier only when engine/schema/platform behavior changes;
- one authority/archive checkpoint after the chapter/substantial milestone is complete.

## Hard rules

- This is a fresh Godot/GDScript implementation.
- Do **not** copy, port, import, or mechanically translate code from the older `zxxdjxxz-del/Diyse` repository unless the task explicitly authorizes a named reuse.
- Historical prototypes may be consulted only for lessons or evidence when specifically requested.
- Diyse is 2.5D: real 3D environments/depth/lighting/traversal combined with stylized 2D/2.5D character presentation.
- Diyse has no player dialogue-choice system. Do not create dialogue wheels, response menus, affinity dialogue, tone selections, persuasion trees, or branching player-spoken responses.
- Production dialogue must use the accepted stable-ID Resource schema rather than embedding canon scene text or raw portrait asset paths into generic engine code.
- Step 7C authorization permits scene writing; it does not permit silent changes to story/system/relationship/final-act canon.
- Combat is discrete round-based command combat, not real-time or timeline combat.
- Maximum active permanent battle party is four.
- Permanent battle commands are Attack / Ability / Card / Item / Defend.
- MP is the universal ordinary Ability resource. Do not invent character-specific gauges/resources.
- Standard Cards are unlimited-use and data-driven.
- Preserve the accepted automatic hostile retarget rule in `docs/COMBAT_RULES.md`.
- Prime Manifestations use the accepted directly controlled replacement/suspension architecture; do not collapse them into ordinary summons or cinematic one-shots.
- Persistent game state must remain separate from scene nodes and serialize as versioned plain data.
- Do not invent mechanics, terminology, characters, Cards, classes, resources, or story outcomes to fill gaps.
- Keep systems and authored content separate. Prefer data-driven definitions where practical.
- Do not hard-code content records into engine logic merely because the technical proof used placeholders.
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
- Any temporary shortcut must be clearly marked and must not masquerade as production architecture or canon content.

## Accepted-proof regression rule

Steps 7B.5 and 7B.6 are closed. Their accepted automated tests and real-device/platform behaviors are part of the implementation regression baseline. Chapter 0's complete Step 7C dialogue/resource/continuity gate is also an accepted production regression baseline.

Do not regress the proven exploration/dialogue/combat/Card/Prime/persistence architecture, production dialogue Resource contract, or approved Chapter 0 scene integration merely because later content is more complex. If a newer approved design genuinely requires changing an accepted behavior, update the controlling authority and tests deliberately rather than silently bypassing them.

Temporary proof fixtures are **not** protected content: graybox geometry, placeholder portraits/sprites, disposable dialogue, `PROOF_SCHEMA`, proof enemies, `Proof Strike`, temporary flat damage/rewards, proof flags/cues, and debug UI should be replaced during production without rewriting the proven subsystem boundaries.