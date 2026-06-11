# Change log

↗️ = updated since previous release




## v2026.6.11

This maintenance release refreshes the pinned infrastructure component versions.

- **Package Dependencies:**
  - [`brainunit==0.4.0`](https://pypi.org/project/brainunit/0.4.0/) ↗️
  - [`brainstate==0.4.2`](https://pypi.org/project/brainstate/0.4.2/) ↗️
  - [`braintools==0.1.10`](https://pypi.org/project/braintools/0.1.10/) ↗️
  - [`brainevent==0.1.0`](https://pypi.org/project/brainevent/0.1.0/)
  - [`braintrace==0.2.0`](https://pypi.org/project/braintrace/0.2.0/)
  - [`braincell==0.0.8`](https://pypi.org/project/braincell/0.0.8/)
  - [`brainpy==2.7.8`](https://pypi.org/project/brainpy/2.7.8/)
  - [`brainpy-state==0.0.4`](https://pypi.org/project/brainpy-state/0.0.4/)
  - [`brainmass==0.0.5`](https://pypi.org/project/brainmass/0.0.5/)
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/)



## v2026.6.8

This release ships inline type information (PEP 561), consolidates the continuous
integration workflows, completes the repository rename to `brainx`, and refreshes
the pinned component versions.

- **Package Dependencies:**
  - [`jax<=0.10.1,>=0.6.0`](https://pypi.org/project/jax/) ↗️ (raised upper bound)
  - [`brainpy==2.7.8`](https://pypi.org/project/brainpy/2.7.8/) ↗️
  - [`brainunit==0.3.2`](https://pypi.org/project/brainunit/0.3.2/) ↗️
  - [`brainstate==0.4.0`](https://pypi.org/project/brainstate/0.4.0/) ↗️
  - [`brainevent==0.1.0`](https://pypi.org/project/brainevent/0.1.0/) ↗️
  - [`braintools==0.1.9`](https://pypi.org/project/braintools/0.1.9/) ↗️
  - [`braintrace==0.2.0`](https://pypi.org/project/braintrace/0.2.0/) ↗️
  - [`braincell==0.0.8`](https://pypi.org/project/braincell/0.0.8/)
  - [`brainpy-state==0.0.4`](https://pypi.org/project/brainpy-state/0.0.4/)
  - [`brainmass==0.0.5`](https://pypi.org/project/brainmass/0.0.5/)
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/)

- **Typing:**
  - Added a [PEP 561](https://peps.python.org/pep-0561/) `py.typed` marker so that
    downstream type checkers (mypy, pyright) treat `BrainX` as a typed package
  - Declared `py.typed` as package data in `pyproject.toml` so it ships in the wheel

- **Continuous Integration:**
  - Merged the push/pull-request workflow and the scheduled workflow into a single
    `CI.yml`
  - The cross-platform test suite (Linux, macOS, Windows) runs on push, pull
    request, and manual dispatch
  - A JAX-version compatibility matrix (`0.7.1`, `0.8.0`, `0.9.0`, and latest) runs
    on a daily schedule and on manual dispatch

- **Repository:**
  - Renamed the GitHub repository from `brain-modeling-ecosystem` to `brainx`;
    updated all source, documentation, and packaging URLs accordingly

- **Documentation:**
  - Corrected the "Open in Colab/Kaggle" badges in every example notebook to target
    their actual paths on the `main` branch
  - Replaced the logo and favicon with hosted WebP assets and removed the bundled
    3.5 MB `plotly.js`
  - Removed unused static assets (legacy PWA manifest, service worker, and stale
    images)

- **README:**
  - Fixed the BrainTrace link, which previously pointed at the renamed `brainscale`
    repository
  - Added PINNx to the list of ecosystem components
  - Replaced the broken Read the Docs badge with Documentation and License badges



## v2026.3.12

This release updates package dependencies and drops Python 3.10 support.

- **Package Dependencies:**
  - [`jax<=0.9.1,>=0.6.0`](https://pypi.org/project/jax/) ↗️ (adjusted upper bound)
  - [`brainpy-state==0.0.4`](https://pypi.org/project/brainpy-state/0.0.4/) ↗️
  - [`brainpy==2.7.7`](https://pypi.org/project/brainpy/2.7.7/) ↗️
  - [`brainunit==0.2.0`](https://pypi.org/project/brainunit/0.2.0/) ↗️
  - [`brainstate==0.3.0`](https://pypi.org/project/brainstate/0.3.0/) ↗️
  - [`brainevent==0.0.7`](https://pypi.org/project/brainevent/0.0.7/) ↗️
  - [`braincell==0.0.8`](https://pypi.org/project/braincell/0.0.8/) ↗️
  - [`braintools==0.1.8`](https://pypi.org/project/braintools/0.1.8/)
  - [`braintrace==0.1.2`](https://pypi.org/project/braintrace/0.1.2/)
  - [`brainmass==0.0.5`](https://pypi.org/project/brainmass/0.0.5/)
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/)

- **Project Configuration:**
  - Dropped Python 3.10 support; minimum Python version is now `>=3.11`
  - Removed version bounds from JAX optional extras (`cpu`, `cuda12`, `cuda13`, `tpu`)



## v2026.1.31

This release updates package dependencies and includes extensive documentation formatting improvements.

- **Package Dependencies:**
  - [`jax>=0.6.0,<0.9.0`](https://pypi.org/project/jax/) ↗️ (added upper bound)
  - [`brainpy-state==0.0.3`](https://pypi.org/project/brainpy-state/0.0.3/)
  - [`brainpy==2.7.6`](https://pypi.org/project/brainpy/2.7.6/)
  - [`brainunit==0.1.4`](https://pypi.org/project/brainunit/0.1.4/) ↗️
  - [`brainstate==0.2.10`](https://pypi.org/project/brainstate/0.2.10/) ↗️
  - [`brainevent==0.0.5`](https://pypi.org/project/brainevent/0.0.5/)
  - [`braincell==0.0.7`](https://pypi.org/project/braincell/0.0.7/)
  - [`braintools==0.1.8`](https://pypi.org/project/braintools/0.1.8/)
  - [`braintrace==0.1.2`](https://pypi.org/project/braintrace/0.1.2/)
  - [`brainmass==0.0.5`](https://pypi.org/project/brainmass/0.0.5/)
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/)

- **Documentation:**
  - Extensive formatting improvements across documentation notebooks and markdown files
  - Renamed `highlight_test_lexer.py` to `fix_ipython.py` for better clarity
  - Updated all example notebooks with improved formatting and structure
  - Refreshed documentation structure and presentation

- **Project Files:**
  - Updated GitHub templates (issue templates, PR template)
  - Improved CI/CD workflow configurations
  - Updated project configuration files (.gitignore, .pre-commit-config.yaml, .readthedocs.yml)
  - Enhanced contributing guidelines and code of conduct



## v2026.1.22

This release updates braintools package dependency.

- **Package Dependencies:**
  - [`jax>=0.6.0`](https://pypi.org/project/jax/)
  - [`brainpy-state==0.0.3`](https://pypi.org/project/brainpy-state/0.0.3/)
  - [`brainpy==2.7.6`](https://pypi.org/project/brainpy/2.7.6/)
  - [`brainunit==0.1.3`](https://pypi.org/project/brainunit/0.1.3/)
  - [`brainstate==0.2.9`](https://pypi.org/project/brainstate/0.2.9/)
  - [`brainevent==0.0.5`](https://pypi.org/project/brainevent/0.0.5/)
  - [`braincell==0.0.7`](https://pypi.org/project/braincell/0.0.7/)
  - [`braintools==0.1.8`](https://pypi.org/project/braintools/0.1.8/) ↗️
  - [`braintrace==0.1.2`](https://pypi.org/project/braintrace/0.1.2/)
  - [`brainmass==0.0.5`](https://pypi.org/project/brainmass/0.0.5/)
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/)



## v2026.1.21

This release updates brainpy package dependency.

- **Package Dependencies:**
  - [`jax>=0.6.0`](https://pypi.org/project/jax/)
  - [`brainpy-state==0.0.3`](https://pypi.org/project/brainpy-state/0.0.3/)
  - [`brainpy==2.7.6`](https://pypi.org/project/brainpy/2.7.6/) ↗️
  - [`brainunit==0.1.3`](https://pypi.org/project/brainunit/0.1.3/)
  - [`brainstate==0.2.9`](https://pypi.org/project/brainstate/0.2.9/)
  - [`brainevent==0.0.5`](https://pypi.org/project/brainevent/0.0.5/)
  - [`braincell==0.0.7`](https://pypi.org/project/braincell/0.0.7/)
  - [`braintools==0.1.7`](https://pypi.org/project/braintools/0.1.7/)
  - [`braintrace==0.1.2`](https://pypi.org/project/braintrace/0.1.2/)
  - [`brainmass==0.0.5`](https://pypi.org/project/brainmass/0.0.5/)
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/)



## v2026.1.19

This release updates package dependencies and CI/CD infrastructure.

- **Package Dependencies:**
  - [`jax>=0.6.0`](https://pypi.org/project/jax/)
  - [`brainpy-state==0.0.3`](https://pypi.org/project/brainpy-state/0.0.3/)
  - [`brainpy==2.7.5`](https://pypi.org/project/brainpy/2.7.5/)
  - [`brainunit==0.1.3`](https://pypi.org/project/brainunit/0.1.3/)
  - [`brainstate==0.2.9`](https://pypi.org/project/brainstate/0.2.9/) ↗️
  - [`brainevent==0.0.5`](https://pypi.org/project/brainevent/0.0.5/)
  - [`braincell==0.0.7`](https://pypi.org/project/braincell/0.0.7/)
  - [`braintools==0.1.7`](https://pypi.org/project/braintools/0.1.7/) ↗️
  - [`braintrace==0.1.2`](https://pypi.org/project/braintrace/0.1.2/)
  - [`brainmass==0.0.5`](https://pypi.org/project/brainmass/0.0.5/)
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/)

- **Documentation:**
  - Updated paper reference for BrainTrace in ecosystem.html

- **CI/CD:**
  - Bumped styfle/cancel-workflow-action from 0.12.1 to 0.13.0 (#57)



## v2026.1.16

This release updates package dependencies, documentation, and copyright notices.

- **Package Dependencies:**
  - [`jax>=0.6.0`](https://pypi.org/project/jax/)
  - [`brainpy-state==0.0.2`](https://pypi.org/project/brainpy-state/0.0.2/)
  - [`brainpy==2.7.5`](https://pypi.org/project/brainpy/2.7.5/)
  - [`brainunit==0.1.3`](https://pypi.org/project/brainunit/0.1.3/)
  - [`brainstate==0.2.9`](https://pypi.org/project/brainstate/0.2.9/) ↗️
  - [`brainevent==0.0.5`](https://pypi.org/project/brainevent/0.0.5/)
  - [`braincell==0.0.6`](https://pypi.org/project/braincell/0.0.6/)
  - [`braintools==0.1.7`](https://pypi.org/project/braintools/0.1.7/) ↗️
  - [`braintrace==0.1.2`](https://pypi.org/project/braintrace/0.1.2/)
  - [`brainmass==0.0.4`](https://pypi.org/project/brainmass/0.0.4/)
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/)

- **Copyright:**
  - Updated copyright notice from BDP Ecosystem Limited to BrainX Ecosystem Limited

- **Documentation:**
  - Updated paper reference for BrainTrace in ecosystem.html
  - Removed papers_using_us.md file

- **CI/CD:**
  - Bumped styfle/cancel-workflow-action from 0.12.1 to 0.13.0 (#57)
  - Bumped braintools from 0.1.6 to 0.1.7 (#56)

- **Code Updates:**
  - Updated import statements from `brainpy` to `brainpy.state` in notebooks (#55)
  - Updated CI configuration to use Python 3.13 and adjusted JAX versions
  - Updated multiple documentation notebooks with corrected imports and examples



## v2025.12.26

This release updates multiple package dependencies and improves CI/CD infrastructure.

- **Package Dependencies:**
  - [`jax>=0.6.0`](https://pypi.org/project/jax/)
  - [`brainpy-state==0.0.2`](https://pypi.org/project/brainpy-state/0.0.2/) ↗️
  - [`brainpy==2.7.5`](https://pypi.org/project/brainpy/2.7.5/) ↗️
  - [`brainunit==0.1.3`](https://pypi.org/project/brainunit/0.1.3/) 
  - [`brainstate==0.2.8`](https://pypi.org/project/brainstate/0.2.8/) 
  - [`brainevent==0.0.5`](https://pypi.org/project/brainevent/0.0.5/) 
  - [`braincell==0.0.6`](https://pypi.org/project/braincell/0.0.6/)
  - [`braintools==0.1.6`](https://pypi.org/project/braintools/0.1.6/) 
  - [`braintrace==0.1.2`](https://pypi.org/project/braintrace/0.1.2/) 
  - [`brainmass==0.0.4`](https://pypi.org/project/brainmass/0.0.4/)
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/)




## v2025.12.25

This release updates multiple package dependencies and improves CI/CD infrastructure.

- **Package Dependencies:**
  - [`jax>=0.6.0`](https://pypi.org/project/jax/)
  - [`brainpy-state==0.0.1`](https://pypi.org/project/brainpy-state/0.0.1/) ↗️ (new, replaces brainpy)
  - [`brainunit==0.1.3`](https://pypi.org/project/brainunit/0.1.3/) ↗️
  - [`brainstate==0.2.8`](https://pypi.org/project/brainstate/0.2.8/) ↗️
  - [`brainevent==0.0.5`](https://pypi.org/project/brainevent/0.0.5/) ↗️
  - [`braincell==0.0.6`](https://pypi.org/project/braincell/0.0.6/)
  - [`braintools==0.1.6`](https://pypi.org/project/braintools/0.1.6/) ↗️
  - [`braintrace==0.1.2`](https://pypi.org/project/braintrace/0.1.2/) ↗️
  - [`brainmass==0.0.4`](https://pypi.org/project/brainmass/0.0.4/)
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/)

- **CI/CD:**
  - Bumped actions/checkout from 5 to 6 (#48)



## v2025.12.2

This release introduces BrainTrace (replacing BrainScale) and updates multiple package dependencies.

- **Package Dependencies:**
  - [`jax>=0.6.0`](https://pypi.org/project/jax/) ↗️
  - [`brainpy==2.7.2`](https://pypi.org/project/brainpy/2.7.2/) ↗️
  - [`brainunit==0.1.2`](https://pypi.org/project/brainunit/0.1.2/)
  - [`brainstate==0.2.6`](https://pypi.org/project/brainstate/0.2.6/) ↗️
  - [`brainevent==0.0.4`](https://pypi.org/project/brainevent/0.0.4/)
  - [`braincell==0.0.6`](https://pypi.org/project/braincell/0.0.6/)
  - [`braintools==0.1.4`](https://pypi.org/project/braintools/0.1.4/) ↗️
  - [`braintrace==0.1.1`](https://pypi.org/project/braintrace/0.1.1/) ↗️ (renamed from brainscale)
  - [`brainmass==0.0.4`](https://pypi.org/project/brainmass/0.0.4/)
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/) ↗️ (new)

- **Documentation Updates:**
  - Renamed BrainScale to BrainTrace in documentation and requirements
  - Updated ecosystem documentation with additional descriptions
  - Deprecated BrainTaichi component
  - Removed 3D card effect from ecosystem.html
  - Added braintools import and updated class inheritance in spiking network notebooks

- **CI/CD:**
  - Bumped actions/upload-artifact from 4 to 5 (#46)



## v2025.10.13

This is the first release of the **complete** BrainX ecosystem, integrating multiple packages for comprehensive brain simulation and analysis.

- **Package Dependencies:**
  - [`jax>=0.6.0,<0.8.0`](https://pypi.org/project/jax/) 
  - [`brainpy==2.7.1`](https://pypi.org/project/brainpy/2.7.1/) ↗️
  - [`brainunit==0.1.1`](https://pypi.org/project/brainunit/0.1.1/)
  - [`brainstate==0.2.3`](https://pypi.org/project/brainstate/0.2.3/) ↗️
  - [`brainevent==0.0.4`](https://pypi.org/project/brainevent/0.0.4/)
  - [`braincell==0.0.6`](https://pypi.org/project/braincell/0.0.6/) ↗️
  - [`braintools==0.1.3`](https://pypi.org/project/braintools/0.1.3/) ↗️
  - [`brainscale==0.1.0`](https://pypi.org/project/brainscale/0.1.0/) ↗️
  - [`brainmass==0.0.4`](https://pypi.org/project/brainmass/0.0.4/) ↗️

- **Documentation Fixes:**
  - Updated BrainPy link in ecosystem documentation (#43)
  - Fixed image sources to use absolute URLs for BrainMass and BrainEvent logos
  - Copied CHANGELOG.md to the documentation directory for better accessibility
  - Reorganized static JavaScript files (moved service-worker.js to js subdirectory)

- **README Updates:**
  - Updated documentation and references (#42, #43)



## v2025.10.08 (yanked)

- **Project Updates:**
  - First integrative version of the BrainX ecosystem (#40)
  - Rebranded to BrainX and revamped documentation (#23)
  - Updated project description and author details to "BrainX Ecosystem"
  - Added support for CUDA 13 in optional dependencies

- **Documentation Enhancements:**
  - Enhanced brain simulation documentation with English and Chinese versions (#36)
  - Added comprehensive core components documentation (#29)
  - Added HH thalamus oscillations notebooks and examples (#31, #32)
  - Updated core components documentation and removed obsolete Golgi file (#33)
  - Added Kaggle dataset download for Golgi cell morphology (#25)
  - Fixed ipython2 lexer to ipython3 in notebooks (#27)
  - Corrected titles and updated references in documentation files

- **Package Dependencies:**
  - `jax>=0.6.0,<0.8.0` ↗️
  - `brainpy==3.0.0` ↗️
  - `brainunit==0.1.1` (from 0.0.18)
  - `brainstate==0.2.1` ↗️ (from 0.1.10)
  - `brainevent==0.0.4`
  - `braincell==0.0.5` ↗️ (from 0.0.4)
  - `braintools==0.1.1` ↗️ (from 0.0.12)
  - `brainscale==0.0.11` ↗️ (from 0.0.10)
  - `brainmass==0.0.3`

- **CI/CD:**
  - Bumped actions/setup-python from 5 to 6 (#26)
  - Bumped actions/checkout from 4 to 5

- **Fixes:**
  - Updated project name and copyright in conf.py; refactored lexer import (#28)
  - Updated Golgi cell notebook to include Kaggle dataset download and path adjustments
  - Updated index.rst to reference brain_simulation_point_neuron.md (#24)

## v2025.9.15
- `BrainX` packages: 
  - `numpy>=1.15` ️↗️ 
  - `jax>=0.4.35,<0.8.0` ↗️ 
  - `brainunit==0.1.1` ↗️
  - `brainstate==0.1.10` ↗️
  - `brainevent==0.0.4` ↗️
  - `braincell==0.0.4` ↗️
  - `braintools==0.0.11` ↗️
  - `brainscale==0.0.10` ↗️
  - `brainmass==0.0.3` ↗️
  - `msgpack>=1.1.0` ↗️
  - `matplotlib` ↗️

