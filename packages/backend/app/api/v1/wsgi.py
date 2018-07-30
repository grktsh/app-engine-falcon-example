# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import falcon

from . import users
from .version import Version

app = falcon.API()
app.add_route('/api/v1/version', Version())
app.add_route('/api/v1/users', users.Collection())
app.add_route('/api/v1/users/{user_id}', users.Item())
