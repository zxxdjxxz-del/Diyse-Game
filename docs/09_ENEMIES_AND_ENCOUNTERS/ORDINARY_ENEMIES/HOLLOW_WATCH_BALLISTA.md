# Hollow Watch Ballista

**Chapter:** 1 — Hollow Watch ordinary fixture  
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
Requires a completed Hollow Watch Sentry **Targeting Signal** at beginning-round.

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
