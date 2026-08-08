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

Full Step 7C dialogue-first scene writing is not the purpose of Step 7B.5. The technical proof should use disposable authored lines only.

The dialogue system must prove that final authored scenes can later support:

- speaker names;
- portrait/expression changes;
- pauses and timing hooks;
- silent reaction beats;
- interruptions;
- character entry/exit staging hooks where needed;
- return to exploration without awkward state loss;
- triggering from story/world state;
- optional dialogue that does not require gameplay reward.

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

## Character-sheet protection

The final script must obey protected character voice/relationship authorities. Engineering should therefore avoid baking character-specific assumptions into generic dialogue UI code.

The dialogue runner should present authored data; it should not decide what Cyanis, Ilyra, Torren, Nimera, Vaelira, Seyrik, or any NPC would say.
