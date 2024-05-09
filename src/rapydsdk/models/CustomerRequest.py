from __future__ import annotations
from typing import List
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .Address import Address


@JsonMap({"type_": "type"})
class PaymentMethod3(BaseModel):
    def __init__(self, type_: str = None, fields: dict = None):
        self.type_ = type_
        self.fields = fields


class PaymentMethod2Guard(OneOfBaseModel):
    class_list = {"str": str, "PaymentMethod3": PaymentMethod3}


PaymentMethod2 = Union[str, PaymentMethod3]


@JsonMap({})
class CustomerRequest(BaseModel):
    def __init__(
        self,
        addresses: List[Address] = None,
        business_vat_id: str = None,
        coupon: str = None,
        default_payment_method: str = None,
        description: str = None,
        email: str = None,
        ewallet: str = None,
        invoice_prefix: str = None,
        metadata: dict = None,
        name: str = None,
        phone_number: str = None,
        payment_method: PaymentMethod2 = None,
    ):
        self.addresses = self._define_list(addresses, Address)
        self.business_vat_id = business_vat_id
        self.coupon = coupon
        self.default_payment_method = default_payment_method
        self.description = description
        self.email = email
        self.ewallet = ewallet
        self.invoice_prefix = invoice_prefix
        self.metadata = metadata
        self.name = name
        self.phone_number = phone_number
        self.payment_method = PaymentMethod2Guard.return_one_of(payment_method)
