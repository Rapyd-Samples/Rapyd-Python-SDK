from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .v1ordersorder_idreturns_items import V1ordersorderIdreturnsItems


@JsonMap({})
class OrderIdReturnsBody(BaseModel):
    """OrderIdReturnsBody

    :param order_id: order_id, defaults to None
    :type order_id: str, optional
    :param items: items
    :type items: List[V1ordersorderIdreturnsItems]
    """

    def __init__(self, items: List[V1ordersorderIdreturnsItems], order_id: str = None):
        """OrderIdReturnsBody

        :param order_id: order_id, defaults to None
        :type order_id: str, optional
        :param items: items
        :type items: List[V1ordersorderIdreturnsItems]
        """
        self.order_id = self._define_str("order_id", order_id, nullable=True)
        self.items = self._define_list(items, V1ordersorderIdreturnsItems)
