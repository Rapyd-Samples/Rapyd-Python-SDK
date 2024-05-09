from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Plan import Plan


@JsonMap({})
class SubscriptionItem(BaseModel):
    def __init__(
        self,
        created: float,
        id: str,
        metadata: dict,
        plan: Plan,
        quantity: float,
        subscription_id: str = None,
    ):
        self.created = created
        self.id = id
        self.metadata = metadata
        self.plan = self._define_object(plan, Plan)
        self.quantity = quantity
        self.subscription_id = subscription_id
