# Agent notes — helix

Notes while learning the Helix editor. See `README.md` for the human-facing overview.

This directory is a **teaching workspace** driven by the `/teach` skill
(`.claude/skills/teach/SKILL.md` at the repo root). Read that skill before adding lessons.

## Layout

- `MISSION.md` — why Zach is learning Helix. Grounds every lesson. If empty, interview first.
- `RESOURCES.md` — trusted sources (docs, tutor, communities). Draw knowledge from here, not from memory.
- `GLOSSARY.md` — canonical terms; add a term only once Zach can use it correctly.
- `NOTES.md` — environment facts and teaching preferences.
- `lessons/NNNN-slug.html` — one short, self-contained lesson each; links `../assets/style.css`.
- `reference/*.html` — printable cheat sheets distilled from lessons; the thing revisited later.
- `assets/` — shared components (`style.css`, `quiz.js`). Reuse before writing new ones.
- `learning-records/NNNN-slug.md` — evidence of what was actually learned (created lazily).

## Conventions

- Helix's model is selection → action (unlike vim's action → motion); keep that framing in
  every explanation. Zach knows vim, so translate from vim where it helps, but teach the Helix way.
- Prefer pointing at `hx --tutor` sections and https://docs.helix-editor.com/ over re-teaching;
  verify any keybinding against the keymap page before putting it in a lesson.
- Lessons should be doable in minutes, end in one concrete win, and include a real-terminal
  task plus a retrieval quiz. Open the lesson with `open lessons/NNNN-slug.html` when done.
- Helix 25.07.1 is installed via Homebrew; no user config exists yet (see `NOTES.md`).
