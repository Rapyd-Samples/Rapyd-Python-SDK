from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .order_response import OrderResponse
from .status import Status


@JsonMap({})
class InlineResponse200_48(BaseModel):
    """InlineResponse200_48

    :param data: data, defaults to None
    :type data: OrderResponse, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: OrderResponse = None, status: Status = None):
        """InlineResponse200_48

        :param data: data, defaults to None
        :type data: OrderResponse, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, OrderResponse)
        self.status = self._define_object(status, Status)
