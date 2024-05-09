from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .EwalletTransactionDetails import (
    EwalletTransactionDetails,
    EwalletTransactionDetailsGuard,
)
from .EwalletTransaction import EwalletTransaction
from .Status import Status


@JsonMap({})
class GetUserTransactionDetails200Response(BaseModel):
    def __init__(self, data: EwalletTransactionDetails = None, status: Status = None):
        self.data = EwalletTransactionDetailsGuard.return_one_of(data)
        self.status = self._define_object(status, Status)
