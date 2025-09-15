# Installing the stack

`BrainX` is a metapackage that can be installed with the following command:

```
pip install BrainX
```

This pins particular versions of component projects which are known to work correctly
together via the integration tests in this repository. Packages include:

- [BrainPy](https://github.com/brainpy/BrainPy)
-

## Pinned versions

The `BrainX` meta-package does periodic releases, with date-based version strings. For
example, if you'd like to pin the set of packages from September 2025, you can use this installation
command:

```
pip install BrainX==2025.9.13
```

For the full list of released versions and the pinned packages, refer to
the [Change log](https://github.com/chaobrain/brain-modeling-ecosystem/blob/main/docs/CHANGELOG.md).

## Hardware support

To install `BrainX` with hardware-specific JAX support, add the JAX installation
command in the same `pip install` invocation. For example:

```
pip install BrainX "jax[cuda]"  # JAX with GPU/CUDA support
pip install BrainX "jax[tpu]"  # JAX with TPU support
```

Or:

```
pip install BrainX[cuda12]  # with CUDA 12 support
pip install BrainX[tpu]  # with TPU support
```

For more information on available options for hardware-specific JAX installation, refer
to [JAX installation](https://docs.jax.dev/en/latest/installation.html).

