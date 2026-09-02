# Helix Resources

## Knowledge

- [Built-in tutor: `hx --tutor` (or `:tutor` inside Helix)](https://docs.helix-editor.com/usage.html)
  Interactive, ships with the editor (v25.07.1 has 8 chapters: movement/insert, motions & selections,
  undo/yank/search, multiple cursors, replace/repeat, registers & macros). Use for: the canonical
  hands-on path; lessons here should point at specific tutor sections rather than re-teach them.
- [Helix docs: Usage](https://docs.helix-editor.com/usage.html)
  Short overview of the selection → action model, modes, multiple selections. Use for: framing.
- [Helix docs: Keymap](https://docs.helix-editor.com/keymap.html)
  The authoritative keybinding reference (normal, select, goto, match, space, view, window modes).
  Use for: checking exactly what a key does before putting it in a lesson or reference sheet.
- [Helix docs: Migrating from Vim](https://docs.helix-editor.com/from-vim.html) and the
  [wiki table of Vim → Helix equivalents](https://github.com/helix-editor/helix/wiki/Migrating-from-Vim)
  Side-by-side key equivalents (`dw`→`wd`, `dd`→`xd`, `$`→`gl`, `%`→`mm` …). Use for: translating
  existing vim muscle memory, and for spotting where a vim habit will misfire.
- [Helix docs: Configuration](https://docs.helix-editor.com/configuration.html)
  `~/.config/helix/config.toml`, `[editor]` options, `:config-open`, `:config-reload`. Use for: any config lesson.
- [Julia Evans, "Notes on switching to Helix from vim" (Oct 2025)](https://jvns.ca/blog/2025/10/10/notes-on-switching-to-helix-from-vim/)
  Experienced vim user's honest account: took a week or two, keep config minimal, learn "the Helix way",
  multiple cursors replace macros, known rough edges (markdown lists, reflow, no persistent undo).
  Use for: expectation-setting and the "which vim habits to drop" question.
- [Helix wiki: FAQ](https://github.com/helix-editor/helix/wiki/FAQ) and
  [Troubleshooting](https://github.com/helix-editor/helix/wiki/Troubleshooting)
  Use for: LSP setup, "why doesn't X work" questions.

## Wisdom (Communities)

- [Matrix space `#helix-community:matrix.org`](https://matrix.to/#/#helix-community:matrix.org)
  The official chat (join `#helix-editor:matrix.org` if the client lacks Spaces). Use for: live questions,
  config help.
- [GitHub Discussions](https://github.com/helix-editor/helix/discussions)
  Official Q&A and ideas. Use for: searchable answers, workflow questions, feature status.
- [r/HelixEditor](https://www.reddit.com/r/HelixEditor/)
  Unofficial but active. Use for: config sharing, "how do you do X" threads.

## Gaps

- No trusted resource yet for LaTeX (texlab) or Markdown workflows in Helix specifically — relevant
  because `basic-mathematics/` is LaTeX. Search when the mission calls for it.
- No resource yet on tree-sitter text objects (`mi(`, `maf` …) beyond the keymap page.
