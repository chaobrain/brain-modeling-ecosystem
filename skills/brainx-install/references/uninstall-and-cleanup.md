# BrainX Uninstall and Cleanup

Use this reference to remove BrainX from one confirmed Python environment while keeping the environment and shared dependencies. Follow this workflow instead of the installation workflow.

## Scope

The BrainX removal list includes the current ecosystem and packages bundled by historical BrainX releases:

```text
BrainX
brainunit
brainstate
brainpy
brainpy-state
brainevent
braincell
braintrace
brainscale
brainmass
braintools
pinnx
```

The optional JAX removal list contains only these JAX runtime and accelerator-plugin distributions:

```text
jax
jaxlib
jax-cuda12-plugin
jax-cuda12-pjrt
jax-cuda13-plugin
jax-cuda13-pjrt
libtpu
libtpu-nightly
```

Treat distribution names case-insensitively and normalize `.`, `_`, and `-` as equivalent when comparing installed metadata. For example, the `brainpy-state` distribution may appear in requirement metadata as `brainpy.state` or `brainpy_state`.

Do not automatically remove packages merely because BrainX or JAX depends on them. Preserve `saiunit`, NumPy, Optax, Matplotlib, Msgpack, SciPy, ML Dtypes, Opt Einsum, NVIDIA runtime wheels, CUDA drivers and toolkits, and all other shared dependencies. Also preserve the virtual environment, source checkouts, caches, datasets, lockfiles, manifests, and this agent skill.

## Core Rules

1. Operate on only one Python environment at a time: identify its exact path, verify that it is a virtual environment or non-base Conda environment rather than a global interpreter, and obtain the user's confirmation before uninstalling anything.
2. Run every pip command through that environment's exact Python executable, for example `"<venv>/bin/python" -m pip`; do not rely on shell activation or use a bare `python` or `pip`, because those commands may target a different environment.
3. Inspect first and include only distributions proven local to the confirmed virtual environment in the proposed uninstall commands.
4. Ask explicitly whether JAX cleanup is included. Installed JAX packages or accelerator hardware are evidence, not consent.
5. Before any mutation, present the complete uninstall specification in this reference and obtain explicit confirmation of the environment, exact package lists, and expected final state.
6. If the environment or proposed scope changes, discard the earlier confirmation, present a corrected specification, and ask again.
7. Never delete an environment, use `--break-system-packages`, invoke an automatic orphan remover, modify dependency files, or expand the package set without approval.

## Workflow

Follow this order without skipping the confirmation gate:

```text
read-only environment inspection
-> installed-target and reverse-dependency inventory
-> explicit JAX cleanup choice
-> complete uninstall specification
-> explicit user confirmation
-> BrainX uninstall
-> optional JAX uninstall
-> metadata and pip-check verification
-> final report
```

## 1. Inspect One Environment

Record the intended run location and identify the exact environment before inspecting packages. Confirm:

- the exact Python executable and version;
- the virtual-environment or Conda-environment path and environment manager;
- evidence that the interpreter is not global and not the Conda base environment;
- the pip version associated with that interpreter;
- installed names and versions from both package lists above;
- the environment's existing `pip check` result;
- remaining installed packages that declare a proposed removal target as a requirement.

Prefer distribution metadata over imports. Use the exact interpreter for read-only inspection:

```bash
"<exact-python>" -m pip list --format=json
"<exact-python>" -m pip check
```

The placeholder is illustrative. Replace it with the platform-appropriate exact interpreter path. Use `importlib.metadata` or another read-only metadata method to inspect declared requirements and find reverse dependencies. Classify each target before planning removal:

- **Local to venv:** its package location is under the virtual environment's `site-packages`; it is eligible for uninstall.
- **Visible from external Python:** it is exposed through `--system-site-packages` or another external path; preserve it.
- **Global interpreter:** `sys.prefix == sys.base_prefix`; stop and do not uninstall.

Only the first case may enter the uninstall specification. If the user asks to uninstall a package visible from external Python or from a global interpreter, explicitly warn that this would modify an external or shared Python environment and stop without uninstalling it. Do not import target packages, upgrade pip, or install a helper merely to inspect the environment.

