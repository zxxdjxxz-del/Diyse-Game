#!/usr/bin/env bash
set -euo pipefail

EXPECTED_ARCHIVE_SHA256="698cad5c8ba148674511cd0ed62fbee2f1367e0330be173138f2e46e86c26509"
EXPECTED_ARCHIVE_SIZE="98580"
EXPECTED_DOCS_FILE_COUNT="813"
EXPECTED_DOCS_TREE="ba3e10d09abba0edfacaa88bc4baa11f19fc79b5"
EXPECTED_ROOT_README_BLOB="b928650be57c6308093156e14512f05554a24c99"
EXPECTED_ROOT_AGENTS_BLOB="cfd260bd19fbdb973111f530282849ce61ec1f4d"
EXPECTED_FINAL_ROOT_TREE="a0bbb147e6a2a059ef8239be844e1f8d770e7d01"
TRANSPORT=".migration/v98-final-closure"
WORKFLOW=".github/workflows/v98-final-closure.yml"

cd "$(git rev-parse --show-toplevel)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
archive="$tmp/v98-final-closure.tar.xz"
extract="$tmp/extract"
mkdir -p "$extract"
: > "$archive"

for i in $(seq -w 0 65); do
  base64 -d "$TRANSPORT/chunks/c${i}.b64" >> "$archive"
done

actual_size="$(wc -c < "$archive" | tr -d '[:space:]')"
actual_sha="$(sha256sum "$archive" | awk '{print $1}')"
test "$actual_size" = "$EXPECTED_ARCHIVE_SIZE"
test "$actual_sha" = "$EXPECTED_ARCHIVE_SHA256"

tar -xJf "$archive" -C "$extract"
for required in 00_MASTER_CONTROL 90_WORKING 99_ARCHIVE README.md PACKAGE_MANIFEST.json; do
  test -e "$extract/$required"
done

mkdir -p docs
# Preserve only the already exact numbered subject domains 01-16.
for path in docs/* docs/.[!.]* docs/..?*; do
  [ -e "$path" ] || continue
  name="$(basename "$path")"
  case "$name" in
    01_CHARACTERS|02_STORY|03_DIALOGUE|04_WORLD_AND_LORE|05_BATTLE_SYSTEM|06_CLASSES_AND_ABILITIES|07_CARDS|08_ITEMS_AND_EQUIPMENT|09_ENEMIES_AND_ENCOUNTERS|10_PROGRESSION_AND_EXP|11_QUESTS|12_ECONOMY_AND_REWARDS|13_UI_AND_IMPLEMENTATION|14_ART_AND_VISUALS|15_AUDIO_AND_MUSIC|16_BALANCE_AND_TESTING)
      ;;
    *) rm -rf "$path" ;;
  esac
done

mv "$extract/00_MASTER_CONTROL" docs/00_MASTER_CONTROL
mv "$extract/90_WORKING" docs/90_WORKING
mv "$extract/99_ARCHIVE" docs/99_ARCHIVE
mv "$extract/README.md" docs/README.md
mv "$extract/PACKAGE_MANIFEST.json" docs/PACKAGE_MANIFEST.json

cp docs/90_WORKING/GITHUB_TRANSITION_STAGING/README_PROPOSED.md README.md
cp docs/90_WORKING/GITHUB_TRANSITION_STAGING/AGENTS_PROPOSED.md AGENTS.md
rm -f _migration_payload_test.txt
rm -rf "$TRANSPORT"
rm -f "$WORKFLOW"
rmdir .migration 2>/dev/null || true

git add -A

actual_count="$(find docs -type f | wc -l | tr -d '[:space:]')"
test "$actual_count" = "$EXPECTED_DOCS_FILE_COUNT"

if grep -RIlF 'Exactly 8 automatic Mastery Points' docs >/dev/null; then
  echo "Stale Mastery Points wording remains" >&2
  exit 1
fi

root_tree="$(git write-tree)"
docs_tree="$(git ls-tree "$root_tree" docs | awk '{print $3}')"
test "$docs_tree" = "$EXPECTED_DOCS_TREE"

test "$(git hash-object README.md)" = "$EXPECTED_ROOT_README_BLOB"
test "$(git hash-object AGENTS.md)" = "$EXPECTED_ROOT_AGENTS_BLOB"
test ! -e _migration_payload_test.txt
test ! -e "$TRANSPORT"
test ! -e "$WORKFLOW"

if [ "${SKIP_FINAL_ROOT_GATE:-0}" != "1" ]; then
  test "$root_tree" = "$EXPECTED_FINAL_ROOT_TREE"
fi

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git commit -m "Finalize exact v98 repository reorganization"
git push origin HEAD:migration/v98-subject-canon
