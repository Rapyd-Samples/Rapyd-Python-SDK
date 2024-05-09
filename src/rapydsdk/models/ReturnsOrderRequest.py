from enum import Enum
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel


class Type4(Enum):
    SKU = "sku"
    SHIPPING = "shipping"
    TAX = "tax"

    def list():
        return list(map(lambda x: x.value, Type4._member_map_.values()))


@JsonMap({"type_": "type"})
class Items1(BaseModel):
    def __init__(
        self,
        description: str = None,
        parent: str = None,
        type_: Type4 = None,
        quantity: float = None,
        currency: str = None,
        amount: float = None,
        order_id: str = None,
    ):
        self.description = description
        self.parent = parent
        self.type_ = (
            self._enum_matching(type_, Type4.list(), "type_") if type_ else None
        )
        self.quantity = quantity
        self.currency = currency
        self.amount = amount
        self.order_id = order_id


@JsonMap({})
class ReturnsOrderRequest(BaseModel):
    def __init__(self, items: List[Items1], order_id: str = None):
        self.order_id = order_id
        self.items = self._define_list(items, Items1)
