# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from app.models.pets import Pet
from app.representations.pets import pet_dict


def test_pet_to_dict(testbed):
    pet = Pet(name='momo')
    pet.put()

    assert pet_dict(pet) == {'id': pet.key.id(), 'name': 'momo'}
