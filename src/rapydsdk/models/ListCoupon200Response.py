from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Coupon import Coupon
from .Status import Status


@JsonMap({})
class ListCoupon200Response(BaseModel):
    def __init__(self, data: List[Coupon] = None, status: Status = None):
        self.data = self._define_list(data, Coupon)
        self.status = self._define_object(status, Status)
