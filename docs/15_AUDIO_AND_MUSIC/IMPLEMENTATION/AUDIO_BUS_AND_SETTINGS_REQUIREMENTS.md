# Diyse — Audio Bus / Settings Requirements

**Status:** ACTIVE AUDIO IMPLEMENTATION REQUIREMENTS  
**Parent authority:** `../AUDIO_AUTHORITY_MASTER.md`

Exact Godot bus layout is OPEN.

At minimum, production should be able to control user-facing volume categories for the audio types that actually ship.

Likely categories may include:
- Master;
- Music;
- SFX;
- Voice

but even this exact naming/number of sliders is not locked until voice scope is decided.

## Requirements
- volume settings persist if implemented;
- lowering music must not mute critical combat/UI readability SFX;
- dialogue/voice must remain intelligible;
- loud boss/Prime events must not create unsafe clipping;
- device speaker playback must remain usable.

## Android
Mix decisions should be validated on:
- phone speakers;
- common earbuds/headphones;
- not only studio monitors.

Exact loudness/mastering targets:
> OPEN.
