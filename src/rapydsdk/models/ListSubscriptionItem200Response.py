from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .SubscriptionItem import SubscriptionItem
from .Status import Status


@JsonMap({})
class ListSubscriptionItem200Response(BaseModel):
    def __init__(self, data: List[SubscriptionItem] = None, status: Status = None):
        self.data = self._define_list(data, SubscriptionItem)
        self.status = self._define_object(status, Status)
