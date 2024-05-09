from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .CardTransaction import CardTransaction
from .Status import Status


@JsonMap({})
class GetCardIssuingTransaction200Response(BaseModel):
    def __init__(self, data: CardTransaction = None, status: Status = None):
        self.data = self._define_object(data, CardTransaction)
        self.status = self._define_object(status, Status)
