# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from ... import __version__


class Version(object):
    def on_get(self, req, resp):
        resp.media = {'version': __version__}
