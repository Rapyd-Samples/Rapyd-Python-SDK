from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Subscription import Subscription
from .Status import Status


@JsonMap({})
class UpdateSubscription200Response(BaseModel):
    def __init__(self, data: Subscription = None, status: Status = None):
        self.data = self._define_object(data, Subscription)
        self.status = self._define_object(status, Status)
