# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from google.appengine.ext import ndb


class BaseModel(ndb.Model):
    def to_dict(self, include=None, exclude=None):
        values = super(BaseModel, self).to_dict(
            include=include, exclude=exclude
        )
        values['id'] = self.key.id()
        return values