Evaluate reverse dependencies against the final proposed scope. Ignore requirements from distributions that are themselves being removed, but list every remaining distribution that requires a planned BrainX or JAX target. Do not automatically add those dependents to the uninstall command. If the target environment cannot be proven non-global, stop and request a virtual or Conda environment instead.

## 2. Confirm Optional JAX Cleanup

Ask the user to choose explicitly between:

- removing installed BrainX targets while preserving all JAX distributions; or
- removing installed BrainX targets and the installed distributions in the optional JAX universe.

Do not infer the choice from a CPU, CUDA, or TPU installation. Explain that pip does not record reliable ownership provenance, so removing JAX can affect unrelated software in the same environment.

If no BrainX target is installed, report that fact. Do not mutate the environment unless the user separately opts into removing installed JAX targets and confirms the resulting specification.

## 3. Present the Complete Specification

Before any uninstall command, show this structure with concrete values:

```text
Confirming the uninstall:

Python environment
- Run location:
- Exact Python executable:
- Python version:
- Virtual-environment path:
- Environment manager:

Current package state
- Non-target packages that depend on removal targets:
- Existing package-integrity issues:

Uninstall scope
- Exact BrainX distributions to remove:
- Optional JAX removal: included or excluded
- Exact JAX distributions to remove:
- Packages and resources explicitly preserved:

Planned changes
- Expected final package state:

Please confirm the entire uninstall specification.
```

Under each exact removal field, list one installed distribution per line as `name==version`. Write `none` when a removal list, reverse-dependency list, or integrity-issue list is empty. The BrainX field may contain only installed packages from the BrainX removal list. The JAX field may contain only installed packages from the optional JAX removal list and must be `none` when optional JAX removal is excluded. The expected final state must say that the listed BrainX packages will be absent, whether JAX will be removed or preserved, and that the confirmed environment and shared dependencies will remain.

A prior general request to uninstall BrainX is not confirmation of this environment-specific specification. Do not mutate anything until the user explicitly confirms the complete, unchanged specification.

If any non-target package depends on a planned removal target, explain that the remaining package may be broken after cleanup and require explicit confirmation with that risk visible. Do not silently uninstall, repair, or reinstall the dependent package.

## 4. Execute the Confirmed Uninstall

When the confirmed BrainX field is not `none`, build its command from that exact list and run it with the confirmed interpreter. The command shape is:

```bash
"<exact-python>" -m pip uninstall -y <installed-brainx-targets-only>
```

When optional JAX cleanup was confirmed and its exact list is not `none`, build its command from that list. Run it after the BrainX command succeeds, or run it directly when the BrainX field is `none`:

```bash
"<exact-python>" -m pip uninstall -y <installed-jax-targets-only>
```

Before execution, ensure each command contains exactly the names in its confirmed list. If a list or command would change, present a corrected specification and obtain new confirmation. Do not run an empty command, add an absent package, invoke `pip-autoremove`, delete site-packages entries manually, remove NVIDIA or system accelerator software, or delete the environment.

If either command fails, stop further mutation, record its exit status and relevant output, and re-inventory both removal lists. Pip uninstalls are not atomic, so report the packages successfully removed and the packages still present rather than assuming rollback.

## 5. Verify

Using the same exact interpreter:

1. Re-read installed distribution metadata for both removal lists.
2. Confirm every distribution in the approved uninstall commands is absent.
3. Confirm preserved candidates were not added to or removed from the approved scope.
4. Run `"<exact-python>" -m pip check` and compare its result with the pre-uninstall baseline.

Do not verify removal by importing the removed packages. Metadata absence is the authority. Report `PASS` only when every approved target is absent. Report `FAIL` if a command failed or any approved target remains. Always report new, unchanged, or resolved `pip check` issues separately; a user-approved broken reverse dependency does not count as a remaining uninstall target, but it must remain visible in the result.

## 6. Report

Report:

- run location, exact interpreter, and environment path;
- BrainX packages removed, with their former versions;
- whether JAX cleanup was excluded or the JAX packages removed;
- packages requested but already absent;
- preserved packages and resources;
- uninstall commands and exit statuses;
- verification results and the before/after `pip check` comparison;
- remaining BrainX or approved JAX targets, if any;
- final status: `PASS` or `FAIL`, with the reason.

For a no-op, state that no approved target was installed and no mutation occurred. Do not claim that shared dependencies are unused or safe to remove merely because the BrainX targets are gone.
