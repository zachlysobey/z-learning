# Agent notes — basic-mathematics

LaTeX notes for Serge Lang's *Basic Mathematics*. See `README.md` for the human-facing overview.

A PDF of the book is at `basic-mathematics-serge-lang.pdf` — consult it to check
the book's actual wording, notation, and rule numbering (e.g. N1–N12 in Chapter 1)
before adding content to the notes.

## Conventions

- Two files per chapter (zero-padded chapter number): `chapter-NN-notes.tex` for
  the notes, and `chapter-NN-exercises.tex` holding the book's exercise questions,
  transcribed verbatim from the PDF, with section numbering mirroring the notes.
  Exercise numbering follows the book (use `enumitem`'s `[resume]` across
  instruction blocks). Questions only — solutions are Zach's work.
- Documents are `article` class with `amsmath`, `amssymb`, `amsthm`, and 1in margins.
- Theorem environments in use: `definition`, `theorem`, `example` — all numbered within sections.
- Section headings follow the book's own section titles for the chapter.
- The book's named rules (N1–N12, Commutativity, etc.) are set with `description`
  lists (`\item[N1.]`), not `itemize` — long bracketed labels overflow itemize's margin.
- These are Zach's study notes: when asked to help, prefer explaining and scaffolding over writing complete solutions to exercises.
- Do not edit the `chapter-NN-exercises.tex` files unless Zach explicitly asks for a specific change — working the solutions (including the LaTeX) is the point. When reviewing his answers, give feedback in the conversation instead.
- LaTeX build artifacts (`.aux`, `.log`, `.pdf`, etc.) are not committed.
- Build with `tectonic <file>.tex`. Zach often has `./watch.sh` running
  (entr + Skim live preview; no args = watch every `.tex` here), so saving a
  `.tex` file already triggers a rebuild — don't start watch loops or extra
  builds when it's running. Check with `pgrep -fl entr` which files are covered.
