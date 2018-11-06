# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import falcon
from typing import Any  # noqa: F401
from typing import Dict  # noqa: F401

from app.entities.pets import Pet


def extract_pet(req, resp, resource, params):
    # type: (falcon.Request, falcon.Response, Any, Dict) -> None
    pet = Pet.get_by_id(int(params['pet_id']))
    if pet is None:
        raise falcon.HTTPNotFound()

    params['pet'] = pet
    del params['pet_id']
