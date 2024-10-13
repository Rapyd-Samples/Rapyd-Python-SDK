from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .address_1 import Address1
from .customer_request_payment_method import CustomerRequestPaymentMethod


@JsonMap({})
class CustomerRequest(BaseModel):
    """CustomerRequest

    :param addresses: Array of address objects associated with this customer. For more information, defaults to None
    :type addresses: List[Address1], optional
    :param business_vat_id: The tax ID number of the customer, defaults to None
    :type business_vat_id: str, optional
    :param coupon: The ID of a coupon that is assigned to this customer, defaults to None
    :type coupon: str, optional
    :param payment_method: The payment method that is used when the transaction does not specify a payment method. String starting with **card_** or other_., defaults to None
    :type payment_method: CustomerRequestPaymentMethod, optional
    :param description: A text description of the customer, defaults to None
    :type description: str, optional
    :param email: Customer's email address, defaults to None
    :type email: str, optional
    :param ewallet: ID of the wallet that is linked to the customer. String starting with **ewallet_**., defaults to None
    :type ewallet: str, optional
    :param invoice_prefix: A custom string that is prefixed to all invoices for this customer., defaults to None
    :type invoice_prefix: str, optional
    :param metadata: A JSON object defined by the Rapyd partner, defaults to None
    :type metadata: dict, optional
    :param name: The name of the individual customer or the business name, defaults to None
    :type name: str, optional
    :param phone_number: Customer's primary phone number in E.164 format, defaults to None
    :type phone_number: str, optional
    """

    def __init__(
        self,
        addresses: List[Address1] = None,
        business_vat_id: str = None,
        coupon: str = None,
        payment_method: CustomerRequestPaymentMethod = None,
        description: str = None,
        email: str = None,
        ewallet: str = None,
        invoice_prefix: str = None,
        metadata: dict = None,
        name: str = None,
        phone_number: str = None,
    ):
        """CustomerRequest

        :param addresses: Array of address objects associated with this customer. For more information, defaults to None
        :type addresses: List[Address1], optional
        :param business_vat_id: The tax ID number of the customer, defaults to None
        :type business_vat_id: str, optional
        :param coupon: The ID of a coupon that is assigned to this customer, defaults to None
        :type coupon: str, optional
        :param payment_method: The payment method that is used when the transaction does not specify a payment method. String starting with **card_** or other_., defaults to None
        :type payment_method: CustomerRequestPaymentMethod, optional
        :param description: A text description of the customer, defaults to None
        :type description: str, optional
        :param email: Customer's email address, defaults to None
        :type email: str, optional
        :param ewallet: ID of the wallet that is linked to the customer. String starting with **ewallet_**., defaults to None
        :type ewallet: str, optional
        :param invoice_prefix: A custom string that is prefixed to all invoices for this customer., defaults to None
        :type invoice_prefix: str, optional
        :param metadata: A JSON object defined by the Rapyd partner, defaults to None
        :type metadata: dict, optional
        :param name: The name of the individual customer or the business name, defaults to None
        :type name: str, optional
        :param phone_number: Customer's primary phone number in E.164 format, defaults to None
        :type phone_number: str, optional
        """
        self.addresses = self._define_list(addresses, Address1)
        self.business_vat_id = self._define_str(
            "business_vat_id", business_vat_id, nullable=True
        )
        self.coupon = self._define_str("coupon", coupon, nullable=True)
        self.payment_method = self._define_object(
            payment_method, CustomerRequestPaymentMethod
        )
        self.description = self._define_str("description", description, nullable=True)
        self.email = self._define_str("email", email, nullable=True)
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
        self.invoice_prefix = self._define_str(
            "invoice_prefix", invoice_prefix, nullable=True
        )
        self.metadata = metadata
        self.name = self._define_str("name", name, nullable=True)
        self.phone_number = self._define_str(
            "phone_number", phone_number, nullable=True
        )
