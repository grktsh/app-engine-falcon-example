# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import os.path

from google.appengine.ext import vendor

vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))
