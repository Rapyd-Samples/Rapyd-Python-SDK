from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Refund import Refund
from .Status import Status


@JsonMap({})
class AllRefunds200Response(BaseModel):
    def __init__(self, data: List[Refund] = None, status: Status = None):
        self.data = self._define_list(data, Refund)
        self.status = self._define_object(status, Status)
