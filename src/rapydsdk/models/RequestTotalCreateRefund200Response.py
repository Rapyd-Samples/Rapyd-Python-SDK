from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Refund import Refund
from .Status import Status


@JsonMap({})
class RequestTotalCreateRefund200Response(BaseModel):
    def __init__(self, data: Refund = None, status: Status = None):
        self.data = self._define_object(data, Refund)
        self.status = self._define_object(status, Status)
