# Diyse — Dialogue Engineering & Presentation Rules

## Hard implementation rule

Diyse has **no player dialogue choices**.

Do not implement response wheels, tone choices, affinity responses, persuasion trees, player-selected jokes, morality dialogue, romance-choice menus, or branching player-spoken responses. Cyanis and the rest of the cast use one authored continuity.

## Current production state

The dialogue study is COMPLETE and its compatible craft findings remain active.

Current whole-project story/dialogue authority is **Complete Master Canon v1.64 / Audit79**, plus any newer explicit user correction.

- Chapters **0–3 are COMPLETE/CLOSED** at story/dialogue/continuity/relationship/affordable-2.5D production-authority level.
- Chapter 0 S001–S006 + C01/C02 is COMPLETE / APPROVED / MERGED as live Resources at `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`, with later canon overlays controlling conflicts.
- Chapter 1 S007–S011 + C03–C05 is converted/validated as production Resources with exact source parity and whole-chapter continuity/final-version checks.
- Chapter 2 S012–S016 + C06/C07 is converted/validated as production Resources with exact source parity and whole-chapter continuity checks.
- Chapter 3 S017–S021 + H01–H04 is converted/validated as production Resources with exact source parity, corrected Cresthaven geography/handoff, Warden/Last Sentinel timing, and optional-scene checks.
- There is **no remaining Chapters 0–3 dialogue-Resource conversion backlog**.
- Chapter 4 — **The Seventh Reaction** — is the next exact scene-authoring frontier.

Use `docs/chapters/` for closed scene/pairing/knowledge/staging authority and `docs/chapters/dialogue/` for exact line-complete Chapter 1–3 wording.

## Proven dialogue architecture

Step 7B.5C passed on Android and proved the generic authored-dialogue architecture: speaker/text presentation, portrait/expression changes, staged speakers, manual progression, silent beats, movement/input lock, world/proximity triggering, clean return to exploration, and no response-menu architecture.

Step 7B.6 passed and locks the production handoff:

- production scenes use `DiyseDialogueSceneDefinition` Resources;
- scenes use stable semantic IDs, not embedded portrait file paths;
- portraits resolve through `DiyseDialoguePortraitRegistry`;
- beat IDs follow `<SCENE_ID>_B###`;
- trigger/completion IDs are explicit content data;
- staging/camera/movement instructions are cue metadata separate from spoken text;
- the generic `DialogueRunner` consumes Resource-backed scenes;
- choice/response/branch fields are forbidden and schema-validated.

Accepted 7B.6 merge: `96c6bdc77f39c988f2185634b4e51546f2a0d76b`.

## Validated closed-chapter baseline

For Chapters 0–3, Resource work is no longer a pending authoring task.

- Treat the validated `.tres` Resources as runtime translations of closed material.
- For Chapters 1–3, exact approved wording remains protected by source-parity validators against `docs/chapters/dialogue/`.
- Preserve scene purpose, protected lines/beats, pair progression, knowledge firewall, geography, roster changes and encounter handoffs.
- Bounded technical/staging adjustments may simplify presentation or change internal IDs/cues where necessary, but they may not silently rewrite dialogue or story.
- Follow-on work may wire triggers, portraits, maps, encounter consumers, hub services and presentation executors without reopening the script.

## Writing/presentation philosophy

Dialogue is grounded, character-specific, and conversational.

**Talk like people. React with expressive 2D/2.5D visual energy. Time jokes like comedy. Structure important scenes like a strong RPG. Remember the war exists. Occasionally let characters argue about absolutely nothing.**

Available conversation behavior includes interruptions, false starts, abandoned sentences, repeated words, partial answers, subject changes, failed jokes, misunderstandings, awkward pauses, profanity, boredom, callbacks, people entering/leaving, and unresolved endings. Use naturally, not as a checklist.

Silence is participation. Do not make every present character comment on every revelation.

## Current early-character voice anchors

- **Cyanis:** social and pleasant company; practical wit, teasing, questions, understatement. Attention to his own needs often becomes practical information. Do not flatten him into a generic stoic lead.
- **Ilyra:** excellent listener but not the party therapist; dry/warm, capable of jokes, gossip, irritation, fatigue and ordinary interests. Anger tends to become still, short, precise and formal.
- **Torren:** practical/social veteran, not a permanent terse dry-quip machine. Can become talkative about terrain, roads, bows, weather, animals and travel. Genuine danger erases humor.
- **Nimera:** engages; challenges wording, asks questions, notices contradictions, revises herself aloud and uses frequent clever profanity. True fury makes her formal and removes the swearing.
- **Maevra:** energetic, social, decisive, argumentative, mischievous and warm; not generic stern commander. Stress can push her into Commander Solmar mode without erasing the person.
- **Mirena:** charismatic, witty, observant, mischievous and politically impatient. Public voice cleaner/slower; private voice faster/warmer/more profane.
- **Lysara:** patient, observant, dryly funny, affectionate, stubborn and practical. Values continuity without stagnation and asks whether a decision should belong to sovereign authority at all.

