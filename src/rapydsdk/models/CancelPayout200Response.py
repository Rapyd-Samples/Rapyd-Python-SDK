from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Payout import Payout
from .Status import Status


@JsonMap({})
class CancelPayout200Response(BaseModel):
    def __init__(self, data: Payout = None, status: Status = None):
        self.data = self._define_object(data, Payout)
        self.status = self._define_object(status, Status)
