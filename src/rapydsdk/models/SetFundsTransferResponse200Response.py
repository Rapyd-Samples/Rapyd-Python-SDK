from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Transfer import Transfer
from .Status import Status


@JsonMap({})
class SetFundsTransferResponse200Response(BaseModel):
    def __init__(self, data: Transfer = None, status: Status = None):
        self.data = self._define_object(data, Transfer)
        self.status = self._define_object(status, Status)
