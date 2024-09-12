from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .refund import Refund
from .status import Status


@JsonMap({})
class InlineResponse200_63(BaseModel):
    """InlineResponse200_63

    :param data: data, defaults to None
    :type data: List[Refund], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[Refund] = None, status: Status = None):
        """InlineResponse200_63

        :param data: data, defaults to None
        :type data: List[Refund], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, Refund)
        self.status = self._define_object(status, Status)
