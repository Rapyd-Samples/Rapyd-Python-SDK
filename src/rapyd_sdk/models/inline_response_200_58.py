from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .plan import Plan
from .status import Status


@JsonMap({})
class InlineResponse200_58(BaseModel):
    """InlineResponse200_58

    :param data: data, defaults to None
    :type data: List[Plan], optional
    :param status: status, defaults to None
    :type status: Status, optional
    """

    def __init__(self, data: List[Plan] = None, status: Status = None):
        """InlineResponse200_58

        :param data: data, defaults to None
        :type data: List[Plan], optional
        :param status: status, defaults to None
        :type status: Status, optional
        """
        self.data = self._define_list(data, Plan)
        self.status = self._define_object(status, Status)
