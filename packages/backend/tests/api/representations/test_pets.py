# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from app.api.representations.pets import pet_to_dict
from app.entities.pets import Pet


def test_pet_to_dict(testbed):
    pet = Pet(name='momo')
    pet.put()

    assert pet_to_dict(pet) == {'id': pet.key.id(), 'name': 'momo'}
