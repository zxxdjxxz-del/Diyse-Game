# Diyse — Step 7C Scene Authoring Template

**Status:** ACTIVE / AUTHORIZED August 8, 2026. Prepared by 7B.6 and now controlling implementation-ready Step 7C scene drafts.

This is the required working template for full Dialogue-First Scene Writing.

## Whole-game scene-authoring gate

Before drafting any new scene, read and apply `docs/SCENE_AUTHORING_STANDARD.md`.

That standard is mandatory for all remaining game authoring from Chapter 4 forward. It requires a scene-level check of story/continuity, knowledge firewall, personalities/voices, relationship state, adult-natural dialogue, expressive JRPG/anime reaction language, affordable 2.5D staging, gameplay breathing room, random-battle spacing where fiction supports it, encounter/Hunt/boss constraints where relevant, and the scene's handoff into the next playable state.

The check is **scene-level**. Draft/review scenes at a normal useful size; do not fragment scenes into tiny blocks merely to perform the check.

## Scene header

- **Scene ID:** `<authoritative ID>`
- **Chapter ID:** `chapter_00` … `chapter_12` / `after_story`
- **Scene kind:** mandatory / character_life / quest / ambient / banter / battle
- **Location ID:** `<approved location ID>`
- **Trigger ID:** `<approved/stable trigger handle>`
- **Completion flag:** `scene.<scene_id_lowercase>.complete` unless controlling state authority requires otherwise
- **Participants:** `<stable character/NPC IDs>`
- **Controlling story authority:** `<master/source section>`
- **Protected character authorities consulted:** `<applicable Steps 1–5 / relationship authorities>`
- **Implementation dependencies:** `<known world flags, portrait expressions, camera/staging requirements>`

## Beat template

For each beat:

- **beat_id:** `<SCENE_ID>_B###`
- **speaker_id:** `<stable ID>` or empty for true silent beat
- **text:** `<authored dialogue>` or empty for true silent beat
- **left:** `{character_id, expression_id}`
- **right:** `{character_id, expression_id}`
- **active_side:** left / right / none
- **advance_mode:** manual
- **cues:**
  - `pause_ms`
  - `staging`
  - `camera`
  - `movement`
  - `interrupt`
  - `implementation_flags`

Do not narrate an expression in text merely because the portrait/staging can show it.

## Scene-writing checklist

### Canon

- Does the scene preserve every controlling story outcome and final-act hard lock?
- Does it avoid silently changing classes, combat, Cards/Primes, Legacy access, relationships, Vaelkor/fragment authority or world-state facts?
- Are participants present at a time/location where they are actually available?
- Are any lore/exposition statements owned by the correct character or source?

### Voice

- Does each speaker sound like the approved character rather than a generic witty RPG voice?
- Is profanity frequency/style correct for that character and emotional state?
- Is humor relationship-specific rather than assigned to a designated comic role?
- Does emotional exposure simplify language where the character authority says it should?
- Is nobody speaking merely because they are present?

### Natural conversation

- Do characters react to one another's exact wording rather than deliver alternating monologues?
- Are interruptions, incomplete thoughts, ordinary observations and silence used where natural?
- Can the conversation spend time on mundane material when the scene permits it?
- Is important eloquence earned rather than constant?
- Does wartime pressure remain present without making every conversation about the war?

### Gameplay spacing

- Does the player regain control between major dialogue beats when the fiction supports it?
- Is there enough traversal/exploration room that the game does not become back-to-back conversations?
- Are random battles enabled in hostile/unsecured traversal spaces where appropriate, with safe/story pockets suppressing encounters only where authored?
- Are random-battle areas long enough to breathe without becoming oversized empty zones?
- Is encounter variety appropriate to the chapter/location?
- Are authored encounters, bosses, Hunts, and random battles kept distinct?

### Portrait/performance

- Does each portrait/expression ID exist in the active registry?
- Is emotional information carried by portrait, staging, pause or silence when speech is unnecessary?
- Are silent reaction beats genuinely silent?
- Are active-side changes intentional?
- Are camera/staging cues instructions rather than prose pretending to be dialogue?

### Affordable 2.5D

- Can the scene be staged with reusable poses, portraits, props, camera inserts, lighting/VFX, small sprite shifts, and authored environment states?
- Can destruction/water/crowds/machinery be communicated through prepared states rather than physics, fluid simulation, crowd AI, or bespoke cinematic animation?
- Are micro-actions simplified when the same meaning can be carried by portrait/performance timing or an interaction pose?

### No-choice continuity

- No response wheel.
- No tone selection.
- No player-selected joke.
- No morality/affinity response.
- No romance dialogue choice.
- No persuasion-response menu.
- No alternate Cyanis personality branch.

### Implementation

- Scene ID is authoritative and unique.
- Every beat ID is unique and follows `<SCENE_ID>_B###`.
- Stable character IDs are used rather than display-name guesses.
- No raw portrait asset path is embedded in scene data.
- Trigger/completion flags are explicit data.
- Cue metadata is a dictionary and does not secretly implement a new gameplay mechanic.
- Schema validator passes.
- Existing 7B.5/7B.6 regression suite remains green after integration.

## Definition of scene complete

A Step 7C scene is complete only when:

1. dialogue and performance are approved for canon/voice;
2. the scene passes the whole-game scene-authoring standard, including gameplay spacing/random-battle/2.5D checks where relevant;
3. Resource data passes schema validation;
4. every referenced ID/expression/flag is valid or explicitly registered as a known production dependency;
5. generic engine code required no character-specific dialogue hack;
6. the scene introduces no player dialogue-choice architecture;
7. implementation notes distinguish current supported cues from later presentation polish;
8. completion is recorded without silently rewriting controlling authority.

Authorization to begin Step 7C does not itself approve an individual draft. Keep scene branches/drafts provisional until their review and validation are complete.