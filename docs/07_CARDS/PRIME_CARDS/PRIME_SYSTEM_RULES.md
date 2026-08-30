# Diyse — Prime System Rules
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary Card/Prime authority:** compatible **Audit116**, superseded where applicable by **Audit119**, **Audit122**, later current v85 working closures, and newer explicit user corrections.  
**Current written whole-project authority:** **v2.20 / Audit135** plus newer approved corrections.  


## Count
Exactly **12 Prime Cards**:
- 6 Story Primes;
- 6 Major-Hunt Primes.

## Progression
Story:
> **Recovered → Awakened**

Major-Hunt:
> acquired **Awakened**

Awakened is final.

Removed:
- Concordant;
- Reactive;
- Prime XP;
- Prime levels;
- duplicate progression;
- upgrade materials;
- third-state progression.

Legacy/final commands formerly described as Concordant functionality remain part of the final Awakened command architecture.

## Invocation is a selected action
Prime Invocation consumes a legal selected combat action.

It is not:
- free reaction;
- passive proc;
- Item action;
- Standard Card play.

## Invocation MP
Prime Invocation costs:
> **0 MP**

Prime commands after manifestation also cost:
> **0 MP**

There is no Prime MP stat, invocation MP charge, or per-Prime-round MP drain.

## Prime use and restoration
Each Prime identity has:
> **one use until restored**

Invoking a Prime spends that specific Prime identity. The spent state persists across battle end and into later battles until the Prime is restored by a valid rest or other explicitly authored Prime-restoration effect.

Using one Prime does not spend any other available Prime.

A battle ending, a same-bar phase change, or a genuine fresh-HP boss form does **not** by itself restore a spent Prime.

## Recovered Story Prime
- manifests in the current ordinary round;
- performs exactly one strong Recovered signature action;
- dismisses in that same ordinary round;
- does not create a persistent three-round body.

## Awakened Prime
- replaces/suspends the active ordinary party;
- is directly controlled for exactly **3 Prime rounds**;
- receives **1 selected Prime command per Prime round**;
- the ordinary party does not act or become targetable during normal Prime rounds;
- party Standard Cards/Items do not operate from off-field unless an explicit Prime effect says so.

### Ordinary Field interaction
Awakened Prime rounds are not normal party rounds.

Therefore, under the global Field lifecycle in `05_BATTLE_SYSTEM/FIELDS.md`:
- ordinary numbered-round Fields remain recorded while the party is suspended;
- Prime rounds do not consume normal-round Field duration checkpoints;
- an ordinary party-authored Field does not automatically treat the manifested Prime body as a normal conscious party member or ally target;
- a Field affects the Prime only where the Field or Prime effect explicitly says it does.

### Ordinary temporary-stat interaction
Awakened Prime rounds also do not consume normal-round temporary Attack/Magic/Defense/Spirit/Speed durations on the suspended party.

Therefore, under `05_BATTLE_SYSTEM/STAT_CHANGES.md`:
- ordinary party temporary core-stat modifiers remain recorded while the party is suspended;
- Prime rounds do not consume those normal-round duration checkpoints;
- suspended-party stat modifiers do not automatically modify the manifested Prime body;
- when the party returns, those modifiers resume with the same remaining duration they had when suspension began.

Prime-local temporary core-stat modifiers use their authored Prime-round/action window and disappear on dismissal unless a command explicitly creates a separate return-to-party effect.

For migrated/current Prime wording, a Prime-local core-stat modifier described only as lasting through an `authored window`, `next window`, or `next-Prime-round window` means:
> **active immediately through the end of the next Prime round, or until dismissal if dismissal occurs first**

Return-to-party stat effects begin when the ordinary party returns and use normal-round timing under `STAT_CHANGES.md`.

## Post-dismissal Prime spacing
After any Prime manifestation ends, the party must complete:
> **2 full normal party rounds**

before another available Prime may be invoked later in that battle.

The spacing gate does not restore the Prime that was just spent. It only controls when a different still-available Prime may be invoked.

## No boss-form refresh
Prime identity availability is not once-per-battle or once-per-fresh-form.

A genuine fresh-HP boss form does **not** refresh:
- a spent Prime identity;
- Prime restoration state;
- the requirement that Prime use returns only through a valid rest/restoration effect.

Same-bar phase changes likewise do not restore spent Primes.

Global fresh-form authority is in:
`05_BATTLE_SYSTEM/BOSS_FORM_RULES.md`.


## Final Severance story-resolution exception

The mandatory Chapter-13 Final Severance sequence occurs:
> **after The Last Command's combat body reaches 0 HP**

It is:
- a story-resolution manifestation sequence;
- not another selected combat Prime Invocation;
- not a third boss combat phase.

Therefore:
> combat spent/availability flags and the two-round Prime-spacing gate do not block the six required Story Prime manifestations in Final Severance.

Combat Prime rules remain unchanged during the actual fight.

Final Severance order:
> HOLD → DISTINGUISH → MAP → PRESERVE → CONTAIN → END
