#!/usr/bin/env bash
set -euo pipefail
root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
ref="$(cat "$root/upstream.ref")"
if [[ ! "$ref" =~ ^[0-9a-f]{40}$ ]]; then
  printf '%s\n' 'upstream.ref deve conter um SHA Git completo.' >&2
  exit 1
fi
target="$root/.local/stustapay"
if [[ -e "$target" ]]; then
  actual="$(git -C "$target" rev-parse HEAD)"
  if [[ "$actual" != "$ref" ]]; then
    printf '%s\n' 'Checkout existente difere de upstream.ref; revisar manualmente para preservar trabalho local.' >&2
    exit 1
  fi
  printf '%s\n' "Checkout existente preservado: $target ($ref)."
  exit 0
fi
mkdir -p "$root/.local"
temporary="$(mktemp -d "$root/.local/upstream.XXXXXX")"
# Preserve a failed download for inspection rather than removing local files.
git -C "$temporary" init -q
git -C "$temporary" remote add origin https://github.com/stustapay/stustapay.git
git -C "$temporary" fetch --depth=1 origin "$ref"
git -C "$temporary" checkout --detach -q FETCH_HEAD
mv -- "$temporary" "$target"
printf '%s\n' "StuStaPay preparado em $target ($ref)."
