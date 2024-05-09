from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status
from .Coupon import Coupon


@JsonMap({})
class RetrieveCoupon200Response(BaseModel):
    def __init__(self, status: Status = None, data: Coupon = None):
        self.status = self._define_object(status, Status)
        self.data = self._define_object(data, Coupon)
