#!/usr/bin/env bash
set -euo pipefail

# backward-compatible entrypoint
# usage: ./scripts/generate_keynote.sh <deck-name>
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
"$SCRIPT_DIR/render_reveal.sh" "$@"
