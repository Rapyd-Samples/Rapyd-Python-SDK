from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel


class Status2(Enum):
    ACT = "ACT"
    RVW = "RVW"
    PRA = "PRA"
    ARB = "ARB"
    LOS = "LOS"
    WIN = "WIN"
    REV = "REV"

    def list():
        return list(map(lambda x: x.value, Status2._member_map_.values()))


@JsonMap({})
class Dispute(BaseModel):
    def __init__(
        self,
        id: str = None,
        token: str = None,
        status: Status2 = None,
        amount: float = None,
        currency: str = None,
        dispute_category: str = None,
        dispute_reason_description: str = None,
        original_transaction_currency: str = None,
        original_transaction_amount: float = None,
        original_dispute_amount: float = None,
        original_dispute_currency: str = None,
        original_transaction_id: str = None,
        ewallet_id: str = None,
        central_processing_date: float = None,
        created_at: float = None,
        updated_at: float = None,
        due_date: float = None,
        payment_method: str = None,
        payment_method_data: dict = None,
        rate: float = None,
        evidence: str = None,
        evidence_reason_code: str = None,
        pre_dispute: bool = None,
        arn: str = None,
    ):
        self.id = id
        self.token = token
        self.status = (
            self._enum_matching(status, Status2.list(), "status") if status else None
        )
        self.amount = amount
        self.currency = currency
        self.dispute_category = dispute_category
        self.dispute_reason_description = dispute_reason_description
        self.original_transaction_currency = (
            self._pattern_matching(
                original_transaction_currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "original_transaction_currency",
            )
            if original_transaction_currency
            else None
        )
        self.original_transaction_amount = original_transaction_amount
        self.original_dispute_amount = original_dispute_amount
        self.original_dispute_currency = (
            self._pattern_matching(
                original_dispute_currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "original_dispute_currency",
            )
            if original_dispute_currency
            else None
        )
        self.original_transaction_id = original_transaction_id
        self.ewallet_id = ewallet_id
        self.central_processing_date = central_processing_date
        self.created_at = created_at
        self.updated_at = updated_at
        self.due_date = due_date
        self.payment_method = payment_method
        self.payment_method_data = payment_method_data
        self.rate = rate
        self.evidence = evidence
        self.evidence_reason_code = evidence_reason_code
        self.pre_dispute = pre_dispute
        self.arn = arn
