# Change log

↗️ = updated since previous release




## v2026.6.29

This is a maintenance and refinement release. It refreshes two ecosystem
components to their latest releases — **BrainState `0.5.2`** and **BrainTrace
`0.2.2`** — slims the bundled dependency set by **removing `pinnx`**, and adds a
cross-package **compatibility / correctness test suite** that exercises the pinned
stack end-to-end. The two component bumps are *coupled*: BrainTrace `0.2.2`
requires BrainState `>= 0.5.2`, and BrainState `0.5.2`'s new `in_new_state_probe()`
is exactly the hook BrainTrace's unified `compile` path uses to cooperate with the
eager state-discovery probe — so the pinned set stays mutually consistent.

- **Package Dependencies:**
  - [`jax<=0.10.2,>=0.8.0`](https://pypi.org/project/jax/)
  - [`brainunit==0.5.1`](https://pypi.org/project/brainunit/0.5.1/)
  - [`brainevent==0.1.1`](https://pypi.org/project/brainevent/0.1.1/)
  - [`brainstate==0.5.2`](https://pypi.org/project/brainstate/0.5.2/) ↗️
  - [`braintools==0.3.0`](https://pypi.org/project/braintools/0.3.0/)
  - [`braintrace==0.2.2`](https://pypi.org/project/braintrace/0.2.2/) ↗️
  - [`braincell==0.1.0`](https://pypi.org/project/braincell/0.1.0/)
  - [`brainpy==2.8.0`](https://pypi.org/project/brainpy/2.8.0/)
  - [`brainpy-state==0.1.0`](https://pypi.org/project/brainpy-state/0.1.0/)
  - [`brainmass==0.1.1`](https://pypi.org/project/brainmass/0.1.1/)
  - `pinnx` — **removed** from the bundled dependency set (see below)

- **BrainState `0.5.2` — additive transform feature:**
  - Adds `brainstate.transform.in_new_state_probe()`, a public predicate that lets
    state-bound, one-shot consumers cooperate with the eager discovery probe that
    `vmap_new_states` / `vmap2_new_states` / `pmap2_new_states` run to enumerate the
    states a function creates before the real mapped pass
  - Implemented as a thread-local depth counter, so it composes under nested
    `*_new_states` calls and resets cleanly even if the probe raises
  - No public API is removed or renamed, and behavior is unchanged for code that
    does not call the new helper; 28 new regression tests, green on the JAX
    `0.7`–latest matrix and the type-check gate

- **BrainTrace `0.2.2` — unified online-learning entry point and vmap fixes:**
  - `braintrace.compile(model, algorithm, *example_inputs, ...)` is now the
    canonical single call for building a compiled eligibility-trace learner — it
    always initializes states, accepts `seed` / `verbose`, adds a `vmap=` option for
    per-sample state initialization, and exposes a structured `CompilationReport`
  - Adds a recurrent mixing mode to graph construction, broadening the set of cell
    topologies the compiler can connect
  - Fixes eligibility-trace convergence under `vmap` / `brainstate.mixin.Batching()`
    by deferring compilation during the discovery probe (aligning convolutional and
    element-wise traces), and routes `LoRA` through the ETP `lora_matmul` primitive
    so its factors participate in trace learning
  - Migrates unit handling from `saiunit` to `brainunit` (a re-export, so it is
    drop-in), raises the `brainstate` floor to `>= 0.5.2`, targets Python 3.14, and
    renames private modules (`_etrace_*` → `_*`); 1604 tests pass and the documented
    0.2.x public API is unchanged

- **Removed `pinnx` from the bundled set:**
  - The default `brainx` install now scopes to the core brain-simulation stack;
    [PINNx](https://github.com/chaobrain/pinnx) (physics-informed neural networks)
    remains a fully supported, independently released ecosystem project and can
    still be installed on its own with `pip install pinnx`

- **Cross-package compatibility testing:**
  - Adds `BrainX/compatibility_test.py`, a co-located suite that imports the pinned
    packages together and drives small, deterministic computations across package
    boundaries: a unit-carrying `brainstate` state integrated by
    `transform.for_loop`, `brainevent` event/sparse operators checked against dense
    references, `braintools` initializers/metrics, a `brainpy.state` neuron step, a
    `braincell.SingleCompartment` integration, a `brainmass` mean-field run, and the
    `braintrace.compile` eligibility-trace path on BrainState `0.5.2`
  - Tests are now co-located beside the package in the suffix style: the legacy
    `BrainX/tests/test_version.py` becomes `BrainX/version_test.py` (the `tests/`
    folder is removed), it drops its `pinnx` import and pin and now also imports
    `braintrace`, and `pyproject.toml` configures pytest to collect `*_test.py`



## v2026.6.19

This is a landmark release: the **first fully integrated and compatibility-hardened
BrainX collection**. Every pinned component has been independently audited for
correctness, retested, and aligned to a single, mutually-consistent dependency
contract — resolving the cross-package incompatibilities and latent numerical bugs
that affected earlier mixed-version combinations. The result is the most complete
and stable BrainX stack to date, spanning the full modeling spectrum: from
**morphologically detailed single-cell modeling** (dendritic, multi-compartment),
through **point-neuron network simulation**, to **neural-mass / firing-rate
whole-brain modeling** — all differentiable, unit-aware, and built on a shared JAX
foundation.

- **Package Dependencies:**
  - [`jax<=0.10.2,>=0.8.0`](https://pypi.org/project/jax/) ↗️ (raised both bounds; JAX 0.10.2 now supported)
  - [`brainunit==0.5.1`](https://pypi.org/project/brainunit/0.5.1/) ↗️
  - [`brainevent==0.1.1`](https://pypi.org/project/brainevent/0.1.1/) ↗️
  - [`brainstate==0.5.1`](https://pypi.org/project/brainstate/0.5.1/) ↗️
  - [`braintools==0.3.0`](https://pypi.org/project/braintools/0.3.0/) ↗️
  - [`braintrace==0.2.1`](https://pypi.org/project/braintrace/0.2.1/) ↗️
  - [`braincell==0.1.0`](https://pypi.org/project/braincell/0.1.0/) ↗️
  - [`brainpy==2.8.0`](https://pypi.org/project/brainpy/2.8.0/) ↗️
  - [`brainpy-state==0.1.0`](https://pypi.org/project/brainpy-state/0.1.0/)
  - [`brainmass==0.1.1`](https://pypi.org/project/brainmass/0.1.1/) ↗️
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/)

- **BrainCell `0.1.0` — multi-compartment, morphologically detailed neurons:**
  - Evolves from single-compartment Hodgkin–Huxley into a complete multi-compartment
    framework: a `Cell` declaration frontend, a frozen `RunnableCell` runtime, and a
    high-level `rcell.run(dt=, duration=)` driver returning a structured `RunResult`
  - Immutable morphology layer (`Soma` / `Dendrite` / `Axon` / `BasalDendrite` /
    `ApicalDendrite` / `CustomBranch`) plus a mutable `Morphology` tree
  - Pure-functional control-volume discretization with composable policies
    (`CVPerBranch`, `DLambda`, `MaxCVLen`) and an execution-graph compute runtime
  - Declarative mechanism system (`braincell.mech`), morphology IO (`braincell.io`:
    SWC / ASC / NeuroML2 readers, NeuroMorpho.Org client), location/region filters,
    and a 2D/3D visualization stack (matplotlib, PyVista, Plotly)
  - Added cerebellar dynamics (Purkinje-cell comparison scaffold); package now
    PEP 561-typed

- **BrainMass `0.1.1` — differentiable whole-brain modeling:**
  - Turns a library of neural-mass *models* into an end-to-end *simulate → observe →
    score* toolkit (introduced in `0.1.0`), with gradients flowing through the entire
    pipeline so parameters can be recovered by gradient descent
  - High-level `Simulator`, `Network`, and `Fitter` (gradient-based Optax,
    gradient-free Nevergrad, and Bayesian scikit-optimize backends)
  - Seven new literature-faithful mean-field models (Epileptor, Larter–Breakspear,
    Coombes–Byrne, Generic 2-D oscillator, Wong–Wang E/I, Lorenz, Linear) — 17 model
    families total — plus nonlinear couplings, an HRF-BOLD forward model, and
    composable differentiable objectives (time-series RMSE, FC, FCD)
  - Bundled `datasets`, optional `viz` helpers, `list_models()`, and a new
    Diátaxis-organized documentation site
  - `0.1.1` raises the `braintools` constraint to `>=0.3.0` (the release that fixed
    the `init.param` batched-init regression), so brainmass co-installs with
    `brainpy` 2.8.0 across the ecosystem

- **BrainPy `2.8.0` — library-wide correctness sweep and static typing:**
  - Audited bug-fix pass across neuron/synapse dynamics, ODE/SDE/FDE integrators, the
    math and object-transform layer, `dnn` layers, optimizers, losses, analysis, and
    runners — each fix backed by regression tests (notably a `CondNeuGroup`
    synaptic-current scaling error that attenuated currents ~1000×)
  - Static typing with a new `mypy` CI gate (PEP 561); coverage raised from ~84% to
    92%+; tests co-located as `<module>_test.py`
  - Removed forked internals by reusing the shared `braintools` (init, metric,
    surrogate) and `brainstate` (transforms) implementations

- **BrainTools `0.3.0` — completed correctness, coverage, and documentation audit:**
  - Completes the codebase-wide audit campaign begun in `0.2.0` across `metric`,
    `trainer`, `optim`, `visualize`, `surrogate`, `quad`, `init`, `conn`, `file`, and
    `cogtask`, lifting per-module coverage to ~92–100%
  - Corrected genuine numerical/algorithmic bugs: inverted surrogate-gradient
    formulas, an `nll_loss` sign error, LFP coherence identically `1`, He/Kaiming
    initialization variance off by 2×, double-applied SM3 momentum, a centered
    RMSprop that was a silent no-op, and dropped `cogtask.Parallel` branches
  - New/restored public API: `file.save_matfile`, gradient accumulation and
    name-based parameter freezing in `trainer`, an `LBFGS` line-search, exported
    `metric.safe_norm` / pairwise-cosine helpers, `cogtask.create_task`, and
    `metric.L1Loss`

- **BrainState `0.5.1` — JAX 0.10.2 compatibility:**
  - Fixes the `vmap` regression caused by JAX 0.10 removing
    `jax.interpreters.batching.not_mapped`; the `unvmap` primitives now resolve the
    sentinel version-agnostically (full suite: 5312 passed). No public API changes;
    compatible across `jax>=0.7.0`

- **BrainEvent `0.1.1` — custom-operator / FFI hardening:**
  - Audit of the JAX custom-op / FFI layer fixed ~30 defects that produced
    silently-wrong output or process crashes (proper `XLA_FFI_Error` propagation,
    fp16/bf16/complex handling, a multi-GPU device-binding race, corrected
    `indptr` / CSC construction)
  - The numba FFI bridge now works across `jax` 0.7–0.9 (not only 0.10+), and
    compatibility with newer JAX is restored. No public API changes

- **BrainTrace `0.2.1` — ecosystem dependency compatibility:**
  - Adopts `brainstate` 0.5's typed (PEP 561) surface (clearing 154 mypy errors),
    updates for hardened convolution validation, and fixes `pytest` 9.1 collection
    (1367 passed, mypy clean, `py.typed` shipped). No functional/API changes

- **BrainUnit `0.5.1` — unit-contract compatibility patch:**
  - Resolves the upstream `saiunit` / `brainunit` unit-contract issue surfaced across
    the ecosystem (the `rtol` dimensionless / `atol` unit-carrying convention),
    keeping numerical-tolerance handling consistent with `braintrace` 0.2.1 and
    `brainevent` 0.1.1. No public API changes

- **Cross-ecosystem compatibility:**
  - BrainState 0.5.1, BrainUnit 0.5.1, BrainEvent 0.1.1, and BrainTrace 0.2.1 jointly
    resolve the JAX 0.10.x `vmap` / FFI regressions and the `saiunit` tolerance-unit
    contract, while BrainPy 2.8.0 and BrainTools 0.3.0 eliminate forked-internals
    drift by reusing the shared `braintools` / `brainstate` implementations. Earlier
    mixed-version stacks could surface `AttributeError` under `vmap`, silently-wrong
    FFI results, or unit-handling crashes — all addressed here
  - BrainMass 0.1.1 raises its `braintools` floor to `>=0.3.0` (matching BrainPy
    2.8.0's requirement), resolving the last `braintools` version conflict so the
    entire pinned set co-installs cleanly. The combination was validated end-to-end:
    the full BrainMass test suite (692 tests) passes against this exact dependency set



## v2026.6.18

This maintenance release upgrades BrainPy-State to its 0.1.0 release.

- **Package Dependencies:**
  - [`brainstate==0.5.0`](https://pypi.org/project/brainstate/0.5.0/)
  - [`brainunit==0.4.0`](https://pypi.org/project/brainunit/0.4.0/)
  - [`braintools==0.1.10`](https://pypi.org/project/braintools/0.1.10/)
  - [`brainevent==0.1.0`](https://pypi.org/project/brainevent/0.1.0/)
  - [`braintrace==0.2.0`](https://pypi.org/project/braintrace/0.2.0/)
  - [`braincell==0.0.8`](https://pypi.org/project/braincell/0.0.8/)
  - [`brainpy==2.7.8`](https://pypi.org/project/brainpy/2.7.8/)
  - [`brainpy-state==0.1.0`](https://pypi.org/project/brainpy-state/0.1.0/) ↗️
  - [`brainmass==0.0.5`](https://pypi.org/project/brainmass/0.0.5/)
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/)



## v2026.6.14

This maintenance release upgrades BrainState to its 0.5.0 release.

- **Package Dependencies:**
  - [`brainstate==0.5.0`](https://pypi.org/project/brainstate/0.5.0/) ↗️
  - [`brainunit==0.4.0`](https://pypi.org/project/brainunit/0.4.0/)
  - [`braintools==0.1.10`](https://pypi.org/project/braintools/0.1.10/)
  - [`brainevent==0.1.0`](https://pypi.org/project/brainevent/0.1.0/)
  - [`braintrace==0.2.0`](https://pypi.org/project/braintrace/0.2.0/)
  - [`braincell==0.0.8`](https://pypi.org/project/braincell/0.0.8/)
  - [`brainpy==2.7.8`](https://pypi.org/project/brainpy/2.7.8/)
  - [`brainpy-state==0.0.4`](https://pypi.org/project/brainpy-state/0.0.4/)
  - [`brainmass==0.0.5`](https://pypi.org/project/brainmass/0.0.5/)
  - [`pinnx==0.0.3`](https://pypi.org/project/pinnx/0.0.3/)



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

