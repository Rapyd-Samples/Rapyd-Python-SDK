from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .order_returned_response import OrderReturnedResponse


@JsonMap({})
class InlineResponse200_56(BaseModel):
    """InlineResponse200_56

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: data, defaults to None
    :type data: OrderReturnedResponse, optional
    """

    def __init__(self, status: Status1 = None, data: OrderReturnedResponse = None):
        """InlineResponse200_56

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: data, defaults to None
        :type data: OrderReturnedResponse, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, OrderReturnedResponse)
