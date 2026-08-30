#!/usr/bin/env bash
set -euo pipefail

EXPECTED_ARCHIVE_SHA256="d057f163901f8f5861d1b229fa38c29730368ebd0de56b85b7b2e215c7f643cc"
EXPECTED_ARCHIVE_SIZE="64436"
TRANSPORT=".migration/domain11_15"
WORKFLOW=".github/workflows/v98-domain11-15-migration.yml"

DOMAINS=(
  "11_QUESTS"
  "12_ECONOMY_AND_REWARDS"
  "13_UI_AND_IMPLEMENTATION"
  "14_ART_AND_VISUALS"
  "15_AUDIO_AND_MUSIC"
)
EXPECTED_COUNTS=(28 27 35 31 26)
EXPECTED_SHAS=(
  "8b6f6ffeb6ffd00a14bedc4b73014c405ef0ddad"
  "9356d664714595b8753b59cf7b8c91b15cae23ba"
  "dc04825e7e79dd0219cdfc580f08f3c5a6baa246"
  "7dfddb740ade1cadb5750e8514417ebf8aad0803"
  "d37965727161f3e32aa3681cf92ce1fb122030f3"
)

cd "$(git rev-parse --show-toplevel)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
archive="$tmp/domains11_15.tar.xz"
extract="$tmp/extract"
mkdir -p "$extract"
: > "$archive"

for f in p00 p01 p02 p03 p04 t00 t01 t02 t03 t04 t05; do
  cat "$TRANSPORT/chunks/${f}.bin" >> "$archive"
done

actual_size="$(wc -c < "$archive" | tr -d '[:space:]')"
actual_sha="$(sha256sum "$archive" | awk '{print $1}')"
test "$actual_size" = "$EXPECTED_ARCHIVE_SIZE"
test "$actual_sha" = "$EXPECTED_ARCHIVE_SHA256"

tar -xJf "$archive" -C "$extract"

for i in "${!DOMAINS[@]}"; do
  domain="${DOMAINS[$i]}"
  target="docs/$domain"
  test -d "$extract/$domain"
  count="$(find "$extract/$domain" -type f | wc -l | tr -d '[:space:]')"
  test "$count" = "${EXPECTED_COUNTS[$i]}"
  rm -rf "$target"
  mv "$extract/$domain" "$target"
  git add -A "$target"
done

root_tree="$(git write-tree)"
for i in "${!DOMAINS[@]}"; do
  domain="${DOMAINS[$i]}"
  target="docs/$domain"
  subtree_sha="$(git ls-tree "$root_tree" "$target" | awk '{print $3}')"
  test "$subtree_sha" = "${EXPECTED_SHAS[$i]}"
done

rm -rf "$TRANSPORT"
rm -f "$WORKFLOW"
git add -A

root_tree="$(git write-tree)"
for i in "${!DOMAINS[@]}"; do
  domain="${DOMAINS[$i]}"
  target="docs/$domain"
  subtree_sha="$(git ls-tree "$root_tree" "$target" | awk '{print $3}')"
  test "$subtree_sha" = "${EXPECTED_SHAS[$i]}"
done

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git commit -m "Add exact v98 quests through audio domains"
git push origin HEAD:migration/v98-subject-canon
