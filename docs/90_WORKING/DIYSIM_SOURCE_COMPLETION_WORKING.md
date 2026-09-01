# DiySim Source-Completion Working Notes

**Status:** WORKING / FEATURE-BRANCH ONLY / NOT OWNER PROMOTION  
**Branch:** `tooling/diysim-phase1`

Purpose: keep simulator-readiness source completions visibly separated from values recovered from current owner/audit authority. Nothing in this file promotes a working completion to `main` or canon by itself.

## Exact values recovered from existing authority

- Crownless War Engine EVA = **0** — current Major Hunt recertification and Audit135 lineage.
- Worldscar Leviathan EVA = **0** — current owner explicitly says EVA0 is intentional; Audit135 lineage agrees.
- The Unfinished World EVA = **0** — recovered from Audit135 raw-stat lineage.

These are restoration/synchronization corrections, not new tuning choices.

## Working completions that were not historically recovered

### Last Sentinel damaging Base Hit
Working branch value:
> **Base Hit 100** for every damaging Last Sentinel command.

Reason:
- current `05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md` requires Prime commands to own an authored Base Hit;
- current/historical Last Sentinel command packages omitted the exact value;
- Audit122 defines approximately 100 as the standard reliable-action authoring band.

This is a working completion, **not a recovered historical number**. Hold the Line remains non-damaging and uses Base Hit N/A.

### Major Hunt current-plus-next Confluence target shape
Working branch target for:
- Worldscar Leviathan — **Confluence Spear**
- The Unfinished World — **Confluence Rupture**

is:
> **one party member**

Reason: both commands are two-hit focused Confluence attacks whose owner text had complete per-hit Power/Base Hit/element-cycle behavior but omitted an explicit target declaration. This is a working source completion, not a recovered Audit135 target line.

## Still to close in this pass

- Hollow Watch Fortress Ballista defensive targeting completeness.
- Hollow Watch Watch Seal explicit passive-target body completeness.
- Hollow Watch Walking-State action identity normalization.
- generic cross-owner linking for support `Enables:` summaries and explicit `Authority:` action references.

Any non-recovered Hollow Watch numeric/identity completion must be added to this note before the feature branch can be considered ready for approval.
