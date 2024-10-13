from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status_1 import Status1
from .inline_response_200_87_data import InlineResponse200_87Data


@JsonMap({})
class InlineResponse200_87(BaseModel):
    """InlineResponse200_87

    :param status: status, defaults to None
    :type status: Status1, optional
    :param data: data, defaults to None
    :type data: List[InlineResponse200_87Data], optional
    """

    def __init__(
        self, status: Status1 = None, data: List[InlineResponse200_87Data] = None
    ):
        """InlineResponse200_87

        :param status: status, defaults to None
        :type status: Status1, optional
        :param data: data, defaults to None
        :type data: List[InlineResponse200_87Data], optional
        """
        self.status = self._define_object(status, Status1)
        self.data = self._define_list(data, InlineResponse200_87Data)
