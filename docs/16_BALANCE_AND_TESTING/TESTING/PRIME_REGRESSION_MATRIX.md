# Diyse — Prime Regression Matrix
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


Required automated/integration cases:

1. Story Prime not acquired → unavailable.
2. Acquired Story Prime may be equipped by any legal permanent character slot.
3. Pre-Volition Prime-slot behavior follows current progression authority.
4. Post-Volition each character supports 2 Prime slots.
5. Recovered Story invocation costs 50 MP.
6. Recovered Story performs one signature action and dismisses same ordinary round.
7. Awakened Story costs 80 MP.
8. Major-Hunt Prime costs 90 MP.
9. Prime commands cost 0 additional MP.
10. Awakened Prime suspends four-person party.
11. Party cannot act during Prime rounds.
12. Party cannot be targeted during Prime rounds.
13. Exactly 3 Prime rounds.
14. Dismissal restores party battle state.
15. Same Prime identity cannot be invoked twice in same body.
16. After dismissal, cooldown counts 3 **full normal party rounds**.
17. Another unused Prime cannot bypass cooldown early.
18. Genuine fresh body refreshes Prime availability.
19. Same-bar state does not refresh.
20. Boss defeat ends battle; no cooldown check after victory.
21. Save/load must not persist transient in-battle Prime state unless a future battle-save feature explicitly requires it.
22. Old bearer-locked `first_champion` proof expectation must be removed from production tests.
