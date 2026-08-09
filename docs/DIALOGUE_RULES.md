# Diyse — Dialogue Engineering & Presentation Rules

## Hard implementation rule

Diyse has **no player dialogue choices**.

Do not implement response wheels, tone choices, affinity responses, persuasion trees, player-selected jokes, good/evil dialogue, romance-choice menus, or branching player-spoken responses. Cyanis and the rest of the cast use authored dialogue.

## Current production state

The dialogue study is **COMPLETE**. **Diyse Active Dialogue Development Annex v1.3** is the current craft, locked authoring-contract, and approved Chapter 0 production-dialogue authority unless the user explicitly revises it.

Step 7B.5C **PASSED on Android** and proved the generic authored dialogue architecture: speaker/text presentation, portrait/expression changes, staged speakers, manual progression, silent reaction beats, movement/input lock, world/proximity triggering, clean return to exploration, and no player response-menu architecture.

Step 7B.6 **PASSED** and locks the production handoff:

- production scenes use `DiyseDialogueSceneDefinition` Resources;
- scenes use stable semantic IDs, not embedded portrait file paths;
- portrait assets resolve through `DiyseDialoguePortraitRegistry`;
- beat IDs follow `<SCENE_ID>_B###`;
- trigger and completion IDs are explicit content data;
- staging/camera/movement instructions travel as cue metadata separate from spoken text;
- the generic `DialogueRunner` consumes Resource-backed scenes through `start_scene(...)`;
- choice/response/branch fields are forbidden and schema-validated.

Accepted 7B.6 implementation merge: `96c6bdc77f39c988f2185634b4e51546f2a0d76b`.

**Step 7C is ACTIVE. Chapter 0 is COMPLETE / APPROVED / MERGED.** S001–S006 plus C01 and C02 are current approved production dialogue. They were merged at `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5` after individual scene review, whole-chapter continuity/repetition/voice/runtime review, full Godot regression and Android export. The current recovery checkpoint is **v1.36 / Audit48**.

The next mandatory production block is **Chapter 1 S007–S011**.

## Chapter-level Step 7C workflow

Use one branch/PR per chapter or comparable substantial narrative block. Review/checkpoint individual scenes in sequence, keep a single chapter tracker, run scene-specific validators as content is authored, perform one whole-chapter continuity/repetition/voice/runtime pass, then run full Godot + Android regression on the exact final chapter head. Full Android export after every dialogue-only scene is unnecessary unless engine/schema/platform behavior changes.

See `docs/DIALOGUE_AUTHORING_SCHEMA.md` and `docs/STEP_7C_AUTHORING_TEMPLATE.md` before authoring or integrating a production scene.

The technical-proof Cyanis/Torren dialogue, `PROOF_SCHEMA`, and placeholder portraits remain disposable fixtures and are not script or visual canon.

## Writing/presentation philosophy

The final dialogue direction is grounded, character-specific, and conversational.

Core shorthand:

**Talk like people. React with expressive anime-style visual energy. Time jokes like strong comedy. Structure scenes like strong RPGs. Remember the war exists. Occasionally let characters argue about absolutely nothing.**

Engineering should support multiple channels where authored content needs them: major scenes, portrait-driven Character-Life scenes, short walk-and-talk dialogue, ambient party chatter, overheard NPC dialogue, battle barks, post-battle dialogue, and silent portrait/staging beats.

## Important system constraints

- Silence must be possible; every present character does not need a line.
- A portrait/expression change must be possible without new dialogue text.
- A conversation must be able to end without a choice menu.
- Dialogue data must not require romance meters, affinity values, or alignment scores.
- Conversation progression may depend on ordinary story/world flags when canon requires it, but not on player-selected personality responses.
- The UI must remain readable on Android in landscape orientation.
- Generic dialogue code must remain character-agnostic; authored records decide what a character says and how a scene is staged.
- Production scene Resources must use registered character/expression IDs rather than raw portrait asset paths.
- Cue metadata must not smuggle in unapproved gameplay mechanics or branching player responses.

## Character-sheet protection

The script must obey protected character voice/relationship authorities and Dialogue Development Annex v1.3. Engineering must not bake character-specific assumptions into generic dialogue UI code. The runner presents authored data; it does not decide what any character would say.

## Step 7C boundary

Step 7C may add exact voiced dialogue, staging, portrait/performance notes, camera intent, contextual line banks, interruptions, pauses and implementation flags. It may not silently reopen story outcomes, class architecture, combat rules, Card/Prime identities, relationship canon, Vaelkor/fragment authority or final-act hard locks.

Every implementation-ready Step 7C scene must follow the stable-ID Resource schema and pass structural validation in addition to narrative/canon review. Chapter completion additionally requires the chapter-level continuity gate and exact-head full regression.