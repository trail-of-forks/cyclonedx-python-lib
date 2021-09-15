# encoding: utf-8

# This file is part of CycloneDX Python Lib
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
#
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) OWASP Foundation. All Rights Reserved.

import toml

from . import BaseParser
from ..model.component import Component


class PoetryParser(BaseParser):

    def __init__(self, poetry_lock_contents: str):
        super().__init__()
        print("Starting Poetry Parser {}".format(len(self.get_components())))
        poetry_lock = toml.loads(poetry_lock_contents)

        for package in poetry_lock['package']:
            self._components.append(Component(
                name=package['name'], version=package['version'],
            ))


class PoetryFileParser(PoetryParser):

    def __init__(self, poetry_lock_filename: str):
        with open(poetry_lock_filename) as r:
            super(PoetryFileParser, self).__init__(poetry_lock_contents=r.read())
        r.close()