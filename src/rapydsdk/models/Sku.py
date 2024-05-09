from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class PackageDimensions1(BaseModel):
    def __init__(
        self,
        height: float = None,
        length: float = None,
        weight: float = None,
        width: float = None,
    ):
        self.height = height
        self.length = length
        self.weight = weight
        self.width = width


@JsonMap({})
class Sku(BaseModel):
    def __init__(
        self,
        active: bool = None,
        attributes: dict = None,
        created_at: float = None,
        currency: str = None,
        id: str = None,
        image: str = None,
        inventory: dict = None,
        metadata: dict = None,
        package_dimensions: PackageDimensions1 = None,
        price: float = None,
        product: str = None,
        updated_at: float = None,
    ):
        self.active = active
        self.attributes = attributes
        self.created_at = created_at
        self.currency = (
            self._pattern_matching(
                currency,
                "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/",
                "currency",
            )
            if currency
            else None
        )
        self.id = id
        self.image = image
        self.inventory = inventory
        self.metadata = metadata
        self.package_dimensions = self._define_object(
            package_dimensions, PackageDimensions1
        )
        self.price = price
        self.product = product
        self.updated_at = updated_at
