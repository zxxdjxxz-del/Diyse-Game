# Diyse Chapter 0 Rebuild — v1.40 Change Control

**Approval date:** August 9, 2026  
**Approval time:** 11:40 PM America/Chicago  
**Status:** ACTIVE CANON CHANGE CONTROL  
**Authority result:** v1.40 controlling overlay over Clean Active Master v1.39  
**Recovery checkpoint target:** v1.40 / Audit55

## 1. Authority result

The user explicitly approved the rebuilt Chapter 0, **The Broken Convoy**, S001-S006. This approval reopens Chapter 0 under the explicit-change-control clause and supersedes the prior Chapter 0 mandatory-scene wording, staging, encounter handoffs, and runtime assumptions wherever they conflict.

v1.40 is intentionally a controlling overlay over v1.39 rather than a reconstructed full-master replacement. All compatible v1.39 and earlier canon remains inherited unless this document directly changes it.

The following remain unchanged and controlling:

- Chapter 1 S007-S011 canon production wording under v1.39;
- S007 opening state Cyanis + Ilyra, with Maevra temporary-playable by the end of S007;
- Torren permanent recruitment by the end of S009;
- S010 as the first sustained four-commandable-character Chapter 1 field leg;
- S011 six-Face operational framing and Dunmere lead;
- First Champion remains unidentified through Chapter 1;
- C01 **The Fire Is Too Close** and C02 **Food After Triage** remain optional post-S006 Character-Life scenes unless separately changed.

## 2. Superseded Chapter 0 implementation

The previous Chapter 0 Resource merge at `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5` remains historical implementation evidence only for S001-S006 after this change control.

The existing repository Resources:

- `game/content/dialogue/chapter_00/S001.tres`
- `game/content/dialogue/chapter_00/S002.tres`
- `game/content/dialogue/chapter_00/S003.tres`
- `game/content/dialogue/chapter_00/S004.tres`
- `game/content/dialogue/chapter_00/S005.tres`
- `game/content/dialogue/chapter_00/S006.tres`

must not be treated as current Chapter 0 content authority until they are replaced by exact serialization of the newly approved rebuild and revalidated.

C01 and C02 are **not** superseded by this change control. Their optional status and nonessential story function remain active.

The old Chapter 0 Godot/Android PASS proves the production dialogue architecture and validation pipeline, but it does **not** validate the v1.40 replacement text or encounter integration.

## 3. Chapter 0 runtime and encounter target

Mandatory Chapter 0 target: approximately **55 minutes**, with a working implementation range of approximately **52-57 minutes** depending chiefly on battle and exploration pace.

Chapter 0 uses approximately seven meaningful authored/tutorial encounters and **does not use the normal random-encounter rhythm**. Normal hostile random encounters begin in Chapter 1.

Approved encounter progression:

1. Black Host Raider — basic discrete-round grammar.
2. Raider + Crossbowman — multiple differentiated threats.
3. Ruin Shieldbearer + Raider — target-value / defender-role decisions.
4. Convoy Rift Hound + Raider — effective-Speed pressure; Speed changes order only.
5. Beast Handler + Rift Hound — complementary enemy support actions.
6. Ruin Vanguard Pursuer — visible locked intent and objective planning.
7. Riftmaw War Beast + two Beast Handlers — first major Cyanis + Ilyra whole-party planning encounter and synthesis of the previous lessons.

## 4. Combat-system lock

Every Chapter 0 battle must use Diyse's established discrete-round rules:

1. At the beginning of a round, each conscious enemy locks one legal action from the legitimate beginning-of-round state.
2. Enemy AI does not read or react to unconfirmed player commands.
3. The player selects one action for every conscious active party member before party confirmation.
4. Item actions resolve first.
5. Defend actions resolve second.
6. Remaining actions resolve by current effective Speed.
7. Speed changes resolution order only and never grants an additional ordinary action.
8. No overwatch, interrupts, reaction commands, real-time interception, hidden bonus turns, or mid-resolution retarget cheating may be introduced.

Visible enemy intent represents an **already-locked action**. It is information available before confirmation, not a reaction window.

Reinforcements that enter during a round receive no ordinary action until the following round unless a separately approved universal rule explicitly says otherwise.

## 5. S001 — Opening

S001 establishes Cyanis through ordinary convoy work and observation before any supernatural event.

Locked boundaries:

