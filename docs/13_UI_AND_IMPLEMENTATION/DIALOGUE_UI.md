# Diyse — Dialogue UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Proven architecture
Production dialogue uses:
- `DiyseDialogueSceneDefinition` Resources;
- stable semantic character/expression IDs;
- `DiyseDialoguePortraitRegistry`;
- generic `DialogueRunner`;
- manual advance;
- silent beats;
- separate cue metadata.

## No choices
Hard rule:
> **Diyse has no player dialogue choices.**

Do not implement:
- response wheel;
- tone choice;
- affinity answer;
- persuasion menu;
- romance response;
- morality response.

## Portrait presentation
Current presentation rule:
- large high-resolution portraits;
- generally ~35–45% screen height where practical;
- dialogue box generally lower 20–25%.

Portraits are a primary acting layer.

## Required beat support
UI/runtime must support:
- speaker label;
- body text;
- left portrait;
- right portrait;
- active-side emphasis;
- portrait change without spoken text;
- true silent beat;
- manual continue;
- movement/input lock;
- clean return to exploration.

## Stable IDs
Production scene data references:
> character ID + expression ID

not final image file paths.

## Current ID correction
Global current chapter IDs extend through:
> `chapter_13`

Current mandatory story sequence extends through:
> **S073**

Older schema documents capped at chapter_12/S062 are stale bookkeeping.

## OPEN PRODUCTION UX
- text speed;
- backlog/history;
- auto mode;
- skip/fast-forward;
- nameplate treatment;
- exact text-box skin;
- exact active/inactive portrait dim amount.
