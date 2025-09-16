# Starting brain simulation with BrainX 

[BrainX](https://github.com/chaobrain) provides a comprehensive platform for 
simulating brain activity at multiple scales, from individual neurons to 
large-scale brain networks. 

This tutorial will guide you through the basics of setting up and running 
your first brain simulation using ``BrainX``.


## Who is this tutorial for?

- Learners new to BrainX who want a gentle, practical start.
- Students of computational neuroscience exploring multi‑scale modeling.
- Researchers and engineers prototyping neuron, network, or rate‑model simulations.
- Python users comfortable with Jupyter notebooks and basic numerical computing.

Recommended prerequisites:

- Python, Jupyter, and basic familiarity with differential equations and signals.
- A working BrainX [installation](./install.md) as set up in your environment for this repo.

## What does this tutorial cover?

This tutorial walks through BrainX across three model scales with runnable notebooks:

- Single‑neuron dynamics with Hodgkin–Huxley:
  - `braincell_HH_neuron.ipynb` — build, stimulate, and analyze a HH neuron; inspect spikes, IV/fi curves, and parameter effects.
- Excitatory/Inhibitory spiking microcircuits:
  - `braincell_HH_EI_network.ipynb` — assemble a small HH E/I network; study balance, oscillations, and raster activity.
- Neural‑mass (mesoscopic) modeling:
  - `brainmass_jansenrit_node_simulation.ipynb` — simulate the Jansen–Rit cortical column; explore rhythms and parameter sweeps.
- Network‑level spiking state examples:
  - `brainstate_EI_spiking_network.ipynb` — configure and run a larger E/I spiking network; examine rates, spectra, and stability.
- And many more ...


Along the way you will:

- Configure models and connectivity, set simulation parameters, and run time‑stepping.
- Record and visualize results (time series, rasters, spectra) and export data.
- Perform small parameter scans and note tips for reproducibility.

## Let's get started!

```{toctree}
:maxdepth: 1

brainstate_LIF_neuron.ipynb
brainstate_EI_spiking_network.ipynb
braincell_HH_neuron.ipynb
braincell_HH_neuron-zh.ipynb
braincell_HH_EI_network.ipynb
brainmass_jansenrit_node_simulation.ipynb
braincell_HH_EI_network-zh.ipynb
brainmass_Whole_brain_neural_mass_modeling_zh.ipynb
```

