# Copyright 2025 BrainX Ecosystem Limited. All Rights Reserved.
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


try:
    # Generated at build time from the publish date by _packaging/calver_backend.py.
    from ._version import __version__, __version_info__
except ImportError:
    # Running from an un-built source checkout: fall back to today's date (UTC).
    import datetime as _dt

    _now = _dt.datetime.now(_dt.timezone.utc)
    __version__ = f"{_now.year}.{_now.month}.{_now.day}"
    __version_info__ = tuple(map(int, __version__.split(".")))
    del _dt, _now
