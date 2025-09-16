# Installing the ecosystem

BrainX is a meta-package that installs a curated set of BrainX components known to work well together.

## Requirements

- Python 3.10-3.13
- pip 23+ (`python -m pip install --upgrade pip`)
- Optional: GPU/TPU drivers and libraries if you plan to use accelerators

## Quick install

```bash
pip install -U BrainX
```

This installs pinned versions of the core packages:

- [brainunit](https://github.com/chaobrain/brainunit)
- [brainstate](https://github.com/chaobrain/brainstate)
- [brainevent](https://github.com/chaobrain/brainevent)
- [braincell](https://github.com/chaobrain/braincell)
- [brainscale](https://github.com/chaobrain/brainscale)
- [brainmass](https://github.com/chaobrain/brainmass)
- [braintools](https://github.com/chaobrain/braintools)
- [jax](https://github.com/jax-ml/jax) 
- and common utilities (numpy, msgpack, matplotlib)

## Hardware-specific installs

Choose one that matches your platform and CUDA/toolchain:

```bash
# CPU only
pip install -U BrainX[cpu]

# NVIDIA GPU (CUDA 12.x)
pip install -U BrainX[cuda12]

# TPU
pip install -U BrainX[tpu]
```


For detailed JAX wheel options and compatible CUDA/cuDNN versions,
see [JAX installation](https://docs.jax.dev/en/latest/installation.html).





## Pin a specific BrainX release

Releases use date-style versions. Example:

```bash
pip install BrainX==2025.9.15
```

See the change log for the exact component versions: [docs/CHANGELOG.md](./CHANGELOG.md)

## From source (development)

```bash
git clone https://github.com/chaobrain/brain-modeling-ecosystem.git
cd brain-modeling-ecosystem
python -m pip install -e .
```

Optional docs deps: `python -m pip install -r docs/requirements.txt`

## Verify your installation

```bash
python -c "import BrainX, jax; print('BrainX OK'); print('JAX devices:', jax.devices())"
```

If using a GPU, you should see a CUDA device listed.

## Troubleshooting

- Upgrade pip/setuptools/wheel: `python -m pip install -U pip setuptools wheel`
- On GPU, ensure the installed JAX wheel matches your CUDA toolkit version
- If import fails, try a clean env: `python -m venv .venv && .venv\\Scripts\\activate && pip install -U BrainX`