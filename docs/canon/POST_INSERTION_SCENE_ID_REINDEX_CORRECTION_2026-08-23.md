# Post-Insertion Scene-ID Reindex Correction — 2026-08-23

**Status:** CURRENT / CONTROLLING SCENE-NUMBER OVERLAY  
**Applies under:** v1.98 / Audit113 and v1.97 / Audit112  
**Scope:** global mandatory-story `S###` numbering from the end of Chapter 9 through the finale after insertion of Chapter 10 — The Last Blank.

## Why this correction exists

Audit113 corrected the late-game **chapter numbers** after Chapter 10 — The Last Blank was inserted, but the global mandatory-story scene sequence also requires a corresponding reindex.

Chapter 9 already ends at **S050 — Mercy Is Not Surrender**.

Audit112 then locks eleven new Chapter-10 story-skeleton scenes:

- S051 — The Missing Middle
- S052 — East of Cerythvale
- S053 — The Old Road
- S054 — Another Wayfinder
- S055 — What the Crown Did Here
- S056 — The Prime Research
- S057 — The Convoy
- S058 — Real Pieces
- S059 — Where They Stopped
- S060 — Beyond the Excavation
- S061 — The Order That Was Missing

Therefore the pre-insertion late-game scene IDs that formerly occupied S051–S062 cannot remain current. Every retained pre-insertion mandatory-story scene after S050 shifts forward by **+11**.

## Current late-game scene sequence — controlling

### Chapter 9 — unchanged
- S047 — Equal Mercy
- S048 — Last Sanctuary
- S049 — Crownfall invasion / current final title still separately governed
- S050 — Mercy Is Not Surrender

### Chapter 10 — The Last Blank
- S051 — The Missing Middle
- S052 — East of Cerythvale
- S053 — The Old Road
- S054 — Another Wayfinder
- S055 — What the Crown Did Here
- S056 — The Prime Research
- S057 — The Convoy
- S058 — Real Pieces
- S059 — Where They Stopped
- S060 — Beyond the Excavation
- S061 — The Order That Was Missing

### Chapter 11 — Crown Engine / Calder / Custodian / Truth
Pre-insertion old Chapter-10 scene skeleton, shifted +11:
- **S062 — The Living Anchor** (formerly S051)
- **S063 — The Custodian** (formerly S052)
- **S064 — The Truth Beneath the Empire** (formerly S053)
- **S065 — First Reckoning** (formerly S054)

### Chapter 12 — The Reforged March
Pre-insertion old Chapter-11 scene skeleton, shifted +11:
- **S066 — Into the Imperial Heartland** (formerly S055; supersedes older title `Into the Heartland`)
- **S067 — The March That Refuses Empire Logic** (formerly S056)
- **S068 — Varkesh Taken Alive** (formerly S057)
- **S069 — Emperor Vaelkor Draeven** (formerly S058)

### Chapter 13 — The Last Command
Pre-insertion old Chapter-12 scene skeleton, shifted +11:
- **S070 — The Deepest City** (formerly S059; supersedes older title `The Ancient Blind Region`)
- **S071 — The Reconstituted Entity** (formerly S060)
- **S072 — No One Is Last Command** (formerly S061)
- **S073 — Last Command** (formerly S062)

## Exact old-to-current mapping

| Pre-insertion ID | Current ID | Current scene title |
|---|---|---|
| S051 | S062 | The Living Anchor |
| S052 | S063 | The Custodian |
| S053 | S064 | The Truth Beneath the Empire |
| S054 | S065 | First Reckoning |
| S055 | S066 | Into the Imperial Heartland |
| S056 | S067 | The March That Refuses Empire Logic |
| S057 | S068 | Varkesh Taken Alive |
| S058 | S069 | Emperor Vaelkor Draeven |
| S059 | S070 | The Deepest City |
| S060 | S071 | The Reconstituted Entity |
| S061 | S072 | No One Is Last Command |
| S062 | S073 | Last Command |

## Synthesis-resolution beat boundary

The three mandatory late-Chapter-12 Synthesis-resolution beats remain locked in function and placement:

- What Holds, What Changes
- Keep Them Alive
- Enough to Move

They were **not previously assigned standalone `S###` IDs**. This correction does not invent new IDs for them.

Until detailed Chapter-12 scene production explicitly determines otherwise, they remain mandatory authored beats within the late-Chapter-12 structure and do not alter the S066–S069 macro-scene numbering above.

If later production deliberately promotes one or more of those beats into standalone mandatory `S###` scenes, that must be handled through explicit scene-number change control so every downstream current ID remains unique and chronological.

## Other ID families

This correction affects the global mandatory-story `S###` sequence only.

It does not renumber:
- `C##` camp / Character-Life scenes;
- `H##` Hunt/optional encounter identifiers;
- Chapter acceptance IDs such as `CH12-A001`;
- Regional Hunt numbers;
- stable implementation IDs that are not player-facing scene numbers.

## Historical-reference rule

Historical canon/audit files may retain their original pre-insertion scene IDs for provenance, but those IDs are not current implementation authority.

Any current-facing reference to an old post-S050 late-game scene ID must use the mapping above.

In particular:
- old S055 `Into the Heartland` / `Into the Imperial Heartland` → current **S066 — Into the Imperial Heartland**;
- old S059 `The Ancient Blind Region` → current **S070 — The Deepest City**;
- old S060 `The Reconstituted Entity` → current **S071**;
- old S061 `No One Is Last Command` → current **S072**;
- old S062 `Last Command` → current **S073**.

## Current global continuity firewall

The mandatory-story scene sequence now runs continuously through the insertion:

**... S047 → S048 → S049 → S050 → S051 ... S061 → S062 ... S073**

No current late-game scene may reuse S051–S061 for pre-insertion material, because those IDs now belong to Chapter 10 — The Last Blank.
