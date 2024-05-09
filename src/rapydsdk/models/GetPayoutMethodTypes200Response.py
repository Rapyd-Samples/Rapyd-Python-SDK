from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .PayoutMethodType import PayoutMethodType
from .Status import Status


@JsonMap({})
class GetPayoutMethodTypes200Response(BaseModel):
    def __init__(self, data: List[PayoutMethodType] = None, status: Status = None):
        self.data = self._define_list(data, PayoutMethodType)
        self.status = self._define_object(status, Status)
