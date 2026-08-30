#!/usr/bin/env bash
set -euo pipefail

EXPECTED_ARCHIVE_SHA256="ef40c9f3c1864ae151aaceb8dbceed6d034f9a946a67fd1f48a0b46ec00db922"
EXPECTED_ARCHIVE_SIZE="129800"
EXPECTED_FILE_COUNT="272"
EXPECTED_SUBTREE_SHA="02fc821579fae3fae7a8718e57b23ef5e51f4d1a"
DOMAIN="docs/09_ENEMIES_AND_ENCOUNTERS"
TRANSPORT=".migration/domain09"
WORKFLOW=".github/workflows/v98-domain09-migration.yml"

cd "$(git rev-parse --show-toplevel)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
archive="$tmp/domain09.tar.xz"
extract="$tmp/extract"
mkdir -p "$extract"
: > "$archive"

for i in 00 01 02 03 04 05 06; do
  cat "$TRANSPORT/prefix/p${i}.bin" >> "$archive"
done
for i in $(seq -w 0 15); do
  base64 -d "$TRANSPORT/tail/t${i}.b64" >> "$archive"
done

actual_size="$(wc -c < "$archive" | tr -d '[:space:]')"
actual_sha="$(sha256sum "$archive" | awk '{print $1}')"
test "$actual_size" = "$EXPECTED_ARCHIVE_SIZE"
test "$actual_sha" = "$EXPECTED_ARCHIVE_SHA256"

tar -xJf "$archive" -C "$extract"
test -d "$extract/09_ENEMIES_AND_ENCOUNTERS"

rm -rf "$DOMAIN"
mv "$extract/09_ENEMIES_AND_ENCOUNTERS" "$DOMAIN"

actual_count="$(find "$DOMAIN" -type f | wc -l | tr -d '[:space:]')"
test "$actual_count" = "$EXPECTED_FILE_COUNT"

git add -A "$DOMAIN"
root_tree="$(git write-tree)"
subtree_sha="$(git ls-tree "$root_tree" "$DOMAIN" | awk '{print $3}')"
test "$subtree_sha" = "$EXPECTED_SUBTREE_SHA"

rm -rf "$TRANSPORT"
rm -f "$WORKFLOW"
git add -A

root_tree="$(git write-tree)"
subtree_sha="$(git ls-tree "$root_tree" "$DOMAIN" | awk '{print $3}')"
test "$subtree_sha" = "$EXPECTED_SUBTREE_SHA"

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git commit -m "Add exact v98 enemies and encounters domain"
git push origin HEAD:migration/v98-subject-canon
