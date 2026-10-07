# Diyse — Prime System Rules

**Status:** ACTIVE PRIME FOUNDATION; EXACT MANIFESTATION SEQUENCING PARKED  
**Authority:** current Prime-domain owner plus `../../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`.  

## Identity and progression

Exactly **12 Prime Cards**:

- 6 Story Primes
- 6 Major-Hunt Primes

Story progression:

**Recovered → Awakened**

Major-Hunt Primes are acquired **Awakened**. Awakened is final.

Prime progression does not use XP, levels, duplicates, material upgrades, or a third progression state.

## Invocation and MP

Prime manifestation is initiated by an eligible active character from that character's TURN.

- Invocation costs **0 MP**.
- Prime commands cost **0 MP** unless a specific Prime explicitly defines another internal restriction.
- Prime manifestation is not a passive proc or ordinary Standard Card play.

## Use state and restoration

Each individual Prime identity has **1 use until restored**.

- invoking one Prime spends only that identity;
- spent/Ready persists across battles;
- battle end does not restore spent Primes;
- entering another battle does not restore spent Primes;
- a valid full rest restores eligible spent Primes;
- a checkpoint-area heal/restoration is a valid restoration point;
- an explicitly authored Prime-restoring item/effect may restore eligible spent Primes;
- same-bar phase/state changes do not restore spent Primes;
- genuine fresh-HP enemy bodies/forms do not restore spent Primes.

### Emergency Kit

Emergency Kit restores every **acquired** Story and Major-Hunt Prime to Ready.

It:

- can restore a Prime spent earlier in the same battle;
- does not grant unacquired Primes;
- does not change Recovered/Awakened progression;
- restores spent/Ready state only;
- does not bypass an active post-Prime party lockout.

## Party replacement concept

During manifestation, the Prime temporarily replaces the normal active party.

- party HP, MP, and persistent battle state are preserved;
- exact party hidden-cycle behavior while manifested is part of the parked sequencing pass;
- exact Recovered and Awakened internal TURN/EXECUTION structure is not yet final.

## Demanifestation finisher

Every manifested Prime has a final automatic signature effect when manifestation ends.

- it does not require another ordinary command selection;
- each Prime may define unique targeting, element, Potency, and secondary effects;
- exact placement and Delay/Interrupt interaction remain part of the parked Prime sequencing pass.

## Party-wide post-Prime lockout

After a Prime demanifests, no party member may invoke any Prime until the **invoking character has processed 3 personal TURNs**.

- the invoking character is the cooldown owner;
- each owner TURN reduces the lockout by 1;
- the owner's hidden reserve TURNs count;
- queued EXECUTION markers do not count;
- swapping itself does not create a count;
- a denied/skipped owner TURN counts if that TURN occurred;
- after the third owner TURN is processed, the party-wide lockout ends;
- restoring a spent Prime does not shorten or bypass this lockout.

This replaces the former three-full-normal-round spacing model.

## Parked manifestation sequencing

The following are intentionally unresolved until the dedicated Prime sequencing pass:

- exact Recovered battle sequence;
- exact Awakened battle sequence;
- whether Awakened still uses exactly 3 Prime TURNs;
- normal party hidden-cycle behavior during manifestation;
- exact finisher placement;
- Delay/Interrupt interaction with Prime commands and finisher.

Do not implement a placeholder three-Prime-round or three-normal-party-round sequence as current authority.

## Boss-form interaction

Prime availability is not enemy-body-scoped.

A same-bar state change or genuine fresh-HP form:

- does not refresh spent Prime identities;
- does not create a new Prime-use allowance;
- does not cancel or shorten an active post-Prime lockout.

## Final Severance story-resolution exception

The mandatory Chapter-13 Final Severance sequence occurs **after The Last Command's combat body reaches 0 HP**.

It is a story-resolution manifestation sequence rather than another selected combat Prime Invocation or another boss combat phase. Combat spent/availability flags and the normal post-Prime lockout therefore do not block the six required Story Prime manifestations in that story-resolution sequence.

Final Severance order remains:

**HOLD → DISTINGUISH → MAP → PRESERVE → CONTAIN → END**
