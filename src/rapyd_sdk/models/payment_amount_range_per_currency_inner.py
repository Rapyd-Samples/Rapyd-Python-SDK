from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class PaymentAmountRangePerCurrencyInner(BaseModel):
    """PaymentAmountRangePerCurrencyInner

    :param maximum_amount: Maximum amount supported by this payout method for the indicated currency. Decimal number., defaults to None
    :type maximum_amount: float, optional
    :param minimum_amount: Minimum amount supported by this payout method for the indicated currency. Decimal number., defaults to None
    :type minimum_amount: float, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    """

    def __init__(
        self,
        maximum_amount: float = None,
        minimum_amount: float = None,
        currency: str = None,
    ):
        """PaymentAmountRangePerCurrencyInner

        :param maximum_amount: Maximum amount supported by this payout method for the indicated currency. Decimal number., defaults to None
        :type maximum_amount: float, optional
        :param minimum_amount: Minimum amount supported by this payout method for the indicated currency. Decimal number., defaults to None
        :type minimum_amount: float, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        """
        self.maximum_amount = self._define_number(
            "maximum_amount", maximum_amount, nullable=True
        )
        self.minimum_amount = self._define_number(
            "minimum_amount", minimum_amount, nullable=True
        )
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
