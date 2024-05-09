from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class VirtualAccountTransactionResponse(BaseModel):
    def __init__(
        self,
        original_amount: float = None,
        original_currency: str = None,
        fx_rate: float = None,
        account_id: str = None,
        account_id_type: str = None,
        amount: float = None,
        created_at: int = None,
        currency: str = None,
        ewallet: str = None,
        id: str = None,
    ):
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
        self.account_id = account_id
        self.account_id_type = account_id_type
        self.amount = amount
        self.created_at = created_at
        self.currency = currency
        self.ewallet = ewallet
        self.id = id
