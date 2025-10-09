# Change log

↗️ = updated since previous release


## v2025.10.08
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

