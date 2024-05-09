from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status
from .OrderReturnedResponse import OrderReturnedResponse


@JsonMap({})
class ListOrderReturn200Response(BaseModel):
    def __init__(self, status: Status = None, data: List[OrderReturnedResponse] = None):
        self.status = self._define_object(status, Status)
        self.data = self._define_list(data, OrderReturnedResponse)
