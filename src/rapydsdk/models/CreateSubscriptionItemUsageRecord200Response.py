from __future__ import annotations
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class Data30(BaseModel):
    def __init__(
        self,
        id: str = None,
        quantity: float = None,
        subscription_item: str = None,
        timestamp: str = None,
    ):
        self.id = id
        self.quantity = quantity
        self.subscription_item = subscription_item
        self.timestamp = timestamp


@JsonMap({})
class CreateSubscriptionItemUsageRecord200Response(BaseModel):
    def __init__(self, data: Data30 = None, status: Status = None):
        self.data = self._define_object(data, Data30)
        self.status = self._define_object(status, Status)
