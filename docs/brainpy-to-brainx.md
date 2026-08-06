# BrainPy to BrainX

[`brainpy`][brainpy] is the experimental precursor to [`brainx`][brainx]. It served as an prototype for
the later [`brainx`][brainx] ecosystem: the initial ideas explored in [`brainpy`][brainpy] inspired
the [`brainx`][brainx], where those ideas were developed into focused,
production-level packages.

For example, the neural-mass modeling explored in [`brainpy`][brainpy] later evolved into
the dedicated [`brainmass`][brainmass] package. The Hodgkin-Huxley cell models in [`brainpy`][brainpy]
inspired the more comprehensive conductance-based models, ion-channel systems,
and neuronal morphology support now provided by [`braincell`][braincell].

[`brainpy`][brainpy] remains useful as an experimental, legacy package and as the origin of many
of the ecosystem's concepts. For new projects, [`brainx`][brainx] provides the
production-level implementations, broader capabilities, and better performance.

## Where brainpy fits

[`brainpy`][brainpy] was designed as a general-purpose package for brain dynamics
programming. Its main advantage was point-neuron modeling, that point-neuron scale has
evolved into [`brainpy.state`][brainpy.state], the production-level point-neuron modeling package
within [`brainx`][brainx].

For new point-neuron projects, use [`brainpy.state`][brainpy.state]. Existing [`brainpy`][brainpy] projects
do not need to be rewritten immediately if they already meet their goals.
Migration becomes more valuable when a project needs deeper integration with
the rest of [`brainx`][brainx], newer infrastructure, or long-term ecosystem support.

## Compatibility

The current [`brainpy`][brainpy] codebase has been reconstructed on top of [`brainstate`][brainstate],
[`brainevent`][brainevent], and [`braintools`][braintools]. This makes it compatible with those foundational
packages and with the modeling packages built on the same infrastructure.

This is not only a dependency relationship. Many internal functions of
[`brainpy`][brainpy] have been rewritten to delegate to the production-level
implementations, so the two share the same underlying code rather than
maintaining parallel ports. For example:

- `brainpy.math.surrogate` is an alias of `braintools.surrogate`, and the
  einops-style helpers in `brainpy.math` are re-exported from `brainunit.math`.
- The sparse and event-driven operators in `brainpy.math.sparse`,
  `brainpy.math.event`, and `brainpy.math.jitconn` build [`brainevent`][brainevent]
  structures such as `CSR`, `COO`, and the just-in-time connectivity types,
  then hand the computation over to them.
- `brainpy.losses` and `brainpy.measure` delegate to `braintools.metric`,
  and `brainpy.initialize` delegates to `braintools.init`.
- `brainpy.inputs` builds its current waveforms from `braintools.input`, and
  `brainpy.visualization` from `braintools.visualize`.
- State handling, environment settings, and compiled transformations come from
  [`brainstate`][brainstate], through `State`, `environ`, and `transform`.

| package | compatibility |
| --- | --- |
| [`brainstate`][brainstate] | compatible |
| [`brainevent`][brainevent] | compatible |
| [`braintools`][braintools] | compatible |
| [`braincell`][braincell] | compatible |
| [`brainmass`][brainmass] | compatible |
| [`brainunit`][brainunit] | not compatible |
| [`braintrace`][braintrace] | not compatible |

The [`brainunit`][brainunit] and [`braintrace`][braintrace] exceptions limit how fully a [`brainpy`][brainpy] project
can participate in the production-level [`brainx`][brainx] ecosystem.

## Cellular modeling

For biophysical neuron models involving ions, ion channels, compartments, or
neuronal morphology, migrate completely to [`brainpy.state`][brainpy.state] and [`braincell`][braincell].

The older ion and channel APIs in [`brainpy`][brainpy] have known design limitations, and
its compartmental modeling support is restricted to single-compartment models.
[`braincell`][braincell] provides more comprehensive conductance-based and Hodgkin-Huxley
models together with morphologically structured, multicompartment cells.
Mixing the experimental [`brainpy`][brainpy] cell APIs into new [`braincell`][braincell]-based work is
therefore not recommended.

## Neural-mass modeling

For neural-mass, whole-brain, and rate-based models, migrate to [`brainmass`][brainmass].

The rate models in [`brainpy`][brainpy] cover FitzHugh-Nagumo, Stuart-Landau,
threshold-linear, and Wilson-Cowan dynamics. [`brainmass`][brainmass] provides direct
counterparts for these, together with many models [`brainpy`][brainpy] never had, including
Jansen-Rit, Epileptor, Hopf, Montbrió-Pazó-Roxin, Wong-Wang, and Larter-Breakspear.

Beyond the models themselves, [`brainmass`][brainmass] adds the infrastructure that
whole-brain work needs: explicit coupling schemes, structured noise processes,
forward models for BOLD, EEG, and MEG signals, and parameter fitting against
empirical data.

Unlike the cellular case, this is not a warning. The [`brainpy`][brainpy] rate models
remain usable, and [`brainmass`][brainmass] is compatible with the same foundational
packages. It is simply that this modeling scale is now developed in
[`brainmass`][brainmass].

## The remaining brainpy exception: analysis

The analysis module in [`brainpy`][brainpy] is the main capability that does not yet have
a direct replacement elsewhere in [`brainx`][brainx]. If a workflow depends on this
module, [`brainpy`][brainpy] may still be the appropriate tool for that part of the
project.

This is the important exception to the general migration guidance: [`brainx`][brainx]
covers the modeling and simulation roles of [`brainpy`][brainpy], but its dedicated
analysis functionality remains unique for now.

## Quick decision guide

| use case | recommended choice |
| --- | --- |
| Starting a new point-neuron project | [`brainpy.state`][brainpy.state] |
| Maintaining an existing [`brainpy`][brainpy] project | Continue with [`brainpy`][brainpy]; migrate for integration |
| Modeling ions, ion channels, or morphology | [`brainpy.state`][brainpy.state] and [`braincell`][braincell] |
| Modeling neural-mass or whole-brain dynamics | [`brainmass`][brainmass] |
| Using [`brainunit`][brainunit] or [`braintrace`][braintrace] | Migrate away from [`brainpy`][brainpy] |
| Relying on the analysis module in [`brainpy`][brainpy] | Continue using [`brainpy`][brainpy] for analysis |

## In short

Treat [`brainpy`][brainpy] as the experimental embryo that inspired the [`brainx`][brainx] ecosystem.
It remains usable for established projects and its unique analysis tools, but
[`brainx`][brainx] is the production-level destination for new work. Use [`brainpy.state`][brainpy.state]
for point-neuron modeling, [`braincell`][braincell] for ions, channels, and morphology, and
[`brainmass`][brainmass] for neural-mass and whole-brain models.

[brainx]: https://brainx.chaobrain.com/
[brainpy]: https://brainpy.readthedocs.io/
[brainpy.state]: https://brainx.chaobrain.com/brainpy-state/
[brainstate]: https://brainx.chaobrain.com/brainstate/
[brainevent]: https://brainx.chaobrain.com/brainevent/
[braintools]: https://brainx.chaobrain.com/braintools/
[braincell]: https://brainx.chaobrain.com/braincell/
[brainmass]: https://brainx.chaobrain.com/brainmass/
[brainunit]: https://brainx.chaobrain.com/brainunit/
[braintrace]: https://brainx.chaobrain.com/braintrace/
