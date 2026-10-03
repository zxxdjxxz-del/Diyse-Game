# Automatic Person runtime context

**Status:** implemented canary architecture; no character or story canon changed.

`external-services/canary/runtime_context.py` is the shared deterministic builder used by the authority compiler, Orchestrator, and Person Agent. Authors no longer assemble `person_runtime_contexts`. Every participant receives one, including profile-only and silent participants. The five completed party brains remain unchanged; this does not complete Seyrik's personality pass.

## Construction and authority boundaries

1. The compiler selects exact current owning sections and fingerprints them. It constructs hard identity/context and reads typed scene assertions, without semantic search or an LLM.
2. Godot preserves `context_construction` and the authority packet while adding curated runtime observations. Live observations cannot grant memory access or overwrite canonical facts.
3. The Orchestrator builds the static contexts, reads persistent revisions, and asks each persistent agent's `/v1/runtime-context` endpoint to reconstruct its own authorized continuity.
4. The Person Agent checks ownership, privacy, approval provenance, canon snapshot, chronology, and policy **before** salience. All legal effects contribute to reconstruction; only optional recollections face the salience budget.
5. Each `/v1/turn` rebuilds from those protected inputs and its own database. Cached `person_runtime_context` contents and the latest unsliced `current_state` are not authority. A changed story revision aborts the build rather than mixing snapshots.
6. The Director/Editor/Checker receive author-facing authority. Person models receive only their constructed context, current observable exchange, their authorized recollections, and their brain/shared behavioral rules. Full story source packets, other people's contexts, and raw continuity indexes are excluded from Person prompts.
7. A build performs no writes. Both commit endpoints require PASS and explicit author approval; expected revisions and idempotent commit IDs remain enforced.

Hard context is never ranked for relevance. Current scene ID, exact supplied story position, participant list, canon snapshot, source fingerprints, stable identity bullets, class labels (reference only, **not** proof of unlock), and a named equipment identity firewall are injected. Recruitment, unlocks, equipment restrictions, reveal gates, and other unresolved hard fields remain explicitly unknown when authority has not established them in a machine-readable form.

## Authoring inputs

Existing specs without new metadata still compile and produce conservative contexts. They do not receive persistent memory by default.

Optional spec fields:

```json
{
  "story_clock": {"chapter": 8, "sequence": 10},
  "forward_only": false,
  "continuity_policy": {
    "mode": "scene_ids",
    "authorized_scene_ids": ["PRIOR_SCENE"]
  }
}
```

These IDs and numbers are illustrative, not newly assigned DIYSE chronology. `sequence` is an explicitly authored ordering within the chapter; scene names, prose, wall-clock timestamps, and commit order are never guessed into a chronology. The chapter must match `chapter_id`.

Supported policies:

| Mode | Additional requirement |
| --- | --- |
| `none` | Default; no persistent story memories |
| `explicit_ids` | `authorized_memory_ids`; all other gates still apply |
| `scene_ids` | `authorized_scene_ids`; all other gates still apply |
| `all_committed_story` | Explicit `forward_only: true` and an exact `story_clock`; future/equal-position records remain forbidden |

For legacy records without a sortable clock, `prior_scene_ids` can explicitly assert that an otherwise authorized source scene precedes this one. This does not override a known future chapter/position. It does not order two prior scenes relative to one another: conflicting values without comparable chronology remain unknown.

A per-person policy can still be supplied as `person_runtime_contexts.<id>.memory_authorization`; the compiler moves it into the protected construction plan. Other manually populated runtime state is rejected with a migration error, because it lacks reproducible source/chronology provenance.

## Typed authority, authored once

An exact selected `02_STORY` section may contain a fenced `diyse-context` block with a JSON list of assertions. The compiler discovers the block automatically whenever that owning section is selected. Alternatively, a spec can provide `context_assertions`, each with a current `source` selector and a verbatim `source_quote`; the compiler verifies and fingerprints the quote. Missing quotes, malformed assertions, and duplicate IDs fail compilation.

An assertion has `id`, `owner_id`, `kind`, `key`, `value`, plus kind-specific metadata. Ownership is explicit: an assertion for one person does not become shared merely because others are present. `forbidden_reveals` topic IDs are also injected as disclosure restrictions; they do not incorrectly imply that the owner is ignorant of their own private history. The author is responsible for the semantic interpretation and scene applicability of an annotation; matching a quote proves provenance, not arbitrary natural-language entailment.

| Kind | Shape and treatment |
| --- | --- |
| `hard` | Supported hard field such as `recruitment_status`, `unlock_state`, `equipment_restrictions`, or `knowledge_gates` |
| `relationship` | `target_id` plus one named dimension; directed and limited to people present |
| `epistemic` | Topic key plus explicit `status`; unknown/forbidden answers are redacted |
| `thread` | Stable thread key and `status: open` or `resolved` |
| `local` | Wants, avoidances, assigned task, attention, participation, discussion boundaries, or expression channel |
| `physical`, `emotional` | Established state only; never inferred from personality or lack of data |

