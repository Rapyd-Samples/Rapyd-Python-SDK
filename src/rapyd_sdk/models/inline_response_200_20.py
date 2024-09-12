from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .status import Status
from .ewallet import Ewallet


@JsonMap({})
class InlineResponse200_20(BaseModel):
    """InlineResponse200_20

    :param status: status, defaults to None
    :type status: Status, optional
    :param data: data, defaults to None
    :type data: List[Ewallet], optional
    """

    def __init__(self, status: Status = None, data: List[Ewallet] = None):
        """InlineResponse200_20

        :param status: status, defaults to None
        :type status: Status, optional
        :param data: data, defaults to None
        :type data: List[Ewallet], optional
        """
        self.status = self._define_object(status, Status)
        self.data = self._define_list(data, Ewallet)
