# Diyse — Active Engineering Canon Guardrails

This file is an implementation-facing summary. It does **not** replace the authoritative Diyse master canon, active annexes, protected character source files, or newer explicit user approvals. If this summary conflicts with a newer controlling project authority, the newer authority wins and this file must be updated deliberately.

## Current written authority

- **Whole-project root:** Diyse: 2.5D JRPG Clean Active Master Canon v1.36 — Chapter 0 Production Dialogue Canonization and Step 7C First-Chapter Completion Revision.
- **Technical annex:** Diyse Active Technical Annex v1.36 — current numerical, proven implementation, production authoring-interface, and Chapter 0 validation authority.
- **Dialogue annex:** Diyse Active Dialogue Development Annex v1.3 — completed study, locked authoring contract, and approved Chapter 0 production-dialogue authority.
- **Implementation evidence:** Diyse Step 7B.5 Technical Feasibility & Android Proof Report v1.0; Diyse Step 7B.6 Production Handoff Lock Report v1.0; Diyse Step 7C Chapter 0 Production Dialogue Completion & Validation Report v1.0.
- **Recovery checkpoint:** v1.36 / Audit48.
- v1.35 / Audit47 and earlier are frozen recovery/history only.

## Workflow state

- Dialogue study: **COMPLETE**.
- Step 7B.5 technical feasibility: **PASS — real Android device**.
- Step 7B.6 production dialogue handoff: **COMPLETE / PASS**.
- Step 7C Dialogue-First Scene Writing: **ACTIVE**.
- Chapter 0 S001–S006 + C01/C02: **COMPLETE / APPROVED / MERGED**.
- Chapter 0 merge: `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`.
- Next mandatory production block: **Chapter 1 S007–S011**.
- Active implementation repository: `zxxdjxxz-del/Diyse-Game`.
- Accepted 7B.5 gameplay baseline: `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`.
- Accepted 7B.6 implementation merge: `96c6bdc77f39c988f2185634b4e51546f2a0d76b`.

The default Step 7C workflow is chapter-level: one branch/PR per chapter or comparable substantial narrative block; scene-by-scene review/checkpointing; one chapter tracker; whole-chapter continuity/repetition/voice/runtime review; full Godot + Android regression at the chapter checkpoint unless engine/schema/platform changes require earlier gating; one authority/archive checkpoint after completion.

## Project foundation

- Diyse is a mature-fantasy 2.5D JRPG with an approximately 20-hour critical path.
- Permanent roster: exactly six — Cyanis Dovaren, Ilyra Amarin, Torren Harth, Nimera Pellan, Vaelira Serren, Seyrik Rell.
- Maximum active permanent battle party: four.
- Character level cap: 50.
- Each permanent character has exactly one Base Class and one Subclass.
- Combat is command-driven and turn-based using discrete rounds.
- MP is the universal ordinary Ability resource.
- There are no character-specific combat gauges/resources.
- Permanent battle commands: Attack / Ability / Card / Item / Defend.
- Current Card collection: 24 Standard Cards + 12 Prime Cards.
- Standard Cards are unlimited-use.
- Current Faces: Might, Elements, Grace, Resource, Change, Ruin.
- After-story free roam exists; no exclusive post-ending progression or hidden true ending.

## Presentation authority

Diyse is a **2.5D** game. This supersedes older implementation text that described the shipped game as fully 3D.

The target combines 3D environments/depth/lighting/traversal with stylized 2D/2.5D character presentation and expressive illustrated dialogue portraits where appropriate. Step 7B.5 proved the architectural coexistence on Android; its graybox method/art remains non-canon.

## Dialogue authority

Diyse has **no player dialogue choices**. Cyanis is a defined authored protagonist. Do not implement response wheels, tone menus, affinity dialogue, branching player-spoken responses, persuasion trees, good/evil dialogue, or romance dialogue choices.

The dialogue study is complete. Step 7B.6 locks the production authoring interface:

- production scene records use `DiyseDialogueSceneDefinition` Resources;
- scene, beat, character/NPC, expression, trigger and completion identifiers are stable semantic IDs;
- beat IDs use `<SCENE_ID>_B###`;
- portrait file paths resolve through `DiyseDialoguePortraitRegistry`, not authored scene data;
- camera/staging/movement/implementation information travels as cue metadata separate from spoken text;
- `DialogueRunner` consumes validated Resource-backed scenes through `start_scene(scene_definition, registry)`;
- known choice/response/branch fields are rejected by schema validation.

