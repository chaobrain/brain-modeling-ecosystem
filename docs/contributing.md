# Contributing to BrainX Documentation

This site documents the BrainX ecosystem. Documentation is authored primarily in Markdown and built with 
[Sphinx](https://www.sphinx-doc.org/) using [MyST](https://myst-parser.readthedocs.io/) and 
the [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io).

## Prerequisites
- Python 3.10+
- From the repo root: `pip install -r docs/requirements.txt`

## Where to edit
- Most pages are Markdown files in `docs/` (for example, `install.md`, `getting_started.md`).
- The table of contents is defined in `docs/index.rst` via Sphinx `toctree` entries.

## Add or edit a page
1) Create or edit a Markdown file under `docs/` (use `#` headings, fenced code blocks, and standard Markdown links).
2) Add the new file to the `toctree` in `docs/index.rst` so it appears in the navigation.
3) Keep titles concise and use sentence case. Prefer short sections with clear bullets and code examples.

## Build locally
From the repo root:

- HTML: `sphinx-build -b html docs docs/_build/html`
- Open `docs/_build/html/index.html` in your browser to preview.

Optional checks:
- Link check: `sphinx-build -b linkcheck docs docs/_build/linkcheck`

## Style guidelines
- Use fenced code blocks with a language tag, e.g., ```python, ```bash, ```bibtex.
- Use inline code for commands and paths: `pip install`, `docs/index.rst`.
- Keep lines reasonably short (< 100 chars) for readability.
- Prefer relative links within the docs; use full URLs only when linking external sites.

## Submitting changes
- Run `pre-commit run --all-files` to auto-format and lint.
- Open a PR with a clear description, screenshots for visual changes, and link related issues.

If you have questions or want to propose a larger restructuring, please open an issue first to discuss.