from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .CardTransaction import CardTransaction
from .Status import Status


@JsonMap({})
class GetCardIssuingTransactions200Response(BaseModel):
    def __init__(self, data: List[CardTransaction] = None, status: Status = None):
        self.data = self._define_list(data, CardTransaction)
        self.status = self._define_object(status, Status)
