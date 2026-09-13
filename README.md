# z-learning

Personal learning notes and experiments.

Published at **<https://zachlysobey.github.io/z-learning/>** — a main page linking
to a landing page per topic, and from there to every lesson, reference sheet, and
built PDF.

## Contents

- [`basic-mathematics/`](basic-mathematics/) — LaTeX notes while working through Serge Lang's *Basic Mathematics*
- [`climbing-volumes/`](climbing-volumes/) — notes while learning to build plywood climbing volumes
- [`helix/`](helix/) — notes while learning the Helix editor

## Publishing

Every push to `main` rebuilds the site (`.github/workflows/pages.yml`).
`tools/build-site.py` discovers topics and lessons by globbing, so adding a topic
directory or dropping a new lesson into `lessons/` is all it takes — no config to
edit. Preview locally with `python3 tools/build-site.py && open _site/index.html`.
