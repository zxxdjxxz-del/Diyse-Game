# Diyse — Card System Master

**Status:** ACTIVE CARD-SYSTEM AUTHORITY  
**Authority:** current Card/Prime-domain owner plus later explicit approved corrections.  

## Collection

Exactly:

- **24 Standard Cards**
- **12 Prime Cards**
- **36 total collectible Card identities**

There are no duplicate-rank, Essence, generated-card, Card-XP, or material-upgrade progression systems.

## Lived-world baseline

**Standard Cards are a normal, known part of modern magical life.** They are known Ancient Diysean magical artifacts that preserve abilities a current holder/user can access. Prime Cards are the exceptional, historically uncertain layer; player/system knowledge of Prime mechanics is not automatically character knowledge.

Story-facing knowledge remains governed by the world/lore knowledge firewalls.

## Current Faces

Exactly:

- Might
- Elements
- Grace
- Perception
- Memory
- Ruin

System-level combat lanes are owned jointly with `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`:

- **Might:** physical force, impact, aggression, vitality
- **Elements:** elemental offense and affinity interaction
- **Grace:** healing, protection, recovery, stability
- **Perception:** precision, criticals, opportunistic timing, especially Interrupt
- **Memory:** Quick, Slow, Delay, Stuck, duration manipulation, delayed/echo effects, controlled recall/copy
- **Ruin:** destructive, degrading, dangerous/high-risk effects

Perception emphasizes precision, criticals, timing, and Interrupt. Memory emphasizes timing/duration manipulation and controlled recall/copy.

## Standard Cards — structural rules

Each permanent character has exactly **4 Standard Card slots**.

Unlocks:

- Base CL1
- Base CL4
- Base CL8
- Base CL12

Standard Cards:

- use the normal selected TURN/action framework;
- are reusable while equipped and legal;
- use normal MP rather than charges or a separate Card gauge;
- have no default per-battle use limit;
- are unique named Cards with no duplicates;
- may be assigned to only one character at a time;
- are assigned outside battle and cannot be reassigned mid-battle;
- grant at least a visible stat bonus, passive effect, or both while equipped;
- retain their character-bound stat/passive benefits while that character is in reserve, except a passive affects the active party from reserve only when explicitly authored;
- use **Intelligence** for all scalable Standard Card numerical output where scaling applies;
- generally cost more MP than comparable native Abilities;
- use the global TURN / EXECUTION system unless explicitly authored otherwise.

Exact Standard Card effects, MP costs, timing, Potencies, equipped bonuses/passives, Face distribution of individual mechanics, and Memory copy/recall eligibility are intentionally parked for the dedicated Card-content pass.

## Prime Cards — current battle foundation

Exactly:

- 6 Story Primes
- 6 Major-Hunt Primes

Story Prime progression:

**Recovered → Awakened**

Major-Hunt Primes are acquired Awakened. Awakened is final.

Prime progression does not use Prime XP, permanent Prime levels, duplicates, material upgrades, or a third progression state.

Prime Invocation costs **0 MP** and consumes the invoking character's current command opportunity. Prime commands cost **0 MP** unless a specific Prime explicitly defines another internal restriction.

Each Prime identity has **1 use until restored**. Spent/Ready state persists across battles.

Valid restoration includes:

- full rest;
- checkpoint-area restoration;
- an explicitly authored Prime-restoring effect;
- Emergency Kit, which restores every acquired Story and Major-Hunt Prime to Ready without changing progression state.

Same-bar phase changes and genuine fresh-HP enemy bodies/forms do **not** automatically restore Prime uses.

## Prime loadout

- Chapter 4 Prime battle-loadout access: **1 Prime slot per permanent character**
- after Sixfold Volition at the end of Chapter 7: **2 Prime slots per permanent character**
- Standard Card slots and Prime slots are separate systems
- Story bearer/Face association is narrative/thematic, not an owner-lock
- any acquired Story Prime may be equipped/invoked by any eligible active permanent through the slot system
- Major-Hunt Primes are not owner-locked

## Prime manifestation structure

### Recovered

A Recovered Story Prime manifests, performs its single signature action, and demanifests immediately.

Recovered does not use the Awakened Manifestation Meter.

### Awakened

Every Awakened Prime manifestation begins with a **3-segment Manifestation Meter**.

- Basic = 1 segment
- Medium = 2 segments
- Heavy = 3 segments

Standard Awakened kit structure:

**2 Basic / 2 Medium / 1 Heavy / 1 automatic Dismissal**

Meter is spent only when the selected command successfully reaches EXECUTION.

When a command empties the meter, the Prime enters **Final Return** and stays manifested until its already-scheduled next TURN. At that TURN its automatic Dismissal ability resolves and the party returns.

The active party is suspended during Awakened manifestation while enemies continue their normal TURN / EXECUTION progression.

Detailed Invocation, meter, Final Return, party suspension, targeting transitions, KO/removal, early dismissal, scaling, restoration, and status/control rules are owned by `PRIME_CARDS/PRIME_SYSTEM_RULES.md`.

## Post-Prime lockout

After any Prime demanifests, Prime Invocation enters a **party-wide lockout measured by the invoking character's next 3 personal TURNs**.

- invoking character is the cooldown owner;
- nobody may manifest any Prime during the lockout;
- the owner's hidden reserve TURNs count;
- queued EXECUTION markers do not count;
- a denied owner TURN counts if the TURN occurred;
- restoring a spent Prime does not bypass an active lockout.

Exact individual Prime kits remain the next Prime content/rebalance pass.
