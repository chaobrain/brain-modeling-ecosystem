# Change log

↗️ = updated since previous release





## v2025.12.2

This release introduces BrainTrace (replacing BrainScale) and updates multiple package dependencies.

- **Package Dependencies:**
  - [`jax>=0.6.0`](https://pypi.org/project/jax/) ↗️ (removed upper bound)
  - [`brainpy==2.7.2`](https://pypi.org/project/brainpy/2.7.2/) ↗️
  - [`brainunit==0.1.2`](https://pypi.org/project/brainunit/0.1.1/)
  - [`brainstate==0.2.6`](https://pypi.org/project/brainstate/0.2.5/) ↗️
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

