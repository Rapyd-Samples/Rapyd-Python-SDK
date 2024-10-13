from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .payment import Payment
from .order_item_response import OrderItemResponse
from .order_returned_item_response import OrderReturnedItemResponse
from .order_response_status_transitions import OrderResponseStatusTransitions


@JsonMap({"id_": "id"})
class OrderResponse(BaseModel):
    """OrderResponse

    :param id_: id_, defaults to None
    :type id_: str, optional
    :param amount: amount, defaults to None
    :type amount: float, optional
    :param amount_returned: amount_returned, defaults to None
    :type amount_returned: float, optional
    :param payment: Collects money from a payment method and deposits it into one or more Rapyd Wallets, defaults to None
    :type payment: Payment, optional
    :param created: created, defaults to None
    :type created: int, optional
    :param customer: customer, defaults to None
    :type customer: str, optional
    :param currency: currency, defaults to None
    :type currency: str, optional
    :param email: email, defaults to None
    :type email: str, optional
    :param external_coupon_code: external_coupon_code, defaults to None
    :type external_coupon_code: str, optional
    :param items: items, defaults to None
    :type items: List[OrderItemResponse], optional
    :param metadata: metadata, defaults to None
    :type metadata: dict, optional
    :param returns: A list of the returns charged against this order., defaults to None
    :type returns: List[OrderReturnedItemResponse], optional
    :param shipping_address: shipping_address, defaults to None
    :type shipping_address: dict, optional
    :param status: status, defaults to None
    :type status: str, optional
    :param status_transitions: Indicates the last time in Unix time that the order transitioned to one of the following statuses. A zero value for a status indicates that the order has never transitioned to it., defaults to None
    :type status_transitions: OrderResponseStatusTransitions, optional
    :param updated: updated, defaults to None
    :type updated: int, optional
    :param upstream_id: upstream_id, defaults to None
    :type upstream_id: str, optional
    :param tax_percent: tax_percent, defaults to None
    :type tax_percent: float, optional
    """

    def __init__(
        self,
        id_: str = None,
        amount: float = None,
        amount_returned: float = None,
        payment: Payment = None,
        created: int = None,
        customer: str = None,
        currency: str = None,
        email: str = None,
        external_coupon_code: str = None,
        items: List[OrderItemResponse] = None,
        metadata: dict = None,
        returns: List[OrderReturnedItemResponse] = None,
        shipping_address: dict = None,
        status: str = None,
        status_transitions: OrderResponseStatusTransitions = None,
        updated: int = None,
        upstream_id: str = None,
        tax_percent: float = None,
    ):
        """OrderResponse

        :param id_: id_, defaults to None
        :type id_: str, optional
        :param amount: amount, defaults to None
        :type amount: float, optional
        :param amount_returned: amount_returned, defaults to None
        :type amount_returned: float, optional
        :param payment: Collects money from a payment method and deposits it into one or more Rapyd Wallets, defaults to None
        :type payment: Payment, optional
        :param created: created, defaults to None
        :type created: int, optional
        :param customer: customer, defaults to None
        :type customer: str, optional
        :param currency: currency, defaults to None
        :type currency: str, optional
        :param email: email, defaults to None
        :type email: str, optional
        :param external_coupon_code: external_coupon_code, defaults to None
        :type external_coupon_code: str, optional
        :param items: items, defaults to None
        :type items: List[OrderItemResponse], optional
        :param metadata: metadata, defaults to None
        :type metadata: dict, optional
        :param returns: A list of the returns charged against this order., defaults to None
        :type returns: List[OrderReturnedItemResponse], optional
        :param shipping_address: shipping_address, defaults to None
        :type shipping_address: dict, optional
        :param status: status, defaults to None
        :type status: str, optional
        :param status_transitions: Indicates the last time in Unix time that the order transitioned to one of the following statuses. A zero value for a status indicates that the order has never transitioned to it., defaults to None
        :type status_transitions: OrderResponseStatusTransitions, optional
        :param updated: updated, defaults to None
        :type updated: int, optional
        :param upstream_id: upstream_id, defaults to None
        :type upstream_id: str, optional
        :param tax_percent: tax_percent, defaults to None
        :type tax_percent: float, optional
        """
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.amount = self._define_number("amount", amount, nullable=True)
        self.amount_returned = self._define_number(
            "amount_returned", amount_returned, nullable=True
        )
        self.payment = self._define_object(payment, Payment)
        self.created = self._define_number("created", created, nullable=True)
        self.customer = self._define_str("customer", customer, nullable=True)
        self.currency = self._define_str("currency", currency, nullable=True)
        self.email = self._define_str("email", email, nullable=True)
        self.external_coupon_code = self._define_str(
            "external_coupon_code", external_coupon_code, nullable=True
        )
        self.items = self._define_list(items, OrderItemResponse)
        self.metadata = metadata
        self.returns = self._define_list(returns, OrderReturnedItemResponse)
        self.shipping_address = shipping_address
        self.status = self._define_str("status", status, nullable=True)
        self.status_transitions = self._define_object(
            status_transitions, OrderResponseStatusTransitions
        )
        self.updated = self._define_number("updated", updated, nullable=True)
        self.upstream_id = self._define_str("upstream_id", upstream_id, nullable=True)
        self.tax_percent = self._define_number(
            "tax_percent", tax_percent, nullable=True
        )
