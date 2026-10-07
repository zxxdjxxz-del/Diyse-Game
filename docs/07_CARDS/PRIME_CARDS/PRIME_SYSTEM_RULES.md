# Diyse — Prime System Rules

**Status:** ACTIVE PRIME MANIFESTATION AUTHORITY  
**Authority:** current Prime-domain owner plus `../../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`.  
**Core battery system:** structurally complete. Exact individual Prime kits remain a later content/rebalance pass.

## 1. Prime collection and states

Exactly **12 Prime Cards**:

- 6 Story Primes
- 6 Major-Hunt Primes

Story Prime progression is:

**Recovered → Awakened**

Major-Hunt Primes are acquired **Awakened**. Awakened is final.

Prime progression does not use XP, permanent Prime levels, duplicates, material upgrades, or a third progression state.

### Recovered Story Prime

A Recovered Story Prime is the one-action manifestation form.

- it manifests;
- it performs its single signature action;
- it demanifests immediately after that action;
- it does not enter the controllable Awakened manifestation sequence;
- it does not use the Manifestation Meter.

### Awakened Prime

An Awakened Prime temporarily replaces the active party and becomes the controllable allied battlefield unit.

Awakened Primes use the Manifestation Meter system below.

## 2. Invocation

Prime Invocation is a special action initiated from an eligible active character's TURN.

- Invocation costs **0 MP**.
- Invocation consumes the invoking character's current command opportunity.
- Invocation resolves immediately.
- Prime Invocation itself cannot be Interrupted.
- The active party is suspended when manifestation resolves.
- An Awakened Prime appears and is immediately ready for its first command.
- There is no separate entry delay or entry-recovery mechanic.

Prime commands cost **0 MP** unless a specific Prime explicitly defines another internal restriction.

Invocation makes that Prime identity **Spent**.

Loadout and bearer-access rules remain in `PRIME_LOADOUT_AND_ACCESS.md`.

## 3. Manifestation Meter

Every Awakened Prime begins each manifestation with a **3-segment Manifestation Meter**.

| Tier | Meter Cost |
|---|---:|
| Basic | 1 |
| Medium | 2 |
| Heavy | 3 |

Common spending sequences include:

- Basic → Basic → Basic
- Basic → Medium
- Medium → Basic
- Heavy

### Universal battery rule

The 3-segment meter is a system-level rule.

Individual Prime kits do **not**:

- increase meter capacity;
- refill meter;
- preserve unused meter between manifestations;
- carry meter into a later manifestation;
- exceed the normal 3-segment maximum.

Any future exception requires an explicit system-wide rule rather than an individual Prime ability silently breaking the battery system.

## 4. Standard Awakened Prime kit structure

Each Awakened Prime uses the same structural command package:

- **2 Basic abilities** — 1 segment each
- **2 Medium abilities** — 2 segments each
- **1 Heavy ability** — 3 segments
- **1 unique Dismissal ability** — automatic, 0 segments

Prime identity comes from effects, targeting, Execution, Return, utility, support profile, status interaction, and Dismissal behavior rather than different meter sizes.

Exact Potency, formulas, status values, timing, and final individual kit content remain part of the later Prime-kit rebalance.

### Basic — 1 segment

Basic abilities are efficient and flexible.

They should generally:

- have lower impact than Medium or Heavy abilities;
- use relatively favorable Return timing;
- support multi-action sequencing;
- provide focused damage, setup, defense, healing, utility, or light control;
- remain useful when repeated.

### Medium — 2 segments

Medium abilities are high-value tactical commitments.

They should generally:

- provide substantially greater impact than a Basic;
- combine stronger damage, healing, protection, setup, control, or utility;
- carry more meaningful timing or another balancing limitation;
- make **Basic + Medium** a real alternative to **three Basics**.

### Heavy — 3 segments

The Heavy ability is the Prime's full-meter commitment.

It should generally:

- be one of the Prime's defining actions;
- create major immediate impact;
- carry meaningful Return risk;
- justify giving up all Basic/Medium sequencing for that manifestation.

Heavy is not automatically the best choice.

### Dismissal — 0 segments

The Dismissal ability is not a selectable normal command.

It:

- costs 0 meter;
- triggers only after a successful normal end of manifestation;
- resolves before the Prime leaves the battlefield;
- may deal damage, heal, revive, buff, debuff, protect, manipulate battlefield state, or perform another Prime-specific effect.

Dismissal abilities are Prime-specific and are not required to be generic final attacks.

## 5. TURN / EXECUTION / Return flow

Prime commands use the normal TURN / EXECUTION battle framework.

