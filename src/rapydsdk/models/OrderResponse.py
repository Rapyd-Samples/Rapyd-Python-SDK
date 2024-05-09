from __future__ import annotations
from typing import List
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .OrderItemResponse import OrderItemResponse
from .OrderReturnedItemResponse import OrderReturnedItemResponse
from .Payment import Payment


class Payment1Guard(OneOfBaseModel):
    class_list = {"str": str, "Payment": Payment}


Payment1 = Union[str, Payment]


@JsonMap({})
class StatusTransitions(BaseModel):
    def __init__(
        self,
        canceled: float = None,
        fulfilled: float = None,
        paid: float = None,
        returned: float = None,
        pending: float = None,
        partial: float = None,
    ):
        self.canceled = canceled
        self.fulfilled = fulfilled
        self.paid = paid
        self.returned = returned
        self.pending = pending
        self.partial = partial


@JsonMap({})
class OrderResponse(BaseModel):
    def __init__(
        self,
        id: str = None,
        amount: float = None,
        amount_returned: float = None,
        payment: Payment1 = None,
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
        status_transitions: StatusTransitions = None,
        updated: int = None,
        upstream_id: str = None,
        tax_percent: float = None,
    ):
        self.id = id
        self.amount = amount
        self.amount_returned = amount_returned
        self.payment = Payment1Guard.return_one_of(payment)
        self.created = created
        self.customer = customer
        self.currency = currency
        self.email = email
        self.external_coupon_code = external_coupon_code
        self.items = self._define_list(items, OrderItemResponse)
        self.metadata = metadata
        self.returns = self._define_list(returns, OrderReturnedItemResponse)
        self.shipping_address = shipping_address
        self.status = status
        self.status_transitions = self._define_object(
            status_transitions, StatusTransitions
        )
        self.updated = updated
        self.upstream_id = upstream_id
        self.tax_percent = tax_percent
