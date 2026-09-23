# Watch Ballista

**Current use:** Chapter 1 — Hollow Watch; Chapter 3 — Cresthaven Ancient tower base carryover  
**Status:** **POWER COMPLETE / RAW BODY AUTHORED**

This file owns the ordinary Hollow Watch fixture.

The stronger **Fortress Ballista** used by Hollow Watch Castellan remains separately owned by:
`../STORY_BOSSES/HOLLOW_WATCH_CASTELLAN.md`

## Ordinary fixture body
| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 170 | 40 | 0 | 22 | 18 | 18 | 0 | 10 |

True construct:
> **Bleed Immune**

## Actions

### Snap Bolt
- one party member
- Physical / Neutral
- **135 Power**
- Base Hit **90**
- no harmful-status rider

After firing:
> next selected Ballista action is **Reload**.

### Marked Heavy Bolt
Requires a completed Watch Sentry **Targeting Signal** at beginning-round.

- fixed marked target
- Physical / Neutral
- **200 Power**
- Base Hit **95**
- **10% Bleed**
- consumes the completed signal

If the fixed target is no longer legal when resolution occurs:
> the marked shot fails rather than retargeting.

After firing or failing:
> next selected Ballista action is **Reload**.

### Reload
> **Power: N/A — no direct damage**

The Ballista cannot fire during Reload.

## Formation teaching role
This implements the Chapter-1 authored beat:
> Sentry marks the shot → player can kill or interrupt the Sentry → Ballista's heavier attack is prevented.

## Chapter-1 behavior lock
Priority order:
1. if Reload is pending, Reload is forced;
2. otherwise, if this Ballista owns a completed Targeting Signal at beginning-round, Marked Heavy Bolt is forced;
3. otherwise use Snap Bolt.

A Ballista may own at most one completed signal at a time.

With two Ballistae and one Sentry:
- only the signaled Ballista gains Marked Heavy Bolt;
- the other Ballista continues its ordinary Snap Bolt / Reload cycle.

Single-target Snap Bolt selection is equal among conscious active party members.
No hidden focus-fire rule is added.


## Chapter-3 Cresthaven carryover lock — 2026-09-23
Watch Ballista returns as an ordinary fixture construct in the **Cresthaven Ancient tower base**.

The established linked behavior remains:
- Snap Bolt;
- Marked Heavy Bolt after a completed Watch Sentry Targeting Signal;
- Reload after firing.

Chapter-3 placement:
- Tower Foundation — primary fit;
- Command Interior — eligible where fixed defensive emplacements make spatial sense;
- not used in the final Warden Chamber.

Do not convert the Ballista into a mobile construct.

Chapter-3 body/tuning requires fresh validation and must not blindly reuse the Chapter-1 raw body.


## Naming correction — 2026-09-23
This reusable Ancient-defense chassis is no longer named after the Hollow Watch location.

Current canonical identity:
> **Watch Ballista**

The former Hollow Watch-specific name is retired.
