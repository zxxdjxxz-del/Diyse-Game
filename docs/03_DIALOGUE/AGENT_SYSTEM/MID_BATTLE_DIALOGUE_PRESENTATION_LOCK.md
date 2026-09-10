# Diyse — Mid-Battle Dialogue Presentation Lock

**Status:** CURRENT EXPLICIT USER DIRECTION  
**Domain:** battle dialogue / scene presentation / HD-2D production

## Hard rule

> **Mid-battle dialogue is allowed sometimes, but it is speech-only. Do not turn mid-battle dialogue into a scripted movement or cinematic blocking sequence.**

Characters may speak during active combat when the moment benefits from it. The battle system continues to own movement, positioning, attack animations, targeting, and combat flow.

## Allowed

- short character lines or exchanges during active combat;
- reactions to a boss state change, dangerous attack, phase transition, visible mechanic, or character beat;
- tactical or emotional speech that does not require authored movement to make sense;
- portrait/text/voice presentation over the existing battle state if supported by implementation;
- boss movement or transformation that is already required by the encounter itself.

## Not allowed for dialogue presentation

- scripted character steps, dodges, repositioning, running, turning, formation changes, or other locomotion;
- bespoke character blocking inserted just to accompany dialogue;
- extra attack/defense animations created only because someone speaks;
- camera cutaways or mini-cutscenes for ordinary mid-battle lines;
- pausing the fight to stage characters unless a separately authorized major cinematic moment explicitly requires it;
- dialogue that depends on a character physically moving to a specific authored spot.

If a line such as `Move!`, `Behind you!`, or `Get down!` is used, it is still only spoken dialogue. The script does not author a corresponding movement beat; normal battle behavior carries the action.

## Frequency

Mid-battle dialogue is optional, not mandatory. Use it when it improves the fight's character, readability, or emotional rhythm. Silence is equally valid.

Boss fights may support more mid-battle dialogue than ordinary random encounters, but even boss dialogue follows the speech-only rule unless a separate explicitly approved cinematic exception exists.

## Relationship to other locks

- Ordinary enemies remain random encounters under `RANDOM_ENCOUNTER_PRESENTATION_LOCK.md`.
- This rule does not convert random encounters into scripted scenes.
- The reductive HD-2D rule still applies: speech should reuse the existing battle presentation rather than creating new staging requirements.
- Walking-dialogue rules concern traversal outside battle and do not prohibit speech-only active-combat lines.
