---
name: brainx-install
description: Install, uninstall, or configure BrainX, change its package version or device target, and resolve BrainX ecosystem compatibility. Use whenever a user asks to install, set up, upgrade, downgrade, pin, migrate, remove, uninstall, clean up, or reconcile BrainX packages; switch or select CPU, CUDA 12, CUDA 13, or TPU support. Do not use for general BrainX modeling.
---

# BrainX Install

## Objective

Install or remove BrainX in one confirmed Python virtual environment, verify, then report the result. For installation, treat each published BrainX release as an indivisible compatibility set; never assemble independently selected subpackage versions.

## Request Routing

For an uninstall, removal, or BrainX package-cleanup request, open [references/uninstall-and-cleanup.md](references/uninstall-and-cleanup.md) and stop here. Follow that reference in full; do not apply the installation workflow's device or release selection.

For installation, upgrade, downgrade, migration, device-target, or compatibility requests, continue with the workflow below.

## Core Rules

1. BrainX package must use a Python interpreter at version `>=3.11`.
2. For a clean environment with no requested version, prefer to use the unpinned BrainX install matching the confirmed device, but resolve and name the current latest Python-compatible BrainX date-style release before confirmation. Critically, if a BrainX component already exists in the environment, or a requested version is specified, you must open [compatibility-and-release-matching.md](references/compatibility-and-release-matching.md), use it as the primary release source, and select one non-separated release. Never mix component versions from different rows.
3. Require the user to explicitly choose `cpu`, `cuda12`, `cuda13`, or `tpu`. Detection is evidence, not consent.
4. Before any mutation, must present the complete specification to the user clearly, show the run location, interpreter, venv path, device extra, release, complete component set, existing packages, expected results, and exact commands.
5. Create or modify nothing until the user confirms that complete specification.
6. After confirmation, install only the selected BrainX meta-package release. Do not install ecosystem components individually.

## Workflow

Follow this order without skipping the confirmation gate:

```text
read-only inspection
-> explicit device choice
-> coherent release selection
-> complete installation specification
-> explicit user confirmation
-> venv creation or reuse
-> pip 23+ upgrade
-> one confirmed BrainX install
-> BrainX/JAX import and device verification
-> final report
```

## 1. Read-Only Inspection

Record the intended run location first. Perform no package installation, or environment creation during inspection.

Choose read-only inspection methods that fit the operating system.

Collect enough evidence to identify:

- OS, version, architecture, and CPU;
- visible NVIDIA or TPU hardware and the driver, toolkit, container, or runtime evidence needed to distinguish `cuda12`, `cuda13`, and `tpu`;
- the active Python executable and version, environment-manager state, pip version, and viable candidate interpreters;
- existing `.venv`, `.venv-brainx`, or user-designated target environments without creating or activating them;
- installed versions of BrainX, BrainUnit, BrainState, BrainEvent, BrainTools, BrainTrace or BrainScale, BrainCell, BrainPy, BrainPy-State, BrainMass, PINNx, JAX, JAXlib, and Optax in every environment relevant to the request;
- for a clean unpinned install, the exact latest BrainX release compatible with the proposed interpreter, resolved from read-only official package-index metadata.

Prefer package metadata and platform-native tools over imports or newly installed helpers. Record missing evidence explicitly as `unknown`, `not_detected`, or a command error rather than guessing. Organize the result in whatever concise structured form best fits the task.

## 2. Confirm the Device Target

Determine whether the intended installation is for:

- `cpu`
- `cuda12`
- `cuda13`
- `tpu`

Do not treat detected hardware as the user's choice. If the target is unstated, implied, contradictory, or unclear, question the user directly and persistently until they explicitly choose one device target. Resolve whether they mean the current machine, a container, a remote host, a cluster node, or another deployment environment. Never infer CUDA 12 or CUDA 13 from GPU visibility alone; consider the NVIDIA driver, toolkit or container runtime, and the intended execution host.

Reflect the understood requirement back to the user before release selection. Use wording such as:

