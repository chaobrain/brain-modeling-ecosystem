# BrainX Package Version Matrix

This reference records the package versions explicitly declared by each BrainX release.

## How to read this table

* `—` means the package or dependency was **not explicitly listed** in that release. It does not prove that the package was unsupported or unavailable.
* **Removed** means the release explicitly removed the package from the default BrainX bundle.
* **Not bundled** means the package remained outside the default bundle after its removal.
* **BrainTrace** replaced **BrainScale** beginning with `v2025.12.2`.
* Optax may have been installed transitively in earlier releases, but `v2026.7.9` was the first release to declare `optax>=0.2.8` explicitly.

## Version compatibility matrix

| BrainX release           | JAX                 | BrainUnit | BrainState | BrainEvent | BrainTools | BrainTrace / BrainScale | BrainCell | BrainPy | BrainPy-State | BrainMass | PINNx           | Optax     |
| ------------------------ | ------------------- | --------- | ---------- | ---------- | ---------- | ----------------------- | --------- | ------- | ------------- | --------- | --------------- | --------- |
| `v2026.7.9`              | `>=0.8.0, <=0.10.2` | `0.5.1`   | `0.5.2`    | `0.1.2`    | `0.3.0`    | BrainTrace `0.2.4`      | `0.1.0`   | `2.8.1` | `0.1.0`       | `0.1.1`   | **Not bundled** | `>=0.2.8` |
| `v2026.6.29`             | `>=0.8.0, <=0.10.2` | `0.5.1`   | `0.5.2`    | `0.1.1`    | `0.3.0`    | BrainTrace `0.2.2`      | `0.1.0`   | `2.8.0` | `0.1.0`       | `0.1.1`   | **Removed**     | —         |
| `v2026.6.19`             | `>=0.8.0, <=0.10.2` | `0.5.1`   | `0.5.1`    | `0.1.1`    | `0.3.0`    | BrainTrace `0.2.1`      | `0.1.0`   | `2.8.0` | `0.1.0`       | `0.1.1`   | `0.0.3`         | —         |
| `v2026.6.18`             | —                   | `0.4.0`   | `0.5.0`    | `0.1.0`    | `0.1.10`   | BrainTrace `0.2.0`      | `0.0.8`   | `2.7.8` | `0.1.0`       | `0.0.5`   | `0.0.3`         | —         |
| `v2026.6.14`             | —                   | `0.4.0`   | `0.5.0`    | `0.1.0`    | `0.1.10`   | BrainTrace `0.2.0`      | `0.0.8`   | `2.7.8` | `0.0.4`       | `0.0.5`   | `0.0.3`         | —         |
| `v2026.6.11`             | —                   | `0.4.0`   | `0.4.2`    | `0.1.0`    | `0.1.10`   | BrainTrace `0.2.0`      | `0.0.8`   | `2.7.8` | `0.0.4`       | `0.0.5`   | `0.0.3`         | —         |
| `v2026.6.8`              | `>=0.6.0, <=0.10.1` | `0.3.2`   | `0.4.0`    | `0.1.0`    | `0.1.9`    | BrainTrace `0.2.0`      | `0.0.8`   | `2.7.8` | `0.0.4`       | `0.0.5`   | `0.0.3`         | —         |
| `v2026.3.12`             | `>=0.6.0, <=0.9.1`  | `0.2.0`   | `0.3.0`    | `0.0.7`    | `0.1.8`    | BrainTrace `0.1.2`      | `0.0.8`   | `2.7.7` | `0.0.4`       | `0.0.5`   | `0.0.3`         | —         |
| `v2026.1.31`             | `>=0.6.0, <0.9.0`   | `0.1.4`   | `0.2.10`   | `0.0.5`    | `0.1.8`    | BrainTrace `0.1.2`      | `0.0.7`   | `2.7.6` | `0.0.3`       | `0.0.5`   | `0.0.3`         | —         |
| `v2026.1.22`             | `>=0.6.0`           | `0.1.3`   | `0.2.9`    | `0.0.5`    | `0.1.8`    | BrainTrace `0.1.2`      | `0.0.7`   | `2.7.6` | `0.0.3`       | `0.0.5`   | `0.0.3`         | —         |
| `v2026.1.21`             | `>=0.6.0`           | `0.1.3`   | `0.2.9`    | `0.0.5`    | `0.1.7`    | BrainTrace `0.1.2`      | `0.0.7`   | `2.7.6` | `0.0.3`       | `0.0.5`   | `0.0.3`         | —         |
| `v2026.1.19`             | `>=0.6.0`           | `0.1.3`   | `0.2.9`    | `0.0.5`    | `0.1.7`    | BrainTrace `0.1.2`      | `0.0.7`   | `2.7.5` | `0.0.3`       | `0.0.5`   | `0.0.3`         | —         |
| `v2026.1.16`             | `>=0.6.0`           | `0.1.3`   | `0.2.9`    | `0.0.5`    | `0.1.7`    | BrainTrace `0.1.2`      | `0.0.6`   | `2.7.5` | `0.0.2`       | `0.0.4`   | `0.0.3`         | —         |
| `v2025.12.26`            | `>=0.6.0`           | `0.1.3`   | `0.2.8`    | `0.0.5`    | `0.1.6`    | BrainTrace `0.1.2`      | `0.0.6`   | `2.7.5` | `0.0.2`       | `0.0.4`   | `0.0.3`         | —         |
| `v2025.12.25`            | `>=0.6.0`           | `0.1.3`   | `0.2.8`    | `0.0.5`    | `0.1.6`    | BrainTrace `0.1.2`      | `0.0.6`   | —       | `0.0.1`       | `0.0.4`   | `0.0.3`         | —         |
| `v2025.12.2`             | `>=0.6.0`           | `0.1.2`   | `0.2.6`    | `0.0.4`    | `0.1.4`    | BrainTrace `0.1.1`      | `0.0.6`   | `2.7.2` | —             | `0.0.4`   | `0.0.3`         | —         |
| `v2025.10.13`            | `>=0.6.0, <0.8.0`   | `0.1.1`   | `0.2.3`    | `0.0.4`    | `0.1.3`    | BrainScale `0.1.0`      | `0.0.6`   | `2.7.1` | —             | `0.0.4`   | —               | —         |
| `v2025.9.15`             | `>=0.4.35, <0.8.0`  | `0.1.1`   | `0.1.10`   | `0.0.4`    | `0.0.11`   | BrainScale `0.0.10`     | `0.0.4`   | —       | —             | `0.0.3`   | —               | —         |

## Installation rule

Treat each row as one declared BrainX package set.

Do not independently combine the newest release of every subpackage. Choose a BrainX release and use the package versions declared for that release.

A `—` entry must not be converted into an assumption. Before installing an unlisted dependency, inspect the selected BrainX release metadata or dependency files.
