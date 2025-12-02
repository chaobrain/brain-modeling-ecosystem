# Contributing to the BrainX Ecosystem

We welcome contributions to the BrainX ecosystem - code, documentation, bug reports, and feature ideas. This repository coordinates components like BrainUnit, BrainCell, BrainState, BrainTaichi, BrainEvent, and BrainTrace, and the glue that ensures they interoperate well together.

## Ways to contribute
- Report bugs and request features via GitHub issues.
- Improve documentation under `docs/`.
- Contribute code to the `BrainX/` package and related tooling.
- Triage issues, review PRs, and help with discussions.

## Development setup
- Fork the repo and create a topic branch: `git checkout -b feat/my-change`.
- Create a virtual environment and install deps:
  - `pip install -e .`
  - `pip install -r docs/requirements.txt`
- Install pre-commit hooks to run linters locally:
  - `pip install pre-commit`
  - `pre-commit install`

## Testing and linting
- Run tests: `pytest BrainX/`.
- Run pre-commit across all files: `pre-commit run --all-files`.

## Documentation
- Pages live in `docs/` (Markdown and a small amount of reStructuredText for `index.rst`).
- To add a page, create a new `.md` file in `docs/` and add it to the toctree in `docs/index.rst`.
- Build locally: `sphinx-build -b html docs docs/_build/html` and open `docs/_build/html/index.html`.

## Pull requests
Before requesting review, please ensure:
- CI passes (tests and linters).
- Docs and type hints are updated where relevant.
- Changes are scoped and focused; prefer multiple small PRs over one large PR.

See `docs/contributing.md` for additional details specific to documentation.

Please also follow our [Code of Conduct](CODE_OF_CONDUCT.md) and report security issues responsibly via [SECURITY.md](SECURITY.md).