from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .SubscriptionItem import SubscriptionItem


@JsonMap({})
class SubscriptionItems(BaseModel):
    def __init__(
        self,
        data: List[SubscriptionItem] = None,
        has_more: bool = None,
        total_count: float = None,
        url: str = None,
    ):
        self.data = self._define_list(data, SubscriptionItem)
        self.has_more = has_more
        self.total_count = total_count
        self.url = url
