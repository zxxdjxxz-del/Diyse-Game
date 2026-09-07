# Diyse — Story → Dialogue Handoff
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, read through all later explicit user corrections and current domain migrations.  
**Primary story authorities:** current chapter index; current chapter files and later explicit corrections; current Prime/character/world corrections.  
**Domain rule:** this folder owns mandatory story structure, chapter purpose, scene order, reveal order, recruitment/Prime milestones, interchapter causality, and story-state outcomes. Exact spoken dialogue belongs in `03_DIALOGUE`; battle numbers in `09_ENEMIES_AND_ENCOUNTERS`; progression numbers in `10_PROGRESSION_AND_EXP`.

`02_STORY` answers:
- what the scene must accomplish;
- what must already be known;
- what must remain unknown;
- who is present;
- the mandatory outcome;
- the relationship/story-state change;
- when mandatory chapter story gives way to cleanup;
- what explicit player action starts the next chapter.

`03_DIALOGUE` will own:
- exact spoken text;
- speaker order;
- pauses;
- delivery-specific line structure;
- optional Character-Life/camp dialogue;
- dialogue-specific acceptance locks.

## Global chapter-end cleanup handoff
For **Chapters 0–12**, dialogue generation must preserve a player-controlled cleanup period after the chapter's final mandatory story beat.

Dialogue / staging must **not**:
- automatically begin the next chapter because the final boss was defeated;
- automatically advance chapters after a rest, overnight cut, travel montage, or arrival at the cleanup hub;
- write a next-chapter opening event as though it occurs before the player has chosen to advance;
- use historical line-complete endings to bypass the current cleanup rule.

Instead:
- the current chapter remains active during cleanup;
- Character-Life scenes and other optional dialogue that are legal in the cleanup state may occur there;
- the player explicitly chooses the chapter-appropriate advance interaction when ready;
- only after that choice may the next chapter's opening dialogue / event begin.

If the transition closes or changes optional content, dialogue/UI staging should make the advance choice clear enough to function as an intentional chapter boundary.

**Chapter 13 exception:** there is no next chapter and no post-game cleanup after the final ending.

## Historical closed dialogue
Chapters 0–4 have historical exact/line-complete sources, but current reopened story authority and the global cleanup rule supersede any incompatible old chapter-ending structure.

## Later dialogue
For Chapters 5–13:
- do not invent line-complete dialogue merely because the story spine is now organized;
- preserve OPEN dialogue work where current authority says it is not yet written;
- when those chapters are authored, end Chapters 5–12 with the same cleanup → explicit player advance structure.
