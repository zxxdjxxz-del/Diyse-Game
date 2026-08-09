# Diyse — Dialogue Engineering & Presentation Rules

## Hard implementation rule

Diyse has **no player dialogue choices**.

Do not implement:

- response wheels;
- tone choices;
- affinity responses;
- persuasion trees;
- player-selected jokes;
- good/evil dialogue;
- romance-choice menus;
- branching player-spoken responses.

Cyanis and the rest of the cast use authored dialogue.

## Current production state

The dialogue study is **COMPLETE**. Diyse Active Dialogue Development Annex v1.1 is the finished craft basis for production dialogue unless the user explicitly revises it.

Step 7B.5C has also **PASSED on Android** and proved that the generic dialogue architecture can support:

- speaker names and authored text;
- portrait/expression changes;
- staged speaker presentation;
- manual authored progression;
- silent reaction beats with no spoken line;
- movement/input lock during conversation;
- world/proximity triggering;
- clean return to exploration;
- authored conversations without response-menu architecture.

The technical-proof Cyanis/Torren dialogue and placeholder portraits were disposable fixtures and are not script or visual canon.

**Step 7C — Dialogue-First Scene Writing remains ON HOLD until explicit user authorization.** Do not infer authorization from completion of the study or technical proof.

When Step 7C is explicitly authorized, the standing production order begins with Chapter 0 S001–S006, then C01 and C02, unless the user changes the order.

## Writing/presentation philosophy

The final dialogue direction is grounded, character-specific, and conversational.

Core shorthand:

**Talk like people. React with expressive anime-style visual energy. Time jokes like strong comedy. Structure scenes like strong RPGs. Remember the war exists. Occasionally let characters argue about absolutely nothing.**

Engineering should not force every line into the same cinematic presentation. The final game may need several channels, including:

- major scene dialogue;
- portrait-driven Character-Life scenes;
- short walk-and-talk dialogue;
- ambient party chatter;
- overheard NPC dialogue;
- battle barks;
- post-battle dialogue;
- silent portrait/staging beats.

## Important system constraints

- Silence must be possible; every present character does not need a line.
- A portrait/expression change must be possible without new dialogue text.
- A conversation must be able to end without a choice menu.
- Dialogue data should not require romance meters, affinity values, or alignment scores.
- Conversation progression may depend on ordinary story/world flags when canon requires it, but not on player-selected personality responses.
- The UI must remain readable on Android in landscape orientation.
- Generic dialogue code must remain character-agnostic; authored records decide what a character says and how a scene is staged.

## Character-sheet protection

The final script must obey protected character voice/relationship authorities and the completed Dialogue Development Annex v1.1. Engineering must not bake character-specific assumptions into generic dialogue UI code.

The dialogue runner presents authored data; it does not decide what Cyanis, Ilyra, Torren, Nimera, Vaelira, Seyrik, or any NPC would say.

## Step 7C boundary

When authorized, Step 7C may add exact voiced dialogue, staging, portrait/performance notes, camera intent, contextual line banks, interruptions, pauses and implementation flags. It may not silently reopen story outcomes, class architecture, combat rules, Card/Prime identities, relationship canon, Vaelkor/fragment authority or final-act hard locks.