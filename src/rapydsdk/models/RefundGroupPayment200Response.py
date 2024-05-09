from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status
from .Payment import Payment


@JsonMap({})
class Data27(BaseModel):
    def __init__(
        self,
        amount: float = None,
        amount_to_replace: float = None,
        cancel_reason: str = None,
        country: str = None,
        currency: str = None,
        description: str = None,
        expiration: float = None,
        id: str = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        payments: List[Payment] = None,
        status: str = None,
    ):
        self.amount = amount
        self.amount_to_replace = amount_to_replace
        self.cancel_reason = cancel_reason
        self.country = country
        self.currency = currency
        self.description = description
        self.expiration = expiration
        self.id = id
        self.merchant_reference_id = merchant_reference_id
        self.metadata = metadata
        self.payments = self._define_list(payments, Payment)
        self.status = status


@JsonMap({})
class RefundGroupPayment200Response(BaseModel):
    def __init__(self, data: Data27 = None, status: Status = None):
        self.data = self._define_object(data, Data27)
        self.status = self._define_object(status, Status)
