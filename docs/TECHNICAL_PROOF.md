# Step 7B.5 — Technical Feasibility & Vertical Slice Proof

## Status

**COMPLETE — PASS on real Android hardware.**

Step 7B.5 has finished. Its purpose was to prove that the intended Diyse architecture can grow into the full game before full production dialogue/content work. Every major gate below passed automated validation and real-device acceptance.

This document is an implementation acceptance record, not an open prototype checklist. See the **v1.36 Clean Active Master**, **Active Technical Annex v1.36**, and the Step 7B.5 Technical Feasibility & Android Proof Report v1.0 for current controlling authority and the proof/non-canon distinction.

**Accepted pre-documentation gameplay baseline:** `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`

## 7B.5A — clean 2.5D exploration baseline — PASS

Proven: clean Godot/GDScript implementation independent of the old prototype; real 3D ground/space, lighting and depth; world-space stylized 2D/2.5D character representation; camera/collision; obstacle/depth presentation; reusable field architecture. Graybox field and placeholder character art are non-canon fixtures.

## 7B.5B — touch + Android field proof — PASS

Proven on Android: landscape launch; touch movement including diagonals; shared desktop/mobile movement path; collision; map-edge containment; camera behavior; readable proof controls; repeatable ARM64 debug APK export/install/run. Temporary D-pad/button presentation is not final UI authority.

## 7B.5C — authored dialogue presentation — PASS

Proven: world/proximity-triggered conversation; speaker/text presentation; portrait/expression switching; left/right speaker staging; authored manual progression; silent visual reaction beats; movement/input lock; no player dialogue choices; clean return to exploration. Proof Cyanis/Torren lines and placeholder portraits are disposable and non-canon.

## 7B.5D — real Diyse round combat foundation — PASS

Proven with four active party members and multiple enemies: Attack/Ability/Item/Defend command paths before Card integration; enemy action locking; one selected action per conscious active party member; Item and Defend priority; remaining actions by effective Speed; current tie rules; HP/MP/targeting/KO; victory/reward proof flow; clean return to exploration. Proof enemies/stats/rewards are non-canon.

## 7B.5E — Standard Card + automatic hostile retargeting — PASS

Proven: Card as the fifth permanent command; data-driven Standard Cards; ordinary Speed-ordered resolution; unlimited reuse without charges/Essence/ranks/refresh/use counters; automatic hostile retargeting when the original enemy target was defeated earlier in the round.

### Accepted retarget rule

If a queued player hostile action's original enemy target is defeated before that action resolves, seek the next living enemy in encounter-slot order, wrap to the first living enemy when needed, change only the target, preserve actor/action/cost/priority/Speed, apply to Attack/hostile Abilities/hostile Standard Cards/equivalent direct-control Prime hostile commands unless explicitly overridden, and expose the retarget in presentation/logging.

`Proof Strike` remains a non-canon placeholder Card identity.

## 7B.5F — direct-control Prime Manifestation — PASS

Recovered First Champion was the representative proof because it is Cyanis's current story Prime. The proof validated bearer lock, Card-action selection, successful-use spending, pending state, completion of already-locked ordinary actions before replacement, party suspension, direct Prime control, Prime-only commands, hostile targeting of the Prime, one selected command per Prime round, two-round Recovered duration, frozen party state, normal return and same-battle use consumption.

Temporary flat proof damage is non-canon. Production Prime formulas/effects remain controlled by current technical authority.

## 7B.5G — versioned save/load persistence — PASS

Proven: persistent state separate from scene nodes; versioned plain-data JSON under Godot `user://`; representative area/position, party HP/MP, inventory, Standard Card acquisition, Prime ownership/progression baseline, equipment placeholders, story/world/NPC/interactable flags and XP/gold; immediate load; full Android app close/relaunch + disk load; safe missing/malformed/future-schema behavior.

Mid-round combat/active-Prime serialization was explicitly outside the proof and is not implied as a current requirement.

## Step 7B.6 follow-on — PASS

The production authoring handoff subsequently proved stable-ID `DiyseDialogueSceneDefinition` Resources, `DiyseDialoguePortraitRegistry` indirection, schema validation, Resource-to-DialogueRunner integration, authoring templates, and structural rejection of player-choice/branch fields. Accepted merge: `96c6bdc77f39c988f2185634b4e51546f2a0d76b`.

## Chapter 0 production exercise — PASS / MERGED

Step 7C is now active and Chapter 0 has exercised the accepted architecture as real production dialogue. S001–S006 plus C01/C02 were approved, continuity-reviewed, validated, and merged at `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`.

Final Chapter 0 exact-head gates:
- Godot Smoke Validation run `31296623423`: success.
- Android APK Proof run `31296623417`: success.
- Android artifact ID `9033158865`; artifact ZIP digest `sha256:ae726063592d9845a6b667a8188d28ab4e5ed69177205be35997e6ba104b92c3`.

The Chapter 0 merge did not replace or weaken the accepted Step 7B.5 architecture; the full technical regression suite remained green.

## Regression baseline

The automated tests accumulated through 7B.5 and 7B.6, together with the accepted Chapter 0 production-dialogue/resource/continuity validation, are project regression baselines. Future production should extend rather than bypass them unless a newer approved authority intentionally changes tested behavior.

## Explicit non-canon proof fixtures

Passing the technical proof does not canonize graybox geometry, temporary obstacle/chest presentation, placeholder world sprites/portraits, disposable technical-proof dialogue, Raider proof enemies/stats, `Proof Strike`, temporary flat damage/rewards, proof chest XP/gold, temporary debug/button UI, or other proof-only fixtures.

## Remaining normal production scope

Normal production continues with final maps/art/animation/portraits, final UI/audio/cinematics/performance, full authored production content and implementations, Chapters 1–12 and remaining Character-Life/Hub scenes, broader Android device/performance/lifecycle testing, release signing/build hardening/store packaging, and mid-combat serialization only if later required.

## Production handoff

Step 7B.5 and Step 7B.6 no longer block production. **Step 7C is ACTIVE; Chapter 0 is COMPLETE / MERGED. The next mandatory production block is Chapter 1 S007–S011.**