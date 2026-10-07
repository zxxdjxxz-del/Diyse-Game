# Diyse — Prime UI

**Status:** ACTIVE UI / IMPLEMENTATION SPEC  
**Authority:** UI implementation defers gameplay behavior to `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md` and `../07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md`.

## Count / progression

Exactly:

- 12 Prime Cards
- 6 Story
- 6 Major-Hunt

Story progression:

**Recovered → Awakened**

Major-Hunt Primes are acquired Awakened. No third progression-state screen is required.

## Loadout

From Chapter-4 Prime battle-loadout access until Sixfold Volition:

- **1 Prime slot per permanent character**

After Sixfold Volition:

- **2 Prime slots per permanent character**

Prime slots are separate from the character's **4 Standard Card slots**.

Any acquired Prime may occupy a legal Prime slot. Story bearer association is narrative and does not owner-lock battle use.

## Costs and availability

- Prime Invocation: **0 MP**
- Prime commands: **0 MP** unless a specific Prime explicitly defines another internal restriction
- each Prime identity has one use until valid restoration
- spent/Ready state persists across battles
- same-bar/fresh-HP form changes do not restore availability

The pre-invocation UI must represent at least:

- Ready vs Spent identity state;
- whether a party-wide post-Prime lockout is active;
- lockout owner;
- owner's personal TURNs remaining in the 3-TURN lockout;
- explicit restoration results.

## Recovered presentation

A Recovered Story Prime is a one-action manifestation.

The UI does not open the Awakened meter HUD. It presents/resolves the Prime's single signature action and then returns to normal battle after demanifestation.

## Awakened Manifestation Meter HUD

Every Awakened manifestation begins with a visible **3-segment Manifestation Meter**.

Command presentation must communicate:

- **Basic** — costs 1 segment
- **Medium** — costs 2 segments
- **Heavy** — costs 3 segments
- current remaining meter
- whether a command is currently affordable
- the command's projected EXECUTION
- the Prime's projected next TURN / Return

The standard kit surface supports:

- 2 Basic abilities
- 2 Medium abilities
- 1 Heavy ability

The Dismissal ability is automatic and is not presented as a normal selectable meter command.

Meter is spent only when the selected Prime command successfully reaches EXECUTION. If a queued Prime command is canceled before EXECUTION, the HUD keeps that meter available.

## Final Return

When a successful command empties the meter:

- the HUD enters a clear **Final Return** state;
- no new Prime command is offered;
- the Prime remains on the battlefield;
- the timeline continues to show the Prime's already-scheduled next TURN;
- legal Delay to that TURN visibly delays Dismissal;
- at that TURN, the automatic Dismissal ability resolves;
- the Prime leaves and the party returns.

The timeline/HUD must make it clear that a Heavy-Return meter-emptying action leaves the Prime exposed longer than a faster-returning action.

## Early / abnormal end states

The UI must distinguish normal Dismissal from:

- Prime KO;
- forced removal/banishment;
- manual early dismissal.

Those three abnormal/early endings do **not** trigger the Dismissal ability.

Manual early dismissal must communicate that:

- remaining meter is lost;
- the Prime's use remains Spent;
- no Dismissal benefit occurs.

## Party suspension presentation

During an Awakened manifestation, the active party is suspended rather than continuing hidden battle progression.

The battle UI must preserve rather than advance:

- party TURN positions;
- queued party EXECUTION markers;
- party status durations;
- party buff/debuff durations.

Prime abilities may explicitly alter the preserved party state through supported beneficial effects such as healing, revival, Quick, or stat-up effects.

## Enemy continuity and retargeting

Enemy TURNs and EXECUTIONs remain active while the Prime is manifested.

Queued hostile intent should remain visible and retarget according to the Prime-system rules when the party/Prime battlefield representation changes.

## Post-manifestation lockout

After any Prime demanifests, nobody may invoke another Prime until the invoking character has processed **3 personal TURNs**.

- that character is the cooldown owner;
- their hidden reserve TURNs count;
- queued EXECUTION markers do not count;
- a denied owner TURN counts if the TURN occurred;
- restoration of spent Primes does not bypass the active lockout.
