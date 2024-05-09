from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .CardIssuing import CardIssuing
from .Status import Status


@JsonMap({})
class UpdateCardStatus200Response(BaseModel):
    def __init__(self, data: CardIssuing = None, status: Status = None):
        self.data = self._define_object(data, CardIssuing)
        self.status = self._define_object(status, Status)
