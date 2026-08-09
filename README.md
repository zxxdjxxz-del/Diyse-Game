# Diyse-Game

Clean Godot production repository for **Diyse**, a 2.5D, party-based, command-driven turn-based JRPG targeting Android.

This repository is the active implementation line. The older `zxxdjxxz-del/Diyse` repository is historical prototype reference only and is not a code source unless an explicit task authorizes a named reuse.

## Current authority and phase

- Written whole-project authority: **Diyse: 2.5D JRPG Clean Active Master Canon v1.35 — Production Dialogue Authoring Contract and Step 7C Handoff Lock Revision**.
- Technical authority: **Diyse Active Technical Annex v1.35**.
- Dialogue craft/authoring authority: **Diyse Active Dialogue Development Annex v1.2 — Completed Study and Locked Step 7C Authoring Contract Authority**.
- Implementation evidence: **Diyse Step 7B.5 Technical Feasibility & Android Proof Report v1.0** and **Diyse Step 7B.6 Production Handoff Lock Report v1.0**.
- Recovery checkpoint: **v1.35 / Audit47**.

**Step 7B.5 is COMPLETE and PASSED on a real Android device.** The clean Godot architecture has proven 2.5D exploration, authored portrait dialogue, Diyse round combat, unlimited data-driven Standard Cards, direct-control Prime replacement, deterministic hostile retargeting, and versioned save/load persistence across app close/relaunch.

**Step 7B.6 is COMPLETE and PASSED.** Production dialogue now has a stable-ID Resource contract, portrait-registry indirection, schema validation, a generic Resource-to-DialogueRunner adapter, and a Step 7C authoring template. The accepted 7B.6 implementation merge is `96c6bdc77f39c988f2185634b4e51546f2a0d76b`.

**Step 7C remains ON HOLD.** Do not begin full Dialogue-First Scene Writing until the user explicitly authorizes it.

The accepted pre-documentation 7B.5 gameplay baseline is commit `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`. Later documentation/authority commits propagate current status and do not by themselves redefine accepted gameplay behavior.

## Baseline rules

- Engine line: Godot 4.7.x stable; accepted proof target Godot 4.7.1.
- Language: GDScript.
- Platform target: Android, landscape.
- Presentation: 2.5D — 3D environments/depth/lighting/traversal with stylized 2D/2.5D character presentation and illustrated dialogue portraits where appropriate.
- Dialogue: fully authored; no player dialogue choices.
- Production dialogue content: stable-ID `DiyseDialogueSceneDefinition` Resources with `DiyseDialoguePortraitRegistry` asset indirection.
- Combat: discrete round-based command combat.
- Maximum active permanent party: four.
- Permanent commands: Attack / Ability / Card / Item / Defend.
- MP is the universal ordinary Ability resource; no character-specific combat gauges.
- Current Cards: 24 Standard + 12 Prime.
- Standard Cards are unlimited-use.
- If a queued player hostile action's original enemy target is defeated before resolution, it retargets to the next living enemy in encounter-slot order, wrapping when necessary, unless an authored effect explicitly overrides targeting.
- Content architecture should be data-driven wherever practical.
- Do not invent mechanics or silently change canon to make implementation easier.

## Proof-content warning

Passing Steps 7B.5 and 7B.6 validates architecture and accepted behavior, **not** temporary prototype content. Graybox geometry, placeholder sprites/portraits, proof dialogue, `PROOF_SCHEMA`, proof enemies, `Proof Strike`, flat proof damage, temporary rewards, proof flags/cues, and debug UI are non-canon fixtures and must remain replaceable.

See `AGENTS.md`, `docs/ACTIVE_CANON.md`, `docs/IMPLEMENTATION_STATUS.md`, `docs/DIALOGUE_AUTHORING_SCHEMA.md`, `docs/STEP_7C_AUTHORING_TEMPLATE.md`, and the relevant subsystem rules before implementing production content.