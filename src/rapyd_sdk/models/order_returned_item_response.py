from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"type_": "type"})
class OrderReturnedItemResponse(BaseModel):
    """OrderReturnedItemResponse

    :param amount: amount, defaults to None
    :type amount: float, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param description: description, defaults to None
    :type description: str, optional
    :param parent: parent, defaults to None
    :type parent: str, optional
    :param quantity: quantity, defaults to None
    :type quantity: float, optional
    :param type_: type_, defaults to None
    :type type_: str, optional
    """

    def __init__(
        self,
        amount: float = None,
        currency: str = None,
        description: str = None,
        parent: str = None,
        quantity: float = None,
        type_: str = None,
    ):
        """OrderReturnedItemResponse

        :param amount: amount, defaults to None
        :type amount: float, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param description: description, defaults to None
        :type description: str, optional
        :param parent: parent, defaults to None
        :type parent: str, optional
        :param quantity: quantity, defaults to None
        :type quantity: float, optional
        :param type_: type_, defaults to None
        :type type_: str, optional
        """
        self.amount = self._define_number("amount", amount, nullable=True)
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.description = self._define_str("description", description, nullable=True)
        self.parent = self._define_str("parent", parent, nullable=True)
        self.quantity = self._define_number("quantity", quantity, nullable=True)
        self.type_ = self._define_str("type_", type_, nullable=True)
