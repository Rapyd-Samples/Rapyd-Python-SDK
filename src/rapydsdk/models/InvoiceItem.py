from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Plan import Plan


@JsonMap({})
class Period(BaseModel):
    def __init__(self, start: str = None, end: str = None):
        self.start = start
        self.end = end


@JsonMap({"type_": "type"})
class InvoiceItem(BaseModel):
    def __init__(
        self,
        id: str = None,
        amount: float = None,
        currency: str = None,
        description: str = None,
        discountable: bool = None,
        invoice_item: str = None,
        metadata: dict = None,
        period: Period = None,
        proration: bool = None,
        quantity: float = None,
        plan: Plan = None,
        subscription: str = None,
        subscription_item: str = None,
        type_: str = None,
    ):
        self.id = id
        self.amount = amount
        self.currency = (
            self._pattern_matching(
                currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "currency",
            )
            if currency
            else None
        )
        self.description = description
        self.discountable = discountable
        self.invoice_item = invoice_item
        self.metadata = metadata
        self.period = self._define_object(period, Period)
        self.proration = proration
        self.quantity = quantity
        self.plan = self._define_object(plan, Plan)
        self.subscription = subscription
        self.subscription_item = subscription_item
        self.type_ = type_
