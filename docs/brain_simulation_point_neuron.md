# Brain simulation with point neuron models

Point neuron networks let us approximate large spiking circuits while keeping every cell to a single dynamic
compartment. This page explains how the notebooks in this section assemble morphology-free neurons into reproducible
experiments that scale from microcircuits to whole-brain studies.


## English version

The following notebooks provide hands-on guides:

- `brainstate_drosophila_wholebrain_simulation.ipynb`: assembles a drosophila-wide connectome, demonstrates balanced
  excitation/inhibition tuning, and benchmarks runtime scaling.
- `brainstate_spiking_gamma_oscillations.ipynb`: reproduces cortical gamma oscillations with point neurons, including
  stimulus-evoked modulation analyses.
- `braincell_HH_thalamus_oscillations.ipynb`: demonstrates Hodgkin-Huxley-inspired point neurons in a thalamic loop,
  highlighting rebound bursting control.

```{toctree}
:maxdepth: 1

brainstate_drosophila_wholebrain_simulation.ipynb
brainstate_spiking_gamma_oscillations.ipynb
braincell_HH_thalamus_oscillations.ipynb
```

## 中文版本

```{toctree}
:maxdepth: 1

braincell_HH_thalamus_oscillations-zh.ipynb
```
