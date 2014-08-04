#!/usr/bin/env python
#
# Copyright 2014 John McLaughlin
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


import os
import shutil
import subprocess

from autopkglib import Processor, ProcessorError

__all__ = ["FlatPkgPacker"]


class FlatPkgPacker(Processor):
    '''Flatten a bundle package using xar'''

    description = __doc__

    input_variables = {
        'destination_pkg': {
            'description': 'Name of destination flat package',
            'required': True,
        },
        'source_pkg': {
            'description': 'Path of bundle package to be flattened',
            'required': True,
        },
    }

    output_variables = {}

    def flatten(self, dest_flat_pkg, source_bundle_pkg):
        try:
            subprocess.check_call(['/usr/bin/xar', '-c', 'f', dest_flat_pkg, source_bundle_pkg])
        except subprocess.CalledProcessError, err:
            raise ProcessorError("%s flattening %s" % (err, source_bundle_pkg))

    def main(self):
	dest_flat_pkg = self.env.get('destination_pkg')
        source_bundle_pkg = self.env.get('source_pkg')

        self.flatten(dest_pkg, source_pkg)

        self.output("Flattened %s to %s" 
            % (source_pkg, dest_pkg))

if __name__ == '__main__':
    processor = FlatPkgCreator()
    processor.execute_shell()