Illustrative assertion, **not canon**:

```json
{
  "id": "example-task",
  "owner_id": "ilyra",
  "kind": "local",
  "key": "current_task",
  "value": "return a borrowed item"
}
```

The builder may propose attending to that assigned task, labeled `inference` and nonpersistent. It does not turn permanent compassion into a scene motive. Multiple wants and avoidances survive together with `motive_resolution: open`. Attention to an open thread does not impose an obligation to speak. Missing willingness to speak is `undecided`, not automatically true. Explicit `silent` or `nonparticipating` blocks speech and skips unnecessary Person-model calls; an Editor violation forces local FAIL.

Private appraisal, visible behavior, spoken expression, and withheld content have distinct fields. No expression is automatically copied into another channel.

## Committed continuity effects

Canon Checker proposals may include typed `context_effects` inside each durable memory. Effects use the same kind/key/value structure as assertions, except persistent memory cannot change hard canon. Each relationship dimension advances only when its own earned delta is approved. Trust never grants disclosure, affectionate insult, profanity, touch, or familial shorthand.

The committing Person service stamps the actual owner, scene ID, supplied `source_story_clock`, canon snapshot, and `{canon_check_status: PASS, author_approved: true}` provenance. It defaults new person-local memories to private. A shared visibility declaration also requires this owner in its explicit audience; it never grants access to a different person's database. Legitimate information transfer needs a separately approved recipient-owned acquisition record.

Corrections are new events for the same epistemic topic; old events are not overwritten. The builder reconstructs the status at the requested scene position and preserves prior beliefs separately. A high-salience mistake cannot erase a low-salience correction: state reconstruction precedes salience selection, and recollections carry their as-of epistemic view.

The ten states are retained: `known_fact`, `direct_observation`, `trusted_report`, `heard_claim`, `inference`, `suspicion`, `assumption`, `misunderstanding`, `unknown`, and `forbidden_future`. Confidence and repetition do not promote status. Forbidden answer text is never sent to the person, including through an otherwise authorized memory effect.

Thread closures remove only the named open thread at the applicable position. Transient local, physical, and emotional memory effects require `applies_to_scene_ids`; otherwise they do not carry forward. This deliberately avoids inventing the duration of injury, fatigue, anger, or a scene-local desire.

## Migration and limitations

- Existing prose is not semantically mined into facts, motives, permissions, or relationships. Current structured assertions/effects are needed where identity and existing scene metadata cannot safely establish the state. Unresolved dependencies are returned for author review; no missing state is silently filled.
- Existing memories without owner/visibility/approval/canon provenance remain unavailable. Migration requires verification and explicit approval, not a blanket trust upgrade. No existing database is rewritten by this change.
- Cross-canon-snapshot memory is denied until reviewed. Deployment snapshot IDs must be updated when authority changes; hashes detect altered bundles, not a newer repository the deployed service has never received.
- Free-form conversations are not mined into structured continuity. Checker proposals and author approval remain necessary. Current in-scene speech is observable evidence, not an automatic known-fact update.
- Salience is intentionally simple (stored practical/emotional importance, deterministic ID tie-break, twelve recollections). Character-specific retrieval ranking remains future work; it cannot widen access.
- Semantic dialogue correctness, source interpretation, and whether an earned delta deserves approval still require the Canon Checker and author. Authenticated commit callers attest PASS/approval; this is not a signed reviewer-receipt system.
- Cross-person commits retain the existing independent revision checks and are not a distributed atomic transaction. This change adds no deployment or production save integration.

## Verification

Run `python tests/dialogue/test_automatic_person_context.py`, the existing compiler/runtime-contract/magic-context Python tests, and the Godot dialogue smoke tests. The new suite covers historical rewrites, private ownership, independent relationship dimensions, belief correction, default denial, explicit forward continuity, silent participation, conflicting motives, stale future injection, Ilyra/Seyrik safe refusal, Torren/Nimera familial chronology, provenance, read-only construction, and commit gates. It runs without external services or paid model calls.

Validation on the implementation branch against starting commit `742a2964`:
- all 28 automatic-context tests passed; existing compiler, runtime-contract, and magic/Card Python gates passed;
- current dialogue mirror and player-facing world-intro synchronization checks passed;
- Godot 4.7.1 imported successfully; 36 of 42 `validate_*.gd` scripts passed, including the changed context builder and its request assembly/preview/client integrations;
- all six failing scripts produced matching errors on an untouched worktree of the starting commit: `validate_chapter_01_resources.gd`, `validate_chapter_03_resources.gd`, `validate_dialogue_field_bridge.gd`, `validate_audit98_encounters.gd`, `validate_hd2d_runtime.gd`, and `validate_save_load.gd`. These involve historical resources, a retired walking-dialogue expectation, encounter fixtures, and typed-array assignment errors. No tests were relaxed to conceal them.
