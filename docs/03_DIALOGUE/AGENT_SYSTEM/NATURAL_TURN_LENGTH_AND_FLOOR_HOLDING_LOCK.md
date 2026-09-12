# Diyse — Natural Turn Length and Floor-Holding Lock

**Status:** LOCKED PRODUCTION WORKFLOW CORRECTION  
**Effective:** 2026-09-12  
**Domain:** dialogue generation / editing rhythm  
**Scope:** Chapters 0–13 and all future story / Character-Life dialogue unless explicitly revised by the user.

## Problem this lock corrects

A recurring production failure has been identified:

> **Characters too often speak exactly one sentence, yield the floor, receive one sentence back, then continue in the same alternating pattern.**

This creates artificial ping-pong dialogue even when the individual lines are good.

The cause is not the portrait/dialogue-box presentation. It is an authoring/editing rhythm error: `concise`, `short`, `conclusion first`, and `cut aggressively` have been over-applied as if they meant **one sentence per speaker turn**.

They do not.

## Hard rule

> **Sentence count is not the unit of a conversational turn. A character keeps the floor until that person's thought, intention, emotional reaction, joke, explanation, refusal, or uncertainty naturally yields — unless another character interrupts.**

A turn may therefore be:
- one word;
- a fragment;
- one sentence;
- two or three sentences;
- several connected sentences when the moment genuinely belongs to that speaker;
- an unfinished thought cut off by interruption;
- silence.

There is no preferred sentence count.

## Concision correction

Character-brain labels such as:
- `concise`;
- `short practical question`;
- `conclusion first`;
- `shorter answers`;
- `lower verbal density`;

control **density, directness, and tendency**, not a maximum turn length.

Examples:
- Torren may still lead with the conclusion, then give two sentences of evidence because someone asked.
- Cyanis may ask a practical question, answer his own second thought, then make the joke before yielding.
- Ilyra may give a direct answer and continue because the consequence matters.
- Nimera may catch her own wording, revise it aloud, and keep going without another speaker being inserted between each clause.

Do not rewrite character brains merely to manufacture long speeches. Interpret their existing brevity traits correctly.

## Dialogue Editor correction

`Cut aggressively` means:
- remove repetition;
- remove canon-compliance speech;
- remove redundant explanation;
- remove weak jokes after the strong joke already landed;
- remove lines that exist only to distribute participation.

It does **not** mean:
- split one person's natural thought into several speaker exchanges;
- force a response after every sentence;
- turn paragraphs into alternating one-liners;
- shorten every speaker to identical dialogue-box length;
- make all characters equally terse.

> **Cut repetition, not floor time.**

If a speaker needs three sentences to complete one natural thought, keep the three sentences together unless interruption or reaction genuinely changes the scene.

## Dialogue box is not conversational turn

The runtime uses portraits + dialogue boxes, but UI pagination must not dictate human rhythm.

If a natural speaker turn is too long for one text box:
- split it into consecutive boxes from the **same speaker**;
- preserve the same floor unless a real interruption occurs;
- use portrait/expression changes or a manual advance if useful;
- do not invent another character response merely to break up text.

> **One dialogue box is a presentation unit. One speaker turn is a conversational unit. They are not the same thing.**

## Rhythm requirements

Across an ordinary scene, natural variation is expected.

Possible rhythm:
- a two-sentence answer;
- a one-word reaction;
- silence;
- one person continues for three sentences;
- an interruption;
- two fast one-liners;
- someone answers only the second half of what was said;
- a longer explanation because that person actually owns the information;
- no response at all.

Rapid one-sentence alternation is legal when the scene genuinely calls for it, such as:
- a sharp argument;
- immediate danger;
- comic volley;
- command shorthand;
- battle reaction;
- a deliberately terse exchange.

It must not become the default grammar of the whole game.

## Person-Agent rehearsal rule

During rehearsal, do not stop a Person Agent after the first syntactically complete sentence.

Let the agent finish the **behavioral turn**:
- what else would this person say before yielding?
- would they revise themselves?
- add evidence?
- qualify the claim?
- make the joke themselves rather than hand setup to another speaker?
- trail off?
- realize halfway through that they do not know?
- keep talking because nobody interrupts?

Another character should enter because that character has a reason to speak, not because the previous speaker reached a period.

## Anti-monologue boundary

This correction does not mean everyone should deliver speeches.

Longer turns must still be earned by:
- ownership of the information;
- emotional pressure;
- personality;
- relationship;
- explanation genuinely requested;
- comic escalation;
- uncertainty being worked through aloud;
- a decision that requires more than one clause.

Do not inflate dialogue merely to create sentence-count variety.

## Quality test

Before a scene is accepted, inspect the conversational shape rather than only line quality.

Ask:

> **Are speakers yielding because another person naturally takes the floor, or because the script reached the end of a sentence?**

Then:

> **If nearly every turn in this scene is one sentence, is there a scene-specific reason for that?**

If the answer is no, the scene fails rhythm review even if every individual line is technically in character.

Also check:
- Are there meaningful multi-sentence turns where the speaker naturally owns the moment?
- Are fragments and silence still available?
- Are interruptions actually interruptions rather than ordinary alternating dialogue?
- Does each character's verbal density differ from the others?
- Does the scene contain sentence-length variation without becoming verbose?

## Retroactive scope

Chapters 0–3 were authored before this failure was explicitly identified.

They remain current working dialogue authority, but they now require a **turn-length / floor-holding rhythm audit** before being treated as dialogue-polished for implementation.

The audit should preserve strong wording and story structure while repairing mechanical one-sentence ping-pong wherever it appears.

Do not rewrite scenes simply to make every turn longer. Change only places where the current cadence is artificial.

## Forward lock

All Chapter 4 onward dialogue must use this rule from the first Person-Agent rehearsal and Dialogue Editor pass.

> **Natural speech rhythm beats uniform line length. Concision is not one-sentence dialogue.**
