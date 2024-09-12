from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .v1orders_items import V1ordersItems
from .address import Address


@JsonMap({})
class V1OrdersBody(BaseModel):
    """V1OrdersBody

    :param coupon: ID of a coupon that is applied against this order. String starting with coupon_. The duration field of the coupon must be set to repeating, and the duration_in_months and discount_duration_in_uses fields must be set to 1., defaults to None
    :type coupon: str, optional
    :param customer: ID of the customer. String starting with cus_.
    :type customer: str
    :param currency: Three-letter ISO 4217 code for the currency used in the objects in the 'items' list.
    :type currency: str
    :param email: Email address of the customer., defaults to None
    :type email: str, optional
    :param items: Array of line items.
    :type items: List[V1ordersItems]
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: dict, optional
    :param shipping_address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
    :type shipping_address: Address, optional
    :param tax_percent: Percentage of tax to charge. Decimal., defaults to None
    :type tax_percent: float, optional
    :param upstream_id: Merchant-defined ID for the order. If the merchant does not define an ID, Rapyd generates it., defaults to None
    :type upstream_id: str, optional
    """

    def __init__(
        self,
        customer: str,
        currency: str,
        items: List[V1ordersItems],
        coupon: str = None,
        email: str = None,
        metadata: dict = None,
        shipping_address: Address = None,
        tax_percent: float = None,
        upstream_id: str = None,
    ):
        """V1OrdersBody

        :param coupon: ID of a coupon that is applied against this order. String starting with coupon_. The duration field of the coupon must be set to repeating, and the duration_in_months and discount_duration_in_uses fields must be set to 1., defaults to None
        :type coupon: str, optional
        :param customer: ID of the customer. String starting with cus_.
        :type customer: str
        :param currency: Three-letter ISO 4217 code for the currency used in the objects in the 'items' list.
        :type currency: str
        :param email: Email address of the customer., defaults to None
        :type email: str, optional
        :param items: Array of line items.
        :type items: List[V1ordersItems]
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: dict, optional
        :param shipping_address: address associated with this specific Rapyd entity Payment/Customer etc..., defaults to None
        :type shipping_address: Address, optional
        :param tax_percent: Percentage of tax to charge. Decimal., defaults to None
        :type tax_percent: float, optional
        :param upstream_id: Merchant-defined ID for the order. If the merchant does not define an ID, Rapyd generates it., defaults to None
        :type upstream_id: str, optional
        """
        self.coupon = self._define_str("coupon", coupon, nullable=True)
        self.customer = customer
        self.currency = currency
        self.email = self._define_str("email", email, nullable=True)
        self.items = self._define_list(items, V1ordersItems)
        self.metadata = metadata
        self.shipping_address = self._define_object(shipping_address, Address)
        self.tax_percent = self._define_number(
            "tax_percent", tax_percent, nullable=True
        )
        self.upstream_id = self._define_str("upstream_id", upstream_id, nullable=True)
