# Brain Simulation Ecosystem (BrainX)

[![PyPI version](https://img.shields.io/pypi/v/brainx)](https://pypi.org/project/brainx/)
![Read the Docs](https://img.shields.io/readthedocs/brainmodeling)
[![Continuous Integration](https://github.com/chaobrain/brain-modeling-ecosystem/actions/workflows/CI.yml/badge.svg)](https://github.com/chaobrain/brain-modeling-ecosystem/actions/workflows/CI.yml)


<p align="center">
  	<img alt="Header image of Brain Modeling Ecosystem." src="https://raw.githubusercontent.com/chaobrain/brain-modeling-ecosystem/main/docs/_static/bdp-ecosystem.png" width=50%>
</p> 

## Overview

The BrainX ecosystem provides comprehensive framework for brain simulation and modeling.
It provides tools and libraries for researchers to model, simulate, train, and analyze neural systems at different
scales.

**Core components** in this ecosystem includes:

- [BrainPy](https://github.com/brainpy/BrainPy): Modeling of point neuron-based spiking neural networks (SNNs), comes
  from Prof. Si Wu's lab at Peking University.

- [BrainUnit](https://github.com/chaobrain/brainunit): Comprehensive physical units and unit-aware mathematical system
  for brain dynamics.

- [BrainCell](https://github.com/chaobrain/braincell): Intuitive, parallel, and efficient simulation for biologically
  detailed brain cell modeling. Collaborated with Prof. Songting Li's lab at Shanghai Jiao Tong University.

- [BrainMass](https://github.com/chaobrain/brainmass): Whole-brain modeling with differentiable neural mass models.

- [BrainState](https://github.com/chaobrain/brainstate): State-based IR compilation for efficient simulation of brain
  models on CPUs, GPUs, and TPUs.

- [BrainTaichi](https://github.com/chaobrain/braintaichi): The first-generation framework for customizing event-driven
  operators based on Taichi Lang syntax.

- [BrainEvent](https://github.com/chaobrain/brainevent): Enabling event-driven computations in brain dynamics.

- [BrainTrace](https://github.com/chaobrain/brainscale): Enabling scalable online learning for brain dynamics: $O(N)$
  complexity for SNNs, and $O(N^2)$ for RNN computations.

- [BrainTools](https://github.com/chaobrain/braintools): Commonly used tools for brain dynamics programming, for example
  checkpointing.

- More components may be added in the future.

## Installation

The ecosystem can be installed with the following command:

```bash
pip install BrainX -U
```

This command installs the core package and pins specific versions of the component projects known to work together,
ensuring compatibility based on integration tests.

On CPU platforms, the following command can be used to install the ecosystem with all components:

```bash
pip install BrainX[cpu] -U
```

On GPU platforms, the following command can be used to install the ecosystem with all components:

```bash
pip install BrainX[cuda12] -U

pip install BrainX[cuda13] -U
```

On TPU platforms, the following command can be used to install the ecosystem with all components:

```bash
pip install BrainX[tpu] -U
```

For development, you might want to clone the repository and install it in editable mode:

```bash
git clone https://github.com/chaobrain/brain-modeling-ecosystem.git
cd brain-modeling-ecosystem
pip install -e .
```

## Documentation

For detailed documentation, tutorials, and examples, visit
our [Documentation Portal](https://brainmodeling.readthedocs.io).

## Contributing

We welcome contributions from the community! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more
information on how to get involved.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Citation

If you use the BrainX Ecosystem in your research, please cite it appropriately. Refer to
the [citation guide](https://brainmodeling.readthedocs.io/citation.html) on our documentation portal.

## Support

If you have questions, encounter issues, or need support, please:

* Check the [documentation](https://brainmodeling.readthedocs.io).
* Search the [existing issues](https://github.com/chaobrain/brain-modeling-ecosystem/issues).
* [Open a new issue](https://github.com/chaobrain/brain-modeling-ecosystem/issues/new/choose) if your problem is not
  addressed.
* Contact us via email: `chao.brain@qq.com`.



