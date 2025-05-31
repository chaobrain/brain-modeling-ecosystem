# Copyright 2024 BDP Ecosystem Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

# -*- coding: utf-8 -*-

import io
import os
import re

from setuptools import find_packages, setup

# version
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'BrainX/', '__init__.py'), 'r') as f:
    init_py = f.read()
version = re.search('__version__ = "(.*)"', init_py).groups()[0]

# obtain long description from README
with io.open(os.path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
    README = f.read()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


def add_option_to_brain_dependencies(lines: list, symbol: str):
    modified_lines = []
    for line in lines:
        line = line.strip()
        # Skip empty lines
        if not line:
            continue

        # Check if line starts with "brain"
        if line.startswith('brain') or line.startswith('jax'):
            # Find where the version specification starts
            for i, char in enumerate(line):
                if char in ['>', '<', '=', '~', '!']:
                    # Add [cuda12] before version specifiers
                    modified_line = f"{line[:i]}[{symbol}]{line[i:]}"
                    modified_lines.append(modified_line)
                    break
            else:
                # If no version specifier is found, just append [cuda12]
                modified_lines.append(f"{line}[{symbol}]")
        else:
            modified_lines.append(line)

    return modified_lines


cpu_requirements = add_option_to_brain_dependencies(requirements, 'cpu')
gpu_requirements = add_option_to_brain_dependencies(requirements, 'cuda12')
tpu_requirements = add_option_to_brain_dependencies(requirements, 'tpu')

# installation packages
packages = find_packages(
    exclude=[
        "docs*",
        "tests*",
        "examples*",
        "benchmark*",
        "experiments*",
        "build*",
        "dist*",
        "BrainX.egg-info*",
        "BrainX/__pycache__*",
        "BrainX/__init__.py"
    ]
)

# setup
setup(
    name='BrainX',
    version=version,
    description='Ecosystem for Brain Modeling.',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Brain Modeling Ecosystem Developers',
    author_email='chao.brain@qq.com',
    packages=packages,
    python_requires='>=3.10',
    install_requires=requirements,
    url='https://github.com/chaobrain/brain-modeling-ecosystem',
    project_urls={
        "Bug Tracker": "https://github.com/chaobrain/brain-modeling-ecosystem/issues",
        "Documentation": "https://brainmodeling.readthedocs.io/",
        "Source Code": "https://github.com/chaobrain/brain-modeling-ecosystem",
    },
    extras_require={
        'cpu': cpu_requirements,
        'cuda12': gpu_requirements,
        'gpu': gpu_requirements,
        'tpu': tpu_requirements,
    },
    keywords=(
        'computational neuroscience, '
        'brain-inspired computation, '
        'brain dynamics programming'
    ),
    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries',
    ],
    license='Apache-2.0 license',
)
