# Mission: Helix

## Why
Move day-to-day coding from VS Code / Cursor to a leaner terminal-based workflow, with Helix
as the editor. Vim has always been intriguing but never became fluent; Helix is the second
attempt, and it has to become comfortable enough to replace an IDE for real code editing at scale.

## Success looks like
- Edits a real codebase in Helix for a full working day without reaching for VS Code.
- Navigates files and symbols (picker, goto, LSP) as fast as in an IDE.
- Uses the select → act rhythm and multiple cursors without thinking about it.
- Has a small, understood `config.toml` (not a copied one).

## Constraints
- Vim: comfortable basics only (modes, hjkl, `dw`/`cw`/`dd`, `/`, `:w`/`:q`); macros and
  registers are not muscle memory. Don't assume deep vim habits, but do use vim as a reference point.
- Very fluent in app-based IDEs; expect comparisons to IDE features (multi-cursor, go-to-definition,
  fuzzy file open) to land well.
- Lessons should be short and finish with one concrete win.

## Out of scope
- Kakoune, neovim, or vim itself.
- Terminal multiplexers, shell tooling, and the wider "terminal workflow" beyond the editor (for now).
- Plugin ecosystems; Helix's built-ins are the target.
