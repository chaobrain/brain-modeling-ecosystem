# Documentation Links

This ecosystem is a collection of tools, libraries, and frameworks that can be used to build brain dynamics models and
applications.

The brain modeling ecosystem is designed to be modular, so you can use as much or as little of it as you need.

We welcome contributions from the community, so if you have an idea for a new tool or library, please let us know!

## `BrainPy`: Legacy & Classical Framework

[**BrainPy**](https://github.com/brainpy/BrainPy) represents the first platform we created for brain dynamics
programming.

This framework offers high flexibility, allowing users to freely define brain dynamics models. It integrates tools such
as event-driven operators, differential equation solvers, and model construction interfaces, enabling users to flexibly
customize models as needed. BrainPy supports various application scenarios such as brain dynamics simulation, training,
and analysis. Within a single model, users can carry out experiments for simulation, offline learning, online learning,
or backpropagation training, or further perform low-dimensional bifurcation analysis or high-dimensional slow-point
analysis.

In terms of performance, BrainPy achieves significant improvements through object-oriented just-in-time compilation
(JIT) and specialized operators tailored for brain dynamics characteristics. However, its JIT interface and event-driven
operators have several drawbacks, so we aim to improve them in the following packages. Additionally, BrainPy has good
extensibility. New features and extensions can be easily implemented through plugin modules, allowing it to adapt to the
evolving field of brain dynamics and meet changing research needs.

## `braintaichi`: Event-Driven Computation Framework

Brain dynamics is characterized by event-driven sparse computations, which are not compatible with existing operators
for matrix multiplication.

[braintaichi](https://github.com/chaobrain/braintaichi) is designed for customizing event-driven operators in brain
dynamics. It leverages [Taichi Lang](https://www.taichi-lang.org/), a domain-specific language embedded in Python that
helps easily write high-performance parallel programs on CPUs and GPUs, and can be embedded into JAX/XLA processes.

Currently, **braintaichi** provides two levels of interface:

1. A framework for customizing event-driven brain dynamics operators.
2. Several commonly used operators, including event-driven matrix-vector
   multiplication, [just-in-time connectivity operators](https://arxiv.org/abs/2311.05106), and common sparse routines.

## `brainunit`: Physical Units

Starting from [brainunit](https://github.com/chaobrain/brainunit), we are developing a new ecosystem for brain dynamics
programming.

**brainunit** provides comprehensive physical units and a unit-aware mathematical system for brain dynamics. It is
designed to be fully compatible with JAX's transformation systems, including `jax.jit`, `jax.grad`, `jax.vmap`,
`jax.pmap`, and others.

Features:

- 2000+ commonly used physical units.
- 200+ unit-aware mathematical operations.

Since most brain dynamics models are based on physical equations, using physical units is essential to ensure
correctness.

## `braincell`: Biologically Detailed Brain Cell Modeling

[braincell](https://github.com/chaobrain/braincell) is a package for dendritic computation in our BDP ecosystem. It
provides tools for building dendritic computation models, including:

- Construction of dendritic trees
- Definition of dendritic compartments
- Implementation of various ions and channels in a neuron

**braincell** is designed for high-performance parallel dendritic modeling. Compartment and neuron computations are
fully parallelized on a single device, ensuring excellent performance.

## `brainstate`: State-based Compilation

Brain dynamics involve intrinsic, memory-intensive computations. Most operations are element-wise and benefit greatly
from JIT compilation.  
[brainstate](https://github.com/chaobrain/brainstate) is an **easy-to-use JIT transformation system** for BDP.

While JAX's JIT interface is difficult to apply directly to complex brain dynamics, **brainstate** provides a highly
intuitive, state-based transformation system for compiling BDP models. It includes:

- Gradient computation
- Control flows
- JIT compilation

**brainstate** forms the foundation for the new BDP ecosystem.

## `brainevent`: Event-Driven Algorithms for Brain Dynamics

**BrainEvent** provides data structures and algorithms for event-driven computation on **CPUs**, **GPUs**, **TPUs**, and
more, enabling efficient and biologically plausible modeling of brain dynamics.

Key classes:

- `EventArray`: Represents a vector or matrix of binary events.

Sparse matrix formats for event-driven computation:

- `COO`: Coordinate format
- `CSR`: Compressed Sparse Row
- `CSC`: Compressed Sparse Column
- `JITCHomoR`: JIT connectivity matrix with homogeneous weights
- `JITCNormalR`: JIT connectivity matrix with normal distribution weights
- `JITCUniformR`: JIT connectivity matrix with uniform distribution weights
- `FixedPreNumConn`: Fixed number of pre-synaptic connections
- `FixedPostNumConn`: Fixed number of post-synaptic connections
- and more...

## `brainscale`: Scalable Online Learning

[brainscale](https://github.com/chaobrain/brainscale) provides a scalable online learning framework for brain dynamics.

- **SNNs**: Achieves O(N) memory and computational complexity.
- **RNNs**: Achieves O(N²) complexity.

## `braintools`: Commonly Used Tools

[braintools](https://github.com/chaobrain/braintools) is a collection of tools for brain dynamics programming and
analysis.


## More details

If you want to know more about the ecosystem, please visit the following links:



```{toctree}
:maxdepth: 1

brainunit documentation <https://brainunit.readthedocs.io/>
braincell documentation <https://braincell.readthedocs.io/>
brainstate documentation <https://brainstate.readthedocs.io/>
brainevent documentation <https://brainevent.readthedocs.io/>
brainscale documentation <https://brainscale.readthedocs.io/>
brainmass documentation <https://brainmass.readthedocs.io/>
braintools documentation <https://braintools.readthedocs.io/>
brainpy documentation <https://brainpy.readthedocs.io/>
braintaichi documentation <https://braintaichi.readthedocs.io/>
```
