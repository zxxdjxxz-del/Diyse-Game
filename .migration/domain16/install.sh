#!/usr/bin/env bash
set -euo pipefail

EXPECTED_ARCHIVE_SHA256="2b4b7f45a64493fa31b99215ad14a25dac21845f561ed095ac0d3a782a02be72"
EXPECTED_ARCHIVE_SIZE="88708"
EXPECTED_FILE_COUNT="64"
EXPECTED_SUBTREE_SHA="69bb768fe48f3bc1632fd6fcb8b52b2b96ba6d66"
DOMAIN="docs/16_BALANCE_AND_TESTING"
TRANSPORT=".migration/domain16"
WORKFLOW=".github/workflows/v98-domain16-migration.yml"

cd "$(git rev-parse --show-toplevel)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
archive="$tmp/domain16.tar.xz"
extract="$tmp/extract"
mkdir -p "$extract"
: > "$archive"

cat "$TRANSPORT/p00.bin" >> "$archive"
for i in 00 01 02 03 04 05; do
  base64 -d "$TRANSPORT/early_text/t${i}.b64" >> "$archive"
done
for i in 06 07 08; do
  cat "$TRANSPORT/t${i}.bin" >> "$archive"
done
base64 -d "$TRANSPORT/t09.b64" >> "$archive"
for i in $(seq -w 0 32); do
  base64 -d "$TRANSPORT/remainder/r${i}.b64" >> "$archive"
done

actual_size="$(wc -c < "$archive" | tr -d '[:space:]')"
actual_sha="$(sha256sum "$archive" | awk '{print $1}')"
test "$actual_size" = "$EXPECTED_ARCHIVE_SIZE"
test "$actual_sha" = "$EXPECTED_ARCHIVE_SHA256"

tar -xJf "$archive" -C "$extract"
test -d "$extract/16_BALANCE_AND_TESTING"

rm -rf "$DOMAIN"
mkdir -p "$(dirname "$DOMAIN")"
mv "$extract/16_BALANCE_AND_TESTING" "$DOMAIN"

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
git commit -m "Add exact v98 balance and testing domain"
git push origin HEAD:migration/v98-subject-canon
