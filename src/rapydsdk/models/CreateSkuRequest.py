from enum import Enum
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel


class Type9(Enum):
    FINITE = "finite"
    INFINITE = "infinite"
    BUCKET = "bucket"

    def list():
        return list(map(lambda x: x.value, Type9._member_map_.values()))


class Value1(Enum):
    IN_STOCK = "in_stock"
    LIMITED = "limited"
    OUT_OF_STOCK = "out_of_stock"

    def list():
        return list(map(lambda x: x.value, Value1._member_map_.values()))


@JsonMap({"type_": "type"})
class Inventory1(BaseModel):
    def __init__(self, type_: Type9 = None, quantity: int = None, value: Value1 = None):
        self.type_ = (
            self._enum_matching(type_, Type9.list(), "type_") if type_ else None
        )
        self.quantity = quantity
        self.value = (
            self._enum_matching(value, Value1.list(), "value") if value else None
        )


@JsonMap({})
class PackageDimensions5(BaseModel):
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
class CreateSkuRequest(BaseModel):
    def __init__(
        self,
        currency: str,
        inventory: Inventory1,
        price: float,
        product: str,
        active: bool = None,
        attributes: List[str] = None,
        image: str = None,
        metadata: dict = None,
        package_dimensions: PackageDimensions5 = None,
    ):
        self.currency = self._pattern_matching(
            currency,
            "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
            "currency",
        )
        self.inventory = self._define_object(inventory, Inventory1)
        self.price = price
        self.product = product
        self.active = active
        self.attributes = attributes
        self.image = image
        self.metadata = metadata
        self.package_dimensions = self._define_object(
            package_dimensions, PackageDimensions5
        )
