# Diyse — Representative True-Battle Suite Status
**v97**

## Certified
1. **Hollow Watch Castellan — Chapter 1 / S008** — **PASS / RETAIN**
   - mandatory Lv2 and high-side Lv3 tested;
   - 20,000-run normal/safety/aggressive distributions;
   - representative turn-by-turn log recorded.
2. **Archive Leviathan — Chapter 2 / S013** — **v97 PASS / RETAIN**
   - mandatory Lv6 prepared: 100% wins / median 10 / mean 10.05 / 0.05% any-KO;
   - completionist/high-side Lv7 prepared: 100% wins / median 9 / mean 8.58 / 0% any-KO;
   - v96 Bleed escalation, exact healing/cleanse behavior, and deterministic Recorded Pattern trigger tested;
   - no HP, raw-stat, status-chance, or Power retune required.

## Next representative anchors
3. **Regulation Crucible → Seventh Reaction** — fresh-HP-form transition test.
4. **Revision Arbiter or Equal Mercy Arbiter** — midgame action-tax/control test.
5. **Rhazek → Bastion Devourer or Calder → Living Anchor** — late two-form test.
6. **Vaelkor → Sovereign Panoply Unbound** — late mandatory full-system test.
7. **Reconstituted Entity → The Last Command** — final mandatory test.
8. **The Unfinished World** — exhaustive completionist full-kit stress test.

The suite remains **ACTIVE**. Do not mark runtime QA complete from these design-layer simulations.


## v96 Bleed escalation rule impact
- Bleed starts at **3% Max HP per qualifying proc**.
- After the affected unit completes **3 turns with the same Bleed uncleared**, magnitude escalates to **4% Max HP per qualifying proc** until removal.
- Regional Hunt magnitude becomes 2.25% → 3%; Major Hunt / mandatory boss magnitude becomes 1.5% → 2%.
- Hollow Watch Castellan remains **PASS / RETAIN** for its normal/smart primary line because the Ballista is destroyed before Heavy Bolt resolves.
- The v93 Aggressive support-ignore KO/Bleed percentages remain historical and must be refreshed before being cited as current risk metrics.
- All subsequent true-battle simulations must use the v96 Bleed escalation rule.
