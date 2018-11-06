# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import falcon

from .v1 import pets
from .v1 import version

app = falcon.API()
app.add_route('/api/v1/version', version.Version())
app.add_route('/api/v1/pets', pets.Collection())
app.add_route('/api/v1/pets/{pet_id}', pets.Item())
