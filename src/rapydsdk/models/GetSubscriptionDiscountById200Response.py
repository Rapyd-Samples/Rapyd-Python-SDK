from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .SubscriptionDiscount import SubscriptionDiscount
from .Status import Status


@JsonMap({})
class GetSubscriptionDiscountById200Response(BaseModel):
    def __init__(self, data: SubscriptionDiscount = None, status: Status = None):
        self.data = self._define_object(data, SubscriptionDiscount)
        self.status = self._define_object(status, Status)
