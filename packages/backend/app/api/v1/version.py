# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import falcon

from ... import __version__


class Version(object):
    def on_get(self, req, resp):
        # type: (falcon.Request, falcon.Response) -> None
        resp.media = {'version': __version__}
