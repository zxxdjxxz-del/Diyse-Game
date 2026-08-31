#!/usr/bin/env python3
"""ZIP-native texture/VFX intake for Diyse Asset Forge v0.9."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

from PIL import Image

IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.webp', '.tga'}
FRAME_RE = re.compile(r'(?i)(?:^|[_-])frame[_-]?(\d+)|(?:^|[_-])(\d+)$')
GRID_RE = re.compile(r'_(\d+)x(\d+)(?:\.[^.]+)$', re.IGNORECASE)

CATEGORY_RULES = [
    ('emission', ('emission', 'lumen', 'light_', '/lights/', 'aimpoit', 'flure')),
    ('fire', ('/fire/', 'anim_fire', 'lava', 'flame', 'ember')),
    ('ritual', ('mistic', 'mystic', 'magic', 'rune', 'glyph', 'ritual')),
    ('brick', ('brick', 'old_bricks', 'medieval flat', 'slim slate', 'weave flooring')),
    ('concrete', ('concrete', 'cement')),
    ('glass', ('glass', 'window')),
    ('metal', ('/metal/', 'metal_', 'grate', 'fence', 'riveted', 'welded', 'beam')),
    ('marble', ('marble',)),
    ('wood', ('/wood/', 'wood_', 'plank', 'crate', 'mansion panel')),
    ('water', ('/water/', 'water_', 'ocean', 'river')),
    ('foliage', ('foliage', 'tree', 'leaf', 'bush', 'plant')),
    ('terrain', ('outdoors', 'sand', 'canyon', 'gravel', 'desert', 'rock', 'stone', 'slab')),
    ('misc', ('miscellaneous', 'wallpaper')),
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def is_metadata_path(name: str) -> bool:
    norm = name.replace('\\', '/')
    base = Path(norm).name
    return norm.startswith('__MACOSX/') or '/__MACOSX/' in norm or base == '.DS_Store' or base.startswith('._')


def parse_grid(member: str) -> tuple[int, int] | None:
    match = GRID_RE.search(Path(member).name)
    return (int(match.group(1)), int(match.group(2))) if match else None


def classify_path(member: str, archive_name: str = '') -> str:
    text = ('/' + archive_name + '/' + member).replace('\\', '/').lower()
    if archive_name.lower().startswith('emission'):
        return 'emission'
    for category, tokens in CATEGORY_RULES:
        if any(token in text for token in tokens):
            return category
    return 'generic'


def animation_group(member: str) -> tuple[str | None, int | None]:
    normalized = member.replace('\\', '/')
    lower = normalized.lower()
    if 'animated extras/' not in lower and 'anim_' not in lower:
        return None, None
    stem = Path(normalized).stem
    match = FRAME_RE.search(stem)
    if not match:
        return None, None
    frame = int(next(group for group in match.groups() if group is not None))
    group_stem = re.sub(r'(?i)(?:[_-]?frame[_-]?\d+|[_-]\d+)$', '', stem)
    return str(Path(normalized).with_name(group_stem)), frame


def inspect_member(archive: zipfile.ZipFile, info: zipfile.ZipInfo, archive_name: str, hash_member: bool = False) -> dict:
    suffix = Path(info.filename).suffix.lower()
    grid = parse_grid(info.filename)
    row = {
        'archive': archive_name,
        'member': info.filename,
        'bytes': info.file_size,
        'crc32': f'{info.CRC:08x}',
        'extension': suffix,
        'category': classify_path(info.filename, archive_name),
        'grid_cols': grid[0] if grid else None,
        'grid_rows': grid[1] if grid else None,
        'grid_frames': grid[0] * grid[1] if grid else None,
    }
    group, frame = animation_group(info.filename)
    row['animation_group'] = group
    row['frame_index'] = frame

    if suffix in IMAGE_EXTS:
        data = archive.read(info)
        with Image.open(io.BytesIO(data)) as image:
            row.update({
                'width': image.width,
                'height': image.height,
                'mode': image.mode,
                'has_alpha': 'A' in image.getbands() or 'transparency' in image.info,
            })
        if hash_member:
            row['sha256'] = hashlib.sha256(data).hexdigest()
    elif hash_member:
        row['sha256'] = hashlib.sha256(archive.read(info)).hexdigest()
    return row


def scan_archives(paths: Iterable[Path], hash_members: bool = False) -> dict:
    archives, members = [], []
    ignored_metadata = 0
    for path in paths:
        with zipfile.ZipFile(path) as archive:
            all_infos = [info for info in archive.infolist() if not info.is_dir()]
            ignored_metadata += sum(1 for info in all_infos if is_metadata_path(info.filename))
            infos = [info for info in all_infos if not is_metadata_path(info.filename)]
            before = len(members)
            for info in infos:
                members.append(inspect_member(archive, info, path.name, hash_member=hash_members))
            rows = members[before:]
            archives.append({
                'archive': path.name,
                'path': str(path.resolve()),
                'bytes': path.stat().st_size,
                'sha256': sha256_file(path),
                'file_members': len(infos),
                'ignored_metadata_members': len(all_infos) - len(infos),
                'uncompressed_bytes': sum(info.file_size for info in infos),
                'categories': dict(sorted(Counter(row['category'] for row in rows).items())),
                'dimensions': [{'size': f'{w}x{h}', 'count': count} for (w, h), count in Counter((row['width'], row['height']) for row in rows if 'width' in row).most_common()],
            })

    grouped = defaultdict(list)
    for row in members:
        key = row.get('sha256') if hash_members else (row['bytes'], row['crc32'])
        grouped[key].append({'archive': row['archive'], 'member': row['member']})
    duplicates = [group for group in grouped.values() if len(group) > 1]
    animation_counts = Counter(row['animation_group'] for row in members if row.get('animation_group'))
    grid_sheets = [row for row in members if row.get('grid_frames')]
    return {
        'archives': archives,
        'totals': {
            'archives': len(archives),
            'file_members': len(members),
            'ignored_metadata_members': ignored_metadata,
            'image_members': sum(1 for row in members if row['extension'] in IMAGE_EXTS),
            'uncompressed_bytes': sum(row['bytes'] for row in members),
            'categories': dict(sorted(Counter(row['category'] for row in members).items())),
            'animation_groups': len(animation_counts),
            'grid_sheets': len(grid_sheets),
            'grid_frames': sum(row['grid_frames'] for row in grid_sheets),
        },
        'animation_groups': dict(sorted(animation_counts.items())),
        'duplicate_basis': 'sha256' if hash_members else 'crc_size',
        'duplicate_groups': duplicates,
        'members': members,
    }


def main() -> int:
    parser = argparse.ArgumentParser(prog='diyse-zip-intake')
    parser.add_argument('archives', nargs='+', type=Path)
    parser.add_argument('--hash-members', action='store_true')
    parser.add_argument('--output', type=Path, default=Path('.asset_forge/zip_intake.json'))
    args = parser.parse_args()
    result = scan_archives(args.archives, hash_members=args.hash_members)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps({k: result['totals'][k] for k in ('archives','file_members','image_members','ignored_metadata_members','grid_sheets','grid_frames','animation_groups')}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
