from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .order_response import OrderResponse


@JsonMap({})
class InlineResponse200_55(BaseModel):
    """InlineResponse200_55

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: data, defaults to None
    :type data: OrderResponse, optional
    """

    def __init__(self, status: Status1 = None, data: OrderResponse = None):
        """InlineResponse200_55

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: data, defaults to None
        :type data: OrderResponse, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, OrderResponse)
