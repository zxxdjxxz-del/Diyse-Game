# AGENTS.md — Diyse Engineering Contract

This file governs AI-assisted engineering work in this repository.

## Read first

Before changing gameplay code, read:

1. `docs/ACTIVE_CANON.md`
2. `docs/IMPLEMENTATION_STATUS.md`
3. `docs/authority/CHAPTER_0_REBUILD_V1_40_CHANGE_CONTROL_2026-08-09.md` when touching Chapter 0 or Chapter 1 handoff state
4. the subsystem document relevant to the task
5. `docs/TECHNICAL_PROOF.md` when the task touches architecture proven in Step 7B.5
6. `docs/DIALOGUE_AUTHORING_SCHEMA.md` and `docs/STEP_7C_AUTHORING_TEMPLATE.md` before authoring or integrating production dialogue

If a task conflicts with these files or with a newer explicit user instruction, stop and flag the conflict. Do not silently reinterpret canon.

## Current authority state

- Controlling written authority: **v1.40 Chapter 0 Rebuild Change-Control Overlay**, inheriting all compatible v1.39 authority.
- Immediate predecessor/root baseline: **Clean Active Master Canon v1.39**.
- Technical baseline: **Active Technical Annex v1.39**, plus v1.40 Chapter 0 change-control implementation requirements.
- Recovery checkpoint target: **v1.40 / Audit55**.
- Step 7B.5 technical feasibility: **COMPLETE / PASS on real Android hardware**.
- Step 7B.6 production authoring handoff: **COMPLETE / PASS**.
- Step 7C: **ACTIVE**.
- Rebuilt Chapter 0 S001-S006: **COMPLETE / USER-APPROVED / ACTIVE CANON**.
- Chapter 0 v1.40 Resource replacement and Godot/Android revalidation: **PENDING**.
- C01/C02: retained optional Chapter 0 Character-Life canon.
- Chapter 1 S007-S011 prose: **CANON / PRESERVED**; its separate Resource-conversion gate remains pending.
- Accepted 7B.5 gameplay baseline: `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`.
- Accepted 7B.6 production-handoff implementation merge: `96c6bdc77f39c988f2185634b4e51546f2a0d76b`.

## Chapter 0 supersession warning

The old mandatory Chapter 0 Resources at `game/content/dialogue/chapter_00/S001.tres` through `S006.tres` were validated and merged previously, but their content is **superseded by v1.40**.

Until exact replacement Resources are ready:

- do not treat those files as current dialogue/story authority;
- do not copy their wording into new content;
- do not report their historical Godot/Android PASS as v1.40 validation;
- do not delete them piecemeal before a complete replacement set and validators are ready;
- do not alter C01/C02 unless an actual compatibility requirement exists.

## Step 7C workflow

Use the chapter-level workflow:

- one production branch/PR per chapter or comparable substantial narrative block;
- review and checkpoint each scene before advancing;
- one chapter tracker rather than a new issue/PR for every scene;
- scene-specific validation plus a whole-chapter continuity/repetition/voice/runtime pass;
- full Godot and Android regression at the chapter checkpoint, or earlier only when engine/schema/platform behavior changes;
- one authority/archive checkpoint after the chapter/substantial milestone is complete.

## Hard rules

- This is a fresh Godot/GDScript implementation.
- Do **not** copy, port, import, or mechanically translate code from the older `zxxdjxxz-del/Diyse` repository unless the task explicitly authorizes a named reuse.
- Diyse is 2.5D: real 3D environments/depth/lighting/traversal combined with stylized 2D/2.5D character presentation.
- Diyse has no player dialogue-choice system. Do not create dialogue wheels, response menus, affinity dialogue, tone selections, persuasion trees, or branching player-spoken responses.
- Production dialogue must use the accepted stable-ID Resource schema rather than embedding canon scene text or raw portrait asset paths into generic engine code.
- Step 7C authorization does not permit silent changes to story/system/relationship/final-act canon.
- Combat is **traditional discrete round-based command combat**, not real-time or timeline combat.
- Enemy actions lock from the legitimate beginning-of-round state before unconfirmed player commands exist.
- The player selects one action for every conscious active party member before confirmation.
- Resolution priority is Items first, Defend second, then remaining actions by current effective Speed.
- Speed determines order only and never grants an extra ordinary action.
- Do not implement overwatch, interrupts, reaction commands, real-time interception, threshold bonus turns, or enemy command-reading/retarget cheating.
- Visible intent means an enemy action is already locked; it is not a reaction window.
- Maximum active battle party is four.
- Permanent battle commands are Attack / Ability / Card / Item / Defend.
- MP is the universal ordinary Ability resource. Do not invent character-specific gauges/resources.
- Standard Cards are unlimited-use and data-driven.
- Preserve the accepted automatic hostile retarget rule in `docs/COMBAT_RULES.md` for queued player hostile actions whose original target is defeated before resolution.
- Prime Manifestations use the accepted directly controlled replacement/suspension architecture; do not collapse them into ordinary summons or cinematic one-shots.
- Persistent game state must remain separate from scene nodes and serialize as versioned plain data.
- Do not invent mechanics, terminology, characters, Cards, classes, resources, or story outcomes to fill gaps.
- Keep systems and authored content separate. Prefer data-driven definitions where practical.
- Do not hard-code content records into engine logic merely because a technical proof used placeholders.
- Do not optimize around placeholder assets in a way that prevents final assets from replacing them.
- Do not change canon/specification documents as a side effect of implementing code.

## Chapter 0 implementation locks

- S001 ends at a clean Raider/battle boundary; no free pre-round strike.
- S002 Crossbowman does not fire before its legal round; Shieldbearer gains no new reaction mechanic; Rift Hound Speed changes order only.
- S003 Handler/Hound synergy consumes legal actions; Pursuer intent is locked before player confirmation; reinforcements gain no arrival action; Ilyra remains unidentified until S004.
- S004 Card response is a scripted field event, not a combat reaction or hidden S005 buff.
- S005 Riftmaw uses one HP bar; Restrained -> Unbound occurs between completed rounds without refill/free action; Cornered changes future round weighting only; Handlers never grant extra actions or retarget after lock.
- S006 keeps the object sealed/unidentified, makes Ilyra permanent by her own decision, and hands off to Brackenwall.

## Accepted-proof regression rule

Steps 7B.5 and 7B.6 remain closed architectural proof. The pre-v1.40 Chapter 0 implementation PASS is historical proof of the production pipeline only.

Do not regress proven exploration/dialogue/combat/Card/Prime/persistence architecture while replacing Chapter 0 content. If a newer approved design requires an accepted behavior to change, update the controlling authority and tests deliberately rather than silently bypassing them.

Temporary proof fixtures and superseded scene text are not protected current content.