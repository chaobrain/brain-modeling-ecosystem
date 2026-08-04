---
orphan: true
---

# brainpy to brainx

`brainpy` is the experimental precursor to `brainx`. It served as an embryo for
the later `brainx` ecosystem: the initial ideas explored in `brainpy` inspired
the architecture of `brainx`, where those ideas were developed into focused,
production-level packages.

For example, the neural-mass modeling explored in `brainpy` later evolved into
the dedicated `brainmass` package. The Hodgkin-Huxley cell models in `brainpy`
inspired the more comprehensive conductance-based models, ion-channel systems,
and neuronal morphology support now provided by `braincell`.

`brainpy` remains useful as an experimental package and as the origin of many
of the ecosystem's concepts. For new projects, `brainx` provides the
production-level implementations, broader capabilities, and better performance.

## Where brainpy fits

`brainpy` was designed as a general-purpose package for brain dynamics
programming. Its main advantage was point-neuron modeling, including individual
neurons, synapses, and spiking neural networks. That point-neuron scale has
evolved into `brainpy.state`, the production-level point-neuron modeling package
within `brainx`.

For new point-neuron projects, use `brainpy.state`. Existing `brainpy` projects
do not need to be rewritten immediately if they already meet their goals.
Migration becomes more valuable when a project needs deeper integration with
the rest of `brainx`, newer infrastructure, or long-term ecosystem support.

## Compatibility

The current `brainpy` codebase has been reconstructed on top of `brainstate`,
`brainevent`, and `braintools`. This makes it compatible with those foundational
packages and with the modeling packages built on the same infrastructure.

| package | compatibility |
| --- | --- |
| `brainstate` | Compatible; the reconstructed `brainpy` runtime is based on `brainstate` |
| `brainevent` | Compatible; reconstructed event-driven operations use `brainevent` |
| `braintools` | Compatible; reconstructed utilities use `braintools` |
| `braincell` | Compatible, but new cellular models should use `braincell` directly |
| `brainmass` | Compatible, but new neural-mass models should use `brainmass` directly |
| `brainunit` | Not compatible |
| `braintrace` | Not compatible |

The `brainunit` and `braintrace` exceptions limit how fully a `brainpy` project
can participate in the production-level `brainx` ecosystem.

## Cellular modeling

For biophysical neuron models involving ions, ion channels, compartments, or
neuronal morphology, migrate completely to `brainpy.state` and `braincell`.

The older ion and channel APIs in `brainpy` have known design limitations, and
its compartmental modeling support is restricted to single-compartment models.
`braincell` provides more comprehensive conductance-based and Hodgkin-Huxley
models together with morphologically structured, multicompartment cells.
Mixing the experimental `brainpy` cell APIs into new `braincell`-based work is
therefore not recommended.

## The remaining brainpy exception: analysis

The analysis module in `brainpy` is the main capability that does not yet have
a direct replacement elsewhere in `brainx`. If a workflow depends on this
module, `brainpy` may still be the appropriate tool for that part of the
project.

This is the important exception to the general migration guidance: `brainx`
covers the modeling and simulation roles of `brainpy`, but its dedicated
analysis functionality remains unique for now.

## Quick decision guide

| use case | recommended choice |
| --- | --- |
| Starting a new point-neuron project | `brainpy.state` |
| Maintaining an existing `brainpy` project | Continue with `brainpy`; migrate for integration |
| Modeling ions, ion channels, or morphology | `brainpy.state` and `braincell` |
| Using `brainunit` or `braintrace` | Migrate away from `brainpy` |
| Relying on the analysis module in `brainpy` | Continue using `brainpy` for analysis |

## In short

Treat `brainpy` as the experimental embryo that inspired the `brainx` ecosystem.
It remains usable for established projects and its unique analysis tools, but
`brainx` is the production-level destination for new work. Use `brainpy.state`
for point-neuron modeling, `braincell` for ions, channels, and morphology, and
`brainmass` for neural-mass and whole-brain models.
