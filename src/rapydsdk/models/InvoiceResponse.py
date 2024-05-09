from __future__ import annotations
from enum import Enum
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .SubscriptionDiscount import SubscriptionDiscount
from .Payment import Payment
from .Payout import Payout
from .InvoiceItem import InvoiceItem


class Type2(Enum):
    PAYMENT = "payment"
    PAYOUT = "payout"

    def list():
        return list(map(lambda x: x.value, Type2._member_map_.values()))


@JsonMap({"type_": "type"})
class InvoiceResponse(BaseModel):
    def __init__(
        self,
        id: str = None,
        attempt_count: float = None,
        billing: str = None,
        billing_reason: str = None,
        created_at: float = None,
        discount: SubscriptionDiscount = None,
        currency: str = None,
        customer: str = None,
        days_until_due: float = None,
        description: str = None,
        due_date: str = None,
        metadata: dict = None,
        payment_fields: dict = None,
        payment_method: str = None,
        statement_descriptor: str = None,
        subscription: str = None,
        tax_percent: float = None,
        payment: Payment = None,
        payout: Payout = None,
        period_end: float = None,
        period_start: float = None,
        lines: List[InvoiceItem] = None,
        subtotal: float = None,
        tax: float = None,
        number: str = None,
        total: float = None,
        status: str = None,
        payout_fields: dict = None,
        type_: Type2 = None,
    ):
        self.id = id
        self.attempt_count = attempt_count
        self.billing = billing
        self.billing_reason = billing_reason
        self.created_at = created_at
        self.discount = self._define_object(discount, SubscriptionDiscount)
        self.currency = (
            self._pattern_matching(
                currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "currency",
            )
            if currency
            else None
        )
        self.customer = customer
        self.days_until_due = days_until_due
        self.description = description
        self.due_date = due_date
        self.metadata = metadata
        self.payment_fields = payment_fields
        self.payment_method = payment_method
        self.statement_descriptor = statement_descriptor
        self.subscription = subscription
        self.tax_percent = tax_percent
        self.payment = self._define_object(payment, Payment)
        self.payout = self._define_object(payout, Payout)
        self.period_end = period_end
        self.period_start = period_start
        self.lines = self._define_list(lines, InvoiceItem)
        self.subtotal = subtotal
        self.tax = tax
        self.number = number
        self.total = total
        self.status = status
        self.payout_fields = payout_fields
        self.type_ = (
            self._enum_matching(type_, Type2.list(), "type_") if type_ else None
        )
