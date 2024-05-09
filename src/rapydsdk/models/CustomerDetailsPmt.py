from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Address import Address
from .CustomerDiscount import CustomerDiscount
from .Subscription import Subscription
from .CustomerPaymentMethod import CustomerPaymentMethod, CustomerPaymentMethodGuard


@JsonMap({})
class PaymentMethods1(BaseModel):
    def __init__(
        self,
        data: List[CustomerPaymentMethod] = None,
        has_more: bool = None,
        total_count: int = None,
        url: str = None,
    ):
        self.data = self._define_list(data, CustomerPaymentMethod)
        self.has_more = has_more
        self.total_count = total_count
        self.url = url


@JsonMap({})
class CustomerDetailsPmt(BaseModel):
    def __init__(
        self,
        name: str,
        addresses: List[Address] = None,
        business_vat_id: str = None,
        created_at: int = None,
        default_payment_method: str = None,
        delinquent: bool = None,
        description: str = None,
        discount: CustomerDiscount = None,
        email: str = None,
        ewallet: str = None,
        id: str = None,
        invoice_prefix: str = None,
        metadata: dict = None,
        payment_methods: PaymentMethods1 = None,
        phone_number: str = None,
        subscriptions: List[Subscription] = None,
        network_reference_id: str = None,
        complete_payment_url: str = None,
        error_payment_url: str = None,
    ):
        self.addresses = self._define_list(addresses, Address)
        self.business_vat_id = business_vat_id
        self.created_at = created_at
        self.default_payment_method = default_payment_method
        self.delinquent = delinquent
        self.description = description
        self.discount = self._define_object(discount, CustomerDiscount)
        self.email = email
        self.ewallet = ewallet
        self.id = id
        self.invoice_prefix = invoice_prefix
        self.metadata = metadata
        self.name = name
        self.payment_methods = self._define_object(payment_methods, PaymentMethods1)
        self.phone_number = phone_number
        self.subscriptions = self._define_list(subscriptions, Subscription)
        self.network_reference_id = network_reference_id
        self.complete_payment_url = complete_payment_url
        self.error_payment_url = error_payment_url
