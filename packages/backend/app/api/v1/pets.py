# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import falcon
import falcon_oas

from ...entities.pets import Pet
from ..hooks import extract_pet
from ..representations.pets import pet_dict


class Collection(object):
    def on_get(self, req, resp):
        # type: (falcon.Request, falcon.Response) -> None
        pets = Pet.query().order(Pet.key)
        resp.media = [pet_dict(pet) for pet in pets]

    def on_post(self, req, resp):
        # type: (falcon_oas.Request, falcon.Response) -> None
        pet = Pet(name=req.oas_media['name'])
        pet.put()

        resp.media = pet_dict(pet)
        resp.status = falcon.HTTP_CREATED


@falcon.before(extract_pet)
class Item(object):
    def on_get(self, req, resp, pet):
        # type: (falcon.Request, falcon.Response, Pet) -> None
        resp.media = pet_dict(pet)

    def on_patch(self, req, resp, pet):
        # type: (falcon_oas.Request, falcon.Response, Pet) -> None
        try:
            pet.name = req.oas_media['name']
            pet.put()
        except KeyError:
            pass
        resp.media = pet_dict(pet)

    def on_delete(self, req, resp, pet):
        # type: (falcon.Request, falcon.Response, Pet) -> None
        pet.key.delete()

        resp.status = falcon.HTTP_NO_CONTENT
