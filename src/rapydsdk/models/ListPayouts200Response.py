from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Payout import Payout
from .Status import Status


@JsonMap({})
class ListPayouts200Response(BaseModel):
    def __init__(self, data: List[Payout] = None, status: Status = None):
        self.data = self._define_list(data, Payout)
        self.status = self._define_object(status, Status)
