# DIYSE — Current Canon Project Library

**Status:** ACTIVE SUBJECT-BASED CANON LIBRARY  
**Current branch:** `main`

This `docs/` tree is the organized current authority library for Diyse. It replaces the old giant cumulative-tracker workflow.

## Read order

1. `00_MASTER_CONTROL/CURRENT_CANON_STATUS.md`
2. `00_MASTER_CONTROL/AUTHORITY_AND_CHANGE_CONTROL.md`
3. `00_MASTER_CONTROL/CANON_QUICK_REFERENCE.md`
4. the relevant numbered owning domain
5. `13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_AUTHORITY_PRECEDENCE.md` for implementation-facing conflicts
6. `90_WORKING/` only when the subject is explicitly open or reopened
7. `99_ARCHIVE/` only for provenance/history

## Authority rule

When current claims conflict:
1. newest explicit approved user correction;
2. current owning numbered-domain authority;
3. current cross-domain authority in `00_MASTER_CONTROL`;
4. clearly marked current working material for an intentionally unresolved question;
5. archived/historical material only for provenance.

`99_ARCHIVE` never silently overrides active canon.

## Active domains

- `00_MASTER_CONTROL` — cross-domain status, terminology, authority, open-work routing
- `01_CHARACTERS` — character identity, biography, chronology, relationships
- `02_STORY` — mandatory story structure, chapter spine, reveals, recruitment, PONR, ending
- `03_DIALOGUE` — exact approved spoken dialogue and line-level continuity
- `04_WORLD_AND_LORE` — regions, locations, factions, history, lore truth
- `05_BATTLE_SYSTEM` — global combat formulas, turns/rounds, targeting, statuses, elements, Critical, Guard
- `06_CLASSES_AND_ABILITIES` — classes, Abilities, Ultimates, Traits, MP, CL, Masteries, donor eligibility
- `07_CARDS` — Six Faces, Standard Cards, Story Primes, Major-Hunt Primes, Card/Prime runtime
- `08_ITEMS_AND_EQUIPMENT` — consumables, ordinary equipment, Relics, Legacies, components/materials
- `09_ENEMIES_AND_ENCOUNTERS` — enemy rosters, formations, bosses, Elites, Hunts, support objects
- `10_PROGRESSION_AND_EXP` — Player EXP, level curve, CEXP, encounter progression planning
- `11_QUESTS` — Character Quests, Side Quests, Hunt access/presentation, optional-content cutoff
- `12_ECONOMY_AND_REWARDS` — G, prices, shops, resale/repurchase, reward boundaries
- `13_UI_AND_IMPLEMENTATION` — UI/runtime requirements, saves, proof-runtime divergence, implementation debt
- `14_ART_AND_VISUALS` — visual authorities, HD-2D grammar, environment/map/VFX handoff
- `15_AUDIO_AND_MUSIC` — music/sound authority and implementation boundary
- `16_BALANCE_AND_TESTING` — balance certification, regression gates, representative true-battle testing

## Working and archive

`90_WORKING` contains only currently unresolved/reopened work. Approved work must be promoted into its owning numbered domain.

`99_ARCHIVE` contains migration history, retired terminology/authority, old package records, and provenance references. It is non-authoritative for current gameplay unless a current owner explicitly cites it for historical evidence.

Completed subject-folder migration/consolidation checklists are historical and do not belong in active domain roots. The current economy certification remains in `12_ECONOMY_AND_REWARDS/MIGRATION_VALIDATION.md` only because that legacy-named file has been converted into an explicitly current G/payout/liquidity validation.

## Current Face terminology

The current six Faces are:
> **Might / Elements / Grace / Perception / Memory / Ruin**

Detailed Face authority:
> `07_CARDS/SIX_FACES.md`

Retired Face labels such as Resource, Acuity, and Change belong only in historical/retirement context.

## Repository/runtime boundary

Canon reorganization does not replace runtime/build/test infrastructure. Preserve the root engineering surfaces routed by `../AGENTS.md`, including `game/`, `tests/`, `tools/`, `.github/`, `project.godot`, and `export_presets.cfg`, unless an explicit implementation task changes them.
