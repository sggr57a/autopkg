#!/usr/bin/python
#
# Copyright 2017 Graham Pugh
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

from autopkglib import Processor, ProcessorError

import subprocess
import os.path
import json
import requests

# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
# Altered to remove output_title and enter prod_name for title - John McLaughlin 12/3/2018

__all__ = ["Slacker"]

class Slacker(Processor):
    description = ("Posts to Slack via webhook based on output of a JSSImporter run. "
                    "Takes elements from " "https://gist.github.com/devStepsize/b1b795309a217d24566dcc0ad136f784"
                    "and https://github.com/autopkg/nmcspadden-recipes/blob/master/PostProcessors/Yo.py")
    input_variables = {
        "JSS_URL": {
            "required": False,
            "description": ("JSS_URL.")
        },
        "policy_category": {
            "required": False,
            "description": ("Policy category.")
        },
        "category": {
            "required": False,
            "description": ("Package category.")
        },
        "prod_name": {
            "required": False,
            "description": ("PROD_NAME.")
        },
        "jss_changed_objects": {
            "required": False,
            "description": ("Dictionary of added or changed values.")
        },
	"package": {
            "required": False,
            "description": ("Package name.")
        },
        "jss_importer_summary_result": {
            "required": False,
            "description": ("Description of interesting results.")
        },
        "webhook_url": {
            "required": False,
            "description": ("Slack webhook.")
        }
    }
    output_variables = {
    }

    __doc__ = description

    def main(self):
        JSS_URL = self.env.get("JSS_URL")
        policy_category = self.env.get("policy_category")
        category = self.env.get("category")
        prod_name = self.env.get("prod_name")
	jss_importer_summary_result = self.env.get("jss_importer_summary_result")
	jss_changed_objects = self.env.get("jss_changed_objects")
	jss_repo_updated = self.env.get("jss_repo_updated")
	jss_package_name = self.env.get("package")
	webhook_url = self.env.get("webhook_url")
	
	print "CHANGES: %s" % jss_changed_objects 
	print "PACKAGE: %s" % jss_package_name

	if jss_changed_objects["jss_repo_updated"]:
            jss_policy_name = "%s" % jss_importer_summary_result["data"]["Policy"]
            jss_policy_version = "%s" % jss_importer_summary_result["data"]["Version"]
            jss_uploaded_package = "%s" % jss_importer_summary_result["data"]["Package"]
            print "JSS address: %s" % JSS_URL
            print "Title: %s" % prod_name
            print "Version: %s" % jss_policy_version
            print "Category: %s" % category
            print "Package: %s" % jss_package_name

            if jss_uploaded_package:
		 slack_text = "*New Item added to JSS*\nURL: %s\nTitle: *%s*\nVersion: *%s*\nCategory: *%s*\nUploaded Package Name: *%s*" % (JSS_URL, prod_name, jss_policy_version, category, jss_package_name)

            slack_data = {'text': slack_text}

            response = requests.post(webhook_url, json=slack_data)
            if response.status_code != 200:
                raise ValueError(
                                'Request to slack returned an error %s, the response is:\n%s'
                                % (response.status_code, response.text)
                                )


if __name__ == "__main__":
    processor = Slacker()
    processor.execute_shell()
