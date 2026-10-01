# Diyse — Mandatory Story Scene-ID Index

**Status:** ACTIVE STORY SCENE-ID ROUTING INDEX  
**Authority:** current chapter masters plus current Dialogue/runtime manifests; historical S### IDs are provenance only where explicitly marked.  
**Domain rule:**** this folder owns mandatory story structure, chapter purpose, scene order, reveal order, recruitment/Prime milestones, interchapter causality, and story-state outcomes. Exact spoken dialogue belongs in `03_DIALOGUE`; battle numbers in `09_ENEMIES_AND_ENCOUNTERS`; progression numbers in `10_PROGRESSION_AND_EXP`.

## Scene-ID rule after Dialogue Engine restructuring

Scene-ID status is chapter-specific.

- **Chapters 0–3:** the live generated runtime mirror already uses the current B/C production IDs. Earlier S### ranges are historical/provenance identifiers only and are not live runtime routing.
- **Chapter 4:** current production authority uses B01–B12 scene specs, but exact current runtime dialogue has not yet been promoted; legacy S022–S026 material remains proof/compatibility provenance only.
- **Later chapters:** retain only the S### anchors explicitly listed below until their current dialogue/runtime migrations are authored.

Current all-dialogue regeneration/experiment authority applies:
- current `02_STORY` structure owns what each scene function must accomplish;
- `03_DIALOGUE` owns generated/approved spoken wording;
- historical line-complete dialogue is reference/provenance only unless an individual exact line is explicitly preserved by current authority;
- for Chapters 0–3, `game/content/dialogue/current/manifest.json` is the implementation routing manifest and retired S### IDs must not be reconstructed as live dependencies.

| Chapter | Mandatory scene IDs | Current routing status |
|---|---|---|
| Ch0 | **B01–B07** | **current mandatory production/runtime IDs; optional Character-Life C01 is also live** |
| Ch1 | **B01–B12** | **current mandatory production/runtime IDs; Character-Life C02–C04 are also live** |
| Ch2 | **B01–B15** | **current mandatory production/runtime IDs; Character-Life C05 is also live** |
| Ch3 | **B01–B11** | **current mandatory production/runtime IDs; Character-Life C06–C07 are also live** |
| Ch4 | S022–S026 | **legacy implementation-compatibility IDs only; current production uses B01–B12, and no one-to-one S### → B## mapping should be inferred until an explicit runtime migration is authored** |
| Ch5 | current detailed S-range not promoted here | beat/macro authority |
| Ch6 | includes S035 / S036 inherited anchors | macro/beat authority |
| Ch7 | current detailed S-range not promoted here | macro authority |
| Ch8 | current detailed S-range not promoted here | macro authority |
| Ch9 | S047–S050 | macro locked |
| Ch10 | S051–S061 | detailed story skeleton locked |
| Ch11 | S062–S065 | macro locked |
| Ch12 | S066–S069 | macro locked; reciprocal-pair resolution beats have no standalone S### IDs |
| Ch13 | S070–S073 | macro locked |

## Current Chapter-0 routing clarification

Current completed Chapter-0 production and runtime structure is:

> **B01 → B02 → B03 → B04 → B05 → B06 → B07 → optional C01 — Six Minutes**

Current functions:
- **B01** — Convoy / Opening Ambush;
- **B02** — Wreck Field;
- **B03** — Evacuation Relay Decision;
- **B04** — Field Triage Camp / Ilyra / First Incomplete Response;
- **B05** — Concealed Ruin Vanguard;
- **B06** — **Riftmaw + Battle Sorcerer / Final Broken Convoy Confrontation**;
- **B07** — Aftermath / Survivor Recovery / Overnight Camp;
- **C01** — `Six Minutes` optional Character-Life scene.

The generated game-facing mirror under `game/content/dialogue/current/chapter_00/` uses these B/C slot IDs now. Former P01–P07 and S001–S006 references are historical/provenance identifiers only; there is no pending Chapter-0 runtime-ID migration.

## Current Chapter-10 scene sequence
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

## Current Chapter-11 sequence
- S062 — The Living Anchor
- S063 — The Custodian
- S064 — The Truth Beneath the Empire
- S065 — First Reckoning

## Current Chapter-12 sequence
- S066 — Into the Imperial Heartland
- S067 — The March That Refuses Empire Logic
- S068 — Varkesh Taken Alive
- S069 — Emperor Vaelkor Draeven

## Current Chapter-13 sequence
- S070 — The Deepest City
- S071 — The Reconstituted Entity
- S072 — No One Is Last Command
- S073 — Last Command

Do not reuse the pre-insertion S051–S062 numbering for old late-game material.
