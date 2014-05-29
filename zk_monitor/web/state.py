# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Copyright 2013 Nextdoor.com, Inc

"""
Handles generating the root index page for web requests.
"""

__author__ = 'matt@nextdoor.com (Matt Wise)'

from tornado import template
from tornado import web

from zk_monitor import utils

from zk_monitor.version import __version__ as VERSION


class StatusHandler(web.RequestHandler):
    """Serves up the zk_monitor /status page"""

    def initialize(self, settings):
        """Log the initialization of this root handler"""
        self.state = settings['ndsr']._zk.connected
        self.paths = settings['paths']

    def get(self):
        self.write(str(self.state))