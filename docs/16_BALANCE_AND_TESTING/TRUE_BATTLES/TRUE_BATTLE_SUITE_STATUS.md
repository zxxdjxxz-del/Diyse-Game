# Diyse — Representative True-Battle Suite Status
**v100**

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
3. **Regulation Crucible → The Seventh Reaction — Chapter 4 / S024** — **v99 PASS / RETAIN**
   - strict mandatory Lv15 prepared, no Prime: **100% wins / median 18 / mean 17.78 / P90 19** over 5,000 runs;
   - strict mandatory Lv15 prepared + one Recovered Last Sentinel use in Form II: **100% wins / median 14 / mean 14.18 / P90 16** over 5,000 runs;
   - chamber-control mandatory line, no Prime: **100% wins / median 18 / mean 18.34 / P90 20** and harmful-status load reduced from ~2.54 to ~0.33 per run;
   - completionist Lv17 reference: median **13** with Last Sentinel / **16** without;
   - fresh Form II does **not** restore a spent Prime identity;
   - representative strict mandatory no-Prime Round-18 clear recorded;
   - Form-I HP2,400 / Form-II HP2,900 / raw stats / Powers retained.
4. **Warden of the Nameless / Revision Arbiter — Chapter 7 climax** — **v100 PASS / RETAIN**
   - strict mandatory Lv30 prepared, no Prime: **100% wins / median 11 / mean 10.76 / P90 12** over 20,000 runs;
   - strict mandatory Lv30 + one Awakened Last Sentinel manifestation: **100% wins / median 9 total combat rounds / mean 9.43 / P90 11** over 10,000 runs;
   - strict no-Prime any-KO incidence: **0.005% (1 / 20,000)** with **0 defeats**;
   - completionist Lv34 upgraded-ordinary reference: **100% wins / median 8 / mean 8.01 / P90 9** over 5,000 no-Prime runs;
   - completionist Lv34 + Last Sentinel: **100% wins / median 8 / mean 7.86 / P90 9** over 5,000 runs;
   - opening Assertion Layers, Revision Claim command variation, and Open Revision Layers all remained behaviorally relevant;
   - HP7,600 / raw stats / Powers / layer counts / repetition locks retained unchanged;
   - detailed certification: `REVISION_ARBITER_TRUE_BATTLE_v100.md`.

## Next representative anchors
5. **Commander Rhazek — Reforged Commander → Bastion Devourer — Chapter 9** — next chronological genuine-fresh-body / persistent-Prime-spend test.
6. **Calder → Crown-Bound Living Anchor** — later two-form/support-object test.
7. **Vaelkor → Sovereign Panoply Unbound** — late mandatory full-system test.
8. **Reconstituted Entity → The Last Command** — final mandatory test.
9. **The Unfinished World** — exhaustive completionist full-kit stress test.

The suite remains **ACTIVE**. Do not mark runtime QA complete from these design-layer simulations.

## v96 Bleed escalation rule impact
- Bleed starts at **3% Max HP per qualifying proc**.
- After the affected unit completes **3 turns with the same Bleed uncleared**, magnitude escalates to **4% Max HP per qualifying proc** until removal.
- Regional Hunt magnitude becomes 2.25% → 3%; Major Hunt / mandatory boss magnitude becomes 1.5% → 2%.
- Hollow Watch Castellan remains **PASS / RETAIN** for its normal/smart primary line because the Ballista is destroyed before Heavy Bolt resolves.
- The v93 Aggressive support-ignore KO/Bleed percentages remain historical and must be refreshed before being cited as current risk metrics.
- All subsequent true-battle simulations must use the v96 Bleed escalation rule.
