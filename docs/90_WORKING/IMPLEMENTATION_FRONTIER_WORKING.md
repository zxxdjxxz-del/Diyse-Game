# Working — Implementation Frontier

**Owner:** `13_UI_AND_IMPLEMENTATION`

## High-impact reconciliation
1. remove Mastery Point assumptions from production state/UI;
2. replace stale bearer-locked `first_champion` Prime proof behavior;
3. implement current Prime loadout/state/economy exactly:
   - 1 Prime slot per permanent character before Sixfold Volition, 2 after;
   - Recovered → Awakened progression only;
   - Invocation and manifested commands cost 0 MP;
   - each Prime identity has one use until restored by valid rest or an explicitly authored restoration effect;
   - spent state persists across battle end;
   - 2 full normal party rounds must pass after demanifest before another available Prime may be invoked in that battle;
   - fresh-HP boss forms do **not** restore spent Primes;
4. migrate proof `gold` semantics to player-facing **G** with version-safe save handling; **Auren is retired and must not be restored as a second or replacement ordinary shop currency**;
5. replace proof item/equipment/party fixtures with current production data;
6. expand and version the production save schema;
7. reconcile stale chapter/scene-ID assumptions through the current Chapter-13 architecture;
8. build production menu/combat/loadout UI against current canon rather than proof-state structures.

## Test debt
Update stale automated Prime expectations before treating the suite as a current green gate, especially any tests that assume:
- MP-paid Prime invocation;
- bearer ownership locks;
- per-battle reset of spent Prime identities;
- fresh-form restoration;
- shorter/character-turn cooldown semantics.

## Rule
Do not build final UI or save behavior around proof-state structures known to be obsolete.
