from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status import Status
from .order_response import OrderResponse


@JsonMap({})
class InlineResponse200_47(BaseModel):
    """InlineResponse200_47

    :param status: status, defaults to None
    :type status: Status, optional
    :param data: data, defaults to None
    :type data: OrderResponse, optional
    """

    def __init__(self, status: Status = None, data: OrderResponse = None):
        """InlineResponse200_47

        :param status: status, defaults to None
        :type status: Status, optional
        :param data: data, defaults to None
        :type data: OrderResponse, optional
        """
        self.status = self._define_object(status, Status)
        self.data = self._define_object(data, OrderResponse)
