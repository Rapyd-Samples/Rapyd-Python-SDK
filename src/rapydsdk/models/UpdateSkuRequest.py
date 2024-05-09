from enum import Enum
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel


class Type8(Enum):
    FINITE = "finite"
    INFINITE = "infinite"
    BUCKET = "bucket"

    def list():
        return list(map(lambda x: x.value, Type8._member_map_.values()))


class Value(Enum):
    IN_STOCK = "in_stock"
    LIMITED = "limited"
    OUT_OF_STOCK = "out_of_stock"

    def list():
        return list(map(lambda x: x.value, Value._member_map_.values()))


@JsonMap({"type_": "type"})
class Inventory(BaseModel):
    def __init__(self, type_: Type8 = None, quantity: int = None, value: Value = None):
        self.type_ = (
            self._enum_matching(type_, Type8.list(), "type_") if type_ else None
        )
        self.quantity = quantity
        self.value = (
            self._enum_matching(value, Value.list(), "value") if value else None
        )


@JsonMap({})
class PackageDimensions4(BaseModel):
    def __init__(
        self,
        length: float = None,
        height: float = None,
        weight: float = None,
        width: float = None,
    ):
        self.length = length
        self.height = height
        self.weight = weight
        self.width = width


@JsonMap({})
class UpdateSkuRequest(BaseModel):
    def __init__(
        self,
        currency: str = None,
        inventory: Inventory = None,
        price: float = None,
        product: str = None,
        active: bool = None,
        attributes: List[str] = None,
        image: str = None,
        metadata: dict = None,
        package_dimensions: PackageDimensions4 = None,
    ):
        self.currency = (
            self._pattern_matching(
                currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "currency",
            )
            if currency
            else None
        )
        self.inventory = self._define_object(inventory, Inventory)
        self.price = price
        self.product = product
        self.active = active
        self.attributes = attributes
        self.image = image
        self.metadata = metadata
        self.package_dimensions = self._define_object(
            package_dimensions, PackageDimensions4
        )
