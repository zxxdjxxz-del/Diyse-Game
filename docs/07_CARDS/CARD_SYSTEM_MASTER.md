# Diyse — Card System Master
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary Card/Prime authority:** compatible **Audit116**, superseded where applicable by **Audit119**, **Audit122**, later current v85 working closures, and newer explicit user corrections.  
**Current written whole-project authority:** **v2.20 / Audit135** plus newer approved corrections.

## Collection size
Exactly:
- **24 Standard Cards**
- **12 Prime Cards**
- **36 total collectible Card identities**

No additional Card rank, duplicate, Essence, upgrade-material, or generated-card progression exists.

## Standard Cards
Standard Cards:
- use one normal selected action;
- are reusable;
- cost MP;
- have no charges;
- have no per-battle use limit;
- do not use deck / hand / draw / discard / shuffle systems;
- do not summon independent collectible manifestations;
- use exactly **3 Standard Card equip slots per character**.

Standard Cards are Ancient Diysean artifacts. Modern enemies do not create them. A battle or exploration reward may expose, release, recover, or grant access to a pre-existing Card.

## Prime Cards
Prime Cards are the collectible manifestation layer.

Exactly:
- 6 Story Primes;
- 6 Major-Hunt Primes.

Prime progression:
> **Recovered → Awakened**

Awakened is final.

Removed:
- Concordant as a progression stage;
- Reactive temporary tracker state;
- Prime XP;
- Prime levels;
- duplicate progression;
- Prime upgrade materials;
- third-stage progression.

Current Invocation MP:
> **0 MP**

Manifested Prime commands also cost **0 MP**.

Each Prime identity has **one use until restored** by a valid rest or other explicitly authored Prime-restoration effect. A spent Prime remains spent across battle end; using one Prime does not spend other available Primes.

After a Prime manifestation ends, **2 full normal party rounds** must pass before another available Prime may be invoked later in the same battle.

Fresh-HP boss forms do not restore spent Primes.

Awakened manifestation turn flow is owned by `../05_BATTLE_SYSTEM/PRIME_ROUND_SEQUENCING.md`.

## Standard vs Prime loadout
Standard Card slots and Prime slots are separate systems.

Current direct project lock:
- from Chapter 4 Prime-battle loadout access until Sixfold Volition, each permanent character has **1 Prime slot**;
- after Sixfold Volition, each permanent character has **2 Prime slots**;
- any acquired Prime may occupy those slots;
- Story bearer/Face association is narrative/thematic, not an owner-lock;
- Major-Hunt Primes are likewise not owner-locked.

## Face distribution
The current six Faces are:
> **Might / Elements / Grace / Perception / Memory / Ruin**

Standard Cards intentionally use an uneven distribution:
- Might — 5
- Elements — 5
- Grace — 4
- Perception — 4
- Memory — 3
- Ruin — 3

Each Face still has:
- 1 Story Prime;
- 1 Major-Hunt Prime.

Perception covers Accuracy-oriented effects under the current Base Hit system, Evasion, Critical Hits, and Fields: battlefield reading, positioning, timing, openings, and controlling/exploiting space.

Memory covers recall, repetition, preservation, and reuse of prior actions/states: what has happened remaining available to influence the present.

## Removed Card-system firewalls
Do not restore:
- Resource, Acuity, or Change as current Face names;
- Card Seals;
- Standard Card summons;
- Imprints as a global Card dependency;
- Composite Reaction as a global Card subsystem;
- Break/Stagger meter contributions;
- Water/Wind standard-element Card language;
- old unlimited-use wording interpreted as zero MP.
