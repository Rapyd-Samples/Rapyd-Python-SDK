from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Coupon import Coupon


@JsonMap({})
class CustomerDiscount(BaseModel):
    def __init__(
        self,
        coupon: Coupon = None,
        customer: str = None,
        end: float = None,
        id: str = None,
        number_of_uses: float = None,
        start: float = None,
        subscription: str = None,
        valid: bool = None,
    ):
        self.coupon = self._define_object(coupon, Coupon)
        self.customer = customer
        self.end = end
        self.id = id
        self.number_of_uses = number_of_uses
        self.start = start
        self.subscription = subscription
        self.valid = valid
