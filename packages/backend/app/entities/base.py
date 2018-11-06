# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from google.appengine.ext import ndb
from typing import Any  # noqa: F401
from typing import Dict  # noqa: F401
from typing import List  # noqa: F401
from typing import Optional  # noqa: F401
from typing import Set  # noqa: F401
from typing import Text  # noqa: F401
from typing import Tuple  # noqa: F401
from typing import Union  # noqa: F401


class BaseModel(ndb.Model):
    def to_dict(
        self,
        include=None,  # type: Optional[Union[List[Text], Tuple[Text], Set[Text]]]  # noqa: E501
        exclude=None,  # type: Optional[Union[List[Text], Tuple[Text], Set[Text]]]  # noqa: E501
    ):
        # type: (...) -> Dict[Text, Any]
        values = super(BaseModel, self).to_dict(
            include=include, exclude=exclude
        )
        values['id'] = self.key.id()
        return values
