# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import falcon

import app


def test_version(client):
    response = client.simulate_get('/api/v1/version')

    assert response.status == falcon.HTTP_OK
    assert response.json['version'] == app.__version__
