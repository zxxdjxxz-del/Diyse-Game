# Diyse — Input & Control Rules

**Status:** ACTIVE UI / IMPLEMENTATION SPEC
**Authority:** current repository UI/implementation domain; cross-domain gameplay/content rules defer to their current numbered owner domains.

**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## IMPLEMENTED FOUNDATION
Current proof exploration supports:
- WASD;
- arrow keys;
- on-screen touch D-pad.

Dialogue:
- manual progression;
- current proof uses a NEXT button;
- player movement can be disabled while dialogue runs.

Combat proof currently supports:
- direct tap/click command buttons;
- target buttons;
- legacy explicit round confirmation.

The legacy proof round-confirm interaction is not current production battle-flow authority.

## CANON REQUIREMENT
Input must never create a different ruleset.

Touch, keyboard, controller, or future accessibility bindings must all resolve to the same:
- current acting-character command selection;
- selected target/content;
- per-turn action confirmation/resolution behavior;
- dialogue advance;
- menu operation.

Normal combat does **not** require a universal whole-party Confirm Round input. Commands are chosen when the relevant player's character turn arrives.

## Movement lock
Authored dialogue/cutscene states may disable field movement.

Loading, save UI, shops, and menus must not allow accidental field movement underneath modal UI.

## No dialogue choices
There is no input action for:
- dialogue response selection;
- tone selection;
- romance answer;
- morality answer.

## OPEN PRODUCTION UX
Not yet canonized:
- final gamepad support/bindings;
- remappable controls;
- touch-stick vs D-pad final choice;
- dedicated cancel/back placement;
- vibration/haptic behavior;
- hold-to-skip/fast-forward behavior;
- auto-advance dialogue mode.
