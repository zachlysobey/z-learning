#!/bin/sh
# Live-preview chapters: rebuild a file on save, Skim reloads just that PDF.
#   usage: ./watch.sh [chapter.tex ...]   (no args: every .tex in this directory)
# Multiple PDFs can be open in Skim at once; each save reverts only its own.
set -e

# Internal mode, invoked by entr with the file that changed.
if [ "$1" = "--rebuild" ]; then
  tex="$2"
  tectonic "$tex"
  pdf="$(pwd)/${tex%.tex}.pdf"
  osascript - "$pdf" <<'EOF'
on run argv
  set pdfPath to item 1 of argv
  tell application "Skim"
    set docs to documents whose path is pdfPath
    if (count of docs) > 0 then
      revert item 1 of docs
    else
      open (POSIX file pdfPath)
    end if
  end tell
end run
EOF
  exit 0
fi

cd "$(dirname "$0")"
[ $# -eq 0 ] && set -- *.tex
for tex in "$@"; do
  tectonic "$tex"
  open -a Skim "${tex%.tex}.pdf"
done
printf '%s\n' "$@" | entr "$0" --rebuild /_