> Understanding your need: you want to install BrainX for **NVIDIA CUDA 12** on **the target environment you identified**, using the `cuda12` extra. Is that correct?

Replace the example values with the user's actual target. If evidence is uncertain, explain the ambiguity and ask a focused question instead of filling in a likely answer. Recommend `cpu` when accelerator support is absent or uncertain, but still require explicit confirmation. Do not proceed until the user confirms or corrects the reflected device target.

## 3. Select One Release

First case, When no BrainX meta-package or ecosystem component is installed and the user has not requested a specific version, do not open the compatibility reference. Use read-only official package-index metadata with the proposed interpreter to identify the exact latest Python-compatible BrainX release, then report it in the form `latest (vYYYY.M.D)`. For example, report `latest (v2026.7.9)` when `2026.7.9` is the verified current release. 

Critically, for the second case, when BrainX packages are already installed or the user requests a specific pinned version, you must open [compatibility-and-release-matching.md](references/compatibility-and-release-matching.md) before selecting a release, then apply the matching procedure below.

- With one exact component match, choose the newest row containing that exact version.
- When one BrainX ecosystem component is installed and its version does not appear in any compatibility matrix row, compare it with the versions declared for that same component across all rows. Choose the BrainX release containing the closest semantic version, favor the newer BrainX release if two rows are equally close, propose installing that entire BrainX release rather than the component alone, and disclose the component version change.
- With multiple installed components that do not identify one coherent row, show the competing candidate rows and require the user to choose. Do not construct a compromise tuple.
- Treat an installed `BrainX` meta-package version as the release anchor, but surface any component drift from its row.
- Do not use JAX or Optax alone as a legacy release anchor unless the user explicitly asks to preserve it.

## 4. Choose the Venv

Prefer reusing an existing relevant Python virtual environment whose interpreter is Python `>=3.11`. This includes environments managed by `venv`, Conda, or another environment manager; inspect the environment before proposing reuse.

- If no suitable existing environment is available, propose creating a fresh virtual environment.
- Never delete, rebuild, overwrite, or silently repurpose an existing environment.
- Never install into the global interpreter or an unrelated environment.

Resolve the exact interpreter inside the proposed environment using the conventions of the confirmed platform and environment manager. Do not rely on shell activation or assume that a bare `python` or `pip` command targets the intended environment.

## 5. Present the Complete Specification

The agent must report the complete proposed setup before any mutation. This is a mandatory reporting contract, not a rigid implementation script. Use concrete values and preserve the following visible structure:

```text
Confirming the setup:

Python environment
- Run location:
- Python version:
- Virtual-environment path:
- Environment action: create or reuse

Device target
- Intended execution environment:
- Detected hardware evidence:
- User-confirmed target: CPU, NVIDIA CUDA 12, NVIDIA CUDA 13, or TPU
- Selected BrainX extra: cpu, cuda12, cuda13, or tpu

BrainX target package state
- Current BrainX ecosystem packages and versions:
- Target BrainX release: latest or selected, with the explicit date-style release (`vYYYY.M.D`)
- Expected final package set after installation, using exact pins or declared constraints

Planned changes
- Packages that will be installed, upgraded, or downgraded:
- Exact commands that will run:
Please confirm the entire setup or correct it.
```

For an existing-package or pinned-version workflow, list the BrainX meta-package and every component declared by the selected compatibility row under `Expected final package set`, using the exact target version or constraint. For a clean unpinned install, name the device-specific meta-package and verified release explicitly under `Target BrainX release` and `Expected final package set`, for example `BrainX[cpu]: latest (v2026.7.9)`.

End by asking the user to confirm the entire setup or correct it, and state explicitly that no environment will be created or modified before confirmation.

Do not combine specification and installation in one turn unless the user has already confirmed this exact environment, release, and device extra.

## 6. Install and Verify

Use exactly the confirmed venv, interpreter, device extra, and unpinned or pinned release method.

1. Create or reuse the confirmed venv.
2. Upgrade pip to version 23 or newer.
3. Install the BrainX meta-package. Never install BrainX components separately.

