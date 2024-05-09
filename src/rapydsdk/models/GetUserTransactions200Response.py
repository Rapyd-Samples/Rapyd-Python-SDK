from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .EwalletTransactionDetails import (
    EwalletTransactionDetails,
    EwalletTransactionDetailsGuard,
)
from .EwalletTransaction import EwalletTransaction
from .Status import Status


@JsonMap({})
class GetUserTransactions200Response(BaseModel):
    def __init__(
        self, data: List[EwalletTransactionDetails] = None, status: Status = None
    ):
        self.data = self._define_list(data, EwalletTransactionDetails)
        self.status = self._define_object(status, Status)
