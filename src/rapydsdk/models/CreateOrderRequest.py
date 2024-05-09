from __future__ import annotations
from enum import Enum
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Address import Address


class Type3(Enum):
    SHIPPING = "shipping"
    SKU = "sku"

    def list():
        return list(map(lambda x: x.value, Type3._member_map_.values()))


@JsonMap({"type_": "type"})
class Items(BaseModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        description: str = None,
        parent: str = None,
        type_: Type3 = None,
        quantity: float = None,
    ):
        self.amount = amount
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
        self.parent = parent
        self.type_ = (
            self._enum_matching(type_, Type3.list(), "type_") if type_ else None
        )
        self.quantity = quantity


@JsonMap({})
class CreateOrderRequest(BaseModel):
    def __init__(
        self,
        customer: str,
        currency: str,
        items: List[Items],
        coupon: str = None,
        email: str = None,
        metadata: dict = None,
        shipping_address: Address = None,
        tax_percent: float = None,
        upstream_id: str = None,
    ):
        self.coupon = coupon
        self.customer = customer
        self.currency = currency
        self.email = email
        self.items = self._define_list(items, Items)
        self.metadata = metadata
        self.shipping_address = self._define_object(shipping_address, Address)
        self.tax_percent = tax_percent
        self.upstream_id = upstream_id
