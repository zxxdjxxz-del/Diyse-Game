#!/usr/bin/env python3
"""Generate the conservative Ilyra anime-body UAL motion proxy.

This modifies only skinned mesh vertex positions/materials in a copy of the UAL2
female mannequin GLB. It preserves the existing skeleton, skin joints, weights,
and inverse bind matrices so the Universal Animation Library remains directly
compatible.

This output is a motion/proportion prototype only. Ilyra's exact approved B00
remains the visual authority.
"""

from __future__ import annotations

import argparse
import json
import struct
from pathlib import Path

JSON_CHUNK = 0x4E4F534A
BIN_CHUNK = 0x004E4942


def smoothstep(a: float, b: float, x: float) -> float:
    t = max(0.0, min(1.0, (x - a) / (b - a)))
    return t * t * (3.0 - 2.0 * t)


def reshape_vertex(x: float, y: float, z: float) -> tuple[float, float, float]:
    # Modest anime head enlargement above the neck.
    head = smoothstep(1.49, 1.60, y)
    head_x = 1.0 + 0.095 * head
    head_z = 1.0 + 0.075 * head

    # Keep arms mostly unchanged; torso edits fade before the shoulder/arm span.
    torso_mask = 1.0 - smoothstep(0.28, 0.46, abs(x))

    # Slight athletic torso, intentionally subtle.
    chest = smoothstep(1.00, 1.18, y) * (1.0 - smoothstep(1.42, 1.52, y))
    chest_x = 1.0 + 0.018 * chest * torso_mask
    chest_z = 1.0 + 0.035 * chest * torso_mask

    # Natural waist: widen rather than exaggerating a pinched mannequin waist.
    waist = smoothstep(0.78, 0.90, y) * (1.0 - smoothstep(1.08, 1.20, y))
    waist_x = 1.0 + 0.055 * waist * torso_mask
    waist_z = 1.0 + 0.020 * waist * torso_mask

    # Slightly more stable athletic hips/upper thighs.
    hip = smoothstep(0.56, 0.72, y) * (1.0 - smoothstep(0.94, 1.04, y))
    hip_mask = 1.0 - smoothstep(0.38, 0.58, abs(x))
    hip_x = 1.0 + 0.025 * hip * hip_mask
    hip_z = 1.0 + 0.018 * hip * hip_mask

    # Reduce blockiness without changing bone lengths.
    leg = 1.0 - smoothstep(0.67, 0.83, y)
    leg_mask = smoothstep(0.05, 0.18, abs(x))
    limb_x = 1.0 - 0.018 * leg * leg_mask
    limb_z = 1.0 - 0.022 * leg * leg_mask

    arm_band = smoothstep(1.10, 1.26, y) * (1.0 - smoothstep(1.48, 1.58, y))
    arm_outer = smoothstep(0.42, 0.62, abs(x))
    arm_z = 1.0 - 0.025 * arm_band * arm_outer

    return (
        x * head_x * chest_x * waist_x * hip_x * limb_x,
        y,
        z * head_z * chest_z * waist_z * hip_z * limb_z * arm_z,
    )


def read_glb(path: Path) -> tuple[dict, bytearray]:
    raw = path.read_bytes()
    magic, version, _ = struct.unpack_from("<4sII", raw, 0)
    if magic != b"glTF" or version != 2:
        raise ValueError(f"{path} is not a GLB 2.0 file")

    offset = 12
    json_bytes = None
    bin_bytes = None
    while offset < len(raw):
        length, chunk_type = struct.unpack_from("<II", raw, offset)
        offset += 8
        chunk = raw[offset : offset + length]
        offset += length
        if chunk_type == JSON_CHUNK:
            json_bytes = chunk
        elif chunk_type == BIN_CHUNK:
            bin_bytes = chunk

    if json_bytes is None or bin_bytes is None:
        raise ValueError("Expected embedded JSON and BIN chunks")

    doc = json.loads(json_bytes.decode("utf-8").rstrip("\x00 "))
    return doc, bytearray(bin_bytes)


def write_glb(path: Path, doc: dict, binary: bytearray) -> None:
    json_bytes = json.dumps(doc, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    json_bytes += b" " * ((4 - len(json_bytes) % 4) % 4)
    bin_bytes = bytes(binary)
    bin_bytes += b"\x00" * ((4 - len(bin_bytes) % 4) % 4)
    total = 12 + 8 + len(json_bytes) + 8 + len(bin_bytes)

    with path.open("wb") as f:
        f.write(struct.pack("<4sII", b"glTF", 2, total))
        f.write(struct.pack("<II", len(json_bytes), JSON_CHUNK))
        f.write(json_bytes)
        f.write(struct.pack("<II", len(bin_bytes), BIN_CHUNK))
        f.write(bin_bytes)


def transform_position_accessor(doc: dict, binary: bytearray, accessor_index: int) -> None:
    accessor = doc["accessors"][accessor_index]
    if accessor["componentType"] != 5126 or accessor["type"] != "VEC3":
        raise ValueError(f"Accessor {accessor_index} is not float VEC3 POSITION data")

    view = doc["bufferViews"][accessor["bufferView"]]
    base = view.get("byteOffset", 0) + accessor.get("byteOffset", 0)
    stride = view.get("byteStride", 12)
    minimum = [float("inf")] * 3
    maximum = [float("-inf")] * 3

    for i in range(accessor["count"]):
        offset = base + i * stride
        x, y, z = struct.unpack_from("<fff", binary, offset)
        values = reshape_vertex(x, y, z)
        struct.pack_into("<fff", binary, offset, *values)
        for axis, value in enumerate(values):
            minimum[axis] = min(minimum[axis], value)
            maximum[axis] = max(maximum[axis], value)

    accessor["min"] = minimum
    accessor["max"] = maximum


def generate(source: Path, output: Path) -> None:
    doc, binary = read_glb(source)

    if not doc.get("meshes") or len(doc["meshes"][0].get("primitives", [])) < 2:
        raise ValueError("Unexpected UAL female mannequin mesh layout")

    position_accessors = [primitive["attributes"]["POSITION"] for primitive in doc["meshes"][0]["primitives"]]
    for accessor_index in position_accessors:
        transform_position_accessor(doc, binary, accessor_index)

    doc["materials"][0]["name"] = "Ilyra_Warden_Pale"
    doc["materials"][0]["pbrMetallicRoughness"].update(
        baseColorFactor=[0.72, 0.80, 0.88, 1.0], metallicFactor=0.0, roughnessFactor=0.68
    )
    doc["materials"][1]["name"] = "Ilyra_Light_Silver"
    doc["materials"][1]["pbrMetallicRoughness"].update(
        baseColorFactor=[0.62, 0.69, 0.78, 1.0], metallicFactor=0.58, roughnessFactor=0.34
    )

    doc["meshes"][0]["name"] = "Ilyra_AnimeBody_Proxy"
    for node in doc.get("nodes", []):
        if node.get("mesh") == 0:
            node["name"] = "Ilyra_AnimeBody_Proxy"
    doc.setdefault("asset", {})["generator"] = "Diyse UAL anime-body proxy generator"
    doc.setdefault("extras", {})["diyse_note"] = (
        "Motion/proportion prototype only. Ilyra B00 remains visual canon."
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    write_glb(output, doc, binary)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "source",
        nargs="?",
        type=Path,
        default=Path("asset_sources/animation/ual/Mannequin_F.glb"),
    )
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        default=Path("asset_sources/animation/ual/Ilyra_AnimeBody_UAL.glb"),
    )
    args = parser.parse_args()
    generate(args.source, args.output)
    print(f"Generated {args.output}")
