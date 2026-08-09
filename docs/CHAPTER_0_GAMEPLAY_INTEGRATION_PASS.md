# Chapter 0 Gameplay Integration Pass

Status: ACTIVE DRAFT — gameplay integration only. Approved S001-S006/C01/C02 dialogue wording remains protected unless a minimal continuity edit is required by a playable handoff.

## Goal
Revalidate Chapter 0 — The Broken Convoy — as an approximately 55-minute JRPG opening with a majority of critical-path time under active player control.

## Fixed story/combat locks
- S001 Opening: Cyanis viewpoint, ordinary observation, ambush, no Ilyra, no Card response.
- S002 Wreck Field exploration: survivor roles, unstable wreckage, Convoy Rift Hound, north-cut evidence.
- S003 Evacuation Relay decision: Cyanis professionally refuses unsound pursuit; officer revises order from evidence.
- S004 Field Triage Camp revelation: Ilyra first appears; independent triage authority; incomplete unidentified Card response.
- S005 Confrontation: final Chapter 0 combat handoff.
- S006 Aftermath: survivor recovery, sealed Card protocol, Ilyra permanent join, Brackenwall route.
- C01/C02 optional after S006; not counted in fixed critical-path runtime.

Combat sequence is fixed:
1. Solo Cyanis vs Level 2 Iron Cohort Soldier at 60% HP — Attack, target selection, Defend tutorial.
2. Solo Cyanis vs Level 3 Convoy Rift Hound at 70% HP — faster enemy and wounded-target pressure.
3. Cyanis + Ilyra vs Level 4 Convoy War-Sorcerer at 70% HP + Level 3 Iron Cohort Soldier at 50% HP — Broken Champion's Ward for 3 rounds under controlling encounter authority.

## Working runtime target
Critical path: 55 minutes total.
- Dialogue/cinematic presentation: target 15–18 min.
- Active exploration/traversal/interactions: target 20–23 min.
- Combat/tutorial battle time: target 10–12 min.
- Menus/rewards/checkpoints/transitions: target 4–6 min.

This is a pacing target, not a new system rule. Final timing is validated after implementation.

## Scene play-flow map

### S001 — Opening (~8 min)
1. CUTSCENE / IN-WORLD DIALOGUE — convoy setup, Cyanis/officer exchange, road concern. ~3 min.
2. SHORT PLAYER CONTROL — walk the east side of the convoy; movement tutorial; inspect spacing points; optional one-line NPC barks. ~2 min.
3. CUTSCENE — halt order, ambush, separation, civilians move to cover. ~1.5 min.
4. COMBAT 1 — solo Cyanis vs wounded Iron Cohort Soldier. ~1.5 min.
5. RETURN TO PLAYER CONTROL — short post-battle handoff into S002.

### S002 — Wreck Field exploration (~12 min)
1. PLAYER CONTROL — traverse wreck field and learn interaction prompt. ~2 min.
2. INTERACTION — assist wounded escort; assign a survivor role through authored interaction, not dialogue choice. ~1.5 min.
3. EXPLORATION / ENVIRONMENT — trapped civilian extraction using rope/spoke interaction; player performs bounded interact steps. ~2 min.
4. PLAYER CONTROL — navigate through wreckage by movement only; center route visibly unstable, stone line viable. No narrative branch. ~2 min.
5. COMBAT 2 — Convoy Rift Hound. ~2 min.
6. INVESTIGATION — inspect dragged chain marks / crushed grass / north-cut geometry. Player triggers authored observations. ~1.5 min.
7. RETURN TO STORY — officer contact and suspicious-route handoff to S003. ~1 min.

### S003 — Evacuation Relay decision (~7 min)
1. PLAYER CONTROL — reach relay, check casualty stations / escort positions / recovery wagon sightline. ~2 min.
2. INTERACTION — gather the three tactical facts already used in approved dialogue: exposed wounded/civilians, damaged defender count, suspicious north cut. These are inspection interactions, not choices. ~1.5 min.
3. CUTSCENE / DIALOGUE — pursuit order, Cyanis objection/refusal, evidence-based revised order. ~3 min.
4. RETURN TO PLAYER CONTROL — carry revised order toward triage route. ~0.5 min.

### S004 — Field Triage Camp revelation (~11 min)
1. PLAYER CONTROL — enter developing triage camp; movement lane remains active. ~1.5 min.
2. INTERACTION / SUPPORT TUTORIAL — help clear crates, move supplies, and identify safe treatment-space boundaries under Ilyra's instructions. ~2 min.
3. CUTSCENE / DIALOGUE — Cyanis/Ilyra jurisdiction exchange and medical check. ~2.5 min.
4. PLAYER CONTROL UNDER PRESSURE — position at defensive lane / move to marked protection point; no freeform combat yet. ~1 min.
5. CUTSCENE / SYSTEM STORY EVENT — incomplete Card response, green-and-gold geometry stabilizes evacuation route. ~2 min.
6. INTERACTION — player helps move/escort one critical casualty through the temporarily stabilized route while Ilyra directs treatment. ~1 min.
7. RETURN TO STORY — Broken Champion's Ward state established, threat approaches. ~1 min.

### S005 — Confrontation (~8 min)
1. SHORT CUTSCENE — Cyanis/Ilyra divide battlefield responsibility. ~1.5 min.
2. COMBAT 3 — Cyanis + Ilyra vs War-Sorcerer + injured Soldier under fixed encounter rules. ~5 min.
3. RETURN TO STORY — retreat/no-pursuit, protection fades, immediate medical/work response. ~1.5 min.

### S006 — Aftermath (~9 min)
1. PLAYER CONTROL — aftermath sweep of camp/wreck boundary; speak/interact with surviving escort and at least one civilian status point. ~2 min.
2. CUTSCENE / DIALOGUE — missing-person count, sealed-Card protocol, Ilyra independently remains. ~3.5 min.
3. PLAYER CONTROL — one bounded south-wreck survivor sweep objective; no combat unless existing authority later requires it. ~2 min.
4. RETURN / CHECKPOINT — chapter-complete handoff, Brackenwall route available, save/checkpoint exposure. ~1.5 min.

## Tutorial pacing rules
- Do not stack more than one new core input/system lesson at a time.
- S001 teaches movement + basic combat.
- S002 teaches interaction/environment reading + second combat pressure.
- S003 teaches objective/evidence tracking through world interaction, not dialogue choices.
- S004 teaches support-space interaction and introduces Ilyra's battle role narratively before two-character combat.
- S005 teaches two-character round planning in the fixed encounter.
- S006 exposes chapter completion, route transition, and checkpoint/save flow.

## Player-control standard for future mandatory scenes
Every mandatory scene authoring sheet must explicitly identify, where applicable:
CUTSCENE / PLAYER CONTROL / EXPLORATION / INTERACTION / COMBAT / REWARD-CHECKPOINT / RETURN TO STORY.

Dialogue Resources remain dialogue data; they do not represent the entirety of scene runtime.
