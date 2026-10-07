# Diyse — Standard Card UI

**Status:** ACTIVE UI / IMPLEMENTATION SPEC  
**Authority:** Card behavior defers to `../07_CARDS/CARD_SYSTEM_MASTER.md` and `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`.  

## Standard Card loadout

Each permanent character has exactly **4 Standard Card slots**.

Unlocks:

- Base CL1
- Base CL4
- Base CL8
- Base CL12

Cards are unique, reusable, selected actions, MP-consuming, and not charge-based.

Every equipped Standard Card must be able to display its equipped stat bonus/passive benefit as well as its active-use effect.

## Card display

The Card UI should be able to communicate:

- name;
- Face;
- equipped character/slot;
- equipped stat bonus/passive;
- MP cost;
- Execution category;
- Return category;
- target pattern;
- Potency or fixed magnitude where relevant;
- physical/magical/other output type where relevant;
- element where relevant;
- crit eligibility where relevant;
- status/timeline rider;
- Interruptible / Delay-only / Uninterruptible classification where the action queues.

Do not use legacy Power/Base-Hit fields as universal current requirements.

## No deck UI

Do not implement draw pile, hand, discard, shuffle, deck-size, duplicate-rank, Card-XP, fusion, or random Card-generation surfaces.

## Prime boundary

Prime slots are separate from the four Standard Card slots. Prime loadout and battle availability use the current Prime UI/spec rather than pretending a Prime consumes a Standard Card slot.
