# Diyse — Mandatory Story Scene-ID Index
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, read through all later explicit user corrections and current domain migrations.  
**Primary story authorities:** current chapter index; current lean chapter structures; Audits 91/92/107/109/112/113; current Chapter-11/12/13 operational projections; current Prime/character/world corrections.  
**Domain rule:** this folder owns mandatory story structure, chapter purpose, scene order, reveal order, recruitment/Prime milestones, interchapter causality, and story-state outcomes. Exact spoken dialogue belongs in `03_DIALOGUE`; battle numbers in `09_ENEMIES_AND_ENCOUNTERS`; progression numbers in `10_PROGRESSION_AND_EXP`.

## Scene-ID rule after Dialogue Engine restructuring

A retained S### range identifies stable legacy **scene-routing IDs** still present in current implementation resources. It does **not** mean the historical exact transcript remains current wording, and it does not override a newer completed chapter manuscript/structure.

Current all-dialogue regeneration/experiment authority applies:
- current `02_STORY` structure owns what each scene function must accomplish;
- `03_DIALOGUE` owns generated/approved spoken wording;
- historical line-complete dialogue is reference/provenance only unless an individual exact line is explicitly preserved by current authority;
- when a newer production manuscript uses different scene labels, those labels may coexist with legacy runtime S### IDs until an explicit implementation migration rewires Resources/tests.

| Chapter | Mandatory scene IDs | Current routing status |
|---|---|---|
| Ch0 | **Production manuscript: P01–P07; legacy runtime Resources: S001–S006** | **P01–P07 current structure; S001–S006 remain implementation-compatibility IDs pending migration** |
| Ch1 | S007–S011 | **IDs retained; current lean structure controls; detailed beat→S### routing requires current mapping where not explicit** |
| Ch2 | S012–S016 | **IDs retained; current lean structure/dialogue regeneration controls** |
| Ch3 | S017–S021 | **IDs retained; current lean structure/dialogue regeneration controls** |
| Ch4 | S022–S026 | **IDs retained; current lean structure + four-element overlay control** |
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

Current completed Chapter-0 production structure is:

> **P01 → P02 → P03 → P04 → P05 → P06 → P07 → optional C01 — Six Minutes**

Current functions:
- **P01** — Convoy / Opening Ambush;
- **P02** — Wreck Field;
- **P03** — Evacuation Relay Decision;
- **P04** — Field Triage Camp / Ilyra / First Incomplete Response;
- **P05** — Concealed Ruin Vanguard;
- **P06** — **Riftmaw + Convoy War-Sorcerer / Final Broken Convoy Confrontation**;
- **P07** — Aftermath / Survivor Recovery / Overnight Camp;
- **C01** — `Six Minutes` optional Character-Life scene.

The former current-repo eight-beat split in which Riftmaw was a separate mandatory encounter before a later War-Sorcerer confrontation is superseded. **Riftmaw and the Convoy War-Sorcerer are fought together in P06.**

### Legacy S### implementation compatibility
Existing Chapter-0 `.tres` Resources and tests still use S001–S006. Those IDs are **not** being silently remapped in this document because doing so would guess a production migration that has not yet been implemented.

Until the Chapter-0 Resource migration is explicitly performed:
- treat P01–P07 as the current story/manuscript structure;
- treat S001–S006 as legacy implementation-routing IDs only;
- do not infer that old S004→S005 or old S005 combat content remains story-correct;
- any Dialogue Engine experiment should use P01–P07 story functions rather than the obsolete eight-beat split.

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
