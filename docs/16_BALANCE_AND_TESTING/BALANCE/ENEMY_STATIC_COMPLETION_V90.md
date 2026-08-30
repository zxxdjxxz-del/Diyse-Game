# Diyse — Enemy Static Completion — v90

**Status:** **CLOSED — STATIC ENEMY DESIGN COMPLETE**

This closure follows the completed Chapters 0–13 mandatory-vs-completionist paper validation and does **not** reopen the global direct-damage Power audit.

## Closed in v90
- four combat Character Quest bosses now have exact production sheets: Elemental Forecast Construct, Crest-Exhausted Warden, Black Host Remnant Captain, Old Relay Warden;
- Chapter 1–13 random-formation compositions are present in the owning `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/` files; Chapter 0 remains authored/tutorial-only by design;
- recovered formation weights are restored where they existed, including Chapter 12 and Chapter 13 30/45/25 phase weights and Chapter 10's 20/55/25 Light/Standard/Heavy tier model;
- all current targetable support objects/components have exact HP/defensive data and explicit Power or `Power: N/A`;
- enemy actions with missing migrated percentage weights now have a production fallback in `09_ENEMIES_AND_ENCOUNTERS/ACTION_SELECTION_DEFAULT.md`; explicit current weights always override it;
- authored identities whose exact scene placement is waiting on later dialogue/story work are centralized in `09_ENEMIES_AND_ENCOUNTERS/AUTHORED_ENCOUNTERS/STORY_INTEGRATION_BOUNDARIES.md` and no longer count as enemy-design gaps.

## What remains outside static enemy design
These do **not** reopen the enemy design pass:
- exact story scene IDs/triggers for bounded authored identities and some Regional Hunt return windows;
- runtime fight-duration/resource testing, especially Major Hunt #6 The Unfinished World with the full Prime/Card/Ultimate/Legacy toolkit;
- implementation QA, AI regression, animation/VFX/readability, and reward/economy ownership outside `09`.

## Final verdict
> **Enemy static design is complete enough to hand off to implementation/runtime QA.**

CEXP recalibration is **closed v91** at ~Lv55–60; the next systemic balance task is canonical mandatory/completionist party snapshots plus representative true-battle simulations.
