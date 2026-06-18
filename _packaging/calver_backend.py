# Copyright 2026 BrainX Ecosystem Limited. All Rights Reserved.
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
"""In-tree PEP 517 build backend that stamps a CalVer ``__version__``.

It wraps :mod:`setuptools.build_meta`. Before every build it writes
``BrainX/_version.py`` with a date-based version (``YYYY.M.D``, UTC) so the
*built artifact* carries the publish/build date as a frozen literal.

Detection rule:
  * Building from a source tree (no top-level ``PKG-INFO``) -> (re)stamp the
    current UTC date. This covers ``python -m build`` and ``pip install .``
    on a local machine and in CI.
  * Building from an unpacked sdist (``PKG-INFO`` present) -> keep the version
    already frozen into the sdist, so wheel-from-sdist stays reproducible.
"""

import datetime
import os

# Re-export the standard PEP 517 hooks (get_requires_for_*, etc.); the wrappers
# defined below shadow the ones we need to stamp first.
from setuptools.build_meta import *  # noqa: F401,F403
from setuptools import build_meta as _bm

_HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_VERSION_FILE = os.path.join(_HERE, "BrainX", "_version.py")

_TEMPLATE = '''# Auto-generated at build time by _packaging/calver_backend.py. Do not edit.
__version__ = "{version}"
__version_info__ = tuple(map(int, __version__.split(".")))
'''


def _building_from_sdist():
    # An unpacked sdist has PKG-INFO at its root; a raw source tree does not.
    return os.path.exists(os.path.join(_HERE, "PKG-INFO"))


def _ensure_version():
    if _building_from_sdist():
        return  # keep the version frozen into the sdist
    now = datetime.datetime.now(datetime.timezone.utc)
    version = f"{now.year}.{now.month}.{now.day}"
    with open(_VERSION_FILE, "w", encoding="utf-8") as fh:
        fh.write(_TEMPLATE.format(version=version))


def get_requires_for_build_sdist(config_settings=None):
    _ensure_version()
    return _bm.get_requires_for_build_sdist(config_settings)


def get_requires_for_build_wheel(config_settings=None):
    _ensure_version()
    return _bm.get_requires_for_build_wheel(config_settings)


def build_sdist(sdist_directory, config_settings=None):
    _ensure_version()
    return _bm.build_sdist(sdist_directory, config_settings)


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    _ensure_version()
    return _bm.build_wheel(wheel_directory, config_settings, metadata_directory)


def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    _ensure_version()
    return _bm.prepare_metadata_for_build_wheel(metadata_directory, config_settings)


if hasattr(_bm, "get_requires_for_build_editable"):

    def get_requires_for_build_editable(config_settings=None):
        _ensure_version()
        return _bm.get_requires_for_build_editable(config_settings)


if hasattr(_bm, "build_editable"):

    def build_editable(editable_directory, config_settings=None, metadata_directory=None):
        _ensure_version()
        return _bm.build_editable(editable_directory, config_settings, metadata_directory)


if hasattr(_bm, "prepare_metadata_for_build_editable"):

    def prepare_metadata_for_build_editable(metadata_directory, config_settings=None):
        _ensure_version()
        return _bm.prepare_metadata_for_build_editable(metadata_directory, config_settings)