If any confirmed choice must change, stop, present a corrected specification, and obtain new approval.

If pip fails, stop and skip verification. Leave the failed environment intact for diagnosis.

After pip succeeds, verify the installation with this simple command:

```bash
python -c "import BrainX, jax; print('BrainX OK'); print('JAX devices:', jax.devices())"
```

Run it through the exact confirmed venv interpreter; the bare `python` spelling is illustrative.

Verification passes only when:

- both `BrainX` and `jax` import successfully;
- the command prints `BrainX OK`;
- `jax.devices()` reports the user-confirmed backend: CPU for `cpu`, a CUDA device for `cuda12` or `cuda13`, or a TPU device for `tpu`.

Do not modify manifests, lockfiles, requirements files, or unrelated environments.

## 7. Report

Report:

- environment path;
- resolved BrainX release and device extra;
- pip command and result;
- verification command output;
- final status: `PASS` or `FAIL`, with the reason.

For a pip failure, include the exit status and relevant stderr and state that verification was not run. For a verification failure, identify the failed condition. Report `PASS` only when both imports succeed and JAX sees the confirmed backend.

## Official Commands to use

Use these official BrainX documentation examples to understand the supported syntax. They are educational patterns, not a rigid workflow or permission to bypass the confirmed interpreter, venv, release behavior, or device choice.

### Quick Install and Dependency Resolution

When no BrainX meta-package or ecosystem component is already installed, prefer the official unpinned quick-install family:

```bash
pip install -U BrainX
```

For a new BrainX environment when user has no existing brainX packages, the bare command and the unpinned `BrainX[cpu]`, `BrainX[cuda12]`, `BrainX[cuda13]`, and `BrainX[tpu]` commands are equally default; choose the one matching the user-confirmed device target. These are the cleanest installation methods because they let pip choose the latest BrainX release compatible with the confirmed Python version and resolve only the dependency changes that release requires. Use an exact release pin only when the user has existing brainX packages, or requests a specific release, reproducibility, or compatibility with an existing BrainX environment.

| Command | BrainX itself | Dependencies |
|---|---|---|
| `pip install -U BrainX` | Replaced with the latest Python-compatible BrainX version if a different version is installed | Replaced only when needed to satisfy that BrainX release's constraints |
| `pip install -U 'BrainX[cuda12]'` | Same as above | Same, plus CUDA 12 JAX dependencies |
| `pip install 'BrainX==2025.9.15'` | Upgraded or downgraded to exactly `2025.9.15` if another version is installed | Replaced only when their installed versions do not satisfy `2025.9.15`'s requirements |

### Hardware-Specific Installs

For a clean environment, each unpinned command below is the default for its corresponding confirmed target. Choose the extra that matches the platform and CUDA toolchain:

```bash
# CPU only
pip install -U BrainX[cpu]

# NVIDIA GPU (CUDA 12.x)
pip install -U BrainX[cuda12]

# NVIDIA GPU (CUDA 13.x)
pip install -U BrainX[cuda13]

# TPU
pip install -U BrainX[tpu]
```

### Pin a Specific BrainX Release

BrainX releases use date-style versions:

```bash
pip install BrainX==2025.9.15
```

When an exact release is requested, preserve the confirmed hardware extra while applying the selected BrainX release pin.

## Reference Routing

Open [references/uninstall-and-cleanup.md](references/uninstall-and-cleanup.md) for any request to uninstall, remove, or clean up BrainX packages. Use its exact package scopes and mandatory uninstall specification; do not use the compatibility matrix to narrow the cleanup set.

Open [references/compatibility-and-release-matching.md](references/compatibility-and-release-matching.md) when the target environment already contains BrainX or BrainX ecosystem packages, or when the user requests a specific pinned BrainX version. This reference is mandatory for that second case and must be read before release selection. Use its matrix to match existing packages, reconcile version drift, evaluate pinned-version compatibility, and select one coherent BrainX release with its declared component versions.

Do not open this reference for a clean installation when no BrainX packages are present and no specific version is requested; use the unpinned quick-install path instead.
