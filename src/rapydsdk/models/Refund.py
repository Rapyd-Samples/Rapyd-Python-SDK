from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class Ewallets2(BaseModel):
    def __init__(self, amount: float = None, ewallet: str = None):
        self.amount = amount
        self.ewallet = ewallet


@JsonMap({})
class Refund(BaseModel):
    def __init__(
        self,
        amount: float = None,
        created_at: float = None,
        currency: str = None,
        ewallets: List[Ewallets2] = None,
        failure_reason: str = None,
        fixed_side: str = None,
        fx_rate: str = None,
        id: str = None,
        merchant_debited_amount: str = None,
        merchant_debited_currency: str = None,
        merchant_reference_id: str = None,
        metadata: dict = None,
        payment: str = None,
        payment_created_at: float = None,
        payment_method_type: str = None,
        proportional_refund: bool = None,
        reason: str = None,
        receipt_number: float = None,
        status: str = None,
        updated_at: float = None,
    ):
        self.amount = amount
        self.created_at = created_at
        self.currency = (
            self._pattern_matching(
                currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "currency",
            )
            if currency
            else None
        )
        self.ewallets = self._define_list(ewallets, Ewallets2)
        self.failure_reason = failure_reason
        self.fixed_side = fixed_side
        self.fx_rate = fx_rate
        self.id = id
        self.merchant_debited_amount = merchant_debited_amount
        self.merchant_debited_currency = merchant_debited_currency
        self.merchant_reference_id = merchant_reference_id
        self.metadata = metadata
        self.payment = payment
        self.payment_created_at = payment_created_at
        self.payment_method_type = payment_method_type
        self.proportional_refund = proportional_refund
        self.reason = reason
        self.receipt_number = receipt_number
        self.status = status
        self.updated_at = updated_at
