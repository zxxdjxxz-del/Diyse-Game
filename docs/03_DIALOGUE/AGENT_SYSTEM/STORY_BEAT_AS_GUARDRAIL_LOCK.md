# Diyse — Story Beat as Guardrail Lock

**Status:** LOCKED DIALOGUE-PRODUCTION CORRECTION  
**Effective:** 2026-09-11  
**Domain:** rehearsal-first Dialogue Engine  
**Scope:** all current and future Diyse dialogue production, including remediation of Chapter 3 Beats 6–8.

## Core rule

> **Story structure controls the situation, hard outcomes, reveal boundaries, and gameplay state. It does not pre-write the conversational path.**

A story/beat packet is a **guardrail and destination**, not a rehearsal script.

The Dialogue Director must not convert a structural packet into a list such as:
- Character A states fact X;
- Character B corrects it;
- Character C voices the safety rule;
- Character D summarizes the conclusion;
- Character A explicitly explains why the final choice is voluntary.

That form predetermines the scene and reduces Person Agents to voice filters over an already-written conversation.

## What may be supplied to Person Agent rehearsals

Supply only what the characters need to inhabit the moment:
- current location and visible situation;
- who is present;
- what just happened;
- each person's actual knowledge and memories;
- relevant relationship state;
- immediate physical/gameplay pressure;
- the genuine problem or decision in front of them;
- hard story outcomes that must be true by the end;
- forbidden reveals / continuity boundaries.

Where a fact has necessary provenance, that provenance remains binding. Example: Torren may own a route observation because he physically copied or observed it; Ilyra may own a medical observation because she personally examined the condition. This is not permission to assign every required story point to a speaker.

## What must NOT be supplied as rehearsal choreography

Do not pre-compose:
- speaker order;
- question → answer → correction sequences;
- required jokes;
- required interruptions;
- required verbal acknowledgements;
- explicit statements of theme;
- explicit statements of character motivation that behavior can show;
- lines whose only purpose is to certify that the scene satisfied a structural rule;
- recruitment speeches explaining why someone is joining;
- safety speeches when a character can simply behave cautiously;
- knowledge-firewall dialogue such as characters repeatedly announcing what they do not know;
- canon-checker phrasing such as `that's all we know`, `nothing is proven`, `important distinction`, `we cannot conclude`, or `that is the fact` when ordinary speech can carry the same boundary.

**Reveal firewalls are production constraints, not required spoken dialogue.** Prefer to preserve them through what characters simply do not claim, or through natural questions, hesitation, disagreement, irritation, incomplete theories, concrete observations, or a plain `don't know` when that is what a person would actually say.

The Canon / Knowledge Checker remains responsible for ensuring the finished scene does not overclaim.

## Outcome versus route

Valid hard outcome:
> By the end of Beat 8, Nimera has chosen to continue and permanently joins the party.

Invalid rehearsal instruction:
> Cyanis tells Nimera she is free to choose; Nimera explains her reasons; Torren asks whether she means permanently; Nimera explicitly confirms permanent recruitment.

Valid hard outcome:
> The party chooses Ivorybridge as the next practical northern search point without Ancient evidence confirming that the routes lead there.

Invalid rehearsal instruction:
> Cyanis states that Ivorybridge is not on the Ancient map; Nimera says it is only a hypothesis; Ilyra restates that the route destination remains unknown; Torren verbally confirms the uncertainty before they leave.

The rehearsal must discover how the people actually get there.

## Dialogue Editor rule

After rehearsal, aggressively remove any line that exists mainly to:
- explain the beat structure;
- explain why a character is allowed to make their own choice;
- summarize a motivation already visible through behavior;
- restate a reveal firewall;
- assign credit to every participant;
- make the scene's theme explicit;
- ensure every present character has spoken.

A required outcome may be communicated by action, silence, gameplay transition, UI confirmation, or a very small exchange. It does not require a speech.

## Quality test

Before approving a scene, hide the beat checklist and ask:

> **Would these people still plausibly arrive at this exchange if they only knew the situation they are living through?**

If the answer is no—if a line exists because the author needs to explain the story architecture—rerun or cut it.

## Chapter 3 Beats 6–8 remediation

Beats 6–8 must be rerun under this rule before Chapter 3 dialogue production continues into Beat 9.

Preserve their structural outcomes and reveal boundaries, but retire conversational choreography from their production specs and drafts.

## Forward rule

This lock supplements:
- `CHAPTER_0_1_PIPELINE_CONTINUITY_LOCK.md`;
- `REHEARSAL_FIRST_AUTHORING_LOCK.md`;
- `KNOWLEDGE_FIREWALL_INVISIBILITY_RULE.md`.

If an older scene spec conflicts by assigning conversational checkpoints, this lock controls the dialogue-generation method while the underlying story outcomes remain authoritative.
