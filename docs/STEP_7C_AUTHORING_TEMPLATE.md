# Diyse — Step 7C Scene Authoring Template

**Status:** ACTIVE / AUTHORIZED  
**Current authority:** v1.73 / Audit88  
**Presentation target:** HD-2D

This is the required working template for implementation-ready Dialogue-First Scene Writing where Step 7C-style production authoring applies.

## Whole-game scene-authoring gate

Before drafting any new scene, read and apply `docs/SCENE_AUTHORING_STANDARD.md`.

That standard is mandatory for remaining new game authoring from **Chapter 5 forward** unless the user explicitly reopens earlier material. It requires scene-level checks of story/continuity, knowledge firewall, personalities/voices, relationship state, adult-natural dialogue, expressive HD-2D/JRPG performance, affordable HD-2D staging, gameplay breathing room, random-battle spacing, encounter/Hunt/boss constraints and scene handoff.

Do **not** use this template to re-author completed Chapters 0–4. Their exact source is already closed, and presentation implementation is controlled by Audit88.

## Scene header

- **Scene ID:** `<authoritative ID>`
- **Chapter ID:** `chapter_00` … `chapter_12` / `after_story`
- **Scene kind:** mandatory / character_life / quest / ambient / banter / battle
- **Location ID:** `<approved location ID>`
- **Trigger ID:** `<approved/stable trigger handle>`
- **Completion flag:** `scene.<scene_id_lowercase>.complete` unless controlling state authority requires otherwise
- **Participants:** `<stable character/NPC IDs>`
- **Controlling story authority:** `<master/source section>`
- **Protected character authorities consulted:** `<applicable character/relationship authorities>`
- **Implementation dependencies:** `<world flags, portrait expressions, camera/staging requirements>`
- **Cutscene tier:** `C0 / C1 / C2 / C3`
- **VFX tier:** `V1 / V2 / V3 / V4`

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

- Preserve every controlling story outcome and final-act hard lock.
- Do not silently change classes, combat, Cards/Primes, Legacy access, relationships, Vaelkor/fragment authority or world-state facts.
- Participants must be present at a time/location where they are actually available.
- Lore/exposition must be owned by the correct character/source.

### Voice

- Each speaker sounds like the approved character rather than a generic witty RPG voice.
- Profanity frequency/style matches that character and emotional state.
- Humor is relationship-specific rather than assigned to one comic role.
- Emotional exposure simplifies language where appropriate.
- Nobody speaks merely because they are present.

### Natural conversation

- Characters react to each other's exact wording rather than alternate monologues.
- Interruptions, incomplete thoughts, ordinary observations and silence appear where natural.
- Mundane material is allowed where scene purpose permits it.
- Important eloquence is earned rather than constant.
- Wartime pressure remains present without making every conversation about the war.

### Gameplay spacing

- Player control returns between major dialogue beats where fiction supports it.
- Traversal/exploration space prevents the game becoming back-to-back conversation.
- Random battles remain enabled in approved hostile/unsecured traversal and suppressed in authored safe/story pockets.
- Do **not** pre-author fixed or approximate random-battle counts; derive expected counts later from implemented geometry/rates.
- Encounter variety matches chapter/location.
- Authored encounters, bosses, Hunts and random battles remain distinct.

### Portrait / performance

- Every portrait/expression ID exists or is an explicit production dependency.
- Emotional information is carried by portrait, staging, pause or silence when speech is unnecessary.
- Silent reaction beats remain genuinely silent.
- Active-side changes are intentional.
- Camera/staging cues are instructions rather than prose pretending to be dialogue.

### Affordable HD-2D

Can the scene be staged with:

- reusable ~80 px field poses;
- large portraits;
- ordinary props;
- bounded camera framing/pans/inserts;
- lighting/VFX;
- small sprite shifts/turns;
- authored environment states;
- layered background loops;
- small reusable battle-background families where combat occurs?

Can destruction, water, crowds, machinery, chains, weather and scale be communicated through authored states/layers/audio rather than simulation?

Are micro-actions simplified when portrait/performance timing or a reusable interaction pose carries the same meaning?

### Production tier

Use:

- C0 Conversational
- C1 Staged
- C2 Dramatic
- C3 Spectacle
- V1 Common
- V2 Face/class identity
- V3 Named signature
- V4 Prime/boss spectacle

Most scenes should remain C0–C1. C3/V4 are rare and must preserve late-game escalation room.

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
- Existing compatible 7B.5/7B.6 regression behavior remains green after integration.
- Presentation implementation follows Audit87/Audit88 rather than retired 2.5D proof art direction.

## Definition of scene complete

A Step 7C-style scene is complete only when:

1. dialogue and performance are approved for canon/voice;
2. the scene passes the whole-game scene-authoring standard, including gameplay spacing/random-battle/HD-2D affordability checks;
3. Resource data passes schema validation;
4. every referenced ID/expression/flag is valid or explicitly registered as a known production dependency;
5. generic engine code required no character-specific dialogue hack;
6. the scene introduces no player dialogue-choice architecture;
7. implementation notes distinguish currently supported cues from later presentation polish;
8. completion is recorded without silently rewriting controlling authority.

Authorization to begin a chapter does not itself approve an individual draft. Keep drafts provisional until reviewed and validated.