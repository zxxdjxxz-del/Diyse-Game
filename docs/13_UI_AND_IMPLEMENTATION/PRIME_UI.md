# Diyse — Prime UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Count / progression
Exactly:
- 12 Prime Cards
- 6 Story
- 6 Major Hunt

Story progression:
> Recovered → Awakened

Major-Hunt Prime:
> acquired Awakened

No Concordant screen.

## Loadout
From Chapter-4 Prime-loadout access until Sixfold Volition:
> **1 Prime slot per permanent character**

After Sixfold Volition:
> **2 Prime slots per permanent character**

Prime slots are separate from 3 Standard Card slots.

Any acquired Prime may occupy a legal Prime slot.

Story bearer association is narrative:
- it does not owner-lock battle use.

## Invocation costs
Prime Invocation costs:
> **0 MP**

Prime commands after manifestation also cost:
> **0 MP**

Do not display or reserve a Prime-specific MP charge, per-round MP drain, or state-based Prime MP tier.

## Recovered UI state
Recovered Story Prime:
- manifests as the selected invocation action;
- performs exactly one strong signature action;
- dismisses that same ordinary round.

Do not show a three-round Recovered duration.

## Awakened UI state
Awakened Prime:
- suspends active party;
- directly controlled for **3 Prime rounds**;
- one selected Prime command per Prime round.

Prime UI must expose:
- rounds remaining;
- legal commands;
- target where required.

## Availability
Each Prime identity:
> once per battle per Prime identity unless explicitly restored.

After normal dismissal:
> 3 full normal party rounds

before another unused equipped Prime may be invoked.

The UI must be able to represent:
- available;
- used;
- cooldown rounds remaining;
- explicit authored restoration only.

Neither same-bar phase changes nor genuine fresh-HP form changes refresh Prime availability.

## Implementation divergence
Current proof runtime still models an old bearer-locked `first_champion` and an outdated proof duration.

Do not ship that proof behavior as final production Prime UX.
