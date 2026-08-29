# Basic Mathematics

Notes from working through **Serge Lang's *Basic Mathematics*** (Springer, 1988).

The book is a from-first-principles treatment of pre-calculus mathematics —
algebra, geometry, coordinate geometry, and a taste of functions and induction —
written with a proof-oriented mindset rather than rote drill.

A copy of the book lives here as `basic-mathematics-serge-lang.pdf`.

## Structure

Two LaTeX files per chapter — `chapter-NN-notes.tex` (my notes) and
`chapter-NN-exercises.tex` (the book's exercise questions, for working through):

- `chapter-01-notes.tex` / `chapter-01-exercises.tex` — Chapter 1: Numbers (integers, rules for addition, rules for multiplication)

## Building

Compile any chapter with `tectonic chapter-01-notes.tex`.

For live preview while editing, run `./watch.sh` — with no arguments it watches
every `.tex` file in the directory; or pass specific files
(`./watch.sh chapter-01-notes.tex`). It builds each once, opens the PDFs in
Skim (one window per document), then watches (via `entr`): every save rebuilds
just the changed file and tells Skim to reload just that PDF. Ctrl-C to stop.

Requires `tectonic` and `entr` (both via Homebrew) and [Skim](https://skim-app.sourceforge.io/).
