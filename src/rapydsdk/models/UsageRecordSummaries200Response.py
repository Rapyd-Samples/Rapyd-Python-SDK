from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status


@JsonMap({})
class Data29(BaseModel):
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
class UsageRecordSummaries200Response(BaseModel):
    def __init__(self, data: List[Data29] = None, status: Status = None):
        self.data = self._define_list(data, Data29)
        self.status = self._define_object(status, Status)
