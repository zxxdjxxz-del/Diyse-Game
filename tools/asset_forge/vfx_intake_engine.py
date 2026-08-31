#!/usr/bin/env python3
"""VFX-focused ZIP intake for Diyse Asset Forge.

Adds VFX-specific structure discovery on top of ordinary archive intake:
- ignores macOS metadata/resource forks;
- recognizes predrawn/flipbook spritesheet grid suffixes such as 6x5 and 8x8;
- records implied source-frame counts without slicing/repacking the sheet;
- pairs color particle sprites with companion alpha masks;
- classifies broad VFX semantic families for later Diyse treatment routing.
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import zipfile
from collections import Counter
from pathlib import Path

from PIL import Image

IMAGE_EXTS = {'.png', '.tga', '.jpg', '.jpeg', '.webp'}
SHEET_RE = re.compile(r'(?i)_(\d+)x(\d+)$')

VFX_KIND_RULES = [
    ('fire', ('fire', 'flame', 'ember')),
    ('smoke', ('smoke', 'cloud')),
    ('impact', ('explosion', 'impact', 'big_hit', 'blood', 'muzzle', 'scorch', 'slash')),
    ('energy', ('electric', 'spark', 'lightstreak', 'spotlight', 'flare', 'charge', 'light_')),
    ('magic', ('magic', 'wavy', 'vortex', 'twirl', 'symbol', 'star')),
    ('debris', ('dirt', 'scratch')),
    ('utility', ('circle', 'effect', 'trace', 'window')),
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def is_metadata_member(member: str) -> bool:
    normalized = member.replace('\\', '/')
    parts = [part.lower() for part in normalized.split('/') if part]
    name = Path(normalized).name.lower()
    return '__macosx' in parts or name == '.ds_store' or name.startswith('._')


def asset_role(member: str) -> str | None:
    lower = member.replace('\\', '/').lower()
    if '/flipbooks/' in lower:
        return 'flipbook'
    if '/predrawn/' in lower:
        return 'predrawn'
    if '/particles/alpha/' in lower:
        return 'particle_alpha'
    if '/particles/opague/' in lower or '/particles/opaque/' in lower:
        return 'particle_color'
    if '/particles/' in lower:
        return 'particle'
    return None


def vfx_kind(member: str) -> str:
    stem = Path(member).stem.lower()
    for kind, tokens in VFX_KIND_RULES:
        if any(token in stem for token in tokens):
            return kind
    return 'utility'


def spritesheet_grid(member: str) -> tuple[int | None, int | None, int | None]:
    match = SHEET_RE.search(Path(member).stem)
    if not match:
        return None, None, None
    columns = int(match.group(1))
    rows = int(match.group(2))
    return columns, rows, columns * rows


def _particle_pair_key(member: str) -> str | None:
    role = asset_role(member)
    if role not in {'particle_color', 'particle_alpha'}:
        return None
    stem = Path(member).stem.lower()
    if stem.endswith('_a'):
        stem = stem[:-2]
    return stem


def scan_vfx_zip(path: Path, hash_members: bool = False) -> dict:
    members: list[dict] = []
    skipped = 0
    with zipfile.ZipFile(path) as archive:
        raw = [info for info in archive.infolist() if not info.is_dir()]
        for info in raw:
            if is_metadata_member(info.filename):
                skipped += 1
                continue
            suffix = Path(info.filename).suffix.lower()
            row = {
                'member': info.filename,
                'bytes': info.file_size,
                'crc32': f'{info.CRC:08x}',
                'extension': suffix,
                'asset_role': asset_role(info.filename),
                'vfx_kind': vfx_kind(info.filename),
            }
            columns, rows, frames = spritesheet_grid(info.filename)
            row['spritesheet_columns'] = columns
            row['spritesheet_rows'] = rows
            row['spritesheet_frames'] = frames

            if suffix in IMAGE_EXTS:
                data = archive.read(info)
                with Image.open(io.BytesIO(data)) as image:
                    row.update({
                        'width': image.width,
                        'height': image.height,
                        'mode': image.mode,
                        'has_alpha': 'A' in image.getbands() or 'transparency' in image.info,
                    })
                if hash_members:
                    row['sha256'] = hashlib.sha256(data).hexdigest()
            elif hash_members:
                row['sha256'] = hashlib.sha256(archive.read(info)).hexdigest()
            members.append(row)

    images = [row for row in members if row['extension'] in IMAGE_EXTS]
    sheets = [row for row in images if row.get('spritesheet_frames')]

    colors = {_particle_pair_key(row['member']): row['member'] for row in images if row['asset_role'] == 'particle_color'}
    alphas = {_particle_pair_key(row['member']): row['member'] for row in images if row['asset_role'] == 'particle_alpha'}
    matched = sorted(set(colors) & set(alphas))
    alpha_only = sorted(key for key in set(alphas) - set(colors) if key is not None)
    color_only = sorted(key for key in set(colors) - set(alphas) if key is not None)

    dup_key = 'sha256' if hash_members else 'crc_size'
    duplicate_map: dict[object, list[str]] = {}
    for row in images:
        key = row.get('sha256') if hash_members else (row['bytes'], row['crc32'])
        duplicate_map.setdefault(key, []).append(row['member'])
    duplicates = [items for items in duplicate_map.values() if len(items) > 1]

    return {
        'archive': path.name,
        'archive_bytes': path.stat().st_size,
        'archive_sha256': sha256_file(path),
        'raw_file_members': len(members) + skipped,
        'skipped_metadata_members': skipped,
        'usable_members': len(members),
        'image_members': len(images),
        'uncompressed_usable_bytes': sum(row['bytes'] for row in members),
        'roles': dict(sorted(Counter(row['asset_role'] for row in images if row.get('asset_role')).items())),
        'vfx_kinds': dict(sorted(Counter(row['vfx_kind'] for row in images).items())),
        'spritesheet_assets': len(sheets),
        'spritesheet_frames': sum(row['spritesheet_frames'] for row in sheets),
        'particle_pairs': {
            'matched_color_alpha_pairs': len(matched),
            'color_only': color_only,
            'alpha_only': alpha_only,
        },
        'duplicate_basis': dup_key,
        'duplicate_groups': duplicates,
        'members': members,
    }


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(prog='diyse-vfx-intake')
    parser.add_argument('archive', type=Path)
    parser.add_argument('--hash-members', action='store_true')
    parser.add_argument('--output', type=Path, default=Path('.asset_forge/vfx_intake.json'))
    args = parser.parse_args()
    result = scan_vfx_zip(args.archive, hash_members=args.hash_members)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps({
        'archive': result['archive'],
        'images': result['image_members'],
        'spritesheets': result['spritesheet_assets'],
        'source_frames': result['spritesheet_frames'],
        'particle_pairs': result['particle_pairs']['matched_color_alpha_pairs'],
        'duplicates': len(result['duplicate_groups']),
        'output': str(args.output),
    }, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
