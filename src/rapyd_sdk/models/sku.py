from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .sku_package_dimensions import SkuPackageDimensions


@JsonMap({"id_": "id"})
class Sku(BaseModel):
    """Sku

    :param active: Indicates whether the product is currently being sold. Default is false., defaults to None
    :type active: bool, optional
    :param attributes: Up to 5 alphanumeric key-value pairs defined by the merchant. Each key must match a string in the attributes list of the corresponding product object., defaults to None
    :type attributes: dict, optional
    :param created_at: Time of creation of this SKU, in Unix time. Response  only., defaults to None
    :type created_at: float, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param id_: ID of the SKU object. Alphanumeric characters and underscores. Defined by the merchant, or a string starting with **sku**., defaults to None
    :type id_: str, optional
    :param image: URL of image associated with the product., defaults to None
    :type image: str, optional
    :param inventory: Contains the following fields: type - One of the following values: finite - Physical objects that can be counted. infinite - Products such as downloadable software. bucket - Products that are sold by measurable quantity. quantity - The number of units available in inventory. Integer. Relevant when type is finite. value - The status of the product on hand in inventory. Relevant when type is bucket. One of the following: in_stock - A normal amount of product is available in inventory. limited - There is enough product in inventory for small orders only. * out_of_stock - No product remains in inventory., defaults to None
    :type inventory: dict, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param package_dimensions: Physical attributes of the SKU item. Contains the following fields, height length weight width These fields are represented as numbers, but it is the responsibility of the merchant to define and interpret the relevant units of length and weight., defaults to None
    :type package_dimensions: SkuPackageDimensions, optional
    :param price: Price of one unit. Decimal., defaults to None
    :type price: float, optional
    :param product: ID of the product that this SKU relates to., defaults to None
    :type product: str, optional
    :param updated_at: Time that this product was last updated, in Unix time. Response only., defaults to None
    :type updated_at: float, optional
    """

    def __init__(
        self,
        active: bool = None,
        attributes: dict = None,
        created_at: float = None,
        currency: str = None,
        id_: str = None,
        image: str = None,
        inventory: dict = None,
        metadata: dict = None,
        package_dimensions: SkuPackageDimensions = None,
        price: float = None,
        product: str = None,
        updated_at: float = None,
    ):
        """Sku

        :param active: Indicates whether the product is currently being sold. Default is false., defaults to None
        :type active: bool, optional
        :param attributes: Up to 5 alphanumeric key-value pairs defined by the merchant. Each key must match a string in the attributes list of the corresponding product object., defaults to None
        :type attributes: dict, optional
        :param created_at: Time of creation of this SKU, in Unix time. Response  only., defaults to None
        :type created_at: float, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param id_: ID of the SKU object. Alphanumeric characters and underscores. Defined by the merchant, or a string starting with **sku**., defaults to None
        :type id_: str, optional
        :param image: URL of image associated with the product., defaults to None
        :type image: str, optional
        :param inventory: Contains the following fields: type - One of the following values: finite - Physical objects that can be counted. infinite - Products such as downloadable software. bucket - Products that are sold by measurable quantity. quantity - The number of units available in inventory. Integer. Relevant when type is finite. value - The status of the product on hand in inventory. Relevant when type is bucket. One of the following: in_stock - A normal amount of product is available in inventory. limited - There is enough product in inventory for small orders only. * out_of_stock - No product remains in inventory., defaults to None
        :type inventory: dict, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param package_dimensions: Physical attributes of the SKU item. Contains the following fields, height length weight width These fields are represented as numbers, but it is the responsibility of the merchant to define and interpret the relevant units of length and weight., defaults to None
        :type package_dimensions: SkuPackageDimensions, optional
        :param price: Price of one unit. Decimal., defaults to None
        :type price: float, optional
        :param product: ID of the product that this SKU relates to., defaults to None
        :type product: str, optional
        :param updated_at: Time that this product was last updated, in Unix time. Response only., defaults to None
        :type updated_at: float, optional
        """
        self.active = active
        self.attributes = attributes
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.currency = self._define_str(
            "currency",
            currency,
            nullable=True,
            pattern="/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
        )
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.image = self._define_str("image", image, nullable=True)
        self.inventory = inventory
        self.metadata = metadata
        self.package_dimensions = self._define_object(
            package_dimensions, SkuPackageDimensions
        )
        self.price = self._define_number("price", price, nullable=True)
        self.product = self._define_str("product", product, nullable=True)
        self.updated_at = self._define_number("updated_at", updated_at, nullable=True)
