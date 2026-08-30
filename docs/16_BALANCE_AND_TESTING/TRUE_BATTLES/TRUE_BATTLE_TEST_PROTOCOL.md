# Diyse — Canonical True-Battle Test Protocol
**v93**

This layer is distinct from the completed paper mandatory-vs-completionist certification. A true-battle test resolves actual rounds, action order, MP, healing, targeting, Hit/Evasion, Criticals, statuses, support objects, phase transitions, Cards, Primes, Traits, Masteries, equipment, and legal consumables as applicable.

## Snapshot rules
For each boss test, define before combat:
- exact Character Level and Class Level for every available permanent character;
- active four (or smaller forced story party);
- selected class and therefore selected Trait/stat package;
- equipment actually available at that story point;
- legal learned persistent Abilities and Masteries;
- equipped Standard Cards and Prime slots only if already acquired;
- consumables carried;
- starting HP/MP and encounter-specific forced states.

## Mandatory baseline
Use only critical-path progression and deterministic mandatory acquisitions available by that encounter. No optional Hunt/CQ/side-quest rewards unless mandatory for the encounter.

## Completionist baseline
Use all legal optional progression/rewards reasonably obtainable before that encounter, respecting actual unlock timing and the level cap.

## Boss-isolation benchmark
Representative boss simulations may begin at full HP/full MP to isolate encounter tuning unless the encounter explicitly owns incoming attrition or a preceding sequence. A separate attrition stress run can be added where needed.

## Stochastic resolution
Where actions/targets/hits/crits/statuses are random, record both:
1. at least one full turn-by-turn representative battle log; and
2. a repeated-run distribution using the exact same tactical policy.

Do not treat a single lucky/unlucky roll as balance authority.

## Player tactical policies
At minimum test a sensible **normal/smart** policy. Add aggressive/safety variants when encounter architecture makes those strategically distinct. Player policy may react only to information legitimately visible at the time.

## Retune rule
Do not reopen a closed Power/stat sheet merely because one stochastic run is strange. Retune only when repeated true-battle outcomes show a structural failure: excessive/insufficient duration, unavoidable death spiral, irrelevant mechanics, resource collapse, trivialization, or a mandatory/completionist inversion outside the intended tier.
