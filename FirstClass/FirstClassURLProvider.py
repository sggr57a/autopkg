#!/usr/bin/env python
#
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


import re
import urllib2
from autopkglib import Processor, ProcessorError


__all__ = ["FirstClassURLProvider"]

update_url = ("http://www.firstclass.com/Resources/MacDownload")


class FirstClassURLProvider(Processor):
    description = "Provides URL to the latest FirstClass release."
    input_variables = {
        "url": {
            "required": False,
            "description": ("Override URL. If provided, this processor "
                "just returns without doing anything."),
        },
    }
    output_variables = {
        "url": {
            "description": "URL to the latest FirstClass release.",
        },
    }
    
    __doc__ = description
    

    def get_fc_url(self):
	'''Read in URL'''
	try:
	    f = urllib2.urlopen(update_url)
	    url_data = f.read()
	    f.close()
	except BaseException as e:
            raise ProcessorError(
                "Can't download %s: %s" % (update_url, e))	

	'''Find installer in URL'''
	for tag in re.findall(r'(?:http://|www.).*?["]*dmg|pkg', url_data):
	    '''Print tag'''
	    if (tag.endswith('.pkg') or tag.endswith('dmg')):
	        print 'This download link contains a valid package: %s' % tag
 	return tag

    def main(self):
	'''Return a download URL for latest FirstClass client'''
        if "url" in self.env:
            self.output("Using input URL %s" % self.env["url"])
            return
        self.env["url"] = self.get_fc_url()
        self.output("Found URL %s" % self.env["url"])
    

if __name__ == '__main__':
    processor = FirstClassURLProvider()
    processor.execute_shell()


