#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
.. module:: tests

This file is part of **python-openzwave** project https://github.com/bibi21000/python-openzwave.
    :platform: Unix, Windows, MacOS X
    :sinopsis: openzwave Library

.. moduleauthor: bibi21000 aka Sébastien GALLET <bibi21000@gmail.com>

License : GPL(v3)

**python-openzwave** is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

**python-openzwave** is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with python-openzwave. If not, see http://www.gnu.org/licenses.

"""

import sys, os, shutil
import time
import unittest
from pprint import pprint
import datetime
import random
import socket
import libopenzwave
import re
import time
from louie import dispatcher, All
import libopenzwave
import openzwave
from openzwave.node import ZWaveNode
from openzwave.value import ZWaveValue
from openzwave.scene import ZWaveScene
from openzwave.controller import ZWaveController
from openzwave.network import ZWaveNetwork
from openzwave.option import ZWaveOption
from tests.common import pyozw_version
from tests.common import SLEEP
from tests.api.common import TestApi
from tests.common import TestPyZWave

class TestNetworkApi(TestPyZWave):

    @classmethod
    def setUpClass(self):
        super(TestNetworkStartStop, self).setUpClass()
        self.options = None
        self.network = None

    @classmethod
    def tearDownClass(self):
        if self.network is not None:
            self.network.stop()
        super(TestNetworkStartStop, self).tearDownClass()

    def test_000_api_network(self):
        self.driver_ready = False
        self.driver_removed = False
        self.touchFile('ttyUSBO_fake')
        self.options = ZWaveOption(device='ttyUSBO_fake', user_path=self.userpath)
        self.options.set_log_file("OZW_Log.log")
        self.options.set_append_log_file(False)
        self.options.set_console_output(False)
        self.options.set_save_log_level("Debug")
        self.options.set_logging(True)
        self.options.lock()
        self.network = ZWaveNetwork(self.options, autostart=False)
        self.rmFile('ttyUSBO_fake')

if __name__ == '__main__':
    sys.argv.append('-v')
    unittest.main()
