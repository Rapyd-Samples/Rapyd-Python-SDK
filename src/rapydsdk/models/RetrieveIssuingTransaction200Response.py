from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .VirtualAccountTransactionResponse import VirtualAccountTransactionResponse
from .Status import Status


@JsonMap({})
class RetrieveIssuingTransaction200Response(BaseModel):
    def __init__(
        self, data: VirtualAccountTransactionResponse = None, status: Status = None
    ):
        self.data = self._define_object(data, VirtualAccountTransactionResponse)
        self.status = self._define_object(status, Status)
