from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class Transactions1(BaseModel):
    def __init__(
        self,
        id: str = None,
        ewallet: str = None,
        account_id: str = None,
        account_id_type: str = None,
        amount: float = None,
        currency: str = None,
        created_at: float = None,
        receiving_currency: bool = None,
        original_currency: str = None,
        original_amount: str = None,
        fx_rate: str = None,
    ):
        self.id = id
        self.ewallet = ewallet
        self.account_id = account_id
        self.account_id_type = account_id_type
        self.amount = amount
        self.currency = currency
        self.created_at = created_at
        self.receiving_currency = receiving_currency
        self.original_currency = original_currency
        self.original_amount = original_amount
        self.fx_rate = fx_rate


@JsonMap({})
class Data15(BaseModel):
    def __init__(
        self,
        id: str = None,
        merchant_reference_id: str = None,
        ewallet: str = None,
        bank_account: dict = None,
        metadata: dict = None,
        status: str = None,
        description: str = None,
        funding_instructions: dict = None,
        currency: str = None,
        transactions: List[Transactions1] = None,
        requested_currency: str = None,
    ):
        self.id = id
        self.merchant_reference_id = merchant_reference_id
        self.ewallet = ewallet
        self.bank_account = bank_account
        self.metadata = metadata
        self.status = status
        self.description = description
        self.funding_instructions = funding_instructions
        self.currency = currency
        self.transactions = self._define_list(transactions, Transactions1)
        self.requested_currency = requested_currency


@JsonMap({})
class RetrieveIssuingByRapydToken200Response(BaseModel):
    def __init__(self, data: Data15 = None, status: Status = None):
        self.data = self._define_object(data, Data15)
        self.status = self._define_object(status, Status)
