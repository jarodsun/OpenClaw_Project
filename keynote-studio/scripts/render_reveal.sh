#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <deck-name>"
  echo "Example: $0 demo-reveal-dracula"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DECK_NAME="$1"
DECK_DIR="$ROOT_DIR/decks/$DECK_NAME"
SOURCE_MD="$DECK_DIR/source.md"
OUTPUT_DIR="$DECK_DIR/output"
OUTPUT_HTML="$OUTPUT_DIR/index.html"

if [ ! -f "$SOURCE_MD" ]; then
  echo "source.md not found: $SOURCE_MD"
  exit 1
fi

mkdir -p "$OUTPUT_DIR"

MARKDOWN_CONTENT="$(cat "$SOURCE_MD")"

cat > "$OUTPUT_HTML" <<HTML
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>${DECK_NAME}</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reset.css" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/dracula.css" id="theme" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/highlight/monokai.css" />
    <style>
      .reveal h1, .reveal h2, .reveal h3 { text-transform: none; }
      .reveal .small { font-size: 0.7em; opacity: 0.85; }
    </style>
  </head>
  <body>
    <div class="reveal">
      <div class="slides">
        <section data-markdown>
          <textarea data-template>
$MARKDOWN_CONTENT
          </textarea>
        </section>
      </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/markdown/markdown.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/notes/notes.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/highlight/highlight.js"></script>
    <script>
      Reveal.initialize({
        hash: true,
        slideNumber: true,
        transition: 'slide',
        plugins: [ RevealMarkdown, RevealNotes, RevealHighlight ]
      });
    </script>
  </body>
</html>
HTML

echo "Generated: $OUTPUT_HTML"
