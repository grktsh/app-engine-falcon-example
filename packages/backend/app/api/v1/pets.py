# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import falcon

from app.api.hooks import extract_pet

from ...entities.pets import Pet


class Collection(object):
    def on_get(self, req, resp):
        # type: (falcon.Request, falcon.Response) -> None
        pets = Pet.query().order(Pet.key)
        resp.media = [pet.to_dict() for pet in pets]

    def on_post(self, req, resp):
        # type: (falcon.Request, falcon.Response) -> None
        if 'name' not in req.media:
            raise falcon.HTTPBadRequest()

        pet = Pet(name=req.media['name'])
        pet.put()

        resp.media = pet.to_dict()
        resp.status = falcon.HTTP_CREATED


@falcon.before(extract_pet)
class Item(object):
    def on_get(self, req, resp, pet):
        # type: (falcon.Request, falcon.Response, Pet) -> None
        resp.media = pet.to_dict()

    def on_patch(self, req, resp, pet):
        # type: (falcon.Request, falcon.Response, Pet) -> None
        if 'name' in req.media:
            pet.name = req.media['name']
            pet.put()

        resp.media = pet.to_dict()

    def on_delete(self, req, resp, pet):
        # type: (falcon.Request, falcon.Response, Pet) -> None
        pet.key.delete()

        resp.status = falcon.HTTP_NO_CONTENT
