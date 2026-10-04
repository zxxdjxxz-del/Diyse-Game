# Diyse — Current Balance Risks / Watchlist

**Status:** ACTIVE BALANCE RISK REGISTER  
**Domain authority:** `../README.md`

## 1. Enemy/boss action-kit and difficulty rebuild — ACTIVE

Current encounter identities/architecture remain useful, but enemy abilities, direct-damage Powers, and difficulty certification are reopened. Current tuning must be recertified from current inputs.

## 2. EXP / CEXP completion timing — ACTIVE DOWNSTREAM

Exact reward placement is provisional. **Lv55–60** remains the target completion window, but final Player EXP/CEXP placement and character completion centers must be rerun after encounter/reward validation.

## 3. Prime proof runtime migration — ACTIVE

The executable combat proof still carries bearer-lock, duration, restoration, and manifestation assumptions that do not match current Prime authority. Current smoke/combat tests deliberately do not certify those mechanics, so production Prime migration must be followed by focused regression coverage from `../../07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md`.

## 4. Save schema / economy persistence — ACTIVE

Currency-key migration is complete: runtime/save state uses `rewards.g` and intentionally normalizes supported incoming `rewards.gold` save data. Remaining risk is the incomplete production save schema plus provisional economy/progression values while those rebuilds remain open.

## 5. Raw stats without full-game playtest — WATCH

Mathematical/static checks do not replace whole-game human playtesting for:
- resource attrition;
- build outliers;
- sequence-specific difficulty spikes;
- underused mechanics.

## 6. Optional overleveling — WATCH

Weak-enemy diminishing returns helps, but mandatory bosses do not dynamically scale. Test whether completionist progression trivializes too much mandatory content before cap.

Do not add dynamic scaling unless explicitly approved.

## 7. Prime burst / spacing — WATCH

Primes are per-identity limited: invocation and Prime commands cost **0 MP**, spent state persists until valid restoration, and boss form/state transitions do **not** refresh availability.

Test burst compression around saved Ready identities, the three-full-normal-round post-dismissal spacing gate, explicit restoration effects, and multi-form transitions.

## 8. Economy rebuild — OPEN

G payouts, prices, liquidity totals, fees, and derived campaign-cash targets remain provisional until the economy rebuild/recalibration closes them.

## 9. Final UI/audio/performance — OPEN

Production UX/audio can change perceived difficulty/readability even when numbers are correct.
