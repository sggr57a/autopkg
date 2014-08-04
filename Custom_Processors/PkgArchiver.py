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

__all__ = ["PkgArchiver"]


class PkgArchiver(Processor):
    '''Archive a bundle package using zip'''

    description = __doc__

    input_variables = {
        'destination_pkg': {
            'description': 'Name of destination package',
            'required': True,
        },
        'source_pkg': {
            'description': 'Path of bundle package to be zipped',
            'required': True,
        },
    }

    output_variables = {}

    def archive(self, dest_flat_pkg, source_bundle_pkg):
        try:
            subprocess.check_call(['/usr/bin/zip', '-r', dest_zip_pkg, source_bundle_pkg])
        except subprocess.CalledProcessError, err:
            raise ProcessorError("%s zipping %s" % (err, source_bundle_pkg))

    def main(self):
	dest_zip_pkg = self.env.get('destination_pkg')
        source_bundle_pkg = self.env.get('source_pkg')

        self.archive(dest_pkg, source_pkg)

        self.output("Zipped %s to %s" 
            % (source_pkg, dest_pkg))

if __name__ == '__main__':
    processor = PkgArchiver()
    processor.execute_shell()
