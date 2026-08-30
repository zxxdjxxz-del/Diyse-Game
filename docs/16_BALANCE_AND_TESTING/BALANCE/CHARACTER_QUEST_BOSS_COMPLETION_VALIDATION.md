# Character Quest Boss Completion / Mandatory-vs-Completionist Validation — v90

**Status:** **COMPLETE — FOUR CURRENT COMBAT CHARACTER-QUEST BOSSES NOW HAVE EXACT SHEETS**

## Scope
This pass closes the numerical/action-sheet deferrals intentionally preserved by the stale-mechanic audit.

It does **not** reopen the campaign-wide direct-damage Power audit. The three formerly deferred sheets are authored now because the user explicitly chose to finish enemy design before CEXP recalibration.

## Current combat Character Quests
| Quest boss | Unlock reference | Boss Lv | HP | Result |
|---|---|---:|---:|---|
| Elemental Forecast Construct | post-Ch7, ~Lv32 mandatory / ~Lv37 completionist | 35 | 6,200 | PASS |
| Crest-Exhausted Warden | post-Ch7, ~Lv32 mandatory / ~Lv37 completionist | 35 | 6,800 | PASS |
| Black Host Remnant Captain | post-Ch8, ~Lv37 mandatory / ~Lv42–44 strong optional | 41 | 7,200 | PASS |
| Old Relay Warden | post-Ch10, Lv47 mandatory / ~Lv55 completionist | 52 | 10,600 | PASS |

Nimera and Ilyra have no boss by current design.

## Tiering rules
- Character Quest bosses are fixed authored encounters; no dynamic player-level scaling.
- They should be materially tougher than ordinary enemies and generally longer than a 2–4-round Elite.
- They should remain below the Regional/Major Hunt tier available around the same unlock window.
- Completionist strength is allowed to shorten the fight substantially.

## Direct-pressure check
Conservative reference uses the no-equipment **Green Arcanist** selected-class body because it is deliberately fragile.

### Post-Ch7 bosses — Lv32 mandatory
- Forecast 260-Power magical single target: ~18.4% Max HP.
- Forecast 185-Power AoE: ~13.1% per target.
- Crest Hammer 260-Power physical: ~18.8%.
- Load-Bearing Test before its protection answer: ~20% baseline, with explicit defensive mitigation when Guard/Barrier is used.

### Old Relay Warden — Lv47 mandatory
- Relay Hammer: ~20.4%.
- Capacitor Arc: ~14.8%.
- Cutoff Sweep: ~14.6% per target.
- Terminal Discharge: ~13.5% per target.

No healthy full-HP one-action deletion is introduced on the conservative reference.

## Architecture result
- Elemental Forecast Construct remains one-bar forecast literacy.
- Crest-Exhausted Warden remains one-bar visible load/protection literacy.
- Black Host Remnant Captain remains one-bar remnant-command pressure.
- Old Relay Warden remains one-bar late relay-security pressure.
- No new second forms, adds, bespoke resources, command prediction, row/grid systems, or retired mechanics are created.

## Closure
> **CHARACTER QUEST BOSS EXACT-SHEET GAP = CLOSED v90**

Next enemy-side work:
1. consolidate approved ordinary formation tables still stranded in older trackers;
2. resolve/record per-action selection logic where the owning kit genuinely lacks it;
3. keep story-owned exact placements bounded rather than inventing dialogue-dependent scene locations;
4. keep runtime-only duration/attrition QA out of the static enemy-design closure.
