from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Coupon import Coupon
from .Status import Status


@JsonMap({})
class CreateCoupon200Response(BaseModel):
    def __init__(self, data: Coupon = None, status: Status = None):
        self.data = self._define_object(data, Coupon)
        self.status = self._define_object(status, Status)
