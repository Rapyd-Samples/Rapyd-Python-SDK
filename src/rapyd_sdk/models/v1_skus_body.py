from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .v1skussku_id_inventory import V1skusskuIdInventory
from .v1skussku_id_package_dimensions import V1skusskuIdPackageDimensions


@JsonMap({})
class V1SkusBody(BaseModel):
    """V1SkusBody

    :param currency: currency
    :type currency: str
    :param inventory: inventory object {quantity, type, value}
    :type inventory: V1skusskuIdInventory
    :param price: The amount of the price. Decimal.
    :type price: float
    :param product: ID of the product that this SKU relates to. The type field of the product must be set to goods.
    :type product: str
    :param active: Indicates whether the product is currently available for purchase., defaults to None
    :type active: bool, optional
    :param attributes: Array of alphanumeric key-value pairs defined by the merchant. Each key must match a string in the "attributes" list of the corresponding "product" object., defaults to None
    :type attributes: List[str], optional
    :param image: URL of image associated with the product., defaults to None
    :type image: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param package_dimensions: Physical attributes of the SKU item. Object containing the following fields - height, length, weight, width, defaults to None
    :type package_dimensions: V1skusskuIdPackageDimensions, optional
    """

    def __init__(
        self,
        currency: str,
        inventory: V1skusskuIdInventory,
        price: float,
        product: str,
        active: bool = None,
        attributes: List[str] = None,
        image: str = None,
        metadata: dict = None,
        package_dimensions: V1skusskuIdPackageDimensions = None,
    ):
        """V1SkusBody

        :param currency: currency
        :type currency: str
        :param inventory: inventory object {quantity, type, value}
        :type inventory: V1skusskuIdInventory
        :param price: The amount of the price. Decimal.
        :type price: float
        :param product: ID of the product that this SKU relates to. The type field of the product must be set to goods.
        :type product: str
        :param active: Indicates whether the product is currently available for purchase., defaults to None
        :type active: bool, optional
        :param attributes: Array of alphanumeric key-value pairs defined by the merchant. Each key must match a string in the "attributes" list of the corresponding "product" object., defaults to None
        :type attributes: List[str], optional
        :param image: URL of image associated with the product., defaults to None
        :type image: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param package_dimensions: Physical attributes of the SKU item. Object containing the following fields - height, length, weight, width, defaults to None
        :type package_dimensions: V1skusskuIdPackageDimensions, optional
        """
        self.currency = self._define_str(
            "currency",
            currency,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.inventory = self._define_object(inventory, V1skusskuIdInventory)
        self.price = price
        self.product = product
        self.active = active
        self.attributes = attributes
        self.image = self._define_str("image", image, nullable=True)
        self.metadata = metadata
        self.package_dimensions = self._define_object(
            package_dimensions, V1skusskuIdPackageDimensions
        )
