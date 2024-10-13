from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .refund import Refund


@JsonMap({})
class InlineResponse200_75(BaseModel):
    """InlineResponse200_75

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: data, defaults to None
    :type data: Refund, optional
    """

    def __init__(self, status: Status1 = None, data: Refund = None):
        """InlineResponse200_75

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: data, defaults to None
        :type data: Refund, optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_object(data, Refund)
