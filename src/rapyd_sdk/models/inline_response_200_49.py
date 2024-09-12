from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .order_returned_response import OrderReturnedResponse
from .status import Status


@JsonMap({})
class InlineResponse200_49(BaseModel):
    """InlineResponse200_49

    :param data: data, defaults to None
    :type data: OrderReturnedResponse, optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: OrderReturnedResponse = None, status: Status = None):
        """InlineResponse200_49

        :param data: data, defaults to None
        :type data: OrderReturnedResponse, optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_object(data, OrderReturnedResponse)
        self.status = self._define_object(status, Status)
