# Diyse — Awakened Prime Round Sequencing

**Status:** ACTIVE COMBAT-SEQUENCING AUTHORITY  
**Scope:** transition from a normal party round into an Awakened Prime manifestation, Prime-round initiative/action economy, dismissal, and return to normal-round flow.  
**Cross-domain Prime resource authority:** `../07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md`.

This file closes the previously unspecified interaction between Awakened Prime manifestation and Diyse's fixed normal-round turn-entry model.

## 1. Invocation during an active normal round
Awakened Prime Invocation is a selected action and consumes the invoking character's current normal-turn action.

When that Invocation resolves:
1. the selected Prime identity is spent under the normal Prime-use rule;
2. the active ordinary party is suspended immediately;
3. the manifested Prime becomes the sole normal allied combat body on the field;
4. the already-locked initiative order for the current normal round is **not rebuilt or restarted**.

For the remainder of that already-started normal round:
- any ordinary party turn slots that have not yet occurred are **skipped**;
- skipped party slots are not banked and do not resume later;
- enemy/support turn slots that already occurred do not occur again;
- enemy/support turn slots that have not yet occurred remain eligible and resolve once in their already-locked positions;
- those enemies/supports target and evaluate the manifested Prime using the legitimate battle state when their turns actually arrive.

After all remaining eligible slots are resolved or skipped, the invocation normal round reaches its normal end-of-round processing.

## 2. Targeting while the ordinary party is suspended
During an Awakened Prime manifestation:
> **the Prime is the sole normal allied battle body.**

Therefore:
- the suspended ordinary party cannot be targeted;
- a hostile action written to affect `all conscious party members` affects the Prime **once**;
- no action creates four phantom party targets merely because four characters were active before suspension;
- an action that explicitly requires several distinct allied targets must use its own authored valid fallback while only the Prime exists;
- if no such fallback exists and its target requirement cannot be met, that branch/action is not legal at that moment.

Prime-specific target exceptions remain legal only where explicitly authored.

## 3. Prime Rounds 1–3
After the invocation normal round finishes, an Awakened Prime receives exactly:
> **3 Prime rounds**

At the beginning of each Prime round:
1. resolve Prime-round beginning checks that are actually eligible to advance during manifestation;
2. build the round's initiative order from the manifested Prime's current Speed and every active enemy/support actor's current Speed;
3. use the ordinary Speed/tie rules unless an owning Prime/encounter rule explicitly overrides them;
4. lock that Prime-round initiative order for the round.

The manifested Prime counts as the allied body for tie resolution, so an exact Prime-vs-enemy Speed tie is won by the Prime.

During each Prime round:
- the Prime receives exactly **1 selected Prime command**;
- each eligible enemy/support receives exactly **1 selected action opportunity**;
- enemy AI chooses its currently legal action when its actual turn arrives;
- actions resolve immediately before the next actor's turn;
- there is no full-round command queue and no Confirm Round step;
- the suspended ordinary party receives no turns.

After every eligible Prime/enemy/support slot completes or is legally lost, resolve Prime-round end processing and advance to the next Prime round.

## 4. Enemy repetition locks and delayed action economy
Enemy repetition locks/cooldowns that regulate **selected-action opportunities** continue to operate through Prime rounds.

Unless an owning enemy action explicitly defines another clock:
- a 1-round repetition lock blocks that selected action on the enemy's **next eligible turn opportunity**;
- a 2-round repetition lock blocks it on the enemy's **next two eligible turn opportunities**;
- a pending authored Preparation/follow-up remains pending and resolves on the next eligible turn allowed by its owner;
- these action-economy locks do not pause merely because the ordinary party is suspended.

This does **not** convert ordinary normal-round duration effects into Prime-round durations.

Effects explicitly measured in **normal party rounds** continue to follow `PRIME_SYSTEM_RULES.md`: ordinary Fields, ordinary normal-round temporary core-stat timers, and ordinary normal-round tactical-state timers remain recorded and paused unless their owner explicitly says otherwise.

## 5. Enemy/boss state changes during manifestation
Normal legal HP thresholds, same-body state changes, support destruction/spawn rules, and genuine fresh enemy bodies may occur while a Prime is manifested.

They do not automatically dismiss the Prime.

A genuine fresh-HP enemy body also does **not** restore a spent Prime identity. Prime restoration remains owned by the valid-rest/explicit-restoration rule.

## 6. Dismissal after Prime Round 3
After the end-of-round processing for Prime Round 3:
- the Prime dismisses;
- the ordinary party returns;
- the next combat round is a **fresh normal party round** with a newly constructed normal initiative order;
- skipped ordinary party slots from the original invocation round do not resume.

The post-dismissal spacing gate begins with that fresh normal round:
> **2 full normal party rounds must be completed before another Ready Prime may be invoked.**

Spacing never restores a spent Prime; restoration remains separate.

## 7. Early Prime defeat
If the manifested Prime reaches 0 HP before completing all three Prime rounds:
1. finish resolving the complete action/effect that reduced the Prime to 0 HP;
2. dismiss the Prime immediately after that action finishes;
3. do not insert ordinary party turns into the unfinished Prime round;
4. return the ordinary party only at the beginning of a fresh normal round;
5. begin the normal 2-full-normal-round post-dismissal spacing gate with that fresh normal round.

Prime defeat does **not** by itself mean the ordinary party is KO'd or defeated unless an encounter explicitly says otherwise.

## 8. Recovered Story Primes remain different
Recovered Story Primes do not create the three-round manifestation structure above.

They retain their current rule:
- Invocation resolves in the current ordinary round;
- the Recovered Prime performs its one signature action;
- it dismisses in that same ordinary round;
- the already-locked normal round then continues normally with remaining eligible ordinary slots.

## 9. Firewall
This sequencing rule does not introduce:
- ATB;
- extra actions from Speed;
- a party command queue;
- Confirm Round;
- a universal Wait/Move command;
- boss-form Prime restoration;
- automatic Prime immunity to harmful statuses.

Prime status/control behavior remains owned by `../07_CARDS/PRIME_CARDS/PRIME_STATUS_CONTROL.md`.
