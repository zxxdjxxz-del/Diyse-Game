# Diyse — Audio Bus / Settings Requirements
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in current reorganized domains.  
**Music supersession authority:** later Complete Master Canon explicitly marks **ALL whole-project music OPEN / under separate redevelopment** and supersedes the older v1.53–v1.57 regional-music prescriptions as active canon.  
**Research preservation:** older approved/researched music material remains valuable development evidence but is **not automatically current soundtrack canon** unless explicitly promoted.  
**Runtime checkpoint:** `3fd07e92eda04f31ba613a654b3b1b28071f44e6`; no production music/SFX/audio asset library is present in the inspected Godot repository.


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