- Ilyra is absent.
- The sealed recovery object is cargo, not chosen-one spectacle.
- No pursuit refusal occurs.
- No Card response occurs.
- Ordinary convoy life and small work-context humor precede the ambush.
- Cyanis notices the absence of expected return traffic without claiming certainty about the cause.
- The ambush separates Cyanis toward the east-side civilian route.
- Cyanis performs immediate survivor/civilian work before combat.
- The ending Raider appears as a threat, but neither side receives a free combat action before Battle 1 initializes.
- Neutral seal language replaces any incidental early use of the color green that could falsely prime the later green-and-gold response.

S001 ends at the clean battle boundary: Raider visible; Cyanis ready; Battle 1 initializes; Round 1 begins normally.

## 6. S002 — Wreck Field

S002 is player-led rescue, traversal, battlefield reading, and four authored tutorial battles.

Locked boundaries:

- Battle 2 Crossbowman may be visibly aimed before combat but does not fire a free pre-battle shot.
- Shieldbearer protection uses only legal selected actions or already-established universal passives; no spontaneous intercept/reaction mechanic is introduced.
- Rift Hound high Speed changes action order only and never action quantity.
- Player rescues survivors, opens safe movement routes, and reads unstable wreckage.
- The moved wagon, impact pattern, relatively clean north route, and genuine northward retreat tracks are observable evidence.
- Cyanis does not decide the pursuit question here.
- S002 ends with evidence complete and the report still owed to the officer.

## 7. S003 — Evacuation Relay Decision

S003 owns the pursuit decision.

Cyanis refuses immediate pursuit professionally because:

- wounded and civilians remain exposed;
- fighting personnel are also carrying and moving casualties;
- the damaged force cannot safely chase while holding the field, recovery cargo, and survivor routes;
- the north route is suspiciously easy to follow, but Cyanis explicitly does **not** claim certainty that it is bait.

The superior officer remains credible, challenges Cyanis's reasoning, and accepts the executable alternative when the field evidence supports it.

Combat locks:

- Handler + Hound support uses separate legal one-action-per-unit round behavior.
- A 60-90 second player-controlled stabilization window separates Handler/Hound from the Pursuer miniboss.
- Pursuer visible intent is locked before player command confirmation and may not dynamically switch after reading Cyanis's choice.
- Limited reinforcements, if retained, enter on legal round timing and receive no arrival bonus action.

Ilyra is **not** clearly shown or heard in S003. S003 may establish that organized medical work has formed, but S004 owns her first identifiable appearance and spoken line.

## 8. S004 — Field Triage Camp

S004 opens with Ilyra already doing the work. Her first clear line remains:

> Walking wounded, blue cloth. If you can answer clearly, help somebody who can't.

Her first relationship with Cyanis is professional jurisdictional cooperation, not romantic framing.

Protected principles and beats:

- Cyanis controls tactical access/security decisions; Ilyra controls medical safety.
- Neither owns the other's field.
- Their cooperation becomes faster as they see each other's competence, but Chapter 0 does not make them an established comedy/intimacy pair.
- The prior encounter-count bookkeeping and flirt-adjacent "handsome" joke are removed.
- Ilyra's combat competence is shown through action rather than class exposition.

Protected lines include:

> The line is holding. Move the wounded now.

and Ilyra's:

> Useful enough. Different standard.

The damaged sealed object produces one incomplete **green-and-gold** protective response during a structural emergency. It braces existing weak points/routes; it does not heal, revive, attack, speak, identify itself, manifest, or make anyone invulnerable.

The phenomenon affects Cyanis. Ilyra can stabilize him medically but cannot identify or stop the unknown phenomenon. Her field stabilization does not silently grant an unauthored S005 combat buff.

First Mercy does not respond.

## 9. S005 — Confrontation

S005 is Cyanis + Ilyra versus:

- Riftmaw War Beast;
- Beast Handler A — restraint/control support;
- Beast Handler B — aggression/direction support;
- Outer Relay Barricade as an authored battlefield objective where retained.

Riftmaw has **one continuous HP bar**.

State architecture:

**Restrained -> Unbound -> optional Cornered behavior**

Unbound is processed only after the current round finishes when the HP threshold has been crossed. The transition:

- does not refill HP;
- does not begin a second battle;
- does not grant a free attack;
- does not interrupt the current round;
- samples surviving Handler state for the next legal round.

