from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .OrderResponse import OrderResponse
from .Status import Status


@JsonMap({})
class UpdateOrder200Response(BaseModel):
    def __init__(self, data: OrderResponse = None, status: Status = None):
        self.data = self._define_object(data, OrderResponse)
        self.status = self._define_object(status, Status)
