# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from typing import Optional
from typing import Text


def user_loader(value):
    # type: (Text) -> Optional[Text]
    if value == 'secret':
        return 'fake user'
    return None
