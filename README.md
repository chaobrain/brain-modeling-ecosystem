# Ecosystem for Brain Modeling 

[![PyPI version](https://img.shields.io/pypi/v/brainmodeling)](https://pypi.org/project/brainmodeling/)
![Read the Docs](https://img.shields.io/readthedocs/brainmodeling)
[![Continuous Integration](https://github.com/chaobrain/brain-modeling-ecosystem/actions/workflows/CI.yml/badge.svg)](https://github.com/chaobrain/brain-modeling-ecosystem/actions/workflows/CI.yml)


<p align="center">
  	<img alt="Header image of Brain Modeling Ecosystem." src="https://raw.githubusercontent.com/chaobrain/brain-modeling-ecosystem/main/docs/_static/bdp-ecosystem.png" width=50%>
</p> 


## Overview

Ecosystem for Brain Modeling provides comprehensive framework for computational neuroscience and brain simulation. 
It provides tools and libraries for researchers to model, simulate, train, and analyze neural systems at different scales.

**Core components** in this ecosystem includes:

- [BrainUnit](https://github.com/chaobrain/brainunit): Comprehensive physical units and unit-aware mathematical system for brain dynamics.

- [BrainCell](https://github.com/chaobrain/braincell): Intuitive, parallel, and efficient simulation for biologically detailed brain cell modeling. 

- [BrainState](https://github.com/chaobrain/brainstate): State-based IR compilation for efficient simulation of brain models on CPUs, GPUs, and TPUs.

- [BrainTaichi](https://github.com/chaobrain/braintaichi): The first-generation framework for customizing event-driven operators based on Taichi Lang syntax.

- [BrainEvent](https://github.com/chaobrain/brainevent): Enabling event-driven computations in brain dynamics. 

- [BrainScale](https://github.com/chaobrain/brainscale): Enabling scalable online learning for brain dynamics: $O(N)$ complexity for SNNs, and $O(N^2)$ for RNN computations.

- [BrainTools](https://github.com/chaobrain/braintools): Commonly used tools for brain dynamics programming, for example checkpointing. 


## Installation

The ecosystem can be installed with the following command:

```bash
pip install brainmodeling
```

This pins particular versions of component projects which are known to work correctly together via the integration tests in this repository. 




## Quick Start

```python
import braintools
import brainstate
import brainunit as u


class EINet(brainstate.nn.Module):
    def __init__(self):
        super().__init__()
        self.n_exc = 3200
        self.n_inh = 800
        self.num = self.n_exc + self.n_inh
        self.N = brainstate.nn.LIFRef(
            self.num, V_rest=-60. * u.mV, V_th=-50. * u.mV, V_reset=-60. * u.mV,
            tau=20. * u.ms, tau_ref=5. * u.ms,
            V_initializer=brainstate.init.Normal(-55., 2., unit=u.mV)
        )
        self.E = brainstate.nn.AlignPostProj(
            comm=brainstate.nn.EventFixedProb(self.n_exc, self.num, 0.02, 0.6 * u.mS),
            syn=brainstate.nn.Expon.desc(self.num, tau=5. * u.ms),
            out=brainstate.nn.COBA.desc(E=0. * u.mV),
            post=self.N
        )
        self.I = brainstate.nn.AlignPostProj(
            comm=brainstate.nn.EventFixedProb(self.n_inh, self.num, 0.02, 6.7 * u.mS),
            syn=brainstate.nn.Expon.desc(self.num, tau=10. * u.ms),
            out=brainstate.nn.COBA.desc(E=-80. * u.mV),
            post=self.N
        )

    def update(self, t, inp):
        with brainstate.environ.context(t=t):
            spk = self.N.get_spike() != 0.
            self.E(spk[:self.n_exc])
            self.I(spk[self.n_exc:])
            self.N(inp)
            return self.N.get_spike()
    
    def save_checkpoint(self):
        braintools.file.msgpack_save('states.msgpack', self.states())

```

## Documentation

For detailed documentation, tutorials, and examples, visit our [Documentation Portal](https://brainmodeling.readthedocs.io).


## Contributing

We welcome contributions from the community! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more information on how to get involved.


## License

This project is licensed under the [Apache License v2.0](LICENSE).

## Citation

If you use the Brain Modeling Ecosystem in your research, please use the following link: https://brainmodeling.readthedocs.io/citation.html


## Support

For questions and support, please [open an issue](https://github.com/chaobrain/brain-modeling-ecosystem/issues) or email to us: chao.brain@qq.com



