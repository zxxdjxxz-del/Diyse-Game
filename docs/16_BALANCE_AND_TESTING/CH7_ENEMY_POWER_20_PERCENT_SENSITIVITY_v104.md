# Diyse — Chapter 7 Enemy Direct-Damage Power +20% Sensitivity — v104

**Status:** **WORKING SENSITIVITY / NOT OWNER CANON**  
**Parent:** `GLOBAL_ENEMY_POWER_20_PERCENT_SENSITIVITY_v104.md`  
**Primary boss:** Warden of the Nameless / Revision Arbiter  
**Purpose:** determine whether the proposed global `enemy direct-damage Power ×1.20` baseline is sufficient for an already true-battle-certified midgame climax.

This is design-layer stochastic balance testing, not runtime-engine QA.

---

# Route anchors
Current owner / v100 true-battle authority:
- mandatory pre-Warden — **Lv30**;
- completionist fixed-content — **Lv34**;
- high side — ~Lv35;
- one continuous 7,600-HP boss body;
- Closed Record → Adjudication → Open Revision;
- no fresh HP body.

The user-directed recalibration rule now supersedes the old equipment-comparison philosophy:
> **mandatory and completionist use the same ordinary equipment in the core difficulty comparison.**

The v100 strict mandatory equipment reference is therefore reused for both levels:
- Cyanis — Crestblade / Crest Plate / Yahtrean Shield;
- Ilyra — Wardrod / Blue Warden Mail / Warding Focus;
- Torren — Yahtrean War Bow / War Archer Gear;
- Vaelira — Arcanist Staff / Green Arcanist Garb.

No Relic/Legacy advantage is given to the Lv34 line.

---

# Current v100 danger baseline
The exact existing v100 true-battle result was:

Mandatory Lv30, no Prime:
- **20,000 / 20,000 wins**;
- median **11 rounds**;
- mean 10.76;
- **1 / 20,000 any-KO = 0.005%**;
- **0 defeats**;
- mean ending combined HP ~66.35%.

Completionist Lv34 in the old report was also 100% wins / 0% any-KO, although that older line used a stronger ordinary equipment reference and is not used as the new same-gear comparison.

Under the new mandatory-route philosophy:
> **the existing v100 difficulty is far too safe.**

---

# ×1.20 direct-Power conversion

Adjudication:
- Name Redaction — 220 → **264**;
- Registry Pulse — 145 AoE → **174**;
- Severing Writ — 205 → **246**;
- Revision Lance — 245 → **294**.

Open Revision:
- Open Revision Lance — 280 → **336**;
- Identity Severance — 270 → **324**;
- Rewrite Wave — 180 AoE → **216**;
- Recursive Judgment — 2×140 → **2×168**.

Unchanged:
- HP / raw stats;
- Assertion/Open Revision layer counts;
- 80% / 40% direct-damage reductions;
- Revision Claim magnitude/duration;
- Reconciliation Order / Final Reconciliation magnitudes;
- status chances;
- repetition locks;
- action count;
- Prime rules.

---

# Action-density observation
The harder recalibration exposes another reason the boss is safe.

Adjudication legal selected actions include:
- 4 direct-damage actions;
- Reconciliation Order — non-damaging;
- Revision Claim — non-damaging.

Where no exact weights override the fallback, uniform selection can therefore spend roughly one-third of ordinary Adjudication selections on non-damaging action-tax/support turns.

Open Revision contains:
- 4 direct-damage actions;
- Final Reconciliation — non-damaging.

So roughly one-fifth of fallback Open selections can also be non-damaging.

Unlike the Deepforge/Zevraya inversion problem, Revision Claim and the Reconciliation actions are intentionally part of the boss identity and should not automatically be converted into passive extra effects. However, their frequency is an important local tuning lever.

---

# Calibrated ×1.20 true-battle sensitivity
A design-layer harness was calibrated so the current-Power Lv30 line returns to approximately the established v100 **11-round median** before applying the scalar.

10,000-run same-gear references:

## Current fallback selection
### Lv30 mandatory — current Power
- 100% wins;
- median **11**;
- ~**0.04% any-KO** in the calibrated harness;
- 0 wipes.

The harness is slightly more KO-prone than the historical exact v100 0.005% result but remains in the same overwhelmingly-safe regime.

### Lv30 mandatory — ×1.20
- **100% wins**;
- median **11**;
- ~**0.25% any-KO**;
- **0 wipes observed**;
- mean ending combined HP falls from roughly 62.6% to roughly **59.1%**.

### Lv34 completionist — same equipment — ×1.20
- **100% wins**;
- median **10**;
- ~**0.01% any-KO**;
- 0 wipes observed.

Verdict:
> **×1.20 is nowhere near sufficient by itself for this boss.**

---

# Modest damage-favoring AI sensitivity
A local selection sensitivity was also checked without granting extra turns:
- Adjudication damaging-action group favored approximately 75%;
- action-tax/support group approximately 25%;
- Open Revision damaging group approximately 80%;
- Final Reconciliation approximately 20%.

At ×1.20 this modest weighting shift did **not** materially solve the problem; mandatory KO incidence remained around the same sub-1% regime.

Interpretation:
> merely nudging the action weights is insufficient while the total punishment package remains this forgiving.

---

# Power-only escalation sanity check
To determine whether the answer should be a larger universal scalar, the same calibrated mandatory harness was run with progressively larger boss-only direct-Power multipliers.

Approximate Lv30 mandatory any-KO sensitivity:
- ×1.20 — ~**0.2%**;
- ×1.30 — ~**0.6%**;
- ×1.40 — ~**1.1%**;
- ×1.50 — ~**2.6%**;
- ×1.60 — ~**5.0%**, with only a tiny observed wipe tail.

This is decisive evidence against raising the **global** enemy scalar above 20% merely to fix bosses.

A +60% whole-roster scalar would be grossly inappropriate for ordinary formations and other encounters that already respond well to +20%.

---

# Chapter-7 boss read

Revision Arbiter should be reopened locally under the new standard.

The correct direction is not:
> raise every enemy in the game by 40–60%.

The correct direction is:
> **retain the global ×1.20 floor, then strengthen this boss's local pressure architecture.**

Potential local levers for a later dedicated retune include:
- stronger consequences for leaving Revision Claim unresolved;
- more meaningful Reconciliation Order / Final Reconciliation setup-payoff;
- damage-action weighting that becomes more aggressive at Open Revision;
- dangerous combinations that reward correct command variation rather than simply adding HP;
- a more threatening Open Revision state while preserving the one-bar identity and action-tax theme.

Do not automatically convert Revision Claim or Reconciliation effects into free extra actions; that would need a dedicated boss-design pass.

---

# Current Chapter-7 verdict

> **GLOBAL ×1.20 STILL VIABLE / REVISION ARBITER REMAINS FAR TOO SAFE / LOCAL BOSS RETUNE REQUIRED**

Across Chapters 5–7, the emerging pattern is now consistent:
- ordinary enemies respond well to the +20% floor;
- structurally sound Deepforge reaches a good mandatory/completionist profile at +20%;
- Furnace Tyrant and Crownstorm Roc remain too safe;
- Zevraya reaches a strong profile once support-object action-density inversion is removed;
- Revision Arbiter remains dramatically too safe even after +20%.

This supports a two-layer balancing model:
1. **global enemy direct-damage Power floor around ×1.20**;
2. **boss-specific pressure/mechanic tuning on top of that floor.**

Next representative step:
> continue the ×1.20 sensitivity into later chapter climaxes, then return to the weak-boss list for dedicated local retunes rather than inflating the global scalar further.
