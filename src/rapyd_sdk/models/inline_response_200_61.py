from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .product import Product
from .status import Status


@JsonMap({})
class InlineResponse200_61(BaseModel):
    """InlineResponse200_61

    :param data: data, defaults to None
    :type data: List[Product], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[Product] = None, status: Status = None):
        """InlineResponse200_61

        :param data: data, defaults to None
        :type data: List[Product], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, Product)
        self.status = self._define_object(status, Status)
