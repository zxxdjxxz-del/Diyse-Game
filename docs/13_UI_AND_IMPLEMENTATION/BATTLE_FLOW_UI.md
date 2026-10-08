# Diyse — Battle Flow UI

**Status:** ACTIVE UI SPEC  
**Gameplay authority:** `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md` and `../07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md`.

The battle UI presents the ordered **TURN / EXECUTION** timeline.

For a player TURN, the command surface must support:

> **Attack / Abilities / Cards / Item / Defend / Swap**

Prime Invocation is a separate special access path when legal.

Before confirming a selected action, the UI should show the projected EXECUTION position and projected next TURN where those values are knowable.

Queued enemy actions should expose current visible intent/targeting information and Delay/Interrupt eligibility according to battle authority.

## Prime flow

Recovered Story Prime:
- presents/resolves one signature action;
- does not open the Awakened meter HUD;
- demanifests after that action.

Awakened Prime:
- replaces the active party;
- shows a 3-segment Manifestation Meter;
- shows Basic / Medium / Heavy meter costs;
- spends meter only on successful EXECUTION;
- enters Final Return when meter reaches 0;
- keeps the Prime on field until its already-scheduled next TURN;
- resolves automatic Dismissal at that TURN;
- restores the suspended party afterward.

Detailed Prime HUD behavior is owned by `PRIME_UI.md`.
