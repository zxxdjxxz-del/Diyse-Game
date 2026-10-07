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

The UI must represent at least:

- Ready vs spent identity state;
- whether a party-wide post-Prime lockout is active;
- lockout owner;
- owner's personal TURNs remaining in the 3-TURN lockout;
- explicit restoration results.

Do not display the old **3 full normal party rounds** cooldown.

## Parked manifestation UI

Exact Recovered/Awakened manifestation TURN sequencing is currently parked.

Therefore, production UI must **not** hard-code:

- exactly one Recovered action in an ordinary round;
- exactly 3 Awakened Prime rounds;
- a Prime-round counter;
- assumptions about normal-party hidden-cycle behavior during manifestation.

The final manifestation HUD/command presentation should be completed after the dedicated Prime sequencing pass.

## Stable post-manifestation lockout

After a Prime demanifests, nobody may invoke another Prime until the invoking character has processed **3 personal TURNs**.

- that character is the cooldown owner;
- their hidden reserve TURNs count;
- queued EXECUTION markers do not count;
- a denied owner TURN counts if the TURN occurred;
- restoration of spent Primes does not bypass the active lockout.
