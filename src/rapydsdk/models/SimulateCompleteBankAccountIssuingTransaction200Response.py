from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class Transactions(BaseModel):
    def __init__(
        self,
        id: str = None,
        ewallet: str = None,
        account_id: str = None,
        account_id_type: str = None,
        amount: float = None,
        currency: str = None,
        created_at: float = None,
        original_amount: float = None,
        original_currency: str = None,
        fx_rate: float = None,
    ):
        self.id = id
        self.ewallet = ewallet
        self.account_id = account_id
        self.account_id_type = account_id_type
        self.amount = amount
        self.currency = currency
        self.created_at = created_at
        self.original_amount = original_amount
        self.original_currency = (
            self._pattern_matching(
                original_currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "original_currency",
            )
            if original_currency
            else None
        )
        self.fx_rate = fx_rate


@JsonMap({})
class Data14(BaseModel):
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
        transactions: List[Transactions] = None,
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
        self.transactions = self._define_list(transactions, Transactions)
        self.requested_currency = requested_currency


@JsonMap({})
class SimulateCompleteBankAccountIssuingTransaction200Response(BaseModel):
    def __init__(self, data: Data14 = None, status: Status = None):
        self.data = self._define_object(data, Data14)
        self.status = self._define_object(status, Status)
