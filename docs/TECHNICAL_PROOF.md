# Step 7B.5 — Technical Feasibility & Vertical Slice Proof

## Status

**COMPLETE — PASS on real Android hardware.**

Step 7B.5 has finished. Its purpose was to prove that the intended Diyse architecture can grow into the full game before full Step 7C dialogue-first scene writing begins. Every major gate below passed automated validation and real-device acceptance.

This document is now an implementation acceptance record, not an open prototype checklist. See the v1.34 Clean Active Master, Active Technical Annex v1.34, and the Step 7B.5 Technical Feasibility & Android Proof Report v1.0 for controlling authority and the proof/non-canon distinction.

**Accepted pre-documentation gameplay baseline:** `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`

## 7B.5A — clean 2.5D exploration baseline — PASS

Proven:

- clean Godot/GDScript implementation independent of the old prototype;
- real 3D ground/space, lighting and depth;
- world-space stylized 2D/2.5D character representation;
- camera and collision;
- obstacle/depth presentation;
- reusable field architecture.

The graybox field and placeholder character art are non-canon fixtures.

## 7B.5B — touch + Android field proof — PASS

Proven on Android:

- landscape launch;
- touch movement including diagonals;
- shared desktop/mobile movement path;
- collision;
- map-edge containment;
- camera behavior;
- readable proof controls;
- repeatable ARM64 debug APK export/install/run.

The temporary D-pad/button presentation is not final UI authority.

## 7B.5C — authored dialogue presentation — PASS

Proven:

- world/proximity-triggered conversation;
- speaker and text presentation;
- portrait/expression switching;
- left/right speaker staging;
- authored manual progression;
- silent visual reaction beat with no spoken line;
- movement/input lock while dialogue owns control;
- no player dialogue choices;
- clean return to exploration.

The proof Cyanis/Torren lines and placeholder portraits are disposable and non-canon.

## 7B.5D — real Diyse round combat foundation — PASS

Proven with four active party members and multiple enemies:

- Attack / Ability / Item / Defend command paths before Card integration;
- enemy action locking before player confirmation;
- one selected action for each conscious active party member before round confirmation;
- Item priority first;
- Defend priority second;
- remaining actions by current effective Speed;
- party-over-enemy exact Speed ties;
- player-selected tied-party order;
- stable deterministic tied-enemy order;
- HP, MP, targeting and KO;
- victory/rewards proof flow;
- clean return to exploration.

Proof enemies/stats and temporary rewards are non-canon.

## 7B.5E — Standard Card + automatic hostile retargeting — PASS

Proven:

- Card becomes the fifth permanent command, yielding Attack / Ability / Card / Item / Defend;
- Standard Card definitions can be data-driven;
- Standard Cards use the ordinary Speed-ordered resolver;
- unlimited reuse works without charges, Essence, ranks, refresh counters or use counters;
- hostile actions automatically retarget when their original enemy target was defeated earlier in the same round.

### Accepted retarget rule

If a queued player hostile action's original enemy target is defeated before that action resolves:

1. Seek the next living enemy in encounter-slot order after the original target.
2. If no later slot is living, wrap to the first living enemy.
3. Change only the target. Do not change actor, action identity, cost, priority tier or Speed.
4. Apply the behavior to Attack, hostile/damaging Abilities, hostile Standard Cards, and equivalent directly controlled Prime hostile commands unless an authored effect explicitly overrides targeting.
5. Expose the retarget in combat presentation/logging.

`Proof Strike` is a non-canon placeholder Card identity.

## 7B.5F — direct-control Prime Manifestation — PASS

Recovered First Champion was used as the representative proof because it is Cyanis's current story Prime.

Proven:

- bearer lock;
- Prime selection through the bearer Card action;
- use is spent on successful manifestation rather than merely opening/queueing the option;
- activation resolves within the ordinary round and establishes the approved pending state;
- already locked ordinary actions finish before party replacement;
- active party suspension occurs at the correct end-of-round boundary;
- Prime becomes the directly controlled active player combatant;
- enemies target the Prime while the party is suspended;
- only the Prime's printed command set is presented, not universal party commands;
- one selected Prime command per Prime round;
- Recovered duration of two Prime action rounds;
- frozen party HP/MP state during suspension;
- normal Prime exit and party restoration;
- same-battle use consumption.

Temporary flat damage used by the proof is non-canon. The production Prime formulas/effects remain controlled by the active technical authority.

## 7B.5G — versioned save/load persistence — PASS

Proven:

- persistent game/session state is separate from scene nodes;
- versioned plain-data JSON serialization under Godot `user://`;
- representative area and Cyanis position persistence;
- representative party HP/MP records;
- inventory;
- Standard Card acquisition;
- Prime ownership/progression baseline;
- equipment placeholders;
- story/world/NPC/interactable flags;
- XP/gold proof data;
- immediate LOAD restoration in the running app;
- full Android app close/relaunch followed by disk LOAD restoration;
- safe handling of missing saves;
- safe handling of malformed JSON;
- safe rejection of unsupported future schema versions.

Mid-round combat/active-Prime serialization was explicitly out of scope and is not implied as a current requirement.

## Regression baseline

The automated tests accumulated through 7B.5 are now the accepted implementation regression baseline. Future production work should extend the architecture while keeping these tests green unless a newer approved authority intentionally changes the tested behavior.

## Explicit non-canon proof fixtures

Passing the technical proof does not canonize:

- graybox field geometry and temporary obstacle/chest presentation;
- placeholder Cyanis/Torren world sprites or portraits;
- disposable technical-proof dialogue;
- Raider proof enemies and temporary stats;
- `Proof Strike`;
- temporary flat damage values;
- temporary 30 XP / 42 gold combat rewards or proof chest XP/gold;
- temporary debug/button UI.

## Remaining normal production scope

Not required to pass 7B.5 and still to be built/polished as production proceeds:

- final maps, character/world art, animation and complete portrait sets;
- final UI/audio/cinematics and performance optimization;
- full production combat formulas/content data;
- all authored Abilities/equipment/enemies/encounters;
- all 24 Standard Cards and all 12 Prime implementations;
- complete Chapter 0–12 content and Character-Life scenes;
- broader Android device/performance/lifecycle stress testing;
- release signing/build hardening/store packaging;
- mid-combat save serialization only if later required.

## Production handoff

Step 7B.5 no longer blocks production on feasibility grounds. The dialogue study is also complete.

**Step 7C remains procedurally ON HOLD until the user explicitly authorizes full Dialogue-First Scene Writing.** A technical PASS does not itself constitute that authorization.