Chapter 0 is the first complete production exercise of that contract. S001–S006, C01 and C02 are approved production dialogue, validated individually and as a cross-scene chapter set. Authorization permits further exact dialogue/staging work but does **not** permit silent changes to story outcomes, chapter order, combat, Cards/Primes, relationships, Vaelkor/fragment authority, or final-act locks.

See `DIALOGUE_AUTHORING_SCHEMA.md` and `STEP_7C_AUTHORING_TEMPLATE.md` before authoring or integrating production dialogue. Disposable technical-proof lines, `PROOF_SCHEMA`, proof cues and placeholder portraits are not canon.

## Combat implementation authority

The accepted round architecture uses beginning-of-round processing, enemy action locking before unconfirmed player commands, one selected action per conscious active party member, Item priority, Defend priority, then current effective Speed ordering with deterministic tie rules. Speed determines order only and never grants extra ordinary actions.

### Automatic hostile retargeting

If a queued player hostile action's original enemy target is defeated before that action resolves:

- seek the next living enemy in encounter-slot order;
- wrap to the first living enemy when needed;
- change only the target — actor, action identity, cost, priority and Speed remain unchanged;
- apply this to Attack, hostile/damaging Abilities, hostile Standard Cards, and equivalent directly controlled Prime hostile commands unless an authored effect explicitly overrides targeting;
- expose the retarget in presentation/logging.

## Card and Prime implementation authority

- Standard Cards remain unlimited-use and data-driven; no charges, Essence, Card ranks, refresh counters, or per-battle Standard-use counters.
- Every collectible Prime Card summons one directly controlled Prime Manifestation under current Prime authority.
- Prime activation consumes the bearer's selected Card action, establishes the approved pending/replacement flow, suspends the active party at the correct boundary, exposes Prime-specific commands, and restores the frozen party according to current Prime rules.
- Prime Manifestations are separate from ordinary summons.

`Proof Strike`, temporary flat Prime/Card damage and other proof numbers are not canon content values.

## Persistence authority

Persistent game/session state remains separate from scene nodes and serializes as versioned plain data under Godot `user://`. Step 7B.5 proved representative persistence across full Android app close/relaunch. Mid-round combat or active-Prime serialization was outside that proof and is not silently implied.

## Permanent character/class/story-Prime identities

- Cyanis — Crest Knight / Crest Magus — Might / First Champion
- Ilyra — Blue Warden / Vowblade — Grace / First Mercy
- Torren — War Archer / Diysean Marksman — Resource / First Sovereign
- Nimera — Cardweaver / Sixfold Knight — Change / First Change
- Vaelira — Green Arcanist / Prism Archer — Elements / First Element
- Seyrik — Ruin Vanguard / Ruin Reclaimer — Ruin / First Reckoning

Maevra is a temporary playable/recurring major ally, not a permanent progression character. Kessara is a nonplayable recurring technical ally.

## Relationship/story guardrails relevant to engineering

- No romance system, affection meter, jealousy system, triangle, triad, or route.
- Authored relationships can exist without gameplay meters.
- Cyanis and Ilyra have an authored mutual love relationship.
- Torren and Maevra have an authored adult intimate relationship.
- All six permanent characters survive the canonical ending.
- Vaelkor does not knowingly ally with the surviving fragment. The fragment covertly influences him and extends his life for nearly 300 years; the influence is subtle and does not remove his agency or responsibility.

## Proof-content exclusion

Do not mistake technical fixtures for canon. Non-canon proof material includes graybox geometry, placeholder Cyanis/Torren sprites/portraits, proof dialogue, `PROOF_SCHEMA`, proof registry/cues, Raider enemies/stats, `Proof Strike`, temporary flat damage/rewards, proof chest/state flags and debug UI.

## Historical repository rule

The older `zxxdjxxz-del/Diyse` repository is **historical prototype material only**. Its libGDX architecture, old field experiments, temporary formulas, assets, and prototype mechanics are not implementation authority for `Diyse-Game`.