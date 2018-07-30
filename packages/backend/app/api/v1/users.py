# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import falcon

from ...entities.user import User


class Collection(object):
    def on_get(self, req, resp):
        users = User.query().order(User.key)
        resp.media = [user.to_dict() for user in users]

    def on_post(self, req, resp):
        user = User(email=req.media['email'])
        user.put()

        resp.media = user.to_dict()
        resp.status = falcon.HTTP_CREATED


class Item(object):
    def on_get(self, req, resp, user_id):
        user = User.get_by_id(int(user_id))
        if user is None:
            raise falcon.HTTPNotFound()
        resp.media = user.to_dict()
