# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import falcon_oas
from typing import List
from typing import Optional
from typing import Text


def user_loader(value, scopes, req):
    # type: (Text, List, falcon_oas.Request) -> Optional[Text]
    if value == 'secret':
        return 'fake user'
    return None
