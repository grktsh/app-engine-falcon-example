# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from google.appengine.ext import ndb

from .base import BaseModel


class User(BaseModel):
    email = ndb.StringProperty(required=True)
