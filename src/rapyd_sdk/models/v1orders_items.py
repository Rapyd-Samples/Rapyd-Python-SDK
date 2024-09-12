from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class V1ordersItemsType(Enum):
    """An enumeration representing different categories.

    :cvar SHIPPING: "shipping"
    :vartype SHIPPING: str
    :cvar SKU: "sku"
    :vartype SKU: str
    """

    SHIPPING = "shipping"
    SKU = "sku"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, V1ordersItemsType._member_map_.values()))


@JsonMap({"type_": "type"})
class V1ordersItems(BaseModel):
    """V1ordersItems

    :param amount: Price of one SKU unit, in the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015., defaults to None
    :type amount: str, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param description: Description of the item., defaults to None
    :type description: str, optional
    :param parent: ID of the SKU object that represents the product. String starting with sku_. Each SKU can appear in this list only one time, for items of type 'sku'. Required when type is sku. Must be null when type is shipping., defaults to None
    :type parent: str, optional
    :param type_: Type of line item., defaults to None
    :type type_: V1ordersItemsType, optional
    :param quantity: Quantity of the product in the line item. Integer. Required when type is sku., defaults to None
    :type quantity: float, optional
    """

    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        description: str = None,
        parent: str = None,
        type_: V1ordersItemsType = None,
        quantity: float = None,
    ):
        """V1ordersItems

        :param amount: Price of one SKU unit, in the currency defined in currency. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015., defaults to None
        :type amount: str, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param description: Description of the item., defaults to None
        :type description: str, optional
        :param parent: ID of the SKU object that represents the product. String starting with sku_. Each SKU can appear in this list only one time, for items of type 'sku'. Required when type is sku. Must be null when type is shipping., defaults to None
        :type parent: str, optional
        :param type_: Type of line item., defaults to None
        :type type_: V1ordersItemsType, optional
        :param quantity: Quantity of the product in the line item. Integer. Required when type is sku., defaults to None
        :type quantity: float, optional
        """
        self.amount = self._define_str("amount", amount, nullable=True)
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.description = self._define_str("description", description, nullable=True)
        self.parent = self._define_str("parent", parent, nullable=True)
        self.type_ = (
            self._enum_matching(type_, V1ordersItemsType.list(), "type_")
            if type_
            else None
        )
        self.quantity = self._define_number("quantity", quantity, nullable=True)
