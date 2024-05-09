from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status
from .CardTransaction import CardTransaction


@JsonMap({})
class Data13(BaseModel):
    def __init__(
        self,
        bank_account: dict = None,
        currency: str = None,
        description: str = None,
        ewallet: str = None,
        funding_instructions: dict = None,
        id: str = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        status: str = None,
        transactions: List[CardTransaction] = None,
        requested_currency: str = None,
    ):
        self.bank_account = bank_account
        self.currency = currency
        self.description = description
        self.ewallet = ewallet
        self.funding_instructions = funding_instructions
        self.id = id
        self.merchant_reference_id = merchant_reference_id
        self.metadata = metadata
        self.status = status
        self.transactions = self._define_list(transactions, CardTransaction)
        self.requested_currency = requested_currency


@JsonMap({})
class CreateIssuing200Response(BaseModel):
    def __init__(self, data: Data13 = None, status: Status = None):
        self.data = self._define_object(data, Data13)
        self.status = self._define_object(status, Status)
