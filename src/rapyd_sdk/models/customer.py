from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .address import Address
from .discount import Discount
from .customer_payment_methods import CustomerPaymentMethods
from .subscription import Subscription


@JsonMap({"id_": "id"})
class Customer(BaseModel):
    """customer

    :param addresses: addresses, defaults to None
    :type addresses: List[Address], optional
    :param business_vat_id: The tax ID number of the customer. Relevant when the customer is a business, defaults to None
    :type business_vat_id: str, optional
    :param created_at: Time of creation of this customer, in Unix time. Response only, defaults to None
    :type created_at: int, optional
    :param default_payment_method: The payment method that is used when the 'payment' object or subscription does not specify a payment method. The value must also appear in the payment_methods list. The payment method is referenced by its name field., defaults to None
    :type default_payment_method: str, optional
    :param delinquent: Indicates whether there is currently a failure of an automatic payment that is part of a subscription, or an invoice that was not paid when due. Response only. true - The account is delinquent false - The account is current, defaults to None
    :type delinquent: bool, optional
    :param description: A text description of the customer, defaults to None
    :type description: str, optional
    :param discount: Describes the fields relating to discounts in REST messages and webhooks for customer profiles and subscriptions Contains information about the coupon that applies to the customer. Read-only field. Adding a discount is a 2-step process - 1. Create Coupon, which returns a coupon ID. 2. Add the coupon ID to the coupon field of the customer with Create Customer or Update Customer., defaults to None
    :type discount: Discount, optional
    :param email: Customer's email address. Maximum 512 characters, defaults to None
    :type email: str, optional
    :param ewallet: ID of the wallet that is linked to the customer. String starting with ewallet_. Each wallet can be associated with only one customer, defaults to None
    :type ewallet: str, optional
    :param id_: ID of the Customer object. String starting with cus_, defaults to None
    :type id_: str, optional
    :param invoice_prefix: A custom string that is prefixed to all invoices for this customer. For more information see Invoice Object at https://docs.rapyd.net/build-with-rapyd/reference/invoices#invoice-object, defaults to None
    :type invoice_prefix: str, optional
    :param metadata: A JSON object defined by the client, defaults to None
    :type metadata: dict, optional
    :param name: The name of the customer
    :type name: str
    :param payment_methods: An object containing the following fields - * data - A list of up to three payment methods. For more information, see Customer Payment Method Object. * has_more - Indicates whether there are more than three payment methods for this customer. * total_count - Total number of payment methods for this customer. * url - URL for requesting all of the payment methods for this customer.., defaults to None
    :type payment_methods: CustomerPaymentMethods, optional
    :param phone_number: Customer's primary phone number in E.164 format. The merchant is responsible for verifying that the number is correct. One method of verifying could be to send an activation code to the phone by SMS, with a limited time for response., defaults to None
    :type phone_number: str, optional
    :param subscriptions: subscriptions, defaults to None
    :type subscriptions: List[Subscription], optional
    """

    def __init__(
        self,
        name: str,
        addresses: List[Address] = None,
        business_vat_id: str = None,
        created_at: int = None,
        default_payment_method: str = None,
        delinquent: bool = None,
        description: str = None,
        discount: Discount = None,
        email: str = None,
        ewallet: str = None,
        id_: str = None,
        invoice_prefix: str = None,
        metadata: dict = None,
        payment_methods: CustomerPaymentMethods = None,
        phone_number: str = None,
        subscriptions: List[Subscription] = None,
    ):
        """customer

        :param addresses: addresses, defaults to None
        :type addresses: List[Address], optional
        :param business_vat_id: The tax ID number of the customer. Relevant when the customer is a business, defaults to None
        :type business_vat_id: str, optional
        :param created_at: Time of creation of this customer, in Unix time. Response only, defaults to None
        :type created_at: int, optional
        :param default_payment_method: The payment method that is used when the 'payment' object or subscription does not specify a payment method. The value must also appear in the payment_methods list. The payment method is referenced by its name field., defaults to None
        :type default_payment_method: str, optional
        :param delinquent: Indicates whether there is currently a failure of an automatic payment that is part of a subscription, or an invoice that was not paid when due. Response only. true - The account is delinquent false - The account is current, defaults to None
        :type delinquent: bool, optional
        :param description: A text description of the customer, defaults to None
        :type description: str, optional
        :param discount: Describes the fields relating to discounts in REST messages and webhooks for customer profiles and subscriptions Contains information about the coupon that applies to the customer. Read-only field. Adding a discount is a 2-step process - 1. Create Coupon, which returns a coupon ID. 2. Add the coupon ID to the coupon field of the customer with Create Customer or Update Customer., defaults to None
        :type discount: Discount, optional
        :param email: Customer's email address. Maximum 512 characters, defaults to None
        :type email: str, optional
        :param ewallet: ID of the wallet that is linked to the customer. String starting with ewallet_. Each wallet can be associated with only one customer, defaults to None
        :type ewallet: str, optional
        :param id_: ID of the Customer object. String starting with cus_, defaults to None
        :type id_: str, optional
        :param invoice_prefix: A custom string that is prefixed to all invoices for this customer. For more information see Invoice Object at https://docs.rapyd.net/build-with-rapyd/reference/invoices#invoice-object, defaults to None
        :type invoice_prefix: str, optional
        :param metadata: A JSON object defined by the client, defaults to None
        :type metadata: dict, optional
        :param name: The name of the customer
        :type name: str
        :param payment_methods: An object containing the following fields - * data - A list of up to three payment methods. For more information, see Customer Payment Method Object. * has_more - Indicates whether there are more than three payment methods for this customer. * total_count - Total number of payment methods for this customer. * url - URL for requesting all of the payment methods for this customer.., defaults to None
        :type payment_methods: CustomerPaymentMethods, optional
        :param phone_number: Customer's primary phone number in E.164 format. The merchant is responsible for verifying that the number is correct. One method of verifying could be to send an activation code to the phone by SMS, with a limited time for response., defaults to None
        :type phone_number: str, optional
        :param subscriptions: subscriptions, defaults to None
        :type subscriptions: List[Subscription], optional
        """
        self.addresses = self._define_list(addresses, Address)
        self.business_vat_id = self._define_str(
            "business_vat_id", business_vat_id, nullable=True
        )
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.default_payment_method = self._define_str(
            "default_payment_method", default_payment_method, nullable=True
        )
        self.delinquent = delinquent
        self.description = self._define_str("description", description, nullable=True)
        self.discount = self._define_object(discount, Discount)
        self.email = self._define_str("email", email, nullable=True)
        self.ewallet = self._define_str("ewallet", ewallet, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.invoice_prefix = self._define_str(
            "invoice_prefix", invoice_prefix, nullable=True
        )
        self.metadata = metadata
        self.name = name
        self.payment_methods = self._define_object(
            payment_methods, CustomerPaymentMethods
        )
        self.phone_number = self._define_str(
            "phone_number", phone_number, nullable=True
        )
        self.subscriptions = self._define_list(subscriptions, Subscription)
