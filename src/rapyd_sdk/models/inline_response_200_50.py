from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status import Status
from .order_returned_response import OrderReturnedResponse


@JsonMap({})
class InlineResponse200_50(BaseModel):
    """InlineResponse200_50

    :param status: status, defaults to None
    :type status: Status, optional
    :param data: data, defaults to None
    :type data: List[OrderReturnedResponse], optional
    """

    def __init__(self, status: Status = None, data: List[OrderReturnedResponse] = None):
        """InlineResponse200_50

        :param status: status, defaults to None
        :type status: Status, optional
        :param data: data, defaults to None
        :type data: List[OrderReturnedResponse], optional
        """
        self.status = self._define_object(status, Status)
        self.data = self._define_list(data, OrderReturnedResponse)
