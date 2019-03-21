# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import falcon
from typing import Any
from typing import Dict

from ..models.pets import Pet


def extract_pet(req, resp, resource, params):
    # type: (falcon.Request, falcon.Response, Any, Dict) -> None
    pet = Pet.get_by_id(params['pet_id'])
    if pet is None:
        raise falcon.HTTPNotFound()

    params['pet'] = pet
    del params['pet_id']
