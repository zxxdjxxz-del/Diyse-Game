# Diyse — Runtime Reconciliation Note

**Status:** ACTIVE RECONCILIATION FIREWALL  
**Purpose:** prevent the repository proof runtime from being mistaken for a blank implementation surface and prevent older technical authority from being copied forward as if every historical mechanic were still current.

## What this reconciles

Two different layers existed and must remain distinct:

1. **Accepted Godot gameplay proof** — the repository baseline demonstrated exploration, four-actor combat proof, Cards/Prime proof, versioned JSON save/load, dialogue Resources, and Android acceptance.
2. **Historical production technical authority** — the v1.36/v1.39 Technical Annex carried a substantially richer target-state/migration model, including the six-permanent/four-active roster architecture, full-roster progression rules, and `SAVE_SCHEMA_VERSION 130`.

The richer technical authority was not equivalent to the literal `game/core/state/game_state.gd` proof state on the accepted gameplay baseline. The accepted proof still used a compact four-character proof fixture and proof save schema 1.

Therefore:
- do **not** treat the compact proof as evidence that roster/progression architecture was never designed;
- do **not** rebuild already-established architecture from scratch merely because the proof fixture is smaller;
- do **not** treat historical v130 mechanics as automatically current, because later canon changed Player Level, Class Level/CEXP, Face terminology, Mastery handling, Prime rules, chapter structure, and other systems;
- do **not** create a parallel sequence of newly invented "production schema v2/v3" milestones without first reconciling against the historical technical authority and the current owning domains.

## Current operating rule

Before any new persistent-state, roster, progression, class, Card, Prime, equipment, economy, or battle-core implementation pass:

1. read the current owning numbered domains;
2. recover the compatible architecture from the historical Technical Annex where useful;
3. inspect what the accepted Godot proof actually implements;
4. classify each requirement as **already implemented**, **historically specified but not literally implemented in the proof**, **superseded**, or **genuinely new**;
5. only then change runtime state or save schema.

## Historical anchors

Accepted gameplay/Android proof baseline:
`f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`

Historical Technical Annex architecture includes:
- six permanent characters;
- four active battle slots;
- reserve/full-roster progression behavior;
- stable permanent-character implementation IDs;
- versioned persistence and migration requirements;
- historical `SAVE_SCHEMA_VERSION 130` target-state authority.

Those historical values are recovery architecture, not a license to restore superseded Level/Class/Mastery/Card/Prime rules.

## September 2 correction

A short implementation detour created a new proof-wallet/roster migration sequence and described schema v2/v3 as production advancement. That work was based on the wrong assumption that the richer roster/progression/save architecture had never already been established in the technical authority.

The repository is being returned to the last pre-detour content state while this reconciliation note remains as the guardrail against repeating that mistake.

## Next-step rule

Do **not** continue automatically into class/loadout, Prime persistence, or battle-core rewrites from the reverted detour.

Resume implementation only from a deliberate current-vs-historical reconciliation of the specific system being worked on.