## Protected relationship progression through Chapter 3

- **Cyanis + Torren:** professional respect becomes close friendship with increasingly profane, vulgar, mutually understood insults. C04 is the first unmistakable profane-friendship turn; Audit79 controls the final **“Old whore.” / “Bitch.”** version. Danger shuts the comedy off.
- **Torren + Maevra:** Chapter 1 = Harth/Solmar; Chapter 2 contains one involuntary `Torren!` crisis breach followed immediately by Harth; Chapter 3 H02 owns the first deliberate `Maevra.` T/Mae are later progression. Edda may call Maevra `Mae` because that is Edda's relationship, not Torren's progression.
- **Ilyra + Maevra:** independent adult professional friendship through dry humor, reality checks, gossip, care and reciprocal self-neglect. Neither is the other's therapist or manager.
- **Ilyra + Nimera:** warmth, humor and curiosity; care without scandalization. H03 is treatment, not therapy.
- **Cyanis + Ilyra:** early mutual competence/care grows gradually; no romance-choice architecture and no need to over-romanticize early scenes.

Exact protected Chapter 0–3 beats are stored in the chapter authority files and validated Resources.

## Knowledge discipline

Characters speak only from evidence they can plausibly have at that scene.

Especially through Chapter 3:

- do not leak the giant buried Crest or integrated Underground Crest civilization early;
- the Six Faces are common Yahtrean knowledge by Chapter 1;
- S020 can produce the first stable Ruby response and exact machine output `/PREVIOUS ERROR/` → `/LAST SENTINEL CONFIRMED/` without identifying Prime/Might in dialogue;
- S021 owns the bounded conclusions **Prime → Might → Last Sentinel → ultimate meaning unknown**;
- S021 unlocks Last Sentinel without manifestation;
- no modern person has a verified Prime activation/sighting until the player's first later real-battle use.

## Geography discipline

Current formal Realms are **Edgelands / Diysereach / Southhold**.

Chapter 3 is **Caelora → Old City / Suppressed Archives → separate Cresthaven**. Dialogue/staging must never imply that Cresthaven is the Warden chamber or part of the Old City.

The corrected handoff is fixed: post-Warden room proves false-order assembly; Torren copies the map-like route; party returns to Mirena; Mirena identifies Cresthaven as an abandoned Crown outpost; party stops overnight; S021 begins next morning with Mirena already establishing the working headquarters.

Legacy stable IDs containing old geography names such as `BORDERLANDS` are technical handles only and do not restore retired player-facing geography.

## Affordable 2.5D dialogue presentation

The scene writer states what the player should understand; engineering need not literalize every physical verb.

- use reusable sit/stand/walk/interaction/casting poses;
- use portraits and expression changes for close acting;
- use props and prop-state swaps for food, maps, reports, bandages, cups, chairs, tools and Cards;
- use camera inserts for checking/testing/reading/alignment;
- use authored before/after environment states + VFX instead of physics destruction;
- use authored water levels instead of fluid simulation;
- use layered crowd groups instead of crowd AI;
- use Warden-owned mechanical strike/emitter presentation for copied functions instead of actor-body mimicry;
- let silence and off-camera handling replace unnecessary bespoke animation.

## Important system constraints

- Silence and true silent beats must remain possible.
- Portrait/expression changes must be possible without dialogue text.
- Conversations end without choice menus.
- Dialogue data does not require romance meters, affinity values or alignment scores.
- Legitimate world-state gating is allowed; selectable protagonist personality responses are not.
- UI remains Android-landscape readable.
- Generic dialogue code remains character-agnostic.
- Production Resources use registered semantic IDs, not raw portrait paths.
- Cue metadata must not smuggle in unapproved mechanics or branching responses.

## Chapter 0 later-canon note

The old internal S004/S005 implementation label `Broken Champion's Ward` is superseded as canon terminology. The effect is an incomplete green/gold protective response from the sealed Card, not a Prime/Last Sentinel activation. A future bounded Resource+validator rename may neutralize the internal handle without reopening Chapter 0 dialogue or changing the already-approved temporary encounter behavior.

## Step 7C boundary

For Chapters 0–3, story/dialogue approval and Resource conversion are closed. Do not re-author them absent explicit change control.

New exact Step 7C scene authoring begins at **Chapter 4 — The Seventh Reaction**. It may add exact dialogue, staging, portrait/performance notes, camera intent, interruptions, pauses and implementation flags while respecting current whole-project story/system authority. It may not silently reopen class architecture, combat rules, Card/Prime identities, relationship canon, geography, or final-act locks.
