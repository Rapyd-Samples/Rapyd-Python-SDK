from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel


class Duration(Enum):
    FOREVER = "forever"
    REPEATING = "repeating"

    def list():
        return list(map(lambda x: x.value, Duration._member_map_.values()))


@JsonMap({})
class Coupon(BaseModel):
    def __init__(
        self,
        amount_off: float = None,
        created: float = None,
        currency: str = None,
        description: str = None,
        discount_duration_in_uses: float = None,
        discount_valid_until: float = None,
        discount_validity_in_months: float = None,
        duration: Duration = None,
        duration_in_months: float = None,
        id: str = None,
        max_redemptions: float = None,
        metadata: dict = None,
        percent_off: float = None,
        redeem_by: float = None,
        times_redeemed: float = None,
        valid: bool = None,
    ):
        self.amount_off = amount_off
        self.created = created
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
        self.discount_duration_in_uses = discount_duration_in_uses
        self.discount_valid_until = discount_valid_until
        self.discount_validity_in_months = discount_validity_in_months
        self.duration = (
            self._enum_matching(duration, Duration.list(), "duration")
            if duration
            else None
        )
        self.duration_in_months = duration_in_months
        self.id = id
        self.max_redemptions = max_redemptions
        self.metadata = metadata
        self.percent_off = percent_off
        self.redeem_by = redeem_by
        self.times_redeemed = times_redeemed
        self.valid = valid
