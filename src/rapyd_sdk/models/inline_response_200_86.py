from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .inline_response_200_86_data import InlineResponse200_86Data
from .status_1 import Status1


@JsonMap({})
class InlineResponse200_86(BaseModel):
    """InlineResponse200_86

    :param data: data, defaults to None
    :type data: List[InlineResponse200_86Data], optional
    :param status: status, defaults to None
    :type status: Status1, optional
    """

    def __init__(
        self, data: List[InlineResponse200_86Data] = None, status: Status1 = None
    ):
        """InlineResponse200_86

        :param data: data, defaults to None
        :type data: List[InlineResponse200_86Data], optional
        :param status: status, defaults to None
        :type status: Status1, optional
        """
        self.data = self._define_list(data, InlineResponse200_86Data)
        self.status = self._define_object(status, Status1)
