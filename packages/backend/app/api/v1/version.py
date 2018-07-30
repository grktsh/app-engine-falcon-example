# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import falcon  # noqa: F401

from ... import __version__


class Version(object):
    def on_get(self, req, resp):
        # type: (falcon.Request, falcon.Response) -> None
        resp.media = {'version': __version__}
