# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from typing import Dict

from ..models.pets import Pet


def pet_dict(pet):
    # type: (Pet) -> Dict
    return {'id': pet.key.id(), 'name': pet.name}
