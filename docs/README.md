# DIYSE — Current Canon Project Library

**Status:** ACTIVE SUBJECT-BASED CANON LIBRARY

This `docs/` tree is the organized current authority library for Diyse. It replaces the old cumulative-tracker workflow.

## Read order

1. `00_MASTER_CONTROL/AUTHORITY_AND_CHANGE_CONTROL.md`
2. `00_MASTER_CONTROL/CANON_QUICK_REFERENCE.md` when a compact cross-domain orientation is useful
3. the relevant numbered owning domain
4. `13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_AUTHORITY_PRECEDENCE.md` for implementation-facing conflicts
5. `90_WORKING/ACTIVE_WORK_QUEUE.md` only for current sequencing/open cross-domain work
6. Git history only when deliberate provenance/recovery is needed

## Authority rule

When current claims conflict:
1. newest explicit approved user correction;
2. current owning numbered-domain authority;
3. current cross-domain authority in `00_MASTER_CONTROL`;
4. clearly marked current working material for an intentionally unresolved question;
5. archived/historical material only for provenance.

Historical material never silently overrides active canon.

## Active domains

- `00_MASTER_CONTROL` — cross-domain authority, index, quick reference, and terminology handoffs
- `01_CHARACTERS` — character identity, biography, chronology, relationships
- `02_STORY` — mandatory story structure, chapter spine, reveals, recruitment, PONR, ending
- `03_DIALOGUE` — exact approved spoken dialogue and line-level continuity
- `04_WORLD_AND_LORE` — regions, locations, factions, history, lore truth
- `05_BATTLE_SYSTEM` — global combat formulas, turns/rounds, targeting, statuses, elements, Critical, Guard
- `06_CLASSES_AND_ABILITIES` — classes, Abilities, Ultimates, Traits, MP, CL, Masteries, donor eligibility
- `07_CARDS` — Six Faces, Standard Cards, Story Primes, Major-Hunt Primes, Card/Prime runtime
- `08_ITEMS_AND_EQUIPMENT` — consumables, ordinary equipment, Relics, Legacies, components/materials
- `09_ENEMIES_AND_ENCOUNTERS` — enemy rosters, formations, bosses, strong normal-pool enemies, Hunts, support objects
- `10_PROGRESSION_AND_EXP` — Player EXP, level curve, CEXP, encounter/progression planning
- `11_QUESTS` — Character Quests, Side Quests, Hunt access/presentation, optional-content cutoff
- `12_ECONOMY_AND_REWARDS` — G, prices, shops, resale/repurchase, reward boundaries
- `13_UI_AND_IMPLEMENTATION` — UI/runtime requirements, saves, proof-runtime divergence, implementation debt
- `14_ART_AND_VISUALS` — exact visual authorities, HD-2D world/presentation grammar, rigged-3D party runtime direction, environment/map/VFX handoff
- `15_AUDIO_AND_MUSIC` — music/sound authority and implementation boundary
- `16_BALANCE_AND_TESTING` — balance frontier, regression gates, QA methods, release gates

## Working and archive

`90_WORKING` now contains only:
- the cross-domain active work queue;
- genuinely active playable-area/route production work.

Detailed open items belong in numbered owner domains.

Git history preserves migration history and superseded evidence. It is non-authoritative unless deliberately consulted for provenance or recovery.

## Current Face terminology

Current Faces:
> **Might / Elements / Grace / Perception / Memory / Ruin**

Detailed Face authority:
> `07_CARDS/SIX_FACES.md`

Retired Face labels such as Resource, Acuity, and Change belong only in historical/retirement context.

## Repository/runtime boundary

Canon reorganization does not replace runtime/build/test infrastructure. Preserve the root engineering surfaces routed by `../AGENTS.md`, including `game/`, `tests/`, `tools/`, `.github/`, `project.godot`, and `export_presets.cfg`, unless an explicit implementation task changes them.
