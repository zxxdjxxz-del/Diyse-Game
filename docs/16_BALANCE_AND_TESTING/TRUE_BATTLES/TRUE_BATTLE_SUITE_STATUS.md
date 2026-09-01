# Diyse — Representative True-Battle Suite Status
**v103 WORKING — DIFFICULTY RECALIBRATION ACTIVE**

## Status change
The previous v93–v102 reports remain valid records of the exact snapshots/rules they measured.

However, the acceptance standard has changed:
> **The mandatory route should be materially harder, and optional progression should produce a clear reduction in KO/wipe pressure even when equipment is held constant.**

Therefore:
- prior mechanical findings remain useful evidence;
- prior duration measurements remain historical reference data;
- from Chapter 5 onward, prior **difficulty PASS / RETAIN** conclusions are provisional until rechecked under the new same-gear standard.

Do not proceed directly to final-boss difficulty certification under the old acceptance logic.

---

# New core comparison standard
For the main mandatory-vs-completionist comparison:
- use the **same ordinary equipment** on both routes;
- use the **same normal-stock consumables**;
- use the same active four and competent tactical policy;
- do not give the completionist route Relic/Legacy equipment merely to make it safer;
- allow the real Player-Level / CEXP / learned-ability difference created by optional play;
- test Prime-specific advantages separately.

Primary difficulty signals:
1. temporary-KO incidence;
2. wipe incidence;
3. ending HP/MP;
4. item/recovery pressure;
5. mechanic-response pressure;
6. duration secondarily.

---

# Current recalibration anchor
## Chapter 5 — Deepforge Colossus → Worldsmith Body
Working report:
`CH5_DEEPFORGE_DIFFICULTY_RECALIBRATION_WORKING_v103.md`

Same-gear route anchors:
- mandatory — **Lv20**;
- completionist — **Lv22**.

Current-package competent-policy sample:
- mandatory Lv20 — **100% wins / 0.095% any-KO** over 20,000 runs;
- completionist Lv22 — **100% wins / 0.005% any-KO** over 20,000 runs.

Verdict:
> **CURRENT PACKAGE TOO SAFE FOR THE NEW MANDATORY-ROUTE STANDARD**

Exploratory ~45% direct-Power sensitivity:
- mandatory Lv20 — **99.415% wins / 22.21% any-KO / ~0.585% wipes**;
- completionist Lv22, same gear — **100% wins / 4.135% any-KO**.

That candidate offensive range is promising but **not locked**.

The test also exposed a Deepforge assembly-payoff issue: removing Guard Press / Repair Arm can remove non-damaging boss actions and inadvertently increase attack density after the party spends turns dismantling those parts. Resolve that interaction before recertifying the encounter.

---

# Historical representative measurements
1. **Hollow Watch Castellan — Chapter 1 / S008 — v93**
   - historical measurement retained.
2. **Archive Leviathan — Chapter 2 / S013 — v97**
   - historical measurement retained.
3. **Regulation Crucible → The Seventh Reaction — Chapter 4 / S024 — v99**
   - historical measurement retained; Chapter 4 is not currently the first recalibration anchor.
4. **Warden of the Nameless / Revision Arbiter — Chapter 7 — v100**
   - old difficulty PASS provisional under the revised standard.
5. **Commander Rhazek → Bastion Devourer — Chapter 9 — v101**
   - old difficulty PASS provisional under the revised standard;
   - fresh-body / Prime-persistence findings retained.
6. **Emperor Vaelkor → Sovereign Panoply Unbound — Chapter 12 — v102**
   - old difficulty PASS provisional under the revised standard;
   - fresh-body / Overrun / Prime-persistence findings retained.

---

# Forward order
1. **Deepforge Colossus — Chapter 5** — resolve assembly payoff and lock new difficulty anchor.
2. Continue forward through later chapter climaxes using the same-gear mandatory-vs-completionist method.
3. Revisit Rhazek and Vaelkor under the new difficulty ramp.
4. **Reconstituted Entity → The Last Command** only after the late-game mandatory difficulty curve is anchored.
5. **The Unfinished World** remains the exhaustive completionist full-kit stress test.

The suite remains **ACTIVE / RECALIBRATING**. Design-layer simulations do not replace runtime QA.

## Current Bleed rule
All recalibration simulations continue using the current Bleed escalation rule:
- 3% Max HP per qualifying ordinary proc;
- escalates to 4% after three affected turns uncleared;
- mandatory-boss conversion 1.5% → 2%.
