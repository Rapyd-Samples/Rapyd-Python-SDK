from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .plan import Plan


@JsonMap({})
class InlineResponse200_69(BaseModel):
    """InlineResponse200_69

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: data, defaults to None
    :type data: List[Plan], optional
    """

    def __init__(self, status: Status1 = None, data: List[Plan] = None):
        """InlineResponse200_69

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: data, defaults to None
        :type data: List[Plan], optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_list(data, Plan)
