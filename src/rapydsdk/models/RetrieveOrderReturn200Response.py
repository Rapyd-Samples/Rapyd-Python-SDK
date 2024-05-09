from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .OrderReturnedResponse import OrderReturnedResponse
from .Status import Status


@JsonMap({})
class RetrieveOrderReturn200Response(BaseModel):
    def __init__(self, data: OrderReturnedResponse = None, status: Status = None):
        self.data = self._define_object(data, OrderReturnedResponse)
        self.status = self._define_object(status, Status)