1. The Prime receives a TURN.
2. The player selects a Basic, Medium, or Heavy command.
3. The Prime's next TURN is scheduled when the command is selected using that command's Return category.
4. The command either EXECUTEs immediately or creates a queued EXECUTION marker.
5. Manifestation Meter is spent only when the command successfully reaches EXECUTION.
6. If meter remains above 0, manifestation continues.
7. If successful EXECUTION reduces meter to 0, the Prime enters **Final Return**.
8. The Prime remains on the field until its already-scheduled next TURN arrives.
9. At that TURN, no new Prime command is selected; the automatic Dismissal ability resolves.
10. The Prime demanifests and the party returns.

Core rule:

> **The Prime dismisses only after returning from the action that emptied its meter.**

## 6. Execution and Return guidance

Execution speed and Return are separate balance axes.

A Prime command may use any appropriate Execution category independently of its Return category.

Default Return guidance:

- **Basic:** generally Fast Return
- **Medium:** generally Normal Return
- **Heavy:** generally Heavy Return

These are defaults rather than rigid requirements.

The final meter-emptying action's Return is especially important because the Prime remains manifested and vulnerable until that next TURN arrives.

## 7. Interrupt and Delay

Awakened Prime commands are not inherently immune to Delay or Interrupt.

### Interrupted command

If a queued Prime command is canceled before EXECUTION:

- its meter cost is **not** spent;
- the Prime remains manifested;
- remaining meter is unchanged;
- the already-scheduled next TURN does not move earlier merely because the EXECUTION was canceled.

### Final Return Delay

After a meter-emptying command successfully EXECUTEs, the Prime waits for its already-scheduled next TURN.

If that TURN marker is legally Delayed:

- the Prime remains manifested;
- Dismissal is delayed with that TURN;
- Delay alone does not cancel the Dismissal ability.

## 8. Ending a manifestation

### Normal Dismissal

A normal Awakened manifestation ends when:

- the meter reaches 0 through a successfully executed command;
- the Prime survives its Final Return;
- its next TURN arrives;
- its Dismissal ability resolves;
- the Prime demanifests.

### KO before Dismissal

If the Prime is KO'd before normal Dismissal:

- the Dismissal ability does not trigger;
- the Prime immediately demanifests;
- the party returns;
- spent meter is not refunded;
- the Prime's use remains consumed.

### Forced removal

If an enemy effect forcibly banishes or removes the Prime before normal Dismissal:

- the Dismissal ability does not trigger;
- the Prime immediately demanifests;
- the party returns;
- spent meter is not refunded;
- the Prime's use remains consumed.

### Manual early dismissal

The player may manually dismiss an active Awakened Prime before natural meter exhaustion.

Early dismissal:

- does not trigger the Dismissal ability;
- immediately returns the party;
- grants no refund or benefit from remaining meter;
- leaves the Prime's use consumed.

### Prime-local state

When a Prime demanifests, its temporary manifestation-local state ends.

This includes temporary:

- buffs;
- debuffs;
- harmful statuses;
- setup states;
- control states.

These do not carry into a later restored manifestation.

## 9. Party state during Awakened manifestation

The four active party members are suspended while an Awakened Prime is manifested.

By default:

- party TURN progression is frozen;
- party queued EXECUTIONs do not progress;
- party status durations do not tick;
- party buffs and debuffs do not expire;
- party timeline positions are preserved;
- ordinary battlefield effects do not affect the suspended party.

When the Prime demanifests, the party returns to its preserved battle state and normal timeline progression resumes.

### Prime effects that reach the suspended party

A Prime ability may explicitly affect the suspended party.

Supported examples include:

- HP healing;
- revival;
- **Quick**;
- stat-up effects;
- other explicitly authored beneficial effects.

These effects modify the party's preserved state while the party remains suspended.

Duration-based beneficial effects applied to the suspended party do not begin ticking until the party returns unless the Prime ability explicitly says otherwise.

## 10. Enemy timeline during manifestation

Enemies remain fully active while an Awakened Prime is manifested.

- enemy TURNs continue;
- enemy EXECUTIONs continue;
- enemy Return continues;
- enemy statuses, buffs, and debuffs continue under normal rules;
- enemies may target and act against the Prime.

Prime manifestation replaces the active party; it does not pause the battle.

## 11. Targeting transitions

### When the Prime manifests

Already-committed hostile actions are not erased by manifestation.

By default:

- a queued single-target hostile action aimed at a party member retargets the Prime;
- a queued multi-target or party-wide hostile action resolves against the Prime when it is the only active allied battlefield target;
- an action fails only when the Prime is genuinely invalid under that action's own targeting restrictions.

### When the Prime demanifests

