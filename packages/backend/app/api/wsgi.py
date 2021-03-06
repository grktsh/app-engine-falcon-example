# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import os.path

from falcon_oas import create_api

from .v1 import version

here = os.path.abspath(os.path.dirname(__file__))
spec_path = os.path.join(here, '../../node_modules/api-docs/openapi.json')
with open(spec_path) as f:
    spec_dict = json.load(f)

app = create_api(spec_dict, base_module='app')
app.add_route('/api/v1/version', version.Version())
