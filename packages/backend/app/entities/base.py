# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from typing import (  # noqa: F401
    Any,
    Dict,
    List,
    Optional,
    Set,
    Text,
    Tuple,
    Union,
)

from google.appengine.ext import ndb


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
