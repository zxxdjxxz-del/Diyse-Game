# Diyse Dialogue Engine — Repository Authority Packet Compiler

**Status:** ACTIVE IMPLEMENTATION CONTRACT  
**Tool:** `tools/dialogue/compile_scene_authority.py`  
**Input schema:** `diyse_scene_authority_spec_v1`  
**Output authority schema:** `diyse_scene_authority_packet_v1`

## Purpose

The Scene Orchestrator should not be handed a giant undifferentiated repository dump and asked to decide what is current.

The authority compiler creates a deterministic scene request seed from **explicit current owning sources**. It exists to make the current one-canon / authority-precedence rules operational before any model writes a line.

The chain is:

> current repository authority → deterministic compiler → scene authority packet → live gameplay/state merge → Dialogue Director → Person Agents → Editor → Canon Checker → Godot packet

The compiler is not a story writer and does not decide scene content.

## Hard source rules

The compiler accepts current `docs/` authority only.

It rejects as scene authority:
- `docs/90_WORKING/`;
- `docs/99_ARCHIVE/`;
- `docs/03_DIALOGUE/LINE_COMPLETE/` historical transcripts;
- pre-reorganization `docs/chapters/` paths.

A missing requested Markdown heading is a **fatal compile error**. The compiler does not silently widen retrieval to the whole file.

Historical wording may still be consulted manually as provenance where current policy permits, but it is not allowed to leak into the generated authority packet merely because the current source is shorter.

## What is compiled automatically

Every scene packet receives a bounded current guardrail set covering:
- current master authority state;
- authority precedence / no-silent-resurrection rule;
- current party/chapter/combat/Card/economy terminology;
- story → dialogue handoff / cleanup rule;
- global Dialogue Engine regeneration rule;
- critical implementation-facing overrides.

When at least two permanent party members are present, the current permanent-six relationship map is also included automatically.

For each named participant, the compiler packages that participant's current file from `01_CHARACTERS` as a profile source. The profile is still subordinate to the owning domain and is not a second canon copy.

## Scene spec responsibilities

A scene spec must explicitly name:
- `scene_id`;
- `chapter_id`;
- `story_position`;
- participants;
- scene purpose;
- one or more current `02_STORY` source sections;
- any additional current scene-specific authority needed;
- any static scene-context seed that is genuinely established;
- any allowed information transfers;
- any exact-line anchors that are still explicitly preserved;
- maximum beat count and production-cost ceiling.

The compiler does **not** infer an old S### mapping from historical line-complete material. If current story authority has not yet mapped a rewritten lean beat to a specific production scene ID, the spec must not pretend that mapping is closed.

## Exact-line anchors

Exact-line anchors are exceptional.

Every exact-line anchor in a spec must:
1. name a participant speaker;
2. provide the literal required text;
3. cite a **current** `03_DIALOGUE` source/section;
4. appear verbatim in that current source.

If the literal line is absent from the cited current source, compilation fails.

This prevents an old historically locked transcript from becoming exact production dialogue merely because a legacy compiler or test still contains it.

## Runtime-state boundary

Repository compilation cannot know live gameplay state.

The compiler deliberately does not invent:
- current HP/MP or injury state;
- fatigue after the player's actual route;
- recent battle sequence;
- current random-encounter pressure;
- exact field position;
- live map-cell state that can vary at runtime;
- current persistent Person-Agent memory/revision;
- C0–C3 cutscene tier;
- V1–V4 VFX tier.

These must be supplied/merged at scene-build time by the game/orchestration layer when relevant.

## Fingerprints

Every compiled source carries:
- repository path;
- full-file SHA-256;
- selected-section SHA-256;
- selected text.

The final authority packet also carries a deterministic bundle SHA-256. The default request ID contains the first 12 characters of that bundle fingerprint.

This does not make a packet permanent authority. It makes stale packets detectable and reviewable.

## Proof fixture

Current deterministic proof:
> `tests/dialogue/fixtures/authority_ch1_brackenwall_protocol.json`

It intentionally uses:
> `PROOF_CH1_BRACKENWALL_PROTOCOL`

rather than asserting an unresolved current S### mapping.

Validation:
> `python3 tests/dialogue/test_scene_authority_compiler.py`

The test verifies current snapshot derivation, exact section extraction, character routing, relationship inclusion, source fingerprints, archive/working/history rejection, missing-heading failure, and current exact-anchor verification.

## Example usage

From repository root:

```bash
python3 tools/dialogue/compile_scene_authority.py \
  tests/dialogue/fixtures/authority_ch1_brackenwall_protocol.json \
  --output /tmp/ch1_brackenwall_authority.json
```

The resulting `request_seed` is shaped for the current `/v1/scene/build` request. Before production submission, merge live runtime state that the scene actually requires and ensure the Orchestrator deployment uses the same `canon_snapshot_id`.