Handler support consumes Handler actions. The physical chains remain even if the Handlers die; killing the Handlers removes or reduces command/control support rather than instantly breaking the restraint.

Cornered is a low-HP AI-weighting/state change only. It is not a third HP bar, third full phase, frenzy double-turn, or immediate threshold attack.

If Riftmaw locks a final relay-pressure action, that intent is visible at the beginning of the round and the player chooses Cyanis's and Ilyra's full round normally.

At zero HP:

- the player's legal action remains the actual finishing action;
- any later locked Riftmaw action is lost under ordinary defeat rules;
- Riftmaw receives no last-gasp bonus action;
- the Card remains completely inert.

If a Handler remains conscious when Riftmaw falls, encounter resolution uses a legal scripted withdrawal/neutralization exit classification. No revenge action or trivial cleanup round is added.

S005 aftermath is intentionally quiet and hands directly to S006.

## 10. S006 — Aftermath

S006 keeps human consequences ahead of artifact mystery.

Approved sequence:

- incomplete casualty accounting;
- bounded south-ditch/rear-wagon survivor sweep;
- one survivor explicitly recovered alive;
- one convoy member confirmed dead;
- at least three additional tracks continue south and remain unresolved;
- Cyanis and Ilyra obey the search boundary while another friendly search element takes the trail;
- sealed-object protocol is discussed only after the human accounting is addressed.

The reciprocal early self-neglect callback is protected:

> CYANIS: You can wait. Don't mistake that for fine.  
> ILYRA: That was my line.  
> CYANIS: Still true.

Mandatory skipped-meal/food discussion is removed so C02 retains ownership of that Character-Life material.

The sealed object remains closed and unidentified for Brackenwall transfer. Ilyra knows the first symptoms of Cyanis's instability and can attempt stabilization if it recurs; she does not claim to understand the object.

Ilyra independently chooses to continue beyond Brackenwall because the humanitarian crisis is unfinished.

Protected recruitment center:

> CYANIS: You're staying.  
> ILYRA: I'm not doing it for you.  
> CYANIS: I know.  
> ILYRA: There are still people missing.  
> CYANIS: Then we find them.

Ilyra becomes a permanent playable party member at S006.

Chapter 0 closes quietly with the reduced convoy moving toward **Brackenwall**.

## 11. Information firewall

Through Chapter 0:

- the damaged Card/object remains unidentified;
- First Champion is not named or identified;
- no Prime/bearer framework is explained;
- First Mercy does not respond;
- the Card does not solve S005;
- no player dialogue choices are introduced;
- no romance-route architecture is introduced.

## 12. Chapter 1 preservation

v1.40 does not rewrite Chapter 1. The approved S007-S011 production wording under v1.39 remains controlling unless separately reopened by explicit change control.

The Chapter 0 ending must feed the existing S007 opening state: Cyanis + Ilyra arrive at Brackenwall with the sealed artifact wagon and the surviving convoy context intact.

## 13. Implementation gate after this approval

The newly approved Chapter 0 is **canon complete but not yet runtime revalidated**.

Before Chapter 0 can again be described as current implementation-validated content:

1. serialize the exact approved S001-S006 wording/cues into `DiyseDialogueSceneDefinition` Resources using stable `Sxxx_B###` IDs;
2. update scene validators and Chapter 0 continuity validation for the new beat counts and new combat/story boundaries;
3. update any encounter handoff data so Battle 1-7 follow the v1.40 round-system locks;
4. run scene-specific validation;
5. run the full Godot regression suite on the exact replacement head;
6. run the Android debug/export checkpoint on that same head;
7. only then replace the historical Chapter 0 implementation PASS with a v1.40 implementation PASS.

Until those gates pass, the repository must report the previous S001-S006 Resources as **superseded implementation pending replacement**, not as current canon.

## 14. Workflow state

- Chapter 0 rebuild design/dialogue approval: **COMPLETE / CANON**.
- Chapter 0 runtime Resource replacement: **PENDING**.
- Chapter 0 Godot/Android revalidation: **PENDING**.
- Chapter 1 S007-S011 prose canon: **PRESERVED**.
- Chapter 1 Resource conversion/implementation validation: remains a separate pending gate under v1.39/v1.40 inherited workflow.
- Phase 29B exact formation tables, Phase 30 numerical rebase, and Phase 31 integrated pacing validation remain downstream work.
