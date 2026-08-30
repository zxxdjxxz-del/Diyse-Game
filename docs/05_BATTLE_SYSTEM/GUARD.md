# Diyse — Guard and Defensive-State Boundary
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current domain authority checked:** repository `docs/COMBAT_RULES.md`, current through **v2.20 / Audit135**, plus compatible Audit115, Audit120, Audit122, Audit135 and newer explicit user corrections.  
**Recovered implementation evidence:** the pre-reorganization proof resolver used the standard Defend state to halve eligible incoming direct damage and cleared that state at the next round boundary.  
**Migration rule:** current explicit user corrections and current organized domain canon outrank stale/open wording inherited by v85.

## Current status

**Guard remains a valid defensive state.**

Guard is **not** a harmful status.

The permanent player command list contains **Defend**.

## Standard Guard / Defend — exact rule

When the permanent **Defend** command resolves, the acting character enters the standard **Guard** state.

Standard Guard grants:

> **50% reduction to eligible incoming direct HP damage**

from the moment Defend resolves through the end of the current normal round.

The standard Guard state is cleared during the round transition before the next round's normal actions begin.

Therefore under the current turn-entry battle flow:
- Defend is chosen only when that character's normal Speed-ordered turn arrives;
- Guard begins when that Defend action resolves;
- attacks or other damage that resolved earlier in the same round are not retroactively reduced;
- eligible direct damage received later in the same round is reduced by 50%;
- Defend has no separate priority band and does not move the character earlier in initiative;
- a slower character may therefore receive damage from faster enemies before having the opportunity to establish Guard.

This timing is intentional under the current Speed-ordered system.

## What standard Guard reduces

Standard Guard applies to eligible ordinary **direct** Physical, Magical, and Hybrid HP damage after the normal direct-damage calculation.

Standard Guard does **not** reduce, unless an explicit owning effect says otherwise:
- Burn;
- Bleed;
- other indirect damage;
- fixed damage;
- percentage-Max-HP damage;
- healing/revival effects.

Critical hits do not bypass Guard; an eligible Crit is still direct damage and the active direct-damage-reduction layer applies to its resulting direct damage.

## Other authored Guard states

An enemy action, Ability, Card, Prime command, equipment effect, or encounter rule may explicitly establish a different Guard magnitude or duration.

If it prints another exact value or timing window, that authored value/window overrides the standard 50%-through-round-end default for that specific Guard state.

Merely using defensive flavor language does not create Guard. The effect must explicitly establish Guard or an explicit direct-damage-reduction state.

## Direct-damage-reduction interaction

Standard Guard participates in the global direct-damage-reduction layer defined in `DAMAGE_FORMULAS.md`.

Multiple active direct-damage-reduction percentages do **not** add or multiply together by default. Use the strongest active legal reduction unless an owning effect explicitly defines a special stacking exception.

Therefore, for example, standard Guard's 50% reduction supersedes a simultaneous ordinary 10% or 15% direct-damage-reduction effect while Guard remains active. The weaker effect keeps its own duration and resumes if it remains active after Guard ends.

Defense/Spirit percentage changes and direct-damage reduction are separate layers. Legacy `Total Defense` wording is only shorthand for equal percentage Defense/Spirit changes under `STAT_CHANGES.md`; it is not its own defensive layer. Guard does not grant Defense or Spirit unless an effect explicitly says it does.

## Prepared defensive/reaction states

Prepared reactions such as explicitly authored intercepts/counters are established when their preparing action resolves on that actor's turn.

They may respond to later eligible actions according to their authored trigger/duration, but they do not retroactively apply to actions that resolved before the Prepared state was established.

## Interception

Interception is not a free universal reaction system.

Where an encounter/effect supports interception or redirection, it must come from an explicitly established authored state/effect rather than being assumed for every defender.

## Firewall

Do not substitute or reintroduce:
- Brace;
- Barrier;
- global Break/Stagger meter;
- hidden stability/posture gauges.