A hostile action queued against the Prime is not erased merely because the Prime leaves.

By default:

- a queued single-target hostile action retargets a valid returning active party member using the normal fallback rules;
- a queued multi-target or party-wide hostile action resolves against the returned party under its normal targeting rules;
- the action fails only if no legal target exists.

This applies to normal Dismissal, manual dismissal, KO, and forced removal unless an effect explicitly overrides it.

## 12. Prime stats and scaling

Primes use their own independent stat profiles.

They do not inherit the invoking character's:

- stats;
- equipment;
- current HP percentage;
- buffs;
- harmful statuses.

Each Prime has its own combat identity through its stat distribution.

### Reference Level

> **Reference Level = highest current level among all currently recruited permanent party members**

The Prime does not permanently store this level and does not gain Prime EXP or permanent Prime levels.

This rule applies before the full six-character roster is assembled and prevents formation changes from changing Prime strength.

### Recovered scaling

Recovered Primes use the same underlying Prime stat identity and Reference Level rule as Awakened Primes.

Recovered changes the manifestation format, not the Prime's core stat identity.

Exact Prime stat formulas and state/identity multipliers require revalidation during the later combat-stat rebalance.

## 13. Combat effects on Awakened Primes

Awakened Primes are normal active battlefield units unless an explicit Prime rule says otherwise.

They may generally:

- take direct and indirect damage;
- receive legal healing;
- receive buffs and stat-up effects;
- receive debuffs and stat-down effects;
- receive applicable harmful statuses;
- be affected by ordinary Delay, Interrupt, targeting, and other battle mechanics.

Primes do not have blanket status/control immunity.

Individual Prime resistances, immunities, or special interactions must be explicitly authored on that Prime.

## 14. Prime use and restoration

Each Prime identity has **1 use until restored**.

Spent/Ready state persists across battles.

A spent Prime is not restored by:

- battle end;
- entering another battle;
- same-bar phase changes;
- genuine fresh-HP enemy forms.

Eligible spent Primes are restored by:

- valid full rest;
- checkpoint-area restoration;
- explicitly authored Prime-restoring effects.

### Emergency Kit

Emergency Kit restores every acquired Story and Major-Hunt Prime to Ready.

It may restore Primes spent earlier in the same battle.

Restoration does not bypass an active post-Prime lockout.

### Restored same-battle manifestation

If a Prime is restored and legally invoked again in the same battle, it begins the new manifestation with:

- **full HP**;
- a fresh **3-segment Manifestation Meter** if Awakened;
- no carried-over temporary Prime-local state.

## 15. Post-Prime party lockout

After any Prime demanifests, Prime Invocation enters a party-wide lockout owned by the invoking character.

No party member may invoke any Prime until that character has processed **3 personal TURNs**.

- each owner TURN reduces the lockout by 1;
- the owner's hidden reserve TURNs count;
- queued EXECUTION markers do not count;
- a denied/skipped owner TURN counts if the TURN occurred;
- restoring a spent Prime does not shorten or bypass the lockout.

After the third owner TURN is processed, Prime Invocation becomes legal again if an otherwise legal Ready Prime is available.

## 16. Individual Prime kit migration boundary

Every Awakened Prime must ultimately use:

**2 Basic / 2 Medium / 1 Heavy / 1 Dismissal**

Individual Prime files currently own identity, role, acquisition/bearer information, and migration anchors. Exact current commands are not locked until the dedicated Prime-kit pass maps those identities into the new meter tiers and current combat language.

That later pass may revise:

- Potency and formulas;
- Execution and Return;
- statuses and chances;
- stat changes and durations;
- Delay / Interrupt behavior;
- targeting;
- setup states;
- party-return effects;
- balance across Basic, Medium, Heavy, and Dismissal;
- any mechanic that does not fit the current battle system.

## 17. Final Severance story-resolution exception

The mandatory Chapter-13 Final Severance sequence occurs **after The Last Command's combat body reaches 0 HP**.

It is a story-resolution manifestation sequence rather than another selected combat Prime Invocation or another boss combat phase. Combat spent/availability flags and the normal post-Prime lockout therefore do not block the six required Story Prime manifestations in that story-resolution sequence.

Final Severance order remains:

**HOLD → DISTINGUISH → MAP → PRESERVE → CONTAIN → END**

## 18. Completion boundary

The **Prime Manifestation Meter / battery system is structurally complete**.

Remaining Prime work is outside the battery-system architecture:

- migration of the twelve individual Prime kits into the 2 Basic / 2 Medium / 1 Heavy / 1 Dismissal structure;
- later full Prime-kit rework;
- final numerical balancing and formula validation;
- implementation/UI execution after authority promotion.
